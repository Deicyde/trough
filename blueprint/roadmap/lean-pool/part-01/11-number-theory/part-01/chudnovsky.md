---
declaration: theorem
origin: cited
lean: Chudnovsky.chudnovskySum_eq_pi_inv
statement: formalized
proof: formalized
---

# A Detailed Proof of the Chudnovsky Formula

> Formalizes the Chudnovsky brothers' rapidly convergent series for 1/π, proving Mathlib's `chudnovskySum = π⁻¹`. Follows Milla's elementary complex-analytic proof: Weierstrass and Eisenstein theory, Liouville and parallelogram-residue calculus, the Kummer hypergeometric bridge and the main modular identity relating the j-invariant to the lattice periods, Baker's division-value machinery, and the singular-moduli inputs at the CM point τ = (1 + √-163)/2 — integrality of j(τ) via modular polynomials and Kronecker's congruence, and rationality of the Weierstrass s₂ invariant via Masser's Appendix A.1.

*Quoted from the card [LeanPool/projects/chudnovsky.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chudnovsky.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Chudnovsky.chudnovskySum_eq_pi_inv`](https://leanpool.github.io/lean-pool/LeanPool/Chudnovsky/Chudnovsky.html#Chudnovsky.chudnovskySum_eq_pi_inv) (theorem; a main declaration), declared in [LeanPool/Chudnovsky/Chudnovsky.lean, line 140](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chudnovsky/Chudnovsky.lean#L140): “Proves the Chudnovsky series identity, i.e. Mathlib's `chudnovskySum = π⁻¹`: the series (12 / 640320^(3/2)) · ∑ₙ (-1)ⁿ (6n)! (545140134 n + 13591409) / ((3n)! (n!)³ 640320^(3n)) sums to 1/π.”

## Project

- Authors: Xuanji Li.
- Source: *A Detailed Proof of the Chudnovsky Formula* by Lorenz Milla, [arXiv:1809.00533](https://arxiv.org/abs/1809.00533).
- Project repository: [ldct/lean-eval-chudnovsky](https://github.com/ldct/lean-eval-chudnovsky).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11Y60, 11F03, 33C05.
- In Lean Pool: [LeanPool/Chudnovsky](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chudnovsky), from the card [LeanPool/projects/chudnovsky.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chudnovsky.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/chudnovsky.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chudnovsky.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Chudnovsky](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Chudnovsky)
