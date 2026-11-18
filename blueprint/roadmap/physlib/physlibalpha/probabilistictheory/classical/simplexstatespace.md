---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.HasPureDecomposition, ProbabilisticTheory.UnitalPositiveLinearMap.HasUniquePureDecomposition, ProbabilisticTheory.IsSimplexStateSpace, ProbabilisticTheory.IsBauerSimplexStateSpace, ProbabilisticTheory.PureState.integrable, ProbabilisticTheory.PureState.toPositive, ProbabilisticTheory.PureState.toPositive_apply, ProbabilisticTheory.PureState.toPositive_add
statement: formalized
proof: formalized
---

# Classical systems: unique decomposition into pure states

The module `PhyslibAlpha.ProbabilisticTheory.Classical.SimplexStateSpace`, [PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean): 16 declarations, 9 with a docstring.

> Pure decompositions, simplex and Bauer simplex state spaces, and measures as functionals.

## i. Overview

> A system is classical when every state is a mixture of pure states in exactly one way. A die is the
> basic example. Its pure states are the six outcomes. Every state is a probability vector, and the
> state fixes the probabilities.
>
> Geometrically, the states of a die form a simplex: the convex hull of six affinely independent
> points. The weights of a state are its barycentric coordinates. In infinite dimensions there can be
> infinitely many pure states, and the weights become a probability measure on the pure states. We
> call this measure a pure decomposition. The state space is a simplex when every state has exactly
> one pure decomposition. It is a Bauer simplex when moreover the pure states form a closed set.
>
> A qubit is not classical. The maximally mixed state is an equal mixture of spin up and spin down,
> but also of spin left and spin right.
>
> On a simplex, measures on the pure states are the same as positive functionals on the observables,
> and this identification respects the order.

## ii. Key results

> - `UnitalPositiveLinearMap.HasPureDecomposition` states that a state is a mixture of pure states.
> - `UnitalPositiveLinearMap.HasUniquePureDecomposition` states that it is so in exactly one way.
> - `IsSimplexStateSpace E` states that every state has exactly one pure decomposition.
> - `IsBauerSimplexStateSpace E` states in addition that the pure states form a closed set.
> - `PureState.toPositive` turns a measure on the pure states into a positive functional.

## iv. References

> * None.

## A. Pure decompositions and simplices

**`ProbabilisticTheory.UnitalPositiveLinearMap.HasPureDecomposition`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L81).

> The state `ω` decomposes into pure states: some regular probability measure on the pure states
> represents it.

```lean
def HasPureDecomposition (ω : 𝓢[ℝ, E]) : Prop
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.HasUniquePureDecomposition`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L87).

> The state `ω` decomposes uniquely into pure states: exactly one regular probability measure on
> the pure states represents it.

```lean
def HasUniquePureDecomposition (ω : 𝓢[ℝ, E]) : Prop
```

**`ProbabilisticTheory.IsSimplexStateSpace`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L96).

> The state space of `E` is a simplex: every state is a unique mixture of pure states, given by
> a regular probability measure on the pure states. In finite dimension this is the convex hull of
> affinely independent pure states, every state having unique barycentric coordinates.

```lean
def IsSimplexStateSpace : Prop
```

**`ProbabilisticTheory.IsBauerSimplexStateSpace`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L102).

> The state space of `E` is a Bauer simplex: a simplex whose pure states form a closed, hence
> compact, set.

```lean
def IsBauerSimplexStateSpace : Prop
```

## B. Measures on the pure states as positive functionals

**`ProbabilisticTheory.PureState.integrable`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L117).

```lean
lemma integrable (μ : Measure (PureState E)) [IsFiniteMeasure μ] (f : E) :
    Integrable (fun ω : PureState E => toState ω.1 f) μ
```

**`ProbabilisticTheory.PureState.toPositive`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L123).

> Integration of the observables against a finite measure on the pure states.

```lean
noncomputable def toPositive (μ : Measure (PureState E)) [IsFiniteMeasure μ] : E →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.PureState.toPositive_apply`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L131).

```lean
lemma toPositive_apply (μ : Measure (PureState E)) [IsFiniteMeasure μ] (f : E) :
    toPositive μ f = ∫ ω, toState ω.1 f ∂μ
```

**`ProbabilisticTheory.PureState.toPositive_add`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L134).

```lean
lemma toPositive_add (μ ν : Measure (PureState E)) [IsFiniteMeasure μ] [IsFiniteMeasure ν] :
    toPositive (μ + ν) = toPositive μ + toPositive ν
```

**`ProbabilisticTheory.PureState.toPositive_mono`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L138).

```lean
lemma toPositive_mono {μ ν : Measure (PureState E)} [IsFiniteMeasure μ] [IsFiniteMeasure ν]
    (h : μ ≤ ν) : toPositive μ ≤ toPositive ν
```

**`ProbabilisticTheory.PureState.toPositive_one`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L142).

```lean
lemma toPositive_one (μ : Measure (PureState E)) [IsFiniteMeasure μ] :
    toPositive μ 1 = μ.real Set.univ
```

**`ProbabilisticTheory.PureState.measure_univ_eq_of_toPositive_eq`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L146).

```lean
lemma measure_univ_eq_of_toPositive_eq {μ ν : Measure (PureState E)} [IsFiniteMeasure μ]
    [IsFiniteMeasure ν] (hμν : toPositive μ = toPositive ν) : μ Set.univ = ν Set.univ
```

**`ProbabilisticTheory.PureState.toPositive_smul_eq`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L152).

```lean
lemma toPositive_smul_eq {μ ν : Measure (PureState E)} [IsFiniteMeasure μ] [IsFiniteMeasure ν]
    {c : ℝ≥0∞} [IsFiniteMeasure (c • μ)] [IsFiniteMeasure (c • ν)]
    (hμν : toPositive μ = toPositive ν) : toPositive (c • μ) = toPositive (c • ν)
```

## C. Simplices identify functionals with measures

**`ProbabilisticTheory.exists_toPositive_eq`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L175).

> Every positive functional is integration against a finite regular measure on the pure
> states.

```lean
lemma exists_toPositive_eq (α : E →ₚ[ℝ] ℝ) :
    ∃ (μ : Measure (PureState E)) (_ : IsFiniteMeasure μ), μ.Regular ∧ toPositive μ = α
```

**`ProbabilisticTheory.eq_of_toPositive_eq_of_isProbabilityMeasure`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L189).

> Regular probability measures on the pure states with the same integrals are equal.

```lean
lemma eq_of_toPositive_eq_of_isProbabilityMeasure {μ ν : Measure (PureState E)} [μ.Regular]
    [ν.Regular] [IsProbabilityMeasure μ] [IsProbabilityMeasure ν]
    (hμν : toPositive μ = toPositive ν) : μ = ν
```

**`ProbabilisticTheory.eq_of_toPositive_eq`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L202).

> Finite regular measures on the pure states with the same integrals are equal.

```lean
lemma eq_of_toPositive_eq {μ ν : Measure (PureState E)} [μ.Regular] [ν.Regular]
    [IsFiniteMeasure μ] [IsFiniteMeasure ν] (hμν : toPositive μ = toPositive ν) : μ = ν
```

**`ProbabilisticTheory.le_of_toPositive_le`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean#L219).

> Unique decomposition makes the order on positive functionals that of measures.

```lean
lemma le_of_toPositive_le {μ θ : Measure (PureState E)} [μ.Regular] [θ.Regular]
    [IsFiniteMeasure μ] [IsFiniteMeasure θ] (hle : toPositive μ ≤ toPositive θ) : μ ≤ θ
```

## Depends on

- [Representations by measures on a boundary](../../mathematics/part-01/convex/choquet-boundaryrepresentation.md)
- [Pure states](purestate.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/SimplexStateSpace.lean)
