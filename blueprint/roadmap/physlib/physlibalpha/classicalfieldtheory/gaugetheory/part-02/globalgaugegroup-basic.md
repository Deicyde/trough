---
declaration: module
origin: cited
lean: GlobalGaugeGroup, GlobalGaugeGroup.ofSubmonoid, GlobalGaugeGroup.mem_ofSubmonoid_iff, GlobalGaugeGroup.mem_ofSubmonoid_iff_of_star_mem
statement: formalized
proof: formalized
---

# Global gauge groups

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean): 5 declarations (1 instance with no name), 4 with a docstring.

> A global gauge group as a closed group of invertible matrices.

## i. Overview

> The global gauge group of a gauge theory is presented here as a closed subgroup `G` of the
> general linear group `GL(κ, ℂ)`. These are the matrix Lie groups. They include every compact
> Lie group, so every gauge group of the Standard Model and its extensions, as well as
> non-compact groups such as `Sp(2n, ℝ)`, `SO(p, q)`, `SL(n, ℝ)` and the Lorentz group,
> disconnected groups such as `O(n)`, and finite groups. A real group sits inside `GL(κ, ℂ)` as
> the real matrices it contains. Lie groups with no faithful finite-dimensional
> representation, such as the metaplectic group, are not covered.
>
> Most groups of physical interest are cut out of the matrices by closed conditions, such as
> unitarity, a determinant or an invariant bilinear form. Such conditions define a closed
> submonoid of matrices, and its invertible elements whose inverses also satisfy the conditions
> form a global gauge group, `GlobalGaugeGroup.ofSubmonoid`. The special cases `U(1)`, `SU(n)`,
> `SO(n)` and `Sp(n)` are built this way in the files `SO.lean`, `SU.lean`, `Sp.lean` and `U1.lean`.
>
> The Lie algebra of a global gauge group is in the `LieAlgebra` directory.

## ii. Key results

> - `GlobalGaugeGroup` : a closed subgroup of a general linear group.
> - `GlobalGaugeGroup.ofSubmonoid` : the global gauge group of the invertible elements of a
>   closed submonoid of matrices.

## iv. References

> * yang-mills-group, *OpenAI-YM-20261028*, `PublicTheory.lean`, the structure `GaugeGroup`,
>   https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicTheory.lean#L22-L33

## A. The structure

**`GlobalGaugeGroup`**, a structure, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L66).

> A global gauge group, a closed subgroup of the general linear group `GL(κ, ℂ)`.

```lean
structure GlobalGaugeGroup (κ : Type) [Fintype κ] [DecidableEq κ] where
  /-- The group, as a subgroup of the general linear group. -/
  group : Subgroup (GeneralLinearGroup κ ℂ)
  /-- The group is closed in the general linear group. -/
  isClosed : IsClosed (group : Set (GeneralLinearGroup κ ℂ))
```

## B. Global gauge groups from closed submonoids of matrices

**`GlobalGaugeGroup.ofSubmonoid`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L84).

> The global gauge group of a closed submonoid `S` of matrices. Its elements are the
> invertible matrices which lie in `S` together with their inverses.

```lean
def ofSubmonoid (S : Submonoid (Matrix κ κ ℂ)) (hS : IsClosed (S : Set (Matrix κ κ ℂ))) :
    GlobalGaugeGroup κ
```

**`GlobalGaugeGroup.mem_ofSubmonoid_iff`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L89).

```lean
lemma mem_ofSubmonoid_iff {S : Submonoid (Matrix κ κ ℂ)} {hS : IsClosed (S : Set (Matrix κ κ ℂ))}
    {g : GeneralLinearGroup κ ℂ} :
    g ∈ (ofSubmonoid S hS).group ↔ (g : Matrix κ κ ℂ) ∈ S ∧ (↑g⁻¹ : Matrix κ κ ℂ) ∈ S
```

**`GlobalGaugeGroup.mem_ofSubmonoid_iff_of_star_mem`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L97).

> For a submonoid of unitary matrices closed under the conjugate transpose, an invertible
> matrix lies in its global gauge group exactly when it lies in the submonoid, since its
> inverse is then its conjugate transpose.

```lean
lemma mem_ofSubmonoid_iff_of_star_mem {S : Submonoid (Matrix κ κ ℂ)}
    {hS : IsClosed (S : Set (Matrix κ κ ℂ))} (hU : S ≤ unitaryGroup κ ℂ)
    (hstar : ∀ A ∈ S, star A ∈ S) {g : GeneralLinearGroup κ ℂ} :
    g ∈ (ofSubmonoid S hS).group ↔ (g : Matrix κ κ ℂ) ∈ S
```

**An instance with no name**, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean#L107).

> The group structure of a global gauge group, recorded directly so that instance search
> does not pass through the units of the matrices.

```lean
instance (G : GlobalGaugeGroup κ) : Group G.group
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Basic.lean)
