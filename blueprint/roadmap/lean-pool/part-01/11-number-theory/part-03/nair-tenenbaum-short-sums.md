---
declaration: theorem
origin: cited
lean: NairTenenbaum.theoremOne_for_families
statement: formalized
proof: formalized
---

# Nair–Tenenbaum short sums of arithmetic functions

> Uniform upper bounds for arithmetic functions at polynomial values in short intervals, including prime arguments, arithmetic progressions, Hooley moments, smooth values and Goldbach upper bounds. Preserves the sieve, polynomial-root, number-field counting and lattice-discrepancy infrastructure. Includes a counterexample to the printed Lemma 1, replacement comparisons used by the main proofs, and the nonconstant-coordinate restriction for Corollary 6.

*Quoted from the card [LeanPool/projects/nair-tenenbaum-short-sums.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/nair-tenenbaum-short-sums.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`NairTenenbaum.theoremOne_for_families`](https://leanpool.github.io/lean-pool/LeanPool/NairTenenbaum/Results/FamilyTheorems.html#NairTenenbaum.theoremOne_for_families) (theorem; a main declaration), declared in [LeanPool/NairTenenbaum/Results/FamilyTheorems.lean, line 42](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/NairTenenbaum/Results/FamilyTheorems.lean#L42): “For an integer polynomial family of positive total degree with no fixed prime divisor, short sums of admissible nonnegative arithmetic functions satisfy the Nair–Tenenbaum sieve bound in its degree-dependent interval range. The height threshold is independent of the coefficients and discriminant; the bound constant depends on the restricted discriminant. Factorization data are constructed from the original family.”
- [`NairTenenbaum.theoremTwo`](https://leanpool.github.io/lean-pool/LeanPool/NairTenenbaum/Results/TheoremTwo.html#NairTenenbaum.theoremTwo) (theorem), declared in [LeanPool/NairTenenbaum/Results/TheoremTwo.lean, line 29](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/NairTenenbaum/Results/TheoremTwo.lean#L29): “For any nonconstant irreducible integer polynomial Q and integer k greater than its degree, the greatest prime factor of the product of its values over (x, x + y], with y = x^(degree(Q)/k), eventually exceeds y times exp((log x)^alpha), for each alpha < 2 - log 4.”
- [`NairTenenbaum.theoremThree_for_families`](https://leanpool.github.io/lean-pool/LeanPool/NairTenenbaum/Results/PrimeFamilyTheorem.html#NairTenenbaum.theoremThree_for_families) (theorem), declared in [LeanPool/NairTenenbaum/Results/PrimeFamilyTheorem.lean, line 31](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/NairTenenbaum/Results/PrimeFamilyTheorem.lean#L31): “Under the same family and growth hypotheses, with nonzero constant term of the product polynomial, the corresponding bound holds at prime arguments. The constant-term correction is explicit and factorization data are constructed from the original family.”
- [`NairTenenbaum.lemmaTwo`](https://leanpool.github.io/lean-pool/LeanPool/NairTenenbaum/Results/LemmaTwo.html#NairTenenbaum.lemmaTwo) (theorem), declared in [LeanPool/NairTenenbaum/Results/LemmaTwo.lean, line 125](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/NairTenenbaum/Results/LemmaTwo.lean#L125): “The smooth-weight tail estimate holds for general scalar class-M weights, with the stated cutoff, convergent series and uniform constant.”

## Project

- Authors: Jason Davies.
- Source: *Short sums of certain arithmetic functions* by Mohan Nair, Gérald Tenenbaum, [doi:10.1007/BF02392880](https://doi.org/10.1007/BF02392880).
- Project repository: [jasondavies/nair-tenenbaum-short-sums](https://github.com/jasondavies/nair-tenenbaum-short-sums), at commit [0102e310](https://github.com/jasondavies/nair-tenenbaum-short-sums/tree/0102e310a529d531c6da324caba9c0f6b57c8ce9).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11N37, 11N36, 11N25, 11N32.
- In Lean Pool: [LeanPool/NairTenenbaum](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/NairTenenbaum), from the card [LeanPool/projects/nair-tenenbaum-short-sums.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/nair-tenenbaum-short-sums.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/nair-tenenbaum-short-sums.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/nair-tenenbaum-short-sums.yaml)
- [Lean Pool at 701389c0: LeanPool/NairTenenbaum](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/NairTenenbaum)
