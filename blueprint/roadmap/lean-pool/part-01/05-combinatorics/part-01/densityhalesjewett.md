---
declaration: theorem
origin: cited
lean: Combinatorics.Line.exists_of_density_atTop, Combinatorics.Line.exists_of_density, Combinatorics.ArithmeticProgression.exists_of_density_nat
statement: formalized
proof: formalized
---

# The density Hales–Jewett theorem and Szemerédi's theorem

> A Lean 4 formalization of the density Hales–Jewett theorem: for every finite alphabet α and every density δ > 0, all sufficiently large n have the property that any set of at least δ·|α|^n words of length n over α contains a combinatorial line. The basis for the formalization is the combinatorial proof of Dodos, Kanellopoulos, and Tyros. As a consequence, we also formalize Szemerédi's theorem on the integers: for every k ≥ 3 and δ > 0, the following holds for all sufficiently large n. Any subset of {0, …, n−1} of size at least δ·n contains a nonconstant arithmetic progression of length k. The thresholds are explicit: the density Hales–Jewett theorem holds for n ≥ A(4|α|, |α| + ⌈1/δ⌉) and Szemerédi's theorem for n ≥ A(4k + 1, k + ⌈1/δ⌉), where A is the Ackermann function, built on Shelah's bound for the Hales–Jewett numbers from the ShelahHalesJewett project. Varnavides' theorem gives at least n²/A(4k + 1, k + ⌈1/δ⌉) such progressions.

*Quoted from the card [LeanPool/projects/densityhalesjewett.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/densityhalesjewett.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Combinatorics.Line.exists_of_density_atTop`](https://leanpool.github.io/lean-pool/LeanPool/DensityHalesJewett/Solution.html#Combinatorics.Line.exists_of_density_atTop) (theorem; a main declaration), declared in [LeanPool/DensityHalesJewett/Solution.lean, line 35](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett/Solution.lean#L35): “Every positive-density subset of sufficiently long words over a finite nontrivial alphabet contains a combinatorial line.”
- [`Combinatorics.ArithmeticProgression.exists_of_density_nat_atTop`](https://leanpool.github.io/lean-pool/LeanPool/DensityHalesJewett/Solution.html#Combinatorics.ArithmeticProgression.exists_of_density_nat_atTop) (theorem), declared in [LeanPool/DensityHalesJewett/Solution.lean, line 49](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett/Solution.lean#L49): “Every positive-density subset of a sufficiently long initial interval of the natural numbers contains an arithmetic progression of any prescribed length at least three with nonzero common difference.”
- [`Combinatorics.Line.exists_of_density`](https://leanpool.github.io/lean-pool/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.html#Combinatorics.Line.exists_of_density) (theorem; a main declaration), declared in [LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean, line 82](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean#L82): “For a finite alphabet α of k letters, δ > 0 and n ≥ A(4k, k + ⌈1/δ⌉), every set of at least δ·k^n words of length n over α contains a combinatorial line.”
- [`Combinatorics.Line.dhjNumber_le_ack`](https://leanpool.github.io/lean-pool/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.html#Combinatorics.Line.dhjNumber_le_ack) (theorem), declared in [LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean, line 102](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean#L102): “For δ > 0, the density Hales–Jewett number of k letters and density δ is at most A(4k, k + ⌈1/δ⌉).”
- [`Combinatorics.ArithmeticProgression.exists_of_density_nat`](https://leanpool.github.io/lean-pool/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.html#Combinatorics.ArithmeticProgression.exists_of_density_nat) (theorem; a main declaration), declared in [LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean, line 140](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean#L140): “For k ≥ 3, δ > 0 and n ≥ A(4k + 1, k + ⌈1/δ⌉), every subset of {0, …, n − 1} with at least δn elements contains a nonconstant arithmetic progression of length k.”
- [`Combinatorics.ArithmeticProgression.exists_many_of_density_nat`](https://leanpool.github.io/lean-pool/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.html#Combinatorics.ArithmeticProgression.exists_many_of_density_nat) (theorem), declared in [LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean, line 153](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett/DensityHalesJewett/Main.lean#L153): “Under the same hypotheses, the subset contains at least n²/A(4k + 1, k + ⌈1/δ⌉) arithmetic progressions of length k.”

## Project

- Authors: Gabriel Dahia.
- Project repository: [gdahia/densityhalesjewett](https://github.com/gdahia/densityhalesjewett), at commit [478533c4](https://github.com/gdahia/densityhalesjewett/tree/478533c44dbfbb286362cb37e19b0ba53fdc5120).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05D10, 05A05, 11B75, 68R15.
- In Lean Pool: [LeanPool/DensityHalesJewett](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett), from the card [LeanPool/projects/densityhalesjewett.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/densityhalesjewett.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/densityhalesjewett.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/densityhalesjewett.yaml)
- [Lean Pool at 701389c0: LeanPool/DensityHalesJewett](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DensityHalesJewett)
