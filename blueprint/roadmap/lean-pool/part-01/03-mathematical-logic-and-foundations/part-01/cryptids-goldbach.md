---
declaration: theorem
origin: cited
lean: ConjectureMachines.Goldbach21.Semantics.halts_candidate_iff_not_goldbach, ConjectureMachines.Brocard28.halts_brocard28_iff_exists_square
statement: formalized
proof: formalized
---

# Finite-state Turing machines for Goldbach and Brocard

> A concrete 21-state binary Turing machine halts on the blank tape exactly when Goldbach's conjecture is false. The proof connects it to the earlier 25-state machine, verifies both machines' prime-search semantics, and preserves finite-machine execution, tape-scanning and reachability infrastructure. A second machine with 28 states halts on the blank tape exactly when there exists a natural number n > 7 for which n! + 1 is a square.

*Quoted from the card [LeanPool/projects/cryptids-goldbach.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/cryptids-goldbach.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ConjectureMachines.Goldbach21.Semantics.halts_candidate_iff_not_goldbach`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Semantics.html#ConjectureMachines.Goldbach21.Semantics.halts_candidate_iff_not_goldbach) (theorem; a main declaration), declared in [LeanPool/CryptidsGoldbach/Semantics.lean, line 70](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach/Semantics.lean#L70): “The explicit 21-state binary Turing machine halts from the blank tape if and only if some even natural number greater than two is not the sum of two primes.”
- [`ConjectureMachines.Goldbach21.candidate_equivalent`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Goldbach21.html#ConjectureMachines.Goldbach21.candidate_equivalent) (theorem), declared in [LeanPool/CryptidsGoldbach/Goldbach21.lean, line 1675](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach/Goldbach21.lean#L1675): “The explicit 21-state and 25-state binary machines have the same blank-tape halting behavior.”
- [`ConjectureMachines.Goldbach21.candidate_fewer_states`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Goldbach21.html#ConjectureMachines.Goldbach21.candidate_fewer_states) (theorem), declared in [LeanPool/CryptidsGoldbach/Goldbach21.lean, line 35](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach/Goldbach21.lean#L35): “The candidate machine has 21 states, strictly fewer than the reference's 25.”
- [`ConjectureMachines.Goldbach21.Semantics.halts_reference_iff_not_goldbach`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/Semantics.html#ConjectureMachines.Goldbach21.Semantics.halts_reference_iff_not_goldbach) (theorem), declared in [LeanPool/CryptidsGoldbach/Semantics.lean, line 61](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach/Semantics.lean#L61): “The 25-state reference machine halts from the blank tape exactly when Goldbach's conjecture is false.”
- [`ConjectureMachines.Brocard28.halts_brocard28_iff_exists_square`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/BrocardSemantics.html#ConjectureMachines.Brocard28.halts_brocard28_iff_exists_square) (theorem; a main declaration), declared in [LeanPool/CryptidsGoldbach/BrocardSemantics.lean, line 68](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach/BrocardSemantics.lean#L68): “The explicit 28-state binary Turing machine halts on the blank tape exactly when n! + 1 is a square for some natural number n greater than seven.”
- [`ConjectureMachines.Brocard28.isSquare_iff_isTri`](https://leanpool.github.io/lean-pool/LeanPool/CryptidsGoldbach/BrocardSemantics.html#ConjectureMachines.Brocard28.isSquare_iff_isTri) (theorem), declared in [LeanPool/CryptidsGoldbach/BrocardSemantics.lean, line 41](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach/BrocardSemantics.lean#L41): “For every natural number n at least four, n! + 1 is a square exactly when n! / 8 is a triangular number.”

## Project

- Authors: Maxence Faldor, Moritz Firsching, Daniel Veljjanoski.
- Project repository: [google-deepmind/cryptids](https://github.com/google-deepmind/cryptids), at commit [481f4e3e](https://github.com/google-deepmind/cryptids/tree/481f4e3e39907304dbcad33e508bf21d80c6d5a6).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 03D10, 11P32.
- In Lean Pool: [LeanPool/CryptidsGoldbach](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach), from the card [LeanPool/projects/cryptids-goldbach.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/cryptids-goldbach.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/cryptids-goldbach.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/cryptids-goldbach.yaml)
- [Lean Pool at bb99e52c: LeanPool/CryptidsGoldbach](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CryptidsGoldbach)
