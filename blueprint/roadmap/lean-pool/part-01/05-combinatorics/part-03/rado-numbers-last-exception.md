---
declaration: theorem
origin: cited
lean: RadoNu.rado_last_exception, RadoNu.rado_eq_LB, RadoNu.not_forced_cstar, RadoNu.nu_iff, RadoNu.nu_5_eq_66
statement: formalized
proof: formalized
---

# The Last Exception for Two-Colour Rado Numbers

> Determines the exact last exception c\*(k) for the 2-colour Rado number R(c, k) of x + y + c = kz for every integer k ≥ 3, where c\*(k) = k(k² + k − 4)/2 for odd k and k(k² − 2)/2 for even k. Proves both halves unconditionally in pure core Lean 4 (zero Mathlib imports): (1) an original reflection proof (x ↦ N + 1 − x) combined with Martinelli and Schaal's lower bound showing R(c, k) = LB(c, k) for every valid c > c\*(k) (k odd or c even), and (2) an explicit boundary colouring avoiding monochromatic solutions on [1, LB(c\*(k), k)]. Finite existence of R(c\*(k), k) is left outside the formalization. As a corollary, the project characterizes the cutoff ν(k) and settles the Kim–Song–Hwang (2023) conjecture ν(5) = 66.

*Quoted from the card [LeanPool/projects/rado-numbers-last-exception.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rado-numbers-last-exception.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RadoNu.rado_last_exception`](https://leanpool.github.io/lean-pool/LeanPool/RadoNumbersLastException/UpperHalf.html#RadoNu.rado_last_exception) (theorem; a main declaration), declared in [LeanPool/RadoNumbersLastException/UpperHalf.lean, line 904](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException/UpperHalf.lean#L904): “For every k ≥ 3, (1) for every valid c > c\*(k) (meaning k is odd or c is even), every 2-colouring of [1, LB(c, k)] has a monochromatic solution of x + y + c = kz while some 2-colouring of [1, LB(c, k) − 1] has none, and (2) some 2-colouring of [1, LB(c\*(k), k)] has no monochromatic solution of x + y + c\*(k) = kz. Finite existence of R(c\*(k), k) is left outside the formalization.”
- [`RadoNu.rado_eq_LB`](https://leanpool.github.io/lean-pool/LeanPool/RadoNumbersLastException/UpperHalf.html#RadoNu.rado_eq_LB) (theorem; a main declaration), declared in [LeanPool/RadoNumbersLastException/UpperHalf.lean, line 876](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException/UpperHalf.lean#L876): “For every k ≥ 3 and every valid c > c\*(k), the 2-colour Rado number R(c, k) of x + y + c = kz equals the Martinelli–Schaal lower bound LB(c, k).”
- [`RadoNu.not_forced_cstar`](https://leanpool.github.io/lean-pool/LeanPool/RadoNumbersLastException/UpperHalf.html#RadoNu.not_forced_cstar) (theorem; a main declaration), declared in [LeanPool/RadoNumbersLastException/UpperHalf.lean, line 882](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException/UpperHalf.lean#L882): “For every k ≥ 3, [1, LB(c\*(k), k)] is not forced for x + y + c\*(k) = kz, i.e., there exists a 2-colouring of [1, LB(c\*(k), k)] avoiding monochromatic solutions.”
- [`RadoNu.nu_iff`](https://leanpool.github.io/lean-pool/LeanPool/RadoNumbersLastException/UpperHalf.html#RadoNu.nu_iff) (theorem; a main declaration), declared in [LeanPool/RadoNumbersLastException/UpperHalf.lean, line 939](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException/UpperHalf.lean#L939): “For every k ≥ 3 and natural number v, R(c, k) = LB(c, k) holds for all valid c ≥ v if and only if c\*(k) < v; hence the least integer cutoff is c\*(k) + 1 and the least valid cutoff ν(k) is c\*(k) + 1 for odd k and c\*(k) + 2 for even k.”
- [`RadoNu.nu_5_eq_66`](https://leanpool.github.io/lean-pool/LeanPool/RadoNumbersLastException/UpperHalf.html#RadoNu.nu_5_eq_66) (theorem; a main declaration), declared in [LeanPool/RadoNumbersLastException/UpperHalf.lean, line 964](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException/UpperHalf.lean#L964): “Settles the Kim–Song–Hwang (2023) conjecture ν(5) = 66: R(c, 5) = LB(c, 5) for all c ≥ 66, and fails for c = 65.”
- [`RadoNu.rado_last_exception_rado`](https://leanpool.github.io/lean-pool/LeanPool/RadoNumbersLastException/UpperHalf.html#RadoNu.rado_last_exception_rado) (theorem), declared in [LeanPool/RadoNumbersLastException/UpperHalf.lean, line 926](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException/UpperHalf.lean#L926): “Restates the both-halves characterization using IsRado and Forced, including that any Rado number R satisfying IsRado (c\*(k)) k R must strictly exceed LB(c\*(k), k).”
- [`RadoNu.nu_small_values`](https://leanpool.github.io/lean-pool/LeanPool/RadoNumbersLastException/UpperHalf.html#RadoNu.nu_small_values) (theorem), declared in [LeanPool/RadoNumbersLastException/UpperHalf.lean, line 953](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException/UpperHalf.lean#L953): “Verifies by kernel decide that the least valid cutoffs ν(k) for k = 3..10 equal 13, 30, 66, 104, 183, 250, 388, and 492.”

## Project

- Authors: Tyler B. Hughes.
- Source: *Two-color Rado number of x + y + c = kz for large c* by Byeong Moon Kim, Byung Chul Song, Woonjae Hwang, [doi:10.1016/j.disc.2023.113597](https://doi.org/10.1016/j.disc.2023.113597), [https://mathdiscoveries.org/results/rado-numbers-last-exception/](https://mathdiscoveries.org/results/rado-numbers-last-exception/).
- Project repository: [mathdiscoveries/rado-numbers-last-exception](https://github.com/mathdiscoveries/rado-numbers-last-exception), at commit [8c0c3e40](https://github.com/mathdiscoveries/rado-numbers-last-exception/tree/8c0c3e402d081b1315530ff3e0e509c5589a9de3).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05D10, 11B75.
- In Lean Pool: [LeanPool/RadoNumbersLastException](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException), from the card [LeanPool/projects/rado-numbers-last-exception.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rado-numbers-last-exception.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/rado-numbers-last-exception.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rado-numbers-last-exception.yaml)
- [Lean Pool at bb99e52c: LeanPool/RadoNumbersLastException](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RadoNumbersLastException)
