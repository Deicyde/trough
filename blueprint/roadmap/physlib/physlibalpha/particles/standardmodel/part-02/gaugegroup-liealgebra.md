---
declaration: module
origin: cited
lean: StandardModel.gaugeAlgebraToMatrix, StandardModel.gaugeAlgebraToMatrix_mem, StandardModel.gaugeAlgebraHom, StandardModel.gaugeAlgebraHom_injective, StandardModel.gaugeAlgebraHom_surjective, StandardModel.gaugeAlgebraEquiv, StandardModel.gaugeAlgebraEquiv_coe, StandardModel.derivMat_su3Fund_gaugeAlgebraEquiv
statement: formalized
proof: formalized
---

# The gauge algebra as the Lie algebra of the global gauge group

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.LieAlgebra`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean): 13 declarations, 13 with a docstring.

> The gauge algebra of the Standard Model is the Lie algebra of its global gauge group.

## i. Overview

> The Lie algebra of the global gauge group `SU(3) × SU(2) × U(1)` consists of the block-diagonal
> matrices `diag(X₃, X₂, X₁)` with `X₃` and `X₂` traceless anti-hermitian and `X₁` an imaginary
> scalar, with the commutator as bracket. The gauge algebra `GaugeAlgebra` has the hermitian
> matrices `c₃`, `c₂` and the real scalar `c₁` instead, with the bracket carrying a factor of `i`.
> The two are identified through `c ↦ diag(i c₃, i c₂, i c₁)`, which is a Lie algebra
> isomorphism.

## ii. Key results

> - `StandardModel.gaugeAlgebraToMatrix` : the block-diagonal matrix `diag(i c₃, i c₂, i c₁)` of
>   an element `c` of the gauge algebra.
> - `StandardModel.gaugeAlgebraEquiv` : the Lie algebra isomorphism from `GaugeAlgebra` to the
>   Lie algebra of `globalGaugeGroup`.
> - `StandardModel.gaugeAlgebraEquiv_coe` : the underlying matrix of its value.
> - `StandardModel.derivMat_su3Fund_gaugeAlgebraEquiv`,
>   `StandardModel.derivMat_su2Fund_gaugeAlgebraEquiv`,
>   `StandardModel.hypercharge_exp_gaugeAlgebraEquiv` : the derivatives of the fundamental
>   representations and of the hypercharge, on the image of a gauge algebra element.
> - `StandardModel.adjointRep_gaugeAlgebraEquiv` : the adjoint action of the global gauge group
>   is the blockwise conjugation `GaugeAlgebra.adjointMap`.
> - `StandardModel.gaugeDualToLie` : a functional on the gauge algebra transported to one on the
>   Lie algebra of `globalGaugeGroup`.

## iv. References

> * None.

## A. The block-diagonal matrix of a gauge algebra element

> The real-linear map `c ↦ diag(i c₃, i c₂, i c₁)`, whose values are traceless anti-hermitian in
> the non-abelian blocks and imaginary in the abelian one.

**`StandardModel.gaugeAlgebraToMatrix`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L75).

> The block-diagonal matrix `diag(i c₃, i c₂, i c₁)` of an element `c` of the gauge algebra,
> with `c₃` and `c₂` hermitian traceless and `c₁` a real scalar.

```lean
noncomputable def gaugeAlgebraToMatrix : GaugeAlgebra →ₗ[ℝ] 𝕄
```

**`StandardModel.gaugeAlgebraToMatrix_mem`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L88).

> The block-diagonal matrix of a gauge algebra element lies in the Lie algebra of the global
> gauge group.

```lean
lemma gaugeAlgebraToMatrix_mem (c : GaugeAlgebra) :
    gaugeAlgebraToMatrix c ∈ globalGaugeGroup.lieAlgebra
```

## B. The Lie algebra homomorphism

> The factor of `i` in the bracket of `GaugeAlgebra` is what makes the map a Lie algebra
> homomorphism to the commutator bracket.

**`StandardModel.gaugeAlgebraHom`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L117).

> The Lie algebra homomorphism from the gauge algebra to the Lie algebra of the global gauge
> group, sending `c` to `diag(i c₃, i c₂, i c₁)`.

```lean
noncomputable def gaugeAlgebraHom : GaugeAlgebra →ₗ⁅ℝ⁆ globalGaugeGroup.lieSubalgebra
```

## C. The equivalence

**`StandardModel.gaugeAlgebraHom_injective`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L139).

> The homomorphism from the gauge algebra is injective.

```lean
lemma gaugeAlgebraHom_injective : Function.Injective gaugeAlgebraHom
```

**`StandardModel.gaugeAlgebraHom_surjective`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L153).

> Every element of the Lie algebra of the global gauge group is the image of an element of the
> gauge algebra. The `SU(3)` and `SU(2)` blocks are traceless and anti-hermitian, and the
> `U(1)` block is an imaginary scalar.

```lean
lemma gaugeAlgebraHom_surjective : Function.Surjective gaugeAlgebraHom
```

**`StandardModel.gaugeAlgebraEquiv`**, a def, [line 177](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L177).

> The Lie algebra isomorphism from the gauge algebra of the Standard Model to the Lie algebra
> of its global gauge group, sending `c` to `diag(i c₃, i c₂, i c₁)`.

```lean
noncomputable def gaugeAlgebraEquiv : GaugeAlgebra ≃ₗ⁅ℝ⁆ globalGaugeGroup.lieSubalgebra
```

**`StandardModel.gaugeAlgebraEquiv_coe`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L183).

> The underlying matrix of the image of `c` under `gaugeAlgebraEquiv` is
> `diag(i c₃, i c₂, i c₁)`.

```lean
lemma gaugeAlgebraEquiv_coe (c : GaugeAlgebra) :
    ((gaugeAlgebraEquiv c : globalGaugeGroup.lieSubalgebra) : 𝕄) =
      fromBlocks (Complex.I • c.toSU3Matrix) 0 0
        (fromBlocks (Complex.I • c.toSU2Matrix) 0 0
          (Complex.I • scalar (Fin 1) c.toU1Value))
```

## D. The fundamental representations and the hypercharge

> On the image of a gauge algebra element `c`, the derivatives of the fundamental representations
> are `i c₃` and `i c₂`, and that of the hypercharge is `i c₁`. The matter fields of the Standard
> Model read their infinitesimal actions off these.

**`StandardModel.derivMat_su3Fund_gaugeAlgebraEquiv`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L201).

> The Lie algebra element `gaugeAlgebraEquiv c` acts on the fundamental representation of the
> `SU(3)` factor by `i c₃`.

```lean
lemma derivMat_su3Fund_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    derivMat su3Fund (gaugeAlgebraEquiv c) = Complex.I • c.toSU3Matrix
```

**`StandardModel.derivMat_su2Fund_gaugeAlgebraEquiv`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L207).

> The Lie algebra element `gaugeAlgebraEquiv c` acts on the fundamental representation of the
> `SU(2)` factor by `i c₂`.

```lean
lemma derivMat_su2Fund_gaugeAlgebraEquiv (c : GaugeAlgebra) :
    derivMat su2Fund (gaugeAlgebraEquiv c) = Complex.I • c.toSU2Matrix
```

**`StandardModel.hypercharge_exp_gaugeAlgebraEquiv`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L213).

> The hypercharge of the exponential of `t` times the image of `c` is `exp (t i c₁)`, so the
> derivative of the hypercharge at `gaugeAlgebraEquiv c` is `i c₁`.

```lean
lemma hypercharge_exp_gaugeAlgebraEquiv (c : GaugeAlgebra) (t : ℝ)
    (g : globalGaugeGroup.group)
    (hg : ((g : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄) =
      NormedSpace.exp (t • ((gaugeAlgebraEquiv c : globalGaugeGroup.lieSubalgebra) : 𝕄))) :
    ((hypercharge g : ℂˣ) : ℂ) = Complex.exp (t * (Complex.I * c.toU1Value))
```

## E. The adjoint action

> The adjoint action of the global gauge group is blockwise conjugation on the gauge algebra, and
> functionals on the gauge algebra are transported to the Lie algebra with their dual action.

**`StandardModel.adjointRep_gaugeAlgebraEquiv`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L236).

> The adjoint action of the global gauge group on its Lie algebra, transported along
> `gaugeGroupEquiv` and `gaugeAlgebraEquiv`, is the blockwise conjugation
> `GaugeAlgebra.adjointMap`.

```lean
lemma adjointRep_gaugeAlgebraEquiv (g : GaugeGroupI) (a : GaugeAlgebra) :
    globalGaugeGroup.adjointRep (gaugeGroupEquiv g) (gaugeAlgebraEquiv a) =
      gaugeAlgebraEquiv (GaugeAlgebra.adjointMap g a)
```

**`StandardModel.dualMap_adjointRep_comp_symm`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L267).

> The dual of the adjoint action of the global gauge group on a functional of the form
> `φ ∘ gaugeAlgebraEquiv⁻¹` is the transport of the dual of `GaugeAlgebra.adjointMap`.

```lean
lemma dualMap_adjointRep_comp_symm (g : GaugeGroupI)
    (φ : Module.Dual ℝ GaugeAlgebra) :
    (globalGaugeGroup.adjointRep (gaugeGroupEquiv g)).dualMap
        (φ ∘ₗ (gaugeAlgebraEquiv.symm : globalGaugeGroup.lieSubalgebra →ₗ[ℝ] GaugeAlgebra)) =
      ((GaugeAlgebra.adjointMap g).dualMap φ) ∘ₗ
        (gaugeAlgebraEquiv.symm : globalGaugeGroup.lieSubalgebra →ₗ[ℝ] GaugeAlgebra)
```

**`StandardModel.gaugeDualToLie`**, an abbrev, [line 279](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean#L279).

> A functional on the gauge algebra `GaugeAlgebra`, transported along `gaugeAlgebraEquiv` to
> one on the Lie algebra of the global gauge group.

```lean
noncomputable abbrev gaugeDualToLie (φ : Module.Dual ℝ GaugeAlgebra) :
    Module.Dual ℝ globalGaugeGroup.lieSubalgebra
```

## Depends on

- [The gauge algebra of the Standard Model](../part-01/gaugealgebra-basic.md)
- [The Standard Model gauge group as a global gauge group](gaugegroup-globalgaugegroup.md)

## Proof depends on

- [The gauge jets of unitary gauge groups](../../../classicalfieldtheory/gaugetheory/part-02/globalgaugegroup-unitaryjet.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LieAlgebra.lean)
