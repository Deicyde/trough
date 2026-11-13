---
declaration: section
origin: cited
lean: MetaMathlibExt.IsBasicSetPartition, MetaMathlibExt.CallanSequence, MetaMathlibExt.setPartition_twoRise_ordinaryGeneratingFunction, MetaMathlibExt.IsMergingFreePartition, MetaMathlibExt.IsOrderedSetPartition, MetaMathlibExt.restricted_growth_word_monomial_generating_function
statement: formalized
proof: formalized
---

# Set partitions: its own results

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html).

Partitions of a finite set into blocks: finite partition API, ordered and cyclic set partitions, restricted-growth words, peaks and rises, noncrossing partitions, merging-free and marriageable-singles partitions, genus of a partition, and linear chord diagrams and hypermonopoles.

## Basic set partition

A partition $P$ of $\{1, \dots, n\}$ is basic when its blocks can
 be listed without repetition as $B_1, \dots, B_k$ with $|B_1| \ge |B_2| \ge \dots \ge |B_k|$
 so that $B_1 \cup \dots \cup B_i = \{1, \dots, |B_1| + \dots + |B_i|\}$ for every $i$ with
 $1 \le i \le k$.

Formalized by `MetaMathlibExt.IsBasicSetPartition`, a definition declared in [MathlibExt/Combinatorics/Finpartition/BasicSetPartition.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Finpartition/BasicSetPartition.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html#is-basic-set-partition).

## Callan sequences

Let $k$ and $n$ be natural numbers. Form the blue base set
$\{1, \dots, k\} \cup \{\star_B\}$ and the red base set $\{1, \dots, n\} \cup \{\star_R\}$,
where the blue star $\star_B$ and the red star $\star_R$ are new elements. An (unbarred)
Callan sequence of size $k \times n$ consists of a natural number $m \le n$ together with a
sequence of $m + 1$ pairs $(B_0, R_0), \dots, (B_m, R_m)$ such that the blue blocks
$B_0, \dots, B_m$ are nonempty subsets of the blue base set and every element of the blue base
set lies in exactly one of them, the red blocks $R_0, \dots, R_m$ are nonempty subsets of the
red base set and every element of the red base set lies in exactly one of them, and the last
pair contains both stars: $\star_B \in B_m$ and $\star_R \in R_m$.

Formalized by `MetaMathlibExt.CallanSequence`, a structure declared in [MathlibExt/Combinatorics/Enumerative/CallanSequence.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CallanSequence.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html#callan-sequence).

## Generating function for set partitions by rises

Fix $k \ge 1$. For $n, r \ge 0$ let
$a_{n,r}$ be the number of words $\pi = \pi_1 \cdots \pi_n$ on the alphabet $\{0, \dots, k-1\}$
that use every letter, satisfy the restricted growth condition that each $\pi_i$ is at most the
number of distinct letters among $\pi_1, \dots, \pi_{i-1}$, and have exactly $r$ rises (the
source's $2$-rises), that is, positions $i < n$ with $\pi_i < \pi_{i+1}$. These words encode the
partitions of $[n]$ into $k$ blocks. Then, in the ring $\mathbb{Q}[[x, y]]$ of formal power
series,

$$\sum_{n, r \ge 0} a_{n,r}\, x^n y^r =
\frac{x^k y^{k-1} (1-y)^k}{\prod_{j=1}^{k} \bigl((1 - x + xy)^j - y\bigr)}.$$

## Sources

- Toufik Mansour and Augustine O. Munagi, “Enumeration of Partitions by Long Rises, Levels, and Descents”, Journal of Integer Sequences 12 (2009), Article 09.1.8, Theorem `thrise2`, lines 505-510, <https://cs.uwaterloo.ca/journals/JIS/VOL12/Munagi/munagi15.tex>.

Formalized by `MetaMathlibExt.setPartition_twoRise_ordinaryGeneratingFunction`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SetPartitionsByTwoRises.lean, line 2653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SetPartitionsByTwoRises.lean#L2653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html#set-partition-two-rise-ordinary-generati).

## Merging-free partitions

Let $n$ be a natural number. A finite sequence
$(B_1, \dots, B_m)$ of subsets of $\{0, 1, \dots, n-1\}$ is a merging-free partition when the
sets $B_i$ are nonempty, pairwise disjoint and cover $\{0, 1, \dots, n-1\}$; their minima increase
strictly, $\min B_1 < \min B_2 < \dots < \min B_m$; and $\max B_i > \min B_{i+1}$ for every
$i < m$.

Formalized by `MetaMathlibExt.IsMergingFreePartition`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MergingFreePartition.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MergingFreePartition.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html#is-merging-free-partition).

## Ordered set partitions of a finite set

For a finite set $V$, a list $(B_1, \dots, B_k)$
of finite sets is an ordered set partition (set composition) of $V$ when every block $B_i$ is
nonempty and contained in $V$, the blocks are pairwise disjoint, and
$B_1 \cup \dots \cup B_k = V$.

Equivalently, an ordered set partition of $V$ is a structure of the composite species of lists
of nonempty sets on $V$.

Formalized by `MetaMathlibExt.IsOrderedSetPartition`, a definition declared in [MathlibExt/Combinatorics/Enumerative/OrderedSetPartition.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/OrderedSetPartition.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html#is-ordered-set-partition).

## Restricted-growth word generating function

Fix $k \ge 0$. A word $u_1 u_2 \cdots u_n$
in the letters $1, \dots, k$ is a restricted-growth word if for every $i$, either $u_i = 1$ or
$u_i \le u_j + 1$ for some $j < i$ (so a nonempty such word begins with $1$). For
$d = (d_1, \dots, d_k) \in \mathbb{N}^k$, let $r(d)$ be the number of restricted-growth words in
which each letter $a$ occurs exactly $d_a + 1$ times. Then, in the ring of formal power series
in $x_1, \dots, x_k$ over $\mathbb{Q}$,

$$\sum_{d} r(d)\, x_1^{d_1} \cdots x_k^{d_k} = \prod_{j=1}^{k} (1 - x_1 - \cdots - x_j)^{-1}.$$

Proof: Decompose restricted-growth words by their first letter to obtain a coefficient
recurrence, lift it to multivariate power series, and iterate power-series inverse
cancellation. The combinatorial route follows Ehrenborg, Hedmark, and Hettle, Theorem 1.

## Sources

- Richard Ehrenborg, Dustin Hedmark, and Cyrus Hettle, "A Restricted Growth Word Approach to Partitions with Odd/Even Size Blocks," Journal of Integer Sequences 20 (2017), Article 17.5.5, Theorem 1, lines 190-200, <https://cs.uwaterloo.ca/journals/JIS/VOL20/Ehrenborg/ehren4.tex>.

Formalized by `MetaMathlibExt.restricted_growth_word_monomial_generating_function`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/Partition/RestrictedGrowthWordGeneratingFunction.lean, line 630](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/Partition/RestrictedGrowthWordGeneratingFunction.lean#L630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html#restricted-growth-word-monomial-generati).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Set partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/set-partitions)
