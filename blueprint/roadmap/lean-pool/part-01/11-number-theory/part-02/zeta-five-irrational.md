---
declaration: theorem
origin: cited
lean: Zeta5Irrational.irrational_five
statement: formalized
proof: formalized
---

# Irrationality of the Riemann zeta function at five

> Proves that Mathlib's Riemann zeta function at five is an irrational real number, following Aabir Fauzan's September 2026 preprint. Constructs integer polynomials of degree 37n with positive values at zeta(5) that decay exponentially in n squared. Includes a general integer-polynomial irrationality criterion, Hankel determinant and moment-integral identities, logarithmic-energy estimates, prime-adic integrality bounds, and kernel-checked rational certificates. The formalization uses a different normalizer and a positive decay constant in place of the paper's specific constant 139/5. Reuses the prime number theorem infrastructure already in the MooreBound project.

*Quoted from the card [LeanPool/projects/zeta-five-irrational.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta-five-irrational.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Zeta5Irrational.irrational_five`](https://leanpool.github.io/lean-pool/LeanPool/Zeta5Irrational/Main.html#Zeta5Irrational.irrational_five) (theorem; a main declaration), declared in [LeanPool/Zeta5Irrational/Main.lean, line 37](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta5Irrational/Main.lean#L37): “There exists an irrational real number x whose complex coercion equals Mathlib's Riemann zeta function evaluated at five.” Its source, as the card gives it: “Fauzan, zeta(5) is irrational, Theorem 1.1, September 17, 2026, https://doi.org/10.5281/zenodo.22826419; upstream Apery/Main.lean. The completed formalization was released on September 23, 2026.”
- [`Zeta5Irrational.main_estimate`](https://leanpool.github.io/lean-pool/LeanPool/Zeta5Irrational/MainEstimate.html#Zeta5Irrational.main_estimate) (theorem), declared in [LeanPool/Zeta5Irrational/MainEstimate.lean, line 85](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta5Irrational/MainEstimate.lean#L85): “There is a positive real c such that, for all sufficiently large n, an integer polynomial Q of degree 37n is a positive rational multiple of the constructed determinant polynomial and satisfies 0 < Q(zeta(5)) < exp(-c\*n^2).” Its source, as the card gives it: “Upstream Apery/MainEstimate.lean; variant of the paper's Theorem 2.1 with c = -800\*(Aeff + U) instead of 139/5.”
- [`Zeta5Irrational.irrational_of_eventually_exists_int_poly`](https://leanpool.github.io/lean-pool/LeanPool/Zeta5Irrational/Criterion.html#Zeta5Irrational.irrational_of_eventually_exists_int_poly) (theorem), declared in [LeanPool/Zeta5Irrational/Criterion.lean, line 62](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta5Irrational/Criterion.lean#L62): “A real xi is irrational if, eventually, integer polynomials of degree at most d(n) have positive values at xi bounded by epsilon(n), and b^d(n)\*epsilon(n) tends to zero for every positive natural b.” Its source, as the card gives it: “Upstream Apery/Criterion.lean; the paper's Section 1.1.”

## Project

- Authors: Moritz Firsching.
- Source: *Zeta5 formalization of Aabir Fauzan's zeta(5) is irrational*.
- Project repository: [mo271/Zeta5](https://github.com/mo271/Zeta5), at commit [f19a1960](https://github.com/mo271/Zeta5/tree/f19a1960609f7d38e7b63fd2acb05e6f60a7b741).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11J72, 11M06, 31A15.
- In Lean Pool: [LeanPool/Zeta5Irrational](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta5Irrational), from the card [LeanPool/projects/zeta-five-irrational.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta-five-irrational.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/zeta-five-irrational.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/zeta-five-irrational.yaml)
- [Lean Pool at 701389c0: LeanPool/Zeta5Irrational](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Zeta5Irrational)
