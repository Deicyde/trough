---
declaration: module
origin: cited
lean: Lorentz.toMatrix_rep_upL, Lorentz.toMatrix_rep_downL, Lorentz.toMatrix_rep_upR, Lorentz.toMatrix_rep_downR, Lorentz.toMatrix_rep_up_apply, Lorentz.toMatrix_rep_down_apply, Lorentz.inv_dagger, Lorentz.IsDaggerCompatible
statement: formalized
proof: formalized
---

# The colours of complex Lorentz tensors are closed under adjoints

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.AdjointClosed`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean): 14 declarations, 14 with a docstring.

## i. Overview

> A family of vectors in a representation `repLorentz` of `SL(2,ℂ)` on `B`, carrying Lorentz
> indices of colours `c`, is packaged as a linear map `f : ℂT(c) →ₗ[ℂ] B`, equivariant in the sense
> `complexLorentzTensor.IsEquivariant c repLorentz f`. The invariants in the range of such a map
> come from invariant tensors whenever the colours are closed under adjoints,
> `TensorSpecies.IsAdjointClosed`.
>
> For `SL(2,ℂ)` this follows from each colour being dagger compatible: in its basis, the matrix of
> `g†` is the conjugate transpose of the matrix of `g`. This holds for all six colours (B), so
> every list of colours is closed under adjoints, `complexLorentzTensor.isAdjointClosed`.

## ii. Key results

> - `Lorentz.IsDaggerCompatible` : the matrix of `g†` is the conjugate transpose of that of `g`.
> - `Lorentz.isDaggerCompatible` : every colour is dagger compatible.
> - `complexLorentzTensor.isAdjointClosed` : every list of colours is closed under adjoints.

## iv. References

> * None.

## A. The matrices of the colours

**`Lorentz.toMatrix_rep_upL`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L56).

> The matrix of `g` on the left-handed Weyl colour is `g`.

```lean
lemma toMatrix_rep_upL (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .upL) (complexLorentzTensor.basis .upL)
      (complexLorentzTensor.rep .upL g) = g.1
```

**`Lorentz.toMatrix_rep_downL`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L62).

> The matrix of `g` on the dual left-handed Weyl colour is `(g⁻¹)ᵀ`.

```lean
lemma toMatrix_rep_downL (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .downL) (complexLorentzTensor.basis .downL)
      (complexLorentzTensor.rep .downL g) = (g.1⁻¹)ᵀ
```

**`Lorentz.toMatrix_rep_upR`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L68).

> The matrix of `g` on the right-handed Weyl colour is the entrywise conjugate of `g`.

```lean
lemma toMatrix_rep_upR (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .upR) (complexLorentzTensor.basis .upR)
      (complexLorentzTensor.rep .upR g) = g.1.map star
```

**`Lorentz.toMatrix_rep_downR`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L74).

> The matrix of `g` on the dual right-handed Weyl colour is `(g⁻¹)ᴴ`.

```lean
lemma toMatrix_rep_downR (g : SL(2,ℂ)) :
    LinearMap.toMatrix (complexLorentzTensor.basis .downR) (complexLorentzTensor.basis .downR)
      (complexLorentzTensor.rep .downR g) = (g.1⁻¹)ᴴ
```

**`Lorentz.toMatrix_rep_up_apply`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L80).

> The matrix of `g` on the contravariant vector colour is the Lorentz matrix of `g`.

```lean
lemma toMatrix_rep_up_apply (g : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3) :
    LinearMap.toMatrix (complexLorentzTensor.basis .up) (complexLorentzTensor.basis .up)
      (complexLorentzTensor.rep .up g) μ ν
      = (((SL2C.toLorentzGroup g).1 μ ν : ℝ) : ℂ)
```

**`Lorentz.toMatrix_rep_down_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L91).

> The matrix of `g` on the covariant vector colour is the transpose of the inverse of the
> Lorentz matrix of `g`.

```lean
lemma toMatrix_rep_down_apply (g : SL(2,ℂ)) (μ ν : Fin 1 ⊕ Fin 3) :
    LinearMap.toMatrix (complexLorentzTensor.basis .down) (complexLorentzTensor.basis .down)
      (complexLorentzTensor.rep .down g) μ ν
      = (((SL2C.toLorentzGroup g)⁻¹.1 ν μ : ℝ) : ℂ)
```

**`Lorentz.inv_dagger`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L101).

> The inverse of `g†` is the dagger of the inverse of `g`.

```lean
lemma inv_dagger (g : SL(2,ℂ)) : (dagger g)⁻¹ = dagger g⁻¹
```

## B. Dagger-compatible colours

**`Lorentz.IsDaggerCompatible`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L114).

> A colour is dagger compatible when, in its basis, the matrix of `g†` is the conjugate
> transpose of the matrix of `g`.

```lean
def IsDaggerCompatible (k : complexLorentzTensor.Color) : Prop
```

**`Lorentz.isDaggerCompatible_of_weyl`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L122).

> The four Weyl colours are dagger compatible.

```lean
lemma isDaggerCompatible_of_weyl {k : complexLorentzTensor.Color}
    (hk : k = .upL ∨ k = .downL ∨ k = .upR ∨ k = .downR) : IsDaggerCompatible k
```

**`Lorentz.isDaggerCompatible_up`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L140).

> The contravariant vector colour is dagger compatible: the Lorentz matrix of `g†` is the
> transpose of that of `g`, and it is real.

```lean
lemma isDaggerCompatible_up : IsDaggerCompatible .up
```

**`Lorentz.isDaggerCompatible_down`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L148).

> The covariant vector colour is dagger compatible: the inverse Lorentz matrix of `g†` is the
> transpose of that of `g`, and it is real.

```lean
lemma isDaggerCompatible_down : IsDaggerCompatible .down
```

**`Lorentz.isDaggerCompatible`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L156).

> Every colour of complex Lorentz tensors is dagger compatible.

```lean
lemma isDaggerCompatible (k : complexLorentzTensor.Color) : IsDaggerCompatible k
```

**`Lorentz.isAdjointClosed_of_isDaggerCompatible`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L166).

> Colours that are all dagger compatible are closed under adjoints, with `g' = g†`.

```lean
lemma isAdjointClosed_of_isDaggerCompatible {n : ℕ} {c : Fin n → complexLorentzTensor.Color}
    (hc : ∀ i, IsDaggerCompatible (c i)) : complexLorentzTensor.IsAdjointClosed c
```

**`complexLorentzTensor.isAdjointClosed`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean#L174).

> Every list of colours of complex Lorentz tensors is closed under adjoints, with
> `g' = g†`.

```lean
lemma complexLorentzTensor.isAdjointClosed {n : ℕ} (c : Fin n → complexLorentzTensor.Color) :
    complexLorentzTensor.IsAdjointClosed c
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Invariant coefficient tensors on spacetime indices](invariants-basic.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Invariants/AdjointClosed.lean)
