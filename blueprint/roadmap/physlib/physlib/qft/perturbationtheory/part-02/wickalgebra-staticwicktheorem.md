---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.static_wick_theorem
statement: formalized
proof: formalized
---

# Static Wick's theorem

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.StaticWickTheorem`, [Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTheorem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTheorem.lean): 1 declaration, 1 with a docstring, 1 listed as significant.

**`FieldSpecification.WickAlgebra.static_wick_theorem`**, a theorem, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTheorem.lean#L57). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For a list `φs` of `𝓕.FieldOp`, the static version of Wick's theorem states that
>
> `φs = ∑ φsΛ, φsΛ.staticWickTerm`
>
> where the sum is over all Wick contraction `φsΛ`.
>
> The proof is via induction on `φs`.
> - The base case `φs = []` is handled by `staticWickTerm_empty_nil`.
>
> The inductive step works as follows:
>
> For the LHS:
> 1. The proof considers `φ₀…φₙ` as `φ₀(φ₁…φₙ)` and uses the induction hypothesis on `φ₁…φₙ`.
> 2. This gives terms of the form `φ * φsΛ.staticWickTerm` on which
>   `mul_staticWickTerm_eq_sum` is used where `φsΛ` is a Wick contraction of `φ₁…φₙ`,
>   to rewrite terms as a sum over optional uncontracted elements of `φsΛ`
>
> On the LHS we now have a sum over Wick contractions `φsΛ` of `φ₁…φₙ` (from 1) and optional
> uncontracted elements of `φsΛ` (from 2)
>
> For the RHS:
> 1. The sum over Wick contractions of `φ₀…φₙ` on the RHS
>   is split via `insertLift_sum` into a sum over Wick contractions `φsΛ` of `φ₁…φₙ` and
>   sum over optional uncontracted elements of `φsΛ`.
>
> Both sides are now sums over the same thing and their terms equate by the nature of the
> lemmas used.

```lean
theorem static_wick_theorem : (φs : List 𝓕.FieldOp) →
    ofFieldOpList φs = ∑ (φsΛ : WickContraction φs.length), φsΛ.staticWickTerm
```

## Depends on

- [Static Wick's terms](wickalgebra-staticwickterm.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTheorem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/StaticWickTheorem.lean)
