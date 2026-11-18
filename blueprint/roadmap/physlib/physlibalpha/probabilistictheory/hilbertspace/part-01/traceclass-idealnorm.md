---
declaration: module
origin: cited
lean: ProbabilisticTheory.traceNorm_transport, ProbabilisticTheory.tsum_sqrt_abs_norm_sq_eq_traceNorm, ProbabilisticTheory.summable_norm_inner_contraction_of_isTraceClass, ProbabilisticTheory.tsum_norm_inner_contraction_le_traceNorm, ProbabilisticTheory.traceNorm_eq_tsum_norm_inner_polarFactor, ProbabilisticTheory.traceNorm_add_le, ProbabilisticTheory.traceNorm_mul_le_of_isHilbertSchmidt, ProbabilisticTheory.traceNorm_mul_mul_le
statement: formalized
proof: formalized
---

# Trace-norm estimates

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.IdealNorm`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean): 8 declarations, 8 with a docstring.

> The duality bound for the trace norm, its subadditivity and the two-sided ideal estimate.

## i. Overview

> For a trace-class operator `A`, a contraction `W` and a Hilbert basis `{eᵢ}`, `∑ᵢ ‖⟪W eᵢ, A eᵢ⟫‖ ≤
> ‖A‖₁`, with equality for the polar factor. From this the trace norm is subadditive and satisfies the
> two-sided ideal estimate `‖B T C‖₁ ≤ ‖B‖ ‖T‖₁ ‖C‖`.

## ii. Key results

> - `tsum_norm_inner_contraction_le_traceNorm` : the duality bound against contractions.
> - `traceNorm_eq_tsum_norm_inner_polarFactor` : the bound is attained at the polar factor.
> - `traceNorm_add_le` : the trace norm is subadditive.
> - `traceNorm_mul_mul_le` : the two-sided ideal estimate.

## iv. References

> * None.

## A. The duality bound against contractions

**`ProbabilisticTheory.traceNorm_transport`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L59).

> The trace norm of an operator only depends on the operator, not on the trace-class witness.

```lean
lemma traceNorm_transport {X Y : H →L[ℂ] H} (hEq : X = Y) (hX : IsTraceClass X) :
    traceNorm X hX = traceNorm Y (hEq ▸ hX)
```

**`ProbabilisticTheory.tsum_sqrt_abs_norm_sq_eq_traceNorm`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L64).

> The Hilbert–Schmidt square sum of `√|A|` computes the trace norm, in every basis.

```lean
lemma tsum_sqrt_abs_norm_sq_eq_traceNorm {A : H →L[ℂ] H} (hA : IsTraceClass A) {w : Set H}
    (b : HilbertBasis w ℂ H) :
    (∑' i : w, ‖CFC.sqrt (CFC.abs A) (b i)‖ ^ 2) = traceNorm A hA
```

**`ProbabilisticTheory.summable_norm_inner_contraction_of_isTraceClass`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L82).

> The contraction pairing `i ↦ ⟪W eᵢ, A eᵢ⟫` is absolutely summable, for trace-class `A` and any
> contraction `W`.

```lean
lemma summable_norm_inner_contraction_of_isTraceClass {A W : H →L[ℂ] H} (hA : IsTraceClass A)
    (hW : ‖W‖ ≤ 1) {w : Set H} (b : HilbertBasis w ℂ H) :
    Summable (fun i : w => ‖⟪W (b i), A (b i)⟫_ℂ‖)
```

**`ProbabilisticTheory.tsum_norm_inner_contraction_le_traceNorm`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L111).

> **The duality bound**: for trace-class `A`, any contraction `W`, and any basis, the pairing
> `∑ᵢ ‖⟪W eᵢ, A eᵢ⟫‖` never exceeds `‖A‖₁`. This is the single quantitative estimate feeding
> subadditivity of the trace norm, and the general two-sided ideal estimate below.

```lean
lemma tsum_norm_inner_contraction_le_traceNorm {A W : H →L[ℂ] H} (hA : IsTraceClass A)
    (hW : ‖W‖ ≤ 1) {w : Set H} (b : HilbertBasis w ℂ H) :
    (∑' i : w, ‖⟪W (b i), A (b i)⟫_ℂ‖) ≤ traceNorm A hA
```

## B. Attainment at the polar factor and subadditivity

**`ProbabilisticTheory.traceNorm_eq_tsum_norm_inner_polarFactor`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L186).

> The trace-norm diagonal in the basis `b` equals the norm-diagonal pairing against `T`'s own
> polar factor: `⟪eᵢ, |T| eᵢ⟫ = ⟪(polarFactor T) eᵢ, T eᵢ⟫` exactly, and the latter is already a
> nonnegative real.

```lean
lemma traceNorm_eq_tsum_norm_inner_polarFactor {T : H →L[ℂ] H} (hT : IsTraceClass T)
    {w : Set H} (b : HilbertBasis w ℂ H) :
    traceNorm T hT = ∑' i : w, ‖⟪Polar.polarFactor T (b i), T (b i)⟫_ℂ‖
```

**`ProbabilisticTheory.traceNorm_add_le`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L216).

> **The trace norm is subadditive.**

```lean
lemma traceNorm_add_le {T T' : H →L[ℂ] H} (hT : IsTraceClass T) (hT' : IsTraceClass T')
    (hTT' : IsTraceClass (T + T')) :
    traceNorm (T + T') hTT' ≤ traceNorm T hT + traceNorm T' hT'
```

## C. The two-sided ideal estimate

**`ProbabilisticTheory.traceNorm_mul_le_of_isHilbertSchmidt`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L254).

> **Quantitative master lemma**: the trace norm of a product of two Hilbert–Schmidt operators is
> bounded by the product of their Hilbert–Schmidt square-root sums, in any common basis.

```lean
lemma traceNorm_mul_le_of_isHilbertSchmidt {R S : H →L[ℂ] H} (hR : IsHilbertSchmidt R)
    (hS : IsHilbertSchmidt S) (hRS : IsTraceClass (R * S)) {w : Set H} (b : HilbertBasis w ℂ H) :
    traceNorm (R * S) hRS ≤
      Real.sqrt (∑' i : w, ‖R (b i)‖ ^ 2) * Real.sqrt (∑' i : w, ‖S (b i)‖ ^ 2)
```

**`ProbabilisticTheory.traceNorm_mul_mul_le`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean#L306).

> **The two-sided ideal estimate**: `‖A T B‖₁ ≤ ‖A‖ ‖T‖₁ ‖B‖`.

```lean
lemma traceNorm_mul_mul_le {A B T : H →L[ℂ] H} (hT : IsTraceClass T)
    (hABT : IsTraceClass (A * T * B)) :
    traceNorm (A * T * B) hABT ≤ ‖A‖ * traceNorm T hT * ‖B‖
```

## Depends on

- [Hilbert–Schmidt operators](traceclass-hilbertschmidt.md)
- [Polar decomposition of bounded operators](traceclass-polar.md)

## Proof depends on

- [Products of Hilbert–Schmidt operators](traceclass-generalproduct.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/IdealNorm.lean)
