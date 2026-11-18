---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.mix, ProbabilisticTheory.UnitalPositiveLinearMap.mix_apply, ProbabilisticTheory.UnitalPositiveLinearMap.algebraicStateSpace, ProbabilisticTheory.UnitalPositiveLinearMap.convex_algebraicStateSpace, ProbabilisticTheory.UnitalPositiveLinearMap.IsPure, ProbabilisticTheory.UnitalPositiveLinearMap.IsMixed, ProbabilisticTheory.UnitalPositiveLinearMap.mem_openSegment_iff_exists_mix, ProbabilisticTheory.UnitalPositiveLinearMap.isPure_iff_forall_mix_eq
statement: formalized
proof: formalized
---

# Convex state spaces (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.State.Convex`, [PhyslibAlpha/ProbabilisticTheory/State/Convex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean): 11 declarations, 11 with a docstring.

> Mixing states, convexity of the state space, and pure and mixed states.

## i. Overview

> States mix: a probabilistic combination of two states is again a state, and the state space
> embeds convexly into the algebraic dual. A pure state is one that is never a proper mixture of
> two others, an extreme point of that convex set. A mixed state is one that is a mixture.

## ii. Key results

> - `UnitalPositiveLinearMap.mix` : randomize between two states with a given probability.
> - `UnitalPositiveLinearMap.convex_algebraicStateSpace` : the state space is convex in the algebraic
>   dual.
> - `UnitalPositiveLinearMap.isPure_iff_forall_mix_eq` : a state is pure iff every proper mixture
>   producing it is trivial.

## iv. References

> * None.

## A. Mixing states

**`ProbabilisticTheory.UnitalPositiveLinearMap.mix`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L58).

> Randomize between two states with probability `t` of choosing the first.

```lean
def mix (ω φ : 𝓢[ℝ, E]) (t : unitInterval) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.mix_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L66).

> Evaluation of a mixture is the pointwise convex combination.

```lean
lemma mix_apply (ω φ : 𝓢[ℝ, E]) (t : unitInterval) (A : E) :
    mix ω φ t A = (t : ℝ) * ω A + (1 - (t : ℝ)) * φ A
```

## B. The state space

**`ProbabilisticTheory.UnitalPositiveLinearMap.algebraicStateSpace`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L76).

> States embedded into the algebraic dual.

```lean
def algebraicStateSpace : Set (E →ₗ[ℝ] ℝ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.convex_algebraicStateSpace`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L80).

> The state space is convex in the algebraic dual.

```lean
lemma convex_algebraicStateSpace : Convex ℝ (algebraicStateSpace (E := E))
```

## C. Pure and mixed states

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L93).

> A state is pure when it is an extreme point of the state space.

```lean
def IsPure (ω : 𝓢[ℝ, E]) : Prop
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsMixed`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L96).

> A state is mixed when it isn't pure.

```lean
def IsMixed (ω : 𝓢[ℝ, E]) : Prop
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.mem_openSegment_iff_exists_mix`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L100).

> A state lies in the open segment between two states iff it is a proper mixture (`t ≠ 0, 1`) of
> them.

```lean
lemma mem_openSegment_iff_exists_mix (ω φ ψ : 𝓢[ℝ, E]) :
    ω.toLinearMap ∈ openSegment ℝ φ.toLinearMap ψ.toLinearMap ↔
      ∃ t : unitInterval, t ≠ 0 ∧ t ≠ 1 ∧ mix φ ψ t = ω
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isPure_iff_forall_mix_eq`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L120).

> A state is pure iff in every proper mixture (`t ≠ 0, 1`) giving it both components equal it.

```lean
lemma isPure_iff_forall_mix_eq {ω : 𝓢[ℝ, E]} :
    ω.IsPure ↔ ∀ (φ ψ : 𝓢[ℝ, E]) (t : unitInterval), t ≠ 0 → t ≠ 1 →
      mix φ ψ t = ω → φ = ω ∧ ψ = ω
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsPure.eq_of_mix`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L138).

> A proper mixture equal to a pure state has both components equal to it.

```lean
lemma IsPure.eq_of_mix {ω φ ψ : 𝓢[ℝ, E]} (hω : ω.IsPure) (t : unitInterval)
    (ht0 : t ≠ 0) (ht1 : t ≠ 1) (hmix : mix φ ψ t = ω) : φ = ω ∧ ψ = ω
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isPure_iff_mem_extremePoints`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L144).

> Purity transported along an injective map sending mixtures to convex combinations: a state
> is pure exactly when its image is an extreme point of the image of the state space.

```lean
lemma isPure_iff_mem_extremePoints {X : Type*} [AddCommGroup X] [Module ℝ X]
    {F : 𝓢[ℝ, E] → X} (hF : Function.Injective F)
    (hmix : ∀ φ ψ t, F (mix φ ψ t) = (t : ℝ) • F φ + (1 - (t : ℝ)) • F ψ) (ω : 𝓢[ℝ, E]) :
    ω.IsPure ↔ F ω ∈ (Set.range F).extremePoints ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.isMixed_iff_exists_mix_ne`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean#L161).

> A state is mixed iff it is a proper mixture of two different states.

```lean
lemma isMixed_iff_exists_mix_ne {ω : 𝓢[ℝ, E]} :
    ω.IsMixed ↔ ∃ (φ ψ : 𝓢[ℝ, E]) (t : unitInterval), t ≠ 0 ∧ t ≠ 1 ∧
      mix φ ψ t = ω ∧ (φ ≠ ω ∨ ψ ≠ ω)
```

## Depends on

- [Channels](../channel/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/Convex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Convex.lean)
