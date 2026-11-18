---
declaration: module
origin: cited
lean: FieldSpecification.wicks_theorem, FieldSpecification.wicks_theorem_congr
statement: formalized
proof: formalized
---

# Wick's theorem

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.WicksTheorem`, [Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheorem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheorem.lean): 2 declarations, 1 with a docstring, 1 listed as significant.

> This file constrains the time-dependent version of Wick's theorem
> for lists of fields containing both fermions and bosons.
>
> Wick's theorem is related to Isserlis' theorem in mathematics.

## Wick terms

## Wick's theorem

**`FieldSpecification.wicks_theorem_congr`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheorem.lean#L42).

```lean
lemma wicks_theorem_congr {φs φs' : List 𝓕.FieldOp} (h : φs = φs') :
    ∑ (φsΛ : WickContraction φs.length), φsΛ.wickTerm
    = ∑ (φs'Λ : WickContraction φs'.length), φs'Λ.wickTerm
```

**`FieldSpecification.wicks_theorem`**, a theorem, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheorem.lean#L79). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For a list `φs` of `𝓕.FieldOp`, Wick's theorem states that
>
> `𝓣(φs) = ∑ φsΛ, φsΛ.wickTerm`
>
> where the sum is over all Wick contraction `φsΛ`.
>
> The proof is via induction on `φs`.
> - The base case `φs = []` is handled by `wickTerm_empty_nil`.
>
> The inductive step works as follows:
>
> For the LHS:
> 1. `timeOrder_eq_maxTimeField_mul_finset` is used to write
>   `𝓣(φ₀…φₙ)` as `𝓢(φᵢ,φ₀…φᵢ₋₁) • φᵢ * 𝓣(φ₀…φᵢ₋₁φᵢ₊₁φₙ)` where `φᵢ` is
>   the maximal time field in `φ₀…φₙ`
> 2. The induction hypothesis is then used on `𝓣(φ₀…φᵢ₋₁φᵢ₊₁φₙ)` to expand it as a sum over
>   Wick contractions of `φ₀…φᵢ₋₁φᵢ₊₁φₙ`.
> 3. This gives terms of the form `φᵢ * φsΛ.wickTerm` on which
>   `mul_wickTerm_eq_sum` is used where `φsΛ` is a Wick contraction of `φ₀…φᵢ₋₁φᵢ₊₁φ`,
>   to rewrite terms as a sum over optional uncontracted elements of `φsΛ`
>
> On the LHS we now have a sum over Wick contractions `φsΛ` of `φ₀…φᵢ₋₁φᵢ₊₁φ` (from 2) and optional
> uncontracted elements of `φsΛ` (from 3)
>
> For the RHS:
> 1. The sum over Wick contractions of `φ₀…φₙ` on the RHS
>   is split via `insertLift_sum` into a sum over Wick contractions `φsΛ` of `φ₀…φᵢ₋₁φᵢ₊₁φ` and
>   sum over optional uncontracted elements of `φsΛ`.
>
> Both sides are now sums over the same thing and their terms equate by the nature of the
> lemmas used.

```lean
theorem wicks_theorem : (φs : List 𝓕.FieldOp) → 𝓣(ofFieldOpList φs) =
    ∑ (φsΛ : WickContraction φs.length), φsΛ.wickTerm
```

## Depends on

- [Wick term](wickalgebra-wickterm.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheorem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/WicksTheorem.lean)
