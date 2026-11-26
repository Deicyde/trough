---
declaration: module
origin: cited
lean: complexLorentzTensor.complexifiedFactor, complexLorentzTensor.complexifiedFactor_τ, complexLorentzTensor.complexifiedAction, complexLorentzTensor.complexifiedAction_apply, complexLorentzTensor.basis_repr_complexifiedAction, complexLorentzTensor.complexifiedAction_prodT, Lorentz.SL2C.toComplexified, Lorentz.SL2C.toComplexified_apply
statement: formalized
proof: formalized
---

# The complexified Lorentz group acting on Weyl tensors

The module `PhyslibAlpha.Relativity.Bispinors.ComplexifiedAction`, [PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean): 50 declarations, 48 with a docstring.

> The complex Lorentz tensors with Weyl colours carry an action of `SL(2, ℂ) × SL(2, ℂ)` with the
> same invariant tensors as `SL(2, ℂ)`.

## i. Overview

> The complexified Lorentz group `SL(2, ℂ) × SL(2, ℂ)` acts on the complex Lorentz tensors with Weyl
> colours, `(M, N)` acting on each undotted index by `M`, on each dotted index by `N`, and on their
> duals by the inverse transposes (`complexifiedAction`, A.1). Restricted along the complexification
> `M ↦ (M, M̄)` it is the action of `SL(2, ℂ)` (A.2).
>
> On undotted indices followed by dotted ones, each factor acts on its own indices only. The
> Reynolds elements of the two factors, applied one after the other, fix an invariant and send every
> product of tensors to a product of invariant tensors, so the invariants of the complexified action
> are spanned by the products of an invariant tensor of the undotted indices and one of the dotted
> indices (B).
>
> The invariant tensors of the two actions are the same (C). One direction is the restriction. For
> the other, take a real square-zero `G`, such as `E` or `F`, and the line `1 + z G` in `SL(2, ℂ)`
> (C.1). Along `t ↦ 1 + c₀ t G`, for real `t`, the matrices of the undotted colours are holomorphic
> in `c₀ t` and those of the dotted colours antiholomorphic (C.2). So the derivative of the
> components of an invariant tensor is `c₀` times the action of `G` on its undotted indices plus `c̄₀`
> times that on its dotted ones, and it vanishes. Taking `c₀ = 1` and `c₀ = i` shows that `G` kills
> the invariant tensor on its undotted indices alone. The components along `s ↦ (1 + s z G, 1)` then
> have derivative zero at the identity, hence everywhere by the group law, so the invariant tensor is
> fixed by `(1 + z G, 1)` (C.3). These elements generate `SL(2, ℂ) × 1`, and
> `(1, N) = (N̄, N) (N̄⁻¹, 1)` (C.4). With B, the invariant tensors with undotted indices followed by
> dotted ones are spanned by products of invariant tensors of each chirality,
> `invariants_append_eq_map₂_prodT`.
>
> Two consequences follow here. A left- and a right-handed Weyl index carry no invariant tensor, the
> element `-1` negating a single Weyl index, and with them neither do the ranges of equivariant maps
> out of such tensors (D). The Pauli matrices change `n` four-vector indices into `n` left- and `n`
> right-handed Weyl indices, `pauliTensorMap`, injectively and equivariantly. For odd `n` the
> invariants on the Weyl side are products of invariants of `n` left-handed indices, of which there
> are none, so an odd number of four-vector indices carries no invariant tensor (E). The bispinor
> classifications of `PhyslibAlpha.Relativity.Bispinors.MetricPairing` and the classification of
> four four-vector indices in `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.ContractionTensor`
> build on the same results.

## ii. Key results

> - `complexLorentzTensor.complexifiedAction` : the action of `SL(2, ℂ) × SL(2, ℂ)` on the complex
>   Lorentz tensors with Weyl colours.
> - `Lorentz.SL2C.toComplexified` : the complexification `M ↦ (M, M̄)`.
> - `complexLorentzTensor.complexifiedAction_comp_toComplexified` : restricted along it, the
>   complexified action is the action of `SL(2, ℂ)`.
> - `complexLorentzTensor.invariants_complexifiedAction_append` : on undotted indices followed by
>   dotted ones, the complexified invariants are spanned by products of invariants.
> - `complexLorentzTensor.invariants_complexifiedAction` : the two actions have the same invariant
>   tensors.
> - `complexLorentzTensor.invariants_append_eq_map₂_prodT` : the invariant tensors with undotted
>   indices followed by dotted ones are spanned by products of invariants.
> - `complexLorentzTensor.invariants_upL_upR_eq_bot` : a left- and a right-handed Weyl index carry
>   no invariant tensor.
> - `Lorentz.reducesInvariantsTo_bot_leftRight` : nor does the range of an equivariant map out of
>   them or out of their duals.
> - `complexLorentzTensor.pauliTensorMap` : the Pauli change of indices on tensors.
> - `complexLorentzTensor.invariants_up_pow_eq_bot_of_odd` : an odd number of four-vector indices
>   carries no invariant tensor.
> - `Lorentz.ComplexVector.reducesInvariantsTo_bot_of_odd` : nor does the range of an equivariant
>   map out of them.

## iv. References

> * R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That*.

## A. The complexified action

### A.1. The action of `SL(2, ℂ) × SL(2, ℂ)`

**`complexLorentzTensor.complexifiedFactor`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L124).

> The factor of the complexified Lorentz group `SL(2, ℂ) × SL(2, ℂ)` under which a colour
> transforms. The undotted colours `upL` and `downL` transform under the first factor `M`. The
> dotted colours `upR` and `downR`, whose representations are conjugate, transform under the
> conjugate of the second factor `N`, so that a dotted index transforms under `N` itself. The
> vector colours, which carry an index of each kind, are not part of the construction, and are put
> under the first factor only so that every colour has one.

```lean
def complexifiedFactor : Color → SL(2,ℂ) × SL(2,ℂ) →* SL(2,ℂ)
```

**`complexLorentzTensor.complexifiedFactor_τ`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L130).

> A colour and its dual transform under the same factor.

```lean
lemma complexifiedFactor_τ (k : Color) :
    complexifiedFactor (complexLorentzTensor.τ k) = complexifiedFactor k
```

**`complexLorentzTensor.complexifiedAction`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L137).

> The complexified Lorentz group `SL(2, ℂ) × SL(2, ℂ)` acting on the complex Lorentz tensors
> with Weyl colours: `(M, N)` acts on an undotted index by `M`, on a dotted index by `N`, and on
> their duals by the inverse transposes.

```lean
noncomputable def complexifiedAction {n : ℕ} (c : Fin n → Color) :
    Representation ℂ (SL(2,ℂ) × SL(2,ℂ)) ℂT(c)
```

**`complexLorentzTensor.complexifiedAction_apply`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L144).

> An element of `SL(2, ℂ) × SL(2, ℂ)` acts on the index `i` through the factor of its colour.

```lean
lemma complexifiedAction_apply (g : SL(2,ℂ) × SL(2,ℂ)) :
    complexifiedAction c g =
      PiTensorProduct.map fun i => complexLorentzTensor.rep (c i) (complexifiedFactor (c i) g)
```

**`complexLorentzTensor.basis_repr_complexifiedAction`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L150).

> The components of `g • t` under the complexified action.

```lean
lemma basis_repr_complexifiedAction (g : SL(2,ℂ) × SL(2,ℂ)) (t : ℂT(c))
    (φ : ComponentIdx (S := complexLorentzTensor) c) :
    (Tensor.basis c).repr (complexifiedAction c g t) φ = ∑ ψ, (∏ i, LinearMap.toMatrix
      (complexLorentzTensor.basis (c i)) (complexLorentzTensor.basis (c i))
      (complexLorentzTensor.rep (c i) (complexifiedFactor (c i) g)) (φ i) (ψ i)) *
      (Tensor.basis c).repr t ψ
```

**`complexLorentzTensor.complexifiedAction_prodT`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L160).

> The complexified action acts on a product of tensors factor by factor.

```lean
lemma complexifiedAction_prodT {m : ℕ} {c1 : Fin m → Color} (g : SL(2,ℂ) × SL(2,ℂ)) (t : ℂT(c))
    (t1 : ℂT(c1)) :
    complexifiedAction (Fin.append c c1) g (prodT t t1) =
      prodT (complexifiedAction c g t) (complexifiedAction c1 g t1)
```

### A.2. The restriction to `SL(2, ℂ)`

**`Lorentz.SL2C.toComplexified`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L179).

> The complexification `M ↦ (M, M̄)` of `SL(2, ℂ)` into the complexified Lorentz group
> `SL(2, ℂ) × SL(2, ℂ)`, with `M̄` the entrywise conjugate of `M`.

```lean
def toComplexified : SL(2,ℂ) →* SL(2,ℂ) × SL(2,ℂ)
```

**`Lorentz.SL2C.toComplexified_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L183).

> The complexification of `M` is `(M, M̄)`.

```lean
lemma toComplexified_apply (M : SL(2,ℂ)) :
    toComplexified M = (M, SpecialLinearGroup.map (starRingEnd ℂ) M)
```

**`Lorentz.SL2C.map_starRingEnd_map_starRingEnd`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L187).

> Conjugating an element of `SL(2, ℂ)` twice gives it back.

```lean
lemma map_starRingEnd_map_starRingEnd (M : SL(2,ℂ)) :
    SpecialLinearGroup.map (starRingEnd ℂ) (SpecialLinearGroup.map (starRingEnd ℂ) M) = M
```

**`complexLorentzTensor.complexifiedFactor_toComplexified`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L201).

> Each colour transforms under `M` when restricted along `M ↦ (M, M̄)`.

```lean
lemma complexifiedFactor_toComplexified (k : Color) (M : SL(2,ℂ)) :
    complexifiedFactor k (toComplexified M) = M
```

**`complexLorentzTensor.complexifiedAction_toComplexified`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L206).

> Restricted along `M ↦ (M, M̄)`, the complexified action is the action of `SL(2, ℂ)`.

```lean
lemma complexifiedAction_toComplexified (M : SL(2,ℂ)) :
    complexifiedAction c (toComplexified M) = complexLorentzTensor.tensorRep c M
```

**`complexLorentzTensor.complexifiedAction_comp_toComplexified`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L213).

> Restricted along `M ↦ (M, M̄)`, the complexified action is the action of `SL(2, ℂ)`.

```lean
lemma complexifiedAction_comp_toComplexified :
    (complexifiedAction c).comp toComplexified = complexLorentzTensor.tensorRep c
```

## B. Undotted indices followed by dotted ones

**`complexLorentzTensor.complexifiedAction_eq_tensorRep_fst`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L226).

> On undotted colours the complexified action of `(M, N)` is the action of `M`.

```lean
lemma complexifiedAction_eq_tensorRep_fst (hL : ∀ i, cL i = .upL ∨ cL i = .downL)
    (g : SL(2,ℂ) × SL(2,ℂ)) :
    complexifiedAction cL g = complexLorentzTensor.tensorRep cL g.1
```

**`complexLorentzTensor.complexifiedAction_eq_tensorRep_snd`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L235).

> On dotted colours the complexified action of `(M, N)` is the action of `N̄`, under which a
> dotted index transforms by `N`.

```lean
lemma complexifiedAction_eq_tensorRep_snd (hR : ∀ i, cR i = .upR ∨ cR i = .downR)
    (g : SL(2,ℂ) × SL(2,ℂ)) :
    complexifiedAction cR g =
      complexLorentzTensor.tensorRep cR (SpecialLinearGroup.map (starRingEnd ℂ) g.2)
```

**`complexLorentzTensor.complexifiedAction_append_prodT`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L245).

> The complexified action on a product of a tensor with undotted indices and one with dotted
> indices.

```lean
lemma complexifiedAction_append_prodT (hL : ∀ i, cL i = .upL ∨ cL i = .downL)
    (hR : ∀ i, cR i = .upR ∨ cR i = .downR) (g : SL(2,ℂ) × SL(2,ℂ)) (x : ℂT(cL)) (y : ℂT(cR)) :
    complexifiedAction (Fin.append cL cR) g (prodT x y) =
      prodT (complexLorentzTensor.tensorRep cL g.1 x)
        (complexLorentzTensor.tensorRep cR (SpecialLinearGroup.map (starRingEnd ℂ) g.2) y)
```

**`complexLorentzTensor.invariants_complexifiedAction_append`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L257).

> The invariants of the complexified action on undotted indices followed by dotted ones are
> spanned by the products of an invariant tensor of the undotted indices and one of the dotted
> indices. The Reynolds elements of the two factors, applied one after the other, fix an
> invariant and send every product of tensors to a product of invariant tensors.

```lean
lemma invariants_complexifiedAction_append (hL : ∀ i, cL i = .upL ∨ cL i = .downL)
    (hR : ∀ i, cR i = .upR ∨ cR i = .downR) :
    (complexifiedAction (Fin.append cL cR)).invariants =
      Submodule.map₂ (prodT (S := complexLorentzTensor))
        (complexLorentzTensor.tensorRep cL).invariants
        (complexLorentzTensor.tensorRep cR).invariants
```

## C. The invariants of the two actions agree

### C.1. The unipotent lines

> A square-zero matrix `G` with `det (1 + z G) = 1`, such as `E` or `F`, gives the line
> `z ↦ 1 + z G` in `SL(2, ℂ)`, on which multiplication adds the parameters.

**`Lorentz.SL2C.inv_one_add_smul`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L324).

> For a square-zero matrix `G`, the inverse of `1 + z G` is `1 - z G`.

```lean
lemma inv_one_add_smul (hGG : G * G = 0) (z : ℂ) : (1 + z • G)⁻¹ = 1 + (-z) • G
```

**`Lorentz.SL2C.one_add_smul_mul_one_add_smul`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L328).

> For a square-zero matrix `G`, multiplying `1 + a G` and `1 + b G` adds the parameters.

```lean
lemma one_add_smul_mul_one_add_smul (hGG : G * G = 0) (a b : ℂ) :
    (1 + a • G) * (1 + b • G) = 1 + (a + b) • G
```

**`Lorentz.SL2C.unipotentLine`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L334).

> The element `1 + z G` of `SL(2, ℂ)`, for a matrix `G` with `det (1 + z G) = 1` for every
> `z`, such as `E = !![0, 1; 0, 0]` or `F = !![0, 0; 1, 0]`.

```lean
def unipotentLine (hG : ∀ z : ℂ, (1 + z • G).det = 1) (z : ℂ) : SL(2,ℂ)
```

**`Lorentz.SL2C.coe_unipotentLine`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L339).

```lean
lemma coe_unipotentLine (z : ℂ) : (unipotentLine hG z : Matrix (Fin 2) (Fin 2) ℂ) = 1 + z • G
```

**`Lorentz.SL2C.unipotentLine_zero`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L343).

```lean
lemma unipotentLine_zero : unipotentLine hG 0 = 1
```

**`Lorentz.SL2C.unipotentLine_add`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L347).

> For a square-zero `G`, multiplication on the line `z ↦ 1 + z G` adds the parameters.

```lean
lemma unipotentLine_add (hGG : G * G = 0) (a b : ℂ) :
    unipotentLine hG (a + b) = unipotentLine hG a * unipotentLine hG b
```

### C.2. The derivatives of the colours

> Along `t ↦ 1 + c₀ t G`, for real `t` and real `G`, the matrix of an undotted colour is holomorphic
> in `c₀ t` and that of a dotted colour antiholomorphic, so its derivative at the identity is `c₀`
> times an undotted generator plus `c̄₀` times a dotted one. Along `t ↦ (1 + c₀ t G, 1)` the dotted
> colours do not move.

**`complexLorentzTensor.undottedGenerator`**, a def, [line 379](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L379).

> The derivative at the identity of the matrices of `t ↦ 1 + t G` on the undotted colours,
> `G` on `upL` and `-Gᵀ` on `downL`, and zero on the other colours.

```lean
def undottedGenerator (G : Matrix (Fin 2) (Fin 2) ℂ) : (k : Color) → basisIdx k → basisIdx k → ℂ
```

**`complexLorentzTensor.dottedGenerator`**, a def, [line 386](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L386).

> The derivative at the identity of the matrices of `t ↦ 1 + t G`, for real `G`, on the dotted
> colours, `G` on `upR` and `-Gᵀ` on `downR`, and zero on the other colours.

```lean
def dottedGenerator (G : Matrix (Fin 2) (Fin 2) ℂ) : (k : Color) → basisIdx k → basisIdx k → ℂ
```

**`complexLorentzTensor.mul_eq_mul_add_star_mul_zero`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L392).

> The derivative on `upL`, written against the two generators.

```lean
lemma mul_eq_mul_add_star_mul_zero (c₀ x : ℂ) : c₀ * x = c₀ * x + star c₀ * 0
```

**`complexLorentzTensor.neg_mul_eq_mul_neg_add_star_mul_zero`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L395).

> The derivative on `downL`, written against the two generators.

```lean
lemma neg_mul_eq_mul_neg_add_star_mul_zero (c₀ x : ℂ) : -c₀ * x = c₀ * -x + star c₀ * 0
```

**`complexLorentzTensor.star_mul_eq_mul_zero_add_star_mul`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L399).

> The derivative on `upR`, written against the two generators.

```lean
lemma star_mul_eq_mul_zero_add_star_mul {x : ℂ} (hx : star x = x) (c₀ : ℂ) :
    star (c₀ * x) = c₀ * 0 + star c₀ * x
```

**`complexLorentzTensor.star_neg_mul_eq_mul_zero_add_star_mul_neg`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L405).

> The derivative on `downR`, written against the two generators.

```lean
lemma star_neg_mul_eq_mul_zero_add_star_mul_neg {x : ℂ} (hx : star x = x) (c₀ : ℂ) :
    star (-c₀ * x) = c₀ * 0 + star c₀ * -x
```

**`complexLorentzTensor.toMatrix_rep_one_add_smul_zero`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L415).

> At the identity of the line `t ↦ 1 + c₀ t G` the matrix of every colour is the unit
> matrix.

```lean
lemma toMatrix_rep_one_add_smul_zero (k : Color) (c₀ : ℂ) (p q : basisIdx k) :
    LinearMap.toMatrix (complexLorentzTensor.basis k) (complexLorentzTensor.basis k)
      (complexLorentzTensor.rep k (unipotentLine hG (c₀ * ((0 : ℝ) : ℂ)))) p q =
      if p = q then 1 else 0
```

**`complexLorentzTensor.toMatrix_rep_complexifiedFactor_zero`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L424).

> At the identity of the line `t ↦ (1 + c₀ t G, 1)` the matrix of every colour under the
> complexified action is the unit matrix.

```lean
lemma toMatrix_rep_complexifiedFactor_zero (k : Color) (c₀ : ℂ) (p q : basisIdx k) :
    LinearMap.toMatrix (complexLorentzTensor.basis k) (complexLorentzTensor.basis k)
      (complexLorentzTensor.rep k
        (complexifiedFactor k (unipotentLine hG (c₀ * ((0 : ℝ) : ℂ)), 1))) p q =
      if p = q then 1 else 0
```

**`complexLorentzTensor.hasDerivAt_toMatrix_rep_one_add_smul`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L438).

> Along the line `t ↦ 1 + c₀ t G` of `SL(2, ℂ)`, for a real square-zero `G`, the matrix of a
> Weyl colour has derivative `c₀` times its undotted generator plus `c̄₀` times its dotted
> generator at the identity.

```lean
lemma hasDerivAt_toMatrix_rep_one_add_smul {k : Color} (hk : k ≠ .up ∧ k ≠ .down) (c₀ : ℂ)
    (p q : basisIdx k) :
    HasDerivAt (fun t : ℝ => LinearMap.toMatrix (complexLorentzTensor.basis k)
      (complexLorentzTensor.basis k) (complexLorentzTensor.rep k (unipotentLine hG (c₀ * t))) p q)
      (c₀ * undottedGenerator G k p q + star c₀ * dottedGenerator G k p q) 0
```

**`complexLorentzTensor.hasDerivAt_toMatrix_rep_complexifiedFactor`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L472).

> Along the line `t ↦ (1 + c₀ t G, 1)` of the complexified Lorentz group, the matrix of a Weyl
> colour under the complexified action has derivative `c₀` times its undotted generator at the
> identity: the dotted colours transform under the second factor, which stays at the
> identity.

```lean
lemma hasDerivAt_toMatrix_rep_complexifiedFactor {k : Color} (hk : k ≠ .up ∧ k ≠ .down)
    (c₀ : ℂ) (p q : basisIdx k) :
    HasDerivAt (fun t : ℝ => LinearMap.toMatrix (complexLorentzTensor.basis k)
      (complexLorentzTensor.basis k)
      (complexLorentzTensor.rep k (complexifiedFactor k (unipotentLine hG (c₀ * t), 1))) p q)
      (c₀ * undottedGenerator G k p q) 0
```

### C.3. The derivative argument

**`complexLorentzTensor.sum_undottedGenerator_mul_repr_eq_zero`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L511).

> An invariant tensor with Weyl colours is killed by the undotted generator acting on its
> undotted indices, one at a time. Along the line `t ↦ 1 + c₀ t G` its components are constant,
> and their derivative is `c₀` times this action plus `c̄₀` times that on the dotted indices.
> Taking `c₀ = 1` and `c₀ = i` separates the two.

```lean
lemma sum_undottedGenerator_mul_repr_eq_zero {t : ℂT(c)}
    (ht : t ∈ (complexLorentzTensor.tensorRep c).invariants)
    (φ : ComponentIdx (S := complexLorentzTensor) c) :
    ∑ s, ∑ q, undottedGenerator G (c s) (φ s) q *
      (Tensor.basis c).repr t (Function.update φ s q) = 0
```

**`complexLorentzTensor.complexifiedAction_one_add_smul_one`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L552).

> An invariant tensor with Weyl colours is fixed by `(1 + z G, 1)` under the complexified
> action. Along `s ↦ (1 + s z G, 1)` the derivative of its components at the identity is `z` times
> the undotted generator acting on them, which vanishes, so by the group law they are constant.

```lean
lemma complexifiedAction_one_add_smul_one {t : ℂT(c)}
    (ht : t ∈ (complexLorentzTensor.tensorRep c).invariants) (z : ℂ) :
    complexifiedAction c (unipotentLine hG z, 1) t = t
```

### C.4. The invariants

> `SL(2, ℂ)` is generated by the unipotent elements `1 + z E` and `1 + z F`, so an invariant tensor
> with Weyl colours is fixed by `(M, 1)` for every `M`. It is fixed by `(M, M̄)`, being invariant,
> and so by `(1, N) = (N̄, N) (N̄⁻¹, 1)` for every `N` as well.

**`complexLorentzTensor.complexifiedAction_mk_one_apply`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L592).

> An invariant tensor with Weyl colours is fixed by `(M, 1)` under the complexified action.

```lean
lemma complexifiedAction_mk_one_apply (hc : ∀ i, c i ≠ .up ∧ c i ≠ .down) {t : ℂT(c)}
    (ht : t ∈ (complexLorentzTensor.tensorRep c).invariants) (M : SL(2,ℂ)) :
    complexifiedAction c (M, 1) t = t
```

**`complexLorentzTensor.invariants_complexifiedAction`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L612).

> The invariant tensors with Weyl colours are the same for `SL(2, ℂ)` and for the complexified
> Lorentz group `SL(2, ℂ) × SL(2, ℂ)`.

```lean
lemma invariants_complexifiedAction (hc : ∀ i, c i ≠ .up ∧ c i ≠ .down) :
    (complexifiedAction c).invariants = (complexLorentzTensor.tensorRep c).invariants
```

**`complexLorentzTensor.invariants_append_eq_map₂_prodT`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L630).

> The invariant tensors with undotted indices followed by dotted ones are spanned by the
> products of an invariant tensor of the undotted indices and one of the dotted indices.

```lean
lemma invariants_append_eq_map₂_prodT (hL : ∀ i, cL i = .upL ∨ cL i = .downL)
    (hR : ∀ i, cR i = .upR ∨ cR i = .downR) :
    (complexLorentzTensor.tensorRep (Fin.append cL cR)).invariants =
      Submodule.map₂ (prodT (S := complexLorentzTensor))
        (complexLorentzTensor.tensorRep cL).invariants
        (complexLorentzTensor.tensorRep cR).invariants
```

## D. A left- and a right-handed Weyl index

### D.1. The invariant tensors

> A tensor with a left- and a right-handed Weyl index is, by C, a combination of products of an
> invariant tensor with one left-handed index and one with one right-handed index. The element `-1`
> negates a single Weyl index, so there are none.

**`complexLorentzTensor.invariants_upL_upR_eq_bot`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L656).

> The only invariant tensor with a left- and a right-handed Weyl index is zero.

```lean
lemma invariants_upL_upR_eq_bot :
    (complexLorentzTensor.tensorRep ![.upL, .upR]).invariants = ⊥
```

### D.2. The reduction to zero

> The dual colours `![.downL, .downR]` are the two indices of `![.upL, .upR]` dualised in turn, so
> they carry no invariant tensor but zero either (`invariants_tensorRep_eq_bot_of_dual`).

**`Lorentz.reducesInvariantsTo_bot_leftRight`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L682).

> The invariants of the range of an equivariant map out of the tensors with a left- and a
> right-handed Weyl index, or with their duals, reduce to `⊥`. A Lorentz invariant of
> `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable submodule, lies in `S`.

```lean
lemma reducesInvariantsTo_bot_leftRight {k k' : complexLorentzTensor.Color}
    (hk : (k = .upL ∧ k' = .upR) ∨ (k = .downL ∧ k' = .downR)) {B : Type*} [AddCommGroup B]
    [Module ℂ B] {repLorentz : Representation ℂ SL(2,ℂ) B} {f : ℂT[k, k'] →ₗ[ℂ] B}
    (hf : complexLorentzTensor.IsEquivariant ![k, k'] repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f) ⊥
```

### D.3. Peeling the pair spans off a Lorentz-stable submodule

> An equivariant map out of `ℂT[.downL, .downR]` carries no invariant, so the span of its
> components, here the join of the lines through them, reduces to `⊥`. Each such span is stable under
> the Lorentz group, so `ReducesInvariantsTo.biSup` combines the reductions over a finite family of
> them, and a whole join is discarded from a Lorentz-stable submodule.

**`Lorentz.mem_of_lorentz_invariant_biSup_dualLeftRightWeyl_span`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L713).

> A finite join of the spans of families with a dual left- and a dual right-handed Weyl index
> carries no Lorentz invariant modulo a Lorentz-stable submodule. Such a family has no invariant,
> so each span reduces to `⊥`, and `ReducesInvariantsTo.biSup` combines the reductions. A Lorentz
> invariant of the join together with `S` lies in `S`.

```lean
lemma mem_of_lorentz_invariant_biSup_dualLeftRightWeyl_span {ι : Type} [DecidableEq ι]
    {T : ι → Fin 2 × Fin 2 → B} (hT : ∀ i, complexLorentzTensor.IsEquivariant ![.downL, .downR]
      repLorentz (liftComponents (T i ∘ pairIdx)))
    (S : Submodule ℂ B) (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) (s : Finset ι)
    {x : B} (hx : x ∈ (⨆ i ∈ s, ⨆ l, ℂ ∙ T i l) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

**`Lorentz.mem_of_lorentz_invariant_iSup_dualLeftRightWeyl_span`**, a lemma, [line 729](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L729).

> The version of `mem_of_lorentz_invariant_biSup_dualLeftRightWeyl_span` joining over a
> whole finite index type.

```lean
lemma mem_of_lorentz_invariant_iSup_dualLeftRightWeyl_span {ι : Type} [Fintype ι]
    [DecidableEq ι] {T : ι → Fin 2 × Fin 2 → B}
    (hT : ∀ i, complexLorentzTensor.IsEquivariant ![.downL, .downR] repLorentz
      (liftComponents (T i ∘ pairIdx))) (S : Submodule ℂ B)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : B}
    (hx : x ∈ (⨆ i, ⨆ l, ℂ ∙ T i l) ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## E. Four-vector indices through the Pauli matrices

> The Pauli matrices change each of `n` four-vector indices into a bispinor index, a left- and a
> right-handed Weyl index (`Lorentz.pauliTransform`). Listing the `n` left-handed indices first and
> then the `n` right-handed ones, this is an injective equivariant map `pauliTensorMap n` from the
> tensors with `n` four-vector indices into the tensors with colours
> `Fin.append (fun _ => .upL) (fun _ => .upR)` (E.1). By C the invariants of the latter are products
> of invariants with `n` left-handed and with `n` right-handed indices. For odd `n` there are none,
> the element `-1` negating an odd number of Weyl indices, and so the tensors with an odd number of
> four-vector indices carry no invariant but zero (E.2).

### E.1. The Pauli change of indices on tensors

**`complexLorentzTensor.bispinorIdx`**, a def, [line 768](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L768).

> The component indices of a tensor with `n` left-handed Weyl indices followed by `n`
> right-handed ones, as `n` bispinor indices, the `s`-th left-handed index paired with the `s`-th
> right-handed one.

```lean
noncomputable def bispinorIdx (n : ℕ) : ComponentIdx (S := complexLorentzTensor)
    (Fin.append (fun _ : Fin n => Color.upL) (fun _ : Fin n => Color.upR)) ≃
      (Fin n → Fin 2 × Fin 2)
```

**`complexLorentzTensor.toMatrix_rep_basisIdxCongr`**, a lemma, [line 775](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L775).

> The matrix entry of a colour, transported along an equality of colours.

```lean
lemma toMatrix_rep_basisIdxCongr {k k' : Color} (h : k = k') (g : SL(2,ℂ)) (x y : basisIdx k) :
    LinearMap.toMatrix (complexLorentzTensor.basis k) (complexLorentzTensor.basis k)
      (complexLorentzTensor.rep k g) x y =
    LinearMap.toMatrix (complexLorentzTensor.basis k') (complexLorentzTensor.basis k')
      (complexLorentzTensor.rep k' g) (basisIdxCongr h x) (basisIdxCongr h y)
```

**`complexLorentzTensor.prod_bispinorMatrix_bispinorIdx`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L785).

> On `n` bispinor indices, the product of the matrix entries of `g` over the `2 n` Weyl indices
> is the product of the entries of the bispinor matrix of `g`.

```lean
lemma prod_bispinorMatrix_bispinorIdx (n : ℕ) (g : SL(2,ℂ))
    (φ ψ : ComponentIdx (S := complexLorentzTensor)
      (Fin.append (fun _ : Fin n => Color.upL) (fun _ : Fin n => Color.upR))) :
    ∏ s, bispinorMatrix g (bispinorIdx n φ s) (bispinorIdx n ψ s) =
      ∏ i, LinearMap.toMatrix
        (complexLorentzTensor.basis (Fin.append (fun _ : Fin n => Color.upL) (fun _ => .upR) i))
        (complexLorentzTensor.basis (Fin.append (fun _ : Fin n => Color.upL) (fun _ => .upR) i))
        (complexLorentzTensor.rep (Fin.append (fun _ : Fin n => Color.upL) (fun _ => .upR) i) g)
        (φ i) (ψ i)
```

**`complexLorentzTensor.pauliTensorMap`**, a def, [line 804](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L804).

> The change of every four-vector index of a tensor into a bispinor index by the covariant
> Pauli matrices, `μ ↦ (σ_μ)_{αα̇}`, landing in the tensors with the left-handed Weyl indices of
> the bispinor indices followed by their right-handed ones.

```lean
noncomputable def pauliTensorMap (n : ℕ) : ℂT(fun _ : Fin n => Color.up) →ₗ[ℂ]
    ℂT(Fin.append (fun _ : Fin n => Color.upL) (fun _ : Fin n => Color.upR))
```

**`complexLorentzTensor.pauliTensorMap_smul`**, a lemma, [line 810](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L810).

> The Pauli change of indices commutes with `SL(2, ℂ)`.

```lean
lemma pauliTensorMap_smul (n : ℕ) (g : SL(2,ℂ)) (t : ℂT(fun _ : Fin n => Color.up)) :
    pauliTensorMap n (g • t) = g • pauliTensorMap n t
```

**`complexLorentzTensor.pauliTensorMap_injective`**, a lemma, [line 820](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L820).

> The Pauli change of indices is injective.

```lean
lemma pauliTensorMap_injective (n : ℕ) : Function.Injective (pauliTensorMap n)
```

**`complexLorentzTensor.pauliTensorMap_mem_invariants`**, a lemma, [line 825](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L825).

> The Pauli change of indices maps invariant tensors to invariant tensors.

```lean
lemma pauliTensorMap_mem_invariants {n : ℕ} {t : ℂT(fun _ : Fin n => Color.up)}
    (ht : t ∈ (complexLorentzTensor.tensorRep (fun _ : Fin n => Color.up)).invariants) :
    pauliTensorMap n t ∈ (complexLorentzTensor.tensorRep
      (Fin.append (fun _ : Fin n => Color.upL) (fun _ : Fin n => Color.upR))).invariants
```

### E.2. An odd number of four-vector indices

**`complexLorentzTensor.invariants_up_pow_eq_bot_of_odd`**, a lemma, [line 843](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L843).

> There are no invariant tensors with an odd number of four-vector indices but zero. The Pauli
> change of indices sends them injectively to invariant tensors with `n` left- and `n`
> right-handed Weyl indices, products of invariants with `n` left-handed indices, of which there
> are none for odd `n`, the element `-1` negating them.

```lean
lemma invariants_up_pow_eq_bot_of_odd {n : ℕ} (hn : Odd n) :
    (complexLorentzTensor.tensorRep (fun _ : Fin n => Color.up)).invariants = ⊥
```

**`Lorentz.ComplexVector.reducesInvariantsTo_bot_of_odd`**, a lemma, [line 864](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean#L864).

> The range of an equivariant map out of the tensors with an odd number of four-vector indices
> reduces to `⊥`. A Lorentz invariant of `LinearMap.range f ⊔ S`, for `S` a Lorentz-stable
> submodule, lies in `S`.

```lean
lemma ComplexVector.reducesInvariantsTo_bot_of_odd {B : Type*} [AddCommGroup B]
    [Module ℂ B] {repLorentz : Representation ℂ SL(2,ℂ) B} {n : ℕ} (hn : Odd n)
    {f : ℂT(fun _ : Fin n => Color.up) →ₗ[ℂ] B}
    (hf : complexLorentzTensor.IsEquivariant (fun _ : Fin n => .up) repLorentz f) :
    ReducesInvariantsTo (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f) ⊥
```

## Depends on

- [The action of `SL(2, ℂ)` on bispinor indices](bispinormatrix.md)
- [Invariant coefficient tensors of the complex vector representation](../tensors/complextensor-vector-invariantcoeff.md)

## Proof depends on

- [The metric pairings of four Weyl indices](../fermions/weyl-metricpairing.md)
- [The eigenspaces of the centre of `SL(2,ℂ)`](../lorentzgroup/invariants-centreeigenspace.md)

## Sources

- [PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/ComplexifiedAction.lean)
