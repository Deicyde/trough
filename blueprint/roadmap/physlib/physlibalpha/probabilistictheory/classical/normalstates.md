---
declaration: module
origin: cited
lean: BoundedMeasurable.eval, BoundedMeasurable.eval_apply, BoundedMeasurable.isNormal_eval, BoundedMeasurable.isPure_eval, BoundedMeasurable.abs_apply_le, BoundedMeasurable.ofMeasure, BoundedMeasurable.ofMeasure_apply, BoundedMeasurable.isNormal_ofMeasure
statement: formalized
proof: formalized
---

# States of a classical system

The module `PhyslibAlpha.ProbabilisticTheory.Classical.NormalStates`, [PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean): 16 declarations, 9 with a docstring.

> The normal states of a classical system are exactly the probability measures on its outcomes.

## i. Overview

> Each outcome `x` gives the deterministic state `f ↦ f x`, which predicts every observable with
> certainty; deterministic states are normal and pure.
>
> In a normal state, the effect-valued measure of the outcome has a probability measure on `Ω` as
> outcome distribution. Conversely, integrating against a probability measure is a normal state.
> These are inverse to each other: the normal states of a classical system are exactly the
> probability measures on its outcomes.

## ii. Key results

> - `BoundedMeasurable.eval` : the deterministic state at an outcome.
> - `BoundedMeasurable.isPure_eval` : deterministic states are pure.
> - `BoundedMeasurable.ofMeasure` : the state given by integrating against a probability measure.
> - `BoundedMeasurable.toMeasure` : the outcome distribution of a normal state.
> - `BoundedMeasurable.normalStateEquiv` : the normal states are the probability measures.

## iv. References

> * None.

## A. Deterministic states

**`BoundedMeasurable.eval`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L64).

> The deterministic state at the outcome `x`.

```lean
def eval (x : Ω) : 𝓢[ℝ, BoundedMeasurable Ω]
```

**`BoundedMeasurable.eval_apply`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L67).

```lean
lemma eval_apply (x : Ω) (f : BoundedMeasurable Ω) : eval x f = f x
```

**`BoundedMeasurable.isNormal_eval`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L69).

```lean
lemma isNormal_eval (x : Ω) : (eval x).IsNormal
```

## B. Purity

**`BoundedMeasurable.isPure_eval`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L80).

> Deterministic states are pure: the value of the smaller of two observables at `x` is the
> smaller value.

```lean
lemma isPure_eval (x : Ω) : (eval x).IsPure
```

## C. From measures to states

**`BoundedMeasurable.abs_apply_le`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L99).

> A state is bounded by any pointwise bound of an observable.

```lean
lemma abs_apply_le (ω : 𝓢[ℝ, BoundedMeasurable Ω]) {g : BoundedMeasurable Ω} {ε : ℝ}
    (hg : ∀ x, |g x| ≤ ε) : |ω g| ≤ ε
```

**`BoundedMeasurable.ofMeasure`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L109).

> Integration against a probability measure, as a state.

```lean
noncomputable def ofMeasure (μ : ProbabilityMeasure Ω) : 𝓢[ℝ, BoundedMeasurable Ω]
```

**`BoundedMeasurable.ofMeasure_apply`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L115).

```lean
lemma ofMeasure_apply (μ : ProbabilityMeasure Ω) (f : BoundedMeasurable Ω) :
    ofMeasure μ f = ∫ x, f x ∂(μ : Measure Ω)
```

**`BoundedMeasurable.isNormal_ofMeasure`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L119).

> Integration against a probability measure is normal, by dominated convergence.

```lean
lemma isNormal_ofMeasure (μ : ProbabilityMeasure Ω) : (ofMeasure μ).IsNormal
```

## D. From states to measures

**`BoundedMeasurable.toMeasure`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L141).

> The outcome distribution of a normal state.

```lean
noncomputable def toMeasure (ω : 𝓢[ℝ, BoundedMeasurable Ω]) (hω : ω.IsNormal) :
    ProbabilityMeasure Ω
```

**`BoundedMeasurable.toMeasure_apply`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L145).

```lean
lemma toMeasure_apply (ω : 𝓢[ℝ, BoundedMeasurable Ω]) (hω : ω.IsNormal) {s : Set Ω}
    (hs : MeasurableSet s) :
    (toMeasure ω hω : Measure Ω) s = ENNReal.ofReal (ω (indicator s hs))
```

**`BoundedMeasurable.measureReal_toMeasure`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L150).

```lean
lemma measureReal_toMeasure (ω : 𝓢[ℝ, BoundedMeasurable Ω]) (hω : ω.IsNormal) {s : Set Ω}
    (hs : MeasurableSet s) :
    (toMeasure ω hω : Measure Ω).real s = ω (indicator s hs)
```

**`BoundedMeasurable.toMeasure_ofMeasure`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L156).

```lean
lemma toMeasure_ofMeasure (μ : ProbabilityMeasure Ω) :
    toMeasure (ofMeasure μ) (isNormal_ofMeasure μ) = μ
```

## E. The correspondence

**`BoundedMeasurable.ofMeasure_toMeasure_staircase`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L170).

> Integration against the outcome distribution agrees with the normal state on indicators, hence
> on staircases.

```lean
lemma ofMeasure_toMeasure_staircase (ω : 𝓢[ℝ, BoundedMeasurable Ω]) (hω : ω.IsNormal)
    (g : BoundedMeasurable Ω) (N K : ℕ) :
    ofMeasure (toMeasure ω hω) (staircase g N K) = ω (staircase g N K)
```

**`BoundedMeasurable.ofMeasure_toMeasure_apply_of_nonneg`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L180).

```lean
lemma ofMeasure_toMeasure_apply_of_nonneg (ω : 𝓢[ℝ, BoundedMeasurable Ω]) (hω : ω.IsNormal)
    {g : BoundedMeasurable Ω} (h0 : 0 ≤ g) {K : ℕ} (hK : ∀ x, g x ≤ K) :
    ofMeasure (toMeasure ω hω) g = ω g
```

**`BoundedMeasurable.ofMeasure_toMeasure`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L196).

> A normal state is integration against its outcome distribution.

```lean
lemma ofMeasure_toMeasure (ω : 𝓢[ℝ, BoundedMeasurable Ω]) (hω : ω.IsNormal) :
    ofMeasure (toMeasure ω hω) = ω
```

**`BoundedMeasurable.normalStateEquiv`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean#L213).

> **The normal states of a classical system are the probability measures on its outcomes.**

```lean
noncomputable def normalStateEquiv :
    {ω : 𝓢[ℝ, BoundedMeasurable Ω] // ω.IsNormal} ≃ ProbabilityMeasure Ω
```

## Depends on

- [Observables of a sample space](boundedmeasurable.md)
- [The Born rule for effect-valued measures](../measurement/bornrule.md)
- [Convex state spaces (PhyslibAlpha)](../state/convex.md)

## Proof depends on

- [Lattice-ordered observables (LatticeObservables)](latticeobservables.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NormalStates.lean)
