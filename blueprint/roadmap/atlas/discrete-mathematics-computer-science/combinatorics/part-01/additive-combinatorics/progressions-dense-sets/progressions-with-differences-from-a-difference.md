---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ProgressionDifferenceSetErdosProblem1185Wanted.progressionWithDifferenceInDifferenceSet, MathlibExt.Combinatorics.ProgressionDifferenceSetErdosProblem1185Wanted.progressionWithDifferenceInDifferenceSet_refuted
statement: formalized
---

# Progressions with differences from a difference set

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progressions-with-differences-from-a-difference/index.html).

## Erdős Problem 1185: progressions with difference in a difference set

This is the
statement that for every real $\delta > 0$ and every natural number $k \ge 3$ there is a natural
number $m \ge 1$ such that for all sufficiently large natural numbers $N$, whenever $A$ and $B$
are subsets of $\{1, \dots, N\}$ with $|A| \ge \delta N$ and $|B| \ge m$, there are natural
numbers $a$ and $d > 0$ such that $b_1 = b_2 + d$ for some $b_1, b_2 \in B$ and $a + i d \in A$
for every natural number $i < k$; that is, $A$ contains the $k$-term arithmetic progression
$a, a + d, \dots, a + (k - 1) d$, whose common difference $d$ is positive and lies in $B - B$.

Formalized by `MathlibExt.Combinatorics.ProgressionDifferenceSetErdosProblem1185Wanted.progressionWithDifferenceInDifferenceSet`, a definition declared in [WantedExt/Combinatorics/ProgressionDifferenceSetErdosProblem1185Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ProgressionDifferenceSetErdosProblem1185Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progressions-with-differences-from-a-difference/index.html#progression-with-difference-in-differenc).

## Erdős Problem 1185 is false

The following statement is false: for every real $\delta > 0$
and every natural number $k \ge 3$ there is a natural number $m \ge 1$ such that for all
sufficiently large natural numbers $N$, whenever $A$ and $B$ are subsets of $\{1, \dots, N\}$
with $|A| \ge \delta N$ and $|B| \ge m$, there are natural numbers $a$ and $d > 0$ such that
$b_1 = b_2 + d$ for some $b_1, b_2 \in B$ and $a + i d \in A$ for every natural number $i < k$.

The answer is negative already for $k = 3$: Furstenberg gave an infinite set $B$ such that
$B - B$ is not $2$-intersective, that is, some set of positive density contains no $3$-term
progression with common difference in $B - B$; truncating both sets at $N$ gives
counterexamples with $|B \cap [1, N]|$ unbounded.

## Sources

- T. F. Bloom, Erdős Problems, Problem #1185, https://www.erdosproblems.com/1185 (status SOLVED); resolution: H. Furstenberg, Recurrence in Ergodic Theory and Combinatorial Number Theory, Princeton University Press (1981), erdosproblems.com/1185: false already at k = 3, since Furstenberg gave an infinite set B such that B - B is not 2-intersective.

Stated but not proved: `MathlibExt.Combinatorics.ProgressionDifferenceSetErdosProblem1185Wanted.progressionWithDifferenceInDifferenceSet_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ProgressionDifferenceSetErdosProblem1185Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ProgressionDifferenceSetErdosProblem1185Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progressions-with-differences-from-a-difference/index.html#progression-with-difference-in-differenc-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Progressions with differences from a difference set](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progressions-with-differences-from-a-difference/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/progressions-with-differences-from-a-difference)
