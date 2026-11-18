---
declaration: module
origin: cited
lean: ProbabilisticTheory.TraceClass.isTraceClass_rankOne, ProbabilisticTheory.TraceClass.trace_rankOne, ProbabilisticTheory.TraceClass.tracePairing_rankOne, ProbabilisticTheory.TraceClass.norm_le_tracePairing, ProbabilisticTheory.TraceClass.norm_tracePairing, ProbabilisticTheory.TraceClass.norm_tracePairingContinuousLinearMap, ProbabilisticTheory.TraceClass.tracePairingLinearIsometry, ProbabilisticTheory.TraceClass.tracePairingLinearIsometry_apply
statement: formalized
proof: formalized
---

# The trace pairing is isometric

The module `PhyslibAlpha.ProbabilisticTheory.WStarAlgebra.TracePairingNorm`, [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean): 9 declarations, 3 with a docstring.

> The trace pairing of bounded operators against trace-class operators is an isometry.

## i. Overview

> The trace of `A |x⟩⟨y|` is `⟪y, A x⟫`, so testing the trace pairing of a bounded operator `A` on
> rank-one operators recovers its operator norm. Together with `‖Tr (A ·)‖ ≤ ‖A‖` this shows that the
> trace pairing is an isometry.

## ii. Key results

> - `trace_rankOne` : the trace of a rank-one operator.
> - `TraceClass.norm_tracePairing` : `‖Tr (A ·)‖ = ‖A‖`.
> - `TraceClass.tracePairingLinearIsometry` : the trace pairing as a linear isometry.

## iv. References

> * None.

## A. Rank-one operators are trace class

**`ProbabilisticTheory.TraceClass.isTraceClass_rankOne`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L60).

```lean
lemma isTraceClass_rankOne (x y : H) :
    IsTraceClass (InnerProductSpace.rankOne ℂ x y)
```

**`ProbabilisticTheory.TraceClass.trace_rankOne`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L90).

```lean
lemma trace_rankOne (x y : H) :
    trace (InnerProductSpace.rankOne ℂ x y) (isTraceClass_rankOne x y) =
      ⟪y, x⟫_ℂ
```

## B. The trace pairing with rank-one operators

**`ProbabilisticTheory.TraceClass.tracePairing_rankOne`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L110).

```lean
lemma tracePairing_rankOne (A : H →L[ℂ] H) (x y : H) :
    tracePairing A (ofOperator (InnerProductSpace.rankOne ℂ x y) (isTraceClass_rankOne x y)) =
      ⟪y, A x⟫_ℂ
```

## C. The norm of the trace pairing

**`ProbabilisticTheory.TraceClass.norm_le_tracePairing`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L140).

```lean
lemma norm_le_tracePairing (A : H →L[ℂ] H) :
    ‖A‖ ≤ ‖tracePairing A‖
```

**`ProbabilisticTheory.TraceClass.norm_tracePairing`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L214).

> The concrete trace pairing is isometric; this is the norm half of the `H →L[ℂ] H` predual
> theorem.

```lean
lemma norm_tracePairing (A : H →L[ℂ] H) :
    ‖tracePairing A‖ = ‖A‖
```

**`ProbabilisticTheory.TraceClass.norm_tracePairingContinuousLinearMap`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L219).

> The operator-to-functional map has the same norm as the operator.

```lean
lemma norm_tracePairingContinuousLinearMap (A : H →L[ℂ] H) :
    ‖tracePairingContinuousLinearMap A‖ = ‖A‖
```

## D. The trace pairing as a linear isometry

**`ProbabilisticTheory.TraceClass.tracePairingLinearIsometry`**, a def, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L231).

> The trace pairing, as a linear isometry from bounded operators into the dual of the trace-class
> operators.

```lean
def tracePairingLinearIsometry :
    (H →L[ℂ] H) →ₗᵢ[ℂ] (TraceClass H →L[ℂ] ℂ)
```

**`ProbabilisticTheory.TraceClass.tracePairingLinearIsometry_apply`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L237).

```lean
lemma tracePairingLinearIsometry_apply (A : H →L[ℂ] H) :
    tracePairingLinearIsometry A = tracePairing A
```

**`ProbabilisticTheory.TraceClass.tracePairingLinearIsometry_norm`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean#L240).

```lean
lemma tracePairingLinearIsometry_norm (A : H →L[ℂ] H) :
    ‖tracePairingLinearIsometry A‖ = ‖A‖
```

## Depends on

- [The trace pairing](../hilbertspace/part-01/traceclass-pairing.md)

## Proof depends on

- [Rank-one positive operators](../hilbertspace/part-01/traceclass-rankone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/TracePairingNorm.lean)
