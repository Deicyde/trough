---
declaration: theorem
origin: cited
lean: ramanujanNagellExact
statement: formalized
proof: formalized
---

# The Ramanujan-Nagell theorem

> Formalizes the Ramanujan-Nagell theorem, proving that the Diophantine equation x^2 + 7 = 2^n has exactly the five positive-integer solutions (|x|, n) = (1, 3), (3, 4), (5, 5), (11, 7), (181, 15).

*Quoted from the card [LeanPool/projects/ramanujan-nagell.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ramanujan-nagell.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ramanujanNagellExact`](https://leanpool.github.io/lean-pool/LeanPool/RamanujanNagell/Basic.html#ramanujanNagellExact) (theorem; a main declaration), declared in [LeanPool/RamanujanNagell/Basic.lean, line 1125](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RamanujanNagell/Basic.lean#L1125): “Proves that the integer solutions of x^2 + 7 = 2^n are exactly (x, n) = (+/-1, 3), (+/-3, 4), (+/-5, 5), (+/-11, 7), (+/-181, 15).” Its source, as the card gives it: “T. Nagell, The Diophantine equation x^2 + 7 = 2^n, Ark. Mat. 4 (1961), 185-187; L. J. Mordell, Diophantine Equations, Academic Press, 1969, Ch. 20.”

## Project

- Authors: Barinder S. Banwait, Xinze Li.
- Source: [arXiv:2604.09808](https://arxiv.org/abs/2604.09808).
- Project repository: [BarinderBanwait/ramanujan_nagell](https://github.com/BarinderBanwait/ramanujan_nagell).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11D61, 11D45, 11R11.
- In Lean Pool: [LeanPool/RamanujanNagell](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RamanujanNagell), from the card [LeanPool/projects/ramanujan-nagell.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ramanujan-nagell.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/ramanujan-nagell.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ramanujan-nagell.yaml)
- [Lean Pool at 701389c0: LeanPool/RamanujanNagell](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RamanujanNagell)
