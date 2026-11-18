---
declaration: module
origin: cited
lean: suTensor.fundAntiFundIdx, suTensor.delta, suTensor.delta_invariant, suTensor.basis_repr_delta, suTensor.basis_repr_smul_fundAntiFund, suTensor.exists_eq_smul_delta_of_invariant, suTensor.invariantReductionToDeltaImage, suTensor.fundAntiFundMap
statement: formalized
proof: formalized
---

# Invariants of a fundamental and an anti-fundamental index of `SU(N)`

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.SU.Invariants.FundAnti`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean): 12 declarations, 12 with a docstring.

## i. Overview

> The invariant tensors of `SuT[N, .fund, .antiFund]` are the multiples of the Kronecker delta
> `δᵃ_b`, the unit tensor `delta N` of the anti-fundamental color (A, B). The components of a
> tensor with these indices form a matrix `C`, which `g` moves to `g C g⁻¹`, so the components of
> an invariant tensor commute with every element of `SU(N)` and are scalar
> (`SU.eq_smul_one_of_commute`).
>
> For an equivariant map `f` out of these tensors, the invariants of `LinearMap.range f ⊔ S`, for
> `S` a stable submodule, reduce to the line through `f (delta N)` (C). A family `T` of vectors
> indexed by `Fin 2 → Fin N`, a fundamental index first, is the map `fundAntiFundMap T`, equivariant
> exactly when `T` obeys the transformation law of the components (D), and `f (delta N)` is then
> the contraction `∑ a, T ![a, a]`.

## ii. Key results

> - `suTensor.delta` : the Kronecker delta.
> - `suTensor.exists_eq_smul_delta_of_invariant` : the invariant tensors are its multiples.
> - `suTensor.invariantReductionToDelta` : the reduction of the invariants of the span of a family
>   to the delta contraction.

## iv. References

> * None.

## A. The Kronecker delta

**`suTensor.fundAntiFundIdx`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L63).

> The component indices of a tensor with a fundamental and an anti-fundamental index, as the
> pair of their labels.

```lean
def fundAntiFundIdx : ComponentIdx (S := suTensor N) ![.fund, .antiFund] ≃ (Fin 2 → Fin N)
```

**`suTensor.delta`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L76).

> The Kronecker delta `δᵃ_b`, the unit tensor of the anti-fundamental color, with a
> fundamental and an anti-fundamental index.

```lean
noncomputable def delta : SuT[N, .fund, .antiFund]
```

**`suTensor.delta_invariant`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L79).

> The Kronecker delta is invariant.

```lean
lemma delta_invariant (g : SU N) : g • delta N = delta N
```

**`suTensor.basis_repr_delta`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L83).

> The components of the Kronecker delta.

```lean
lemma basis_repr_delta (n : Fin 2 → Fin N) :
    (Tensor.basis _).repr (delta N) (fundAntiFundIdx.symm n) = if n 0 = n 1 then 1 else 0
```

## B. The invariant tensors

**`suTensor.basis_repr_smul_fundAntiFund`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L100).

> The components of `g • t` for a tensor with a fundamental and an anti-fundamental index:
> the matrix of components `C` is moved to `g C g⁻¹`.

```lean
lemma basis_repr_smul_fundAntiFund (g : SU N) (t : SuT[N, .fund, .antiFund])
    (n : Fin 2 → Fin N) :
    (Tensor.basis _).repr (g • t) (fundAntiFundIdx.symm n)
      = ∑ x, ∑ y, g.1 (n 0) x * (g⁻¹).1 y (n 1)
        * (Tensor.basis _).repr t (fundAntiFundIdx.symm ![x, y])
```

**`suTensor.exists_eq_smul_delta_of_invariant`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L117).

> An invariant tensor with a fundamental and an anti-fundamental index is a multiple of the
> Kronecker delta: its matrix of components commutes with every element of `SU(N)`.

```lean
lemma exists_eq_smul_delta_of_invariant (t : SuT[N, .fund, .antiFund])
    (ht : ∀ g : SU N, g • t = t) : ∃ a : ℂ, t = a • delta N
```

## C. The invariants of an equivariant map

**`suTensor.invariantReductionToDeltaImage`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L153).

> For an equivariant map `f` out of the tensors with a fundamental and an anti-fundamental
> index, the invariants of the range of `f` reduce to the span of the image `f (delta N)` of the
> Kronecker delta.

```lean
noncomputable def invariantReductionToDeltaImage
    (hf : (suTensor N).IsEquivariant ![.fund, .antiFund] ρ f) :
    InvariantReductionToSpan (fun g : SU N => ρ g) (LinearMap.range f)
```

## D. Maps from components

**`suTensor.fundAntiFundMap`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L167).

> The linear map out of the tensors with a fundamental and an anti-fundamental index sending
> the basis tensor with labels `n` to `T n`.

```lean
noncomputable def fundAntiFundMap (T : (Fin 2 → Fin N) → B) :
    SuT[N, .fund, .antiFund] →ₗ[ℂ] B
```

**`suTensor.fundAntiFundMap_delta`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L172).

> The map of a family sends the Kronecker delta to the contraction `∑ a, T ![a, a]`.

```lean
lemma fundAntiFundMap_delta (T : (Fin 2 → Fin N) → B) :
    fundAntiFundMap T (delta N) = ∑ a, T ![a, a]
```

**`suTensor.fundAntiFundMap_smul_of_law`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L187).

> A linear map moving a family as `g` moves the components of a tensor with a fundamental and an
> anti-fundamental index intertwines the map of the family with the action of `g`: a factor of `g`
> on the first index and of its complex conjugate on the second, the summed index first.

```lean
lemma fundAntiFundMap_smul_of_law (T : (Fin 2 → Fin N) → B) {σ : B →ₗ[ℂ] B} (g : SU N)
    (hσ : ∀ l : Fin 2 → Fin N, σ (T l)
      = ∑ a : Fin 2 → Fin N, (g.1 (a 0) (l 0) * starRingEnd ℂ (g.1 (a 1) (l 1))) • T a)
    (t : SuT[N, .fund, .antiFund]) :
    σ (fundAntiFundMap T t) = fundAntiFundMap T (g • t)
```

**`suTensor.isEquivariant_fundAntiFundMap`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L202).

> The map of a family is equivariant when the family moves as the components of a tensor
> with a fundamental and an anti-fundamental index.

```lean
lemma isEquivariant_fundAntiFundMap (T : (Fin 2 → Fin N) → B)
    (hT : ∀ (g : SU N) (l : Fin 2 → Fin N), ρ g (T l)
      = ∑ a : Fin 2 → Fin N, (g.1 (a 0) (l 0) * starRingEnd ℂ (g.1 (a 1) (l 1))) • T a) :
    (suTensor N).IsEquivariant ![.fund, .antiFund] ρ (fundAntiFundMap T)
```

**`suTensor.invariantReductionToDelta`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean#L210).

> For a family whose map is equivariant, the invariants of the span of the family reduce to
> the span of the delta contraction `∑ a, T ![a, a]`.

```lean
noncomputable def invariantReductionToDelta {T : (Fin 2 → Fin N) → B}
    (hT : (suTensor N).IsEquivariant ![.fund, .antiFund] ρ (fundAntiFundMap T)) :
    InvariantReductionToSpan (fun g : SU N => ρ g) (Submodule.span ℂ (Set.range T))
```

## Depends on

- [The unit tensors](../../../../physlib/relativity/tensors/part-01/unittensor.md)
- [The complex tensor species of `SU(N)`](localgaugedata-su-tensorspecies.md)

## Proof depends on

- [Elements of `SU(N)` in a coordinate plane, and what commutes with them](localgaugedata-su-invariants-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/SU/Invariants/FundAnti.lean)
