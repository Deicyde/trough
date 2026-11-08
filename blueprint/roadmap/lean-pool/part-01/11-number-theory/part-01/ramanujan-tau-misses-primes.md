---
declaration: theorem
origin: cited
lean: main_theorem, reduction_lemma, abc_bound_E2, abc_bound_E4
statement: formalized
proof: formalized
---

# ABC implies that Ramanujan's tau function misses almost all primes

> Formalizes the ABC-conditional proof that Ramanujan's tau function takes prime values only rarely.

*Quoted from the card [LeanPool/projects/ramanujan-tau-misses-primes.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ramanujan-tau-misses-primes.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`main_theorem`](https://leanpool.github.io/lean-pool/LeanPool/RamanujanTauMissesPrimes/Solution.html#main_theorem) (theorem; a main declaration), declared in [LeanPool/RamanujanTauMissesPrimes/Solution.lean, line 5345](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RamanujanTauMissesPrimes/Solution.lean#L5345): “ABC implies that Ramanujan's tau function misses almost all primes.”
- [`reduction_lemma`](https://leanpool.github.io/lean-pool/LeanPool/RamanujanTauMissesPrimes/Solution.html#reduction_lemma) (theorem; a main declaration), declared in [LeanPool/RamanujanTauMissesPrimes/Solution.lean, line 3969](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RamanujanTauMissesPrimes/Solution.lean#L3969): “Reduces the main prime-value statement to the key analytic estimates.”
- [`abc_bound_E2`](https://leanpool.github.io/lean-pool/LeanPool/RamanujanTauMissesPrimes/Solution.html#abc_bound_E2) (theorem; a main declaration), declared in [LeanPool/RamanujanTauMissesPrimes/Solution.lean, line 5086](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RamanujanTauMissesPrimes/Solution.lean#L5086): “ABC-bound input for the Eisenstein-series term E2.”
- [`abc_bound_E4`](https://leanpool.github.io/lean-pool/LeanPool/RamanujanTauMissesPrimes/Solution.html#abc_bound_E4) (theorem; a main declaration), declared in [LeanPool/RamanujanTauMissesPrimes/Solution.lean, line 5291](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RamanujanTauMissesPrimes/Solution.lean#L5291): “ABC-bound input for the Eisenstein-series term E4.”

## Project

- Authors: Evan Chen, Kenny Lau, Ken Ono, Jujian Zhang.
- Source: [arXiv:2603.29970](https://arxiv.org/abs/2603.29970).
- Project repository: [AxiomMath/ramanujan-tau-misses-primes](https://github.com/AxiomMath/ramanujan-tau-misses-primes).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2026 Axiom Math”.
- MSC2020: 11F30, 11N05.
- In Lean Pool: [LeanPool/RamanujanTauMissesPrimes](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RamanujanTauMissesPrimes), from the card [LeanPool/projects/ramanujan-tau-misses-primes.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ramanujan-tau-misses-primes.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/ramanujan-tau-misses-primes.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ramanujan-tau-misses-primes.yaml)
- [Lean Pool at 2b205bf9: LeanPool/RamanujanTauMissesPrimes](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RamanujanTauMissesPrimes)
