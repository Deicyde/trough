---
declaration: module
origin: cited
lean: ProbabilisticTheory.StateSpace.denseEval, ProbabilisticTheory.StateSpace.denseEval_injective, ProbabilisticTheory.UnitalPositiveLinearMap.exists_pure_representingMeasure, ProbabilisticTheory.PureState.measurableSet_setOf_isPure, ProbabilisticTheory.PureState.measurableEmbedding_val, ProbabilisticTheory.PureState.map_comap_val_eq, ProbabilisticTheory.PureState.isProbabilityMeasure_comap_val, ProbabilisticTheory.PureState.hasPureDecomposition_of_separable
statement: formalized
proof: formalized
---

# Classical systems with separable observables

The module `PhyslibAlpha.ProbabilisticTheory.Classical.SeparableObservables`, [PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean): 9 declarations, 6 with a docstring.

> Choquet–Meyer: with separable observables, classical exactly when ensembles refine.

## i. Overview

> Most systems in physics can be described by countably many observables: the observables are
> separable. For such systems every state is a mixture of pure states. This is Choquet's theorem.
>
> The idea is simple. The states form a compact convex set. Its corners are the pure states.
> A state that is not pure is the midpoint of two other states, so its weight can be pushed
> outwards to them. Pushing weight outwards as far as possible leaves a probability measure that
> lives on the pure states. Countably many observables are needed to make this limit exist.
>
> Combined with the uniqueness theorem, this gives a clean criterion. A system with separable
> observables is classical exactly when its ensembles refine.

## ii. Key results

> - `UnitalPositiveLinearMap.exists_pure_representingMeasure` proves that every state is the
>   barycenter of a probability measure living on the pure states.
> - `PureState.hasPureDecomposition_of_separable` proves that every state has a pure
>   decomposition.
> - `isSimplexStateSpace_iff_ensemblesRefine` proves that the system is classical exactly when
>   ensembles refine. This is the **Choquet–Meyer theorem**.

## iv. References

> - G. Choquet and P.-A. Meyer, *Existence et unicité des représentations intégrales dans les
>   convexes compacts quelconques*, Ann. Inst. Fourier 13 (1963), 139–154.

## A. A dense sequence of observables separates states

**`ProbabilisticTheory.StateSpace.denseEval`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L73).

> The expectation value of the `n`-th observable of a dense sequence, as a continuous linear
> functional on the weak dual.

```lean
noncomputable def denseEval (n : ℕ) : WeakDual ℝ E →L[ℝ] ℝ
```

**`ProbabilisticTheory.StateSpace.denseEval_injective`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L77).

> The expectation values of a dense sequence of observables separate states.

```lean
lemma denseEval_injective (x y : stateSpace E)
    (h : ∀ n, denseEval n (x : WeakDual ℝ E) = denseEval n (y : WeakDual ℝ E)) :
    x = y
```

## B. Every state is a mixture of pure states

**`ProbabilisticTheory.UnitalPositiveLinearMap.exists_pure_representingMeasure`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L95).

> **Choquet representation of states.** Every state is the barycenter of a probability measure
> living on the pure states.

```lean
lemma exists_pure_representingMeasure (ω : 𝓢[ℝ, E]) :
    ∃ μ : ProbabilityMeasure (stateSpace E),
      barycenter μ = ω ∧ ∀ᵐ φ : stateSpace E ∂(μ : Measure _), (toState φ).IsPure
```

## C. Pure decompositions

**`ProbabilisticTheory.PureState.measurableSet_setOf_isPure`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L113).

```lean
lemma measurableSet_setOf_isPure : MeasurableSet {ω : stateSpace E | (toState ω).IsPure}
```

**`ProbabilisticTheory.PureState.measurableEmbedding_val`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L117).

```lean
lemma measurableEmbedding_val : MeasurableEmbedding (Subtype.val : PureState E → stateSpace E)
```

**`ProbabilisticTheory.PureState.map_comap_val_eq`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L121).

> A probability measure on the state space living on the pure states, restricted to them.

```lean
lemma map_comap_val_eq {μ : Measure (stateSpace E)}
    (hμ : ∀ᵐ φ ∂μ, (toState φ).IsPure) :
    (μ.comap (Subtype.val : PureState E → stateSpace E)).map Subtype.val = μ
```

**`ProbabilisticTheory.PureState.isProbabilityMeasure_comap_val`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L127).

```lean
lemma isProbabilityMeasure_comap_val {μ : Measure (stateSpace E)} [IsProbabilityMeasure μ]
    (hμ : ∀ᵐ φ ∂μ, (toState φ).IsPure) :
    IsProbabilityMeasure (μ.comap (Subtype.val : PureState E → stateSpace E))
```

**`ProbabilisticTheory.PureState.hasPureDecomposition_of_separable`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L135).

> With separable observables, every state decomposes into pure states.

```lean
lemma hasPureDecomposition_of_separable (ω : 𝓢[ℝ, E]) : ω.HasPureDecomposition
```

## D. Classical systems are those whose ensembles refine

**`ProbabilisticTheory.isSimplexStateSpace_iff_ensemblesRefine`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean#L156).

> **Choquet–Meyer**: for separable observables, the state space is a simplex exactly when
> ensembles refine.

```lean
lemma isSimplexStateSpace_iff_ensemblesRefine : IsSimplexStateSpace E ↔ EnsemblesRefine E
```

## Depends on

- [Refinement of ensembles](ensemblerefinement.md)
- [Barycenters of random states](../state/barycenter.md)

## Proof depends on

- [Every point is a mixture of extreme points](../../mathematics/part-01/convex/choquet-extremepointdecomposition.md)
- [Uniqueness of pure decompositions](uniquedecomposition.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SeparableObservables.lean)
