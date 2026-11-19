---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.Effect.convex, PhyslibAlpha.ProbabilisticTheory.Effect.mix, PhyslibAlpha.ProbabilisticTheory.Effect.coe_mix
statement: formalized
proof: formalized
---

# Convexity and mixtures of effects (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.Effect.Convex`, [PhyslibAlpha/ProbabilisticTheory/Effect/Convex.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Convex.lean): 3 declarations, 3 with a docstring.

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

**`PhyslibAlpha.ProbabilisticTheory.Effect.convex`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Convex.lean#L52).

> The effect interval is convex.

```lean
lemma convex : Convex ℝ (Effect E)
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.mix`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Convex.lean#L55).

> Randomize between two effects with probability `t` of testing the first.

```lean
def mix (e f : Effect E) (t : unitInterval) : Effect E
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.coe_mix`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Convex.lean#L61).

> Evaluation of a mixture is the pointwise convex combination.

```lean
lemma coe_mix (e f : Effect E) (t : unitInterval) :
    ((mix e f t : Effect E) : E) = (t : ℝ) • (e : E) + (1 - (t : ℝ)) • (f : E)
```

## Depends on

- [Effects (PhyslibAlpha)](interval.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Effect/Convex.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Convex.lean)
