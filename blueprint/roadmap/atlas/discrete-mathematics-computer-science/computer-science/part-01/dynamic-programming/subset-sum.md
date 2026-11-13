---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums, Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_mem, Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_zero_mem, Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_sorted, Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_length_le_pow, Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_length_le_target, Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_length_le_sum, Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_powers_of_two
statement: formalized
proof: formalized
---

# Subset sum

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html).

## Attainable sums in exact subset sum

Given a list $x = (x_1, \dots, x_n)$ of natural
numbers and a target $t \in \mathbb{N}$, this timed procedure starts from the list $L_0 = (0)$
and, for $i = 1, \dots, n$ in order, forms $L_i$ from $L_{i-1}$ in four steps: add $x_i$ to
every entry of $L_{i-1}$; merge $L_{i-1}$ with this shifted list (the standard merge of two
lists, comparing entries with $\le$); delete adjacent repeated values; and keep only the values
at most $t$. It returns $L_n$. The counted events are the initial assignment and, in each
phase, one event per addition, one per merge comparison, one per comparison of adjacent
values, one per comparison with $t$, and one for the phase assignment.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums).

## Characterization of the exact subset sum list

Let $x$ be a list of natural numbers,
$t$ a natural number, and $L$ the final list of sums computed by the exact subset sum traversal
on $x$ with target $t$. A natural number $z$ belongs to $L$ if and only if $z \le t$ and $z$ is
the sum of some sublist of $x$ (a subsequence, not necessarily contiguous).

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums-mem).

## Zero is always a computed sum

For every list $x$ of natural numbers and every natural
number $t$, the final list of sums computed by the exact subset sum traversal on $x$ with target
$t$ contains $0$.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_zero_mem`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums-zero-mem).

## The exact subset sum list is strictly increasing

For every list $x$ of natural numbers
and every natural number $t$, the final list of sums computed by the exact subset sum traversal
on $x$ with target $t$ is strictly increasing; in particular it has no repeated entries.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_sorted`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums-sorted).

## The number of computed sums is at most two to the power of the input length

For every
list $x$ of natural numbers, of length $n$, and every natural number $t$, the final list of sums
computed by the exact subset sum traversal on $x$ with target $t$ has length at most $2^n$.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_length_le_pow`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums-length-le-pow).

## The number of computed sums is at most the target plus one

For every list $x$ of
natural numbers and every natural number $t$, the final list of sums computed by the exact subset
sum traversal on $x$ with target $t$ has length at most $t + 1$.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_length_le_target`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums-length-le-target).

## The number of computed sums is at most the input total plus one

For every list $x$ of
natural numbers with sum $S$ and every natural number $t$, the final list of sums computed by the
exact subset sum traversal on $x$ with target $t$ has length at most $S + 1$.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_length_le_sum`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums-length-le-sum).

## Prefixes of the powers of two attain every sum

Let $i \le n$ be natural numbers. On the
list $1, 2, 4, \dots, 2^{i-1}$ (the first $i$ entries of $1, 2, \dots, 2^{n-1}$) with target
$2^n - 1$, the final list of sums computed by the exact subset sum traversal is exactly
$0, 1, 2, \dots, 2^i - 1$ in increasing order.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSumSums_powers_of_two`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-sums-powers-of-two).

## Exact subset sum procedure

Given a list $x$ of natural numbers and a target
$t \in \mathbb{N}$, the procedure first computes the list $L = (\ell_1, \dots, \ell_m)$ of
attainable sums of $x$ with target $t$, then scans it from left to right, keeping a running
maximum that starts at $0$, and returns $\max(0, \ell_1, \dots, \ell_m)$. Its counted events
are those of computing $L$ plus one per entry of $L$.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum).

## Exact subset sum returns the maximum of the computed sums

For every list $x$ of natural
numbers and every natural number $t$, the value returned by the exact subset sum algorithm on $x$
with target $t$ equals $\max(\cdots\max(\max(0, s_1), s_2)\cdots, s_k)$, where $s_1, \dots, s_k$
is the final list of sums computed by the exact subset sum traversal on $x$ with target $t$.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-ret).

## Event count of exact subset sum

Let $x = (x_1, \dots, x_n)$ be a list of natural
numbers and $t \in \mathbb{N}$ a target. For $0 \le i \le n$ let $L_i$ be the list of attainable
sums of the prefix $(x_1, \dots, x_i)$ with target $t$. For $i < n$ let $M_i$ be the merge of
$L_i$ with the list obtained by adding $x_{i+1}$ to every entry of $L_i$, let $c_i$ be the
number of comparisons this merge makes, and let $D_i$ be $M_i$ with adjacent repeated values
deleted. Then the number of counted events of the exact subset-sum procedure on $x$ and $t$ is

$$1 + n + \sum_{i=0}^{n-1} \bigl(|L_i| + c_i + (|M_i| - 1) + |D_i|\bigr) + |L_n|,$$

where $|\cdot|$ denotes length and $|M_i| - 1$ is truncated subtraction of natural numbers.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-time).

## Exponential lower bound for exact subset sum on powers of two

For every
$n \in \mathbb{N}$, the exact subset-sum procedure on the list $(2^0, 2^1, \dots, 2^{n-1})$
(empty when $n = 0$) with target $2^n - 1$ makes at least $2^n - 1$ counted events.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_time_ge_powers_of_two`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-time-ge-powers-of-two).

## Exponential upper bound for exact subset sum

For every list $x$ of $n$ natural numbers
and every target $t \in \mathbb{N}$, the exact subset-sum procedure on $x$ and $t$ makes at most
$1 + n + 7(2^n - 1) + 2^n$ counted events.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_time_le_exponential`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-time-le-exponential).

## Pseudo-polynomial bound for exact subset sum

For every list $x$ of $n$ natural numbers
with sum $s$ and every target $t \in \mathbb{N}$, the exact subset-sum procedure on $x$ and $t$
makes at most $1 + n + (7n + 1)\min(t + 1, s + 1)$ counted events.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_time_le_numeric`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-time-le-numeric).

## Polynomial event bound for exact subset sum with a polynomially bounded target

Let $x$
be a list of $n$ natural numbers and let $t, d \in \mathbb{N}$ with $t \le n^d$. Then the exact
subset-sum procedure on $x$ and $t$ makes at most $1 + n + (7n + 1)(n^d + 1)$ counted events.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_time_le_of_target_le_pow`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-time-le-of-target-le-po).

## Polynomial event bound for exact subset sum with polynomially bounded inputs

Let $x$ be
a list of $n$ natural numbers and let $d \in \mathbb{N}$ be such that every entry of $x$ is at
most $n^d$. Then for every target $t \in \mathbb{N}$ the exact subset-sum procedure on $x$ and
$t$ makes at most $1 + n + (7n + 1)(n \cdot n^d + 1)$ counted events.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_time_le_of_values_le_pow`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-time-le-of-values-le-po).

## Optimality of exact subset sum

Let $x$ be a list of natural numbers, $t$ a natural
number, and $r$ the value returned by the exact subset sum algorithm on $x$ with target $t$.
Then $r$ is the sum of some sublist of $x$ (a subsequence, not necessarily contiguous),
$r \le t$, and every sublist of $x$ whose sum is at most $t$ has sum at most $r$.

The entries of $x$ may be zero or repeated.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_optimal`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-optimal).

## Optimality of exact subset sum for distinct positive inputs

Let $x$ be a list of
distinct positive natural numbers, $t$ a positive natural number, and $r$ the value returned by
the exact subset sum algorithm on $x$ with target $t$. Then $r$ is the sum of some sublist of
$x$ (a subsequence, not necessarily contiguous), $r \le t$, and every sublist of $x$ whose sum
is at most $t$ has sum at most $r$.

These are the hypotheses of CLRS, Section 35.5; the proof does not use them.

Formalized by `Cslib.Algorithms.Lean.ExactSubsetSum.exactSubsetSum_optimal_of_positive`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/ExactSubsetSum.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html#exact-subset-sum-optimal-of-positive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subset sum](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/subset-sum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/dynamic-programming/subset-sum)
