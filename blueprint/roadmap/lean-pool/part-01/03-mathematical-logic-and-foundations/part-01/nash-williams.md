---
declaration: theorem
origin: cited
lean: Front.IsFront.nash_williams, TwoBQO.wellQuasiOrdered
statement: formalized
proof: formalized
---

# Nash-Williams fronts and 2-better-quasi-orders

> Formalizes Nash-Williams fronts through their well-founded prefix trees and ordinal ranks, proves the finite-color Nash-Williams theorem, and derives the infinite Ramsey theorem for arbitrary finite arity. The order-theoretic development proves that 2-better-quasi-orders are well-quasi-orders and establishes closure under finite products, lexicographic sums, domination of subsets, and pointwise embedding of sequences. Throughout, TwoBQO r is the good-triple property of an arbitrary binary relation r (every pair-sequence has m < n < l with f(m,n) related to f(n,l)); it assumes no reflexivity or transitivity of r.

*Quoted from the card [LeanPool/projects/nash-williams.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nash-williams.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Front.IsFront.nash_williams`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliams/Combinatorics/Front/NashWilliams.html#Front.IsFront.nash_williams) (theorem; a main declaration), declared in [LeanPool/NashWilliams/Combinatorics/Front/NashWilliams.lean, line 227](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams/Combinatorics/Front/NashWilliams.lean#L227): “Every two-coloring of a Nash-Williams front on an infinite set has an infinite restriction whose front is monochromatic.”
- [`Front.IsFront.nash_williams_fin`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliams/Combinatorics/Front/NashWilliams.html#Front.IsFront.nash_williams_fin) (theorem), declared in [LeanPool/NashWilliams/Combinatorics/Front/NashWilliams.lean, line 273](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams/Combinatorics/Front/NashWilliams.lean#L273): “Every finite coloring of a Nash-Williams front has an infinite restriction whose front is monochromatic.”
- [`infinite_ramsey`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliams/Combinatorics/Ramsey/Infinite.html#infinite_ramsey) (theorem), declared in [LeanPool/NashWilliams/Combinatorics/Ramsey/Infinite.lean, line 59](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams/Combinatorics/Ramsey/Infinite.lean#L59): “Every finite coloring of the r-element subsets of an infinite set of natural numbers is constant on all r-element subsets of some infinite subset.”
- [`TwoBQO.wellQuasiOrdered`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliams/Order/TwoBQO.html#TwoBQO.wellQuasiOrdered) (theorem; a main declaration), declared in [LeanPool/NashWilliams/Order/TwoBQO.lean, line 125](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams/Order/TwoBQO.lean#L125): “Every 2-better-quasi-order is a well-quasi-order.”
- [`TwoBQO.lexSigmaQO`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliams/Order/TwoBQO.html#TwoBQO.lexSigmaQO) (theorem), declared in [LeanPool/NashWilliams/Order/TwoBQO.lean, line 365](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams/Order/TwoBQO.lean#L365): “The 2-BQO good-triple property is preserved by lexicographic sums: if the index relation and every fibre relation have it, so does the lexicographic-sum relation on the sigma type. This asserts nothing about reflexivity or transitivity of the sum; those are proved separately (LexSumRelQO.refl and LexSumRelQO.trans) under the corresponding order hypotheses on the index and fibres.”
- [`TwoBQO.embedForAll_wqo`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliams/Order/TwoBQO.html#TwoBQO.embedForAll_wqo) (theorem), declared in [LeanPool/NashWilliams/Order/TwoBQO.lean, line 509](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams/Order/TwoBQO.lean#L509): “If a preorder is a 2-better-quasi-order, then its infinite sequences are well-quasi-ordered by the relation admitting a strictly monotone reindexing along which corresponding terms are related.”

## Project

- Authors: Yann Pequignot.
- Source: *Towards better: A motivated introduction to better-quasi-orders* by Yann Pequignot, [doi:10.4171/EMSS/4-2-2](https://doi.org/10.4171/EMSS/4-2-2).
- Project repository: [yannpequignot/TwoBQO](https://github.com/yannpequignot/TwoBQO), at commit [8adea92d](https://github.com/yannpequignot/TwoBQO/tree/8adea92d7fa41700372ba16b9ff816dc7500579b).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 03E05, 05D10, 06A07.
- In Lean Pool: [LeanPool/NashWilliams](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams), from the card [LeanPool/projects/nash-williams.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nash-williams.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/nash-williams.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nash-williams.yaml)
- [Lean Pool at 2b205bf9: LeanPool/NashWilliams](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliams)
