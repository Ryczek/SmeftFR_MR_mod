# AGENTS.md

## Purpose of this repository

This repository contains **SmeftFR**, a **Mathematica / FeynRules** package for deriving **Feynman rules for the Standard Model Effective Field Theory (SMEFT)** directly in the **physical (mass-eigenstate) basis**.

SmeftFR 3.0 supports

- the complete set of **dimension-6 SMEFT operators**,
- the complete set of **bosonic dimension-8 operators**,
- consistent EFT expansion up to dimension 8, including
  - linear dimension-6 terms,
  - quadratic dimension-6 terms,
  - linear bosonic dimension-8 terms.

The package works as an overlay to **FeynRules** and is distributed under the **GPLv3** license. :contentReference[oaicite:0]{index=0}

---

## Authors and maintainer

Authors:

- A. Dedes
- J. Rosiek
- M. Ryczkowski
- K. Suxho
- L. Trifyllis

Program maintainer:

- **Janusz Rosiek**
- `janusz.rosiek@fuw.edu.pl` :contentReference[oaicite:1]{index=1}

---

## General principles

This is a **physics-convention-heavy Mathematica codebase**.  
When working in this repository, always prioritize:

1. **physics correctness**
2. **consistency of conventions**
3. **minimal, transparent edits**
4. **reproducibility**
5. **compatibility with the existing SmeftFR workflow**

Do **not** perform broad refactors, mass renamings, automatic cleanup, or stylistic rewrites unless explicitly requested.

Do **not** assume this repository follows standard Python, C++, or generic software-project conventions.  
The package is organized around **Mathematica notebooks/scripts**, **FeynRules model files**, **symbolic expressions**, and **export interfaces**.

---

## Scientific scope

SmeftFR is intended for symbolic and phenomenological SMEFT calculations requiring a systematic derivation of interaction vertices after electroweak symmetry breaking.

Main supported capabilities include:

- complete **dimension-6 SMEFT** implementation in the Warsaw basis
- complete **bosonic dimension-8** implementation in version 3.0
- generation of Feynman rules directly in the **mass basis**
- support for **unitary gauge** and **linear \(R_\xi\)** gauges
- generation of **Goldstone** and **ghost** sectors in \(R_\xi\) gauge
- support for **user-defined input-parameter schemes**
- predefined electroweak schemes such as
  - \((G_F, M_Z, M_W, M_H)\)
  - \((\alpha_{\mathrm{em}}, M_Z, M_W, M_H)\)
- export to **UFO**, **FeynArts**, **LaTeX**, and **WCxf** formats. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

---

## Repository structure

The package distribution is expected to contain at least the following important files and directories:

- `SmeftFR-init.nb`
- `smeft_fr_init.m`
- `SmeftFR-interfaces.nb`
- `smeft_fr_interfaces.m`
- `SmeftFR_v3.pdf`
- `README.txt`
- `README.md`
- `CITATION.cff`
- `LICENSE`
- `CHANGELOG.md`
- `AGENTS.md`
- `code/`
- `lagrangian/`
- `definitions/`
- `output/` :contentReference[oaicite:4]{index=4}

Directory roles in the distributed package:

- `code/` contains package code and utilities
- `lagrangian/` contains the SM Lagrangian and dimension-5, 6 and 8 operators in FeynRules format
- `definitions/` contains templates of SMEFT model files and example WCxf numerical input
- `output/` contains dynamically generated parameter files and exported output. :contentReference[oaicite:5]{index=5}

Do not rename or move these files casually.  
The names are part of the expected user workflow.

---

## Installation and execution model

SmeftFR is not a standalone package. It is designed to run inside a **FeynRules** installation.

Expected installation pattern:

1. create `Models/SMEFT_3_03` inside the main FeynRules directory,
2. unpack the SmeftFR distribution there,
3. edit `$FeynRulesPath` in:
   - `SmeftFR-init.nb`
   - `SmeftFR-interfaces.nb`
4. run `SmeftFR-init.nb` first,
5. quit the Mathematica kernel,
6. run `SmeftFR-interfaces.nb` in a new kernel.

Equivalent text-script workflow:

<< smeft_fr_init.m
<< smeft_fr_interfaces.m

Agents should preserve this two-stage workflow unless explicitly instructed to redesign it. 

---

## Core files and their roles

### `SmeftFR-init.nb` / `smeft_fr_init.m`

These generate:

* the SMEFT Lagrangian in the mass basis
* Feynman rules in Mathematica format. 

### `SmeftFR-interfaces.nb` / `smeft_fr_interfaces.m`

These perform exports to supported external formats, including:

* WCxf
* LaTeX
* UFO
* FeynArts. 

### `SmeftFR_v3.pdf`

This is the main package manual and the authoritative reference for conventions, algorithms, options, and supported features. 

When uncertain about conventions or scope, consult the manual before changing code.

---

## High-risk areas

Use extra caution when editing any code related to:

* field normalisation
* bilinear terms
* canonical normalisation
* mass diagonalisation
* gauge fixing
* ghost sectors
* Goldstone sectors
* EFT truncation logic
* Wilson-coefficient definitions
* flavour rotations
* CKM / PMNS handling
* neutrino conventions
* input-parameter schemes
* dynamic model generation
* export layers
* WCxf input/output

Small symbolic edits in these areas can change physical predictions.

---

## What must be preserved

Unless explicitly instructed otherwise, all changes must preserve:

* generation of Feynman rules in the **physical basis**
* full **dimension-6** support
* **bosonic dimension-8** support in version 3.0
* correct EFT truncation through the implemented order
* support for **quadratic dimension-6** terms
* support for **linear dimension-8** bosonic terms
* support for **unitary gauge**
* support for **linear (R_\xi)** gauges
* correct generation of **ghost** and **Goldstone** interactions
* compatibility with **FeynRules**
* compatibility of the package with its established two-stage execution model
* export support for **UFO**, **FeynArts**, **LaTeX**, and **WCxf**
* existing user-facing file names and workflow expectations.  

---

## Mathematica and FeynRules assumptions

Assume the package is intended to run with:

* **Mathematica 12.1 or later**
* **FeynRules 2.3** or a compatible recent version.

Earlier Mathematica versions were reported to have problems running the code. 

Do not introduce syntax or workflows that obviously require a much newer Mathematica version unless explicitly requested.

---

## Input schemes

SmeftFR supports both:

* the default SMEFT parameterisation
* direct output in terms of a **user-defined set of input observables**.

Predefined schemes include:

* ((G_F, M_Z, M_W, M_H))
* ((\alpha_{\mathrm{em}}, M_Z, M_W, M_H)). 

When editing input-scheme logic:

* preserve EFT-order consistency,
* preserve the mapping to the default SMEFT parameters,
* avoid hidden assumptions about which parameters are fundamental,
* do not remove user extensibility.

---

## Neutrino conventions

SmeftFR can treat neutrinos as either:

* massless Weyl fermions, or
* massive Majorana fermions when the dimension-5 Weinberg operator is included. 

Do not change neutrino-related code casually.
Majorana support affects vertices, propagators, and combinatorics.

---

## Gauge handling

SmeftFR supports:

* **unitary gauge**
* **linear (R_\xi)** gauges.

In (R_\xi) gauge, the ghost and Goldstone sectors are part of the supported physics content and must remain consistent with gauge-fixing conventions. 

Do not edit gauge-related logic without checking:

* gauge-parameter handling
* ghost interactions
* Goldstone interactions
* consistency in the mass basis
* downstream export behaviour

---

## EFT truncation rules

Version 3.0 performs consistent calculations up to dimension 8 in the EFT expansion, including:

* linear dimension-6 terms
* quadratic dimension-6 terms
* linear bosonic dimension-8 terms,

while higher-order terms are truncated. 

Do not “simplify” symbolic expressions in a way that may accidentally change the EFT order.

Preserve the existing truncation logic unless the task is explicitly about extending or modifying EFT-order handling.

---

## Dynamic model generation

SmeftFR dynamically generates reduced model files including only the selected subset of operators, which improves runtime and keeps the resulting output simpler. 

When touching this functionality:

* preserve the ability to work with selected operator subsets,
* do not force inclusion of the full operator basis by accident,
* avoid introducing unnecessary symbolic dependencies,
* preserve naming consistency between internal parameters and exported outputs.

---

## Exports

The package supports export through FeynRules and its own interfaces to formats such as:

* **UFO**
* **FeynArts**
* **LaTeX**
* **WCxf**. 

When editing export-related code:

* preserve established external names where possible,
* do not silently change output structure,
* avoid modifying file names or conventions unless explicitly requested,
* update examples or documentation when export behaviour changes.

---

## Performance considerations

The manual notes that runtime depends strongly on options and operator subsets, ranging from minutes to several hours for large exports. It also notes that v3 includes performance improvements relative to v2.  

When making edits:

* avoid unnecessary symbolic blow-up,
* preserve subset-based workflows,
* avoid broad changes that may degrade performance without a compelling reason.

---

## Testing guidance

After any meaningful code change, check as many of the following as possible:

1. the package loads without errors in Mathematica,
2. FeynRules integration still works,
3. `SmeftFR-init.nb` or `smeft_fr_init.m` still runs for a small known setup,
4. `SmeftFR-interfaces.nb` or `smeft_fr_interfaces.m` still exports at least one supported format,
5. a small operator subset still produces Feynman rules,
6. gauge-related options still behave sensibly,
7. no obvious EFT-order contamination has been introduced.

If benchmark notebooks or example scripts exist, use those first.

Prefer minimal reproducible tests over large full-model runs.

---

## Documentation expectations

If you change any of the following, update the relevant documentation:

* installation steps
* file names
* user-facing workflow
* supported output formats
* input schemes
* supported Mathematica/FeynRules versions
* default behaviour
* package scope

Relevant documentation may include:

* `README.md`
* `README.txt`
* `CHANGELOG.md`
* `SmeftFR_v3.pdf`
* comments inside notebooks/scripts

Do not silently change user-facing behaviour.

---

## Style guidance

When editing code:

* keep edits small and targeted,
* preserve existing naming conventions,
* preserve comments unless they are clearly incorrect,
* avoid unrelated reformatting,
* do not combine physics changes with style-only cleanup.

When editing documentation:

* be precise,
* avoid overselling,
* keep terminology consistent with the papers and manual,
* distinguish clearly between supported features and future possibilities.

---

## What not to do

Do not:

* rewrite the package into another language unless explicitly requested,
* convert symbolic expressions into hard-coded numerical approximations,
* remove terms that look redundant without understanding EFT bookkeeping,
* rename physics variables for style alone,
* alter conventions silently,
* alter author lists,
* alter citation information without explicit instruction,
* change the installation model casually,
* move core package files without a strong reason.

---

## If uncertain

If a requested change may affect conventions, normalization, truncation order, or supported workflows:

* identify the relevant files first,
* make the smallest possible change,
* document assumptions clearly,
* prefer preserving behaviour over speculative cleanup.

When in doubt, treat the package manual and the established SmeftFR workflow as authoritative.

---

## Short summary for agents

SmeftFR is a **Mathematica/FeynRules research package**, not a generic software repository.

Small symbolic edits can have large physics consequences.

Prefer:

* minimal changes,
* preserved conventions,
* preserved workflow,
* preserved output compatibility,
* and documented reasoning.


