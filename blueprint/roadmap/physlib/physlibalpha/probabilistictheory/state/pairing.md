---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.apply_mem_Icc, ProbabilisticTheory.UnitalPositiveLinearMap.apply_mix, ProbabilisticTheory.UnitalPositiveLinearMap.ext_of_effect_eq_of_nonneg, ProbabilisticTheory.UnitalPositiveLinearMap.ext_of_effect_eq, ProbabilisticTheory.UnitalPositiveLinearMap.injective_apply_effect, ProbabilisticTheory.Effect.dist_eq_sSup_abs_apply, ProbabilisticTheory.Effect.ext_of_forall_apply_eq, ProbabilisticTheory.Effect.injective_apply_state
statement: formalized
proof: formalized
---

# The state–effect pairing (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.State.Pairing`, [PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean): 8 declarations, 8 with a docstring.

> The state–effect pairing is affine, takes values in [0, 1], and separates states and effects.

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

> * None.

## A. State–effect evaluation

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_mem_Icc`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L66).

> State–effect evaluation takes values in `[0, 1]`.

```lean
lemma apply_mem_Icc (ω : 𝓢[ℝ, E]) (e : Effect E) : ω (e : E) ∈ Set.Icc (0 : ℝ) 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_mix`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L70).

> Evaluation is affine in the effect argument.

```lean
lemma apply_mix (ω : 𝓢[ℝ, E]) (e f : Effect E) (t : unitInterval) :
    ω ((Effect.mix e f t : E)) = (t : ℝ) * ω (e : E) + (1 - (t : ℝ)) * ω (f : E)
```

## B. Effects separate states

**`ProbabilisticTheory.UnitalPositiveLinearMap.ext_of_effect_eq_of_nonneg`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L81).

> Two states that agree on all effects agree on every nonnegative element.

```lean
lemma ext_of_effect_eq_of_nonneg {ω φ : 𝓢[ℝ, E]}
    (h : ∀ e : Effect E, ω (e : E) = φ (e : E)) {B : E} (hB : 0 ≤ B) : ω B = φ B
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.ext_of_effect_eq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L87).

> A state is determined by its values on effects.

```lean
lemma ext_of_effect_eq {ω φ : 𝓢[ℝ, E]}
    (h : ∀ e : Effect E, ω (e : E) = φ (e : E)) : ω = φ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.injective_apply_effect`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L94).

> Evaluation on effects is injective on states.

```lean
lemma injective_apply_effect :
    Function.Injective (fun (ω : 𝓢[ℝ, E]) (e : Effect E) => ω (e : E))
```

## C. States separate effects

**`ProbabilisticTheory.Effect.dist_eq_sSup_abs_apply`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L106).

> The distance between two effects is the supremum of the difference in their evaluations over
> all states.

```lean
lemma _root_.ProbabilisticTheory.Effect.dist_eq_sSup_abs_apply [Nontrivial E] (e f : Effect E) :
    Dist.dist e f = sSup (Set.range fun ω : 𝓢[ℝ, E] => |ω (e : E) - ω (f : E)|)
```

**`ProbabilisticTheory.Effect.ext_of_forall_apply_eq`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L112).

> An effect is determined by its values under all states.

```lean
lemma _root_.ProbabilisticTheory.Effect.ext_of_forall_apply_eq {e f : Effect E}
    (h : ∀ ω : 𝓢[ℝ, E], ω (e : E) = ω (f : E)) : e = f
```

**`ProbabilisticTheory.Effect.injective_apply_state`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean#L117).

> Evaluation by states is injective on effects.

```lean
lemma _root_.ProbabilisticTheory.Effect.injective_apply_state :
    Function.Injective (fun (e : Effect E) (ω : 𝓢[ℝ, E]) => ω (e : E))
```

## Depends on

- [Convexity and mixtures of effects](../../../physlib/probabilistictheory/effect/convex.md)
- [The metric space of effects](../../../physlib/probabilistictheory/effect/metric.md)
- [Channels](../channel/basic.md)

## Proof depends on

- [Separation by states (PhyslibAlpha)](separation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Pairing.lean)
