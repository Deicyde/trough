---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.longestCommonSubsequence, Cslib.Algorithms.Lean.longestCommonSubsequence_correct, Cslib.Algorithms.Lean.longestCommonSubsequence_time
statement: formalized
proof: formalized
---

# Longest common subsequence

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-common-subsequence/index.html).

## Longest common subsequence by dynamic programming

Given lists $x = x_1 \cdots x_m$ and
$y = y_1 \cdots y_n$ over a type with a boolean equality test, fill a table $c_{i,j}$ for
$0 \le i \le m$ and $0 \le j \le n$ by $c_{i,0} = c_{0,j} = 0$, by $c_{i,j} = c_{i-1,j-1} + 1$ when
the test reports $x_i = y_j$, and by $c_{i,j} = \max(c_{i-1,j}, c_{i,j-1})$ otherwise. Then build
a witness $w$ by walking back from $(m, n)$ until $i = 0$ or $j = 0$: when the test reports
$x_i = y_j$, put $x_i$ in front of $w$ and move to $(i-1, j-1)$; otherwise move to $(i-1, j)$ if
$c_{i-1,j} \ge c_{i,j-1}$ and to $(i, j-1)$ if not. The algorithm returns the pair $(c_{m,n}, w)$.

The abstract time counts one step for each table entry $c_{i,j}$ with $i, j \ge 1$ and one for
each backward step taken from a position with $i, j \ge 1$; everything else is free.

Formalized by `Cslib.Algorithms.Lean.longestCommonSubsequence`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestCommonSubsequence.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestCommonSubsequence.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-common-subsequence/index.html#longest-common-subsequence).

## Correctness of the longest common subsequence algorithm

Let $\alpha$ be a type whose
boolean equality test agrees with equality, let $x$ and $y$ be lists over $\alpha$, and let
$(k, w)$ be the pair returned by the dynamic-programming longest common subsequence algorithm on
$x$ and $y$. Then $w$ has length $k$, $w$ is a subsequence (not necessarily contiguous) of both
$x$ and $y$, and every common subsequence of $x$ and $y$ has length at most the length of $w$.

Formalized by `Cslib.Algorithms.Lean.longestCommonSubsequence_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestCommonSubsequence.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestCommonSubsequence.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-common-subsequence/index.html#longest-common-subsequence-correct).

## Running time of the longest common subsequence algorithm

For lists $x$ and $y$ of
lengths $m$ and $n$ over a type with a boolean equality test, the abstract time of the
dynamic-programming longest common subsequence algorithm on $x$ and $y$ (its number of table
and reconstruction transitions) is at most $mn + (m + n)$.

Formalized by `Cslib.Algorithms.Lean.longestCommonSubsequence_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/LongestCommonSubsequence.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/LongestCommonSubsequence.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-common-subsequence/index.html#longest-common-subsequence-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Longest common subsequence](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/longest-common-subsequence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/dynamic-programming/longest-common-subsequence)
