---
declaration: theorem
origin: cited
lean: ConjectureMachines.Goldbach21.Semantics.halts_candidate_iff_not_goldbach
statement: formalized
proof: formalized
---

# A 21-state Turing machine for Goldbach's conjecture

> A concrete 21-state binary Turing machine halts on the blank tape exactly when Goldbach's conjecture is false. The proof connects it to the earlier 25-state machine, verifies both machines' prime-search semantics, and preserves finite-machine execution, tape-scanning and reachability infrastructure. This imports only the Goldbach dependency closure of Cryptids, excluding its Riemann, ZF and Busy Beaver developments.

*Quoted from the card [LeanPool/projects/cryptids-goldbach.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/cryptids-goldbach.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ConjectureMachines.Goldbach21.Semantics.halts_candidate_iff_not_goldbach`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Semantics.html#ConjectureMachines.Goldbach21.Semantics.halts_candidate_iff_not_goldbach) (theorem; a main declaration), declared in [LeanPool/CryptidsGoldbach/Semantics.lean, line 70](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CryptidsGoldbach/Semantics.lean#L70): “The explicit 21-state binary Turing machine halts from the blank tape if and only if some even natural number greater than two is not the sum of two primes.”
- [`ConjectureMachines.Goldbach21.candidate_equivalent`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Goldbach21.html#ConjectureMachines.Goldbach21.candidate_equivalent) (theorem), declared in [LeanPool/CryptidsGoldbach/Goldbach21.lean, line 1832](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CryptidsGoldbach/Goldbach21.lean#L1832): “The explicit 21-state and 25-state binary machines have the same blank-tape halting behavior.”
- [`ConjectureMachines.Goldbach21.candidate_fewer_states`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Goldbach21.html#ConjectureMachines.Goldbach21.candidate_fewer_states) (theorem), declared in [LeanPool/CryptidsGoldbach/Goldbach21.lean, line 35](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CryptidsGoldbach/Goldbach21.lean#L35): “The candidate machine has 21 states, strictly fewer than the reference's 25.”
- [`ConjectureMachines.Goldbach21.Semantics.halts_reference_iff_not_goldbach`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Semantics.html#ConjectureMachines.Goldbach21.Semantics.halts_reference_iff_not_goldbach) (theorem), declared in [LeanPool/CryptidsGoldbach/Semantics.lean, line 61](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CryptidsGoldbach/Semantics.lean#L61): “The 25-state reference machine halts from the blank tape exactly when Goldbach's conjecture is false.”

## Project

- Authors: Maxence Faldor, Moritz Firsching.
- Project repository: [google-deepmind/cryptids](https://github.com/google-deepmind/cryptids), at commit [f8734348](https://github.com/google-deepmind/cryptids/tree/f873434871b2301d5c8c91ba6fa224f92c93c1e1).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03D10, 11P32.
- In Lean Pool: [LeanPool/CryptidsGoldbach](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CryptidsGoldbach), from the card [LeanPool/projects/cryptids-goldbach.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/cryptids-goldbach.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/cryptids-goldbach.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/cryptids-goldbach.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CryptidsGoldbach](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CryptidsGoldbach)
