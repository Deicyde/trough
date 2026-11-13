---
declaration: theorem
origin: cited
lean: Biswal.Theorem23.thm_manifest_coeff_nonneg
statement: formalized
proof: formalized
---

# Chebyshev Quotients and Demazure Multiplicities

> Formalizes positivity results for the coefficients of Chebyshev-type polynomial quotients attached to integer partitions, modelling Demazure multiplicities. Proves that the relevant generating function is a polynomial and that its coefficients are eventually positive (Theorem 1), gives explicit Cauchy-product and matrix-inverse formulas for the coefficients (Theorem 2), and establishes their nonnegativity through a Dyck-path lattice counting model (Theorem 3).

*Quoted from the card [LeanPool/projects/biswal.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/biswal.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Biswal.Theorem1.genFun_is_polynomial`](https://leanpool.github.io/lean-pool/LeanPool/Biswal/Theorem1.html#Biswal.Theorem1.genFun_is_polynomial) (theorem), declared in [LeanPool/Biswal/Theorem1.lean, line 2259](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Biswal/Theorem1.lean#L2259): “Proves that the generating function attached to a partition is a polynomial whenever its parts are bounded by the parameter `m`.”
- [`Biswal.Theorem1.genFun_coeff_eventually_pos`](https://leanpool.github.io/lean-pool/LeanPool/Biswal/Theorem1.html#Biswal.Theorem1.genFun_coeff_eventually_pos) (theorem), declared in [LeanPool/Biswal/Theorem1.lean, line 2268](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Biswal/Theorem1.lean#L2268): “Proves that the coefficients of the generating function attached to a partition are eventually strictly positive.”
- [`Biswal.Theorem23.thm_manifest_coeff_nonneg`](https://leanpool.github.io/lean-pool/LeanPool/Biswal/Theorem23.html#Biswal.Theorem23.thm_manifest_coeff_nonneg) (theorem; a main declaration), declared in [LeanPool/Biswal/Theorem23.lean, line 1079](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Biswal/Theorem23.lean#L1079): “Proves that every coefficient of the generating function is nonnegative, via the explicit Dyck-path lattice counting model.”

## Project

- Authors: Jujian Zhang.
- Source: *Chebyshev quotients, Demazure multiplicities, and Dyck-path models* by Evan Chen, Kenny Lau, Seewoo Lee, Ken Ono, Jujian Zhang, [arXiv:2604.25246](https://arxiv.org/abs/2604.25246).
- Project repository: [AxiomMath/Biswal](https://github.com/AxiomMath/Biswal).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 05E10.
- In Lean Pool: [LeanPool/Biswal](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Biswal), from the card [LeanPool/projects/biswal.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/biswal.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/biswal.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/biswal.yaml)
- [Lean Pool at 701389c0: LeanPool/Biswal](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Biswal)
