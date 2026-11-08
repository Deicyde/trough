---
declaration: theorem
origin: cited
lean: ACMax.acmax_conjecture
statement: formalized
proof: formalized
---

# Kolokolnikov's ACMAX conjecture

> Proves that every simple graph on n ≥ 4 vertices with 2(n−2) edges has algebraic connectivity at most 2, attained by the complete bipartite graph K₂,ₙ₋₂. Develops Laplacian test-vector bounds, sparse cut certificates, and non-backtracking walk estimates used in the proof.

*Quoted from the card [LeanPool/projects/acmax-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/acmax-conjecture.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`ACMax.acmax_conjecture`](https://leanpool.github.io/lean-pool/LeanPool/ACMax.html#ACMax.acmax_conjecture) (theorem; a main declaration), declared in [LeanPool/ACMax.lean, line 42](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ACMax.lean#L42): “For n ≥ 4, the algebraic connectivity of K₂,ₙ₋₂ is 2, and every simple graph on Fin n with exactly 2(n−2) edges has algebraic connectivity at most 2. Algebraic connectivity is the second-smallest eigenvalue of the combinatorial Laplacian, defined using Mathlib's ordered spectrum.”
- [`ACMax.algConn_mul_sq_le`](https://leanpool.github.io/lean-pool/LeanPool/ACMax/Spectral/RayleighUpper.html#ACMax.algConn_mul_sq_le) (theorem), declared in [LeanPool/ACMax/Spectral/RayleighUpper.lean, line 29](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ACMax/Spectral/RayleighUpper.lean#L29): “For a graph on any nonempty finite vertex type and any real vector whose coordinates sum to zero, algebraic connectivity times the squared norm is at most the Laplacian quadratic form.”
- [`ACMax.algConn_le_two_of_testvector`](https://leanpool.github.io/lean-pool/LeanPool/ACMax/Spectral/TestVector.html#ACMax.algConn_le_two_of_testvector) (theorem), declared in [LeanPool/ACMax/Spectral/TestVector.lean, line 31](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ACMax/Spectral/TestVector.lean#L31): “A nonzero real vector with coordinate sum zero and Laplacian quadratic form at most twice its squared norm certifies algebraic connectivity at most 2.”
- [`ACMax.algConn_completeBipartite_two`](https://leanpool.github.io/lean-pool/LeanPool/ACMax/Spectral/AlgConnK2.html#ACMax.algConn_completeBipartite_two) (theorem), declared in [LeanPool/ACMax/Spectral/AlgConnK2.lean, line 24](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ACMax/Spectral/AlgConnK2.lean#L24): “For n ≥ 4, the complete bipartite graph with parts of sizes 2 and n−2 has algebraic connectivity exactly 2.”

## Project

- Authors: Zeru Zhu, Jinzheng Li, Yuanjie Ren.
- Source: *Maximizing algebraic connectivity for certain families of graphs, Conjecture 1.5* by Theodore Kolokolnikov, [doi:10.1016/j.laa.2014.12.023](https://doi.org/10.1016/j.laa.2014.12.023), [arXiv:1412.6147](https://arxiv.org/abs/1412.6147), [https://github.com/MerLeanProver/ACMaxConjecture/tree/78736ca2f5c29a4d5ad7dfdee4ac715bbfcde770](https://github.com/MerLeanProver/ACMaxConjecture/tree/78736ca2f5c29a4d5ad7dfdee4ac715bbfcde770).
- Project repository: [MerLeanProver/ACMaxConjecture](https://github.com/MerLeanProver/ACMaxConjecture), at commit [78736ca2](https://github.com/MerLeanProver/ACMaxConjecture/tree/78736ca2f5c29a4d5ad7dfdee4ac715bbfcde770).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C50, 05C35.
- In Lean Pool: [LeanPool/ACMax](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ACMax), from the card [LeanPool/projects/acmax-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/acmax-conjecture.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/acmax-conjecture.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/acmax-conjecture.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ACMax](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ACMax)
