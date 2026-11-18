---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.toWeight_isNormal
statement: formalized
proof: formalized
---

# Normal states give normal weights

The module `PhyslibAlpha.ProbabilisticTheory.State.NormalEquivalence`, [PhyslibAlpha/ProbabilisticTheory/State/NormalEquivalence.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/NormalEquivalence.lean): 1 declaration, 1 with a docstring.

> The weight of a normal state is a normal weight.

## i. Overview

> The weight of a normal state is normal: suprema of directed families of nonnegative observables are
> suprema in the whole space, where the state is normal.

## ii. Key results

> - `UnitalPositiveLinearMap.IsNormal.toWeight_isNormal` : normal states give normal weights.

## iv. References

> * None.

## A. Normal weights from normal states

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.toWeight_isNormal`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/NormalEquivalence.lean#L51).

> A normal state induces a normal weight.  No new normality predicate is introduced: the proof
> transports a nonempty directed positive set to `E`, applies the canonical state predicate, and
> then transports the nonnegative scalar supremum through `ENNReal.ofReal`.

```lean
lemma IsNormal.toWeight_isNormal {s : 𝓢[ℝ, E]} (hs : s.IsNormal) : s.toWeight.IsNormal
```

## Depends on

- [Normal channels](../channel/normal.md)
- [States and finite normalized weights](weightequivalence.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/NormalEquivalence.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/NormalEquivalence.lean)
