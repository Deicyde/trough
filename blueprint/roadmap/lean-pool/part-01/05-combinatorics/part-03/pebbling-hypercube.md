---
declaration: theorem
origin: cited
lean: PebblingLean.Hypercube.Paper.optimalPebblingNumber_theta
statement: formalized
proof: formalized
---

# Optimal Pebbling Number of the Hypercube

> Formalizes that the optimal pebbling number of the n-dimensional hypercube Q_n is Theta((4/3)^n). Builds a weight-function lower bound of (4/3)^n and a probabilistic recursive upper bound C \* (4/3)^n with an explicit constant, combining them into a two-sided big-Theta witness.

*Quoted from the card [LeanPool/projects/pebbling-hypercube.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pebbling-hypercube.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PebblingLean.Hypercube.Paper.optimalPebblingNumber_theta`](https://leanpool.github.io/lean-pool/LeanPool/PebblingLean/Paper.html#PebblingLean.Hypercube.Paper.optimalPebblingNumber_theta) (theorem; a main declaration), declared in [LeanPool/PebblingLean/Paper.lean, line 177](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PebblingLean/Paper.lean#L177): “The optimal pebbling number of Q_n has order (4/3)^n: there is a positive constant C with (4/3)^n <= o(Q_n) <= C \* (4/3)^n for all n.”
- [`PebblingLean.Hypercube.Paper.lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/PebblingLean/Paper.html#PebblingLean.Hypercube.Paper.lower_bound) (theorem), declared in [LeanPool/PebblingLean/Paper.lean, line 145](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PebblingLean/Paper.lean#L145): “The optimal pebbling number of Q_n is at least (4/3)^n, proved by a weight-function argument summing one-pebble weights over the cube.”
- [`PebblingLean.Hypercube.Paper.upper_bound`](https://leanpool.github.io/lean-pool/LeanPool/PebblingLean/Paper.html#PebblingLean.Hypercube.Paper.upper_bound) (theorem), declared in [LeanPool/PebblingLean/Paper.lean, line 160](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PebblingLean/Paper.lean#L160): “The optimal pebbling number of Q_n is at most C \* (4/3)^n for an explicit constant C, via a probabilistic recursive splitting construction.”

## Project

- Authors: Lior Pachter.
- Source: *Optimal pebbling number of the hypercube* by Lior Pachter.
- Project repository: [pachterlab/P_2026_2](https://github.com/pachterlab/P_2026_2).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C57.
- In Lean Pool: [LeanPool/PebblingLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PebblingLean), from the card [LeanPool/projects/pebbling-hypercube.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pebbling-hypercube.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/pebbling-hypercube.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pebbling-hypercube.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PebblingLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PebblingLean)
