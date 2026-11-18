---
declaration: module
origin: cited
lean: Finsupp.norm_linearCombination_eq_of_inner_eq
statement: formalized
proof: formalized
---

# Comparing linear combinations by their Gram kernels

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.InnerProductSpace.LinearCombination`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/LinearCombination.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/LinearCombination.lean): 1 declaration, 1 with a docstring.

> Two families with the same pairwise inner products give linear combinations of the same norm when
> supplied with the same finitely supported coefficients.

## i. Overview

> Two families with the same pairwise inner products give linear combinations of the same norm
> when supplied with the same finitely supported coefficients. This comparison applies in
> seminormed inner product spaces and is useful for comparing realizations of a positive-definite
> kernel before constructing an isometry between their closed spans.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`Finsupp.norm_linearCombination_eq_of_inner_eq`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/LinearCombination.lean#L50).

> Families with equal pairwise inner products give linear combinations of equal norm
> for the same finitely supported coefficients.

```lean
lemma norm_linearCombination_eq_of_inner_eq (f : α →₀ 𝕜) {φ : α → E} {ψ : α → F}
    (h : ∀ a b, ⟪φ a, φ b⟫_𝕜 = ⟪ψ a, ψ b⟫_𝕜) :
    ‖linearCombination 𝕜 φ f‖ = ‖linearCombination 𝕜 ψ f‖
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/LinearCombination.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/InnerProductSpace/LinearCombination.lean)
