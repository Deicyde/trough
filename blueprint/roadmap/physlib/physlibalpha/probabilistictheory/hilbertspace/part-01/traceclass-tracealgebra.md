---
declaration: module
origin: cited
lean: ProbabilisticTheory.trace_smul, ProbabilisticTheory.trace_add, ProbabilisticTheory.trace_mul_cycle
statement: formalized
proof: formalized
---

# Linearity and cyclicity of the trace

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.TraceAlgebra`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/TraceAlgebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/TraceAlgebra.lean): 3 declarations, 3 with a docstring.

> The trace is linear on trace-class operators and cyclic against bounded operators.

## i. Overview

> The trace is linear on trace-class operators and cyclic against bounded operators: `Tr (A T) = Tr (T
> A)` for trace-class `T` and bounded `A`.

## ii. Key results

> - `trace_add`, `trace_smul` : the trace is linear.
> - `trace_mul_cycle` : the trace is cyclic.

## iv. References

> * None.

## A. Linearity and cyclicity of the trace

**`ProbabilisticTheory.trace_smul`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/TraceAlgebra.lean#L56).

> Scalar homogeneity of the trace, with the canonical trace-class proof for the scaled
> operator.

```lean
lemma trace_smul {T : H →L[ℂ] H} (c : ℂ) (hT : IsTraceClass T) :
    trace (c • T) (isTraceClass_smul c hT) = c * trace T hT
```

### A.1. Additivity and cyclicity

**`ProbabilisticTheory.trace_add`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/TraceAlgebra.lean#L75).

> Additivity of the unconditional trace.

```lean
lemma trace_add {T T' : H →L[ℂ] H} (hT : IsTraceClass T) (hT' : IsTraceClass T') :
    trace (T + T') (isTraceClass_add hT hT') = trace T hT + trace T' hT'
```

**`ProbabilisticTheory.trace_mul_cycle`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/TraceAlgebra.lean#L93).

> Cyclicity of the trace across a bounded factor and a trace-class factor.

```lean
lemma trace_mul_cycle {A T : H →L[ℂ] H} (hT : IsTraceClass T) :
    trace (A * T) (isTraceClass_mul_mul (A := A) (B := 1) hT) =
      trace (T * A) (isTraceClass_mul_mul (A := 1) (B := A) hT)
```

## Depends on

- [The trace-class Banach space](traceclass-banach.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/TraceAlgebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/TraceAlgebra.lean)
