---
declaration: section
origin: cited
lean: Nat.Overpartition, Nat.Overpartition.IsOverlined, Nat.Overpartition.isOverlined_iff, Nat.Overpartition.isOverlined_mem_parts, Nat.Overpartition.isOverlined_pos, Nat.Overpartition.ofPartition, Nat.Overpartition.ofPartition_toPartition, Nat.Overpartition.ofPartition_overlines
statement: formalized
proof: formalized
---

# Overpartitions

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html).

## Overpartition

## Overpartition

An overpartition of a natural number $n$ consists of a partition $p$ of $n$
together with a finite set of overlined part sizes, each of which occurs as a part of $p$.

Formalized by `Nat.Overpartition`, a structure declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#overpartition).

## Overlined part size

A natural number $a$ is overlined in an overpartition $O$ of $n$
when $a$ belongs to the set of overlined part sizes of $O$.

Formalized by `Nat.Overpartition.IsOverlined`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#is-overlined).

## Characterization of overlined sizes

For an overpartition $O$ of $n$ and a natural
number $a$, $a$ is overlined in $O$ if and only if $a$ belongs to the set of overlined part
sizes of $O$.

Formalized by `Nat.Overpartition.isOverlined_iff`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#is-overlined-iff).

## Overlined sizes are parts

If $a$ is overlined in an overpartition $O$ of $n$, then $a$
is a part of the underlying partition of $O$.

Formalized by `Nat.Overpartition.isOverlined_mem_parts`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#is-overlined-mem-parts).

## Overlined sizes are positive

If $a$ is overlined in an overpartition $O$ of $n$, then
$a > 0$.

Formalized by `Nat.Overpartition.isOverlined_pos`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#is-overlined-pos).

## The overpartition attached to a partition

For a partition $p$ of a natural number $n$, the
overpartition of $n$ attached to $p$ has underlying partition $p$ and no overlined part sizes.

Formalized by `Nat.Overpartition.ofPartition`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#of-partition).

## The underlying partition of the overpartition attached to a partition

For every partition
$p$ of a natural number $n$, the underlying partition of the overpartition of $n$ attached to $p$
(underlying partition $p$, no part size overlined) is $p$.

Formalized by `Nat.Overpartition.ofPartition_toPartition`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#of-partition-to-partition).

## The overpartition attached to a partition has no overlined sizes

For every partition
$p$ of a natural number $n$, the overpartition of $n$ attached to $p$ (underlying partition $p$,
no part size overlined) has an empty set of overlined part sizes.

Formalized by `Nat.Overpartition.ofPartition_overlines`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#of-partition-overlines).

## No overlines in a plain partition

For every partition $p$ of $n$ and every natural
number $a$, $a$ is not overlined in the overpartition whose underlying partition is $p$ and
whose set of overlined part sizes is empty.

Formalized by `Nat.Overpartition.not_isOverlined_ofPartition`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#not-is-overlined-of-partition).

## Fully overlined overpartition

For a partition $p$ of $n$, the fully overlined
overpartition of $p$ is the overpartition of $n$ whose underlying partition is $p$ and whose
set of overlined part sizes is the set of all distinct parts of $p$.

Formalized by `Nat.Overpartition.full`, a definition declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#full).

## Underlying partition of the fully overlined overpartition

For every partition $p$ of
$n$, the underlying partition of the fully overlined overpartition of $p$ is $p$.

Formalized by `Nat.Overpartition.full_toPartition`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#full-to-partition).

## Overlined sizes of the fully overlined overpartition

For every partition $p$ of $n$,
the set of overlined part sizes of the fully overlined overpartition of $p$ is the set of
distinct parts of $p$.

Formalized by `Nat.Overpartition.full_overlines`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#full-overlines).

## Overlined sizes in the fully overlined overpartition

For every partition $p$ of $n$ and
every natural number $a$, $a$ is overlined in the fully overlined overpartition of $p$ if and
only if $a$ is a part of $p$.

Formalized by `Nat.Overpartition.isOverlined_full`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#is-overlined-full).

## Overpartitions of zero have no overlined sizes

Every overpartition of $0$ has no
overlined part sizes.

Formalized by `Nat.Overpartition.overlines_eq_empty_of_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#overlines-eq-empty-of-zero).

## Uniqueness of the overpartition of zero

Any two overpartitions of $0$ are equal.

Formalized by `Nat.Overpartition.eq_of_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/Partition/Overpartition.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html#eq-of-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Overpartitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/overpartitions)
