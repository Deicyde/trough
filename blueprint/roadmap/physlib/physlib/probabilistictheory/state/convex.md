---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap.mix, UnitalPositiveLinearMap.mix_apply, UnitalPositiveLinearMap.toLinearMap_mix, UnitalPositiveLinearMap.mix_symm, UnitalPositiveLinearMap.stateSpace, UnitalPositiveLinearMap.stateSpace_convex, UnitalPositiveLinearMap.IsPure, UnitalPositiveLinearMap.IsMixed
statement: formalized
proof: formalized
---

# Convex state spaces

The module `Physlib.ProbabilisticTheory.State.Convex`, [Physlib/ProbabilisticTheory/State/Convex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean): 12 declarations, 12 with a docstring.

> Convexity of the state space and its pure and mixed states.

## i. Overview

> States mix: a probabilistic combination of two states is again a state, and the state space
> embeds convexly into the algebraic dual. A pure state is one that's never a genuine mixture of
> two others, an extreme point of that convex set. A mixed state is one that is a mixture.

## ii. Key results

> - `UnitalPositiveLinearMap.mix` : randomize between two states with a given probability.
> - `UnitalPositiveLinearMap.stateSpace_convex` : the state space is convex in the algebraic dual.
> - `UnitalPositiveLinearMap.IsPure` : pure states are extreme points of the state space.
> - `UnitalPositiveLinearMap.isPure_iff_forall_mix_eq` : a pure state admits only trivial
>   genuine mixtures.
> - `UnitalPositiveLinearMap.isMixed_iff_exists_mem_openSegment` : mixed states lie between
>   two other states.

## iv. References

## A. Mixing states

**`UnitalPositiveLinearMap.mix`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L59).

> Randomize between two states with probability `t` of choosing the first, so
> `t • ω + σ t • φ` with `σ t = 1 - t`.

```lean
def mix (ω φ : 𝓢[ℝ, E]) (t : unitInterval) : 𝓢[ℝ, E]
```

**`UnitalPositiveLinearMap.mix_apply`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L65).

> Evaluation of a mixture is the pointwise convex combination.

```lean
lemma mix_apply (ω φ : 𝓢[ℝ, E]) (t : unitInterval) (A : E) :
    mix ω φ t A = (t : ℝ) * ω A + (1 - (t : ℝ)) * φ A
```

**`UnitalPositiveLinearMap.toLinearMap_mix`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L70).

> The underlying linear map of a mixture is the corresponding combination of linear maps.

```lean
lemma toLinearMap_mix (ω φ : 𝓢[ℝ, E]) (t : unitInterval) :
    (mix ω φ t).toLinearMap = (t : ℝ) • ω.toLinearMap + (1 - (t : ℝ)) • φ.toLinearMap
```

**`UnitalPositiveLinearMap.mix_symm`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L76).

> Swapping the two states swaps the weights: `σ` is the symmetry of the interval.

```lean
lemma mix_symm (ω φ : 𝓢[ℝ, E]) (t : unitInterval) : mix ω φ t = mix φ ω (σ t)
```

## B. The state space

**`UnitalPositiveLinearMap.stateSpace`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L87).

> States embedded into the algebraic dual.

```lean
def stateSpace : Set (E →ₗ[ℝ] ℝ)
```

**`UnitalPositiveLinearMap.stateSpace_convex`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L91).

> The state space is convex in the algebraic dual.

```lean
lemma stateSpace_convex : Convex ℝ (stateSpace (E := E))
```

## C. Pure and mixed states

**`UnitalPositiveLinearMap.IsPure`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L104).

> A state is pure when it is an extreme point of the state space.

```lean
def IsPure (ω : 𝓢[ℝ, E]) : Prop
```

**`UnitalPositiveLinearMap.IsMixed`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L107).

> A state is mixed when it isn't pure.

```lean
def IsMixed (ω : 𝓢[ℝ, E]) : Prop
```

**`UnitalPositiveLinearMap.isPure_iff_forall_mem_openSegment`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L110).

> A state is pure exactly when any open segment containing it has both endpoints equal to it.

```lean
lemma isPure_iff_forall_mem_openSegment {ω : 𝓢[ℝ, E]} :
    ω.IsPure ↔ ∀ φ ψ : 𝓢[ℝ, E],
      ω.toLinearMap ∈ openSegment ℝ φ.toLinearMap ψ.toLinearMap → φ = ω ∧ ψ = ω
```

**`UnitalPositiveLinearMap.isMixed_iff_exists_mem_openSegment`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L117).

> A state is mixed exactly when it lies in an open segment with a different endpoint.

```lean
lemma isMixed_iff_exists_mem_openSegment {ω : 𝓢[ℝ, E]} :
    ω.IsMixed ↔ ∃ φ ψ : 𝓢[ℝ, E],
      ω.toLinearMap ∈ openSegment ℝ φ.toLinearMap ψ.toLinearMap ∧ (φ ≠ ω ∨ ψ ≠ ω)
```

**`UnitalPositiveLinearMap.mem_openSegment_iff_exists_mix`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L123).

> Open segments between states consist exactly of their genuine mixtures.

```lean
lemma mem_openSegment_iff_exists_mix (ω φ ψ : 𝓢[ℝ, E]) :
    ω.toLinearMap ∈ openSegment ℝ φ.toLinearMap ψ.toLinearMap ↔
      ∃ t : unitInterval, 0 < t ∧ t < 1 ∧ mix φ ψ t = ω
```

**`UnitalPositiveLinearMap.isPure_iff_forall_mix_eq`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean#L132).

> A state is pure exactly when every genuine binary mixture producing it is trivial.

```lean
lemma isPure_iff_forall_mix_eq {ω : 𝓢[ℝ, E]} :
    ω.IsPure ↔ ∀ φ ψ t, 0 < t → t < 1 → mix φ ψ t = ω → φ = ω ∧ ψ = ω
```

## Depends on

- [Positive unital maps](../channel/basic.md)
- [Ordered vector spaces and order units](../orderunit/basic.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Convex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Convex.lean)
