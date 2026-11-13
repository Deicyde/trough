---
declaration: module
origin: cited
lean: ProbabilisticTheory.PureState.finite_setOf_isPure, ProbabilisticTheory.PureState.affineIndependent_of_isSimplex, ProbabilisticTheory.PureState.affineCombination_measureReal, ProbabilisticTheory.PureState.eq_of_isSimplex, ProbabilisticTheory.PureState.isSimplexStateSpace_of_isSimplex, ProbabilisticTheory.sum_weighted_eq_of_sum_smul_eq, ProbabilisticTheory.EnsemblesRefine.affineIndependent_extremePoints, ProbabilisticTheory.IsSimplexStateSpace.isSimplex
statement: formalized
proof: formalized
---

# Finite classical systems

The module `PhyslibAlpha.ProbabilisticTheory.Classical.FiniteDimensional`, [PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean): 10 declarations, 10 with a docstring.

> A finite-dimensional system is classical exactly when its state space is a geometric simplex.

## i. Overview

> A system with finitely many independent observables is classical exactly when its state space is a
> geometric simplex. A geometric simplex is the convex hull of finitely many affinely independent
> points, its corners. The corners are the pure states. Every state is a mixture of them with unique
> weights, its barycentric coordinates.
>
> One direction is direct. Finitely many pure states form a closed set, so every state has a pure
> decomposition, and affine independence fixes the weights. For the other direction, refinement of
> ensembles makes the pure states affinely independent. In finite dimension there are then only
> finitely many of them, and by the Krein–Milman theorem they span the state space.

## ii. Key results

> - `PureState.isSimplexStateSpace_of_isSimplex` proves that a geometric simplex of states is
>   classical.
> - `EnsemblesRefine.affineIndependent_extremePoints` proves that, when ensembles refine, the pure
>   states are affinely independent.
> - `isSimplexStateSpace_iff_isSimplex` proves that a finite system is classical exactly when its
>   state space is a geometric simplex.

## iv. References

> * None.

## A. Geometric simplices decompose uniquely

**`ProbabilisticTheory.PureState.finite_setOf_isPure`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L71).

> If the state space is a geometric simplex, there are finitely many pure states.

```lean
lemma finite_setOf_isPure : {φ : stateSpace E | (toState φ).IsPure}.Finite
```

**`ProbabilisticTheory.PureState.affineIndependent_of_isSimplex`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L76).

> If the state space is a geometric simplex, its pure states are affinely independent.

```lean
lemma affineIndependent_of_isSimplex :
    AffineIndependent ℝ fun k : PureState E => (k.1 : WeakDual ℝ E)
```

**`ProbabilisticTheory.PureState.affineCombination_measureReal`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L86).

> A probability measure on finitely many pure states writes its barycenter as the mixture of the
> pure states weighted by their masses.

```lean
lemma affineCombination_measureReal [Fintype (PureState E)] {μ : Measure (PureState E)}
    [IsProbabilityMeasure μ] {ω : 𝓢[ℝ, E]} (hμ : ∀ f, ∫ k, toState k.1 f ∂μ = ω f) :
    Finset.univ.affineCombination ℝ (fun k : PureState E => (k.1 : WeakDual ℝ E))
        (fun k => μ.real {k}) =
      ((StateSpace.ofState ω) : WeakDual ℝ E)
```

**`ProbabilisticTheory.PureState.eq_of_isSimplex`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L99).

> On a geometric simplex, a state has at most one decomposition into pure states.

```lean
lemma eq_of_isSimplex [Fintype (PureState E)] {μ ν : Measure (PureState E)}
    [IsProbabilityMeasure μ] [IsProbabilityMeasure ν] {ω : 𝓢[ℝ, E]}
    (hμ : ∀ f, ∫ k, toState k.1 f ∂μ = ω f) (hν : ∀ f, ∫ k, toState k.1 f ∂ν = ω f) : μ = ν
```

**`ProbabilisticTheory.PureState.isSimplexStateSpace_of_isSimplex`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L112).

> **A geometric simplex of states is a simplex**: every state decomposes uniquely into pure
> states.

```lean
lemma isSimplexStateSpace_of_isSimplex : IsSimplexStateSpace E
```

## B. Simplices are geometric simplices

**`ProbabilisticTheory.sum_weighted_eq_of_sum_smul_eq`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L129).

> Equal mixtures of states in the weak dual are equal mixtures of weighted states.

```lean
lemma sum_weighted_eq_of_sum_smul_eq {ι : Type*} {s : Finset ι} {φ : ι → stateSpace E}
    {w₁ w₂ : ι → ℝ} (h₁ : ∀ i ∈ s, 0 ≤ w₁ i) (h₂ : ∀ i ∈ s, 0 ≤ w₂ i)
    (hw : ∑ i ∈ s, w₁ i • ((φ i) : WeakDual ℝ E) = ∑ i ∈ s, w₂ i • ((φ i) : WeakDual ℝ E)) :
    ∑ i : s, (toState (φ i)).weighted ⟨w₁ i, h₁ i i.2⟩ =
      ∑ i : s, (toState (φ i)).weighted ⟨w₂ i, h₂ i i.2⟩
```

**`ProbabilisticTheory.EnsemblesRefine.affineIndependent_extremePoints`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L146).

> When ensembles refine, the pure states are affinely independent.

```lean
lemma EnsemblesRefine.affineIndependent_extremePoints (hE : EnsemblesRefine E) :
    AffineIndependent ℝ
      (Subtype.val : (stateSpace E).extremePoints ℝ → WeakDual ℝ E)
```

**`ProbabilisticTheory.IsSimplexStateSpace.isSimplex`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L160).

> On a simplex with finitely many independent observables, the state space is a geometric
> simplex.

```lean
lemma IsSimplexStateSpace.isSimplex [FiniteDimensional ℝ E] (h : IsSimplexStateSpace E) :
    IsSimplex (stateSpace E)
```

**`ProbabilisticTheory.isSimplexStateSpace_iff_isSimplex`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L176).

> **Finite simplices**: for finitely many independent observables, the state space is a simplex
> exactly when it is the convex hull of finitely many affinely independent pure states.

```lean
lemma isSimplexStateSpace_iff_isSimplex [FiniteDimensional ℝ E] :
    IsSimplexStateSpace E ↔ IsSimplex (stateSpace E)
```

**`ProbabilisticTheory.isSimplexStateSpace_of_affineEquiv_stdSimplexSet`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean#L181).

> A state space affinely equivalent to a standard simplex is a simplex.

```lean
lemma isSimplexStateSpace_of_affineEquiv_stdSimplexSet {ι : Type*} [Fintype ι]
    (e : WeakDual ℝ E ≃ᵃ[ℝ] (ι → ℝ)) (he : e '' stateSpace E = stdSimplexSet ι) :
    IsSimplexStateSpace E
```

## Depends on

- [Simplices](../../mathematics/part-02/geometry/simplex.md)
- [Refinement of ensembles](ensemblerefinement.md)

## Proof depends on

- [Bauer simplices](bauersimplex.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteDimensional.lean)
