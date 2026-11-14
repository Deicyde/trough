---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsTraceClass, ProbabilisticTheory.hasSum_norm_sq_inner_basis, ProbabilisticTheory.hasSum_norm_sq_apply_of_selfAdjoint, ProbabilisticTheory.summable_inner_abs_of_hilbertBasis, ProbabilisticTheory.isTraceClass_iff, ProbabilisticTheory.isTraceClass_of_finiteDimensional, ProbabilisticTheory.trace_eq_sum_inner_hilbertBasis_of_finiteDimensional, ProbabilisticTheory.traceNorm
statement: formalized
proof: formalized
---

# Trace-class operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.Basic`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean): 24 declarations, 18 with a docstring.

> Defines trace-class operators, their trace norm and trace, and shows basis independence.

## i. Overview

> For a bounded operator `T` on a complex Hilbert space, `|T| = √(T⋆T)` is its absolute value. `T` is
> trace class when the diagonal sum `∑ᵢ ⟪eᵢ, |T| eᵢ⟫` converges for a Hilbert basis `{eᵢ}`. The sum is
> the trace norm `‖T‖₁`, and `Tr T = ∑ᵢ ⟪eᵢ, T eᵢ⟫` is the trace.
>
> For positive and self-adjoint operators the diagonal sums do not depend on the basis. The proof
> writes `⟪eᵢ, S eᵢ⟫ = ‖√S eᵢ‖²`, expands in a second basis by Parseval and exchanges the two
> nonnegative sums. In finite dimension the trace agrees with the linear-algebra trace.
>
> A projection has finite multiplicity when it is trace class, that is, when its range is finite
> dimensional.

## ii. Key results

> - `IsTraceClass` : a bounded operator is trace class.
> - `traceNorm`, `trace` : the trace norm and the trace.
> - `summable_inner_abs_of_hilbertBasis` : trace class does not depend on the basis.
> - `traceNorm_eq_of_hilbertBasis` : the trace norm does not depend on the basis.
> - `trace_eq_of_hilbertBasis_of_isSelfAdjoint` : the trace of a self-adjoint trace-class operator
>   does not depend on the basis.
> - `trace_eq_sum_inner_hilbertBasis_of_finiteDimensional` : in finite dimension the linear-algebra
>   trace is the diagonal sum.
> - `HasFiniteMultiplicity` : a projection of finite rank.

## iv. References

> * None.

## A. Trace class

**`ProbabilisticTheory.IsTraceClass`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L72).

> **`T` is trace class**: `∑ᵢ ⟪eᵢ, |T| eᵢ⟫` converges for some Hilbert basis `{eᵢ}` of `H`
> (`|T| := CFC.abs T`, Mathlib's continuous functional calculus absolute value `√(T⋆T)`). By the
> basis-independence theorem below, "some" is equivalent to "every".

```lean
def IsTraceClass (T : H →L[ℂ] H) : Prop
```

### A.1. Basis independence

> The proofs use the square root of the functional calculus and Parseval's identity for Hilbert
> bases.

**`ProbabilisticTheory.hasSum_norm_sq_inner_basis`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L82).

> **Parseval's identity**: `∑ᵢ |⟪eᵢ, y⟫|² = ‖y‖²` for a Hilbert basis `{eᵢ}`.

```lean
lemma hasSum_norm_sq_inner_basis {w : Set H} (b : HilbertBasis w ℂ H) (y : H) :
    HasSum (fun i : w => ‖⟪b i, y⟫_ℂ‖ ^ 2) (‖y‖ ^ 2)
```

**`ProbabilisticTheory.hasSum_norm_sq_apply_of_selfAdjoint`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L95).

> For self-adjoint `S`, the sum `∑ᵢ ‖S eᵢ‖²` does not depend on the Hilbert basis.

```lean
lemma hasSum_norm_sq_apply_of_selfAdjoint {S : H →L[ℂ] H} (hS : IsSelfAdjoint S)
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H)
    (hb : Summable (fun i : w => ‖S (b i)‖ ^ 2)) :
    HasSum (fun j : w' => ‖S (c j)‖ ^ 2) (∑' i : w, ‖S (b i)‖ ^ 2)
```

**`ProbabilisticTheory.summable_inner_abs_of_hilbertBasis`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L153).

> **Trace class does not depend on the basis**: the diagonal of `|T|` is summable in every Hilbert
> basis.

```lean
lemma summable_inner_abs_of_hilbertBasis {T : H →L[ℂ] H} (h : IsTraceClass T) {w : Set H}
    (b : HilbertBasis w ℂ H) :
    Summable (fun i => (⟪b i, CFC.abs T (b i)⟫_ℂ).re)
```

**`ProbabilisticTheory.isTraceClass_iff`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L182).

> An operator is trace class iff the diagonal of `|T|` is summable in every Hilbert basis.

```lean
lemma isTraceClass_iff {T : H →L[ℂ] H} :
    IsTraceClass T ↔
      ∀ (w : Set H) (b : HilbertBasis w ℂ H),
        Summable (fun i => (⟪b i, CFC.abs T (b i)⟫_ℂ).re)
```

**`ProbabilisticTheory.isTraceClass_of_finiteDimensional`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L194).

> Every operator on a finite-dimensional Hilbert space is trace class.

```lean
lemma isTraceClass_of_finiteDimensional [FiniteDimensional ℂ H] (T : H →L[ℂ] H) :
    IsTraceClass T
```

**`ProbabilisticTheory.trace_eq_sum_inner_hilbertBasis_of_finiteDimensional`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L205).

> The ordinary finite-dimensional trace is the diagonal sum in any Hilbert basis.

```lean
lemma trace_eq_sum_inner_hilbertBasis_of_finiteDimensional
    [FiniteDimensional ℂ H] (T : H →L[ℂ] H) {w : Set H} (b : HilbertBasis w ℂ H) :
    LinearMap.trace ℂ H T.toLinearMap = ∑' i : w, ⟪b i, T (b i)⟫_ℂ
```

**`ProbabilisticTheory.traceNorm`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L217).

> The trace norm `‖T‖₁ := ∑ᵢ ⟪eᵢ, |T| eᵢ⟫`, computed via a chosen witness Hilbert basis (any
> basis gives the same value, by `summable_inner_abs_of_hilbertBasis` — this definition just needs
> *a* witness to compute with).

```lean
def traceNorm (T : H →L[ℂ] H) (h : IsTraceClass T) : ℝ
```

**`ProbabilisticTheory.traceNorm_congr`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L223).

> The witness proof argument of `traceNorm` is immaterial.  This small lemma is useful when
> transporting a trace-class operator through a construction that produces a new proof of the same
> proposition.

```lean
lemma traceNorm_congr {T : H →L[ℂ] H} {h₁ h₂ : IsTraceClass T} :
    traceNorm T h₁ = traceNorm T h₂
```

**`ProbabilisticTheory.trace`**, a def, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L230).

> **The trace** `Tr T = ∑ᵢ ⟪eᵢ, T eᵢ⟫` of a trace-class operator, in the basis witnessing that it
> is trace class.

```lean
def trace (T : H →L[ℂ] H) (h : IsTraceClass T) : ℂ
```

**`ProbabilisticTheory.trace_congr`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L234).

> The trace does not depend on the proof that the operator is trace class.

```lean
lemma trace_congr {T : H →L[ℂ] H} {h₁ h₂ : IsTraceClass T} :
    trace T h₁ = trace T h₂
```

**`ProbabilisticTheory.traceNorm_eq_of_hilbertBasis`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L242).

> The trace norm is independent of the witness basis used in `IsTraceClass`.  This is the
> strong form of `summable_inner_abs_of_hilbertBasis`: the square-root/Parseval argument identifies
> the actual sums, not merely their convergence.

```lean
lemma traceNorm_eq_of_hilbertBasis {T : H →L[ℂ] H} (h : IsTraceClass T) {w : Set H}
    (b : HilbertBasis w ℂ H) :
    traceNorm T h = ∑' i, (⟪b i, CFC.abs T (b i)⟫_ℂ).re
```

**`ProbabilisticTheory.real_inner_nonneg_of_nonneg`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L288).

```lean
lemma real_inner_nonneg_of_nonneg {T : H →L[ℂ] H} (hT : 0 ≤ T) (x : H) :
    0 ≤ (⟪x, T x⟫_ℂ).re
```

**`ProbabilisticTheory.traceNorm_nonneg`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L300).

> The trace norm is nonnegative.  This is exposed separately from its basis-independence result
> so norm estimates can use it without unpacking the chosen Hilbert-basis witness.

```lean
lemma traceNorm_nonneg (T : H →L[ℂ] H) (h : IsTraceClass T) : 0 ≤ traceNorm T h
```

**`ProbabilisticTheory.real_inner_mono_of_le`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L306).

```lean
lemma real_inner_mono_of_le {P Q : H →L[ℂ] H} (hPQ : P ≤ Q) (x : H) :
    (⟪x, P x⟫_ℂ).re ≤ (⟪x, Q x⟫_ℂ).re
```

**`ProbabilisticTheory.isTraceClass_posPart_of_isSelfAdjoint`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L319).

```lean
lemma isTraceClass_posPart_of_isSelfAdjoint {T : H →L[ℂ] H} (hT : IsSelfAdjoint T)
    (h : IsTraceClass T) : IsTraceClass T⁺
```

**`ProbabilisticTheory.isTraceClass_negPart_of_isSelfAdjoint`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L335).

```lean
lemma isTraceClass_negPart_of_isSelfAdjoint {T : H →L[ℂ] H} (hT : IsSelfAdjoint T)
    (h : IsTraceClass T) : IsTraceClass T⁻
```

**`ProbabilisticTheory.summable_inner_of_nonneg`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L351).

```lean
lemma summable_inner_of_nonneg {T : H →L[ℂ] H} (hT : 0 ≤ T) (h : IsTraceClass T)
    {w : Set H} (b : HilbertBasis w ℂ H) :
    Summable (fun i => ⟪b i, T (b i)⟫_ℂ)
```

> Basis-independent trace for positive trace-class operators.
>
> For a positive operator the absolute value is the operator itself.  Taking its continuous-
> functional-calculus square root turns every diagonal coefficient into a squared norm, so the
> Parseval double-sum theorem already proved above gives the same sum in every Hilbert basis.  This
> is the positive case needed by density operators and does not use polar decomposition.

**`ProbabilisticTheory.trace_eq_of_hilbertBasis_of_nonneg`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L386).

```lean
lemma trace_eq_of_hilbertBasis_of_nonneg {T : H →L[ℂ] H} (hT : 0 ≤ T)
    (h : IsTraceClass T) {w : Set H} (b : HilbertBasis w ℂ H) :
    trace T h = ∑' i, ⟪b i, T (b i)⟫_ℂ
```

**`ProbabilisticTheory.trace_eq_of_hilbertBasis_of_isSelfAdjoint`**, a lemma, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L435).

> Basis-independent trace for self-adjoint trace-class operators.  The proof reduces to the
> positive theorem through the continuous-functional-calculus decomposition `T = T⁺ - T⁻`; no
> polar decomposition is needed for this self-adjoint case.

```lean
lemma trace_eq_of_hilbertBasis_of_isSelfAdjoint {T : H →L[ℂ] H} (hT : IsSelfAdjoint T)
    (h : IsTraceClass T) {w : Set H} (b : HilbertBasis w ℂ H) :
    trace T h = ∑' i, ⟪b i, T (b i)⟫_ℂ
```

## B. Finite multiplicity

**`ProbabilisticTheory.HasFiniteMultiplicity`**, a def, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L485).

> A projection has finite multiplicity when it is trace class.

```lean
def HasFiniteMultiplicity (p : H →L[ℂ] H) : Prop
```

**`ProbabilisticTheory.HasFiniteMultiplicity.finiteDimensional_range`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L488).

> A projection of finite multiplicity has finite-dimensional range.

```lean
lemma HasFiniteMultiplicity.finiteDimensional_range {p : H →L[ℂ] H}
    (hp : HasFiniteMultiplicity p) :
    FiniteDimensional ℂ (LinearMap.range p.toLinearMap)
```

**`ProbabilisticTheory.HasFiniteMultiplicity.trace_eq_finrank_range`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L543).

> A finite-multiplicity projection has the expected trace.  The basis calculation is finite-rank:
> extend an orthonormal basis of the range to one of `H`; the projection vanishes on the complementary
> basis vectors and is the identity on the range basis.

```lean
lemma HasFiniteMultiplicity.trace_eq_finrank_range
    {p : H →L[ℂ] H} (hp : HasFiniteMultiplicity p) :
    trace p hp.2 = (Module.finrank ℂ (LinearMap.range p.toLinearMap) : ℂ)
```

**`ProbabilisticTheory.HasFiniteMultiplicity.trace_eq_finrank_range_of_finiteDimensional`**, a lemma, [line 704](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean#L704).

> In finite dimension, the trace of a projection is the dimension of its range.

```lean
lemma HasFiniteMultiplicity.trace_eq_finrank_range_of_finiteDimensional
    [FiniteDimensional ℂ H] {p : H →L[ℂ] H} (hp : HasFiniteMultiplicity p) :
    trace p hp.2 = (Module.finrank ℂ (LinearMap.range p.toLinearMap) : ℂ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Basic.lean)
