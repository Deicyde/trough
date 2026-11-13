---
declaration: theorem
origin: cited
lean: LieTrotter.norm_trotter_sub_le_commutator, LieTrotter.trotter_product
statement: formalized
proof: formalized
---

# Lie–Trotter product formula with commutator scaling

> Proves the Lie–Trotter product formula in a complete normed real algebra with norm-one unit, with an explicit error bound proportional to the commutator.

*Quoted from the card [LeanPool/projects/lie-trotter-commutator.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lie-trotter-commutator.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LieTrotter.norm_trotter_sub_le_commutator`](https://leanpool.github.io/lean-pool/LeanPool/LieTrotter/Commutator.html#LieTrotter.norm_trotter_sub_le_commutator) (theorem; a main declaration), declared in [LeanPool/LieTrotter/Commutator.lean, line 176](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LieTrotter/Commutator.lean#L176): “For elements A and B of a complete normed real algebra with norm-one unit and every integer n at least one, the norm of the difference between (exp(A/n) exp(B/n))^n and exp(A+B) is at most norm(AB-BA) exp(norm(A)+norm(B))/(2n).”
- [`LieTrotter.trotter_product`](https://leanpool.github.io/lean-pool/LeanPool/LieTrotter/Basic.html#LieTrotter.trotter_product) (theorem; a main declaration), declared in [LeanPool/LieTrotter/Basic.lean, line 312](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LieTrotter/Basic.lean#L312): “For any two elements of a complete normed real algebra with norm-one unit, (exp(A/n) exp(B/n))^n converges in norm to exp(A+B).”

## Project

- Authors: Zayn Blore.
- Project repository: [zblore/lie-trotter-lean](https://github.com/zblore/lie-trotter-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 46H30, 47D06, 15A16.
- In Lean Pool: [LeanPool/LieTrotter](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LieTrotter), from the card [LeanPool/projects/lie-trotter-commutator.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lie-trotter-commutator.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/lie-trotter-commutator.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lie-trotter-commutator.yaml)
- [Lean Pool at 701389c0: LeanPool/LieTrotter](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LieTrotter)
