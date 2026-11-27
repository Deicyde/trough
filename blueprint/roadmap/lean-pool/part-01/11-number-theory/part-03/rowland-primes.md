---
declaration: theorem
origin: cited
lean: RowlandPrimes.rowland_diff_eq_one_or_prime, RowlandPrimes.increment_eq_one_or_minFac
statement: formalized
proof: formalized
---

# Rowland's prime-generating recurrence

> Proves Rowland's 2008 theorem that the sequence a(1) = 7, a(n) = a(n - 1) + gcd(n, a(n - 1)) has every increment a(n) - a(n - 1), n >= 2, equal to 1 or a prime, in the form stated without proof in Formal Conjectures. The core is the r = 3 case of Rowland's Lemma 1, proved for any sequence obeying the recurrence from some index on - from a point N >= 2 with a(N) = 3N the increments are 1 until the step into N + (p - 1)/2, which adds the least prime factor p of 2N - 1 and lands again on a = 3n. Consequences - no increment is 2, infinitely many increments are prime, a closed form between checkpoints, and a kernel-checked example showing that the first term matters (a(1) = 532 gives the composite increment 9 at n = 18).

*Quoted from the card [LeanPool/projects/rowland-primes.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rowland-primes.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RowlandPrimes.rowland_diff_eq_one_or_prime`](https://leanpool.github.io/lean-pool/LeanPool/RowlandPrimes/Sequence.html#RowlandPrimes.rowland_diff_eq_one_or_prime) (theorem; a main declaration), declared in [LeanPool/RowlandPrimes/Sequence.lean, line 98](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RowlandPrimes/Sequence.lean#L98): “For Rowland's sequence a(1) = 7, a(n) = a(n - 1) + gcd(n, a(n - 1)), every increment a(n) - a(n - 1) with n >= 2 is 1 or a prime (Rowland 2008, Theorem 1; the statement of Formal Conjectures' RowlandSequence.rowland_diff_eq_one_or_prime).”
- [`RowlandPrimes.increment_eq_one_or_minFac`](https://leanpool.github.io/lean-pool/LeanPool/RowlandPrimes/Basic.html#RowlandPrimes.increment_eq_one_or_minFac) (theorem; a main declaration), declared in [LeanPool/RowlandPrimes/Basic.lean, line 247](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RowlandPrimes/Basic.lean#L247): “For any sequence obeying a(n + 1) = a(n) + gcd(n + 1, a(n)) for n >= n0, if N >= n0, N >= 2 and a(N) = 3N, then for every n >= N the increment a(n + 1) - a(n) is either 1 or equal to the least prime factor of 2M - 1 for a checkpoint M with n + 1 = M + (minFac(2M - 1) - 1)/2 (the r = 3 case of Rowland's Lemma 1, iterated).”
- [`RowlandPrimes.isCheckpoint_next`](https://leanpool.github.io/lean-pool/LeanPool/RowlandPrimes/Basic.html#RowlandPrimes.isCheckpoint_next) (theorem), declared in [LeanPool/RowlandPrimes/Basic.lean, line 202](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RowlandPrimes/Basic.lean#L202): “If a(N) = 3N with N >= 2 (and the recurrence holds from N on), then a(N + (p - 1)/2) = 3(N + (p - 1)/2), where p is the least prime factor of 2N - 1.”
- [`RowlandPrimes.infinite_setOf_prime_rowlandDiff`](https://leanpool.github.io/lean-pool/LeanPool/RowlandPrimes/Sequence.html#RowlandPrimes.infinite_setOf_prime_rowlandDiff) (theorem), declared in [LeanPool/RowlandPrimes/Sequence.lean, line 135](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RowlandPrimes/Sequence.lean#L135): “Infinitely many increments of Rowland's sequence are prime.”
- [`RowlandPrimes.rowlandSeqFrom_532_composite`](https://leanpool.github.io/lean-pool/LeanPool/RowlandPrimes/Sequence.html#RowlandPrimes.rowlandSeqFrom_532_composite) (theorem), declared in [LeanPool/RowlandPrimes/Sequence.lean, line 155](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RowlandPrimes/Sequence.lean#L155): “With first term a(1) = 532 instead of 7, the increment a(18) - a(17) equals 9, which is not prime.”

## Project

- Authors: Yujie Sun, Claude Opus 5.5 (AI).
- Source: *A natural prime-generating recurrence* by Eric S. Rowland, [arXiv:0710.3217](https://arxiv.org/abs/0710.3217), [https://cs.uwaterloo.ca/journals/JIS/VOL11/Rowland/rowland21.html](https://cs.uwaterloo.ca/journals/JIS/VOL11/Rowland/rowland21.html).
- Project repository: [Feynman724/rowland-primes-lean](https://github.com/Feynman724/rowland-primes-lean), at commit [93e323e0](https://github.com/Feynman724/rowland-primes-lean/tree/93e323e048d49ecd3d52c6ab86815c0118a143e5).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11A41, 11B37.
- In Lean Pool: [LeanPool/RowlandPrimes](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RowlandPrimes), from the card [LeanPool/projects/rowland-primes.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rowland-primes.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/rowland-primes.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rowland-primes.yaml)
- [Lean Pool at bb99e52c: LeanPool/RowlandPrimes](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RowlandPrimes)
