---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual, ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual_apply, ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual_injective, ProbabilisticTheory.UnitalPositiveLinearMap.norm_toStrongDual_le, ProbabilisticTheory.UnitalPositiveLinearMap.norm_toStrongDual, ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual_mix, ProbabilisticTheory.stateSpace, ProbabilisticTheory.StateSpace.toState
statement: formalized
proof: formalized
---

# The state space

The module `PhyslibAlpha.ProbabilisticTheory.State.StateSpace`, [PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean): 26 declarations (4 instances with no name), 13 with a docstring.

> The weak-star state space: compact, convex, with the pure states as its extreme points.

## i. Overview

> A state is a normalized positive functional: it gives the certain outcome `1` the value `1` and
> every positive observable a nonnegative value. So the states form a subset `stateSpace E` of the
> dual of `E`. This file studies it with the weak-star topology, the topology of `WeakDual ℝ E`.
>
> Two states are close in the weak-star topology when they predict nearly the same expectation value
> for every observable, one observable at a time. In this topology the state space is compact, by
> the Banach–Alaoglu theorem, and metrizable when `E` is separable.
>
> On `𝓢[ℝ, E]` itself the states carry the finer state metric.

## ii. Key results

> - `stateSpace E` is the set of states in the weak dual of `E`.
> - `StateSpace.toState` and `StateSpace.ofState` pass between points of `stateSpace E` and states.
> - `StateSpace.tendsto_iff_forall_apply_tendsto` proves that weak-star convergence is convergence of
>   every expectation value.
> - `isCompact_stateSpace` proves that the state space is weak-star compact.
> - `convex_stateSpace` proves that the state space is convex.
> - `StateSpace.isPure_iff_mem_extremePoints` proves that the pure states are its extreme points.

## iv. References

> * None.

## A. States as continuous functionals

**`ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L70).

> A state as a continuous linear functional for the order-unit norm.

```lean
noncomputable def toStrongDual (ω : 𝓢[ℝ, E]) : StrongDual ℝ E
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual_apply`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L76).

```lean
lemma toStrongDual_apply (ω : 𝓢[ℝ, E]) (A : E) : ω.toStrongDual A = ω A
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual_injective`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L78).

```lean
lemma toStrongDual_injective : Function.Injective (toStrongDual : 𝓢[ℝ, E] → StrongDual ℝ E)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.norm_toStrongDual_le`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L81).

```lean
lemma norm_toStrongDual_le (ω : 𝓢[ℝ, E]) : ‖ω.toStrongDual‖ ≤ 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.norm_toStrongDual`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L86).

> Every state has norm `1`.

```lean
lemma norm_toStrongDual [Nontrivial E] (ω : 𝓢[ℝ, E]) : ‖ω.toStrongDual‖ = 1
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.toStrongDual_mix`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L92).

```lean
lemma toStrongDual_mix (ω φ : 𝓢[ℝ, E]) (t : unitInterval) :
    (mix ω φ t).toStrongDual = (t : ℝ) • ω.toStrongDual + (1 - (t : ℝ)) • φ.toStrongDual
```

## B. The state space in the weak dual

**`ProbabilisticTheory.stateSpace`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L108).

> The state space: the functionals in the weak dual sending `1` to `1` and positive observables
> to nonnegative numbers.

```lean
def stateSpace : Set (WeakDual ℝ E)
```

**`ProbabilisticTheory.StateSpace.toState`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L113).

> The state given by a point of the state space.

```lean
noncomputable def toState (ω : stateSpace E) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.StateSpace.ofState`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L117).

> A state, as a point of the state space.

```lean
noncomputable def ofState (ω : 𝓢[ℝ, E]) : stateSpace E
```

**`ProbabilisticTheory.StateSpace.coe_apply`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L120).

```lean
lemma coe_apply (ω : stateSpace E) (A : E) : (ω : WeakDual ℝ E) A = toState ω A
```

**`ProbabilisticTheory.StateSpace.toState_ofState`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L122).

```lean
lemma toState_ofState (ω : 𝓢[ℝ, E]) : toState (ofState ω) = ω
```

**`ProbabilisticTheory.StateSpace.ofState_toState`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L124).

```lean
lemma ofState_toState (ω : stateSpace E) : ofState (toState ω) = ω
```

**`ProbabilisticTheory.StateSpace.equivState`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L127).

> Points of the state space are states.

```lean
noncomputable def equivState : stateSpace E ≃ 𝓢[ℝ, E]
```

**`ProbabilisticTheory.StateSpace.toState_injective`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L130).

```lean
lemma toState_injective : Function.Injective (toState (E := E))
```

**An instance with no name**, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L133).

> The Borel sets of the weak-star topology.

```lean
noncomputable instance : MeasurableSpace (stateSpace E)
```

**An instance with no name**, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L135).

```lean
instance : BorelSpace (stateSpace E)
```

## C. Pointwise convergence

**`ProbabilisticTheory.StateSpace.continuous_apply`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L145).

> Each expectation value depends continuously on the state.

```lean
lemma continuous_apply (A : E) : Continuous fun ω : stateSpace E => toState ω A
```

**`ProbabilisticTheory.StateSpace.tendsto_iff_forall_apply_tendsto`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L149).

> States converge weak-star exactly when every expectation value converges.

```lean
lemma tendsto_iff_forall_apply_tendsto {ι : Type*} {f : ι → stateSpace E} {l : Filter ι}
    {ω : stateSpace E} :
    Tendsto f l (𝓝 ω) ↔ ∀ A : E, Tendsto (fun i => toState (f i) A) l (𝓝 (toState ω A))
```

## D. Compactness

**`ProbabilisticTheory.isClosed_stateSpace`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L164).

```lean
lemma isClosed_stateSpace : IsClosed (stateSpace E)
```

**`ProbabilisticTheory.stateSpace_subset_closedBall`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L172).

```lean
lemma stateSpace_subset_closedBall :
    stateSpace E ⊆ WeakDual.toStrongDual ⁻¹' Metric.closedBall 0 1
```

**`ProbabilisticTheory.isCompact_stateSpace`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L177).

> **Banach–Alaoglu** for states: the state space is weak-star compact.

```lean
lemma isCompact_stateSpace : IsCompact (stateSpace E)
```

**An instance with no name**, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L181).

```lean
instance : CompactSpace (stateSpace E)
```

**An instance with no name**, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L184).

> For separable `E`, the state space is metrizable.

```lean
instance [TopologicalSpace.SeparableSpace E] : TopologicalSpace.MetrizableSpace (stateSpace E)
```

## E. Convexity and pure states

**`ProbabilisticTheory.convex_stateSpace`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L194).

> A mixture of states is a state.

```lean
lemma convex_stateSpace : Convex ℝ (stateSpace E)
```

**`ProbabilisticTheory.StateSpace.range_ofState`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L201).

```lean
lemma range_ofState : Set.range (fun ω : 𝓢[ℝ, E] => (ofState ω : WeakDual ℝ E)) = stateSpace E
```

**`ProbabilisticTheory.StateSpace.isPure_iff_mem_extremePoints`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean#L205).

> A state is pure exactly when it is an extreme point of the state space.

```lean
lemma isPure_iff_mem_extremePoints (ω : stateSpace E) :
    (toState ω).IsPure ↔ (ω : WeakDual ℝ E) ∈ (stateSpace E).extremePoints ℝ
```

## Depends on

- [Archimedean order-unit spaces](../../../physlib/probabilistictheory/orderunit/archimedean.md)
- [Convex state spaces](convex.md)

## Proof depends on

- [Separation by states](separation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/StateSpace.lean)
