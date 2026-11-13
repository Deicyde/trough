---
declaration: theorem
origin: cited
lean: LeanPoolSensitivity.sensitivity_ge_sqrt_degree
statement: formalized
proof: formalized
---

# Sensitivity Conjecture: sqrt(deg) <= sensitivity

> Formalizes the quantitative Nisan-Szegedy/Huang sensitivity theorem for Boolean functions.

*Quoted from the card [LeanPool/projects/sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/sensitivity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPoolSensitivity.sensitivity_ge_sqrt_degree`](https://leanpool.github.io/lean-pool/LeanPool/Sensitivity/Main.html#LeanPoolSensitivity.sensitivity_ge_sqrt_degree) (theorem; a main declaration), declared in [LeanPool/Sensitivity/Main.lean, line 46](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Sensitivity/Main.lean#L46): “Proves that the square root of multilinear degree is bounded above by sensitivity.”
- [`LeanPoolSensitivity.degree_le_sensitivity_sq`](https://leanpool.github.io/lean-pool/LeanPool/Sensitivity/Consequences.html#LeanPoolSensitivity.degree_le_sensitivity_sq) (theorem), declared in [LeanPool/Sensitivity/Consequences.lean, line 32](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Sensitivity/Consequences.lean#L32): “Derives the degree bound by the square of sensitivity.”

## Project

- Authors: Samuel Schlesinger.
- Source: [doi:10.4007/annals.2019.190.3.6](https://doi.org/10.4007/annals.2019.190.3.6), [arXiv:1907.00847](https://arxiv.org/abs/1907.00847).
- Project repository: [SamuelSchlesinger/sensitivity-conjecture](https://github.com/SamuelSchlesinger/sensitivity-conjecture).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 06E30, 68Q17.
- In Lean Pool: [LeanPool/Sensitivity](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Sensitivity), from the card [LeanPool/projects/sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/sensitivity.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/sensitivity.yaml)
- [Lean Pool at 701389c0: LeanPool/Sensitivity](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Sensitivity)
