---
declaration: module
origin: cited
lean: ProbabilisticTheory.TraceClass.trace_rankOne_formula, ProbabilisticTheory.TraceClass.tracePairing_rankOne_left
statement: formalized
proof: formalized
---

# Rank-one operators in the trace pairing

The module `PhyslibAlpha.ProbabilisticTheory.WStarAlgebra.RankOnePairing`, [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/RankOnePairing.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/RankOnePairing.lean): 2 declarations, none with a docstring.

> The trace pairing of a rank-one operator `|x⟩⟨y|` with a trace-class `T` is `⟪y, T x⟫`.

## i. Overview

> For a bounded operator `A` and a trace-class operator `T`, the trace pairing of `A |x⟩⟨y|` with `T`
> is a matrix coefficient. This recovers a predual element from its values on rank-one operators.

## ii. Key results

> - `trace_rankOne_formula` : the trace of a rank-one operator times a trace-class operator.
> - `TraceClass.tracePairing_rankOne_left` : the trace pairing with a rank-one operator.

## iv. References

> * None.

## A. The trace of a rank-one operator

**`ProbabilisticTheory.TraceClass.trace_rankOne_formula`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/RankOnePairing.lean#L55).

```lean
lemma trace_rankOne_formula (x y : H) :
    trace (InnerProductSpace.rankOne ℂ x y) (isTraceClass_rankOne x y) =
      ⟪y, x⟫_ℂ
```

## B. The trace pairing with a rank-one operator

**`ProbabilisticTheory.TraceClass.tracePairing_rankOne_left`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/RankOnePairing.lean#L75).

```lean
lemma tracePairing_rankOne_left (T : TraceClass H) (x y : H) :
    tracePairing (InnerProductSpace.rankOne ℂ x y) T =
      ⟪y, T.1 x⟫_ℂ
```

## Depends on

- [The trace pairing is isometric](tracepairingnorm.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/RankOnePairing.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/RankOnePairing.lean)
