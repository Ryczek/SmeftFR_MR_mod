# Changelog

All notable changes to **SmeftFR** are documented in this file.

The format is intentionally simple and focused on public releases of the package.

---

## [3.03] - April 2026 (Current version)

- Typo in  \((\alpha_{\mathrm{em}}, M_Z, M_W, M_H)\) input scheme has been corrected. 
- A workaround for clashes of definitions of **Commutator and MatrixSymbol**  between FeynRules package and Mathematica versionis 14.3 or later


## [3.0] - 2024

### Added
- Complete support for the **bosonic dimension-8 SMEFT operator set**
- Consistent EFT expansion up to **dimension 8**, including
  - linear dimension-6 contributions,
  - quadratic dimension-6 contributions,
  - linear bosonic dimension-8 contributions
- Direct output of Feynman rules in terms of **user-defined input parameters**
- Predefined electroweak input schemes:
  - \((G_F, M_Z, M_W, M_H)\)
  - \((\alpha_{\mathrm{em}}, M_Z, M_W, M_H)\)
- Predefined CKM input scheme support
- **WCxf** interface for Wilson-coefficient input/output
- Dedicated **LaTeX** generator for human-readable analytic expressions

### Improved
- Dynamic generation of reduced FeynRules model files for user-selected operator subsets
- Export workflow for supported formats, including **UFO** and **FeynArts**
- Performance relative to v2, with approximately **order-of-magnitude speedup** for comparable dimension-6 calculations at \(1/\Lambda^2\) accuracy
- Support for calculations directly in terms of chosen observable input schemes, avoiding later manual reparametrization

### Preserved / extended
- Full **dimension-6 SMEFT** support in the Warsaw basis
- Support for **unitary gauge** and **linear \(R_\xi\)** gauges
- Generation of the corresponding **Goldstone** and **ghost** interactions in \(R_\xi\) gauge
- Support for neutrinos as massless Weyl fermions or, when the dimension-5 Weinberg operator is included, as massive Majorana fermions

---

## [2.0] - 2020

### Expanded
- Publicly documented and extended release of **SmeftFR**
- Broader options and user capabilities compared with the initial version

### Included
- Dimension-6 SMEFT workflow based on the Warsaw basis
- Generation of Feynman rules in the **mass basis**
- Support for **linear \(R_\xi\)** gauges
- Corresponding **ghost** and **Goldstone** sectors
- Export support through **FeynRules**

---

## [1.0] - initial public version

### Introduced
- Initial public version of **SmeftFR**
- First implementation of the package for deriving SMEFT Feynman rules
- Initial version announced in the earlier foundational work of the project

---

## Notes

For full technical details, see the package manual and the associated publications cited in `README.md`.
