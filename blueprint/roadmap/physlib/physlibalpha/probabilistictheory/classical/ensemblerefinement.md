---
declaration: module
origin: cited
lean: ProbabilisticTheory.EnsemblesRefine, ProbabilisticTheory.IsClassical.ensemblesRefine, ProbabilisticTheory.EnsemblesRefine.exists_table, ProbabilisticTheory.EnsemblesRefine.eq_of_sum_weighted_eq, ProbabilisticTheory.EnsemblesRefine.upperEnvelope_add_le, ProbabilisticTheory.IsSimplexStateSpace.isClassical, ProbabilisticTheory.IsSimplexStateSpace.ensemblesRefine
statement: formalized
proof: formalized
---

# Refinement of ensembles

The module `PhyslibAlpha.ProbabilisticTheory.Classical.EnsembleRefinement`, [PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean): 7 declarations, 7 with a docstring.

> Refinement of ensembles, its consequences for pure states, and refinement on a simplex.

## i. Overview

> An ensemble is a recipe for preparing a state: choose one of finitely many states with given
> probabilities. We write it as a finite list of weighted states, a state times a nonnegative weight.
> Its total is their sum, the state it prepares. Two ensembles with the same total cannot be told
> apart by any measurement.
>
> Ensembles refine when any two ensembles with the same total have a common refinement. This is a
> table of weighted states. Its rows add up to the members of the first ensemble, and its columns add
> up to the members of the second. For a die it is a joint probability distribution with the two
> ensembles as marginals.
>
> Refinement is the physical content of being classical. On a simplex it follows from uniqueness:
> decompose every member into pure states and cut. Conversely, refinement is all the uniqueness
> lemma needs. A qubit shows the failure: the maximally mixed state is an equal mixture of spin up
> and down and of spin left and right, and these two ensembles have no common refinement.

## ii. Key results

> - `EnsemblesRefine E` states that ensembles refine.
> - `IsClassical.ensemblesRefine` proves that ensembles refine when positive functionals form a
>   lattice.
> - `EnsemblesRefine.eq_of_sum_weighted_eq` proves that, when ensembles refine, a mixture of different
>   pure states determines its weights.
> - `EnsemblesRefine.upperEnvelope_add_le` proves that, when ensembles refine, upper envelopes are
>   subadditive.
> - `IsSimplexStateSpace.ensemblesRefine` proves that ensembles refine on a simplex.

## iv. References

> * None.

## A. Ensembles of weighted states

**`ProbabilisticTheory.EnsemblesRefine`**, an abbrev, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean#L76).

> Ensembles of weighted states refine: any two finite families of weighted states with the same
> total have a common refinement, weighted states `γ i j` whose rows add up to the first family and
> whose columns add up to the second.

```lean
abbrev EnsemblesRefine (E : Type*) [OrderUnitSpace E] : Prop
```

**`ProbabilisticTheory.IsClassical.ensemblesRefine`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean#L82).

> On a lattice dual cone, ensembles of weighted states refine.

```lean
lemma IsClassical.ensemblesRefine (hE : IsClassical E) : EnsemblesRefine E
```

**`ProbabilisticTheory.EnsemblesRefine.exists_table`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean#L87).

> When ensembles refine, any two finite ensembles with the same total have a common refinement,
> indexed by arbitrary finite types.

```lean
lemma EnsemblesRefine.exists_table (hE : EnsemblesRefine E) {ι κ : Type*} [Fintype ι] [Fintype κ]
    (α : ι → E →ₚ[ℝ] ℝ) (β : κ → E →ₚ[ℝ] ℝ) (h : ∑ i, α i = ∑ j, β j) :
    ∃ γ : ι → κ → E →ₚ[ℝ] ℝ, (∀ i, ∑ j, γ i j = α i) ∧ ∀ j, ∑ i, γ i j = β j
```

## B. Refinement separates pure states

**`ProbabilisticTheory.EnsemblesRefine.eq_of_sum_weighted_eq`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean#L103).

> When ensembles refine, a mixture of distinct pure states determines its weights.

```lean
lemma EnsemblesRefine.eq_of_sum_weighted_eq (hE : EnsemblesRefine E) {ι : Type*} [Fintype ι]
    {e : ι → 𝓢[ℝ, E]} (he : ∀ i, (e i).IsPure) (hinj : Function.Injective e) {a b : ι → ℝ≥0}
    (h : ∑ i, (e i).weighted (a i) = ∑ i, (e i).weighted (b i)) : a = b
```

## C. Upper envelopes on refining ensembles

**`ProbabilisticTheory.EnsemblesRefine.upperEnvelope_add_le`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean#L126).

> **Choquet–Meyer**: when ensembles refine, the upper envelope is subadditive.

```lean
lemma EnsemblesRefine.upperEnvelope_add_le {ι : Type*} [Fintype ι] [Nonempty ι]
    (hE : EnsemblesRefine E) (s : ι → E)
    (α β : E →ₚ[ℝ] ℝ) : upperEnvelope s (α + β) ≤ upperEnvelope s α + upperEnvelope s β
```

## D. Ensembles refine on a simplex

**`ProbabilisticTheory.IsSimplexStateSpace.isClassical`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean#L147).

> On a simplex, any two positive functionals have a least upper bound: integration against the
> supremum of their measures.

```lean
lemma IsSimplexStateSpace.isClassical : IsClassical E
```

**`ProbabilisticTheory.IsSimplexStateSpace.ensemblesRefine`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean#L165).

> **On a simplex, ensembles refine.**

```lean
lemma IsSimplexStateSpace.ensemblesRefine : EnsemblesRefine E
```

## Depends on

- [Upper envelopes](../../mathematics/part-02/order/positivedual-upperenvelope.md)
- [Classical systems](basic.md)
- [Classical systems: unique decomposition into pure states](simplexstatespace.md)

## Proof depends on

- [Regular measures](../../mathematics/part-02/measuretheory/regularmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/EnsembleRefinement.lean)
