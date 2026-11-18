---
declaration: def
origin: cited
lean: BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph, BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph_fst, BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph_snd, BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph_symm_coe, BC4lean.ProperActions.OrbitCell.fixedSpace_nonempty_iff, BC4lean.ProperActions.OrbitCell.fixedSpace_isEmpty_of_cosets, BC4lean.ProperActions.OrbitCell.fixedSpace_isEmpty_of_parameter, BC4lean.ProperActions.InvariantSubset.inclusionMap
statement: formalized
proof: formalized
---

# Baum–Connes Conjecture — BC4lean

[ylsong1024/BC4lean](https://github.com/ylsong1024/BC4lean) at commit [a4e91f0c](https://github.com/ylsong1024/BC4lean/tree/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221), 2026-10-20.

> BC4lean is an open-source Lean formalization project developing the foundations for the **coefficient-free, reduced Baum–Connes conjecture for countable discrete groups**. All algebras and Hilbert spaces are complex.

*Quoted from [README.md](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/README.md), Apache-2.0.*

## Depends on

- [Subgroup](../../general-algebra/group-theory/part-01/subgroup.md)

## Proof depends on

- [Normal endomorphism](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/endomorphisms/normal-endomorphism.md)
- [Class formula](../../general-algebra/group-theory/part-01/class-formula.md)
- [Self-adjoint operator](../../analysis/hilbert-spaces/self-adjoint-operator.md)
- [Completeness](../uniform-notions/completeness.md)
- [Norm of a continuous linear map](../../analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Hahn-Banach theorem](../../analysis/normed-vector-spaces-banach-spaces/hahn-banach-theorem.md)
- [Normed vector space over a normed field](../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Group](../../general-algebra/group-theory/part-01/group.md)

## Main results

Its Lean names are 8 of the 92 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/OrbitCellFixedSpace.lean#L12) (def)
- [`BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph_fst`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/OrbitCellFixedSpace.lean#L32) (theorem)
- [`BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph_snd`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/OrbitCellFixedSpace.lean#L36) (theorem)
- [`BC4lean.ProperActions.OrbitCell.fixedSpaceHomeomorph_symm_coe`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/OrbitCellFixedSpace.lean#L40) (theorem)
- [`BC4lean.ProperActions.OrbitCell.fixedSpace_nonempty_iff`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/OrbitCellFixedSpace.lean#L45) (theorem)
- [`BC4lean.ProperActions.OrbitCell.fixedSpace_isEmpty_of_cosets`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/OrbitCellFixedSpace.lean#L55) (theorem)
- [`BC4lean.ProperActions.OrbitCell.fixedSpace_isEmpty_of_parameter`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/OrbitCellFixedSpace.lean#L60) (theorem)
- [`BC4lean.ProperActions.InvariantSubset.inclusionMap`](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/BC4lean/InvariantSubspaceMaps.lean#L9) (def)

No file its headlines import, directly or not (8 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 951 .lean files; its Lean libraries `BC4lean` hold 941, declaring 11,343 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/ylsong1024/BC4lean/blob/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221/LICENSE)).

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).

## Placement

Of its imports of Mathlib modules in an overview area, 103 of 389 are in Topology, 3.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Topology (103 of 389 imports, 3.5×), Analysis (190 of 389 imports, 1.8×), General algebra (51 of 389 imports, 0.4×). *Proof depends on* names 8 of the 57 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [ylsong1024/BC4lean at a4e91f0c](https://github.com/ylsong1024/BC4lean/tree/a4e91f0c0076cb2bdb5b2a56b31a4fb9eb6d1221)
