---
declaration: module
origin: cited
lean: suTensor.adjPairIdx, suTensor.basis_repr_smul_adjPair, suTensor.adjUnitTensor, suTensor.adjUnitTensor_invariant, suTensor.basis_repr_adjUnitTensor, suTensor.invariants_adj_adj_eq_span_adjUnitTensor, suTensor.invariants_adj_adj_eq_span_two_smul_adjUnitTensor, suTensor.reducesInvariantsTo_bot_of_isEquivariant_adj
statement: formalized
proof: formalized
---

# The unit tensor of the adjoint colour of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Invariants.AdjUnit`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean): 18 declarations, 18 with a docstring.

> Up to scale, the unit tensor is the only invariant with two adjoint indices.

## i. Overview

> A tensor with one adjoint index has no invariants but zero (`suTensor.invariants_adj_eq_bot`, with
> the adjoint colour). A tensor with two adjoint indices has a matrix of components `C` in the
> Gell-Mann basis, moved by `g` to `M C Mᵀ`, where `M` is the matrix of the adjoint action of `g`.
> That matrix is real and `Mᵀ` is the matrix of `g⁻¹`, so the components of an invariant tensor are
> the matrix of an endomorphism of the complexified Lie algebra commuting with the adjoint action. By
> `suTensor.eq_smul_id_of_commute_adjRep` that endomorphism is scalar, and the invariant tensors are
> the line through the unit tensor of the adjoint color, `∑ λ_a ⊗ λ_a / 2` (A).
>
> For equivariant maps out of these tensors the invariants of the range reduce to `⊥` for one
> adjoint index and to the image of the unit tensor for two (B). A family indexed by the Gell-Mann
> labels is the map `liftComponents (T ∘ adjIdx)` or `liftComponents (T ∘ adjPairIdx)`, and for two
> indices the image of twice the unit tensor is the trace contraction `∑ a, T ![a, a]` (C). The
> invariants of the tensor square of the adjoint representation are the line through the unit
> `∑ λ_a ⊗ λ_a / 2` (D).

## ii. Key results

> - `suTensor.invariants_adj_adj_eq_span_adjUnitTensor` : the invariant tensors with two adjoint
>   indices are the line through the unit tensor.
> - `suTensor.invariantReductionToTrace` : the reduction of the invariants of the span of a family
>   with two adjoint indices to the trace contraction.
> - `suTensor.invariants_tprod_eq_span_adjUnitVal` : the invariants of the tensor square of the
>   adjoint representation are the line through the unit.

## iv. References

> * None.

## A. Two adjoint indices

**`suTensor.adjPairIdx`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L71).

> The component indices of a tensor with two adjoint indices, as the pair of their Gell-Mann
> labels.

```lean
def adjPairIdx : ComponentIdx (S := suTensor N) ![.adj, .adj] ≃ (Fin 2 → GellMann.Index N)
```

**`suTensor.basis_repr_smul_adjPair`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L83).

> The components of `g • t` for a tensor with two adjoint indices. The matrix of components
> `C` is moved to `M C Mᵀ`.

```lean
lemma basis_repr_smul_adjPair (g : SU N) (t : SuT[N, .adj, .adj])
    (n : Fin 2 → GellMann.Index N) :
    (Tensor.basis _).repr (g • t) (adjPairIdx.symm n)
      = ∑ x, ∑ y, adjMatrix g (n 0) x * adjMatrix g (n 1) y
        * (Tensor.basis _).repr t (adjPairIdx.symm ![x, y])
```

**`suTensor.adjUnitTensor`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L96).

> The unit tensor of the adjoint color, `∑ λ_a ⊗ λ_a / 2`, with two adjoint indices.

```lean
noncomputable def adjUnitTensor : SuT[N, .adj, .adj]
```

**`suTensor.adjUnitTensor_invariant`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L99).

> The unit tensor of the adjoint color is invariant.

```lean
lemma adjUnitTensor_invariant (g : SU N) : g • adjUnitTensor N = adjUnitTensor N
```

**`suTensor.basis_repr_adjUnitTensor`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L104).

> The components of the unit tensor of the adjoint color, `δ / 2`, the Gell-Mann matrices
> being orthogonal with `tr (λ_a λ_b) = 2 δ_ab`.

```lean
lemma basis_repr_adjUnitTensor (n : Fin 2 → GellMann.Index N) :
    (Tensor.basis _).repr (adjUnitTensor N) (adjPairIdx.symm n)
      = if n 0 = n 1 then 1 / 2 else 0
```

**`suTensor.invariants_adj_adj_eq_span_adjUnitTensor`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L126).

> The invariant tensors with two adjoint indices are the line through the unit tensor of the
> adjoint color. The matrix of components of an invariant tensor commutes with the matrices of the
> adjoint action, so it is the matrix of an endomorphism commuting with the adjoint action, which
> is scalar.

```lean
lemma invariants_adj_adj_eq_span_adjUnitTensor :
    ((suTensor N).tensorRep ![.adj, .adj]).invariants = ℂ ∙ adjUnitTensor N
```

**`suTensor.invariants_adj_adj_eq_span_two_smul_adjUnitTensor`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L167).

> The invariant tensors with two adjoint indices are the line through twice the unit tensor,
> the tensor whose image under a map of a family is the trace contraction.

```lean
lemma invariants_adj_adj_eq_span_two_smul_adjUnitTensor :
    ((suTensor N).tensorRep ![.adj, .adj]).invariants = ℂ ∙ ((2 : ℂ) • adjUnitTensor N)
```

## B. The invariants of equivariant maps

**`suTensor.reducesInvariantsTo_bot_of_isEquivariant_adj`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L182).

> For an equivariant map out of the tensors with one adjoint index, the invariants of the range
> reduce to `⊥`.

```lean
lemma reducesInvariantsTo_bot_of_isEquivariant_adj {f : SuT[N, .adj] →ₗ[ℂ] B}
    (hf : (suTensor N).IsEquivariant ![.adj] ρ f) :
    ReducesInvariantsTo (fun g : SU N => ρ g) (LinearMap.range f) ⊥
```

## C. Maps from components

**`suTensor.adjIdx`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L194).

> The component indices of a tensor with one adjoint index, as its Gell-Mann label.

```lean
def adjIdx : ComponentIdx (S := suTensor N) ![.adj] ≃ GellMann.Index N
```

**`suTensor.liftComponents_adj_smul_of_law`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L205).

> A linear map moving a family indexed by one adjoint label by the matrix of the adjoint action
> of `g` intertwines the map of the family with the action of `g`.

```lean
lemma liftComponents_adj_smul_of_law (T : GellMann.Index N → B) {σ : B →ₗ[ℂ] B} (g : SU N)
    (hσ : ∀ a : GellMann.Index N, σ (T a) = ∑ b, adjMatrix g b a • T b) (t : SuT[N, .adj]) :
    σ (liftComponents (T ∘ adjIdx) t) = liftComponents (T ∘ adjIdx) (g • t)
```

**`suTensor.isEquivariant_liftComponents_adj`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L214).

> The map of a family indexed by one adjoint label is equivariant when the family moves by the
> matrix of the adjoint action, the summed label first.

```lean
lemma isEquivariant_liftComponents_adj (T : GellMann.Index N → B)
    (hT : ∀ (g : SU N) (a : GellMann.Index N), ρ g (T a) = ∑ b, adjMatrix g b a • T b) :
    (suTensor N).IsEquivariant ![.adj] ρ (liftComponents (T ∘ adjIdx))
```

**`suTensor.reducesInvariantsTo_bot_span_adj`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L221).

> For a family indexed by one adjoint label whose map is equivariant, the invariants of the
> span of the family reduce to `⊥`.

```lean
lemma reducesInvariantsTo_bot_span_adj {T : GellMann.Index N → B}
    (hT : (suTensor N).IsEquivariant ![.adj] ρ (liftComponents (T ∘ adjIdx))) :
    ReducesInvariantsTo (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T)) ⊥
```

**`suTensor.liftComponents_two_smul_adjUnitTensor`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L229).

> The map of a family relabelled by `adjPairIdx` sends twice the unit tensor to the trace
> contraction `∑ a, T ![a, a]`.

```lean
lemma liftComponents_two_smul_adjUnitTensor (T : (Fin 2 → GellMann.Index N) → B) :
    liftComponents (T ∘ adjPairIdx) ((2 : ℂ) • adjUnitTensor N) = ∑ a, T ![a, a]
```

**`suTensor.liftComponents_adjPair_smul_of_law`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L243).

> A linear map moving a family indexed by two adjoint labels by the matrix of the adjoint
> action of `g` on each label intertwines the map of the family with the action of `g`.

```lean
lemma liftComponents_adjPair_smul_of_law (T : (Fin 2 → GellMann.Index N) → B) {σ : B →ₗ[ℂ] B}
    (g : SU N) (hσ : ∀ l : Fin 2 → GellMann.Index N, σ (T l)
      = ∑ a : Fin 2 → GellMann.Index N, (adjMatrix g (a 0) (l 0) * adjMatrix g (a 1) (l 1)) • T a)
    (t : SuT[N, .adj, .adj]) :
    σ (liftComponents (T ∘ adjPairIdx) t) = liftComponents (T ∘ adjPairIdx) (g • t)
```

**`suTensor.isEquivariant_liftComponents_adjPair`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L254).

> The map of a family indexed by two adjoint labels is equivariant when the family moves by the
> matrix of the adjoint action on each label, the summed label first.

```lean
lemma isEquivariant_liftComponents_adjPair (T : (Fin 2 → GellMann.Index N) → B)
    (hT : ∀ (g : SU N) (l : Fin 2 → GellMann.Index N), ρ g (T l)
      = ∑ a : Fin 2 → GellMann.Index N, (adjMatrix g (a 0) (l 0) * adjMatrix g (a 1) (l 1)) • T a) :
    (suTensor N).IsEquivariant ![.adj, .adj] ρ (liftComponents (T ∘ adjPairIdx))
```

**`suTensor.invariantReductionToTrace`**, a def, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L262).

> For a family indexed by two adjoint labels whose map is equivariant, the invariants of the
> span of the family reduce to the span of the trace contraction `∑ a, T ![a, a]`.

```lean
noncomputable def invariantReductionToTrace {T : (Fin 2 → GellMann.Index N) → B}
    (hT : (suTensor N).IsEquivariant ![.adj, .adj] ρ (liftComponents (T ∘ adjPairIdx))) :
    InvariantReductionToSpan (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T))
```

## D. The invariants of the tensor square of the adjoint representation

**`suTensor.adjUnitTensor_eq_fromPairT`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L276).

> The unit tensor of the adjoint color is the tensor of `∑ b_a ⊗ bᵃ`.

```lean
lemma adjUnitTensor_eq_fromPairT :
    adjUnitTensor N = fromPairT (S := suTensor N) (c1 := .adj) (c2 := .adj) (adjUnitVal N)
```

**`suTensor.invariants_tprod_eq_span_adjUnitVal`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean#L283).

> The invariants of the tensor square of the adjoint representation are the line through the
> unit `∑ b_a ⊗ bᵃ`.

```lean
lemma invariants_tprod_eq_span_adjUnitVal :
    ((adjRep N).tprod (adjRep N)).invariants = ℂ ∙ adjUnitVal N
```

## Depends on

- [The complex tensor species of `SU(N)`](globalgaugegroup-su-tensorspecies.md)

## Proof depends on

- [What commutes with the adjoint action of `SU(N)`, and the Reynolds element of its tensors](globalgaugegroup-su-invariants-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/AdjUnit.lean)
