---
declaration: theorem
origin: cited
lean: pentagonalNumberTheorem_powerSeries, Nat.Partition.sum_partition
statement: formalized
proof: formalized
---

# Euler's pentagonal number theorem

> Formalizes Euler's pentagonal number theorem as a generating-function identity for power series and for real/complex numbers, with a partition-recurrence corollary and a self-contained Franklin-style combinatorial proof.

*Quoted from the card [LeanPool/projects/pentagonal-number-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/pentagonal-number-theorem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`pentagonalNumberTheorem_powerSeries`](https://leanpool.github.io/lean-pool/LeanPool/PentagonalNumberTheorem/PowerSeries.html#pentagonalNumberTheorem_powerSeries) (theorem; a main declaration), declared in [LeanPool/PentagonalNumberTheorem/PowerSeries.lean, line 82](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PentagonalNumberTheorem/PowerSeries.lean#L82): “Proves Euler's pentagonal number theorem as a formal power series identity ∏(1-xⁿ) = Σ(-1)ᵏ x^(k(3k-1)/2).”
- [`pentagonalNumberTheorem_complex`](https://leanpool.github.io/lean-pool/LeanPool/PentagonalNumberTheorem/Complex.html#pentagonalNumberTheorem_complex) (theorem), declared in [LeanPool/PentagonalNumberTheorem/Complex.lean, line 117](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PentagonalNumberTheorem/Complex.lean#L117): “Proves the analytic version of the pentagonal number theorem for real or complex numbers of norm less than one.”
- [`Nat.Partition.sum_partition`](https://leanpool.github.io/lean-pool/LeanPool/PentagonalNumberTheorem/Partition.html#Nat.Partition.sum_partition) (theorem; a main declaration), declared in [LeanPool/PentagonalNumberTheorem/Partition.lean, line 134](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PentagonalNumberTheorem/Partition.lean#L134): “Derives Euler's pentagonal recurrence for the partition function from the pentagonal number theorem.”

## Project

- Authors: Weiyi Wang.
- Source: [https://en.wikipedia.org/wiki/Pentagonal_number_theorem](https://en.wikipedia.org/wiki/Pentagonal_number_theorem).
- Project repository: [wwylele/PentagonalNumberTheorem](https://github.com/wwylele/PentagonalNumberTheorem).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11P81, 05A17.
- In Lean Pool: [LeanPool/PentagonalNumberTheorem](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PentagonalNumberTheorem), from the card [LeanPool/projects/pentagonal-number-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/pentagonal-number-theorem.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/pentagonal-number-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/pentagonal-number-theorem.yaml)
- [Lean Pool at bb99e52c: LeanPool/PentagonalNumberTheorem](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PentagonalNumberTheorem)
