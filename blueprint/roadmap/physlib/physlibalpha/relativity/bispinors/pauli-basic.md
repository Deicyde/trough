---
declaration: module
origin: cited
lean: Lorentz.ComplexVector.contrToLeftRightLinear, Lorentz.ComplexVector.contrToLeftRightLinear_basis, Lorentz.ComplexVector.contrToLeftRightLinear_rep, Lorentz.ComplexVector.contrToLeftRight, Lorentz.ComplexVector.contrToLeftRight_basis, Lorentz.ComplexVector.contrToLeftRight_surjective, Lorentz.ComplexVector.lTensor_contrToLeftRight_metricVal, Lorentz.ComplexVector.contrToLeftRight_bijective
statement: formalized
proof: formalized
---

# The Pauli tensor is the unique invariant

The module `PhyslibAlpha.Relativity.Bispinors.Pauli.Basic`, [PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean): 24 declarations, 24 with a docstring.

> Up to scale, the Pauli tensor `σ^{μ α α̇}` is the only invariant with a vector, a left-handed and a
> right-handed Weyl index.

## i. Overview

> The covariant Pauli matrices `σ_μ = η_{μμ} σ^μ` move under `M ∈ SL(2, ℂ)` as a covariant vector,
> `M σ_μ Mᴴ = Σ_ν Λ_{ν μ} σ_ν`, so `e_μ ↦ σ_μ` is an equivariant linear map `contrToLeftRight`
> from the complex four-vectors to `LeftHandedWeyl ⊗ RightHandedWeyl` (A). By the Fierz completeness
> relation the `σ_μ` span all `2 × 2` matrices, so this map is onto. Applied to the second index of
> the metric `η^{μν}` it gives the Pauli tensor `pauliVal`, the two lowerings cancelling (B).
>
> The map `contrToLeftRight` is onto between spaces of dimension four, so it is bijective, and so
> is `id ⊗ contrToLeftRight`. It carries the invariants of `ComplexVector ⊗ ComplexVector`, the line
> through the metric, onto those of `ComplexVector ⊗ (LeftHandedWeyl ⊗ RightHandedWeyl)`, which are
> therefore the line through `σ` (C). The tensor product is tensorial, so section D restates this
> for the tensor `toTensor pauliVal`, relabelled as the tensor `pauliTensor` of
> `ℂT[.up, .upL, .upR]`, the line through which is the invariant tensors with a four-vector and a
> left-right Weyl pair of indices, and for its dual-Weyl form in `ℂT[.up, .downR, .downL]`. It then
> applies this to equivariant maps out of these tensors, the shape of the fermion kinetic term.

## ii. Key results

> - `Lorentz.ComplexVector.contrToLeftRight` : the equivariant map `e_μ ↦ σ_μ`.
> - `Lorentz.ComplexVector.lTensor_contrToLeftRight_metricVal` : it carries the metric to the Pauli
>   tensor.
> - `Lorentz.ComplexVector.invariants_tprod_eq_span_pauliVal` : the invariants are the line through
>   the Pauli tensor.
> - `Lorentz.pauliTensor` : the Pauli tensor as a tensor of `ℂT[.up, .upL, .upR]`.
> - `complexLorentzTensor.invariants_up_upL_upR_eq_span_pauli` : the invariant tensors with the
>   indices of the Pauli tensor are the line through `pauliTensor`.
> - `Lorentz.invariantReductionToPauliVal`, `Lorentz.invariantReductionToPauliValDualWeyl` : the
>   invariants of the range of an equivariant map reduce to the image of the Pauli tensor.
> - `Lorentz.isEquivariant_upDownRDownL_mul` : a one-index family times a once-derived one of the
>   other chirality is an equivariant map out of `ℂT[.up, .downR, .downL]`.

## iv. References

> The Pauli tensor `ComplexVector.pauliVal` and the intertwining map `ComplexVector.pauli` are in
> `Physlib.Relativity.Bispinors.Pauli.Basic`, where sections A to C are written to move. The
> uniqueness of the metric of the complex four-vectors is in
> `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Metrics.Pre`. The tensorial structures of the
> three factors are in `PhyslibAlpha.Relativity.Tensors.ComplexTensor.Vector.Tensorial` and
> `PhyslibAlpha.Relativity.Fermions.Weyl.Tensorial`.

## A. The Pauli matrices as an equivariant map

**`Lorentz.ComplexVector.contrToLeftRightLinear`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L90).

> The covariant Pauli matrices as a map `e_μ ↦ σ_μ` from complex four-vectors to a left- and a
> right-handed Weyl index.

```lean
def contrToLeftRightLinear : ComplexVector →ₗ[ℂ] LeftHandedWeyl ⊗[ℂ] RightHandedWeyl
```

**`Lorentz.ComplexVector.contrToLeftRightLinear_basis`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L94).

> The basis vector `e_μ` is sent to the lowered Pauli matrix `σ_μ`.

```lean
lemma contrToLeftRightLinear_basis (μ : Fin 1 ⊕ Fin 3) :
    contrToLeftRightLinear (ComplexVector.basis μ) = leftRightToMatrix.symm (pauliLower μ)
```

**`Lorentz.ComplexVector.contrToLeftRightLinear_rep`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L99).

> The covariant Pauli matrices move as a covariant vector, so `e_μ ↦ σ_μ` is equivariant.

```lean
lemma contrToLeftRightLinear_rep (M : SL(2,ℂ)) (v : ComplexVector) :
    contrToLeftRightLinear (ComplexVector.SL2CRep M v) =
      TensorProduct.map (LeftHandedWeyl.rep M) (RightHandedWeyl.rep M)
        (contrToLeftRightLinear v)
```

**`Lorentz.ComplexVector.contrToLeftRight`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L121).

> The covariant Pauli matrices as an intertwining map `e_μ ↦ σ_μ` from complex four-vectors to
> a left- and a right-handed Weyl index.

```lean
def contrToLeftRight :
    ComplexVector.SL2CRep.IntertwiningMap (LeftHandedWeyl.rep.tprod RightHandedWeyl.rep)
```

**`Lorentz.ComplexVector.contrToLeftRight_basis`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L126).

> The basis vector `e_μ` is sent to the lowered Pauli matrix `σ_μ`.

```lean
lemma contrToLeftRight_basis (μ : Fin 1 ⊕ Fin 3) :
    contrToLeftRight (ComplexVector.basis μ) = leftRightToMatrix.symm (pauliLower μ)
```

**`Lorentz.ComplexVector.contrToLeftRight_surjective`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L132).

> The covariant Pauli matrices span the `2 × 2` matrices, by the Fierz completeness relation,
> so `e_μ ↦ σ_μ` is onto.

```lean
lemma contrToLeftRight_surjective : Function.Surjective contrToLeftRight
```

## B. The metric goes to the Pauli tensor

**`Lorentz.ComplexVector.lTensor_contrToLeftRight_metricVal`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L163).

> Applying `e_μ ↦ σ_μ` to the second index of the metric `η^{μν}` gives the Pauli tensor. The
> lowering in `σ_μ` cancels the metric.

```lean
lemma lTensor_contrToLeftRight_metricVal :
    contrToLeftRight.lTensor ComplexVector.SL2CRep ComplexVector.metricVal =
      ComplexVector.pauliVal
```

## C. The Pauli tensor is the unique invariant

**`Lorentz.ComplexVector.contrToLeftRight_bijective`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L178).

> The map `e_μ ↦ σ_μ` is bijective: it is onto, between spaces of dimension four.

```lean
lemma contrToLeftRight_bijective : Function.Bijective contrToLeftRight
```

**`Lorentz.ComplexVector.invariants_tprod_eq_span_pauliVal`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L195).

> The `SL(2,ℂ)`-invariants of `ComplexVector ⊗ (LeftHandedWeyl ⊗ RightHandedWeyl)` are the line
> through the Pauli tensor `σ^{μ α α̇}`. The bijection `id ⊗ contrToLeftRight` carries the
> invariants of `ComplexVector ⊗ ComplexVector`, the line through the metric, onto them.

```lean
lemma invariants_tprod_eq_span_pauliVal :
    (ComplexVector.SL2CRep.tprod (LeftHandedWeyl.rep.tprod RightHandedWeyl.rep)).invariants =
      ℂ ∙ ComplexVector.pauliVal
```

## D. The Pauli tensor as a complex Lorentz tensor

> Complex four-vectors and Weyl fermions are tensorial, so
> `ComplexVector ⊗ (LeftHandedWeyl ⊗ RightHandedWeyl)` is tensorial through
> `TensorSpecies.Tensorial.prod`. Its tensors carry the indices
> `Fin.append ![.up] (Fin.append ![.upL] ![.upR])`, and the Pauli tensor is the tensor
> `toTensor pauliVal`. The equivalence `toTensor` carries the action of `SL(2, ℂ)` on the tensor
> product to the action on tensors, so the invariant tensors are the line through
> `toTensor pauliVal`. Relabelling the colours as the plain list `![.up, .upL, .upR]`
> (`isReindexing_append_three`), the invariant tensors of `ℂT[.up, .upL, .upR]` are the line
> through the relabelled tensor `pauliTensor`. For an equivariant map `f` out of these tensors every
> Lorentz invariant in the range of `f` is then a multiple of `f pauliTensor`, modulo a
> Lorentz-stable submodule, `invariantReductionToPauliVal` (D.1).
>
> The Standard Model's fermion symbols are `Module.Dual`-valued, so their spinor indices are dual
> Weyl indices, and a family of them is an equivariant map out of `ℂT[.up, .downR, .downL]`.
> Dualising both Weyl indices, `dualWeylMap`, is an equivariant surjection onto these tensors, so
> every invariant in the range of such a map `f` is a multiple of
> `f (dualWeylMap pauliTensor)`, the image of the Pauli tensor with dual Weyl indices (D.2).
> A family indexed by a four-vector, a dual left-handed and a dual right-handed Weyl index is
> relabelled by `dualIndexEquiv`, and its map is equivariant when it obeys the transformation law
> of these indices (D.3). A one-index Weyl family times a once-derived one of the other chirality
> is such a family, the shape of the fermion kinetic term (D.4).

### D.1. The invariant tensors

**`Lorentz.ComplexVector.toTensor_SL2CRep_tprod`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L250).

> The equivalence `toTensor` carries the action of `SL(2, ℂ)` on
> `ComplexVector ⊗ (LeftHandedWeyl ⊗ RightHandedWeyl)` to the action on tensors.

```lean
lemma ComplexVector.toTensor_SL2CRep_tprod (g : SL(2,ℂ))
    (x : ComplexVector ⊗[ℂ] (LeftHandedWeyl ⊗[ℂ] RightHandedWeyl)) :
    toTensor ((ComplexVector.SL2CRep.tprod (LeftHandedWeyl.rep.tprod RightHandedWeyl.rep)) g x)
      = g • toTensor x
```

**`Lorentz.pauliTensor`**, a def, [line 267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L267).

> The Pauli tensor `σ^{μ α α̇}` as a tensor of `ℂT[.up, .upL, .upR]`, the tensor
> `toTensor pauliVal` with its colours `Fin.append ![.up] (Fin.append ![.upL] ![.upR])` relabelled
> as the plain list.

```lean
noncomputable def pauliTensor : ℂT[.up, .upL, .upR]
```

**`complexLorentzTensor.invariants_up_upL_upR_eq_span_pauli`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L274).

> The invariant tensors with a four-vector index and a left-right Weyl pair are the line
> through the Pauli tensor. The equivalence `toTensor` carries the invariants of the tensor
> product, the line through `pauliVal`, onto the invariant tensors of the colours of the
> tensorial structure, and relabelling the colours carries these onto those of the plain list.

```lean
lemma _root_.complexLorentzTensor.invariants_up_upL_upR_eq_span_pauli :
    (complexLorentzTensor.tensorRep ![.up, .upL, .upR]).invariants = ℂ ∙ pauliTensor
```

**`Lorentz.invariantReductionToPauliVal`**, a def, [line 289](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L289).

> For an equivariant map `f` out of the tensors with the indices of the Pauli tensor, the
> Lorentz invariants of the range of `f` reduce to the span of the image `f pauliTensor` of the
> Pauli tensor.

```lean
noncomputable def invariantReductionToPauliVal {B : Type*} [AddCommGroup B] [Module ℂ B]
    {repLorentz : Representation ℂ SL(2,ℂ) B} {f : ℂT[.up, .upL, .upR] →ₗ[ℂ] B}
    (hf : complexLorentzTensor.IsEquivariant ![.up, .upL, .upR] repLorentz f) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

### D.2. Dual Weyl indices

> A family `T^μ{}_{α' α}` with a four-vector index and a dual right- and a dual left-handed Weyl
> index is an equivariant map out of `ℂT[.up, .downR, .downL]`. Dualising both Weyl indices,
> `dualWeylMap`, is an equivariant surjection onto these tensors from the tensors with the indices
> of the Pauli tensor. Composing with it gives an equivariant map with the same range out of the
> latter, and section D.1 applies.

**`Lorentz.dualWeylMap`**, a def, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L311).

> Dualising the two Weyl indices of a tensor with the indices of the Pauli tensor, the dual
> indices listed in the order of `ℂT[.up, .downR, .downL]`.

```lean
noncomputable def dualWeylMap : ℂT[.up, .upL, .upR] →ₗ[ℂ] ℂT[.up, .downR, .downL]
```

**`Lorentz.dualWeylMap_equivariant`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L317).

> Dualising the Weyl indices commutes with the action of `SL(2,ℂ)`.

```lean
lemma dualWeylMap_equivariant (g : SL(2,ℂ)) (t : ℂT[.up, .upL, .upR]) :
    dualWeylMap (g • t) = g • dualWeylMap t
```

**`Lorentz.dualWeylMap_surjective`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L326).

> Dualising the Weyl indices is surjective. The dualisations are inverted by raising the
> indices again, and the relabelling by its inverse.

```lean
lemma dualWeylMap_surjective : Function.Surjective dualWeylMap
```

**`Lorentz.isEquivariant_comp_dualWeylMap`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L343).

> Composing with the dualisation of the Weyl indices gives an equivariant map out of the
> tensors with the indices of the Pauli tensor.

```lean
lemma isEquivariant_comp_dualWeylMap :
    complexLorentzTensor.IsEquivariant ![.up, .upL, .upR] repLorentz (f ∘ₗ dualWeylMap)
```

**`Lorentz.range_comp_dualWeylMap`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L349).

> Composing with the dualisation of the Weyl indices does not change the range.

```lean
lemma range_comp_dualWeylMap : LinearMap.range (f ∘ₗ dualWeylMap) = LinearMap.range f
```

**`Lorentz.invariantReductionToPauliValDualWeyl`**, a def, [line 356](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L356).

> The Lorentz invariants of the range of `f` reduce to the span of the image
> `f (dualWeylMap pauliTensor)` of the Pauli tensor with dual Weyl indices, the kinetic term of a
> Weyl fermion.

```lean
noncomputable def invariantReductionToPauliValDualWeyl :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g) (LinearMap.range f)
```

### D.3. Maps from dual components

> A family `T (μ, α, α')` of vectors, indexed by a four-vector index, a dual left-handed and a
> dual right-handed Weyl index, is relabelled by `dualIndexEquiv`, and its map
> `liftComponents (T ∘ dualIndexEquiv)` sends `e_μ ⊗ e_α' ⊗ e_α` to `T (μ, α, α')`. It is
> equivariant when the vectors are moved as the basis tensors are.

**`Lorentz.dualIndexEquiv`**, a def, [line 384](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L384).

> The component indices of a tensor of `ℂT[.up, .downR, .downL]`, as a four-vector index, a
> dual left-handed and a dual right-handed Weyl index.

```lean
def dualIndexEquiv : ComponentIdx (S := complexLorentzTensor) ![.up, .downR, .downL] ≃
    (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2
```

**`Lorentz.isEquivariant_liftComponents_upDownRDownL`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L396).

> The map of a family relabelled by `dualIndexEquiv` is equivariant when `T (μ, α, α')` is moved
> as `T^μ{}_{α α'}`, the vector index by the Lorentz matrix, the dual left index by `(g⁻¹)ᵀ` and
> the dual right index by `(g⁻¹)ᴴ`, the summed index first in each factor.

```lean
lemma isEquivariant_liftComponents_upDownRDownL
    {repLorentz : Representation ℂ SL(2,ℂ) B} (T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B)
    (hT : ∀ (g : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2),
      repLorentz g (T (μ, l)) = ∑ (ν : Fin 1 ⊕ Fin 3), ∑ (a : Fin 2 × Fin 2),
        ((((SL2C.toLorentzGroup g).1 ν μ : ℝ) : ℂ)
          * ((g.1⁻¹)ᵀ a.1 l.1 * (g.1⁻¹)ᴴ a.2 l.2)) • T (ν, a)) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents (T ∘ dualIndexEquiv))
```

**`Lorentz.invariantReductionToPauliValDualWeylOfComponents`**, a def, [line 417](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L417).

> For a family whose map is equivariant, the Lorentz invariants of the span of the family
> reduce to the span of the image under `liftComponents (T ∘ dualIndexEquiv)` of the Pauli tensor
> with dual Weyl indices, `dualWeylMap pauliTensor`.

```lean
noncomputable def invariantReductionToPauliValDualWeylOfComponents
    {repLorentz : Representation ℂ SL(2,ℂ) B} {T : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B}
    (hT : complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents (T ∘ dualIndexEquiv))) :
    InvariantReductionToSpan (fun g : SL(2,ℂ) => repLorentz g)
      (Submodule.span ℂ (Set.range T))
```

### D.4. Once-derived one-index Weyl families and their products

> A once-derived fermion symbol carries a four-vector index, from the derivative, besides its
> spinor index. The derivative slot moves by the columns of the Lorentz matrix and the spinor
> slot by the contragredient of the Weyl representation of its chirality, conjugated for the
> dotted one. Only the value index of a fermion symbol is dualised, so the derivative slot keeps the
> plain Lorentz law. A one-index family of one chirality times a once-derived family of the other
> is an equivariant map out of `ℂT[.up, .downR, .downL]`, in either order.

**`Lorentz.isEquivariant_upDownRDownL_mul`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L453).

> An undotted family times a once-derived dotted one is an equivariant map out of
> `ℂT[.up, .downR, .downL]`, the derivative supplying the four-vector index.

```lean
lemma isEquivariant_upDownRDownL_mul {X : Fin 2 → B} {Y : (Fin 1 ⊕ Fin 3) → Fin 2 → B}
    (hX : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), repLorentz Λ (X a) = ∑ β, (Λ⁻¹).1 a β • X β)
    (hY : ∀ (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : Fin 2), repLorentz Λ (Y μ a)
      = ∑ ν, ∑ β, ((((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) * star ((Λ⁻¹).1 a β)) • Y ν β) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p => X p.2.1 * Y p.1 p.2.2) ∘ dualIndexEquiv))
```

**`Lorentz.isEquivariant_upDownRDownL_mul_swap`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean#L473).

> A dotted family times a once-derived undotted one is an equivariant map out of
> `ℂT[.up, .downR, .downL]`, the two spinor slots exchanged.

```lean
lemma isEquivariant_upDownRDownL_mul_swap {X : Fin 2 → B} {Y : (Fin 1 ⊕ Fin 3) → Fin 2 → B}
    (hX : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), repLorentz Λ (X a) = ∑ β, star ((Λ⁻¹).1 a β) • X β)
    (hY : ∀ (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : Fin 2), repLorentz Λ (Y μ a)
      = ∑ ν, ∑ β, ((((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) * (Λ⁻¹).1 a β) • Y ν β) :
    complexLorentzTensor.IsEquivariant ![.up, .downR, .downL] repLorentz
      (liftComponents ((fun p => X p.2.2 * Y p.1 p.2.1) ∘ dualIndexEquiv))
```

## Depends on

- [Physlib.Relativity.Bispinors.Pauli.Basic](../../../physlib/relativity/bispinors/pauli-basic.md)
- [Weyl fermions as tensors](../fermions/weyl-tensorial.md)
- [The covariant Pauli matrices as plain matrices](../paulimatrices/selfadjoint.md)
- [Complex four-vectors as tensors](../tensors/complextensor-vector-tensorial.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [Reynolds elements for complex Lorentz tensors](../lorentzgroup/invariants-reynolds.md)
- [The metrics are the unique invariants](../tensors/complextensor-metrics-pre.md)

## Sources

- [PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/Bispinors/Pauli/Basic.lean)
