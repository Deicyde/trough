---
declaration: theorem
origin: cited
lean: SumDifferenceExponent.sSup_admissibleExponents
statement: formalized
proof: formalized
---

# The optimal exponent relating sumsets and difference sets

> For a finite integer set A with at least two elements, proves that C(A) = log(|A+A|/|A|) / log(|A-A|/|A|) is strictly below 2, while explicit finite sets have exponents tending to 2. Thus 2 is the supremum and is never attained. Also gives an explicit witness within 10^(-999) of 2. This imports the upstream base-39 row-and-column variant, not the paper's base-12 automaton construction or its quantitative cardinality estimates. Supporting infrastructure includes injective digit expansions and the strict Pluennecke-Petridis equality argument for finite integer sets.

*Quoted from the card [LeanPool/projects/sum-difference-exponent.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sum-difference-exponent.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SumDifferenceExponent.growthExponent_lt_two`](https://leanpool.github.io/lean-pool/LeanPool/SumDifferenceExponent/Basic.html#SumDifferenceExponent.growthExponent_lt_two) (theorem), declared in [LeanPool/SumDifferenceExponent/Basic.lean, line 449](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent/Basic.lean#L449): “For every finite set A of integers with at least two elements, log(|A+A|/|A|) / log(|A-A|/|A|) is strictly less than 2.”
- [`SumDifferenceExponent.tendsto_growthExponent_approximatingSet`](https://leanpool.github.io/lean-pool/LeanPool/SumDifferenceExponent/Main.html#SumDifferenceExponent.tendsto_growthExponent_approximatingSet) (theorem), declared in [LeanPool/SumDifferenceExponent/Main.lean, line 37](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent/Main.lean#L37): “The growth exponents of the explicit finite integer sets approximatingSet l converge to 2 as l tends to infinity; these sets have at least two elements whenever l is positive.”
- [`SumDifferenceExponent.isLUB_admissibleExponents`](https://leanpool.github.io/lean-pool/LeanPool/SumDifferenceExponent/Main.html#SumDifferenceExponent.isLUB_admissibleExponents) (theorem), declared in [LeanPool/SumDifferenceExponent/Main.lean, line 53](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent/Main.lean#L53): “The number 2 is the least upper bound of the growth exponents of all finite integer sets with at least two elements.”
- [`SumDifferenceExponent.sSup_admissibleExponents`](https://leanpool.github.io/lean-pool/LeanPool/SumDifferenceExponent/Main.html#SumDifferenceExponent.sSup_admissibleExponents) (theorem; a main declaration), declared in [LeanPool/SumDifferenceExponent/Main.lean, line 67](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent/Main.lean#L67): “The supremum of the growth exponents of all finite integer sets with at least two elements equals 2.”
- [`SumDifferenceExponent.supremum_not_attained`](https://leanpool.github.io/lean-pool/LeanPool/SumDifferenceExponent/Main.html#SumDifferenceExponent.supremum_not_attained) (theorem), declared in [LeanPool/SumDifferenceExponent/Main.lean, line 77](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent/Main.lean#L77): “No finite integer set with at least two elements has growth exponent equal to 2.”
- [`SumDifferenceExponent.quantitative_example`](https://leanpool.github.io/lean-pool/LeanPool/SumDifferenceExponent/Quantitative.html#SumDifferenceExponent.quantitative_example) (theorem), declared in [LeanPool/SumDifferenceExponent/Quantitative.lean, line 131](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent/Quantitative.lean#L131): “The explicitly defined finite integer set quantitativeSet has growth exponent strictly between 2 - 10^(-999) and 2.”

## Project

- Authors: Haowei Lin, Shanda Li.
- Source: *Settling the Optimal Exponent Relating Sumsets and Difference Sets* by Haowei Lin, Shanda Li, [arXiv:2607.27199](https://arxiv.org/abs/2607.27199).
- Project repository: [linhaowei1/sum-diff-proof](https://github.com/linhaowei1/sum-diff-proof), at commit [f53f8422](https://github.com/linhaowei1/sum-diff-proof/tree/f53f84223b48457ac922836b661227309d9340c3).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11B13, 11B30, 05D10.
- In Lean Pool: [LeanPool/SumDifferenceExponent](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent), from the card [LeanPool/projects/sum-difference-exponent.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sum-difference-exponent.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/sum-difference-exponent.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sum-difference-exponent.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SumDifferenceExponent](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumDifferenceExponent)
