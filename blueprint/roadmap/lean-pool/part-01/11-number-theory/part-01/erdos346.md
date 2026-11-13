---
declaration: theorem
origin: cited
lean: Erdos346.intended_problem_if_limit_exists
statement: formalized
proof: formalized
---

# Erdős Problem 346: Ratio Limit Forces the Golden Ratio

> Formalizes the limit-exists interpretation of Erdős Problem 346: for a strictly increasing positive integer sequence with a uniform ratio gap whose finite deletions are complete but whose infinite deletions are not, if the consecutive quotient sequence converges to some real limit greater than one, then that limit must equal the golden ratio and the quotient sequence tends to it.

*Quoted from the card [LeanPool/projects/erdos346.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos346.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Erdos346.intended_problem_if_limit_exists`](https://leanpool.github.io/lean-pool/LeanPool/Erdos346/LimitExistsVariant.html#Erdos346.intended_problem_if_limit_exists) (theorem; a main declaration), declared in [LeanPool/Erdos346/LimitExistsVariant.lean, line 6820](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos346/LimitExistsVariant.lean#L6820): “Existence of any limit greater than one for the quotient sequence forces convergence to the golden ratio, the intended Erdős–Graham conclusion.”
- [`Erdos346.ratio_limit_eq_goldenRatio`](https://leanpool.github.io/lean-pool/LeanPool/Erdos346/LimitExistsVariant.html#Erdos346.ratio_limit_eq_goldenRatio) (theorem), declared in [LeanPool/Erdos346/LimitExistsVariant.lean, line 6574](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos346/LimitExistsVariant.lean#L6574): “If the quotient sequence converges to a limit greater than one under the completeness and incompleteness deletion hypotheses, that limit equals the golden ratio.”
- [`Erdos346.ratio_tendsto_goldenRatio_of_limit_exists`](https://leanpool.github.io/lean-pool/LeanPool/Erdos346/LimitExistsVariant.html#Erdos346.ratio_tendsto_goldenRatio_of_limit_exists) (theorem), declared in [LeanPool/Erdos346/LimitExistsVariant.lean, line 6698](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos346/LimitExistsVariant.lean#L6698): “Under the same hypotheses, the quotient sequence converges to the golden ratio itself.”

## Project

- Authors: KitaKen1.
- Source: *Erdős Problem \#346* by KitaKen1, [https://www.erdosproblems.com/346](https://www.erdosproblems.com/346).
- Project repository: [KitaKen1/erdos346-ratio-limit-lean](https://github.com/KitaKen1/erdos346-ratio-limit-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11B05, 11J70.
- In Lean Pool: [LeanPool/Erdos346](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos346), from the card [LeanPool/projects/erdos346.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos346.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/erdos346.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos346.yaml)
- [Lean Pool at 701389c0: LeanPool/Erdos346](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos346)
