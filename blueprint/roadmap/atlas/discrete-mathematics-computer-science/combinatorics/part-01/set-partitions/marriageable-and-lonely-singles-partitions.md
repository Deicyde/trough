---
declaration: section
origin: cited
lean: MetaMathlibExt.mergedSameBlock, MetaMathlibExt.mergedHasCrossing, MetaMathlibExt.IsMarriageableSingles, MetaMathlibExt.marriageableSinglesCount, MetaMathlibExt.lonelySinglesCount, MetaMathlibExt.marriageableSinglesCount_of_le_one, MetaMathlibExt.lonelySinglesCount_zero_one, MetaMathlibExt.noncrossingBlockSingletonCount
statement: formalized
---

# Marriageable and lonely singles partitions

27 results, 16 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html).

## Same block after merging two blocks

Let $P$ be a set partition of $\{0, \dots, n-1\}$ and
let $i, j, x, y \in \{0, \dots, n-1\}$. Then $x$ and $y$ lie in the same block after merging the
blocks of $i$ and $j$ if either $x$ and $y$ lie in the same block of $P$, or each of $x$ and $y$
lies in the block of $i$ or in the block of $j$. For singleton blocks $\{i\}$ and $\{j\}$ this
joins them into the block $\{i, j\}$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definition 3 (the partition `π'` obtained by joining `{i}` and `{j}`).

Formalized by `MetaMathlibExt.mergedSameBlock`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#merged-same-block).

## Crossing after merging two blocks

Let $P$ be a set partition of $\{0, \dots, n-1\}$ and
let $i, j \in \{0, \dots, n-1\}$. The partition obtained from $P$ by merging the blocks of $i$ and
$j$ has a crossing if there are $a < b < c < d$ in $\{0, \dots, n-1\}$ such that $a$ and $c$ lie
in one of its blocks and $b$ and $d$ lie in a different one of its blocks.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definitions 2 and 3 (crossing partitions, the partition `π'`).

Formalized by `MetaMathlibExt.mergedHasCrossing`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#merged-has-crossing).

## Marriageable singles partition

A set partition $P$ of $\{0, \dots, n-1\}$ is a
marriageable singles partition if it has two distinct singleton blocks $\{i\}$ and $\{j\}$ such
that the partition obtained from $P$ by joining them into the block $\{i, j\}$ has no crossing.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definition 3.

Formalized by `MetaMathlibExt.IsMarriageableSingles`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#is-marriageable-singles).

## Number of marriageable singles partitions

For $n \ge 0$, $M_n$ is the number of
noncrossing partitions of $\{0, \dots, n-1\}$ that are marriageable singles partitions.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definition 3.

Formalized by `MetaMathlibExt.marriageableSinglesCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#marriageable-singles-count).

## Number of lonely singles partitions

For $n \ge 0$, $L_n$ is the number of lonely singles
partitions of $\{0, \dots, n-1\}$, that is, of noncrossing partitions of $\{0, \dots, n-1\}$ that
are not marriageable singles partitions.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definition 3.

Formalized by `MetaMathlibExt.lonelySinglesCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#lonely-singles-count).

## Small values of the marriageable singles count

For every $n \le 1$, the number of
marriageable singles partitions of $\{0, \dots, n-1\}$ is $M_n = 0$: a marriageable singles
partition needs two distinct points.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Table 1.

Formalized by `MetaMathlibExt.marriageableSinglesCount_of_le_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#marriageable-singles-count-of-le-one).

## Small values of the lonely singles count

The numbers of lonely singles partitions of
$\{0, \dots, n-1\}$ for $n = 0$ and $n = 1$ are $L_0 = 1$ and $L_1 = 1$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Table 1.

Formalized by `MetaMathlibExt.lonelySinglesCount_zero_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#lonely-singles-count-zero-one).

## Noncrossing partitions by number of blocks and of singleton blocks

For natural numbers
$n$, $m$ and $k$, $NC_{n,m,k}$ is the number of noncrossing partitions of $\{0, \dots, n-1\}$
that have exactly $m$ blocks, exactly $k$ of which are singletons.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definition 23.

Formalized by `MetaMathlibExt.noncrossingBlockSingletonCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#noncrossing-block-singleton-count).

## Base value of the noncrossing block and singleton count

Exactly one noncrossing partition
of the empty set has $0$ blocks, $0$ of which are singletons, namely the empty partition; that
is, $NC_{0,0,0} = 1$, where $NC_{n,m,k}$ is the number of noncrossing partitions of
$\{0, \dots, n-1\}$ with $m$ blocks of which $k$ are singletons.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Remark 25.

Formalized by `MetaMathlibExt.noncrossingBlockSingletonCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#noncrossing-block-singleton-count-zero).

## Zero-extended binomial coefficient

For integers $a$ and $b$, the zero-extended binomial
coefficient $\binom{a}{b}$ is the usual binomial coefficient of $a$ and $b$ when $a \ge 0$ and
$b \ge 0$, and $0$ otherwise.

This is the convention under which the paper's formulas "give $0$" in the degenerate cases (for
example $\binom{-1}{0} = 0$ in the count of noncrossing partitions of a one-element set with
one block and no singleton block).

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, proof of Proposition 24 (degenerate cases giving `0`).

Formalized by `MetaMathlibExt.zeroExtendedChoose`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#zero-extended-choose).

## The zero-extended binomial coefficient on natural numbers

Extend the binomial coefficient
$\binom{a}{b}$ to all integers $a$, $b$ by setting it to $0$ when $a < 0$ or $b < 0$. For all
natural numbers $a$ and $b$, this extended binomial coefficient at $a$ and $b$ viewed as integers
equals the usual binomial coefficient $\binom{a}{b}$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, proof of Proposition 24 (degenerate cases giving `0`).

Formalized by `MetaMathlibExt.zeroExtendedChoose_natCast`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#zero-extended-choose-nat-cast).

## The zero-extended binomial coefficient vanishes at $(-1, 0)$

Extend the binomial
coefficient $\binom{a}{b}$ to all integers $a$, $b$ by setting it to $0$ when $a < 0$ or $b < 0$.
Under this convention $\binom{-1}{0} = 0$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, proof of Proposition 24 (degenerate cases giving `0`).

Formalized by `MetaMathlibExt.zeroExtendedChoose_neg_one_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#zero-extended-choose-neg-one-zero).

## Lanes with a common point

The standard road intersection of size $n$ has entries
$E_0, \dots, E_{n-1}$ and exits $X_0, \dots, X_{n-1}$ on a circle, with $E_i$ at position $2i$
and $X_j$ at position $2j + 1$; the lane $E_iX_j$ is the chord from $E_i$ to $X_j$. Two lanes
$E_iX_j$ and $E_{i'}X_{j'}$ have a common point if $i = i'$, or $j = j'$, or exactly one of the
positions $2i'$ and $2j' + 1$ lies strictly between $2i$ and $2j + 1$ (that is, the chords cross).

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definitions 10 and 13 (lanes, noncrossing lanes).

Formalized by `MetaMathlibExt.lanesMeet`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#lanes-meet).

## Maximal set of lanes

In the standard road intersection of size $n$, the lane $E_iX_j$
joins the entry $E_i$ to the exit $X_j$, for $i, j \in \{0, \dots, n-1\}$. Given a set $A$ of
allowed lanes, a set $S$ of lanes is a maximal set of lanes (MSL) among $A$ if $S \subseteq A$,
no two distinct lanes of $S$ have a common point, and every lane of $A$ not in $S$ has a common
point with some lane of $S$. The standard road intersection allows every lane; the restricted one
forbids the U-turns $E_iX_i$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definitions 12 and 13 (restricted standard road intersection, MSL).

Formalized by `MetaMathlibExt.IsMaximalSetOfLanes`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#is-maximal-set-of-lanes).

## Absolute maximal set of lanes

In the standard road intersection of size $n$, the lane
$E_iX_j$ joins the entry $E_i$ to the exit $X_j$, for $i, j \in \{0, \dots, n-1\}$. A set $S$ of
lanes is absolute if it is a maximal set of lanes among all lanes and there are no $i \ne j$ such
that $S$ contains both U-turns $E_iX_i$ and $E_jX_j$ and replacing these two lanes in $S$ by
$E_iX_j$ and $E_jX_i$ gives again a maximal set of lanes among all lanes.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definition 15.

Formalized by `MetaMathlibExt.IsAbsoluteMaximalSetOfLanes`, a definition declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#is-absolute-maximal-set-of-lanes).

## Maximal sets of lanes for an intersection of size two

Write $E_iX_j$ for the lane from the
$i$-th entry to the $j$-th exit. In the standard road intersection of size $2$, in which every lane
is allowed, the maximal sets of lanes are exactly $\{E_1X_1, E_2X_2\}$ and $\{E_1X_2, E_2X_1\}$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Definition 13 (MSL).

Formalized by `MetaMathlibExt.maximalSetsOfLanes_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#maximal-sets-of-lanes-two).

## Noncrossing partitions split into lonely and marriageable singles partitions

For every
$n \ge 0$, the number $C_n$ of noncrossing partitions of $\{0, \dots, n-1\}$ equals $L_n + M_n$,
where $M_n$ is the number of those that are marriageable singles partitions and $L_n$ is the
number of those that are not.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Lemma 6 (`jis-2025-25.1.1-lem-6`).

Stated but not proved: `MetaMathlibExt.card_noncrossingPartition_eq_lonely_add_marriageable` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#card-noncrossing-partition-eq-lonely-add).

## Maximal sets of lanes and noncrossing partitions

For every $n \ge 0$, the maximal sets of
lanes of the standard road intersection of size $n$, in which every lane is allowed, are in
bijection with the noncrossing partitions of $\{0, \dots, n-1\}$, and their number is the Catalan
number $C_n$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Lemma 16 (`jis-2025-25.1.1-lem-16`).

Stated but not proved: `MetaMathlibExt.maximalSetsOfLanes_equiv_noncrossingPartition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#maximal-sets-of-lanes-equiv-noncrossing).

## Nonabsolute maximal sets of lanes are counted by marriageable singles partitions

For
every $n \ge 0$, the number of maximal sets of lanes of the standard road intersection of size $n$
that are not absolute equals $M_n$, the number of noncrossing partitions of $\{0, \dots, n-1\}$
that are marriageable singles partitions.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Corollary 17 (`jis-2025-25.1.1-cor-17`).

Stated but not proved: `MetaMathlibExt.card_nonabsolute_maximalSetsOfLanes` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#card-nonabsolute-maximal-sets-of-lanes).

## Absolute maximal sets of lanes are counted by lonely singles partitions

For every
$n \ge 0$, the number of absolute maximal sets of lanes of the standard road intersection of
size $n$ equals $L_n$, the number of noncrossing partitions of $\{0, \dots, n-1\}$ that are not
marriageable singles partitions.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Corollary 18 (`jis-2025-25.1.1-cor-18`).

Stated but not proved: `MetaMathlibExt.card_absolute_maximalSetsOfLanes` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#card-absolute-maximal-sets-of-lanes).

## Maximal sets of lanes without U-turns are counted by lonely singles partitions

For every
$n \ge 0$, consider the restricted standard road intersection of size $n$, in which the lane
$E_iX_j$ from the entry $E_i$ to the exit $X_j$, for $i, j \in \{0, \dots, n-1\}$, is allowed
exactly when $i \ne j$ (the U-turns $E_iX_i$ are forbidden). The number of maximal sets of lanes
among these allowed lanes equals $L_n$, the number of noncrossing partitions of
$\{0, \dots, n-1\}$ that are not marriageable singles partitions.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Corollary 19 (`jis-2025-25.1.1-cor-19`).

Stated but not proved: `MetaMathlibExt.card_restricted_maximalSetsOfLanes` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#card-restricted-maximal-sets-of-lanes).

## Strict growth of the lonely and marriageable singles counts

$L_n < L_{n+1}$ for every
$n \ge 2$, and $M_n < M_{n+1}$ for every $n \ge 3$, where $M_n$ is the number of noncrossing
partitions of $\{0, \dots, n-1\}$ that are marriageable singles partitions and $L_n$ is the
number of those that are not.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Proposition 20 (`jis-2025-25.1.1-prop-20`).

Stated but not proved: `MetaMathlibExt.lonely_marriageable_strictMono` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#lonely-marriageable-strict-mono).

## The marriageable and lonely singles counts tend to infinity

Let $M_n$ and $L_n$ be the
numbers of noncrossing partitions of $\{0, \dots, n-1\}$ that are marriageable singles partitions
and lonely singles partitions, respectively. Then $M_n \to \infty$ and $L_n \to \infty$ as
$n \to \infty$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Corollary 21 (`jis-2025-25.1.1-cor-21`).

Stated but not proved: `MetaMathlibExt.tendsto_marriageable_lonely_atTop` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#tendsto-marriageable-lonely-at-top).

## Recursive lower bound for marriageable singles partitions

For every $n \ge 0$,
$C_n + 3M_n \le M_{n+2}$, where $C_n$ is the number of noncrossing partitions of
$\{0, \dots, n-1\}$ and $M_n$ is the number of those that are marriageable singles partitions.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Proposition 22 (`jis-2025-25.1.1-prop-22`).

Stated but not proved: `MetaMathlibExt.card_add_three_mul_marriageable_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#card-add-three-mul-marriageable-le).

## Counting noncrossing partitions with no or one singleton block

Write $NC_{n,m,k}$ for the
number of noncrossing partitions of $\{0, \dots, n-1\}$ with $m$ blocks of which $k$ are
singletons, and extend the binomial coefficient $\binom{a}{b}$ to all integers $a$, $b$ by setting
it to $0$ when $a < 0$ or $b < 0$. For all natural numbers $n$ and $m$: if $(n, m) \ne (0, 0)$,
then the following holds in $\mathbb{Q}$, where $1/0$ is taken to be $0$ (the denominator
vanishes only for $m = n + 1$, where $\binom{n}{m} = 0$):

$$NC_{n,m,0} = \frac{1}{n-m+1} \binom{n}{m} \binom{n-m-1}{m-1};$$

and if $(n, m) \ne (1, 1)$, then

$$NC_{n,m,1} = \binom{n}{m-1} \binom{n-m-1}{m-2}.$$

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Proposition 24 (`jis-2025-25.1.1-prop-24`).

Stated but not proved: `MetaMathlibExt.noncrossingBlockSingletonCount_formulas` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#noncrossing-block-singleton-count-formul).

## Lower bound for the number of lonely singles partitions

For every $n \ge 2$, the number
$L_n$ of lonely singles partitions of $\{0, \dots, n-1\}$ satisfies

$$
L_n \ge \sum_{m=1}^{\lfloor n/2 \rfloor} \frac{1}{n-m+1} \binom{n}{m} \binom{n-m-1}{m-1} +
\sum_{m=2}^{\lfloor (n+1)/2 \rfloor} \binom{n}{m-1} \binom{n-m-1}{m-2},
$$

where a binomial coefficient $\binom{a}{b}$ with $a < 0$ or $b < 0$ is taken to be $0$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Proposition 26 (`jis-2025-25.1.1-prop-26`).

Stated but not proved: `MetaMathlibExt.lonelySinglesCount_ge_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#lonely-singles-count-ge-sum).

## Lower bound for the number of marriageable singles partitions

Extend the binomial
coefficient $\binom{a}{b}$ to all integers $a$, $b$ by setting it to $0$ when $a < 0$ or $b < 0$,
and for every natural number $N$ let

$$S(N) = \sum_{m=0}^{\lfloor N/2 \rfloor} \frac{1}{N-m+1} \binom{N}{m} \binom{N-m-1}{m-1}.$$

For every $n \ge 3$, the number $M_n$ of noncrossing partitions of $\{0, \dots, n-1\}$ that are
marriageable singles partitions satisfies

$$M_n \ge \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} S(n+i-j-1)\, S(j-i-1).$$

For $N \ge 1$, $S(N)$ is the number of noncrossing partitions of an $N$-element set with no
singleton block; with the convention above, $S(0) = 0$.

## Sources

- Julien Rouyer and Alain Ninet, *Two New Integer Sequences Related to Crossroads and Catalan Numbers*, Journal of Integer Sequences 28 (2025), Article 25.1.1, Proposition 27 (`jis-2025-25.1.1-prop-27`).

Stated but not proved: `MetaMathlibExt.marriageableSinglesCount_ge_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/LonelyMarriageableSinglesWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html#marriageable-singles-count-ge-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Marriageable and lonely singles partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/set-partitions/marriageable-and-lonely-singles-partitions)
