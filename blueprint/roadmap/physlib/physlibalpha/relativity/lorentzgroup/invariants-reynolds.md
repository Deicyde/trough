---
declaration: module
origin: cited
lean: Lorentz.toMatrix_rep_upL, Lorentz.toMatrix_rep_downL, Lorentz.toMatrix_rep_upR, Lorentz.toMatrix_rep_downR, Lorentz.toMatrix_rep_up_apply, Lorentz.toMatrix_rep_down_apply, Lorentz.continuous_toLorentzGroup_apply, Lorentz.continuous_toMatrix_rep
statement: formalized
proof: formalized
---

# Reynolds elements for complex Lorentz tensors

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.Reynolds`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean): 9 declarations, 9 with a docstring.

> The action of `SL(2, ℂ)` on complex Lorentz tensors is continuous, so the tensors have a Reynolds
> element.

## i. Overview

> A family of vectors in a representation `repLorentz` of `SL(2,ℂ)` on `B`, carrying Lorentz
> indices of colours `c`, is packaged as a linear map `f : ℂT(c) →ₗ[ℂ] B`, equivariant in the sense
> `complexLorentzTensor.IsEquivariant c repLorentz f`. The invariants in the range of such a map
> come from invariant tensors whenever the tensors have a Reynolds element,
> `TensorSpecies.HasReynolds`.
>
> In its basis the matrix of `g` on a colour is `g`, `(g⁻¹)ᵀ`, the entrywise conjugate of `g`,
> `(g⁻¹)ᴴ`, the Lorentz matrix of `g`, or the transpose of the inverse of that (A). So its entries
> depend continuously on `g` (B). The tensors with any list of colours are finite-dimensional, and
> the continuous action of `SL(2,ℂ)` on them has a Reynolds element by
> `Representation.exists_isReynolds_of_specialLinearGroup`, `complexLorentzTensor.hasReynolds` (C).

## ii. Key results

> - `Lorentz.continuous_toMatrix_rep` : the matrix entries of every colour depend continuously on
>   the element of `SL(2,ℂ)`.
> - `complexLorentzTensor.hasReynolds` : the tensors with any list of colours have a Reynolds
>   element.

## iv. References

> * None.

## A. The matrices of the colours

**`Lorentz.toMatrix_rep_upL`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L65).

> The matrix of `g` on the left-handed Weyl colour is `g`.

```lean
lemma toMatrix_rep_upL (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .upL) (complexLorentzTensor.basis .upL)
      (complexLorentzTensor.rep .upL g) = g.1
```

**`Lorentz.toMatrix_rep_downL`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L71).

> The matrix of `g` on the dual left-handed Weyl colour is `(g⁻¹)ᵀ`.

```lean
lemma toMatrix_rep_downL (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .downL) (complexLorentzTensor.basis .downL)
      (complexLorentzTensor.rep .downL g) = (g.1⁻¹)ᵀ
```

**`Lorentz.toMatrix_rep_upR`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L77).

> The matrix of `g` on the right-handed Weyl colour is the entrywise conjugate of `g`.

```lean
lemma toMatrix_rep_upR (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .upR) (complexLorentzTensor.basis .upR)
      (complexLorentzTensor.rep .upR g) = g.1.map star
```

**`Lorentz.toMatrix_rep_downR`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L83).

> The matrix of `g` on the dual right-handed Weyl colour is `(g⁻¹)ᴴ`.

```lean
lemma toMatrix_rep_downR (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .downR) (complexLorentzTensor.basis .downR)
      (complexLorentzTensor.rep .downR g) = (g.1⁻¹)ᴴ
```

**`Lorentz.toMatrix_rep_up_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L89).

> The matrix of `g` on the contravariant vector colour is the Lorentz matrix of `g`.

```lean
lemma toMatrix_rep_up_apply (g : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3) :
    LinearMap.toMatrix (complexLorentzTensor.basis .up) (complexLorentzTensor.basis .up)
      (complexLorentzTensor.rep .up g) μ ν
      = (((SL2C.toLorentzGroup g).1 μ ν : ℝ) : ℂ)
```

**`Lorentz.toMatrix_rep_down_apply`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L100).

> The matrix of `g` on the covariant vector colour is the transpose of the inverse of the
> Lorentz matrix of `g`.

```lean
lemma toMatrix_rep_down_apply (g : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3) :
    LinearMap.toMatrix (complexLorentzTensor.basis .down) (complexLorentzTensor.basis .down)
      (complexLorentzTensor.rep .down g) μ ν
      = (((SL2C.toLorentzGroup g)⁻¹.1 ν μ : ℝ) : ℂ)
```

## B. Continuity of the matrices

**`Lorentz.continuous_toLorentzGroup_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L117).

> The entries of the Lorentz matrix of `g` depend continuously on `g`, through the trace
> formula `L(g)_{i j} = ½ tr (σ'_i g σ'_j g†)`.

```lean
lemma continuous_toLorentzGroup_apply (i j : Fin 1 ⊕ Fin 3) :
    Continuous fun g : SL(2,ℂ) => (((SL2C.toLorentzGroup g).1 i j : ℝ) : ℂ)
```

**`Lorentz.continuous_toMatrix_rep`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L125).

> The entries of the matrix of `g` on every colour depend continuously on `g`.

```lean
lemma continuous_toMatrix_rep (k : complexLorentzTensor.Color) (x y : basisIdx k) :
    Continuous fun g : SL(2,ℂ) => LinearMap.toMatrix (complexLorentzTensor.basis k)
      (complexLorentzTensor.basis k) (complexLorentzTensor.rep k g) x y
```

## C. Reynolds elements

**`complexLorentzTensor.hasReynolds`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean#L155).

> The complex Lorentz tensors with any list of colours have a Reynolds element. They are
> finite-dimensional, and `SL(2,ℂ)` acts on them continuously.

```lean
lemma complexLorentzTensor.hasReynolds {n : ℕ} (c : Fin n → complexLorentzTensor.Color) :
    complexLorentzTensor.HasReynolds c
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [Reynolds elements for SL(2, ℂ)](../../classicalfieldtheory/gaugetheory/part-06/localfieldalgebra-realization-lorentz.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/Reynolds.lean)
