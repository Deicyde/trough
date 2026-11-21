---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.convex, ProbabilisticTheory.Effect.mix, ProbabilisticTheory.Effect.coe_mix
statement: formalized
proof: formalized
---

# Convexity and mixtures of effects (Physlib)

The module `Physlib.ProbabilisticTheory.Effect.Convex`, [Physlib/ProbabilisticTheory/Effect/Convex.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Convex.lean): 3 declarations, 3 with a docstring.

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

**`ProbabilisticTheory.Effect.convex`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Convex.lean#L50).

> The effect interval is convex.

```lean
lemma convex : Convex ℝ P.Effect
```

**`ProbabilisticTheory.Effect.mix`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Convex.lean#L53).

> Randomize between two effects with probability `t` of testing the first.

```lean
def mix (e f : P.Effect) (t : unitInterval) : P.Effect
```

**`ProbabilisticTheory.Effect.coe_mix`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Convex.lean#L59).

> Evaluation of a mixture is the pointwise convex combination.

```lean
lemma coe_mix (e f : P.Effect) (t : unitInterval) :
    ((mix e f t : P.Effect) : P.Observables) = (t : ℝ) • e.1 + (1 - (t : ℝ)) • f.1
```

## Depends on

- [Effects (Physlib)](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Convex.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/Effect/Convex.lean)
