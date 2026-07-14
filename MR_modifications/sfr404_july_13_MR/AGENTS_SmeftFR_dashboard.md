# AGENTS_SmeftFR_dashboard.md — SmeftFR dashboard front end

This note documents the prototype Mathematica dashboard added for the
SmeftFR v4 workflow.  It is intended as a handover/reference document for
future AI-assisted work and for manual maintenance of the dashboard.

The dashboard currently consists of:

- `SmeftFR-dashboard.nb` — the Mathematica notebook front end.
- `code/smeft_dashboard_driver.m` — the dashboard implementation code.

---

## 1. What `SmeftFR-dashboard.nb` is

`SmeftFR-dashboard.nb` is a lightweight Mathematica notebook that loads the
dashboard driver and displays the interactive front end.

At present it does essentially two things:

```mathematica
Get[FileNameJoin[{NotebookDirectory[], "code", "smeft_dashboard_driver.m"}]];
SMEFTDashboard[]
```

The notebook itself intentionally contains very little logic.  This is by
design: the real implementation lives in a plain-text `.m` file so it can be
edited, diffed, and reviewed more easily than a notebook.

The displayed dashboard provides controls for:

- choosing the FeynRules installation path;
- choosing a WCXF input file;
- selecting the gauge, currently `Unitary` or `Rxi`;
- setting `ExpansionOrder`;
- setting `MaxParticles`;
- selecting `InputScheme`, `CKMInput`, and `PMNSInput`;
- selecting operators grouped by dimension/class;
- choosing which export stages to run:
  - Mathematica/FeynRules generation;
  - WCXF;
  - LaTeX;
  - FeynArts;
  - UFO;
- choosing whether UFO should use real-only flavour parameters.

The dashboard is not meant to replace the SmeftFR physics code.  It is a user
front end that prepares options and calls the existing SmeftFR routines.

---

## 2. What `code/smeft_dashboard_driver.m` does

`code/smeft_dashboard_driver.m` defines the functions used by the notebook.
The most important ones are:

```mathematica
SMEFTDashboard[]
SMEFTDashboardDefaultConfig[]
SMEFTDashboardOperatorGroups[]
SMEFTPrepareEnvironment[config]
SMEFTRunGeneration[config]
SMEFTRunInterfaces[config]
SMEFTRunUFO[config]
SMEFTRunGenerationExternal[config]
SMEFTRunInterfacesExternal[config]
SMEFTRunUFOExternal[config]
```

### Operator lists

The dashboard reads the operator lists from:

```text
code/smeft_variables.m
```

The current dashboard grouping uses, among others:

```mathematica
SMEFT$Dim6BosonicOperators
SMEFT$Dim6TwoFermionOperators
SMEFT$Dim6FourFermionOperators
SMEFT$Dim6FourFermionBLVOperators
SMEFT$Dim8BosonicOperators
SMEFT$Dim8TwoFermionOperators
SMEFT$Dim8FourFermionOperators
SMEFT$Dim8FourFermionBLVOperators
```

At the time of writing, dimension-5 operators such as `vv` are not included
in the dashboard menu because the dashboard does not yet include
`SMEFT$Dim5TwoFermionBLVOperators` in its groups.

### Environment loading

The dashboard infers the FeynRules path by searching upward from the model
directory for a directory containing:

```text
FeynRulesPackage.m
```

The expected local layout is:

```text
FeynRules/
  FeynRules.m
  FeynRulesPackage.m
  Interfaces/
  Models/
    SMEFT_4_03/
      SmeftFR-dashboard.nb
      code/
        smeft_dashboard_driver.m
```

The dashboard ultimately loads the standard FeynRules wrapper:

```mathematica
Get[FileNameJoin[{$FeynRulesPath, "FeynRules.m"}]]
```

and then loads:

```mathematica
code/smeft_package.m
```

### External kernel execution

The dashboard does not run the heavy FeynRules/SmeftFR operations inside the
notebook kernel.  Instead, the buttons launch fresh external `wolframscript`
kernels.

This was introduced because loading FeynRules directly in the notebook
front-end kernel proved fragile.  The command-line/external-kernel route is
closer to the original SmeftFR script workflow.

The external runners are:

```mathematica
SMEFTRunGenerationExternal[config]
SMEFTRunInterfacesExternal[config]
SMEFTRunUFOExternal[config]
```

They write logs to:

```text
output/dashboard_generation.log
output/dashboard_interfaces.log
output/dashboard_ufo.log
```

For live progress, use a terminal:

```bash
tail -f output/dashboard_generation.log
tail -f output/dashboard_interfaces.log
tail -f output/dashboard_ufo.log
```

The notebook currently waits for the external process to finish; it does not
stream progress live into the notebook.

### Generation stage

The generation stage calls the existing SmeftFR sequence:

```mathematica
SMEFTInitializeModel[...]
SMEFTLoadModel[]
SMEFTFindMassBasis[]
SMEFTFeynmanRules[]
SMEFTOutput[]
```

Successful generation writes:

```text
output/smeft_feynman_rules.m
output/smeft_par_MB.fr
output/smeft_par_MB_real.fr
output/smeft_par_MB_complex.fr
```

### Interface/export stage

The interface stage reloads the mass-basis output using:

```mathematica
SMEFTInitializeMB[...]
```

and then optionally runs:

```mathematica
SMEFTToWCXF[...]
SMEFTToLatex[...]
FeynRules`WriteFeynArtsOutput[...]
```

The FeynArts output base is:

```text
output/FeynArts/FeynArts
```

Because of how the FeynRules FeynArts interface works, this means the real
files are expected as:

```text
output/FeynArts/FeynArts.mod
output/FeynArts/FeynArts.gen
output/FeynArts/FeynArts.pars
```

The directory:

```text
output/FeynArts/FeynArts/
```

may be created by the FeynRules interface but can remain empty.  That is not
by itself an error.

### UFO stage

The UFO stage reloads the mass-basis model and calls:

```mathematica
SMEFTToUFO[...]
```

The dashboard exposes a checkbox labelled “UFO real parameters only”.

If checked, the dashboard sets:

```mathematica
"UFORealParameters" -> True
```

and uses:

```text
output/smeft_par_MB_real.fr
```

If unchecked, it uses:

```text
output/smeft_par_MB_complex.fr
```

The UFO log prints the selected mode and model file explicitly.

### BLV operator handling

The dashboard automatically detects selections from groups whose names contain
`BLV`.

If any BLV operator is selected, the dashboard passes:

```mathematica
"IncludeBL4Fermion" -> True
```

to generation/export configurations.  This is required for operators such as:

```mathematica
"duq", "qqu", "qqq", "duu", "duu3"
```

Without this option, BL-violating four-fermion vertices may be absent from
interface outputs.

---

## 3. How to install this in a SmeftFR package checkout

Assume a standard FeynRules/SmeftFR tree:

```text
/path/to/FeynRules/
  FeynRules.m
  FeynRulesPackage.m
  Models/
    SMEFT_4_03/
```

Install by copying:

```text
SmeftFR-dashboard.nb
code/smeft_dashboard_driver.m
```

into:

```text
/path/to/FeynRules/Models/SMEFT_4_03/
```

with the driver under the model’s `code/` subdirectory:

```text
/path/to/FeynRules/Models/SMEFT_4_03/code/smeft_dashboard_driver.m
```

Then open:

```text
SmeftFR-dashboard.nb
```

in Mathematica and evaluate the cells.

If the notebook cannot infer the FeynRules path automatically, enter it
manually in the dashboard path field.  For example:

```text
/home/sakis/Documents/PROJECTS/FeynRules
```

Do not enter the model directory as the FeynRules path.  The dashboard expects
the directory that contains `FeynRules.m` and `FeynRulesPackage.m`.

The system also requires that `wolframscript` is available from the shell path,
because heavy jobs are launched in external kernels.

Check with:

```bash
which wolframscript
```

---

## 4. What the dashboard currently does

The dashboard currently supports:

- reading implemented operator lists from `code/smeft_variables.m`;
- selecting operators by broad group;
- preserving operator selections across groups;
- automatic `IncludeBL4Fermion -> True` for selected BLV groups;
- selecting gauge, expansion order, `MaxParticles`, input scheme, CKM, PMNS;
- running SmeftFR generation in an external kernel;
- writing `output/smeft_feynman_rules.m`;
- running WCXF and LaTeX exports;
- running UFO export with either real-only or complex flavour parameters;
- running FeynArts export through the real FeynRules FeynArts interface;
- logging generation/export output to files under `output/`;
- warning for known problematic dual-field-strength operators before FeynArts
  export.

Tests performed during development included:

- dim-6 `{phiBox, eW}`;
- dim-6 `{eW, phiW, qq1, qq3}` in `Rxi` gauge;
- dim-8 `qdGWphin2` generation;
- BLV `qqq`, including successful appearance of `Cqqq` in
  `output/FeynArts/FeynArts.mod` when `IncludeBL4Fermion -> True`;
- UFO real-parameter mode selecting `output/smeft_par_MB_real.fr`.

---

## 5. What the dashboard does not yet do

The dashboard is still a prototype.  Current limitations include:

- It does not stream external-kernel progress live into the notebook.  Progress
  must be followed via log files, e.g.

  ```bash
  tail -f output/dashboard_generation.log
  ```

- It does not yet include dimension-5 operators such as `vv` in the operator
  menu.

- It does not validate every typed/free-form operator name.  Invalid names may
  be ignored by SmeftFR, depending on the underlying package behavior.

- It does not prevent users from requesting very expensive or impractical
  combinations.

- It does not solve the FeynArts interface bottleneck for CP-odd/dual
  field-strength operators.  In particular, operators such as `qdGWphin2` can
  generate Levi-Civita Lorentz structures that make FeynArts export extremely
  slow or effectively unusable.

- It does not yet provide a cancel/kill button for external jobs.

- It does not yet provide live status polling inside the notebook.

- It does not yet separate “generation configuration” from “export
  configuration” in a saved project/profile file.

- It does not yet provide robust cleanup of stale output files before every
  run.  Users should be aware that old files under `output/` may remain unless
  explicitly removed.

- It does not replace the original batch scripts:

  ```text
  smeft_fr_init.m
  smeft_fr_interfaces.m
  smeft_fr_ufo.m
  ```

  Those scripts remain useful references and fallback workflows.

---

## 6. Practical debugging notes

If generation appears silent in the notebook, inspect:

```bash
tail -f output/dashboard_generation.log
```

If UFO export appears silent:

```bash
tail -f output/dashboard_ufo.log
```

If WCXF/LaTeX/FeynArts export appears silent:

```bash
tail -f output/dashboard_interfaces.log
```

For FeynArts, check:

```bash
ls -lh output/FeynArts/FeynArts.*
```

For a BLV test such as `qqq`, check:

```bash
rg Cqqq output/smeft_feynman_rules.m
rg Cqqq output/FeynArts/FeynArts.mod
```

If `Cqqq` is present in `smeft_feynman_rules.m` but not in
`FeynArts.mod`, verify that the interface/export run used:

```mathematica
IncludeBL4Fermion -> True
```

---

## 7. Recommended next improvements

Useful next development steps:

1. Add dimension-5 operator groups, especially `vv`.
2. Add live log polling to the notebook UI.
3. Add a cancel button for external `wolframscript` jobs.
4. Add run profiles saved as JSON or `.m` associations.
5. Add stronger validation of selected operators against
   `SMEFT$AllOperators`.
6. Add explicit stale-output cleanup options.
7. Add a FeynArts risk estimator or hard warning for known slow structures,
   especially dual-field-strength operators with Levi-Civita tensors.
