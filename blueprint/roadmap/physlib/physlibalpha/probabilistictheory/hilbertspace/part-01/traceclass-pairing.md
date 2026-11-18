---
declaration: module
origin: cited
lean: ProbabilisticTheory.TraceClass.norm_trace_le, ProbabilisticTheory.TraceClass.trace_transport, ProbabilisticTheory.TraceClass.isTraceClass_mul_coe, ProbabilisticTheory.TraceClass.tracePairingLinearMap, ProbabilisticTheory.TraceClass.tracePairingLinearMap_apply, ProbabilisticTheory.TraceClass.norm_tracePairingLinearMap_apply_le, ProbabilisticTheory.TraceClass.tracePairing, ProbabilisticTheory.TraceClass.tracePairing_apply
statement: formalized
proof: formalized
---

# The trace pairing

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.Pairing`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean): 12 declarations, 9 with a docstring.

> The trace pairing `T ↦ Tr (A T)` as a bounded functional on trace-class operators.

## i. Overview

> A bounded operator `A` defines a bounded functional `T ↦ Tr (A T)` on the trace-class operators, of
> norm at most `‖A‖`. The assignment `A ↦ Tr (A ·)` is itself a bounded linear map from bounded
> operators to the dual of `𝒮₁(H)`.

## ii. Key results

> - `norm_trace_le` : `‖Tr T‖ ≤ ‖T‖₁`.
> - `TraceClass.tracePairing` : the functional `T ↦ Tr (A T)`.
> - `TraceClass.norm_tracePairing_le` : its norm is at most `‖A‖`.
> - `TraceClass.tracePairingContinuousLinearMap` : the trace pairing as a bounded linear map into the
>   dual.

## iv. References

> * None.

## A. Trace bounds and transport

**`ProbabilisticTheory.TraceClass.norm_trace_le`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L63).

> **The trace is dominated by the trace norm**, for an arbitrary (not necessarily positive or
> self-adjoint) trace-class operator. Proved from the duality bound
> `tsum_norm_inner_contraction_le_traceNorm` at the identity contraction.

```lean
lemma norm_trace_le {T : H →L[ℂ] H} (hT : IsTraceClass T) : ‖trace T hT‖ ≤ traceNorm T hT
```

**`ProbabilisticTheory.TraceClass.trace_transport`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L77).

> Transporting `trace` across an equality of the underlying operator. Needed because `rw` cannot
> rewrite `trace`'s operator argument directly (the motive depends on the witness proof).

```lean
lemma trace_transport {X Y : H →L[ℂ] H} (hEq : X = Y) (hX : IsTraceClass X) :
    trace X hX = trace Y (hEq ▸ hX)
```

**`ProbabilisticTheory.TraceClass.isTraceClass_mul_coe`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L83).

> Every trace-class `T.1` sandwiched by a bounded `A` on the left (and `1` on the right) is
> trace class: the general two-sided ideal estimate, specialized.

```lean
lemma isTraceClass_mul_coe (A : H →L[ℂ] H) (T : TraceClass H) : IsTraceClass (A * T.1)
```

## B. The trace pairing at a fixed operator

**`ProbabilisticTheory.TraceClass.tracePairingLinearMap`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L95).

> **The trace pairing at a fixed bounded operator `A`**, `T ↦ Tr(A T)`, as a `ℂ`-linear map on
> the trace-class Banach space.

```lean
def tracePairingLinearMap (A : H →L[ℂ] H) : TraceClass H →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.TraceClass.tracePairingLinearMap_apply`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L120).

```lean
lemma tracePairingLinearMap_apply (A : H →L[ℂ] H) (T : TraceClass H) :
    tracePairingLinearMap A T = trace (A * T.1) (isTraceClass_mul_coe A T)
```

**`ProbabilisticTheory.TraceClass.norm_tracePairingLinearMap_apply_le`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L125).

> **The trace pairing is bounded**: `‖φ_A T‖ ≤ ‖A‖ ‖T‖₁`. Combines `norm_trace_le` with the
> general two-sided ideal norm estimate `traceNorm_mul_mul_le`.

```lean
lemma norm_tracePairingLinearMap_apply_le (A : H →L[ℂ] H) (T : TraceClass H) :
    ‖tracePairingLinearMap A T‖ ≤ ‖A‖ * ‖T‖
```

**`ProbabilisticTheory.TraceClass.tracePairing`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L142).

> **The trace pairing `T ↦ Tr(A T)`, as a continuous (bounded) linear functional** on the
> trace-class Banach space.

```lean
def tracePairing (A : H →L[ℂ] H) : TraceClass H →L[ℂ] ℂ
```

**`ProbabilisticTheory.TraceClass.tracePairing_apply`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L145).

```lean
lemma tracePairing_apply (A : H →L[ℂ] H) (T : TraceClass H) :
    tracePairing A T = trace (A * T.1) (isTraceClass_mul_coe A T)
```

**`ProbabilisticTheory.TraceClass.norm_tracePairing_le`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L149).

> The trace pairing's operator norm is bounded by `‖A‖`.

```lean
lemma norm_tracePairing_le (A : H →L[ℂ] H) : ‖tracePairing A‖ ≤ ‖A‖
```

## C. The trace pairing as a bounded linear map

**`ProbabilisticTheory.TraceClass.tracePairingLinear`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L160).

> **`A ↦ φ_A` is itself a `ℂ`-linear map** from `H →L[ℂ] H` into the strong dual of the
> trace-class Banach space.

```lean
def tracePairingLinear : (H →L[ℂ] H) →ₗ[ℂ] (TraceClass H →L[ℂ] ℂ)
```

**`ProbabilisticTheory.TraceClass.tracePairingContinuousLinearMap`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L185).

> The trace pairing `A ↦ (T ↦ Tr (A T))`, as a bounded linear map from bounded operators to the
> dual of the trace-class operators.

```lean
def tracePairingContinuousLinearMap : (H →L[ℂ] H) →L[ℂ] (TraceClass H →L[ℂ] ℂ)
```

**`ProbabilisticTheory.TraceClass.tracePairingContinuousLinearMap_apply`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean#L191).

```lean
lemma tracePairingContinuousLinearMap_apply (A : H →L[ℂ] H) :
    tracePairingContinuousLinearMap A = tracePairing A
```

## Depends on

- [The trace-class Banach space](traceclass-banach.md)

## Proof depends on

- [Linearity and cyclicity of the trace](traceclass-tracealgebra.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Pairing.lean)
