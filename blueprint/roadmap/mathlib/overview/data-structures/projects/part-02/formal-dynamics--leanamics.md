---
declaration: theorem
origin: cited
lean: Averaging.not_tendsto_of_colorable, Averaging.walkLambda_lt_one, Averaging.abs_avgIter_sub_walkStationary_le, Averaging.strong_reconstruction, Averaging.Opportunistic.oppRun_isSome_iff, Averaging.Opportunistic.oppRun_getD, Averaging.Opportunistic.sum_avgRun, Averaging.Opportunistic.meanStepMatrix_mulVec_cutVec
statement: formalized
proof: formalized
---

# Leanamics

[formal-dynamics/leanamics](https://github.com/formal-dynamics/leanamics) at commit [81fd0712](https://github.com/formal-dynamics/leanamics/tree/81fd0712a766bebfe6419a66bfa35f9c0f91e753), 2026-11-04.

> Lean 4 + Mathlib formalizations of classical results on opinion dynamics and related distributed processes. Each project is paired with a [leanblueprint](https://github.com/PatrickMassot/leanblueprint) connecting the paper proof to the Lean code statement-by-statement.

*Quoted from [README.md](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/README.md), MIT, Copyright (c) 2026 The Leanamics contributors.*

## Depends on

- [Limit of a map with respect to filters](../../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [List](../../list-like-structures/list.md)

## Proof depends on

- [Simple graph](../../../combinatorics/graph-theory/simple-graph.md)
- [Formula for the Number of Combinations](../../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Ring-valued matrix](../../../linear-algebra/matrices/ring-valued-matrix.md)
- [Finite set](../../sets/finite-set.md)
- [Logarithm](../../../analysis/special-functions/logarithm.md)
- [Real number](../../../general-algebra/numbers/real-number.md)
- [Exponential](../../../analysis/special-functions/exponential.md)
- [Filter](../../../topology/general-topology/part-01/filter.md)

## Main results

Its Lean names are 8 of the 20 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`Averaging.not_tendsto_of_colorable`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/Basic.lean#L503) (theorem)
- [`Averaging.walkLambda_lt_one`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/Rate.lean#L54) (theorem)
- [`Averaging.abs_avgIter_sub_walkStationary_le`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/Rate.lean#L61) (theorem)
- [`Averaging.strong_reconstruction`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/Reconstruction.lean#L123) (theorem)
- [`Averaging.Opportunistic.oppRun_isSome_iff`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/OpportunisticModel.lean#L98) (theorem)
- [`Averaging.Opportunistic.oppRun_getD`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/OpportunisticModel.lean#L104) (theorem)
- [`Averaging.Opportunistic.sum_avgRun`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/OpportunisticModel.lean#L114) (theorem)
- [`Averaging.Opportunistic.meanStepMatrix_mulVec_cutVec`](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/averaging/Averaging/OpportunisticClustered.lean#L703) (theorem)

No file its headlines import, directly or not (20 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.32.0, Mathlib at [2d8c533b](https://github.com/leanprover-community/mathlib4/tree/2d8c533bd0a0515caa32f18c0ab4485bd6229378).
- 383 .lean files; its Lean libraries `Averaging` hold 28, declaring 431 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: MIT ([LICENSE](https://github.com/formal-dynamics/leanamics/blob/81fd0712a766bebfe6419a66bfa35f9c0f91e753/LICENSE)).

## Builds on

- Mathlib, at [2d8c533b](https://github.com/leanprover-community/mathlib4/tree/2d8c533bd0a0515caa32f18c0ab4485bd6229378).
- `dynamics`.

## Placement

4 of the 11 Mathlib concepts its files name are in Data structures.

## Mathlib use

*Proof depends on* lists 8 of the 11 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [formal-dynamics/leanamics at 81fd0712](https://github.com/formal-dynamics/leanamics/tree/81fd0712a766bebfe6419a66bfa35f9c0f91e753)
