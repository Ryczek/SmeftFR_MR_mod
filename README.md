# SmeftFR 3.0

**SmeftFR** is a **Mathematica / FeynRules** package for deriving **Feynman rules for the Standard Model Effective Field Theory (SMEFT)** directly in the **physical (mass-eigenstate) basis**.

Version 3.0 supports

- the complete set of **dimension-6 SMEFT operators**, and
- the complete set of **bosonic dimension-8 operators**,

with consistent EFT expansion up to dimension 8, including

- linear dimension-6 contributions,
- quadratic dimension-6 contributions,
- linear bosonic dimension-8 contributions.

SmeftFR can generate interaction vertices for the full model or for a user-selected subset of operators, in **unitary gauge** or in **linear \(R_\xi\) gauges**, and export the resulting Lagrangian and Feynman rules to formats supported by **FeynRules**, including **UFO**, **FeynArts**, **LaTeX**, and **WCxf**.

---

## Authors

A. Dedes, J. Rosiek, M. Ryczkowski, K. Suxho, L. Trifyllis

**Program maintainer:** janusz.rosiek@fuw.edu.pl

---

## License

SmeftFR is distributed under the **GPLv3** license.

---

## Main features

- Complete **dimension-6 SMEFT** implementation in the Warsaw basis
- Complete **bosonic dimension-8** implementation
- Feynman rules generated directly in the **mass basis**
- Consistent EFT expansion through **\(\mathcal{O}(1/\Lambda^4)\)**
- Support for **unitary gauge** and **linear \(R_\xi\)** gauges
- Generation of **Goldstone** and **ghost** vertices in \(R_\xi\) gauge
- Output in terms of either
  - the default SMEFT parameter set, or
  - a **user-defined input-parameter scheme**
- Predefined electroweak input schemes:
  - \((G_F, M_Z, M_W, M_H)\)
  - \((\alpha_{\mathrm{em}}, M_Z, M_W, M_H)\)
- Dynamic generation of reduced FeynRules model files for selected operator subsets
- Export to **UFO**, **FeynArts**, and other FeynRules-supported formats
- **WCxf** interface for Wilson-coefficient input/output
- Dedicated **LaTeX** generator for readable analytic expressions
- Support for neutrinos as
  - massless Weyl fermions, or
  - massive Majorana fermions when the dimension-5 Weinberg operator is included

---

## Scientific scope

SmeftFR is intended for symbolic and phenomenological SMEFT calculations where one needs a systematic derivation of interaction vertices after electroweak symmetry breaking.

Typical applications include:

- collider phenomenology in SMEFT
- model-file generation for Monte Carlo tools
- analytical calculations in the mass basis
- gauge-consistency checks in \(R_\xi\) gauges
- studies where bosonic dimension-8 effects are relevant, such as high-energy vector boson scattering

For dimension-6 fermionic operators, SmeftFR uses Wilson coefficients in the **Warsaw mass basis**, extended in version 3.0 by the implemented bosonic dimension-8 sector.

---

## Requirements

Running SmeftFR requires:

- **Wolfram Mathematica 12.1 or later**
- **FeynRules** installed and working correctly

SmeftFR has been tested with **Mathematica 12.1 or later** and with **FeynRules 2.3**. Earlier Mathematica versions were reported to have problems running the code.

Typical running times range from **a few minutes** for small operator subsets to **several hours** for large model exports, depending on the chosen options and output format.

---

## Installation

SmeftFR works as an overlay to **FeynRules**, so **FeynRules must be installed first**.

After installing FeynRules:

1. Create the subdirectory
   
   Models/SMEFT_3_03

inside the main FeynRules installation directory.

2. Unpack the SmeftFR distribution into

   Models/SMEFT_3_03

3. Edit the variable `$FeynRulesPath` at the top of the files

   * `SmeftFR-init.nb`
   * `SmeftFR-interfaces.nb`

   so that it is equal to the absolute path of the main FeynRules installation directory.

   Example:

   $FeynRulesPath = "/home/username/FeynRules"

4. Run `SmeftFR-init.nb` first to generate the SMEFT Lagrangian in mass basis and the Feynman rules in Mathematica format.

5. Quit the Mathematica kernel.

6. Run `SmeftFR-interfaces.nb` in a new kernel to export the output to other supported formats.

The same steps can also be performed using the text scripts:

<< smeft_fr_init.m
<< smeft_fr_interfaces.m

Further user-defined options are described in the manual.

---

## Typical workflow

A standard SmeftFR workflow is:

1. choose the operator subset,
2. choose the gauge,
3. choose the EFT expansion order,
4. choose the input-parameter scheme,
5. initialise the model,
6. generate the mass-basis Lagrangian and Feynman rules in Mathematica format,
7. restart the kernel,
8. export the result to the desired external format.

The initialization stage dynamically generates the relevant FeynRules model files, and the interface stage exports the already generated output to formats such as **WCxf**, **LaTeX**, **UFO**, and **FeynArts**.

---

## Input schemes

SmeftFR supports both the default SMEFT parameterisation and direct output in terms of a user-defined set of input observables.

### Predefined electroweak schemes

* ((G_F, M_Z, M_W, M_H))
* ((\alpha_{\mathrm{em}}, M_Z, M_W, M_H))

In both cases:

* the strong coupling is treated as an input,
* all quark and lepton masses are inputs,
* CKM input support is provided,
* the PMNS matrix is used as input without SMEFT corrections.

Users may also define their own input scheme by supplying the required relations to the default SMEFT parameters up to the requested EFT order.

---

## Gauge choice

SmeftFR supports:

* **unitary gauge**
* **linear (R_\xi) gauges**

In linear (R_\xi) gauges, the package also generates the corresponding **Goldstone** and **ghost** interactions. Independent gauge-fixing parameters can be used for detailed amplitude checks.

---

## Output formats

Feynman rules are generated first in **Mathematica / FeynRules** format and can then be exported to formats supported by FeynRules, including:

* **UFO**
* **FeynArts**

SmeftFR also provides:

* **LaTeX** output for human-readable analytic expressions
* **WCxf** input/output for Wilson coefficients

These outputs can be used in external tools such as Monte Carlo generators and symbolic amplitude frameworks.

---

## Package contents

The SmeftFR distribution contains the following main files and subdirectories:

* `SmeftFR-init.nb` (`smeft_fr_init.m`)
  notebook and equivalent text script generating the SMEFT Lagrangian in mass basis and Feynman rules in Mathematica format

* `SmeftFR-interfaces.nb` (`smeft_fr_interfaces.m`)
  notebook and equivalent text script with routines for exporting Feynman rules in various formats: WCxf, LaTeX, UFO and FeynArts

* `SmeftFR_v3.pdf`
  package manual in PDF format

* `README.txt`
  brief installation instructions

* `code/`
  package code and utilities

* `lagrangian/`
  expressions for the SM Lagrangian and dimension-5, 6 and 8 operators coded in FeynRules format

* `definitions/`
  templates of SMEFT model files and example numerical input for Wilson coefficients in WCxf format

* `output/`
  dynamically generated parameter files and output for Feynman rules in various formats; by default Mathematica, LaTeX, UFO and FeynArts are generated

---

## What is new in version 3.0

Compared with earlier versions, SmeftFR 3.0 adds:

* the complete **bosonic dimension-8** sector
* consistent EFT expansion to dimension 8
* support for **quadratic dimension-6** contributions
* direct output in terms of **user-defined input parameters**
* predefined input schemes including dimension-8 corrections
* substantial performance improvements over version 2 for comparable dimension-6 calculations

---

## Documentation

For full details on conventions, algorithms, operator content, options, input schemes, and example workflows, see:

* `SmeftFR_v3.pdf`
* `README.txt`

The latest version of SmeftFR can also be found at:

www.fuw.edu.pl/smeft

---

## Citation

If you use SmeftFR in scientific work, please cite the relevant publications.

### SmeftFR v3.0

A. Dedes, J. Rosiek, M. Ryczkowski, K. Suxho, L. Trifyllis,
"SmeftFR v3 – Feynman rules generator for the Standard Model Effective Field Theory",
Comput. Phys. Commun. 294 (2024) 108943,
doi:10.1016/j.cpc.2023.108943,
arXiv:2302.01353 [hep-ph]

### Earlier SmeftFR release

A. Dedes, M. Paraskevas, J. Rosiek, K. Suxho, L. Trifyllis,
"SmeftFR – Feynman rules generator for the Standard Model Effective Field Theory",
Comput. Phys. Commun. 247 (2020) 106931,
arXiv:1904.03204 [hep-ph]

### Gauge-fixing and foundational implementation

A. Dedes, W. Materkowska, M. Paraskevas, J. Rosiek, K. Suxho,
"Feynman rules for the Standard Model Effective Field Theory in Rξ-gauges",
JHEP 06 (2017) 143,
arXiv:1704.03888 [hep-ph]

---

## Repository status

SmeftFR is research software developed for high-energy-physics applications.

Bug reports and well-documented issues are welcome.

---


