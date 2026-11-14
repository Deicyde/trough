---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.innerEvaluation, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.continuous_innerEvaluation, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_apply, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_map, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.ext_of_scalarMeasure_eq, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.re_inner_nonneg, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.re_inner_eq_norm_sq
statement: formalized
proof: formalized
---

# Scalar and diagonal measures of a spectral measure

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.ScalarMeasure`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean): 21 declarations, 4 with a docstring.

> The scalar and diagonal measures obtained by pairing a spectral measure with vectors.

## i. Overview

> Pairing a spectral measure `μ` with two vectors gives the complex measure `S ↦ ⟪y, μ S x⟫`, and with
> one vector the finite positive measure `μₓ S = ‖μ S x‖²`, the distribution of the observable in the
> vector state `x`. A spectral measure is determined by its complex measures.

## ii. Key results

> - `WOTSpectralMeasure.scalarMeasure` : the complex measure `S ↦ ⟪y, μ S x⟫`.
> - `WOTSpectralMeasure.ext_of_scalarMeasure_eq` : a spectral measure is determined by its complex
>   measures.
> - `WOTSpectralMeasure.diagonalMeasure` : the measure `S ↦ ‖μ S x‖²`.

## iv. References

> * None.

## A. The scalar (matrix-coefficient) measure and extensionality

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.innerEvaluation`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L62).

> Evaluation of a WOT operator between two test vectors.

```lean
def innerEvaluation (x y : H) : (H →WOT[ℂ] H) →+ ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.continuous_innerEvaluation`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L69).

```lean
lemma continuous_innerEvaluation (x y : H) :
    Continuous (innerEvaluation (H := H) x y)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L76).

> The complex scalar measure obtained by testing a WOT spectral measure against `x` and `y`.
> This is the measure used to state the unbounded reconstruction law weakly.

```lean
def scalarMeasure (x y : H) : ComplexMeasure α
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_apply`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L81).

```lean
lemma scalarMeasure_apply (x y : H) (S : Set α) :
    μS.scalarMeasure x y S = ⟪y, μS S x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_map`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L85).

```lean
lemma scalarMeasure_map {β : Type*} [MeasurableSpace β]
    (f : α → β) (hf : Measurable f) (x y : H) :
    (μS.map f hf).scalarMeasure x y = (μS.scalarMeasure x y).map f
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.ext_of_scalarMeasure_eq`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L98).

> A weak spectral measure is determined by all of its scalar matrix-coefficient measures.
> This is the extensionality principle used when comparing two spectral constructions obtained by
> different bounded or unbounded routes.

```lean
lemma ext_of_scalarMeasure_eq {μS νS : WOTSpectralMeasure α H}
    (h : ∀ x y : H, μS.scalarMeasure x y = νS.scalarMeasure x y) : μS = νS
```

## B. Positivity on the diagonal

> A weak spectral measure gives a positive measure in every vector state.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.re_inner_nonneg`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L112).

```lean
lemma re_inner_nonneg (S : Set α) (x : H) :
    0 ≤ (⟪x, μS S x⟫_ℂ).re
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.re_inner_eq_norm_sq`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L132).

```lean
lemma re_inner_eq_norm_sq (S : Set α) (x : H) :
    (⟪x, μS S x⟫_ℂ).re = ‖μS S x‖ ^ 2
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.inner_eq_inner_projection`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L154).

```lean
lemma inner_eq_inner_projection (S : Set α) (x : H) :
    ⟪x, μS S x⟫_ℂ = ⟪μS S x, μS S x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.inner_eq_zero_of_disjoint`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L171).

```lean
lemma inner_eq_zero_of_disjoint {A B : Set α} (h : Disjoint A B)
    (hA : MeasurableSet A) (hB : MeasurableSet B) (x : H) :
    ⟪μS A x, μS B x⟫_ℂ = 0
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonal_tsum`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L189).

```lean
lemma diagonal_tsum {f : ℕ → Set α} (hf : ∀ i, MeasurableSet (f i))
    (hdisj : Pairwise (Disjoint on f)) (x : H) :
    ENNReal.ofReal (⟪x, μS (⋃ i, f i) x⟫_ℂ).re =
      ∑' i, ENNReal.ofReal (⟪x, μS (f i) x⟫_ℂ).re
```

## C. The diagonal (vector-state) measure

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L212).

> The positive scalar measure obtained by testing a weak PVM on a vector.
>
> Its value on a measurable set is `ofReal (re ⟪x,E(S)x⟫)`. The projection identity below shows
> that this is the usual vector-state spectral measure.

```lean
noncomputable def diagonalMeasure (x : H) : Measure α
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_apply`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L223).

```lean
lemma diagonalMeasure_apply (x : H) (S : Set α) (hS : MeasurableSet S) :
    μS.diagonalMeasure x S = ENNReal.ofReal (⟪x, μS S x⟫_ℂ).re
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_apply_eq_norm_sq`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L227).

```lean
lemma diagonalMeasure_apply_eq_norm_sq (x : H) (S : Set α) (hS : MeasurableSet S) :
    μS.diagonalMeasure x S = ENNReal.ofReal (‖μS S x‖ ^ 2)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_univ`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L231).

```lean
lemma diagonalMeasure_univ (x : H) :
    μS.diagonalMeasure x Set.univ = ENNReal.ofReal (‖x‖ ^ 2)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_map`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L238).

```lean
lemma diagonalMeasure_map {β : Type*} [MeasurableSpace β]
    (f : α → β) (hf : Measurable f) (x : H) :
    (μS.map f hf).diagonalMeasure x = Measure.map f (μS.diagonalMeasure x)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_isFinite`**, an instance, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L249).

```lean
instance diagonalMeasure_isFinite (x : H) : IsFiniteMeasure (μS.diagonalMeasure x)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_neg`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L254).

```lean
lemma diagonalMeasure_neg (x : H) :
    μS.diagonalMeasure (-x) = μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_I_smul`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L261).

```lean
lemma diagonalMeasure_I_smul (x : H) :
    μS.diagonalMeasure (Complex.I • x) = μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_smul`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L268).

```lean
lemma diagonalMeasure_smul (c : ℂ) (x : H) :
    μS.diagonalMeasure (c • x) = ENNReal.ofReal (‖c‖ ^ 2) • μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_parallelogram`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean#L286).

```lean
lemma diagonalMeasure_parallelogram (x y : H) :
    μS.diagonalMeasure (x + y) + μS.diagonalMeasure (x - y) =
      (μS.diagonalMeasure x + μS.diagonalMeasure x) +
        (μS.diagonalMeasure y + μS.diagonalMeasure y)
```

## Depends on

- [Weak-operator spectral measures](../part-01/unbounded-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/ScalarMeasure.lean)
