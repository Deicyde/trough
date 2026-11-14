---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap.apply_mem_Icc, UnitalPositiveLinearMap.apply_mix, UnitalPositiveLinearMap.ext_of_effect_eq_of_nonneg, UnitalPositiveLinearMap.ext_of_effect_eq, UnitalPositiveLinearMap.injective_apply_effect, Effect.dist_eq_sSup_abs_apply, Effect.ext_of_forall_apply_eq, Effect.injective_apply_state
statement: formalized
proof: formalized
---

# The state–effect pairing (Physlib)

The module `Physlib.ProbabilisticTheory.State.Pairing`, [Physlib/ProbabilisticTheory/State/Pairing.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean): 8 declarations, 8 with a docstring.

> State–effect evaluation gives probabilities and separates both states and effects.

## i. Overview

> States and effects are paired by evaluation, `(ω, e) ↦ ω e ∈ [0, 1]`. This pairing is affine in
> both arguments. It also separates both spaces: a state is determined by its values on all
> effects, and an effect is determined by its values under all states. Moreover, the distance
> between two effects is the largest difference in probability that they can produce over all
> states.
>
> Thus states and effects admit faithful representations as probability-valued functions on one
> another.

## ii. Key results

> - `UnitalPositiveLinearMap.apply_mem_Icc` : state–effect evaluation takes values in `[0, 1]`.
> - `UnitalPositiveLinearMap.apply_mix` : evaluation is affine in the effect argument.
> - `UnitalPositiveLinearMap.ext_of_effect_eq` : effects separate states.
> - `Effect.dist_eq_sSup_abs_apply` : effect distance is determined by state evaluations.
> - `Effect.ext_of_forall_apply_eq` : states separate effects.
> - `UnitalPositiveLinearMap.injective_apply_effect` : states embed into functions on effects.
> - `Effect.injective_apply_state` : effects embed into functions on states.

## iv. References

## A. State–effect evaluation

**`UnitalPositiveLinearMap.apply_mem_Icc`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L66).

> State–effect evaluation takes values in `[0, 1]`.

```lean
lemma apply_mem_Icc (ω : 𝓢[ℝ, E]) (e : Effect E) : ω e ∈ Set.Icc 0 1
```

**`UnitalPositiveLinearMap.apply_mix`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L70).

> Evaluation is affine in the effect argument.

```lean
lemma apply_mix (ω : 𝓢[ℝ, E]) (e f : Effect E) (t : unitInterval) :
    ω (Effect.mix e f t) = (t : ℝ) * ω e + (1 - (t : ℝ)) * ω f
```

## B. Effects separate states

**`UnitalPositiveLinearMap.ext_of_effect_eq_of_nonneg`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L81).

> Two states that agree on all effects agree on every nonnegative element.

```lean
lemma ext_of_effect_eq_of_nonneg {ω φ : 𝓢[ℝ, E]}
    (h : ∀ e : Effect E, ω e = φ e) {B : E} (hB : 0 ≤ B) : ω B = φ B
```

**`UnitalPositiveLinearMap.ext_of_effect_eq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L87).

> A state is determined by its values on effects.

```lean
lemma ext_of_effect_eq {ω φ : 𝓢[ℝ, E]}
    (h : ∀ e : Effect E, ω e = φ e) : ω = φ
```

**`UnitalPositiveLinearMap.injective_apply_effect`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L94).

> Evaluation on effects is injective on states.

```lean
lemma injective_apply_effect :
    Function.Injective (fun (ω : 𝓢[ℝ, E]) (e : Effect E) => ω e)
```

## C. States separate effects

**`Effect.dist_eq_sSup_abs_apply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L114).

> The distance between two effects is the supremum of the difference in their evaluations over
> all states.

```lean
lemma dist_eq_sSup_abs_apply [Nontrivial E] (e f : Effect E) :
    Dist.dist e f = sSup (Set.range fun ω : 𝓢[ℝ, E] => |ω e - ω f|)
```

**`Effect.ext_of_forall_apply_eq`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L120).

> An effect is determined by its values under all states.

```lean
lemma ext_of_forall_apply_eq {e f : Effect E}
    (h : ∀ ω : 𝓢[ℝ, E], ω e = ω f) : e = f
```

**`Effect.injective_apply_state`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean#L125).

> Evaluation by states is injective on effects.

```lean
lemma injective_apply_state :
    Function.Injective (fun (e : Effect E) (ω : 𝓢[ℝ, E]) => ω e)
```

## Depends on

- [Positive unital maps](../channel/basic.md)
- [Convexity and mixtures of effects](../effect/convex.md)
- [The metric space of effects](../effect/metric.md)

## Proof depends on

- [Separation by states (Physlib)](separation.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Pairing.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Pairing.lean)
