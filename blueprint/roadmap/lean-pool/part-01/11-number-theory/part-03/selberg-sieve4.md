---
declaration: theorem
origin: cited
lean: fundamental_theorem_simple, primeCounting_isBigO_atTop, primesBetween_le
statement: formalized
proof: formalized
---

# Selberg Sieve

> Formalizes the Selberg sieve with applications to prime-counting bounds and a Brun-Titchmarsh-style estimate.

*Quoted from the card [LeanPool/projects/selberg-sieve4.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/selberg-sieve4.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`fundamental_theorem_simple`](https://leanpool.github.io/lean-pool/LeanPool/SelbergSieve4/MainResults.html#fundamental_theorem_simple) (theorem; a main declaration), declared in [LeanPool/SelbergSieve4/MainResults.lean, line 29](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SelbergSieve4/MainResults.lean#L29): “Proves the simple Selberg sieve upper-bound theorem.”
- [`primeCounting_isBigO_atTop`](https://leanpool.github.io/lean-pool/LeanPool/SelbergSieve4/MainResults.html#primeCounting_isBigO_atTop) (theorem; a main declaration), declared in [LeanPool/SelbergSieve4/MainResults.lean, line 35](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SelbergSieve4/MainResults.lean#L35): “Derives the asymptotic prime-counting upper bound.”
- [`primeCounting_le_mul`](https://leanpool.github.io/lean-pool/LeanPool/SelbergSieve4/MainResults.html#primeCounting_le_mul) (theorem), declared in [LeanPool/SelbergSieve4/MainResults.lean, line 39](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SelbergSieve4/MainResults.lean#L39): “Gives an eventual explicit constant upper bound for the prime-counting function.”
- [`primesBetween_le`](https://leanpool.github.io/lean-pool/LeanPool/SelbergSieve4/MainResults.html#primesBetween_le) (theorem; a main declaration), declared in [LeanPool/SelbergSieve4/MainResults.lean, line 42](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SelbergSieve4/MainResults.lean#L42): “Bounds the number of primes in an interval using the sieve estimate.”

## Project

- Authors: Arend Mellendijk.
- Source: *Sieve Methods* by Heini Halberstam, Hans-Egon Richert, [https://archive.org/details/sievemethods0000halb](https://archive.org/details/sievemethods0000halb).
- Project repository: [amellendijk/selberg-sieve4](https://github.com/amellendijk/selberg-sieve4).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11N35, 11N05, 11N13.
- In Lean Pool: [LeanPool/SelbergSieve4](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SelbergSieve4), from the card [LeanPool/projects/selberg-sieve4.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/selberg-sieve4.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/selberg-sieve4.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/selberg-sieve4.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SelbergSieve4](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SelbergSieve4)
