---
declaration: theorem
origin: cited
lean: IwaniecLinearSieve.iwaniecBound
statement: formalized
proof: formalized
---

# Iwaniec's linear sieve and Jacobsthal's bound

> Proves an absolute O((r log r)^2) bound for any run of consecutive integers covered by r distinct primes, using the Rosser-Iwaniec linear sieve at the sifting limit. Preserves the combinatorial sieve, delay-equation majorants, prime-sum estimates and the proved strong prime-number-theorem dependency. This imports the dependency closure of the Jacobsthal corollary, rather than claiming the upstream formalizations of both papers in full.

*Quoted from the card [LeanPool/projects/iwaniec-linear-sieve.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/iwaniec-linear-sieve.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`IwaniecLinearSieve.iwaniecBound`](https://leanpool.github.io/lean-pool/LeanPool/IwaniecLinearSieve/Jacobsthal.html#IwaniecLinearSieve.iwaniecBound) (theorem; a main declaration), declared in [LeanPool/IwaniecLinearSieve/Jacobsthal.lean, line 35](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IwaniecLinearSieve/Jacobsthal.lean#L35): “There is an absolute real constant C such that, for every finite set S of at least two primes and every interval of m consecutive integers each divisible by a prime in S, m is at most C times (|S| log |S|)^2.”
- [`IwaniecLinearSieve.shiftedSieve`](https://leanpool.github.io/lean-pool/LeanPool/IwaniecLinearSieve/Jacobsthal/ShiftedSieve.html#IwaniecLinearSieve.shiftedSieve) (theorem), declared in [LeanPool/IwaniecLinearSieve/Jacobsthal/ShiftedSieve.lean, line 455](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IwaniecLinearSieve/Jacobsthal/ShiftedSieve.lean#L455): “Rosser's lower-bound sieve for the first r primes transfers to any set of r primes, bounding the number of integers avoiding all those primes.”
- [`IwaniecLinearSieve.linearSieveEstimate`](https://leanpool.github.io/lean-pool/LeanPool/IwaniecLinearSieve/LinearSieve/Estimate.html#IwaniecLinearSieve.linearSieveEstimate) (theorem), declared in [LeanPool/IwaniecLinearSieve/LinearSieve/Estimate.lean, line 122](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IwaniecLinearSieve/LinearSieve/Estimate.lean#L122): “At a fixed constant times z squared, Rosser's lower-bound sieve has main term bounded below by a positive constant times R(z)/log z and support bounded above by a constant times z squared divided by log squared z, for all sufficiently large z.”

## Project

- Authors: Jason Davies, PrimeNumberTheoremAnd contributors.
- Source: *On the problem of Jacobsthal* by Henryk Iwaniec, [doi:10.1515/dema-1978-0121](https://doi.org/10.1515/dema-1978-0121), [https://github.com/jasondavies/iwaniec-linear-sieve/tree/c8d01549d2ae640b36ec198c1f0f6495f1b036cf](https://github.com/jasondavies/iwaniec-linear-sieve/tree/c8d01549d2ae640b36ec198c1f0f6495f1b036cf).
- Project repository: [jasondavies/iwaniec-linear-sieve](https://github.com/jasondavies/iwaniec-linear-sieve), at commit [c8d01549](https://github.com/jasondavies/iwaniec-linear-sieve/tree/c8d01549d2ae640b36ec198c1f0f6495f1b036cf).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11N35, 11N36, 11N25.
- In Lean Pool: [LeanPool/IwaniecLinearSieve](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IwaniecLinearSieve), from the card [LeanPool/projects/iwaniec-linear-sieve.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/iwaniec-linear-sieve.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/iwaniec-linear-sieve.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/iwaniec-linear-sieve.yaml)
- [Lean Pool at 2b205bf9: LeanPool/IwaniecLinearSieve](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/IwaniecLinearSieve)
