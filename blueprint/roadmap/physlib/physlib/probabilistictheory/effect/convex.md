---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.convex, ProbabilisticTheory.Effect.mix, ProbabilisticTheory.Effect.coe_mix
statement: formalized
proof: formalized
---

# Convexity and mixtures of effects

The module `Physlib.ProbabilisticTheory.Effect.Convex`, [Physlib/ProbabilisticTheory/Effect/Convex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Convex.lean): 3 declarations, 3 with a docstring.

> The effect interval is convex, so effects can be mixed with a given probability.

## i. Overview

> The effect interval `[0, 1]` is convex: randomizing between two effects with some probability
> gives back an effect. Physically, flipping a biased coin to decide which of two measurements to
> actually run is itself a legitimate measurement.

## ii. Key results

> - `Effect.convex` : the effect interval is convex.
> - `Effect.mix` : randomize between two effects with a given probability.

## iv. References

> * None.

## A. Convexity and mixtures of effects

**`ProbabilisticTheory.Effect.convex`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Convex.lean#L52).

> The effect interval is convex.

```lean
lemma convex : Convex ℝ (Effect E)
```

**`ProbabilisticTheory.Effect.mix`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Convex.lean#L55).

> Randomize between two effects with probability `t` of testing the first.

```lean
def mix (e f : Effect E) (t : unitInterval) : Effect E
```

**`ProbabilisticTheory.Effect.coe_mix`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Convex.lean#L61).

> Evaluation of a mixture is the pointwise convex combination.

```lean
lemma coe_mix (e f : Effect E) (t : unitInterval) :
    ((mix e f t : Effect E) : E) = (t : ℝ) • (e : E) + (1 - (t : ℝ)) • (f : E)
```

## Depends on

- [Effects](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Convex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Convex.lean)
