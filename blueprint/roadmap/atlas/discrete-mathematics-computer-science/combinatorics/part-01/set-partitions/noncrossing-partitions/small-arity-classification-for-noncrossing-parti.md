---
declaration: section
origin: cited
lean: NoncrossingPartition.eq_indiscrete_one, NoncrossingPartition.discrete_two_ne_indiscrete_two, NoncrossingPartition.eq_discrete_or_indiscrete_two, NoncrossingPartition.card_zero, NoncrossingPartition.card_one, NoncrossingPartition.card_two, NoncrossingPartition.properTwoEquiv, NoncrossingPartition.twoBlockPartition
statement: formalized
proof: formalized
---

# Small-arity classification for noncrossing partitions

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html).

## Noncrossing partitions of one point are indiscrete

Every noncrossing partition of the
one-point set $\{0\}$ equals the indiscrete noncrossing partition of $\{0\}$.

Formalized by `NoncrossingPartition.eq_indiscrete_one`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#eq-indiscrete-one).

## The discrete and indiscrete partitions of a two-element set differ

The discrete
noncrossing partition of $\{0, 1\}$ is not equal to the indiscrete noncrossing partition of
$\{0, 1\}$.

Formalized by `NoncrossingPartition.discrete_two_ne_indiscrete_two`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#discrete-two-ne-indiscrete-two).

## Classification of noncrossing partitions of a two-element set

Every noncrossing partition
of $\{0, 1\}$ is either the discrete or the indiscrete noncrossing partition of $\{0, 1\}$.

Formalized by `NoncrossingPartition.eq_discrete_or_indiscrete_two`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#eq-discrete-or-indiscrete-two).

## Noncrossing partitions of the empty set

There is exactly one noncrossing partition of the
empty set, that is, of $\{0, \dots, n-1\}$ for $n = 0$.

Formalized by `NoncrossingPartition.card_zero`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#card-zero).

## Noncrossing partitions of a one-element set

There is exactly one noncrossing partition
of $\{0\}$.

Formalized by `NoncrossingPartition.card_one`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#card-one).

## Noncrossing partitions of a two-element set

There are exactly two noncrossing partitions
of $\{0, 1\}$.

Formalized by `NoncrossingPartition.card_two`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#card-two).

## The proper noncrossing partition of two points

Call a noncrossing partition of $\{0, 1\}$
proper if it is not the indiscrete one. This is the bijection from a one-element set onto the set
of proper noncrossing partitions of $\{0, 1\}$, sending its element to the discrete noncrossing
partition; in particular the discrete partition is the only proper one.

Formalized by `NoncrossingPartition.properTwoEquiv`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#proper-two-equiv).

## Two-block partition of three points

For $a \in \{0, 1, 2\}$, this is the noncrossing
partition of $\{0, 1, 2\}$ whose blocks are $\{a\}$ and $\{0, 1, 2\} \setminus \{a\}$.

Formalized by `NoncrossingPartition.twoBlockPartition`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#two-block-partition).

## Noncrossing partitions of three points have one, two or three blocks

Every noncrossing
partition of $\{0, 1, 2\}$ has one, two, or three blocks.

Formalized by `NoncrossingPartition.three_card_one_two_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#three-card-one-two-three).

## A noncrossing partition of three points with one block is indiscrete

If a noncrossing
partition $P$ of $\{0, 1, 2\}$ has exactly one block, then $P$ is the indiscrete noncrossing
partition of $\{0, 1, 2\}$.

Formalized by `NoncrossingPartition.eq_indiscrete_of_card_one_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#eq-indiscrete-of-card-one-three).

## A noncrossing partition of three points with three blocks is discrete

If a noncrossing
partition $P$ of $\{0, 1, 2\}$ has exactly three blocks, then $P$ is the discrete noncrossing
partition of $\{0, 1, 2\}$.

Formalized by `NoncrossingPartition.eq_discrete_of_card_three_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#eq-discrete-of-card-three-three).

## Classification of noncrossing partitions of a three-element set

Every noncrossing
partition $P$ of $\{0, 1, 2\}$ is the discrete noncrossing partition of $\{0, 1, 2\}$, the
indiscrete noncrossing partition of $\{0, 1, 2\}$, or, for some $a \in \{0, 1, 2\}$, the
two-block noncrossing partition whose blocks are $\{a\}$ and $\{0, 1, 2\} \setminus \{a\}$.

Formalized by `NoncrossingPartition.eq_discrete_or_indiscrete_or_twoBlock_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#eq-discrete-or-indiscrete-or-two-block-t).

## The discrete and indiscrete partitions of a three-element set differ

The discrete
noncrossing partition of $\{0, 1, 2\}$ is not equal to the indiscrete noncrossing partition of
$\{0, 1, 2\}$.

Formalized by `NoncrossingPartition.discrete_three_ne_indiscrete_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#discrete-three-ne-indiscrete-three).

## The two-block partitions of three points are not indiscrete

For every
$a \in \{0, 1, 2\}$, the noncrossing partition of $\{0, 1, 2\}$ with blocks $\{a\}$ and
$\{0, 1, 2\} \setminus \{a\}$ is different from the indiscrete noncrossing partition of
$\{0, 1, 2\}$.

Formalized by `NoncrossingPartition.twoBlockPartition_ne_indiscrete_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#two-block-partition-ne-indiscrete-three).

## Enumerating the two-block noncrossing partitions of three points

The map sending
$a \in \{0, 1, 2\}$ to the partition of $\{0, 1, 2\}$ with blocks $\{a\}$ and
$\{0, 1, 2\} \setminus \{a\}$ is a bijection from $\{0, 1, 2\}$ onto the set of noncrossing
partitions of $\{0, 1, 2\}$ with exactly two blocks.

Formalized by `NoncrossingPartition.twoBlockEquiv`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#two-block-equiv).

## Enumerating the proper noncrossing partitions of three points

Call a noncrossing
partition of $\{0, 1, 2\}$ proper if it is not the indiscrete one. Adjoin an extra element $\ast$
to $\{0, 1, 2\}$; this is the bijection from $\{\ast, 0, 1, 2\}$ onto the set of proper
noncrossing partitions of $\{0, 1, 2\}$ that sends $\ast$ to the discrete noncrossing partition
and each $a \in \{0, 1, 2\}$ to the noncrossing partition with blocks $\{a\}$ and
$\{0, 1, 2\} \setminus \{a\}$.

Formalized by `NoncrossingPartition.properThreeEquiv`, a definition declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#proper-three-equiv).

## Noncrossing partitions of a three-element set

There are exactly five noncrossing
partitions of $\{0, 1, 2\}$.

Formalized by `NoncrossingPartition.card_three`, a theorem declared in [MathlibExt/Combinatorics/NoncrossingPartition/Small.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/NoncrossingPartition/Small.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html#card-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Small-arity classification for noncrossing partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/set-partitions/noncrossing-partitions/small-arity-classification-for-noncrossing-parti)
