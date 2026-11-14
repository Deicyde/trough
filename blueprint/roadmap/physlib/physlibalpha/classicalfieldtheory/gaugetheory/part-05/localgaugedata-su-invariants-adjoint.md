---
declaration: module
origin: cited
lean: suTensor.eq_zero_of_adjRep_eq_self, suTensor.eq_zero_of_invariant_adj, suTensor.adjPairIdx, suTensor.basis_repr_smul_adjPair, suTensor.adjUnitTensor, suTensor.adjUnitTensor_invariant, suTensor.basis_repr_adjUnitTensor, suTensor.exists_eq_smul_adjUnitTensor_of_invariant
statement: formalized
proof: formalized
---

# Invariants of one and of two adjoint indices of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.Invariants.Adjoint`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean): 20 declarations, 20 with a docstring.

## i. Overview

> A tensor with one adjoint index is an element `A` of the complexified Lie algebra `ℂ ⊗[ℝ] su(N)`,
> moved by `g` to `g A g⁻¹`. The matrix of an invariant one commutes with every element of `SU(N)`, so
> it is scalar (`SU.eq_smul_one_of_commute`), and being traceless it is zero (A).
>
> A tensor with two adjoint indices has a matrix of components `C` in the Gell-Mann basis, moved by
> `g` to `M C Mᵀ`, where `M` is the matrix of the adjoint action of `g`. That matrix is real and
> `Mᵀ` is the matrix of `g⁻¹`, so the components of an invariant tensor are the matrix of an
> endomorphism of the complexified Lie algebra commuting with the adjoint action. By
> `suTensor.eq_smul_id_of_commute_adjRep` that endomorphism is scalar, and the invariant tensors are
> the multiples of the unit tensor of the adjoint color, `∑ λ_a ⊗ λ_a / 2` (B).
>
> For equivariant maps out of these tensors the invariants of the range reduce to `⊥` for one
> adjoint index and to the image of the unit tensor for two (C). Families indexed by the Gell-Mann
> labels are turned into maps by `adjMap` and `adjPairMap`, and for two indices the image of twice
> the unit tensor is the trace contraction `∑ a, T ![a, a]` (D).

## ii. Key results

> - `suTensor.eq_zero_of_invariant_adj` : an invariant tensor with one adjoint index is zero.
> - `suTensor.exists_eq_smul_unitTensor_of_invariant_adjPair` : an invariant tensor with two adjoint
>   indices is a multiple of the unit tensor.
> - `suTensor.invariantReductionToTrace` : the reduction of the invariants of the span of a family
>   with two adjoint indices to the trace contraction.

## iv. References

> * None.

## A. One adjoint index

**`suTensor.eq_zero_of_adjRep_eq_self`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L68).

> An invariant element of the complexified Lie algebra is zero: its matrix commutes with every
> element of `SU(N)`, so it is a scalar, and its trace vanishes.

```lean
lemma eq_zero_of_adjRep_eq_self {A : SUAlgebraComplexified N} (hA : ∀ g : SU N, adjRep N g A = A) :
    A = 0
```

**`suTensor.eq_zero_of_invariant_adj`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L87).

> An invariant tensor with one adjoint index is zero.

```lean
lemma eq_zero_of_invariant_adj (t : SuT[N, .adj]) (ht : ∀ g : SU N, g • t = t) : t = 0
```

## B. Two adjoint indices

**`suTensor.adjPairIdx`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L102).

> The component indices of a tensor with two adjoint indices, as the pair of their Gell-Mann
> labels.

```lean
def adjPairIdx : ComponentIdx (S := suTensor N) ![.adj, .adj] ≃ (Fin 2 → GellMann.Index N)
```

**`suTensor.basis_repr_smul_adjPair`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L114).

> The components of `g • t` for a tensor with two adjoint indices: the matrix of components
> `C` is moved to `M C Mᵀ`.

```lean
lemma basis_repr_smul_adjPair (g : SU N) (t : SuT[N, .adj, .adj])
    (n : Fin 2 → GellMann.Index N) :
    (Tensor.basis _).repr (g • t) (adjPairIdx.symm n)
      = ∑ x, ∑ y, adjMatrix g (n 0) x * adjMatrix g (n 1) y
        * (Tensor.basis _).repr t (adjPairIdx.symm ![x, y])
```

**`suTensor.adjUnitTensor`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L127).

> The unit tensor of the adjoint color, `∑ λ_a ⊗ λ_a / 2`, with two adjoint indices.

```lean
noncomputable def adjUnitTensor : SuT[N, .adj, .adj]
```

**`suTensor.adjUnitTensor_invariant`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L130).

> The unit tensor of the adjoint color is invariant.

```lean
lemma adjUnitTensor_invariant (g : SU N) : g • adjUnitTensor N = adjUnitTensor N
```

**`suTensor.basis_repr_adjUnitTensor`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L135).

> The components of the unit tensor of the adjoint color: `δ / 2`, the Gell-Mann matrices
> being orthogonal with `tr (λ_a λ_b) = 2 δ_ab`.

```lean
lemma basis_repr_adjUnitTensor (n : Fin 2 → GellMann.Index N) :
    (Tensor.basis _).repr (adjUnitTensor N) (adjPairIdx.symm n)
      = if n 0 = n 1 then 1 / 2 else 0
```

**`suTensor.exists_eq_smul_adjUnitTensor_of_invariant`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L156).

> An invariant tensor with two adjoint indices is a multiple of the unit tensor of the adjoint
> color. Its matrix of components commutes with the matrices of the adjoint action, so it is the
> matrix of an endomorphism commuting with the adjoint action, which is scalar.

```lean
lemma exists_eq_smul_adjUnitTensor_of_invariant (t : SuT[N, .adj, .adj])
    (ht : ∀ g : SU N, g • t = t) : ∃ a : ℂ, t = a • adjUnitTensor N
```

## C. The invariants of equivariant maps

**`suTensor.reducesInvariantsTo_bot_of_isEquivariant_adj`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L204).

> For an equivariant map out of the tensors with one adjoint index, the invariants of the range
> reduce to `⊥`.

```lean
lemma reducesInvariantsTo_bot_of_isEquivariant_adj {f : SuT[N, .adj] →ₗ[ℂ] B}
    (hf : (suTensor N).IsEquivariant ![.adj] ρ f) :
    ReducesInvariantsTo (fun g : SU N => ρ g) (LinearMap.range f) ⊥
```

**`suTensor.invariantReductionToAdjUnitImage`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L211).

> For an equivariant map `f` out of the tensors with two adjoint indices, the invariants of the
> range reduce to the span of the image of the unit tensor.

```lean
noncomputable def invariantReductionToAdjUnitImage {f : SuT[N, .adj, .adj] →ₗ[ℂ] B}
    (hf : (suTensor N).IsEquivariant ![.adj, .adj] ρ f) :
    InvariantReductionToSpan (fun g : SU N => ρ g) (LinearMap.range f)
```

## D. Maps from components

**`suTensor.adjIdx`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L224).

> The component indices of a tensor with one adjoint index, as its Gell-Mann label.

```lean
def adjIdx : ComponentIdx (S := suTensor N) ![.adj] ≃ GellMann.Index N
```

**`suTensor.adjMap`**, a def, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L235).

> The linear map out of the tensors with one adjoint index sending the basis tensor with label
> `a` to `T a`.

```lean
noncomputable def adjMap (T : GellMann.Index N → B) : SuT[N, .adj] →ₗ[ℂ] B
```

**`suTensor.adjMap_smul_of_law`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L240).

> A linear map moving a family indexed by one adjoint label by the matrix of the adjoint action
> of `g` intertwines the map of the family with the action of `g`.

```lean
lemma adjMap_smul_of_law (T : GellMann.Index N → B) {σ : B →ₗ[ℂ] B} (g : SU N)
    (hσ : ∀ a : GellMann.Index N, σ (T a) = ∑ b, adjMatrix g b a • T b) (t : SuT[N, .adj]) :
    σ (adjMap T t) = adjMap T (g • t)
```

**`suTensor.isEquivariant_adjMap`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L248).

> The map of a family indexed by one adjoint label is equivariant when the family moves by the
> matrix of the adjoint action, the summed label first.

```lean
lemma isEquivariant_adjMap (T : GellMann.Index N → B)
    (hT : ∀ (g : SU N) (a : GellMann.Index N), ρ g (T a) = ∑ b, adjMatrix g b a • T b) :
    (suTensor N).IsEquivariant ![.adj] ρ (adjMap T)
```

**`suTensor.reducesInvariantsTo_bot_span_of_adjMap`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L255).

> For a family indexed by one adjoint label whose map is equivariant, the invariants of the
> span of the family reduce to `⊥`.

```lean
lemma reducesInvariantsTo_bot_span_of_adjMap {T : GellMann.Index N → B}
    (hT : (suTensor N).IsEquivariant ![.adj] ρ (adjMap T)) :
    ReducesInvariantsTo (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T)) ⊥
```

**`suTensor.adjPairMap`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L263).

> The linear map out of the tensors with two adjoint indices sending the basis tensor with
> labels `n` to `T n`.

```lean
noncomputable def adjPairMap (T : (Fin 2 → GellMann.Index N) → B) :
    SuT[N, .adj, .adj] →ₗ[ℂ] B
```

**`suTensor.adjPairMap_two_smul_adjUnitTensor`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L268).

> The map of a family sends twice the unit tensor to the trace contraction `∑ a, T ![a, a]`.

```lean
lemma adjPairMap_two_smul_adjUnitTensor (T : (Fin 2 → GellMann.Index N) → B) :
    adjPairMap T ((2 : ℂ) • adjUnitTensor N) = ∑ a, T ![a, a]
```

**`suTensor.adjPairMap_smul_of_law`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L282).

> A linear map moving a family indexed by two adjoint labels by the matrix of the adjoint
> action of `g` on each label intertwines the map of the family with the action of `g`.

```lean
lemma adjPairMap_smul_of_law (T : (Fin 2 → GellMann.Index N) → B) {σ : B →ₗ[ℂ] B} (g : SU N)
    (hσ : ∀ l : Fin 2 → GellMann.Index N, σ (T l)
      = ∑ a : Fin 2 → GellMann.Index N, (adjMatrix g (a 0) (l 0) * adjMatrix g (a 1) (l 1)) • T a)
    (t : SuT[N, .adj, .adj]) :
    σ (adjPairMap T t) = adjPairMap T (g • t)
```

**`suTensor.isEquivariant_adjPairMap`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L292).

> The map of a family indexed by two adjoint labels is equivariant when the family moves by the
> matrix of the adjoint action on each label, the summed label first.

```lean
lemma isEquivariant_adjPairMap (T : (Fin 2 → GellMann.Index N) → B)
    (hT : ∀ (g : SU N) (l : Fin 2 → GellMann.Index N), ρ g (T l)
      = ∑ a : Fin 2 → GellMann.Index N, (adjMatrix g (a 0) (l 0) * adjMatrix g (a 1) (l 1)) • T a) :
    (suTensor N).IsEquivariant ![.adj, .adj] ρ (adjPairMap T)
```

**`suTensor.invariantReductionToTrace`**, a def, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean#L300).

> For a family indexed by two adjoint labels whose map is equivariant, the invariants of the
> span of the family reduce to the span of the trace contraction `∑ a, T ![a, a]`.

```lean
noncomputable def invariantReductionToTrace {T : (Fin 2 → GellMann.Index N) → B}
    (hT : (suTensor N).IsEquivariant ![.adj, .adj] ρ (adjPairMap T)) :
    InvariantReductionToSpan (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T))
```

## Depends on

- [The unit tensors](../../../../physlib/relativity/tensors/part-01/unittensor.md)
- [The complex tensor species of `SU(N)`](localgaugedata-su-tensorspecies.md)

## Proof depends on

- [Elements of `SU(N)` in a coordinate plane, and what commutes with them](localgaugedata-su-invariants-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/Adjoint.lean)
