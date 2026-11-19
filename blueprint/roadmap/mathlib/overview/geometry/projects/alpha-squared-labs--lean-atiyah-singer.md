---
declaration: module
origin: cited
lean: AtiyahSinger
statement: formalized
---

# Lean-Atiyah-Singer

*Lean formalization of the Atiyah–Singer index theorem*

[alpha-squared-labs/Lean-Atiyah-Singer](https://github.com/alpha-squared-labs/Lean-Atiyah-Singer) at commit [09fc7bab](https://github.com/alpha-squared-labs/Lean-Atiyah-Singer/tree/09fc7bab3f9ff606901bde4b5a5580470da63a70), 2026-11-06.

> This project formalizes the classical Atiyah–Singer index theorem and its cohomological and twisted spin Dirac formulations in Lean 4, using mathlib and a library of supporting results. The main proof follows the embedding and K-theory approach in Lawson and Michelsohn's *Spin Geometry*, with supplementary arguments from the references below.

*Quoted from [README.md](https://github.com/alpha-squared-labs/Lean-Atiyah-Singer/blob/09fc7bab3f9ff606901bde4b5a5580470da63a70/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Topological fiber bundle](../../topology/general-topology/part-01/topological-fiber-bundle.md)
- [Lie group](../differentiable-manifolds/part-01/lie-group.md)
- [Topological vector bundle](../../topology/general-topology/part-01/topological-vector-bundle.md)
- [Covariant derivatives](../smooth-vector-and-fiber-bundles/covariant-derivatives.md)
- [Smooth immersion](../differentiable-manifolds/part-01/smooth-immersion.md)
- [Product of manifolds](../differentiable-manifolds/part-01/product-of-manifolds.md)
- [Smooth embedding](../differentiable-manifolds/part-01/smooth-embedding.md)
- [Orthogonal group](../../../undergraduate/group-theory/classical-automorphism-groups/orthogonal-group.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`AtiyahSinger`](https://github.com/alpha-squared-labs/Lean-Atiyah-Singer/blob/09fc7bab3f9ff606901bde4b5a5580470da63a70/AtiyahSinger.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Comparator/Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 2,373 .lean files; its Lean libraries `AtiyahSinger`, `Statements`, `Challenge`, `Solution` hold 2,373, declaring 8,980 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/alpha-squared-labs/Lean-Atiyah-Singer/blob/09fc7bab3f9ff606901bde4b5a5580470da63a70/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 231 of 1421 are in Geometry, 6.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (231 of 1421 imports, 6.9×), Topology (274 of 1421 imports, 2.6×), Linear algebra (184 of 1421 imports, 2.2×). *Proof depends on* lists 8 of the 163 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [alpha-squared-labs/Lean-Atiyah-Singer at 09fc7bab](https://github.com/alpha-squared-labs/Lean-Atiyah-Singer/tree/09fc7bab3f9ff606901bde4b5a5580470da63a70)
