---
declaration: theorem
origin: cited
lean: OddPrimeValuationDistribution.oddPrimeValuationGeneratingSeries_identity
statement: formalized
proof: formalized
---

# Exact odd-prime distributions of central-binomial valuations

> Formalizes the exact distribution of the p-adic valuation of the central binomial coefficient binom(2n,n) over every complete block 0 <= n < p^k for every odd prime p. The development proves Kummer correctness for padded digit words, constructs the two-state doubling carry enumerator, identifies it with the arithmetic valuation polynomial, derives its second-order recurrence, proves the rational bivariate generating function, and obtains closed formulas for valuations zero and one.

*Quoted from the card [LeanPool/projects/odd-prime-valuation-distribution.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/odd-prime-valuation-distribution.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`OddPrimeValuationDistribution.oddPrimeValuationGeneratingSeries_identity`](https://leanpool.github.io/lean-pool/LeanPool/OddPrimeValuationDistribution/GeneratingFunction.html#OddPrimeValuationDistribution.oddPrimeValuationGeneratingSeries_identity) (theorem; a main declaration), declared in [LeanPool/OddPrimeValuationDistribution/GeneratingFunction.lean, line 33](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OddPrimeValuationDistribution/GeneratingFunction.lean#L33): “For every odd prime p = 2h+1, proves the denominator-cleared identity for the bivariate series whose coefficient of T^k X^r counts n < p^k with nu_p(binomial(2n,n)) = r; equivalently the series is (1-XT)/(1-(h+1)(1+X)T+pXT^2).” Its source, as the card gives it: “A. Straub, V. H. Moll, T. Amdeberhan, The p-adic valuation of k-central binomial coefficients, Acta Arith. 140 (2009), 31-42.”
- [`OddPrimeValuationDistribution.oddPrimeValuationPolynomial_recurrence`](https://leanpool.github.io/lean-pool/LeanPool/OddPrimeValuationDistribution/ValuationBlocks.html#OddPrimeValuationDistribution.oddPrimeValuationPolynomial_recurrence) (theorem), declared in [LeanPool/OddPrimeValuationDistribution/ValuationBlocks.lean, line 128](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OddPrimeValuationDistribution/ValuationBlocks.lean#L128): “Proves that the exact valuation polynomials satisfy F\_{k+2}(X)+pX F_k(X)=(h+1)(1+X)F\_{k+1}(X), with F_0=1 and F_1=(h+1)+hX.”
- [`OddPrimeValuationDistribution.padicValNat_oddPrime_centralBinom_ofDigits_eq_carryCount`](https://leanpool.github.io/lean-pool/LeanPool/OddPrimeValuationDistribution/CarryArithmetic.html#OddPrimeValuationDistribution.padicValNat_oddPrime_centralBinom_ofDigits_eq_carryCount) (theorem), declared in [LeanPool/OddPrimeValuationDistribution/CarryArithmetic.lean, line 238](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OddPrimeValuationDistribution/CarryArithmetic.lean#L238): “Proves Kummer correctness for every valid padded base-p word: the p-adic valuation of its central binomial coefficient equals the number of carries produced by doubling the word.”
- [`OddPrimeValuationDistribution.card_oddPrimeBlock_valuation_one`](https://leanpool.github.io/lean-pool/LeanPool/OddPrimeValuationDistribution/LowValuations.html#OddPrimeValuationDistribution.card_oddPrimeBlock_valuation_one) (theorem), declared in [LeanPool/OddPrimeValuationDistribution/LowValuations.lean, line 132](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OddPrimeValuationDistribution/LowValuations.lean#L132): “Gives a closed formula for the number of n below p^(k+2) whose central binomial coefficient has p-adic valuation exactly one.”

## Project

- Authors: Egor Lyfar.
- Source: *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen* by Ernst Eduard Kummer, [doi:10.1515/crll.1852.44.93](https://doi.org/10.1515/crll.1852.44.93).
- Project repository: [lyfar/gkp-carry-lean](https://github.com/lyfar/gkp-carry-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11A63, 11B65.
- In Lean Pool: [LeanPool/OddPrimeValuationDistribution](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OddPrimeValuationDistribution), from the card [LeanPool/projects/odd-prime-valuation-distribution.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/odd-prime-valuation-distribution.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/odd-prime-valuation-distribution.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/odd-prime-valuation-distribution.yaml)
- [Lean Pool at 2b205bf9: LeanPool/OddPrimeValuationDistribution](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OddPrimeValuationDistribution)
