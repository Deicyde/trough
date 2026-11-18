---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.integrable_apply, ProbabilisticTheory.UnitalPositiveLinearMap.barycenter, ProbabilisticTheory.UnitalPositiveLinearMap.barycenter_apply
statement: formalized
proof: formalized
---

# Barycenters of random states

The module `PhyslibAlpha.ProbabilisticTheory.State.Barycenter`, [PhyslibAlpha/ProbabilisticTheory/State/Barycenter.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Barycenter.lean): 3 declarations, 2 with a docstring.

> The barycenter of a probability measure on states: the state a random preparation produces.

## i. Overview

> A probability measure `μ` on the states is a random state: pick a state `ω` according to `μ`, then
> measure. The expectation value of an observable `A` is then the average of `ω A`. These averages
> form a state again, the barycenter of `μ`. It is the state that the random procedure prepares.

## ii. Key results

> - `UnitalPositiveLinearMap.barycenter` is the barycenter of a probability measure on states.

## iv. References

> * None.

## A. Integrability of expectation values

**`ProbabilisticTheory.UnitalPositiveLinearMap.integrable_apply`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Barycenter.lean#L56).

> An expectation value is integrable against every probability measure on states.

```lean
lemma integrable_apply (μ : ProbabilityMeasure (stateSpace E)) (A : E) :
    Integrable (fun ω : stateSpace E => toState ω A) (μ : Measure (stateSpace E))
```

## B. Barycenters

**`ProbabilisticTheory.UnitalPositiveLinearMap.barycenter`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Barycenter.lean#L69).

> The barycenter of `μ`: the state predicting, for every observable, the `μ`-average of the
> predictions.

```lean
noncomputable def barycenter (μ : ProbabilityMeasure (stateSpace E)) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.barycenter_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Barycenter.lean#L82).

```lean
lemma barycenter_apply (μ : ProbabilityMeasure (stateSpace E)) (A : E) :
    barycenter μ A = ∫ ω : stateSpace E, toState ω A ∂(μ : Measure (stateSpace E))
```

## Depends on

- [The state space](statespace.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/Barycenter.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Barycenter.lean)
