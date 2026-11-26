---
declaration: module
origin: cited
lean: suTensor.fundAntiFundIdx, suTensor.delta, suTensor.delta_invariant, suTensor.basis_repr_delta, suTensor.basis_repr_smul_fundAntiFund, suTensor.invariants_fund_antiFund_eq_span_delta, suTensor.liftComponents_delta, suTensor.liftComponents_fundAntiFund_smul_of_law
statement: formalized
proof: formalized
---

# The Kronecker delta of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.SU.Invariants.Delta`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean): 12 declarations, 12 with a docstring.

> Up to scale, the Kronecker delta is the only invariant tensor with a fundamental and an
> anti-fundamental index.

## i. Overview

> The invariant tensors of `SuT[N, .fund, .antiFund]` are the line through the Kronecker delta
> `δᵃ_b`, the unit tensor `delta N` of the anti-fundamental color (A, B). The components of a
> tensor with these indices form a matrix `C`, which `g` moves to `g C g⁻¹`, so the components of
> an invariant tensor commute with every element of `SU(N)` and are scalar
> (`SU.eq_smul_one_of_commute`).
>
> A family `T` of vectors indexed by `Fin 2 → Fin N`, a fundamental index first, is the map
> `liftComponents (T ∘ fundAntiFundIdx)`, equivariant exactly when `T` obeys the transformation law of
> the components, and `f (delta N)` is then the contraction `∑ a, T ![a, a]`. The invariants of the
> span of such a
> family, modulo a stable submodule, reduce to the line through that contraction (C).
>
> The invariants of `ℂᴺ ⊗ ℂᴺ` under the fundamental and the anti-fundamental representation are the
> line through `∑ eᵢ ⊗ eᵢ` (D).

## ii. Key results

> - `suTensor.delta` : the Kronecker delta.
> - `suTensor.invariants_fund_antiFund_eq_span_delta` : the invariant tensors are the line through it.
> - `suTensor.invariantReductionToDelta` : the reduction of the invariants of the span of a family
>   to the delta contraction.
> - `suTensor.invariants_tprod_eq_span_pairUnitVal` : the invariants of the fundamental times the
>   anti-fundamental representation are the line through `∑ eᵢ ⊗ eᵢ`.

## iv. References

> * None.

## A. The Kronecker delta

**`suTensor.fundAntiFundIdx`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L72).

> The component indices of a tensor with a fundamental and an anti-fundamental index, as the
> pair of their labels.

```lean
def fundAntiFundIdx : ComponentIdx (S := suTensor N) ![.fund, .antiFund] ≃ (Fin 2 → Fin N)
```

**`suTensor.delta`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L85).

> The Kronecker delta `δᵃ_b`, the unit tensor of the anti-fundamental color, with a
> fundamental and an anti-fundamental index.

```lean
noncomputable def delta : SuT[N, .fund, .antiFund]
```

**`suTensor.delta_invariant`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L88).

> The Kronecker delta is invariant.

```lean
lemma delta_invariant (g : SU N) : g • delta N = delta N
```

**`suTensor.basis_repr_delta`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L92).

> The components of the Kronecker delta.

```lean
lemma basis_repr_delta (n : Fin 2 → Fin N) :
    (Tensor.basis _).repr (delta N) (fundAntiFundIdx.symm n) = if n 0 = n 1 then 1 else 0
```

## B. The invariant tensors

**`suTensor.basis_repr_smul_fundAntiFund`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L109).

> The components of `g • t` for a tensor with a fundamental and an anti-fundamental index.
> The matrix of components `C` is moved to `g C g⁻¹`.

```lean
lemma basis_repr_smul_fundAntiFund (g : SU N) (t : SuT[N, .fund, .antiFund])
    (n : Fin 2 → Fin N) :
    (Tensor.basis _).repr (g • t) (fundAntiFundIdx.symm n)
      = ∑ x, ∑ y, g.1 (n 0) x * (g⁻¹).1 y (n 1)
        * (Tensor.basis _).repr t (fundAntiFundIdx.symm ![x, y])
```

**`suTensor.invariants_fund_antiFund_eq_span_delta`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L127).

> The invariant tensors with a fundamental and an anti-fundamental index are the line through
> the Kronecker delta. The matrix of components of an invariant tensor commutes with every element
> of `SU(N)`.

```lean
lemma invariants_fund_antiFund_eq_span_delta :
    ((suTensor N).tensorRep ![.fund, .antiFund]).invariants = ℂ ∙ delta N
```

## C. Maps from components

**`suTensor.liftComponents_delta`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L162).

> The map of a family relabelled by `fundAntiFundIdx` sends the Kronecker delta to the
> contraction `∑ a, T ![a, a]`.

```lean
lemma liftComponents_delta (T : (Fin 2 → Fin N) → B) :
    liftComponents (T ∘ fundAntiFundIdx) (delta N) = ∑ a, T ![a, a]
```

**`suTensor.liftComponents_fundAntiFund_smul_of_law`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L178).

> A linear map moving a family as a group element moves the components of a tensor with a
> fundamental and an anti-fundamental index intertwines the map of the family with the action of
> that element. The element acts by one factor of itself on the first index and of its complex
> conjugate on the second, the summed index first.

```lean
lemma liftComponents_fundAntiFund_smul_of_law (T : (Fin 2 → Fin N) → B) {σ : B →ₗ[ℂ] B}
    (g : SU N) (hσ : ∀ l : Fin 2 → Fin N, σ (T l)
      = ∑ a : Fin 2 → Fin N, (g.1 (a 0) (l 0) * starRingEnd ℂ (g.1 (a 1) (l 1))) • T a)
    (t : SuT[N, .fund, .antiFund]) :
    σ (liftComponents (T ∘ fundAntiFundIdx) t) = liftComponents (T ∘ fundAntiFundIdx) (g • t)
```

**`suTensor.isEquivariant_liftComponents_fundAntiFund`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L194).

> The map of a family is equivariant when the family moves as the components of a tensor
> with a fundamental and an anti-fundamental index.

```lean
lemma isEquivariant_liftComponents_fundAntiFund (T : (Fin 2 → Fin N) → B)
    (hT : ∀ (g : SU N) (l : Fin 2 → Fin N), ρ g (T l)
      = ∑ a : Fin 2 → Fin N, (g.1 (a 0) (l 0) * starRingEnd ℂ (g.1 (a 1) (l 1))) • T a) :
    (suTensor N).IsEquivariant ![.fund, .antiFund] ρ (liftComponents (T ∘ fundAntiFundIdx))
```

**`suTensor.invariantReductionToDelta`**, a def, [line 202](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L202).

> For a family whose map is equivariant, the invariants of the span of the family reduce to
> the span of the delta contraction `∑ a, T ![a, a]`.

```lean
noncomputable def invariantReductionToDelta {T : (Fin 2 → Fin N) → B}
    (hT : (suTensor N).IsEquivariant ![.fund, .antiFund] ρ (liftComponents (T ∘ fundAntiFundIdx))) :
    InvariantReductionToSpan (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T))
```

## D. The invariants of the tensor product

**`suTensor.delta_eq_fromPairT`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L215).

> The Kronecker delta is the tensor of `∑ eᵢ ⊗ eᵢ`.

```lean
lemma delta_eq_fromPairT :
    delta N = fromPairT (S := suTensor N) (c1 := .fund) (c2 := .antiFund) (pairUnitVal N)
```

**`suTensor.invariants_tprod_eq_span_pairUnitVal`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean#L222).

> The invariants of `ℂᴺ ⊗ ℂᴺ` under the fundamental and the anti-fundamental representation are
> the line through `∑ eᵢ ⊗ eᵢ`.

```lean
lemma invariants_tprod_eq_span_pairUnitVal :
    ((fundRep N).tprod (antiFundRep N)).invariants = ℂ ∙ pairUnitVal N
```

## Depends on

- [The complex tensor species of `SU(N)`](globalgaugegroup-su-tensorspecies.md)

## Proof depends on

- [What commutes with the adjoint action of `SU(N)`, and the Reynolds element of its tensors](globalgaugegroup-su-invariants-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/SU/Invariants/Delta.lean)
