---
declaration: theorem
origin: cited
lean: LeanDag.ViewPace.commits_recur_local, LeanDag.dos_resistance, LeanDag.ViewPace.exists_honest_floor, LeanDag.PaceCore.viewAt_ids, LeanDag.ViewPace.heldOf_inj, LeanDag.ViewPace.dos_resistance_of_pace, LeanDag.Barnacle.Agreement.holds, LeanDag.Barnacle.Progress.holds
statement: formalized
proof: formalized
---

# lean-dag

[gdanezis/lean-dag](https://github.com/gdanezis/lean-dag) at commit [48aa36cc](https://github.com/gdanezis/lean-dag/tree/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa), 2026-11-13.

> A Lean 4 + Mathlib formalization of uncertified DAG consensus in the style of Mysticeti: the DAG itself, the commit rule, and machine-checked safety and liveness — together with further developments built on the same foundation, each in its own module consuming the core read-only.

*Quoted from [README.md](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/README.md), MIT, Copyright (c) 2026 George Danezis (University College London).*

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)

## Proof depends on

- [Ackermann function](../../logic-and-computation/computability/ackermann-function.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [List](../../data-structures/list-like-structures/list.md)
- [Sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/sigma-algebra.md)
- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Filter](../../topology/general-topology/part-01/filter.md)
- [Events](../../../undergraduate/probability-theory/definitions-of-a-probability-space/events.md)
- [Set](../../data-structures/sets/set.md)

## Main results

Its Lean names are 8 of the 17 theorems its README names in code:

- [`LeanDag.ViewPace.commits_recur_local`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/Mysticeti/ViewPace.lean#L534) (theorem)
- [`LeanDag.dos_resistance`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/DoS/Novelty.lean#L729) (theorem)
- [`LeanDag.ViewPace.exists_honest_floor`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/Mysticeti/ViewPace.lean#L661) (theorem)
- [`LeanDag.PaceCore.viewAt_ids`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/Mysticeti/ViewPace.lean#L261) (theorem)
- [`LeanDag.ViewPace.heldOf_inj`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/Mysticeti/PaceDelivery.lean#L57) (theorem)
- [`LeanDag.ViewPace.dos_resistance_of_pace`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/Mysticeti/PaceDelivery.lean#L151) (theorem)
- [`LeanDag.Barnacle.Agreement.holds`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/Barnacle/Agreement/Proof.lean#L16) (theorem)
- [`LeanDag.Barnacle.Progress.holds`](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LeanDag/Barnacle/Progress/Proof.lean#L17) (theorem)

No file its headlines import, directly or not (72 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.32.2, Mathlib at [905b9581](https://github.com/leanprover-community/mathlib4/tree/905b95818eb32af7874a58b427f50c1711a5e96c).
- 806 .lean files; its Lean libraries `LeanDag`, `LeanDagTest` hold 804, declaring 6,878 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/gdanezis/lean-dag/blob/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa/LICENSE)).

## Builds on

- Mathlib, at [905b9581](https://github.com/leanprover-community/mathlib4/tree/905b95818eb32af7874a58b427f50c1711a5e96c).

## Placement

Of its imports of Mathlib modules in an overview area, 19 of 124 are in Combinatorics, 3.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Combinatorics (19 of 124 imports, 3.6×), Data structures (55 of 124 imports, 3.1×), Topology (17 of 124 imports, 1.8×). *Proof depends on* lists 8 of the 10 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [gdanezis/lean-dag at 48aa36cc](https://github.com/gdanezis/lean-dag/tree/48aa36cc90afdf41b5cd64b92ebd5d2676a0c8fa)
