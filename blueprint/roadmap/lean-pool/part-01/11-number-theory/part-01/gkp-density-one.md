---
declaration: theorem
origin: cited
lean: GKPCarry.tendsto_gkpSuccessProportion_one
statement: formalized
proof: formalized
---

# Density-One GKP Divisibility and Its Carry-Language Characterization

> Proves that the exponents k satisfying the Graham--Knuth--Patashnik divisibility condition have natural density one. The proof gives an exact all-depth modular sieve, quantitative bounds for possible failures in initial intervals, and a density-zero limit for the failure proportion. It also develops the Kummer digit-sum bridge, the binary-popcount reduction, and a verified ternary carry automaton. The universal GKP conjecture remains open because the possible density-zero failure set may be nonempty.

*Quoted from the card [LeanPool/projects/gkp-density-one.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/gkp-density-one.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 8 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`GKPCarry.tendsto_gkpSuccessProportion_one`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/DensityOne.html#GKPCarry.tendsto_gkpSuccessProportion_one) (theorem; a main declaration), declared in [LeanPool/GKPCarry/DensityOne.lean, line 254](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/DensityOne.lean#L254): “The proportion of exponents k below N for which nine divides the central binomial coefficient indexed by 2^k tends to one as N tends to infinity.”
- [`GKPCarry.card_gkpFailureExponentsBelow_le`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/DensityOne.html#GKPCarry.card_gkpFailureExponentsBelow_le) (theorem), declared in [LeanPool/GKPCarry/DensityOne.lean, line 104](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/DensityOne.lean#L104): “At each ternary depth n+3, the number of possible failures below N is at most (N divided by 2\*3^(n+2), plus one) times (n+9)\*2^n.”
- [`GKPCarry.gkp_exact_modular_sieve`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/InfiniteSieve.html#GKPCarry.gkp_exact_modular_sieve) (theorem), declared in [LeanPool/GKPCarry/InfiniteSieve.lean, line 228](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/InfiniteSieve.lean#L228): “At depth n+3, exactly (n+9)\*2^n of the 2\*3^(n+2) exponent classes remain uncertified; every other class gives divisibility by nine and avoids the deficient carry language for all exponents in that class.”
- [`GKPCarry.gkpConjecture_iff_badCarryLanguageExclusion`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/GKPCharacterization.html#GKPCarry.gkpConjecture_iff_badCarryLanguageExclusion) (theorem), declared in [LeanPool/GKPCarry/GKPCharacterization.lean, line 143](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/GKPCharacterization.lean#L143): “The GKP conjecture is equivalent to the assertion that every nonexceptional power of two avoids the explicitly defined deficient-carry regular language. This is an exact reformulation and does not prove the remaining avoidance assertion.”
- [`GKPCarry.nine_dvd_centralBinom_iff_two_le_ternaryDoubleCarryCount`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/GKPCharacterization.html#GKPCarry.nine_dvd_centralBinom_iff_two_le_ternaryDoubleCarryCount) (theorem), declared in [LeanPool/GKPCarry/GKPCharacterization.lean, line 35](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/GKPCharacterization.lean#L35): “For every natural number n, its central binomial coefficient is divisible by nine exactly when doubling the canonical ternary expansion of n creates at least two carries.”
- [`GKPCarry.badCarryLanguage_true_iff_shape`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/BadCarryLanguage.html#GKPCarry.badCarryLanguage_true_iff_shape) (theorem), declared in [LeanPool/GKPCarry/BadCarryLanguage.lean, line 314](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/BadCarryLanguage.lean#L314): “The deficient-carry automaton accepts exactly three concrete little-endian ternary word shapes: all digits zero or one; a unique top digit two; or a unique two followed by a higher zero with all other digits zero or one.”
- [`GKPCarry.card_badCarryWords`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/BadCarryCounting.html#GKPCarry.card_badCarryWords) (theorem), declared in [LeanPool/GKPCarry/BadCarryCounting.lean, line 149](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/BadCarryCounting.lean#L149): “Among all ternary words of length n+2, exactly (n+7) times 2^n create fewer than two carries when doubled.”
- [`GKPCarry.nine_dvd_centralBinom_four_pow_in_finite_range`](https://leanpool.github.io/lean-pool/LeanPool/GKPCarry/FiniteRangeCorollary.html#GKPCarry.nine_dvd_centralBinom_four_pow_in_finite_range) (theorem), declared in [LeanPool/GKPCarry/FiniteRangeCorollary.lean, line 28](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry/FiniteRangeCorollary.lean#L28): “For every m from 27 through 6560, nine divides the central binomial coefficient indexed by 4^m; this is a bounded computational corollary, not the headline result.”

## Project

- Authors: Egor Lyfar.
- Source: *Concrete Mathematics: A Foundation for Computer Science, Second Edition* by Ronald L. Graham, Donald E. Knuth, Oren Patashnik, [https://cs.stanford.edu/~knuth/gkp.html](https://cs.stanford.edu/~knuth/gkp.html).
- Project repository: [lyfar/gkp-carry-lean](https://github.com/lyfar/gkp-carry-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11A63, 11B65, 68Q45.
- In Lean Pool: [LeanPool/GKPCarry](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry), from the card [LeanPool/projects/gkp-density-one.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/gkp-density-one.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/gkp-density-one.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/gkp-density-one.yaml)
- [Lean Pool at 701389c0: LeanPool/GKPCarry](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/GKPCarry)
