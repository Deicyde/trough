---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.bestSet, Cslib.Algorithms.Lean.TimeM.greedySetCover, Cslib.Algorithms.Lean.TimeM.greedySetCover_mem, Cslib.Algorithms.Lean.TimeM.greedySetCover_covers, Cslib.Algorithms.Lean.TimeM.greedySetCover_length_le, Cslib.Algorithms.Lean.TimeM.greedySetCover_time_le, Cslib.Algorithms.Lean.TimeM.div_le_harmonic_sub, Cslib.Algorithms.Lean.TimeM.card_le_sum_card_inter
statement: formalized
proof: formalized
---

# Greedy set cover

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html).

## Greedy choice of a set

Given a list $F$ of finite sets and a finite set $U$, the best set
of $F$ for $U$ is the first set $S$ in the list $F$ that maximizes $|S \cap U|$, or $\emptyset$
when $F$ is empty.

Formalized by `Cslib.Algorithms.Lean.TimeM.bestSet`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#best-set).

## Greedy set cover

Let $F = [S_1, \dots, S_n]$ be a list of finite sets and $U$ a finite
set. The greedy set cover of $U$ from $F$ is computed as follows. Let $T$ be the first $S_i$ in
the list that maximizes $|S_i \cap U|$, or $T = \emptyset$ when $n = 0$. If
$T \cap U = \emptyset$, the result is the empty list; otherwise it is $T$ followed by the greedy
set cover of $U \setminus T$ from $F$. Each step, including the last one, costs
$n + |S_1| + \dots + |S_n|$.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover).

## The greedy set cover draws its sets from the family

For every list $F$ of finite sets and
every finite set $U$, every set in the list returned by the greedy set cover algorithm on $F$ and
$U$ is a member of $F$.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-mem).

## The greedy set cover is a cover

Let $F$ be a list of finite sets and $U$ a finite set
such that every element of $U$ lies in some set of $F$. Then every element of $U$ lies in some
set of the list returned by the greedy set cover algorithm on $F$ and $U$.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_covers`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-covers).

## The greedy set cover has at most as many sets as elements

For every list $F$ of finite
sets and every finite set $U$, the list returned by the greedy set cover algorithm on $F$ and $U$
has length at most $|U|$.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_length_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-length-le).

## Running time of greedy set cover

Let $F$ be a list of finite sets and $U$ a finite set.
The running time of greedy set cover of $U$ from $F$ is at most
$(|U| + 1)(|F| + \sum_{S \in F} |S|)$, where $|F|$ is the length of the list and the sum runs
over the entries of $F$, counted with repetition.

There are at most $|U| + 1$ searches for a best set, each costing $|F| + \sum_{S \in F} |S|$.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-time-le).

## Lower bound for a difference of harmonic numbers

Write
$H(n) = 1 + \frac12 + \dots + \frac1n$ for the $n$-th harmonic number, so $H(0) = 0$. For natural
numbers $d \le a \le k$, we have $\frac{d}{k} \le H(a) - H(a - d)$, where $\frac{d}{k}$ is read
as $0$ when $k = 0$.

Each of the $d$ reciprocals $\frac{1}{a - d + 1}, \dots, \frac{1}{a}$ is at least $\frac1k$.

Formalized by `Cslib.Algorithms.Lean.TimeM.div_le_harmonic_sub`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#div-le-harmonic-sub).

## Covering bound by intersections

Let $L$ be a list of finite sets and $T$ a finite set
such that every element of $T$ lies in some member of $L$. Then
$|T| \le \sum_{S \in L} |S \cap T|$, where the sum runs over the list $L$ with repetitions.

Formalized by `Cslib.Algorithms.Lean.TimeM.card_le_sum_card_inter`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#card-le-sum-card-inter).

## Potential bound for greedy set cover

Let $F$ be a list of finite sets, $U$ a finite set,
and $H(n) = 1 + \frac12 + \dots + \frac1n$ the $n$-th harmonic number. For every list $C^*$ of
members of $F$ that together cover $U$, the list of sets returned by the greedy set cover
algorithm on $F$ and $U$ has length at most $\sum_{S \in C^*} H(|S \cap U|)$, where the sum
runs over the list $C^*$ with repetitions.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_length_le_sum_harmonic`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-length-le-sum-harmonic).

## Harmonic bound in the largest set size for greedy set cover

Let $F$ be a list of finite
sets each with at most $d$ elements, $U$ a finite set, and $H(n) = 1 + \frac12 + \dots + \frac1n$
the $n$-th harmonic number. For every list $C^*$ of members of $F$ that together cover $U$, the
list of sets returned by the greedy set cover algorithm on $F$ and $U$ has length at most
$|C^*| \cdot H(d)$, where $|C^*|$ is the length of $C^*$.

## Sources

- CLRS, third edition, Theorem 35.4.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_approx`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-approx).

## Harmonic bound in the universe size for greedy set cover

Let $F$ be a list of finite
sets, $U$ a finite set, and $H(n) = 1 + \frac12 + \dots + \frac1n$ the $n$-th harmonic number. For
every list $C^*$ of members of $F$ that together cover $U$, the list of sets returned by the
greedy set cover algorithm on $F$ and $U$ has length at most $|C^*| \cdot H(|U|)$, where $|C^*|$
is the length of $C^*$.

## Sources

- CLRS, third edition, Corollary 35.5, in the stronger harmonic form.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_approx_card`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-approx-card).

## Greedy set cover is a logarithmic approximation

Let $F$ be a list of finite sets and $U$
a finite set. For every list $C^*$ of members of $F$ that together cover $U$, the list of sets
returned by the greedy set cover algorithm on $F$ and $U$ has length at most
$|C^*| \cdot (\ln |U| + 1)$, where $|C^*|$ is the length of $C^*$ and $\ln 0 = 0$.

## Sources

- CLRS, third edition, Corollary 35.5, via Mathlib's `harmonic_le_one_add_log`.

Formalized by `Cslib.Algorithms.Lean.TimeM.greedySetCover_approx_log`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/SetCover.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/SetCover.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#greedy-set-cover-approx-log).

## Set with the least cost per new element

Given a list $F$ of finite sets, a finite set $U$
and a rational cost $w(S)$ for each finite set $S$, this is the first set $S$ in $F$ with
$S \cap U \ne \emptyset$ that minimizes the ratio $w(S) / |S \cap U|$ among the sets of $F$ meeting
$U$, or nothing when no set of $F$ meets $U$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bestRatioSet`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#best-ratio-set).

## Weighted greedy set cover

Let $F = [S_1, \dots, S_n]$ be a list of finite sets, $U$ a
finite set and $w$ a function giving each finite set $S$ a rational cost $w(S)$. The weighted
greedy set cover of $U$ from $F$ with costs $w$ is computed as follows. If no $S_i$ meets $U$,
the result is the empty list. Otherwise let $T$ be the first $S_i$ in the list with
$S_i \cap U \ne \emptyset$ that minimizes $w(S_i) / |S_i \cap U|$ among the sets of $F$ meeting
$U$; the result is $T$ followed by the weighted greedy set cover of $U \setminus T$ from $F$ with
costs $w$. Each step, including the last one, costs $n + |S_1| + \dots + |S_n|$.

Formalized by `Cslib.Algorithms.Lean.TimeM.weightedGreedySetCover`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#weighted-greedy-set-cover).

## The weighted greedy set cover uses sets of the family

For every list $F$ of finite sets,
finite set $U$ and rational cost function $w$ on finite sets, every set chosen by the weighted
greedy set cover of $U$ from $F$ with costs $w$ belongs to $F$.

Formalized by `Cslib.Algorithms.Lean.TimeM.weightedGreedySetCover_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#weighted-greedy-set-cover-mem).

## The weighted greedy set cover is a cover

Let $F$ be a list of finite sets, $U$ a finite
set and $w$ any rational cost function on finite sets. If every element of $U$ lies in some set of
$F$, then every element of $U$ lies in some set chosen by the weighted greedy set cover of $U$ from
$F$ with costs $w$.

Formalized by `Cslib.Algorithms.Lean.TimeM.weightedGreedySetCover_covers`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#weighted-greedy-set-cover-covers).

## Running time of weighted greedy set cover

Let $F = [S_1, \dots, S_m]$ be a list of finite
sets, $U$ a finite set and $w$ a rational cost function on finite sets. The weighted greedy set
cover of $U$ from $F$ with costs $w$ runs in time at most
$(|U| + 1)\,(m + |S_1| + \dots + |S_m|)$: at most $|U| + 1$ searches for a best set, each costing
$m$ plus the total size of the sets of $F$.

Formalized by `Cslib.Algorithms.Lean.TimeM.weightedGreedySetCover_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#weighted-greedy-set-cover-time-le).

## Total cost of a list of sets

For a function $w$ assigning a rational cost to each finite
set, the total cost of a list $C = [S_1, \dots, S_m]$ of finite sets is
$w(S_1) + \dots + w(S_m)$, a set that occurs several times in $C$ being counted each time.

Formalized by `Cslib.Algorithms.Lean.TimeM.totalCost`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#total-cost).

## Potential bound for weighted greedy set cover

Let $F$ be a list of finite sets, $U$ a
finite set and $w$ a rational cost function on finite sets with $w(S) \ge 0$ for every $S$ in $F$.
If $C^*$ is a list of sets from $F$ whose union contains $U$, then the weighted greedy set cover of
$U$ from $F$ with costs $w$ has total cost at most $\sum_{S \in C^*} w(S)\, H(|S \cap U|)$, the sum
running over the entries of $C^*$ with repetition, where
$H(n) = 1 + \frac{1}{2} + \dots + \frac{1}{n}$ is the $n$-th harmonic number.

Formalized by `Cslib.Algorithms.Lean.TimeM.weightedGreedySetCover_cost_le_sum_harmonic`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#weighted-greedy-set-cover-cost-le-sum-ha).

## Chvátal's bound

Let $F$ be a list of finite sets, $U$ a finite set, $w$ a rational cost
function on finite sets with $w(S) \ge 0$ for every $S$ in $F$, and $d$ a natural number such that
every set in $F$ has at most $d$ elements. If $C^*$ is a list of sets from $F$ whose union contains
$U$, then the weighted greedy set cover of $U$ from $F$ with costs $w$ has total cost at most
$H(d)$ times the total cost of $C^*$, where $H(d) = 1 + \frac{1}{2} + \dots + \frac{1}{d}$ is the
$d$-th harmonic number.

Formalized by `Cslib.Algorithms.Lean.TimeM.weightedGreedySetCover_approx`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Approximation/WeightedSetCover.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html#weighted-greedy-set-cover-approx).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Greedy set cover](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/approximation-algorithms/greedy-set-cover)
