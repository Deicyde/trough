---
declaration: section
origin: cited
lean: Nat.Partition.card_count_ge, Nat.Partition.card_monotone, Nat.Partition.mul_card_eq_sum, Nat.Partition.exists_exp_div_pow_le_card, Nat.Partition.card_le_exp, Nat.Partition.succ_le_two_mul_card, Nat.Partition.exists_logb_card_bounds
statement: formalized
proof: formalized
---

# Bounds on the partition function

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html).

## Bijection removing $k$ copies of a part from partitions

Removing `k` copies of the positive part `v` gives a bijection from partitions of `E`
containing at least `k` copies of `v` to partitions of `E - k * v`.

Formalized by `Nat.Partition.card_count_ge`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Counting.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Counting.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html#card-count-ge).

## Monotonicity of the partition function

The number of integer partitions is monotone in the integer being partitioned.

Formalized by `Nat.Partition.card_monotone`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Counting.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Counting.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html#card-monotone).

## Sum-of-parts recurrence for the partition function

A recurrence obtained by summing all parts of all partitions of `E`, first by partition
and then by part value and multiplicity threshold.

Formalized by `Nat.Partition.mul_card_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Counting.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Counting.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html#mul-card-eq-sum).

## Exponential lower bound for the partition function

The number of partitions of `n` is at least
`H * exp (pi * sqrt (2 / 3) * sqrt n) / n ^ B` for some `H > 0` and natural `B`, when `n ≥ 1`.

Formalized by `Nat.Partition.exists_exp_div_pow_le_card`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/ExponentialLowerBound.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/ExponentialLowerBound.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html#exists-exp-div-pow-le-card).

## Exponential upper bound for the partition function

The number of integer partitions of `n` is at most
`exp (π * sqrt (2 / 3) * sqrt n)`.

Formalized by `Nat.Partition.card_le_exp`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/ExponentialUpperBound.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/ExponentialUpperBound.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html#card-le-exp).

## Linear lower bound for the partition function

The number of partitions of `n` is at least `(n + 1) / 2`.

Formalized by `Nat.Partition.succ_le_two_mul_card`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/LinearLowerBound.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/LinearLowerBound.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html#succ-le-two-mul-card).

## Logarithmic bounds for the partition function

There are constants `B` and `C` such that the base-two logarithm of the number of integer
partitions of `n` differs from its leading square-root term by at most a logarithmic lower-order
term below and a constant above.

Formalized by `Nat.Partition.exists_logb_card_bounds`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/LogBounds.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/LogBounds.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html#exists-logb-card-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounds on the partition function](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/bounds-on-the-partition-function)
