---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsFacetSum, ProbabilisticTheory.vals_sum_tmul_facet, ProbabilisticTheory.isFacetSum_vals, ProbabilisticTheory.mem_minTensorCone_of_isFacetSum, ProbabilisticTheory.exists_isApproxBinaryJointEffect, ProbabilisticTheory.IsNuclear.isClassical, ProbabilisticTheory.hasRieszDecomposition_of_minTensorCone_eq_square, HasRieszDecomposition.maxTensorCone_subset_square
statement: formalized
proof: formalized
---

# Classical theories compose uniquely with the square

The module `PhyslibAlpha.ProbabilisticTheory.Classical.NamiokaPhelps`, [PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean): 12 declarations, 11 with a docstring.

> Namioka–Phelps square test: classical exactly when composition with the square is unique.

## i. Overview

> When a system is combined with another, the parts do not decide which composite observables are
> nonnegative. The minimal choice admits only sums of products of nonnegative observables; the maximal
> choice admits everything that local preparations keep nonnegative. For a classical system the two
> coincide: there is only one way to compose it.
>
> It suffices to test composition with the square, the simplest nonclassical state space. A composite
> observable of `E` with the square is given by its four vertex values in `E`. It is in the maximal
> cone when all four values are nonnegative, and in the minimal cone when the values are the facet
> sums of four nonnegative observables of `E`. Solving for these four observables is exactly a Riesz
> decomposition in `E`. So composition with the square is unique exactly when `E` has the Riesz
> decomposition; for complete observables this means that the state space is a Choquet simplex, and
> that every two yes/no measurements are compatible.

## ii. Key results

> - `IsNuclear.isClassical` : a nuclear system is classical.
> - `minTensorCone_eq_maxTensorCone_square_iff` : composition with the square is unique exactly when
>   the observables have the Riesz decomposition.
> - `isClassical_of_minTensorCone_eq_square` : if composition with the square is unique, the
>   positive functionals form a lattice.
> - `isClassical_iff_minTensorCone_eq_square` : **Namioka–Phelps square test**: on a complete
>   Archimedean order-unit space, the state space is a Choquet simplex exactly when composition with
>   the square is unique.
> - `jointlyMeasurable_iff_minTensorCone_eq_square` : every two yes/no measurements are compatible
>   exactly when composition with the square is unique.

## iv. References

> - I. Namioka and R. R. Phelps, *Tensor products of compact convex sets*, Pacific J. Math. 31 (1969),
>   469–480.

## A. Facet coordinates of the minimal cone

**`ProbabilisticTheory.IsFacetSum`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L69).

> Vertex values that are the facet sums of four nonnegative observables.

```lean
def IsFacetSum (A : Fin 4 → E) : Prop
```

**`ProbabilisticTheory.vals_sum_tmul_facet`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L72).

```lean
lemma vals_sum_tmul_facet (X : Fin 4 → E) :
    vals (∑ j, X j ⊗ₜ[ℝ] facet j) = ![X 2 + X 3, X 0 + X 3, X 1 + X 2, X 0 + X 1]
```

**`ProbabilisticTheory.isFacetSum_vals`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L78).

> The vertex values of a composite observable in the minimal cone are facet sums.

```lean
lemma isFacetSum_vals {z : E ⊗[ℝ] Square} (hz : z ∈ minTensorCone E Square) :
    IsFacetSum (vals z)
```

**`ProbabilisticTheory.mem_minTensorCone_of_isFacetSum`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L97).

> A composite observable whose vertex values are facet sums is in the minimal cone.

```lean
lemma mem_minTensorCone_of_isFacetSum {z : E ⊗[ℝ] Square} (hz : IsFacetSum (vals z)) :
    z ∈ minTensorCone E Square
```

## B. Nuclear systems are classical

**`ProbabilisticTheory.exists_isApproxBinaryJointEffect`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L109).

> If the maximal cone of the composite with the square lies in the closure of the minimal cone,
> every two effects have joint effects up to any error: the composite observable with vertex values
> `f, e, 1 - e, 1 - f` is in the maximal cone, and the facet coordinates of a nearby minimal-cone
> observable give the joint effect.

```lean
lemma exists_isApproxBinaryJointEffect
    (h : (maxTensorCone E Square : Set (E ⊗[ℝ] Square)) ⊆ minTensorClosure E Square)
    (e f : Effect E) {δ : ℝ} (hδ : 0 < δ) : ∃ g : E, Effect.IsApproxBinaryJointEffect e f δ g
```

**`ProbabilisticTheory.IsNuclear.isClassical`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L132).

> **Nuclear systems are classical.** If composition with every Archimedean system is unique, the
> positive functionals form a lattice: the state space is a Choquet simplex.

```lean
lemma IsNuclear.isClassical (h : IsNuclear E) : IsClassical E
```

## C. The square test

**`ProbabilisticTheory.hasRieszDecomposition_of_minTensorCone_eq_square`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L145).

> If composition with the square is unique, observables have the Riesz decomposition: the
> composite observable with vertex values `f₁, g, f₁ + f₂ - g, f₂` is in the maximal cone, and its
> facet coordinates split `g`.

```lean
lemma hasRieszDecomposition_of_minTensorCone_eq_square
    (h : minTensorCone E Square = maxTensorCone E Square) : HasRieszDecomposition E
```

**`HasRieszDecomposition.maxTensorCone_subset_square`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L162).

> With the Riesz decomposition, every composite observable with the square in the maximal cone
> is in the minimal cone.

```lean
lemma _root_.HasRieszDecomposition.maxTensorCone_subset_square (hE : HasRieszDecomposition E) :
    maxTensorCone E Square ≤ minTensorCone E Square
```

**`ProbabilisticTheory.minTensorCone_eq_maxTensorCone_square_iff`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L176).

> **Square test.** Composition with the square is unique exactly when the observables have the
> Riesz decomposition.

```lean
lemma minTensorCone_eq_maxTensorCone_square_iff :
    minTensorCone E Square = maxTensorCone E Square ↔ HasRieszDecomposition E
```

## D. Classicality

**`ProbabilisticTheory.isClassical_of_minTensorCone_eq_square`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L185).

> If composition with the square is unique, the positive functionals form a lattice: the state
> space is a Choquet simplex.

```lean
lemma isClassical_of_minTensorCone_eq_square
    (h : minTensorCone E Square = maxTensorCone E Square) : IsClassical E
```

**`ProbabilisticTheory.isClassical_iff_minTensorCone_eq_square`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L197).

> **Namioka–Phelps square test.** On a complete Archimedean order-unit space, the state space is
> a Choquet simplex exactly when composition with the square is unique.

```lean
lemma isClassical_iff_minTensorCone_eq_square :
    IsClassical E ↔ minTensorCone E Square = maxTensorCone E Square
```

**`ProbabilisticTheory.jointlyMeasurable_iff_minTensorCone_eq_square`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean#L204).

> **Two probes of classicality.** On a complete Archimedean order-unit space, every two yes/no
> measurements are compatible exactly when composition with the square is unique.

```lean
lemma jointlyMeasurable_iff_minTensorCone_eq_square :
    (∀ e f : Effect E, Measurement.JointlyMeasurable (Effect.binaryMeasurement e)
      (Effect.binaryMeasurement f)) ↔ minTensorCone E Square = maxTensorCone E Square
```

## Depends on

- [Classical systems](basic.md)
- [The square](../examples/square.md)
- [Compatibility of measurements](../measurement/compatibility.md)

## Proof depends on

- [Classical theories are those without incompatibility](compatibility.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/NamiokaPhelps.lean)
