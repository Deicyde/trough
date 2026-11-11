---
declaration: section
origin: cited
lean: NoncrossingPartition.isNoncrossing_bot, NoncrossingPartition.isNoncrossing_top, NoncrossingPartition.discrete, NoncrossingPartition.indiscrete, NoncrossingPartition.block_discrete, NoncrossingPartition.block_indiscrete, NoncrossingPartition.discrete_parts, NoncrossingPartition.indiscrete_parts_zero
statement: formalized
proof: formalized
---

# Extremal noncrossing partitions: discrete and indiscrete

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html).

## The discrete partition is noncrossing

For every natural number $n$, the discrete
partition of $\{0, \dots, n-1\}$, whose blocks are the singletons, is noncrossing.

Formalized by `NoncrossingPartition.isNoncrossing_bot`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#is-noncrossing-bot).

## The indiscrete partition is noncrossing

For every natural number $n$, the indiscrete
partition of $\{0, \dots, n-1\}$, the coarsest partition of this set, is noncrossing.

Formalized by `NoncrossingPartition.isNoncrossing_top`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#is-noncrossing-top).

## Discrete noncrossing partition

For a natural number $n$, the discrete noncrossing
partition of $\{0, \dots, n-1\}$ is the finest partition of this set, whose blocks are the
singletons $\{a\}$ for $a \in \{0, \dots, n-1\}$; it is noncrossing.

Formalized by `NoncrossingPartition.discrete`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#discrete).

## The indiscrete noncrossing partition

For a natural number $n$, the indiscrete noncrossing
partition of $\{0, \dots, n-1\}$ is the coarsest partition of this set: its only block is the whole
set when $n > 0$, and it has no blocks when $n = 0$. It is noncrossing.

Formalized by `NoncrossingPartition.indiscrete`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#indiscrete).

## The block of a point in the discrete noncrossing partition

For every natural number
$n$ and every $a \in \{0, \dots, n-1\}$, the block containing $a$ in the discrete noncrossing
partition of $\{0, \dots, n-1\}$ is the singleton $\{a\}$.

Formalized by `NoncrossingPartition.block_discrete`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#block-discrete).

## The block of a point in the indiscrete noncrossing partition

For every natural number
$n$ and every $a \in \{0, \dots, n-1\}$, the block containing $a$ in the indiscrete noncrossing
partition of $\{0, \dots, n-1\}$ is the whole set $\{0, \dots, n-1\}$.

For $n = 0$ there is no such $a$, so the statement is vacuous.

Formalized by `NoncrossingPartition.block_indiscrete`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#block-indiscrete).

## The discrete noncrossing partition consists of the singletons

For every natural number
$n$, the set of blocks of the discrete noncrossing partition of $\{0, \dots, n-1\}$ is exactly
the set of singletons $\{a\}$ with $a \in \{0, \dots, n-1\}$.

Formalized by `NoncrossingPartition.discrete_parts`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#discrete-parts).

## The indiscrete partition of the empty set has no blocks

For $n = 0$, the set of blocks
of the indiscrete noncrossing partition of $\{0, \dots, n-1\}$, the empty set, is empty.

Formalized by `NoncrossingPartition.indiscrete_parts_zero`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#indiscrete-parts-zero).

## The discrete partition of the empty set has no blocks

For $n = 0$, the discrete
noncrossing partition of the empty set $\{0, \dots, n-1\}$ has no blocks: its set of blocks is
empty.

Formalized by `NoncrossingPartition.discrete_parts_zero`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#discrete-parts-zero).

## The indiscrete partition of a nonempty set has a single block

For a natural number $n$
with $0 < n$, the set of blocks of the indiscrete noncrossing partition of $\{0, \dots, n-1\}$ is
$\{\{0, \dots, n-1\}\}$: its only block is the whole set.

Formalized by `NoncrossingPartition.indiscrete_parts_pos`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#indiscrete-parts-pos).

## Characterization of the discrete noncrossing partition

Let $n$ be a natural number. A
noncrossing partition $P$ of $\{0, \dots, n-1\}$ equals the discrete noncrossing partition if
and only if $P$, viewed as a set partition, is the finest partition of $\{0, \dots, n-1\}$.

Formalized by `NoncrossingPartition.eq_discrete_iff_val_eq_bot`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#eq-discrete-iff-val-eq-bot).

## Characterization of the indiscrete noncrossing partition

Let $n$ be a natural number.
A noncrossing partition $P$ of $\{0, \dots, n-1\}$ equals the indiscrete noncrossing partition
if and only if $P$, viewed as a set partition, is the coarsest partition of
$\{0, \dots, n-1\}$.

Formalized by `NoncrossingPartition.eq_indiscrete_iff_val_eq_top`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#eq-indiscrete-iff-val-eq-top).

## A partition whose blocks are all the whole set is indiscrete

Let $n$ be a natural number
and let $P$ be a noncrossing partition of $\{0, \dots, n-1\}$. If for every
$a \in \{0, \dots, n-1\}$ the block of $P$ containing $a$ is the whole set $\{0, \dots, n-1\}$,
then $P$ is the indiscrete noncrossing partition.

Formalized by `NoncrossingPartition.eq_indiscrete_of_forall_block_eq_univ`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#eq-indiscrete-of-forall-block-eq-univ).

## The empty set has a unique noncrossing partition

For $n = 0$, every noncrossing partition
of $\{0, \dots, n-1\}$, the empty set, equals the indiscrete noncrossing partition of this set.

Formalized by `NoncrossingPartition.eq_indiscrete_zero`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#eq-indiscrete-zero).

## Discrete and indiscrete partitions agree on the empty set

For $n = 0$, the discrete and
the indiscrete noncrossing partitions of the empty set $\{0, \dots, n-1\}$ are equal.

Formalized by `NoncrossingPartition.discrete_zero_eq_indiscrete_zero`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#discrete-zero-eq-indiscrete-zero).

## The only noncrossing partition of the empty set is the discrete one

For $n = 0$, every
noncrossing partition of the empty set $\{0, \dots, n-1\}$ equals the discrete noncrossing
partition.

Formalized by `NoncrossingPartition.eq_discrete_zero`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/NoncrossingPartition/Operations.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html#eq-discrete-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extremal noncrossing partitions: discrete and indiscrete](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/set-partitions/noncrossing-partitions/extremal-noncrossing-partitions-discrete-and-ind)
