---
declaration: module
origin: cited
lean: ProbabilisticTheory.sqrt_abs_diagonal_eq_norm_sq, ProbabilisticTheory.isHilbertSchmidt_sqrt_abs_of_isTraceClass, ProbabilisticTheory.summable_trace_diagonal_of_isTraceClass, ProbabilisticTheory.tsum_diagonal_eq_of_isTraceClass, ProbabilisticTheory.trace_eq_of_hilbertBasis_unconditional, ProbabilisticTheory.trace_eq_of_hilbertBasis
statement: formalized
proof: formalized
---

# Basis independence of the trace

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.GeneralIdeal`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean): 6 declarations, 1 with a docstring.

> The trace of every trace-class operator is an absolutely summable, basis-independent sum.

## i. Overview

> For a trace-class operator `T`, `√|T|` is Hilbert–Schmidt, so the diagonal of `T = (U √|T|) √|T|` is
> a diagonal of a product of Hilbert–Schmidt operators. This shows that the trace of every trace-class
> operator is an absolutely convergent sum whose value does not depend on the basis.

## ii. Key results

> - `isHilbertSchmidt_sqrt_abs_of_isTraceClass` : `√|T|` is Hilbert–Schmidt.
> - `summable_trace_diagonal_of_isTraceClass` : the diagonal of a trace-class operator is absolutely
>   summable.
> - `trace_eq_of_hilbertBasis` : the trace does not depend on the basis.

## iv. References

> * None.

## A. The Hilbert–Schmidt square root of `|T|`

**`ProbabilisticTheory.sqrt_abs_diagonal_eq_norm_sq`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean#L58).

```lean
lemma sqrt_abs_diagonal_eq_norm_sq {T : H →L[ℂ] H} {w : Set H} (b : HilbertBasis w ℂ H)
    (i : w) :
    (⟪b i, CFC.abs T (b i)⟫_ℂ).re = ‖(CFC.sqrt (CFC.abs T)) (b i)‖ ^ 2
```

**`ProbabilisticTheory.isHilbertSchmidt_sqrt_abs_of_isTraceClass`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean#L76).

```lean
lemma isHilbertSchmidt_sqrt_abs_of_isTraceClass {T : H →L[ℂ] H} (hT : IsTraceClass T) :
    IsHilbertSchmidt (CFC.sqrt (CFC.abs T))
```

## B. Basis independence of the trace

**`ProbabilisticTheory.summable_trace_diagonal_of_isTraceClass`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean#L89).

```lean
lemma summable_trace_diagonal_of_isTraceClass {T : H →L[ℂ] H} (hT : IsTraceClass T)
    {w : Set H} (b : HilbertBasis w ℂ H) :
    Summable (fun i : w => ⟪b i, T (b i)⟫_ℂ)
```

**`ProbabilisticTheory.tsum_diagonal_eq_of_isTraceClass`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean#L103).

```lean
lemma tsum_diagonal_eq_of_isTraceClass {T : H →L[ℂ] H} (hT : IsTraceClass T)
    {w w' : Set H} (b : HilbertBasis w ℂ H) (c : HilbertBasis w' ℂ H) :
    (∑' i : w, ⟪b i, T (b i)⟫_ℂ) = ∑' j : w', ⟪c j, T (c j)⟫_ℂ
```

**`ProbabilisticTheory.trace_eq_of_hilbertBasis_unconditional`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean#L121).

```lean
lemma trace_eq_of_hilbertBasis_unconditional {T : H →L[ℂ] H} (hT : IsTraceClass T) {w : Set H}
    (b : HilbertBasis w ℂ H) :
    trace T hT = ∑' i : w, ⟪b i, T (b i)⟫_ℂ
```

**`ProbabilisticTheory.trace_eq_of_hilbertBasis`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean#L131).

> **Basis-independent trace evaluation for an arbitrary trace-class operator.** Unlike the
> witness-basis definition, this requires no self-adjointness/positivity hypothesis.

```lean
lemma trace_eq_of_hilbertBasis {T : H →L[ℂ] H} (hT : IsTraceClass T) {w : Set H}
    (b : HilbertBasis w ℂ H) :
    trace T hT = ∑' i : w, ⟪b i, T (b i)⟫_ℂ
```

## Depends on

- [Hilbert–Schmidt operators](traceclass-hilbertschmidt.md)

## Proof depends on

- [Polar decomposition of bounded operators](traceclass-polar.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralIdeal.lean)
