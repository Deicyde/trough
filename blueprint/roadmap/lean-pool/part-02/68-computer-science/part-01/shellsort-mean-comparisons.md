---
declaration: theorem
origin: cited
lean: Shellsort.HarvestFullSchedule.exists_size_indexed_family, Shellsort.PredeterminedOptimum.exists_optimal_executed_family, Shellsort.PhysicalKeyOptimum.exists_uniform_family_for_physical_keys
statement: formalized
proof: formalized
---

# Optimal mean comparison count for ordinary Shellsort

> An input-independent gap table attains the minimum mean key comparison count of ordinary Shellsort on uniform permutations of distinct keys. The minimum has order n log n, and a witnessing upper-bound table uses at most the base-two logarithm of n passes rounded down.

*Quoted from the card [LeanPool/projects/shellsort-mean-comparisons.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/shellsort-mean-comparisons.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Shellsort.HarvestFullSchedule.exists_size_indexed_family`](https://leanpool.github.io/lean-pool/LeanPool/ShellsortMean/HarvestFullSchedule.html#Shellsort.HarvestFullSchedule.exists_size_indexed_family) (theorem; a main declaration), declared in [LeanPool/ShellsortMean/HarvestFullSchedule.lean, line 106](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ShellsortMean/HarvestFullSchedule.lean#L106): “For each input size n at least two, one strictly decreasing positive gap table ending in one sorts every rank permutation. It uses at most the base-two logarithm of n passes rounded down and averages at most (1 + 2^165) n log_2 n comparisons under the uniform distribution.”
- [`Shellsort.PredeterminedOptimum.exists_optimal_executed_family`](https://leanpool.github.io/lean-pool/LeanPool/ShellsortMean/VerifiedOptimum.html#Shellsort.PredeterminedOptimum.exists_optimal_executed_family) (theorem; a main declaration), declared in [LeanPool/ShellsortMean/VerifiedOptimum.lean, line 38](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ShellsortMean/VerifiedOptimum.lean#L38): “A size-indexed family of legal gap tables minimizes the mean number of executed key comparisons. For n at least two the minimum lies between log_2(n!) and (1 + 2^165) n log_2 n.”
- [`Shellsort.PhysicalKeyOptimum.exists_uniform_family_for_physical_keys`](https://leanpool.github.io/lean-pool/LeanPool/ShellsortMean/PhysicalKeyOptimum.html#Shellsort.PhysicalKeyOptimum.exists_uniform_family_for_physical_keys) (theorem; a main declaration), declared in [LeanPool/ShellsortMean/PhysicalKeyOptimum.lean, line 60](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ShellsortMean/PhysicalKeyOptimum.lean#L60): “The same tables sort and attain the same optimal mean comparison count for every ordered key set of size n under uniform bijective input.”

## Project

- Authors: Miaozhen Yu.
- Source: *Optimal mean comparisons in ordinary Shellsort* by Miaozhen Yu.
- Project repository: [EternalYMZ/Optimal-mean-comparisons-in-Shellsort](https://github.com/EternalYMZ/Optimal-mean-comparisons-in-Shellsort), at commit [b173885b](https://github.com/EternalYMZ/Optimal-mean-comparisons-in-Shellsort/tree/b173885b5e49fb74afd4eed879729a35ada4a053).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 68P10, 68Q25.
- In Lean Pool: [LeanPool/ShellsortMean](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ShellsortMean), from the card [LeanPool/projects/shellsort-mean-comparisons.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/shellsort-mean-comparisons.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/shellsort-mean-comparisons.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/shellsort-mean-comparisons.yaml)
- [Lean Pool at bb99e52c: LeanPool/ShellsortMean](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ShellsortMean)
