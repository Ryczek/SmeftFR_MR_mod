# CLAUDE.md

Guidance for Claude Code when working in this repository (SmeftFR — a
Mathematica/FeynRules package for SMEFT Feynman rules in the mass basis).

## Read first

- `AGENTS.md` (repo root) — general principles, high-risk areas, what must
  be preserved. This is a physics-convention-heavy codebase: prioritize
  physics correctness, minimal edits, and convention consistency.

## Dimension-8 fermionic operators (IMPORTANT)

If asked to implement, extend, or verify **dim-8 fermionic SMEFT
operators** (basis of Murphy, arXiv:2005.00059), ALWAYS read
`MR_modifications/sfr404_july_13_MR/AGENTS_Dim8_Fermionic_Ops.md`
FIRST. It is the working log and single source of truth for:

- the per-operator file layout (`lagrangian/2XX_<class>/<opname>.fr`,
  on-demand loaders in `code/smeft_io.m`);
- all established code conventions: 8-suffixed field copies (`Phi8`,
  `LL8`, `Ta8`, `T8`, ...), Hermitian-derivative and Htilde idioms,
  dual field strengths, FlavorExpand recipes ({SU2D8} then {SU2W8}),
  Hermiticity / `+ h.c.` rules, Straub classes and rotation matrices;
- naming rules (paper name with `H -> phi`, superscript `(n) -> nN`,
  plus documented exceptions like class-16 `leWHD2n1`);
- the three files to update for every new operator:
  `lagrangian/2XX_.../<name>.fr`, `code/smeft_variables.m`
  (`SMEFT$Dim8TwoFermionOperators` + `SMEFT$TensorWC`), and the
  commented `OpList8` reference list in `smeft_fr_init.m`;
- the verification checklist (inventory == paper table == variable list
  == TensorWC rows == `LQ` symbols == WC strings; wolframscript parse
  and `LQ<name>` symbol check; pre-existing bodies kept byte-identical);
- a progress log of which classes are done (9-17 two-fermion complete
  as of 2026-07-14) and what remains (classes 18-21 four-fermion).

After finishing any operator work, append a dated progress-log entry and
any new conventions/decisions to that AGENTS_Dim8 file so the next
session stays fast.

## Active working copy

The active development tree for dim-8 fermionic work is
`MR_modifications/sfr404_july_13_MR/` (NOT the repo root, which holds
the published SmeftFR v3.0). The paper source with all operator tables
is in `MR_modifications/sfr404_july_13_MR/papers/arXiv-2005.00059v6/`.

## Verification tools

- `wolframscript` is available; use it to `Get` every new/edited `.fr`
  and `.m` file (syntax check) and to confirm each file defines its
  `LQ<name>` symbol.
- Full `SMEFTInitializeModel` / Feynman-rule runs are expensive — do not
  launch them unprompted; suggest a small `OpList8` subset instead.

## Instructions from the maintainer

- The methodology for adding operators is described in
  `MR_modifications/sfr404_july_13_MR/FermionicDim8Operators.tex`
  (authors' official instructions) — the AGENTS_Dim8 file extends it
  with everything learned during implementation.
