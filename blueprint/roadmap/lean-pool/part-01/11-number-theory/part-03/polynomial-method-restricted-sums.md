---
declaration: theorem
origin: cited
lean: ANR_polynomial_method, cauchy_davenport, dias_da_silva_hamidoune
statement: formalized
proof: formalized
---

# The polynomial method and restricted sums of congruence classes

> Formalizes the polynomial method (Alon–Tarsi-style combinatorial Nullstellensatz arguments) and applies it to restricted sums of congruence classes, including Cauchy–Davenport, Dias da Silva–Hamidoune, and a Vandermonde coefficient formula.

*Quoted from the card [LeanPool/projects/polynomial-method-restricted-sums.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/polynomial-method-restricted-sums.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`ANR_polynomial_method`](https://leanpool.github.io/lean-pool/LeanPool/PolynomialMethodRestrictedSums/ANRPolynomialMethod.html#ANR_polynomial_method) (theorem; a main declaration), declared in [LeanPool/PolynomialMethodRestrictedSums/ANRPolynomialMethod.lean, line 1073](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PolynomialMethodRestrictedSums/ANRPolynomialMethod.lean#L1073): “The Alon–Nathanson–Rusza polynomial method theorem, giving a non-vanishing-coefficient criterion for restricted sums.” Its source, as the card gives it: “N. Alon, M. B. Nathanson, I. Z. Ruzsa, The polynomial method and restricted sums of congruence classes, J. Number Theory 56 (1996), 404-417, doi:10.1006/jnth.1996.0029.”
- [`cauchy_davenport`](https://leanpool.github.io/lean-pool/LeanPool/PolynomialMethodRestrictedSums/CauchyDavenportTheorem.html#cauchy_davenport) (theorem; a main declaration), declared in [LeanPool/PolynomialMethodRestrictedSums/CauchyDavenportTheorem.lean, line 193](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PolynomialMethodRestrictedSums/CauchyDavenportTheorem.lean#L193): “The Cauchy–Davenport theorem on sums of subsets of the cyclic group of prime order.” Its source, as the card gives it: “N. Alon, Combinatorial Nullstellensatz, Combinatorics, Probability and Computing 8 (1999), 7-29, doi:10.1017/S0963548398003411.”
- [`dias_da_silva_hamidoune`](https://leanpool.github.io/lean-pool/LeanPool/PolynomialMethodRestrictedSums/DiasDaSilvaHamidoune.html#dias_da_silva_hamidoune) (theorem; a main declaration), declared in [LeanPool/PolynomialMethodRestrictedSums/DiasDaSilvaHamidoune.lean, line 102](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PolynomialMethodRestrictedSums/DiasDaSilvaHamidoune.lean#L102): “The Dias da Silva–Hamidoune lower bound for restricted sums of distinct elements in a prime cyclic group.” Its source, as the card gives it: “J. A. Dias da Silva, Y. O. Hamidoune, Cyclic spaces for Grassmann derivatives and additive theory, Bull. London Math. Soc. 26 (1994), 140-146, doi:10.1112/blms/26.2.140.”
- [`restricted_sum_distinct_sizes`](https://leanpool.github.io/lean-pool/LeanPool/PolynomialMethodRestrictedSums/RestrictedSumDistinctSizes.html#restricted_sum_distinct_sizes) (theorem), declared in [LeanPool/PolynomialMethodRestrictedSums/RestrictedSumDistinctSizes.lean, line 293](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PolynomialMethodRestrictedSums/RestrictedSumDistinctSizes.lean#L293): “A lower bound for restricted sums when the summand sets have distinct sizes.” Its source, as the card gives it: “N. Alon, M. B. Nathanson, I. Z. Ruzsa, The polynomial method and restricted sums of congruence classes, J. Number Theory 56 (1996), 404-417, doi:10.1006/jnth.1996.0029.”
- [`Vandermonde_coefficient_formula`](https://leanpool.github.io/lean-pool/LeanPool/PolynomialMethodRestrictedSums/VandermondeCoefficientFormula.html#Vandermonde_coefficient_formula) (theorem), declared in [LeanPool/PolynomialMethodRestrictedSums/VandermondeCoefficientFormula.lean, line 553](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PolynomialMethodRestrictedSums/VandermondeCoefficientFormula.lean#L553): “A closed-form expression for a specific Vandermonde-style coefficient used by the polynomial method.” Its source, as the card gives it: “N. Alon, M. B. Nathanson, I. Z. Ruzsa, The polynomial method and restricted sums of congruence classes, J. Number Theory 56 (1996), 404-417, doi:10.1006/jnth.1996.0029.”

## Project

- Authors: Nick Adfor.
- Project repository: [NickAdfor/The-polynomial-method-and-restricted-sums-of-congruence-classes](https://github.com/NickAdfor/The-polynomial-method-and-restricted-sums-of-congruence-classes).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11B30, 11B75, 11P70.
- In Lean Pool: [LeanPool/PolynomialMethodRestrictedSums](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PolynomialMethodRestrictedSums), from the card [LeanPool/projects/polynomial-method-restricted-sums.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/polynomial-method-restricted-sums.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/polynomial-method-restricted-sums.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/polynomial-method-restricted-sums.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PolynomialMethodRestrictedSums](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PolynomialMethodRestrictedSums)
