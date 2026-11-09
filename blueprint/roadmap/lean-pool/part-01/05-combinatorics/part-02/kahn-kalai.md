---
declaration: theorem
origin: cited
lean: KahnKalai.covering_theorem, KahnKalai.park_pham
statement: formalized
proof: formalized
---

# Kahn–Kalai expectation-threshold theorem

> Formalizes Tran and Vu's short proof of the Park–Pham theorem resolving the Kahn–Kalai expectation-threshold conjecture. For an ℓ-bounded family of subsets of a finite ground set, it proves the strengthened covering theorem with the explicit constant L = 1000 and derives the threshold bound p_c(F) ≤ K q(F) log₂ ℓ with the explicit witness K = 100000. The supporting library develops finite-set cover cost, level-density, double-counting, binomial-tail, and numeric estimates.

*Quoted from the card [LeanPool/projects/kahn-kalai.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kahn-kalai.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`KahnKalai.covering_theorem`](https://leanpool.github.io/lean-pool/LeanPool/KahnKalai.html#KahnKalai.covering_theorem) (theorem; a main declaration), declared in [LeanPool/KahnKalai.lean, line 34](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KahnKalai.lean#L34): “If ℓ ≤ N, p lies in [0, 1], and an ℓ-bounded family H has cover cost at least 1/2 - 2^(-(ℓ+2)), then its upset has at least (2/3 + 2^(-(ℓ+2))) choose(N, m) members of cardinality m, where m = floor(1000 p N log₂(ℓ+1)). For m ≤ N this is the corresponding level-density bound; for N < m both cardinalities are zero.”
- [`KahnKalai.park_pham`](https://leanpool.github.io/lean-pool/LeanPool/KahnKalai.html#KahnKalai.park_pham) (theorem; a main declaration), declared in [LeanPool/KahnKalai.lean, line 49](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KahnKalai.lean#L49): “There is an absolute positive constant K such that every ℓ-bounded finite family with ℓ at least two satisfies p_c(F) ≤ K q(F) log₂ ℓ; the proof supplies K = 100000.”

## Project

- Authors: Dan Clemens Posch.
- Source: *A Short Proof of Kahn-Kalai Conjecture* by Phuc Tran, Van Vu, [doi:10.37236/12266](https://doi.org/10.37236/12266), [arXiv:2303.02144](https://arxiv.org/abs/2303.02144).
- Project repository: [dcposch/kahn-kalai-lean](https://github.com/dcposch/kahn-kalai-lean), at commit [641aa75f](https://github.com/dcposch/kahn-kalai-lean/tree/641aa75f8e873d31442f2f7c317b2e7582a26d94).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C80, 60C05.
- In Lean Pool: [LeanPool/KahnKalai](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KahnKalai), from the card [LeanPool/projects/kahn-kalai.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kahn-kalai.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/kahn-kalai.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kahn-kalai.yaml)
- [Lean Pool at 2b205bf9: LeanPool/KahnKalai](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KahnKalai)
