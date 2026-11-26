---
declaration: module
origin: cited
lean: GlobalGaugeGroup.lieAlgebra, GlobalGaugeGroup.mem_lieAlgebra_iff, GlobalGaugeGroup.lieSubalgebra, GlobalGaugeGroup.mem_lieSubalgebra
statement: formalized
proof: formalized
---

# The Lie algebra of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LieAlgebra.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean): 9 declarations (5 instances with no name), 3 with a docstring.

> The generators of the one-parameter subgroups of a global gauge group.

## i. Overview

> The Lie algebra `𝔤` of a global gauge group `G ⊆ GL(κ, ℂ)` is determined by the group. It
> is the real subspace of matrices `X` whose one-parameter subgroup `t ↦ exp (t X)` lies in
> `G`, `Matrix.lieAlgebraOfIsClosed`. That this is a subspace closed under the commutator, and
> invariant under conjugation by `G`, is proved there. A finite group has zero Lie algebra. For
> a compact group inside the unitary group the generators `X` are anti-hermitian, and the
> hermitian generators of physics are `−i X`.
>
> The one-parameter subgroups of the generators are in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LieAlgebra.OneParameter`,
> and the adjoint action of `G` on `𝔤` is in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LieAlgebra.Adjoint`.

## ii. Key results

> - `GlobalGaugeGroup.lieAlgebra` : the Lie algebra of a global gauge group.
> - `GlobalGaugeGroup.lieSubalgebra` : the Lie algebra as a Lie subalgebra of matrices.

## iv. References

> * B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).

## A. The Lie algebra

**`GlobalGaugeGroup.lieAlgebra`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L65).

> The Lie algebra of a global gauge group, the generators of its one-parameter
> subgroups.

```lean
def lieAlgebra : Submodule ℝ (Matrix κ κ ℂ)
```

**`GlobalGaugeGroup.mem_lieAlgebra_iff`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L68).

```lean
lemma mem_lieAlgebra_iff (X : Matrix κ κ ℂ) : X ∈ G.lieAlgebra ↔
    ∀ t : ℝ, exp (t • X) ∈ Set.range fun g : G.group => (g.1 : Matrix κ κ ℂ)
```

## B. The Lie algebra as a Lie subalgebra

**`GlobalGaugeGroup.lieSubalgebra`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L78).

> The Lie algebra, as a Lie subalgebra of matrices under the commutator.

```lean
def lieSubalgebra : LieSubalgebra ℝ (Matrix κ κ ℂ)
```

**`GlobalGaugeGroup.mem_lieSubalgebra`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L85).

```lean
lemma mem_lieSubalgebra {X : Matrix κ κ ℂ} : X ∈ G.lieSubalgebra ↔ X ∈ G.lieAlgebra
```

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L87).

```lean
noncomputable instance : AddCommGroup G.lieSubalgebra
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L89).

```lean
noncomputable instance : Module ℝ G.lieSubalgebra
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L91).

```lean
noncomputable instance : LieRing G.lieSubalgebra
```

**An instance with no name**, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L93).

```lean
noncomputable instance : LieAlgebra ℝ G.lieSubalgebra
```

**An instance with no name**, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean#L96).

> The Lie algebra is finite-dimensional, as a subspace of the matrices.

```lean
instance : Module.Finite ℝ G.lieSubalgebra
```

## Depends on

- [Global gauge groups](globalgaugegroup-basic.md)
- [The Lie algebra of a closed group of matrices](../../../mathematics/part-02/formathlib/analysis-normed-algebra-matrixliealgebra.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Basic.lean)
