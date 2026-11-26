---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.mix, ProbabilisticTheory.State.mix_apply, ProbabilisticTheory.State.toLinearMap_mix, ProbabilisticTheory.State.mix_symm, ProbabilisticTheory.State.stateSpace, ProbabilisticTheory.State.stateSpace_convex, ProbabilisticTheory.State.IsPure, ProbabilisticTheory.State.IsMixed
statement: formalized
proof: formalized
---

# Convex state spaces (Physlib)

The module `Physlib.ProbabilisticTheory.State.Convex`, [Physlib/ProbabilisticTheory/State/Convex.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean): 13 declarations, 13 with a docstring.

> Convexity of the state space and its pure and mixed states.

## i. Overview

> States mix: a probabilistic combination of two states is again a state, and the state space
> embeds convexly into the algebraic dual. A pure state is one that's never a genuine mixture of
> two others, an extreme point of that convex set. A mixed state is one that is a mixture.

## ii. Key results

> - `ProbabilisticTheory.State.mix` : randomize between two states with a given probability.
> - `ProbabilisticTheory.State.stateSpace_convex` : the state space is convex in the algebraic dual.
> - `ProbabilisticTheory.State.IsPure` : pure states are extreme points of the state space.
> - `ProbabilisticTheory.State.isPure_iff_forall_mix_eq` : a pure state admits only trivial
>   genuine mixtures.
> - `ProbabilisticTheory.State.isMixed_iff_exists_mem_openSegment` : mixed states lie between
>   two other states.

## iv. References

## A. Mixing states

**`ProbabilisticTheory.State.mix`**, an abbrev, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L58).

> Randomize between two states with probability `t` of choosing the first, so
> `t • ω + σ t • φ` with `σ t = 1 - t`.

```lean
abbrev mix (ω φ : P.State) (t : unitInterval) : P.State
```

**`ProbabilisticTheory.State.mix_apply`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L62).

> Evaluation of a mixture is the pointwise convex combination.

```lean
lemma mix_apply (ω φ : P.State) (t : unitInterval) (A : P.Observables) :
    mix ω φ t A = (t : ℝ) * ω A + (1 - (t : ℝ)) * φ A
```

**`ProbabilisticTheory.State.toLinearMap_mix`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L66).

> The underlying linear map of a mixture is the corresponding combination of linear maps.

```lean
lemma toLinearMap_mix (ω φ : P.State) (t : unitInterval) :
    (mix ω φ t).toLinearMap = (t : ℝ) • ω.toLinearMap + (1 - (t : ℝ)) • φ.toLinearMap
```

**`ProbabilisticTheory.State.mix_symm`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L71).

> Swapping the two states swaps the weights: `σ` is the symmetry of the interval.

```lean
lemma mix_symm (ω φ : P.State) (t : unitInterval) : mix ω φ t = mix φ ω (σ t)
```

## B. The state space

**`ProbabilisticTheory.State.stateSpace`**, an abbrev, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L81).

> States embedded into the algebraic dual.

```lean
abbrev stateSpace : Set (P.Observables →ₗ[ℝ] ℝ)
```

**`ProbabilisticTheory.State.stateSpace_convex`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L85).

> The state space is convex in the algebraic dual.

```lean
lemma stateSpace_convex : Convex ℝ (stateSpace (P := P))
```

## C. Pure and mixed states

**`ProbabilisticTheory.State.IsPure`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L95).

> A state is pure when it is an extreme point of the state space.

```lean
def IsPure (ω : P.State) : Prop
```

**`ProbabilisticTheory.State.IsMixed`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L98).

> A state is mixed when it isn't pure.

```lean
def IsMixed (ω : P.State) : Prop
```

**`ProbabilisticTheory.State.isPure_iff_forall_mem_openSegment`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L101).

> A state is pure exactly when any open segment containing it has both endpoints equal to it.

```lean
lemma isPure_iff_forall_mem_openSegment {ω : P.State} :
    ω.IsPure ↔ ∀ φ ψ : P.State,
      ω.toLinearMap ∈ openSegment ℝ φ.toLinearMap ψ.toLinearMap → φ = ω ∧ ψ = ω
```

**`ProbabilisticTheory.State.isMixed_iff_exists_mem_openSegment`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L109).

> A state is mixed exactly when it lies in an open segment with a different endpoint.

```lean
lemma isMixed_iff_exists_mem_openSegment {ω : P.State} :
    ω.IsMixed ↔ ∃ φ ψ : P.State,
      ω.toLinearMap ∈ openSegment ℝ φ.toLinearMap ψ.toLinearMap ∧ (φ ≠ ω ∨ ψ ≠ ω)
```

**`ProbabilisticTheory.State.mem_openSegment_iff_exists_mix`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L115).

> Open segments between states consist exactly of their genuine mixtures.

```lean
lemma mem_openSegment_iff_exists_mix (ω φ ψ : P.State) :
    ω.toLinearMap ∈ openSegment ℝ φ.toLinearMap ψ.toLinearMap ↔
      ∃ t : unitInterval, 0 < t ∧ t < 1 ∧ mix φ ψ t = ω
```

**`ProbabilisticTheory.State.isPure_iff_forall_mix_eq`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L121).

> A state is pure exactly when every genuine binary mixture producing it is trivial.

```lean
lemma isPure_iff_forall_mix_eq {ω : P.State} :
    ω.IsPure ↔ ∀ φ ψ t, 0 < t → t < 1 → mix φ ψ t = ω → φ = ω ∧ ψ = ω
```

**`ProbabilisticTheory.State.apply_eq_zero_of_mix_eq`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean#L128).

> A positive observable with vanishing expectation in a genuine mixture vanishes in both
> components.

```lean
lemma apply_eq_zero_of_mix_eq {ω φ ψ : P.State} {t : unitInterval} (ht0 : 0 < t) (ht1 : t < 1)
    (h : mix φ ψ t = ω) {A : P.Observables} (hA : 0 ≤ A) (hωA : ω A = 0) :
    φ A = 0 ∧ ψ A = 0
```

## Depends on

- [Convex spaces of channels](../channel/convex.md)
- [States](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Convex.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Convex.lean)
