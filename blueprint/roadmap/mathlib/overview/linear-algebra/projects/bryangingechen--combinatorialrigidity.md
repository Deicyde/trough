---
declaration: theorem
origin: cited
lean: SimpleGraph.IsTight.not_isSparse_of_lt, SimpleGraph.IsLaman.exists_two_le_degree_le_three, SimpleGraph.Henneberg.typeII_isLaman, SimpleGraph.top_fin_four_minus_edge_isLaman, SimpleGraph.IsGenericallyRigidInj.mono, SimpleGraph.IsGenericallyRigid.iso, SimpleGraph.top_fin_two_isGenericallyRigid, SimpleGraph.IsGenericallyRigid.card_mul_le_two
statement: formalized
proof: formalized
---

# CombinatorialRigidity

[bryangingechen/CombinatorialRigidity](https://github.com/bryangingechen/CombinatorialRigidity) at commit [072e20b5](https://github.com/bryangingechen/CombinatorialRigidity/tree/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8), 2026-11-13.

> A Lean 4 / mathlib4 formalization of combinatorial rigidity theory. It began with **Laman's theorem** (Pollaczek-Geiringer 1927, Laman 1970): for `n ≥ 2`, a graph is generically rigid in the plane iff it contains a `(2, 3)`-tight spanning subgraph.

*Quoted from [README.md](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/README.md), Apache-2.0.*

## Depends on

- [Simple graph](../../combinatorics/graph-theory/simple-graph.md)

## Proof depends on

- [Vector subspace](../../../undergraduate/linear-algebra/fundamentals/vector-subspace.md)
- [Triple product](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/low-dimensions/triple-product.md)
- [Cross product](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/low-dimensions/cross-product.md)
- [Affine span](../../geometry/affine-and-euclidean-geometry/affine-span.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Rank of a set of vectors](../../../undergraduate/linear-algebra/finite-dimensional-vector-spaces/rank-of-a-set-of-vectors.md)
- [Dual vector space](../duality/dual-vector-space.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)

## Main results

Its Lean names are 8 of the 85 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`SimpleGraph.IsTight.not_isSparse_of_lt`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/Sparsity.lean#L307) (theorem)
- [`SimpleGraph.IsLaman.exists_two_le_degree_le_three`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/Laman.lean#L104) (theorem)
- [`SimpleGraph.Henneberg.typeII_isLaman`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/Henneberg.lean#L373) (theorem)
- [`SimpleGraph.top_fin_four_minus_edge_isLaman`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/HennebergReverse.lean#L235) (theorem)
- [`SimpleGraph.IsGenericallyRigidInj.mono`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/Framework.lean#L308) (theorem)
- [`SimpleGraph.IsGenericallyRigid.iso`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/Framework.lean#L232) (theorem)
- [`SimpleGraph.top_fin_two_isGenericallyRigid`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/Framework.lean#L377) (theorem)
- [`SimpleGraph.IsGenericallyRigid.card_mul_le_two`](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/CombinatorialRigidity/LamanTheorem.lean#L48) (theorem)

No file its headlines import, directly or not (26 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.36.0-rc1, Mathlib at [ba5499e0](https://github.com/leanprover-community/mathlib4/tree/ba5499e069f24171b4be2229dea365c897205f5e).
- 221 .lean files; its Lean libraries `CombinatorialRigidity` hold 197, declaring 3,226 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/bryangingechen/CombinatorialRigidity/blob/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8/LICENSE)).

## Builds on

- Mathlib, at [ba5499e0](https://github.com/leanprover-community/mathlib4/tree/ba5499e069f24171b4be2229dea365c897205f5e).
- `Matroid` (https://github.com/apnelson1/Matroid.git) at `8ece6307`.

## Placement

Of its imports of Mathlib modules in an overview area, 53 of 152 are in Linear algebra, 6.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (53 of 152 imports, 6.0×), Combinatorics (37 of 152 imports, 5.7×), Data structures (29 of 152 imports, 1.3×). *Proof depends on* names 8 of the 41 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [bryangingechen/CombinatorialRigidity at 072e20b5](https://github.com/bryangingechen/CombinatorialRigidity/tree/072e20b5a0b9ed41b7d0e018b93c49a47a9db8a8)
