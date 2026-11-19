---
declaration: module
origin: cited
lean: GlobalGaugeGroup, GlobalGaugeGroup.lieAlgebra, GlobalGaugeGroup.mem_lieAlgebra_iff, GlobalGaugeGroup.lieSubalgebra, GlobalGaugeGroup.mem_lieSubalgebra
statement: formalized
proof: formalized
---

# Global gauge groups

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean): 7 declarations (2 instances with no name), 3 with a docstring.

> A global gauge group as a closed group of invertible matrices, with its Lie algebra.

## i. Overview

> The global gauge group of a gauge theory is presented here as a closed subgroup `G` of the
> general linear group `GL(κ, ℂ)`. These are the matrix Lie groups. They include every compact
> Lie group, so every gauge group of the Standard Model and its extensions, as well as
> non-compact groups such as `Sp(2n, ℝ)`, `SO(p, q)`, `SL(n, ℝ)` and the Lorentz group,
> disconnected groups such as `O(n)`, and finite groups, whose Lie algebra is zero. A real
> group sits inside `GL(κ, ℂ)` as the real matrices it contains. Lie groups with no faithful
> finite-dimensional representation, such as the metaplectic group, are not covered.
>
> The Lie algebra `𝔤` is determined by the group: it is the real subspace of matrices `X`
> whose one-parameter subgroup `t ↦ exp (t X)` lies in `G`, `Matrix.lieAlgebraOfIsClosed`.
> That this is a subspace closed under the commutator, and invariant under conjugation by `G`,
> is proved there. For a compact group inside the unitary group the generators `X` are
> anti-hermitian, and the hermitian generators of physics are `−i X`.

## ii. Key results

> - `GlobalGaugeGroup` : a closed subgroup of a general linear group.
> - `GlobalGaugeGroup.lieAlgebra` : its Lie algebra.
> - `GlobalGaugeGroup.lieSubalgebra` : the Lie algebra as a Lie subalgebra of matrices.

## iv. References

> * yang-mills-group, *OpenAI-YM-20261028*, `PublicTheory.lean`, the structure `GaugeGroup`,
>   https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicTheory.lean#L22-L33

## A. The structure

**`GlobalGaugeGroup`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L63).

> A global gauge group: a closed subgroup of the general linear group `GL(κ, ℂ)`.

```lean
structure GlobalGaugeGroup (κ : Type) [Fintype κ] [DecidableEq κ] where
  /-- The group, as a subgroup of the general linear group. -/
  group : Subgroup (GeneralLinearGroup κ ℂ)
  /-- The group is closed in the general linear group. -/
  isClosed : IsClosed (group : Set (GeneralLinearGroup κ ℂ))
```

## B. The Lie algebra

**`GlobalGaugeGroup.lieAlgebra`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L80).

> The Lie algebra: the generators of the one-parameter subgroups of the group.

```lean
def lieAlgebra : Submodule ℝ (Matrix κ κ ℂ)
```

**`GlobalGaugeGroup.mem_lieAlgebra_iff`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L83).

```lean
lemma mem_lieAlgebra_iff (X : Matrix κ κ ℂ) : X ∈ G.lieAlgebra ↔
    ∀ t : ℝ, exp (t • X) ∈ Set.range fun g : G.group => (g.1 : Matrix κ κ ℂ)
```

**`GlobalGaugeGroup.lieSubalgebra`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L87).

> The Lie algebra, as a Lie subalgebra of matrices under the commutator.

```lean
def lieSubalgebra : LieSubalgebra ℝ (Matrix κ κ ℂ)
```

**`GlobalGaugeGroup.mem_lieSubalgebra`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L94).

```lean
lemma mem_lieSubalgebra {X : Matrix κ κ ℂ} : X ∈ G.lieSubalgebra ↔ X ∈ G.lieAlgebra
```

**An instance with no name**, [line 96](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L96).

```lean
noncomputable instance : LieRing G.lieSubalgebra
```

**An instance with no name**, [line 98](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L98).

```lean
noncomputable instance : LieAlgebra ℝ G.lieSubalgebra
```

## Depends on

- [The Lie algebra of a closed group of matrices](../../../mathematics/part-02/formathlib/analysis-normed-algebra-matrixliealgebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean)
