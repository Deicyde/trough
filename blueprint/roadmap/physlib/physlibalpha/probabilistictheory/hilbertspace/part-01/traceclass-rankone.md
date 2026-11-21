---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.rankOne_self_diagonal, PhyslibAlpha.ProbabilisticTheory.isTraceClass_rankOne_self, PhyslibAlpha.ProbabilisticTheory.trace_rankOne_self, PhyslibAlpha.ProbabilisticTheory.traceNorm_rankOne_self
statement: formalized
proof: formalized
---

# Rank-one positive operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.RankOne`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean): 4 declarations, none with a docstring.

> The rank-one operator `|x⟩⟨x|` is trace class with trace and trace norm `‖x‖²`.

## i. Overview

> The positive rank-one operator `|x⟩⟨x|` is trace class, with trace and trace norm `‖x‖²`. This is
> the normalization of vector states.

## ii. Key results

> - `isTraceClass_rankOne_self` : `|x⟩⟨x|` is trace class.
> - `trace_rankOne_self`, `traceNorm_rankOne_self` : its trace and trace norm are `‖x‖²`.

## iv. References

> * None.

## A. Rank-one positive operators

**`PhyslibAlpha.ProbabilisticTheory.rankOne_self_diagonal`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean#L53).

```lean
lemma rankOne_self_diagonal {x : H} {w : Set H}
    (b : HilbertBasis w ℂ H) (i : w) :
    (⟪b i, (InnerProductSpace.rankOne ℂ x x) (b i)⟫_ℂ).re =
      ‖⟪x, b i⟫_ℂ‖ ^ 2
```

**`PhyslibAlpha.ProbabilisticTheory.isTraceClass_rankOne_self`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean#L62).

```lean
lemma isTraceClass_rankOne_self (x : H) :
    IsTraceClass (InnerProductSpace.rankOne ℂ x x)
```

**`PhyslibAlpha.ProbabilisticTheory.trace_rankOne_self`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean#L73).

```lean
lemma trace_rankOne_self (x : H) :
    trace (InnerProductSpace.rankOne ℂ x x) (isTraceClass_rankOne_self x) =
      (‖x‖ ^ 2 : ℝ)
```

**`PhyslibAlpha.ProbabilisticTheory.traceNorm_rankOne_self`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean#L90).

```lean
lemma traceNorm_rankOne_self (x : H) :
    traceNorm (InnerProductSpace.rankOne ℂ x x) (isTraceClass_rankOne_self x) =
      ‖x‖ ^ 2
```

## Depends on

- [Trace-class operators](traceclass-basic.md)

## Proof depends on

- [Basis independence of the trace](traceclass-generalideal.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/RankOne.lean)
