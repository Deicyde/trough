---
declaration: section
origin: cited
lean: MetaMathlibExt.IsIncreasingCyclePerm, MetaMathlibExt.setPartitionGenus, MetaMathlibExt.partitionGenusCount, MetaMathlibExt.isIncreasingCyclePerm_one, MetaMathlibExt.setPartitionGenus_one, MetaMathlibExt.isIncreasingCyclePerm_finRotate, MetaMathlibExt.setPartitionGenus_finRotate, MetaMathlibExt.pairing_genus_generatingFunction
statement: formalized
---

# Genus of a set partition

10 results, 7 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html).

## Increasing-cycle permutation

A permutation $\tau$ of $\{0, \dots, n-1\}$ is an
increasing-cycle permutation when, for all $x$ and $y$ in $\{0, \dots, n-1\}$ such that
$\tau(x) \le x$ and $y$ lies in the same cycle of $\tau$ as $x$, we have $\tau(x) \le y$. That
is, whenever $\tau(x) \le x$, the value $\tau(x)$ is the least element of the cycle of $x$;
equivalently, each cycle of $\tau$ runs through its elements in increasing order and returns from
the largest to the least.

Set partitions of $\{0, \dots, n-1\}$ correspond bijectively to increasing-cycle permutations,
the blocks being the cycles (fixed points give singleton blocks), and partitions are counted
through this encoding.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Section 2.4 (the permutation `τ` whose cycles are the parts, with their elements in increasing order).

Formalized by `MetaMathlibExt.IsIncreasingCyclePerm`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#is-increasing-cycle-perm).

## Genus of a set partition

Let $\sigma$ be the cyclic permutation $i \mapsto i + 1 \pmod n$
of $\{0, \dots, n-1\}$. For a permutation $\tau$ of $\{0, \dots, n-1\}$, thought of as encoding the
set partition whose blocks are its cycles, let $|\alpha|$ be the number of cycles of $\tau$ and $c$
the number of cycles of $\sigma \circ \tau^{-1}$, fixed points counted as cycles in both. The genus
of $\tau$ is the integer part of $\frac{1}{2} \max(0,\ n + 1 - |\alpha| - c)$.

For $n \ge 1$ the number $n + 1 - |\alpha| - c$ is nonnegative and even, so the genus is the
number $g$ with $-2g = |\alpha| - 1 - n + c$; for $n = 0$ the genus is $0$.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Section 2.4, equation (genus).

Formalized by `MetaMathlibExt.setPartitionGenus`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#set-partition-genus).

## Number of set partitions of given type and genus

For natural numbers $n$ and $g$ and a
multiset $\alpha$ of natural numbers, $C_{n,[\alpha]}^{(g)}$ is the number of increasing-cycle
permutations $\tau$ of $\{0, \dots, n-1\}$ whose multiset of cycle lengths, fixed points counted
as cycles of length $1$, is $\alpha$ and whose genus is $g$.

Through the encoding of set partitions by increasing-cycle permutations, this is the number of
set partitions of $\{0, \dots, n-1\}$ of type $[\alpha]$ (multiset of block sizes $\alpha$) and
genus $g$.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Section 2.4 (the numbers `C_{n,[α]}^{(g)}`).

Formalized by `MetaMathlibExt.partitionGenusCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#partition-genus-count).

## The identity is an increasing-cycle permutation

For every natural number $n$, the
identity permutation of $\{0, \dots, n-1\}$ is an increasing-cycle permutation.

Its cycles are the singletons, so it encodes the partition of $\{0, \dots, n-1\}$ into
singletons.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Section 2.4.

Formalized by `MetaMathlibExt.isIncreasingCyclePerm_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#is-increasing-cycle-perm-one).

## The partition into singletons has genus zero

For every natural number $n$, the genus of
the identity permutation of $\{0, \dots, n-1\}$ is $0$; the identity encodes the partition of
$\{0, \dots, n-1\}$ into singletons.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Section 2.4.

Formalized by `MetaMathlibExt.setPartitionGenus_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#set-partition-genus-one).

## The cyclic rotation is an increasing-cycle permutation

For every natural number $n$,
the cyclic permutation $i \mapsto i + 1 \pmod n$ of $\{0, \dots, n-1\}$ is an increasing-cycle
permutation.

For $n \ge 1$ its only cycle is all of $\{0, \dots, n-1\}$, so it encodes the set partition with a
single block.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Section 2.4.

Formalized by `MetaMathlibExt.isIncreasingCyclePerm_finRotate`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#is-increasing-cycle-perm-fin-rotate).

## The one-block partition has genus zero

For every natural number $n$, the genus of the
cyclic permutation $i \mapsto i + 1 \pmod n$ of $\{0, \dots, n-1\}$ is $0$.

For $n \ge 1$ its only cycle is all of $\{0, \dots, n-1\}$, so this says that the partition with a
single block has genus $0$.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Section 2.4 ("one-part partitions (`k = 1`) necessarily have genus 0").

Formalized by `MetaMathlibExt.setPartitionGenus_finRotate`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#set-partition-genus-fin-rotate).

## Genus generating function of pairings

Let $g \ge 1$, and for $k \ge 0$ let
$C_{2k,[2^k]}^{(g)}$ be the number of genus-$g$ set partitions of $\{0, \dots, 2k-1\}$ into $k$
blocks of size $2$. There is a polynomial $Q^{(g)}$ with rational coefficients, of degree
$g - 1$, with $Q^{(g)}(0) = \frac{(4g)!}{2^{2g}\,(2g+1)!}$, such that, as formal power series
in $u$ over $\mathbb{Q}$,

$$\sum_{k \ge 0} C_{2k,[2^k]}^{(g)}\, u^k = u^{2g}\, Q^{(g)}(u)\, (1 - 4u)^{-(6g-1)/2}.$$

Here $(1 - 4u)^{-(6g-1)/2}$ is the binomial series $(1 + X)^r = \sum_{m \ge 0} \binom{r}{m} X^m$
with $r = -(6g-1)/2$, evaluated at $X = -4u$.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Proposition 11 (`jis-2024-24.2.6-prop-11`).

Stated but not proved: `MetaMathlibExt.pairing_genus_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#pairing-genus-generating-function).

## Genus of two-block partitions

Let $\sigma$ be the cyclic permutation
$i \mapsto i + 1 \pmod n$ of $\{0, \dots, n-1\}$, and let $\tau$ be an increasing-cycle permutation
of $\{0, \dots, n-1\}$ with exactly two cycles, fixed points counted as cycles (so $\tau$ encodes a
set partition into two blocks). Then $\sigma \circ \tau^{-1}$ has exactly one cycle of length at
least $2$. Moreover, for every $x_0$ in $\{0, \dots, n-1\}$, if $B$ is the cycle of $\tau$
containing $x_0$ and $s$ is the number of elements of $B$ fixed by $\sigma \circ \tau^{-1}$, then
the genus $g$ of $\tau$ satisfies $g + 1 + s = |B|$.

Taking $x_0$ in each of the two blocks, of sizes $p$ and $n - p$, and writing $s_1$ and $s_2$ for
the corresponding values of $s$, gives $g = p - s_1 - 1 = (n - p) - s_2 - 1$.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Lemma 13 (`jis-2024-24.2.6-lem-13`).

Stated but not proved: `MetaMathlibExt.twoBlock_oneFace_and_genus` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#two-block-one-face-and-genus).

## Genus count of two-block partitions

Let $n$, $p$ and $g$ be natural numbers with
$2 \le p < n$. The number $C_{n,[p,\,n-p]}^{(g)}$ of genus-$g$ set partitions of
$\{0, \dots, n-1\}$ into two blocks of sizes $p$ and $n - p$ equals

$$\frac{n}{g+1} \binom{p-1}{g} \binom{n-p-1}{g}$$

when $n \ne 2p$, and half of this number when $n = 2p$.

## Sources

- Coquereaux and Zuber, *Counting Partitions by Genus: a Compendium of Results*, Journal of Integer Sequences 27 (2024), Article 24.2.6, Proposition 14 (`jis-2024-24.2.6-prop-14`).

Stated but not proved: `MetaMathlibExt.partitionGenusCount_twoBlocks` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PartitionGenusWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html#partition-genus-count-two-blocks).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Genus of a set partition](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/set-partitions/genus-of-a-set-partition)
