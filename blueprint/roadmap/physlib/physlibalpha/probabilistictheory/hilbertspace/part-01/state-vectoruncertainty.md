---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.centered_ofVec_apply, ProbabilisticTheory.UnitalPositiveLinearMap.apply_centered_mul_centered_ofVec, ProbabilisticTheory.UnitalPositiveLinearMap.variance_ofVec, ProbabilisticTheory.UnitalPositiveLinearMap.centeredGramDefect_ofVec, ProbabilisticTheory.UnitalPositiveLinearMap.fluctuation, ProbabilisticTheory.UnitalPositiveLinearMap.gram_fluctuation, ProbabilisticTheory.UnitalPositiveLinearMap.transpose_gram_fluctuation, ProbabilisticTheory.UnitalPositiveLinearMap.gram_mulVec_eq_zero_iff
statement: formalized
proof: formalized
---

# Uncertainty in vector states

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.State.VectorUncertainty`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean): 9 declarations, 9 with a docstring.

> Variance and uncertainty defect in a vector state via fluctuation vectors `a ψ - ⟨a⟩ ψ`.

## i. Overview

> In a vector state `ψ` the centered observable `a - ⟨a⟩` sends `ψ` to the fluctuation vector `a ψ -
> ⟨a⟩ ψ`. The variance is its squared norm, and the uncertainty defect of two observables is the
> Cauchy–Schwarz defect of their fluctuation vectors.
>
> For a family of observables, `Σ + iΩ` is the Gram matrix of the fluctuation vectors. Equality in
> Robertson's relation `|det Ω| ≤ det Σ`, with `det Ω ≠ 0`, forces the kernel of this Gram matrix to
> have at least half the dimension: the fluctuation vectors satisfy many linear relations.

## ii. Key results

> - `UnitalPositiveLinearMap.apply_centered_mul_centered_ofVec` : the covariance matrix entry is the
>   inner product of fluctuation vectors.
> - `UnitalPositiveLinearMap.variance_ofVec` : the variance is the squared norm of the fluctuation
>   vector.
> - `UnitalPositiveLinearMap.centeredGramDefect_ofVec` : the uncertainty defect is `‖x‖² ‖y‖² - ‖⟪x,
>   y⟫‖²`.
> - `UnitalPositiveLinearMap.gram_fluctuation` : `Σ + iΩ` is the Gram matrix of the fluctuation
>   vectors.
> - `UnitalPositiveLinearMap.card_le_two_mul_finrank_ker_gram_fluctuation` : at equality in
>   Robertson's relation for several observables, the fluctuation vectors satisfy at least half as
>   many independent linear relations as there are observables.

## iv. References

> * H. P. Robertson, *An indeterminacy relation for several observables and its classical
>   interpretation*, Phys. Rev. 46 (1934) 794.

## A. Fluctuation vectors in vector states

**`ProbabilisticTheory.UnitalPositiveLinearMap.centered_ofVec_apply`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L72).

> The fluctuation vector `a ψ - ⟨a⟩ ψ` is the centered observable applied to `ψ`.

```lean
lemma centered_ofVec_apply (h : ‖ψ‖ = 1) (a : Observable (H →L[ℂ] H)) :
    (centered (ofVec h) a : H →L[ℂ] H) ψ = (a : H →L[ℂ] H) ψ - (ofVec h)⟨a⟩ • ψ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_centered_mul_centered_ofVec`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L79).

> The state of a product of centered observables is the inner product of the two fluctuation
> vectors.

```lean
lemma apply_centered_mul_centered_ofVec (h : ‖ψ‖ = 1) (a b : Observable (H →L[ℂ] H)) :
    ofVec h ((centered (ofVec h) a : H →L[ℂ] H) * (centered (ofVec h) b : H →L[ℂ] H)) =
      ⟪(a : H →L[ℂ] H) ψ - (ofVec h)⟨a⟩ • ψ, (b : H →L[ℂ] H) ψ - (ofVec h)⟨b⟩ • ψ⟫_ℂ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.variance_ofVec`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L87).

> The variance in a vector state is the squared norm of the fluctuation vector.

```lean
lemma variance_ofVec (h : ‖ψ‖ = 1) (a : Observable (H →L[ℂ] H)) :
    variance (ofVec h) a = ‖(a : H →L[ℂ] H) ψ - (ofVec h)⟨a⟩ • ψ‖ ^ 2
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.centeredGramDefect_ofVec`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L94).

> The centered Gram defect of a vector state is the Cauchy–Schwarz defect of the two
> fluctuation vectors.

```lean
lemma centeredGramDefect_ofVec (h : ‖ψ‖ = 1) (a b : Observable (H →L[ℂ] H)) :
    centeredGramDefect (ofVec h) a b =
      ‖(a : H →L[ℂ] H) ψ - (ofVec h)⟨a⟩ • ψ‖ ^ 2 * ‖(b : H →L[ℂ] H) ψ - (ofVec h)⟨b⟩ • ψ‖ ^ 2 -
        ‖⟪(a : H →L[ℂ] H) ψ - (ofVec h)⟨a⟩ • ψ, (b : H →L[ℂ] H) ψ - (ofVec h)⟨b⟩ • ψ⟫_ℂ‖ ^ 2
```

## B. Equality in Robertson's relation for several observables

**`ProbabilisticTheory.UnitalPositiveLinearMap.fluctuation`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L112).

> The fluctuation vector `a ψ - ⟨a⟩ ψ` of an observable in a vector state.

```lean
noncomputable def fluctuation (h : ‖ψ‖ = 1) (a : Observable (H →L[ℂ] H)) : H
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gram_fluctuation`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L116).

> In a vector state, `Σ + iΩ` is the Gram matrix of the fluctuation vectors.

```lean
lemma gram_fluctuation (h : ‖ψ‖ = 1) (a : ι → Observable (H →L[ℂ] H)) :
    gram ℂ (fun j => fluctuation h (a j)) =
      (covarianceMatrix (ofVec h) a).map ((↑) : ℝ → ℂ) +
        Complex.I • (bracketMatrix (ofVec h) a).map ((↑) : ℝ → ℂ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.transpose_gram_fluctuation`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L126).

> In a vector state, `Σ − iΩ` is the transpose of the Gram matrix of the fluctuation vectors.

```lean
lemma transpose_gram_fluctuation (h : ‖ψ‖ = 1) (a : ι → Observable (H →L[ℂ] H)) :
    (gram ℂ (fun j => fluctuation h (a j)))ᵀ =
      (covarianceMatrix (ofVec h) a).map ((↑) : ℝ → ℂ) -
        Complex.I • (bracketMatrix (ofVec h) a).map ((↑) : ℝ → ℂ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gram_mulVec_eq_zero_iff`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L137).

> The kernel of a Gram matrix is the space of linear relations among the vectors.

```lean
lemma gram_mulVec_eq_zero_iff [Fintype ι] (v : ι → H) (c : ι → ℂ) :
    gram ℂ v *ᵥ c = 0 ↔ ∑ j, c j • v j = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.card_le_two_mul_finrank_ker_gram_fluctuation`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean#L153).

> **Equality in Robertson's relation for several observables.** In a vector state with
> `|det Ω| = det Σ ≠ 0`, the fluctuation vectors of the family satisfy linear relations
> `∑ j, c j • (a_j ψ - ⟨a_j⟩ ψ) = 0` forming a space of at least half the size of the family.

```lean
lemma card_le_two_mul_finrank_ker_gram_fluctuation [Fintype ι] [DecidableEq ι] (h : ‖ψ‖ = 1)
    (a : ι → Observable (H →L[ℂ] H)) (hΩ : (bracketMatrix (ofVec h) a).det ≠ 0)
    (heq : |(bracketMatrix (ofVec h) a).det| = (covarianceMatrix (ofVec h) a).det) :
    Fintype.card ι ≤
      2 * Module.finrank ℂ (LinearMap.ker (gram ℂ fun j => fluctuation h (a j)).mulVecLin)
```

## Depends on

- [Uncertainty relations](../../cstaralgebra/uncertainty.md)
- [Vector states](state-vector.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/VectorUncertainty.lean)
