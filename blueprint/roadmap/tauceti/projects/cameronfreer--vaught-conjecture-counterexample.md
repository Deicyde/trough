---
declaration: theorem
origin: cited
lean: VaughtConjecture.MainTheorem.vaughtCounterexample_allCarriers, VaughtConjecture.MainTheorem.vaughtCounterexample_allCarriers_densitySentence, VaughtConjecture.IsTemplateChart.hereditary, VaughtConjecture.IsTemplateChart.jointEmbedding, VaughtConjecture.IsTemplateChart.amalgamation, VaughtConjecture.proposition434Target, VaughtConjecture.proposition434Clauses_of_countable, VaughtConjecture.exists_lift_zero_of_realize_templateSentence
statement: formalized
proof: formalized
---

# vaught-conjecture-counterexample

*A counterexample to Vaught's conjecture for $L{\omega1,\omega}$*

[cameronfreer/vaught-conjecture-counterexample](https://github.com/cameronfreer/vaught-conjecture-counterexample) at commit [d159d16a](https://github.com/cameronfreer/vaught-conjecture-counterexample/tree/d159d16aa19bf338d8ad556becfa7749d5c13bb8), 2026-11-17.

> By Nathanael Ackerman, Cameron Freer, and Robin Knight.

*Quoted from [README.md](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/README.md), Apache-2.0.*

## Depends on

- [Language](../../mathlib/overview/logic-and-computation/formal-languages/language.md)
- [Ordinal](../../mathlib/overview/logic-and-computation/set-theory/ordinals/ordinal.md)
- [Set](../../mathlib/overview/data-structures/sets/set.md)

## Proof depends on

- [First-order structure](../../mathlib/overview/logic-and-computation/model-theory/first-order-structure.md)
- [Aleph numbers](../../mathlib/overview/logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Cardinal](../../mathlib/overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Finite set](../../mathlib/overview/data-structures/sets/finite-set.md)
- [Permutation group of a type](../../mathlib/overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Closure](../../mathlib/overview/topology/general-topology/part-01/closure.md)
- [Continuous function](../../mathlib/overview/topology/general-topology/part-01/continuous-function.md)
- [List](../../mathlib/overview/data-structures/list-like-structures/list.md)

## Main results

Its Lean names are 8 of the 56 theorems its README names in code:

- [`VaughtConjecture.MainTheorem.vaughtCounterexample_allCarriers`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/MainTheorem/GrowthLevelRoute.lean#L131) (theorem)
- [`VaughtConjecture.MainTheorem.vaughtCounterexample_allCarriers_densitySentence`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/MainTheorem/GrowthLevelRoute.lean#L150) (theorem)
- [`VaughtConjecture.IsTemplateChart.hereditary`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/Correspondence/Charts/Chart.lean#L310) (theorem)
- [`VaughtConjecture.IsTemplateChart.jointEmbedding`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/Correspondence/Charts/Chart.lean#L350) (theorem)
- [`VaughtConjecture.IsTemplateChart.amalgamation`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/Correspondence/Charts/Chart.lean#L377) (theorem)
- [`VaughtConjecture.proposition434Target`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/Correspondence/Proposition434.lean#L99) (theorem)
- [`VaughtConjecture.proposition434Clauses_of_countable`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/Correspondence/Proposition434.lean#L83) (theorem)
- [`VaughtConjecture.exists_lift_zero_of_realize_templateSentence`](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/VaughtConjecture/Correspondence/Proposition434.lean#L105) (theorem)

No file its headlines import, directly or not (418 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.36.0-rc1, Mathlib at [2e318fae](https://github.com/leanprover-community/mathlib4/tree/2e318faecff7d70d4e0cf8cc875104424a737355).
- 796 .lean files; its Lean libraries `VaughtConjecture` hold 783, declaring 12,290 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/cameronfreer/vaught-conjecture-counterexample/blob/d159d16aa19bf338d8ad556becfa7749d5c13bb8/LICENSE)).

## Builds on

- Mathlib, at [2e318fae](https://github.com/leanprover-community/mathlib4/tree/2e318faecff7d70d4e0cf8cc875104424a737355).
- `ComputableModelTheory` (https://github.com/cameronfreer/computable-model-theory) at `5d5f65ce`.
- `InfinitaryLogic` (https://github.com/cameronfreer/infinitary-logic) at `004f6381`.
- [TauCeti](../README.md) at `330da7fe`.

## Placement

Its Lake manifest requires `TauCeti`.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Logic and computation (17 of 87 imports, 18.3×), Topology (21 of 87 imports, 3.2×), Data structures (36 of 87 imports, 2.9×). *Proof depends on* lists 8 of the 15 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [cameronfreer/vaught-conjecture-counterexample at d159d16a](https://github.com/cameronfreer/vaught-conjecture-counterexample/tree/d159d16aa19bf338d8ad556becfa7749d5c13bb8)
