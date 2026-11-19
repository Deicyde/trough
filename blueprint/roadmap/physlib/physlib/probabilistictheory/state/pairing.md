---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.apply_mem_Icc, ProbabilisticTheory.State.apply_mix, ProbabilisticTheory.State.ext_of_effect_eq, ProbabilisticTheory.Effect.ext_of_forall_apply_eq
statement: formalized
proof: formalized
---

# The state–effect pairing (Physlib)

The module `Physlib.ProbabilisticTheory.State.Pairing`, [Physlib/ProbabilisticTheory/State/Pairing.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Pairing.lean): 4 declarations, 4 with a docstring.

> State–effect evaluation gives probabilities that distinguish states and effects alike.

## i. Overview

> Evaluating an effect in a state gives a probability, and evaluation is affine in the effect.
> A state is determined by its probabilities on all effects. Conversely, an effect is determined
> by its probabilities in all states. The pairing therefore separates both sides.

## ii. Key results

> - `ProbabilisticTheory.State.apply_mem_Icc` : state–effect evaluation takes values in `[0, 1]`.
> - `ProbabilisticTheory.State.apply_mix` : evaluation is affine in the effect argument.
> - `ProbabilisticTheory.State.ext_of_effect_eq` : effects separate states.
> - `ProbabilisticTheory.Effect.ext_of_forall_apply_eq` : states separate effects.

## iv. References

## A. State–effect evaluation

**`ProbabilisticTheory.State.apply_mem_Icc`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Pairing.lean#L56).

> State–effect evaluation takes values in `[0, 1]`.

```lean
lemma apply_mem_Icc (ω : P.State) (e : P.Effect) : ω e ∈ Set.Icc 0 1
```

**`ProbabilisticTheory.State.apply_mix`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Pairing.lean#L60).

> Evaluation is affine in the effect argument.

```lean
lemma apply_mix (ω : P.State) (e f : P.Effect) (t : unitInterval) :
    ω (Effect.mix e f t) = (t : ℝ) * ω e + (1 - (t : ℝ)) * ω f
```

## B. Effects separate states

**`ProbabilisticTheory.State.ext_of_effect_eq`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Pairing.lean#L71).

> A state is determined by its values on effects.

```lean
lemma ext_of_effect_eq {ω φ : P.State} (h : ∀ e : P.Effect, ω e = φ e) : ω = φ
```

## C. States separate effects

**`ProbabilisticTheory.Effect.ext_of_forall_apply_eq`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Pairing.lean#L93).

> An effect is determined by its values under all states.

```lean
lemma ext_of_forall_apply_eq {e f : P.Effect}
    (h : ∀ ω : P.State, ω e = ω f) : e = f
```

## Depends on

- [Convexity and mixtures of effects (Physlib)](../effect/convex.md)
- [States](basic.md)

## Proof depends on

- [Separation by states (Physlib)](separation.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Pairing.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Pairing.lean)
