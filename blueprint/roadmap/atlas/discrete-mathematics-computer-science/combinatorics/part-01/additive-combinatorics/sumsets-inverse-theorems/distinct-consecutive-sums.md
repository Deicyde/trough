---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.consecutiveSums, MathlibExt.Combinatorics.IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.manyDistinctConsecutiveSums, MathlibExt.Combinatorics.IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.manyDistinctConsecutiveSums_holds
statement: formalized
---

# Distinct consecutive sums

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/distinct-consecutive-sums/index.html).

## Consecutive sums

Let $k \in \mathbb{N}$ and let $a_0, \dots, a_{k-1}$ be natural
numbers. The consecutive sums of $a$ form the finite set of natural numbers
$a_u + a_{u+1} + \dots + a_v$ for indices $0 \le u \le v \le k - 1$.

Formalized by `MathlibExt.Combinatorics.IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.consecutiveSums`, a definition declared in [WantedExt/Combinatorics/IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/distinct-consecutive-sums/index.html#consecutive-sums).

## Erdős Problem 356

The proposition that there is a real number $c > 0$ such that for all
sufficiently large $n \in \mathbb{N}$ there exist $k \in \mathbb{N}$ and natural numbers
$a_0 < a_1 < \dots < a_{k-1}$ with $1 \le a_i \le n$ for every $i$, whose set of consecutive sums
$a_u + a_{u+1} + \dots + a_v$ (for $u \le v$) has at least $c n^2$ elements.

Formalized by `MathlibExt.Combinatorics.IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.manyDistinctConsecutiveSums`, a definition declared in [WantedExt/Combinatorics/IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/distinct-consecutive-sums/index.html#many-distinct-consecutive-sums).

## Erdős Problem 356 has a positive answer

There is a real number $c > 0$ such that for all
sufficiently large $n \in \mathbb{N}$ there exist $k \in \mathbb{N}$ and natural numbers
$a_0 < a_1 < \dots < a_{k-1}$ with $1 \le a_i \le n$ for every $i$, whose set of consecutive sums
$a_u + a_{u+1} + \dots + a_v$ (for $u \le v$) has at least $c n^2$ elements.

## Sources

- T. F. Bloom, Erdős Problems, Problem #356, https://www.erdosproblems.com/356 (status PROVED (LEAN)); resolution: A. Beker, On a problem of Erdős and Graham about consecutive sums in strictly increasing sequences, arXiv:2311.10087 (2023), erdosproblems.com/356: the original problem was solved in the affirmative by Beker, https://arxiv.org/abs/2311.10087.

Stated but not proved: `MathlibExt.Combinatorics.IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.manyDistinctConsecutiveSums_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/IncreasingSequenceConsecutiveSumsErdosProblem356Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/distinct-consecutive-sums/index.html#many-distinct-consecutive-sums-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distinct consecutive sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/distinct-consecutive-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/distinct-consecutive-sums)
