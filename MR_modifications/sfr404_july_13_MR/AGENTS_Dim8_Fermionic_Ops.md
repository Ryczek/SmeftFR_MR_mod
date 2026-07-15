# AGENTS.md — SmeftFR v4 fermionic dimension-8 operators

This file tracks AI-assisted work on adding fermionic dimension-8 SMEFT
operators to the `SmeftFR` model (basis of Murphy, arXiv:2005.00059).
It is intended as a working log and quick reference for future sessions.

## How to add a new fermionic dim-8 operator (summary of `FermionicDim8Operators.tex`)

For an operator from class `XX` in 2005.00059, three places must be edited:

1. **`lagrangian/2XX_<class_name>.fr`** — define the Mathematica entry
   `LQ<name>` using standard FeynRules syntax, with the replacement
   `Phi -> Phi8` (speeds up mass-dimension expansions). Operator naming
   follows 2005.00059 with `H -> phi` and superscript `(n)` -> `nN`, e.g.
   `Q_{leG^2H}^{(1)} -> "leG2phin1"`, with Lagrangian symbol `LQleG2phin1`.

2. **`code/smeft_variables.m`**:
   - add the operator string to the relevant list near the top
     (here `SMEFT$Dim8TwoFermionOperators`);
   - add a row to `SMEFT$TensorWC`:
     `{"name", {rotations}, BLviolating?, StraubClass}`.
     - rotations `VXY`: `X in {L,U,D}` fermion type, `Y in {L,R}` chirality.
       For a left doublet `q_L` either `VUL` or `VDL` may be used (it only
       affects where the CKM matrix appears in the mass basis).
     - 3rd entry: `False` for all (non-BLV) 2-fermion dim-8 operators.
     - 4th entry: "Straub" symmetry class. Class `1` = no flavour symmetry
       imposed for 2-fermion operators (safe default).

3. **`smeft_fr_init.m`** (or `SmeftFR-init.nb`): add the operator name to
   `OpList8` to include it in an actual calculation. (Only the commented
   reference list near the top was updated here — the active `OpList8`
   used for runs is left for the user to choose, since full dim-8 runs are
   very expensive.)

## Conventions used (cross-checked against existing code)

- Reference dim-6 operators: `lagrangian/00_..11_*.fr` (arXiv:1704.03888).
- Reference dim-8 operators: other `2XX_*.fr` files.
- Lepton scalar bilinear `(lbar_p e_r) H`:
  `LLbar[sp,ii,ff1].lR[sp,ff2] Phi8[ii]`  (cf. `03_psi2phi3.fr`, `LQephi`).
- Up-quark scalar bilinear `(qbar_p u_r) Htilde`:
  `QLbar[sp,ii,ff1,cc].uR[sp,ff2,cc] Eps[ii,kk] HC[Phi8[kk]]`
  (cf. `LQuphi`). The conjugate Higgs is `Htilde_i = eps_ik H_k^*`.
- Down-quark scalar bilinear `(qbar_p d_r) H`:
  `QLbar[sp,ii,ff1,cc].dR[sp,ff2,cc] Phi8[ii]` (cf. `LQdphi`, `LQdG`,
  `LQdW`). **Important**: down-quark and lepton class-9 operators use the
  *plain* Higgs `H` (its doublet index is contracted with the left
  doublet, directly or through `tau^I`); only the up-quark operators use
  the conjugate `Htilde`. This mirrors the up/down asymmetry of the
  dim-6 dipole/Yukawa operators (`uphi/uG/uW` use `Htilde`, `dphi/dG/dW`
  use `H`).
- `tau^I` doublet insertion: `2 Ta[ll,ii,jj]` (cf. dim-6 `LQeW`, `LQuW`).
- Tensor bilinear `sigma^{mu nu}`: `Sigma[mu,nu,sp1,sp2]` with distinct
  spinor indices `sp1,sp2` (scalar bilinears reuse a single `sp`).
- Dual field strength `Xtilde_{mu nu} = (1/2) eps_{mu nu al be} X^{al be}`:
  `Eps[mu,nu,al,be]/2 HC[FS[X,al,be,..]]`  (cf. `04_X2phi2.fr`,
  `205_X3phi2.fr`, `201_X4.fr`).
- `W^{K rho}_nu` contraction (shared Lorentz index `ro`):
  `FS[Wi,mu,ro,bb] FS[Wi,nu,ro,cc]` (cf. `205_X3phi2.fr` cubic-W operators).
- SU(3) constants: symmetric `dSUN[A,B,C]`, antisymmetric `f[A,B,C]`,
  generator `T[A,m,n]` (cf. `201_X4.fr`, `219_psi4X.fr`).
- SU(2) `eps^{IJK}`: `Eps[I,J,K]` resolved under `FlavorExpand->{SU2W}`
  (cf. `205_W3phi2n1`, `W2Bphi2n1`).
- `FlavorExpand`: `{SU2D}` for operators without W; any operator with `W`
  and/or `tau^I` uses **two-step expansion**: `{SU2D}` first, then `{SU2W}`
  (cf. `LQl4Wn1` in `219_psi4X.fr`). Single-step
  `FlavorExpand->{SU2W,SU2D}` can hit `$RecursionLimit` during Lagrangian
  generation (seen for `leW2phin3`).
- SU(2) `eps^{IJK}`: `Eps[I,J,K]` resolved in the `{SU2W}` step.
- Every operator ends with `(aux + HC[aux]) /. SMEFTGaugeRules` because
  class-9 operators come with `+ h.c.`

## IMPORTANT: conventions added after the class-9 log below

- **8-suffixed field copies (July 2026 model)**: all dim-8 operator code in
  this model version now uses the dim-8-specific field copies:
  `LL8`, `LL8bar`, `lR8`, `lR8bar`, `QL8`, `QL8bar`, `uR8`, `uR8bar`, `dR8`,
  `dR8bar`, `Phi8`, `Phi8bar`, `FS[Gl8,..]`, `FS[Wi8,..]`, `FS[B8,..]`,
  `Ta8` (SU(2) generator), `T8` (SU(3) generator), and index names
  `SU2D8`, `SU2W8` in `FlavorExpand`. The class-9 conventions listed below
  (plain `LLbar`, `Ta`, `SU2D`, ...) are the *old* names — always add the
  `8` suffix in this model. Lorentz/spin objects (`Ga`, `Sigma`, `Eps`,
  `DC`, `HC`) and `Eps` for SU(2)/Lorentz indices are unchanged.
- **Per-operator file layout**: each dim-8 class lives in its own directory
  `lagrangian/2XX_<class_name>/` with one file `<opname>.fr` per operator
  (file name == operator name == WC name; Lagrangian symbol `LQ<opname>`).
  `code/smeft_io.m` loads them on demand via the
  `Scan[... Select[SMEFT$OperatorList, FileExistsQ[...]]]` block — adding a
  new operator requires *no* smeft_io.m change, just drop the file in the
  class directory and register the name in `smeft_variables.m`.
  Currently separated: `209_psi2X2phi`, `210_psi2Xphi3`, `211_psi2phi2D3`,
  `212_psi2phi5` (renamed from old `Dim8Class12`), `213_psi2phi4D`.
- **Hermitian conjugates (classes 10-13, Table 5 of 2005.00059)**:
  - Class 10 (psi^2 X H^3) and class 12 (psi^2 H^5): every operator has
    `+ h.c.` -> end with `(aux + HC[aux])`, Straub class `1`, rotations
    `le -> {VLL,VLR}`, `qu -> {VUL,VUR}`, `qd -> {VDL,VDR}`.
  - Classes 11 (psi^2 H^2 D^3) and 13 (psi^2 H^4 D): per the Table-5
    caption ONLY `udphi2D3` and `udphi4D` have Hermitian conjugates
    (`(aux + HC[aux])`, `{VUR,VDR}`, Straub class `1`). All other class
    11/13 operators are treated as Hermitian (following the authors'
    pre-existing `l2phi2D3n1`, `l2phi4Dn1` templates): plain `aux`, no HC,
    Straub class `2`, rotations `l2 -> {VLL,VLL}`, `e2 -> {VLR,VLR}`,
    `q2 -> {VDL,VDL}`, `u2 -> {VUR,VUR}`, `d2 -> {VDR,VDR}`
    (mirrors dim-6 `phil1`/`phie`/`phiq1`/`phiu`/`phid`/`phiud`).
- **Hermitian derivative** (eq. 2.9 of 2005.00059):
  `i H^dag <-> D_mu H` -> `I (Phi8bar[jj] DC[Phi8[jj],mu] - DC[Phi8bar[jj],mu] Phi8[jj])`;
  `i H^dag <-> D^I_mu H` -> `I 2 Ta8[ll,mm,nn] (Phi8bar[mm] DC[Phi8[nn],mu] - DC[Phi8bar[mm],mu] Phi8[nn])`
  (cf. dim-6 `LQphil1`, `LQphil3` in `06_psi2phi2D.fr`). No extra HC.
- **Symmetrized double derivative** `D_(mu D_nu)` (class 11):
  `(DC[DC[X,mu],nu] + DC[DC[X,nu],mu])` with the 1/2 absorbed into the
  overall `I/2` prefactor (cf. authors' `l2phi2D3n1`).
- **Htilde^dag** (`ud` operators): `Htilde^dag_j = eps_jk H_k` ->
  `Eps[jj,kk] Phi8[kk] ...` acting on `DC[...Phi8[jj]...]`
  (equivalently `HC[Phi8bar[kk]]`, cf. dim-6 `LQphiud`); for
  `Htilde^dag <-> D_mu H` both derivative placements are written out:
  `Eps[jj,kk] (Phi8[kk] DC[Phi8[jj],mu] - DC[Phi8[kk],mu] Phi8[jj])`.
- **FlavorExpand recipes used** (all verified to parse; follow the
  per-class template):
  - class 10: `tmp = (H^dag H)` expanded `{SU2D8}` separately; main
    expression single-step `{SU2W8,SU2D8}` if it contains `W`/`tau^I`,
    else `{SU2D8}` only. (`B`/`G`-only operators never need `SU2W8` here
    because they contain no covariant derivatives.)
  - class 11: fermion bilinear and Higgs bilinear expanded separately with
    `{SU2D8}` (doublets only), final combination expanded `{SU2W8}` —
    `SU2W8` is required even without explicit `W` because `DC[...]`
    contains W bosons.
  - class 13: all SU(2)-doublet pieces expanded `{SU2D8}` as separate
    `tmpN`, final combination `{SU2W8}` (or single-step `{SU2W8,SU2D8}`
    for the simple n1-type operators, following the authors' `l2phi4Dn1`).
  - shared adjoint dummies (`ll` / `aa,bb,cc` with `Eps[aa,bb,cc]`) across
    separately-expanded `tmpN` factors are fine — they contract in the
    final `{SU2W8}` step.

- **Fermionic Hermitian derivative** `(psibar ga^mu <-> D^nu psi)`
  (class 14; cf. authors' `l2G2D`):
  `(F8bar[..].DC[F8[..],nu] - DC[F8bar[..],nu].F8[..]) Ga[mu,sp1,sp2]`
  — note `DC` acts directly on the barred field. Insert `T8[aa,mm,nn]`
  (colour, distinct fundamental indices `mm,nn`) and/or `2 Ta8[ll,ii,jj]`
  (isospin, distinct doublet indices `ii,jj`) as needed. When a plain
  (non-`T8`) quark bilinear coexists with `f`/`dSUN`/`Eps[aa,bb,cc]`
  group symbols, name the fundamental colour index `co` to avoid
  clashing with the adjoint dummy `cc`.
- **Class-14 field-strength contractions**: `X_{mu ro} Y_nu^{ro}` ->
  `FS[X8,mu,ro,adj] FS[Y8,nu,ro,adj2]` (shared `ro`); dual
  `Xtilde_{a ro}` -> `Eps[a,ro,al,be]/2 HC[FS[X8,al,be,adj]]`.
  SU(3): antisymmetric `f[aa,bb,cc]`, symmetric `dSUN[aa,bb,cc]`,
  contracted with `T8[aa,mm,nn]` (cf. `201_X4.fr`, `219_psi4X.fr`).
- **Class-14 Hermiticity**: NO operator in class 14 has `+ h.c.` — the
  explicit `i` (or its absence) printed in the paper table makes each
  operator Hermitian on its own. Implement the `i`/no-`i` prefactor
  literally, never add `HC[aux]`, and register every operator with
  Straub class `2` and rotations `{VLL,VLL}`/`{VLR,VLR}`/`{VDL,VDL}`/
  `{VUR,VUR}`/`{VDR,VDR}` (same rule as Hermitian class-11/13 ops).
- Class-14 FlavorExpand: build the full `aux`, then two-step
  `ExpandIndices[...,{SU2D8}]` followed by `ExpandIndices[aux,{SU2W8}]`
  (the `SU2D8` step is a harmless no-op for singlet fermions; `SU2W8`
  is always needed since `DC` on doublets/`Phi8` contains W).
- **Class-15 Hermitian-derivative convention (IMPORTANT)**: the paper
  tables write `(H^dag <-> D^mu H)` WITHOUT a factor i, and the authors'
  own template (`e2Wphi2Dn4` in `FermionicDim8Operators.tex` and the
  pre-existing sample `e2Bphi2Dn4.fr`) implements it literally with
  **no explicit `I`**:
  `(Phi8bar[kk] DC[Phi8[kk],mu] - DC[Phi8bar[kk],mu] Phi8[kk])`
  (isospin-triplet version: `2 Ta8[ll,kk,oo] (Phi8bar[kk] DC[Phi8[oo],mu]
  - DC[Phi8bar[kk],mu] Phi8[oo])`). This differs from the dim-6
  `phil1`-type code, where the operator is defined with `H^dag i <-> D H`
  and carries an explicit `I` — do NOT add `I` in class 15; follow the
  authors' template.
- **Class-15 total derivative** `D^mu (H^dag H)` / `D^mu (H^dag tau^I H)`
  by the Leibniz rule (both placements, `+` sign):
  `(DC[Phi8bar[kk],mu] Phi8[kk] + Phi8bar[kk] DC[Phi8[kk],mu])`, with
  `2 Ta8[ll,kk,oo]` inserted in both terms for the `tau^I` version
  (same construction as class-13 `l2phi4Dn4`).
- **Class-15 Hermiticity**: only the six `udXphi2` operators carry
  `+ h.c.` -> `(aux + HC[aux])`, rotations `{VUR,VDR}`, Straub class `1`.
  All other class-15 operators: plain `aux`, no HC, Straub class `2`,
  rotations `{VLR,VLR}`/`{VUR,VUR}`/`{VDR,VDR}`/`{VLL,VLL}`/`{VDL,VDL}`
  (same rule as Hermitian class-11/13/14 ops).
- **`Htilde^dag <-> D^{(I) mu} H`** (`ud` class-15 ops): both derivative
  placements written out with `Eps[jj,kk]`:
  `Eps[jj,kk] (Phi8[kk] DC[Phi8[jj],mu] - DC[Phi8[kk],mu] Phi8[jj])`;
  isospin version inserts `2 Ta8[ll,jj,oo]` in both terms:
  `Eps[jj,kk] (Phi8[kk] 2 Ta8[ll,jj,oo] DC[Phi8[oo],mu] -
  DC[Phi8[kk],mu] 2 Ta8[ll,jj,oo] Phi8[oo])`.
- **Class-15 `eps^{IJK}` operators** (`l2W`/`q2W` n9-n12):
  `Eps[aa,bb,cc]` with `2 Ta8[aa,ii,jj]` on the fermion bilinear,
  `2 Ta8[bb,kk,oo]` in the Higgs bilinear, field strength on `cc`.
- Class-15 FlavorExpand: same two-step recipe as class 14
  (`{SU2D8}` then `{SU2W8}`); the pre-existing sample `e2Bphi2Dn4`
  keeps its original single-step `{SU2W8,SU2D8}` (both work here).
- Dual `Btilde`: written `Eps[mu,nu,al,be]/2 HC[FS[B8,al,be]]` in the new
  files (the `HC` is a harmless no-op for the real abelian B; the
  pre-existing `e2Bphi2Dn4` uses plain `FS[B8,al,be]`).
- Naming: paper `Q_{udXH^2}^{(n)}` has no `D` in its name ->
  `udGphi2n1/n2`, `udWphi2n1/n2`, `udBphi2n1/n2` (not `...phi2Dn`).
- **Class-16 naming exception (IMPORTANT)**: the authors' pre-existing,
  already-registered sample is `leWHD2n1` — it keeps the paper's `H`
  instead of applying the `H -> phi` rule (`leWphiD2n1` would be the
  rule-conforming name). To avoid renaming a registered WC, ALL class-16
  operators follow this `<f><X>HD2nN` pattern (`leB`, `quG/W/B`,
  `qdG/W/B` + `HD2n1..3`). Class 17 follows its sample `lephi3D2n1`
  (`phi3D2` — rule-conforming).
- **Derivative on a fermion inside a bilinear** (class 16 n1/n2):
  `F8bar[..].DC[f8[..],si]` — `DC` sits on the right field inside the
  Dot (cf. authors' `leWHD2n1`).
- **Derivative of a field strength** `D_rho X_{mu nu}` (class 16 n3):
  `DC[FS[X8,mu,nu,adj],si]`. Verified against the FeynRules source
  (ToolBox.m / Core/Initialisation.m): `FS` eagerly expands into
  `del[A]` terms + the nonabelian `g f A A` piece, and `DC` distributes
  over sums and products (Leibniz) with `FieldQ[del[f,_]] := FieldQ[f]`,
  so `DC[FS[...],si]` is the correct covariant derivative of the field
  strength.
- **Derived Htilde** (class 16/17 `qu` ops): `D_nu Htilde_i ->
  Eps[ii,kk] DC[Phi8bar[kk],nu]`; with `tau^I`:
  `2 Ta8[ll,ii,jj] Eps[jj,kk] DC[Phi8bar[kk],nu]`. Underived `Htilde`
  keeps the classic `Eps[ii,jj] HC[Phi8[jj]]` idiom (cf. 209/210/212).
- **Class-17 n5/n6 bracket order**: `le`/`qd` use `(H^dag D_mu H)` ->
  `Phi8bar[kk] DC[Phi8[kk],mu]`, but `qu` uses `(D_mu H^dag H)` ->
  `DC[Phi8bar[kk],mu] Phi8[kk]` — implemented literally per the paper
  table (hypercharge pattern), do not "unify".
- Class-16 FlavorExpand: sample's two-step — full expression
  `ExpandIndices[...,{SU2D8}]` into `tmp`, then WC-multiplied
  `ExpandIndices[...,{SU2W8}]`. Class-17: class-13-style separate
  `tmp1` (Higgs bilinear) / `tmp2` (fermion bilinear + its H factor),
  each `{SU2D8}`, final WC-multiplied combination `{SU2W8}` (required:
  n2/n4 share the adjoint dummy `ll` across `tmp1`/`tmp2`, and the
  n5/n6 fermion bracket contains `DC`).
- Class-16/17 Hermiticity: EVERY operator in both classes has `+ h.c.`
  (Table-9 caption) -> `(aux + HC[aux])`, Straub class `1`, rotations
  `le -> {VLL,VLR}`, `qu -> {VUL,VUR}`, `qd -> {VDL,VDR}` (same as
  classes 9/10/12).

## Four-fermion conventions (class 18, applicable to 19-21)

- **Class-18 tables**: the class spans `tab:smeft8class_18_21` (Table 10:
  `(LR)(RL) H^2 + h.c.` block, 6 ops, + the `18(Bslash)` BLV block,
  10 ops; the class-21 blocks of that table are NOT class 18) and
  `tab:smeft8class_18` (Table 11: `(LL)(LL)` 11, `(RR)(RR)` 7,
  `(LL)(RR)` 16, `(LR)(LR) + h.c.` 15). Total 65 operators.
  NB: the paper numbering has NO `Q_{q^4H^2}^{(4)}` — the `q4phi2`
  family is n1, n2, n3, n5 (n4 was removed in a paper revision); do not
  "fix" the gap.
- **Per-operator layout**: `lagrangian/218_psi4phi2/<name>.fr` (55 ops)
  and — BLV operators marked by a separate directory —
  `lagrangian/218BL_psi4phi2/<name>.fr` (10 ops, header comment
  `BLV operator` + warning line). Both get their own
  `Scan/Select/FileExistsQ` loader in `code/smeft_io.m`. BLV names are
  registered in `SMEFT$Dim8FourFermionBLVOperators` (NOT in the
  FourQuark/TwoQuarkTwoLepton/FourLepton lists) and carry `True` as the
  3rd `SMEFT$TensorWC` entry.
- **4F registration lists**: non-BLV names split by field content into
  `SMEFT$Dim8FourLeptonOperators` / `SMEFT$Dim8FourQuarkOperators` /
  `SMEFT$Dim8TwoQuarkTwoLeptonOperators` (e.g. `e2u2phi2` is
  two-quark-two-lepton, `u2d2phi2*` is four-quark).
- **Gamma currents**: two bilinears joined by Dot, one Ga per current:
  `(F8bar[sp1,..,ff1].F8[sp2,..,ff2]).(G8bar[sp3,..,ff3].G8[sp4,..,ff4])
  Ga[mu,sp1,sp2] Ga[mu,sp3,sp4]` (cf. authors' `l4phi2n1`). Scalar
  bilinears reuse one `sp` per bilinear; tensor bilinears use 4 spinor
  indices with `Sigma[mu,nu,sp1,sp2] Sigma[mu,nu,sp3,sp4]` (cf. dim-6
  `lequ3`).
- **Colour-octet pair**: `T8[aa,cc1,dd1] T8[aa,cc2,dd2]` with barred
  fields carrying `cc1/cc2` and unbarred `dd1/dd2` (cf. dim-6 `quqd8`).
- **`(tau^I eps)_{jk} x (H^dag tau^I H)` idiom** (authors' `q2udphi2n2`
  template): `tmp = 2 Ta8[aa,mm,nn] 2 Ta8[aa,jj,ll] // SU2Simplify;`
  then `tmp Eps[ll,kk] Phi8bar[mm] Phi8[nn]` with the first bilinear
  carrying `jj`, the second `kk` — the adjoint index is eliminated
  before ExpandIndices, so `FlavorExpand->{SU2D8}` suffices. Used for
  all `(tau eps)`/`(eps tau)` LR-LR and BLV variants (implement the
  eps/tau index order literally per table).
- **FlavorExpand for 4F**: no derivatives/field strengths in class 18,
  so: no `Ta8` -> `{SU2D8}` (with `(H^dag H)` pre-expanded as separate
  `tmp`); explicit `2 Ta8 ... 2 Ta8` pairs -> single-step
  `{SU2D8,SU2W8}` (authors' `l4phi2n2`/`l2e2phi2n2` style); the
  `eps^{IJK}` three-`Ta8` ops (`l2q2phi2n5`, `q4phi2n5`) -> two-step
  `{SU2D8}` then `{SU2W8}` (authors' `l4Wn1` style). Colour indices
  never need FlavorExpand.
- **(LR)(RL) `Htilde^dag` bilinears** (`l2udphi2`, `lequphi2n5`,
  `q2udphi2n5/n6`): `(Fbar f H)` -> `Phi8[ii]` on the barred doublet
  index; `(Htilde^dag ubar f)` -> `Eps[jj,kk] Phi8[kk]` on the unbarred
  doublet index (same Htilde^dag rule as classes 13/15).
- **`(qbar u Htilde)(qbar u Htilde)`** (`q2u2phi2n5/n6`): each Htilde as
  `Eps[ii,kk] HC[Phi8[kk]]` (classic idiom).
- **BLV bilinear** `(psi1 C psi2)`:
  `HC[CC[X8][sp1,(doublet,)ff,(colour)]].Ga[0,sp1,sp2].Y8[sp2,...]`,
  bilinears multiplied (not dotted), colour `Eps[aa,bb,cc]`
  (cf. dim-6 `11_BL.fr` and authors' `lqudphi2n1`). BLV Higgs factors
  are UN-barred: `H^k H^n -> Phi8[kk] Phi8[nn]`, `Htilde^k ->
  Eps[kk,ww] HC[Phi8[ww]]`; `(H^dag_m H^k) -> Phi8bar[mm] Phi8[kk]`.
  Paper typos: the `C` is missing in the first bilinears of
  `Q_{lqd^2H^2}` and `Q_{eq^2dH^2}` in Table 10 — it is implied
  (noted in the file headers).
- **Class-18 Hermiticity / Straub classes / rotations**:
  - `(LL)(LL)`, `(RR)(RR)`, `(LL)(RR)` blocks: Hermitian, plain `aux`,
    no HC. Straub classes follow the dim-6 analogues: identical
    currents -> `4` (`ll/qq/uu/dd`-like: `q4phi2n1/n3`, `d4phi2`),
    `e4phi2` -> `6` (`ee`-like), two independent currents -> `5`
    (`lq/qe/lu/ld/eu/ed/qu/qd/ud`-like, incl. the `eps^{IJK}`
    `l2q2phi2n5`); `q4phi2n2` -> `9` mirroring the authors' choice for
    `l4phi2n2` (tau on only one of two identical currents), and
    `q4phi2n5` -> `9` (`eps^{IJK}` over identical currents).
  - `(LR)(LR)`, `(LR)(RL)` and ALL BLV operators: `+ h.c.` ->
    `(aux + HC[aux])`, Straub class `9`.
  - Rotations: 4 entries in field order p,r,s,t. Dim-8 convention for
    `q_L`: pick the V matching the partner in the bilinear — `q` paired
    with `u` -> `VUL` (`q2udphi2*` = `{VUL,VUR,VDL,VDR}` per the
    pre-existing samples, `lequphi2n1-4` = `{VLL,VLR,VUL,VUR}` — NB
    differs from dim-6 `lequ1/quqd1` which use `VDL` there); Hermitian
    `(qbar ... q)` currents -> `{VDL,VDL}`; BLV rows follow the dim-6
    BLV analogues (`duq`, `qqu`, `duu`, `qqq` patterns).
  - **FLAGGED, not changed**: pre-existing `lqudphi2n1` is registered
    with Straub class `7` (= `qque`-like, symmetric in the first two
    flavour indices), but its structure `eps_abc (d C u)(q C l)` has NO
    p<->r symmetry and the identical dim-6 `duq` uses class `9`. Kept
    as the authors registered it; `lqudphi2n2` (same field content)
    uses `9`. Maintainer should confirm/fix `n1`.

## Progress log

### 2026-06-16 (MR, AI-assisted) — Class 9 (psi^2 X^2 H + h.c.), 1st column of 2005.00059

Implemented the full first column of the class-9 table. The single
pre-existing operator `leG2phin1` (by AD, 08/06/2026) was kept; the
remaining 23 operators were added in `lagrangian/209_psi2X2phi.fr`:

Leptonic (`(lbar_p e_r) H ...`, Higgs `H = Phi8[ii]`):
- `leG2phin1` : `G^A_{mu nu} G^{A mu nu}`            (pre-existing)
- `leG2phin2` : `Gtilde^A_{mu nu} G^{A mu nu}`
- `leW2phin1` : `W^I_{mu nu} W^{I mu nu}`
- `leW2phin2` : `Wtilde^I_{mu nu} W^{I mu nu}`
- `leW2phin3` : `eps^{IJK} sigma^{mu nu} tau^I, W^J_{mu ro} W^{K ro}_nu`

Quark (`(qbar_p ... u_r) Htilde ...`, `Htilde = Eps[ii,kk] HC[Phi8[kk]]`):
- `quG2phin1` : `G^A G^A`
- `quG2phin2` : `Gtilde^A G^A`
- `quG2phin3` : `d^{ABC} T^A, G^B G^C`
- `quG2phin4` : `d^{ABC} T^A, Gtilde^B G^C`
- `quG2phin5` : `f^{ABC} sigma^{mu nu} T^A, G^B_{mu ro} G^{C ro}_nu`
- `quGWphin1` : `T^A tau^I, G^A W^I`
- `quGWphin2` : `T^A tau^I, Gtilde^A W^I`
- `quGWphin3` : `sigma^{mu nu} T^A tau^I, G^A_{mu ro} W^{I ro}_nu`
- `quGBphin1` : `T^A, G^A B`
- `quGBphin2` : `T^A, Gtilde^A B`
- `quGBphin3` : `sigma^{mu nu} T^A, G^A_{mu ro} B_nu^{ro}`
- `quW2phin1` : `W^I W^I`
- `quW2phin2` : `Wtilde^I W^I`
- `quW2phin3` : `eps^{IJK} sigma^{mu nu} tau^I, W^J_{mu ro} W^{K ro}_nu`
- `quWBphin1` : `tau^I, W^I B`
- `quWBphin2` : `tau^I, Wtilde^I B`
- `quWBphin3` : `sigma^{mu nu} tau^I, W^I_{mu ro} B_nu^{ro}`
- `quB2phin1` : `B B`
- `quB2phin2` : `Btilde B`

Files modified:
- `lagrangian/209_psi2X2phi.fr` — 23 new `LQ...` definitions + header notes.
- `code/smeft_variables.m` — names added to
  `SMEFT$Dim8TwoFermionOperators`; rows added to `SMEFT$TensorWC`
  (`le*` -> `{VLL,VLR}`, `qu*` -> `{VUL,VUR}`, all `False`, Straub class `1`).
- `smeft_fr_init.m` — class-09 entry of the (commented) `OpList8`
  reference list expanded to the full set.

### 2026-06-16 (MR, AI-assisted) — Class 9, 2nd column of 2005.00059

Implemented the full second column of the class-9 table (24 operators):
the leptonic `WB`/`B^2` operators and the complete down-quark (`qd`)
analogues of the column-1 up-quark operators. All of these use the
*plain* Higgs `H` (`Phi8[ii]`, contracted with the left doublet directly
or via `tau^I`), in contrast to the column-1 up-quark operators which use
`Htilde`.

Leptonic (`(lbar_p ... e_r) ... H ...`):
- `leWBphin1` : `tau^I, W^I B`
- `leWBphin2` : `tau^I, Wtilde^I B`
- `leWBphin3` : `sigma^{mu nu} tau^I, W^I_{mu ro} B_nu^{ro}`
- `leB2phin1` : `B B`
- `leB2phin2` : `Btilde B`

Down-quark (`(qbar_p ... d_r) ... H ...`):
- `qdG2phin1` : `G^A G^A`
- `qdG2phin2` : `Gtilde^A G^A`
- `qdG2phin3` : `d^{ABC} T^A, G^B G^C`
- `qdG2phin4` : `d^{ABC} T^A, Gtilde^B G^C`
- `qdG2phin5` : `f^{ABC} sigma^{mu nu} T^A, G^B_{mu ro} G^{C ro}_nu`
- `qdGWphin1` : `T^A tau^I, G^A W^I`
- `qdGWphin2` : `T^A tau^I, Gtilde^A W^I`
- `qdGWphin3` : `sigma^{mu nu} T^A tau^I, G^A_{mu ro} W^{I ro}_nu`
- `qdGBphin1` : `T^A, G^A B`
- `qdGBphin2` : `T^A, Gtilde^A B`
- `qdGBphin3` : `sigma^{mu nu} T^A, G^A_{mu ro} B_nu^{ro}`
- `qdW2phin1` : `W^I W^I`
- `qdW2phin2` : `Wtilde^I W^I`
- `qdW2phin3` : `eps^{IJK} sigma^{mu nu} tau^I, W^J_{mu ro} W^{K ro}_nu`
- `qdWBphin1` : `tau^I, W^I B`
- `qdWBphin2` : `tau^I, Wtilde^I B`
- `qdWBphin3` : `sigma^{mu nu} tau^I, W^I_{mu ro} B_nu^{ro}`
- `qdB2phin1` : `B B`
- `qdB2phin2` : `Btilde B`

Files modified (same three as above):
- `lagrangian/209_psi2X2phi.fr` — 24 new `LQ...` definitions appended;
  header comment updated to document both columns and the H/Htilde rule.
- `code/smeft_variables.m` — names added to
  `SMEFT$Dim8TwoFermionOperators`; rows added to `SMEFT$TensorWC`
  (`le*` -> `{VLL,VLR}`, `qd*` -> `{VDL,VDR}`, all `False`, Straub class `1`).
- `smeft_fr_init.m` — class-09 reference `OpList8` extended to all 48
  class-9 two-fermion operators.

Status: the full class-9 (`psi^2 X^2 H + h.c.`) two-fermion table of
2005.00059 (both columns, 48 operators) is now implemented.

### 2026-07-13 (MR, AI-assisted) — Classes 10-13 complete (Table 5 of 2005.00059)

Implemented all remaining operators of Table 5 as per-operator files
(new files use the 8-suffixed field conventions, see section above):

- **Class 10 (psi^2 X H^3 + h.c.)** — `lagrangian/210_psi2Xphi3/`,
  11 operators (9 new + pre-existing `leWphi3n1`, `leWphi3n2` moved
  unchanged from the old flat file): `leBphi3`, `quGphi3`, `quWphi3n1`,
  `quWphi3n2`, `quBphi3`, `qdGphi3`, `qdWphi3n1`, `qdWphi3n2`, `qdBphi3`.
  Sigma bilinears; `qu*` use `Htilde` (`Eps[ii,kk] HC[Phi8[kk]]`, and
  `tau^I Htilde -> 2 Ta8[ll,ii,jj] Eps[jj,kk] HC[Phi8[kk]]`), `le*`/`qd*`
  use plain `H`; the `n2` variants carry `(H^dag tau^I H)` instead of
  `(H^dag H)`. All `+ h.c.`.
- **Class 11 (psi^2 H^2 D^3)** — `lagrangian/211_psi2phi2D3/`,
  15 operators (14 new + pre-existing `l2phi2D3n1`):
  `l2phi2D3n2..n4`, `e2phi2D3n1/n2`, `q2phi2D3n1..n4`, `u2phi2D3n1/n2`,
  `d2phi2D3n1/n2`, `udphi2D3`. `n1/n3`-type: `(D_(mu D_nu) H^dag ... H)`;
  `n2/n4`-type: `(H^dag ... D_(mu D_nu) H)`; `n3/n4` carry `tau^I` in both
  bilinears. Only `udphi2D3` has `+ h.c.`.
  (NB: the `(4)` entry printed as `Q_{q^2H^2D^2}^{(4)}` in the paper table
  is a typo for `q^2H^2D^3` — implemented as `q2phi2D3n4`.)
- **Class 12 (psi^2 H^5 + h.c.)** — directory `Dim8Class12/` renamed to
  `lagrangian/212_psi2phi5/` (3 operators unchanged: `lephi5`, `quphi5`,
  `qdphi5`); old flat `212_psi2phi5.fr` and the `SMEFT$Dim8Class12`
  loader variable removed.
- **Class 13 (psi^2 H^4 D)** — `lagrangian/213_psi2phi4D/`,
  12 operators (11 new + pre-existing `l2phi4Dn1`): `l2phi4Dn2..n4`,
  `e2phi4D`, `q2phi4Dn1..n4`, `u2phi4D`, `d2phi4D`, `udphi4D`.
  `n2` = sum of two bracket terms sharing one WC; `n3`/`n4` carry
  `Eps[aa,bb,cc]` over three `Ta8` insertions; `n4` has **no factor i**
  and uses `D_mu(H^dag tau^K H)` by the Leibniz rule
  (`DC[Phi8bar]..Phi8 + Phi8bar..DC[Phi8]`). Only `udphi4D` has `+ h.c.`.

Files modified:
- `code/smeft_io.m` — flat `Get`s for 210/211/213 and the `Dim8Class12`
  block replaced by four on-demand `Scan/Select/FileExistsQ` loaders
  (dirs `210_psi2Xphi3`, `211_psi2phi2D3`, `212_psi2phi5`,
  `213_psi2phi4D`), same pattern as class 209.
- `code/smeft_variables.m` — all 41 class-10..13 names in
  `SMEFT$Dim8TwoFermionOperators`; `SMEFT$TensorWC` rows per the
  Hermiticity/rotation rules above.
- `smeft_fr_init.m` — commented reference `OpList8` lists for classes
  10-13 completed (also fixed the duplicated `"leWphi3n2"` typo).

Verified: all 41 `.fr` files + edited `.m` files parse in wolframscript;
file names == `SMEFT$Dim8TwoFermionOperators` (class 10-13 section) ==
`SMEFT$TensorWC` rows == `LQ` symbols == WC strings inside files;
pre-existing operator bodies (`leWphi3n1/n2`, `l2phi2D3n1`, `l2phi4Dn1`)
carried over byte-identical modulo headers.

Status: Table 5 (classes 10-13) fully implemented. Together with class 9,
all two-fermion dim-8 classes 9-17 sample coverage now: 9-13 complete,
14-17 still only sample operators (`l2G2D`, `e2Bphi2Dn4`, `leWHD2n1`,
`lephi3D2n1`).

### 2026-07-13 (MR, AI-assisted) — Class 14 complete (psi^2 X^2 D, Table 6 of 2005.00059)

Implemented all 57 class-14 operators as per-operator files in
`lagrangian/214_psi2X2D/` (56 new + pre-existing `l2G2D` moved with
byte-identical body). The class spans two tables in the paper: the
hadronic table (`tab:smeft8class_14qud`, 44 ops) and the top of the
class-14-leptonic/class-15 table (`tab:smeft8class_14le_15RR`, 13 ops).

Operator inventory (structure -> template):
- `X^2` type `i (psibar ga^mu <->D^nu psi) X_{mu ro} X_nu^{ro}`:
  `q2G2Dn1`, `q2W2Dn1`, `q2B2D`, `u2G2Dn1`, `u2W2D`, `u2B2D`,
  `d2G2Dn1`, `d2W2D`, `d2B2D`, `l2G2D`, `l2W2Dn1`, `l2B2D`,
  `e2G2D`, `e2W2D`, `e2B2D`.
- `f^{ABC} T^A` (no i): `q2G2Dn2`, `u2G2Dn2`, `d2G2Dn2`;
  `i d^{ABC} T^A`: `q2G2Dn3`, `u2G2Dn3`, `d2G2Dn3`.
- `f^{ABC} T^A` with `(G Gtilde -+ Gtilde G)`: `n4` (i, minus),
  `n5` (no i, plus) for `q2/u2/d2G2D`.
- `eps^{IJK} tau^I`: `q2W2Dn2`, `l2W2Dn2` (no i, `W W`);
  `q2W2Dn3`, `l2W2Dn3` (i, `W Wtilde - Wtilde W`);
  `q2W2Dn4`, `l2W2Dn4` (no i, `W Wtilde + Wtilde W`).
- mixed-pair type `(X_{mu ro} Y_nu^{ro} -+ X_{nu ro} Y_mu^{ro})`,
  n1(-,no i), n2(+,i), n3(-,no i, dual on Y), n4(+,i, dual on Y):
  `q2GWDn1-4` (X=G^A, Y=W^I, both `T8` and `Ta8`),
  `q2GBDn1-4`/`u2GBDn1-4`/`d2GBDn1-4` (X=B, Y=G^A, `T8`),
  `q2WBDn1-4`/`l2WBDn1-4` (X=B, Y=W^I, `Ta8`).

Files were generated from a template script (scratchpad `gen_class14.py`)
to keep the 4-fold n1..n4 families uniform; the i/no-i prefactor of every
file was audited 1:1 against the paper tables.

Files modified (same pattern as classes 9-13):
- `code/smeft_io.m` — flat `Get[214_psi2X2D.fr]` replaced by the
  on-demand `Scan/Select/FileExistsQ` loader for `214_psi2X2D/`.
- `code/smeft_variables.m` — 57 names added to
  `SMEFT$Dim8TwoFermionOperators` (ordered as in the paper tables);
  57 `SMEFT$TensorWC` rows, all `False`, Straub class `2`,
  rotations `q2 -> {VDL,VDL}`, `u2 -> {VUR,VUR}`, `d2 -> {VDR,VDR}`,
  `l2 -> {VLL,VLL}`, `e2 -> {VLR,VLR}`.
- `smeft_fr_init.m` — Class 14 reference list completed.

Verified: 57 files parse in wolframscript; names == operator list ==
TensorWC rows == `LQ` symbols == WC strings; i-factors of all 57 files
match the paper; `l2G2D` body unchanged.

Status: two-fermion classes 9-14 fully implemented and separated.

### 2026-07-14 (MR, AI-assisted) — Class 15 complete (psi^2 X H^2 D, Tables 7-8 of 2005.00059)

Completed and verified all 86 class-15 operators as per-operator files in
`lagrangian/215_psiXphi2D/` (85 new + pre-existing `e2Bphi2Dn4` kept with
its original body). The class spans two tables in the paper: the bottom of
`tab:smeft8class_14le_15RR` (Table 7, `(RR) X H^2 D`, 38 ops — the top of
that table is the class-14 leptonic block logged above) and
`tab:smeft8class_15LL` (Table 8, `(LL) X H^2 D`, 48 ops). The file bodies
and registration were generated in the 2026-07-13 session but left
unlogged; this session audited every file 1:1 against the paper and
completed the documentation.

Operator inventory (structure -> template; n1/n2 = `D^mu(H^dag ... H)`
with plain/dual X, n3/n4 = `(H^dag <-> D^{(I)mu} H)` with plain/dual X):
- RR, isospin triplet Higgs bilinear (`D^mu(H^dag tau^I H)` resp.
  `<-> D^{I mu}`): `e2Wphi2Dn1-4`, `u2Wphi2Dn1-4`, `d2Wphi2Dn1-4`.
- RR, isospin singlet: `e2Bphi2Dn1-4`, `u2Bphi2Dn1-4`, `d2Bphi2Dn1-4`,
  and with `T8`: `u2Gphi2Dn1-4`, `d2Gphi2Dn1-4`.
- RR `+ h.c.`: `udGphi2n1/n2` (`T8`, `Htilde^dag <-> D^mu H`),
  `udWphi2n1/n2` (`Htilde^dag <-> D^{I mu} H`), `udBphi2n1/n2`.
- LL `l2Wphi2Dn1-12` / `q2Wphi2Dn1-12`: n1-n4 singlet fermion bilinear x
  triplet Higgs bilinear; n5-n8 `tau^I` fermion bilinear x singlet Higgs
  bilinear; n9-n12 `eps^{IJK}` over fermion `tau^I`, Higgs `tau^J`, `W^K`.
- LL `l2Bphi2Dn1-8` / `q2Bphi2Dn1-8`: n1-n4 `tau^I` x `tau^I` (shared
  adjoint dummy `ll`); n5-n8 singlet x singlet; B field strength.
- LL `q2Gphi2Dn1-8`: n1-n4 `T^A tau^I` x `tau^I`; n5-n8 `T^A` x singlet;
  gluon field strength.

Files modified (same pattern as classes 9-14):
- `code/smeft_io.m` — on-demand `Scan/Select/FileExistsQ` loader for
  `215_psiXphi2D/`.
- `code/smeft_variables.m` — 86 names in
  `SMEFT$Dim8TwoFermionOperators` (ordered as in the paper tables);
  86 `SMEFT$TensorWC` rows, all `False`; `ud*` -> `{VUR,VDR}`, Straub
  class `1`; all others Straub class `2` with `e2 -> {VLR,VLR}`,
  `u2 -> {VUR,VUR}`, `d2 -> {VDR,VDR}`, `l2 -> {VLL,VLL}`,
  `q2 -> {VDL,VDL}`.
- `smeft_fr_init.m` — Class 15 reference list completed.

Verified (this session): file inventory == paper Tables 7-8 == operator
list == TensorWC rows == `LQ` symbols == WC strings (86 each, no
duplicates; full two-fermion list now 234 names = 48+41+57+86+1+1);
per-file structural audit (dual `Eps[mu,nu,al,be]/2` exactly on even-n
ops, `Eps[aa,bb,cc]` exactly on `l2W`/`q2W` n9-n12, `T8` exactly on
gluonic ops, `(aux + HC[aux])` exactly on the six `ud*` ops, no stray
explicit `I` anywhere — the class has none); all 86 files `Get` cleanly
in wolframscript and define their `LQ<name>` symbols; edited `.m` files
parse; pre-existing `e2Bphi2Dn4` body unchanged.

Status: two-fermion classes 9-15 fully implemented and separated.
User task naming note: "Classes 14 and 15 (Tables 7 and 8)" = paper
Table 7 (`tab:smeft8class_14le_15RR`: class-14 leptonic block, done
2026-07-13, + class-15 RR block) and Table 8 (`tab:smeft8class_15LL`).

### 2026-07-14 (MR, AI-assisted) — Classes 16-17 complete (psi^2 X H D^2 and psi^2 H^3 D^2, Table 9 of 2005.00059)

Implemented all remaining operators of Table 9 (`tab:smeft8class_16_17`)
as per-operator files (generated from scratchpad `gen_class16_17.py`,
audited 1:1 against the paper):

- **Class 16 (psi^2 X H D^2 + h.c.)** — `lagrangian/216_psiXphiD2/`,
  24 operators (23 new + pre-existing `leWHD2n1` moved with
  byte-identical body from the old flat file). Structure per family
  `f in {le, qu, qd}` x gauge `X in {G (qu/qd only), W, B}`:
  - n1: `(Fbar sigma^{mu nu} [T^A/tau^I] D^rho f) (D_nu H~) X_{rho mu}`
    -> `F8bar.DC[f8,si] Sigma[mu,nu,..] ... FS[X8,si,mu,adj]`;
  - n2: `(Fbar [T^A/tau^I] D^rho f) (D^nu H~) Xtilde_{rho nu}` — scalar
    bilinear (single `sp`), dual `Eps[si,nu,al,be]/2 HC[FS[X8,al,be,..]]`;
  - n3: `(Fbar sigma^{mu nu} [T^A/tau^I] f) (D^rho H~) (D_rho X_{mu nu})`
    -> `DC[Phi8...,si] DC[FS[X8,mu,nu,adj],si]`.
  `qu*` use derived `Htilde` (`Eps[ii,kk] DC[Phi8bar[kk],..]`),
  `le*`/`qd*` plain `H`; `W` families carry `2 Ta8`, `G` families `T8`.
  Names keep the sample's `HD2` pattern (see naming-exception note).
- **Class 17 (psi^2 H^3 D^2 + h.c.)** — `lagrangian/217_psi2phi3D2/`,
  18 operators (17 new + pre-existing `lephi3D2n1` moved with
  byte-identical body). Per family n1-n6:
  n1/n2 `(D_mu H^dag [tau^I] D^mu H)(Fbar f [tau^I] H~)` (scalar),
  n3/n4 same with `(D_mu H^dag [tau^I] D_nu H)` and `sigma^{mu nu}`,
  n5 `(H^dag D_mu H)(Fbar f D^mu H~)` (`qu`: `(D_mu H^dag H)`),
  n6 same with `sigma^{mu nu}` and `D_nu H~`.

Files modified (same pattern as classes 9-15):
- `code/smeft_io.m` — flat `Get`s for `216_psiXphiD2.fr` /
  `217_psi2phi3D2.fr` replaced by on-demand `Scan/Select/FileExistsQ`
  loaders; the two flat files deleted.
- `code/smeft_variables.m` — 42 names in
  `SMEFT$Dim8TwoFermionOperators` (paper-table order); 42 `SMEFT$TensorWC`
  rows, all `False`, Straub class `1`, rotations `le -> {VLL,VLR}`,
  `qu -> {VUL,VUR}`, `qd -> {VDL,VDR}` (pre-existing sample rows kept).
- `smeft_fr_init.m` — Class 16/17 reference lists completed.

Verified: file inventory == Table 9 == operator list == TensorWC rows ==
`LQ` symbols == WC strings (24+18, no duplicates; full two-fermion list
now 274 names = 48+41+57+86+24+18); structural audit (Sigma exactly on
n1/n3 (class 16) and n3/n4/n6 (class 17), fermion-`DC` exactly on class-16
n1/n2, `DC[FS[..]]` exactly on class-16 n3, dual exactly on class-16 n2,
`T8`/`Ta8`/`Phi8bar` placement per family, `(aux + HC[aux])` in all 42,
no stray `I` — Table 9 has none); Module variable lists match used
indices; all 42 files `Get` cleanly in wolframscript and define their
`LQ<name>` symbols; edited `.m` files parse; both pre-existing operator
bodies carried over byte-identical (diff-checked against the flat files
before deletion).

Status: ALL two-fermion dim-8 classes 9-17 of 2005.00059 are now fully
implemented as per-operator files.

TODO / notes for future work:
- Run a small test (e.g. `OpList8 = {"qdWphi3n2", "q2phi2D3n3",
  "l2phi4Dn4", "udphi4D", "q2GWDn3", "q2W2Dn3", "l2Wphi2Dn9",
  "udWphi2n1", "quWHD2n3", "quphi3D2n4"}`) through
  `SMEFTInitializeModel` / Feynman-rule generation to sanity-check index
  expansion of the most complex new structures before doing a large run
  (not yet done — same status as for classes 9-15). The class-16 n3
  operators (`DC[FS[...]]`) especially deserve a runtime check, as they
  are the first use of a covariant derivative of a field strength in
  this codebase.
- Classes 19-21 (4-fermion) still partially implemented in flat files
  (class 18 done, see 2026-07-15 entry).

### 2026-07-15 (MR, AI-assisted) — Class 18 complete (psi^4 H^2, Tables 10-11 of 2005.00059)

Implemented all 65 class-18 operators as per-operator files (generated
from scratchpad `gen_class18.py`, audited 1:1 against the paper):

- **B/L-conserving** — `lagrangian/218_psi4phi2/`, 55 operators
  (45 new + 10 pre-existing moved with byte-identical bodies:
  `leqdphi2n1/n2`, `l4phi2n1/n2`, `e4phi2`, `u4phi2`, `l2e2phi2n1/n2`,
  `q2udphi2n1/n2`):
  - `(LR)(RL) + h.c.` (Table 10): `leqdphi2n1/n2` (pre-existing),
    `l2udphi2`, `lequphi2n5`, `q2udphi2n5/n6`.
  - `(LL)(LL)` (Table 11): `l4phi2n1/n2`, `q4phi2n1/n2/n3/n5`,
    `l2q2phi2n1..n5`.
  - `(RR)(RR)`: `e4phi2`, `u4phi2`, `d4phi2`, `e2u2phi2`, `e2d2phi2`,
    `u2d2phi2n1/n2`.
  - `(LL)(RR)`: `l2e2phi2n1/n2`, `l2u2phi2n1/n2`, `l2d2phi2n1/n2`,
    `q2e2phi2n1/n2`, `q2u2phi2n1..n4`, `q2d2phi2n1..n4`.
  - `(LR)(LR) + h.c.`: `q2udphi2n1..n4`, `lequphi2n1..n4`,
    `l2e2phi2n3`, `leqdphi2n3/n4`, `q2u2phi2n5/n6`, `q2d2phi2n5/n6`.
- **BLV (marked)** — `lagrangian/218BL_psi4phi2/`, 10 operators
  (9 new + pre-existing `lqudphi2n1` moved byte-identical); all headers
  carry a BLV warning line; all `+ h.c.`: `lqudphi2n1/n2`, `eq2uphi2`,
  `lq3phi2n1/n2/n3`, `eu2dphi2`, `lqu2phi2`, `lqd2phi2`, `eq2dphi2`.
  (Below-dashed-line ops `lq3phi2n3`, `lqu2phi2`, `lqd2phi2`,
  `eq2dphi2` — and non-BLV `q4phi2n5` — vanish for one generation;
  implemented literally, class 9 keeps the redundant entries.)

Files modified (same pattern as classes 9-17):
- `code/smeft_io.m` — flat `Get`s for `218_psi4phi2.fr` /
  `218BL_psi4phi2.fr` replaced by on-demand `Scan/Select/FileExistsQ`
  loaders; the two flat files deleted.
- `code/smeft_variables.m` — 55 non-BLV names distributed over
  `SMEFT$Dim8FourLeptonOperators` (6) / `SMEFT$Dim8FourQuarkOperators`
  (26) / `SMEFT$Dim8TwoQuarkTwoLeptonOperators` (23) and 10 BLV names
  in `SMEFT$Dim8FourFermionBLVOperators` (paper-table order);
  65 `SMEFT$TensorWC` rows per the Hermiticity/Straub/rotation rules in
  the conventions section above (BLV rows `True`).
- `smeft_fr_init.m` — Class 18 reference lists (BL conserving +
  BL violating) completed.

Verified: file inventory == paper Tables 10-11 == operator lists ==
TensorWC rows == `LQ` symbols == WC strings (55+10, no duplicates);
structural audit (HC exactly on the `(LR)(LR)`/`(LR)(RL)`/BLV ops,
`T8` pairs exactly on the octet ops, `Sigma` exactly on
`lequphi2n3/n4`/`leqdphi2n4`, `CC` exactly in the 10 BLV files,
`Eps[aa,bb,cc]` exactly on `eps^{IJK}`+BLV(colour) ops, `Ta8` counts
0/2/3 per family, no explicit `I` — the class has none); Module
variable lists match used indices (only pre-existing `q2udphi2n2`
carries an unused `ii`, kept byte-identical); all 65 files `Get`
cleanly in wolframscript and define their `LQ<name>` symbols; edited
`.m` files parse (`smeft_fr_init.m`/`smeft_io.m` via
`ReadList[..,Hold[Expression]]`); all 11 pre-existing bodies
diff-checked against the flat files before deletion.

Status: two-fermion classes 9-17 AND four-fermion class 18 fully
implemented as per-operator files. Remaining: classes 19-21
(4-fermion), still sample-only in flat files 219/220/221(BL).
Runtime TODO: no `SMEFTInitializeModel` run yet — suggested class-18
smoke subset: `OpList8 = {"l2q2phi2n5", "q4phi2n5", "q2udphi2n4",
"lequphi2n3", "q2u2phi2n6", "l2udphi2", "lqudphi2n2", "lq3phi2n3",
"lqu2phi2", "eq2dphi2"}` (covers eps^IJK, tau-eps SU2Simplify, T8
pairs, Htilde/Htilde^dag idioms and all BLV structure types).
