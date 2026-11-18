---
declaration: theorem
origin: cited
lean: BGW.LocallyFinite.exists_unique_bienaymeLaw, BGW.LocallyFinite.bienaymeLaw_toLocallyFinite
statement: formalized
proof: formalized
---

# Random Trees in Lean

[igor-kortchemski/random-trees-lean](https://github.com/igor-kortchemski/random-trees-lean) at commit [1117de92](https://github.com/igor-kortchemski/random-trees-lean/tree/1117de92488e1d0b90872400b766f8a941944559), 2026-11-10.

## Depends on

- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)

## Proof depends on

- [Gromov-Hausdorff space](../../topology/metric-spaces/gromov-hausdorff-space.md)
- [Egorov's theorem](../../../thousand-plus/analysis/28-measure-and-integration/egorovs-theorem.md)
- [Exponential law](../random-variables-and-their-laws/exponential-law.md)
- [Bolzano–Weierstrass theorem (1000+ theorems)](../../../thousand-plus/analysis/26-real-functions/part-01/bolzano-weierstrass-theorem.md)
- [Hausdorff distance](../../topology/metric-spaces/hausdorff-distance.md)
- [Convergence in distribution](../convergence-of-a-sequence-of-random-variables/convergence-in-distribution.md)
- [Lévy continuity theorem](../../../thousand-plus/probability-and-statistics/levy-continuity-theorem.md)
- [Uniform integrability](../../analysis/measures-and-integral-calculus/part-01/uniform-integrability.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`BGW.LocallyFinite.exists_unique_bienaymeLaw`](https://github.com/igor-kortchemski/random-trees-lean/blob/1117de92488e1d0b90872400b766f8a941944559/BGW/LocallyFinite/Unique.lean#L173) (theorem)
- [`BGW.LocallyFinite.bienaymeLaw_toLocallyFinite`](https://github.com/igor-kortchemski/random-trees-lean/blob/1117de92488e1d0b90872400b766f8a941944559/BGW/LocallyFinite/Atoms.lean#L36) (theorem)

No file its headlines import, directly or not (15 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 905 .lean files; its Lean libraries `BGW` hold 871, declaring 4,881 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/igor-kortchemski/random-trees-lean/blob/1117de92488e1d0b90872400b766f8a941944559/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `BrownianMotion`.

## Placement

Of its imports of Mathlib modules in an overview area, 131 of 807 are in Probability Theory, 8.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (131 of 807 imports, 8.5×), Topology (179 of 807 imports, 3.0×), Analysis (376 of 807 imports, 1.7×). *Proof depends on* names 8 of the 82 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [igor-kortchemski/random-trees-lean at 1117de92](https://github.com/igor-kortchemski/random-trees-lean/tree/1117de92488e1d0b90872400b766f8a941944559)
