---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ZeroSubsetSumSqrtErdosProblem540Wanted.sqrtSizeHasZeroSubsetSum, MathlibExt.Combinatorics.ZeroSubsetSumSqrtErdosProblem540Wanted.sqrtSizeHasZeroSubsetSum_holds
statement: formalized
---

# Zero subset sums in cyclic groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-subset-sums-in-cyclic-groups/index.html).

## The Erdős–Heilbronn zero subset sum statement (Erdős Problem 540)

This is the statement
that there is a real number $C > 0$ such that for every integer $N \ge 1$, every set
$A \subseteq \mathbb{Z}/N\mathbb{Z}$ with $|A| \ge C\sqrt{N}$ has a nonempty subset $S \subseteq A$
whose elements sum to $0$ in $\mathbb{Z}/N\mathbb{Z}$.

Formalized by `MathlibExt.Combinatorics.ZeroSubsetSumSqrtErdosProblem540Wanted.sqrtSizeHasZeroSubsetSum`, a definition declared in [WantedExt/Combinatorics/ZeroSubsetSumSqrtErdosProblem540Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ZeroSubsetSumSqrtErdosProblem540Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-subset-sums-in-cyclic-groups/index.html#sqrt-size-has-zero-subset-sum).

## Zero subset sums of large sets in $\mathbb{Z}/N\mathbb{Z}$ (Erdős Problem 540)

There is a real
number $C > 0$ such that for every integer $N \ge 1$, every set $A \subseteq \mathbb{Z}/N\mathbb{Z}$
with $|A| \ge C\sqrt{N}$ has a nonempty subset $S \subseteq A$ whose elements sum to $0$ in
$\mathbb{Z}/N\mathbb{Z}$.

Resolved true: Olson proved it for prime $N$ and Szemerédi for all $N$ (in every finite abelian
group); Hamidoune and Zémor showed $(1 + o(1))\sqrt{2N}$ suffices.

## Sources

- T. F. Bloom, Erdős Problems, Problem #540, https://www.erdosproblems.com/540 (status PROVED (LEAN)); resolution: E. Szemerédi, On a conjecture of Erdős and Heilbronn, Acta Arith. (1970), 227-229, erdosproblems.com/540: yes; Olson for N prime, Szemerédi for all N (indeed for all finite abelian groups), https://www.erdosproblems.com/540.

Stated but not proved: `MathlibExt.Combinatorics.ZeroSubsetSumSqrtErdosProblem540Wanted.sqrtSizeHasZeroSubsetSum_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ZeroSubsetSumSqrtErdosProblem540Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ZeroSubsetSumSqrtErdosProblem540Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-subset-sums-in-cyclic-groups/index.html#sqrt-size-has-zero-subset-sum-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zero subset sums in cyclic groups](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-subset-sums-in-cyclic-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-subset-sums-in-cyclic-groups)
