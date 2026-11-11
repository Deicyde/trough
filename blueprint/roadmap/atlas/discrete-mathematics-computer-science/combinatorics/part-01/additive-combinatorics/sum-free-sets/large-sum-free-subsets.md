---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GreenProblem1LargeSumFreeWanted.IsSumFree, MathlibExt.Combinatorics.GreenProblem1LargeSumFreeWanted.conjecture, MathlibExt.Combinatorics.GreenProblem1LargeSumFreeWanted.conjecture_holds
statement: formalized
---

# Large sum-free subsets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/large-sum-free-subsets/index.html).

## Sum-free sets of natural numbers

A finite set $S$ of natural numbers is sum-free if
$x + y \notin S$ for all $x, y \in S$, where $x = y$ is allowed.

## Sources

- [GREEN-001].

Formalized by `MathlibExt.Combinatorics.GreenProblem1LargeSumFreeWanted.IsSumFree`, a definition declared in [WantedExt/Combinatorics/GreenProblem1LargeSumFreeWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem1LargeSumFreeWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/large-sum-free-subsets/index.html#is-sum-free).

## Green's Problem 1 on large sum-free subsets

The statement that there is a function
$\omega$ from the natural numbers to the real numbers with $\omega(n) \to \infty$ as
$n \to \infty$ such that every finite set $A$ of positive integers contains a sum-free subset
$B \subseteq A$ with $|B| \ge |A|/3 + \omega(|A|)$.

## Sources

- Ben Green, Problem 1 [GREEN-001].

Formalized by `MathlibExt.Combinatorics.GreenProblem1LargeSumFreeWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/GreenProblem1LargeSumFreeWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem1LargeSumFreeWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/large-sum-free-subsets/index.html#conjecture).

## Bedert's theorem on large sum-free subsets

There is a function $\omega$ from the natural
numbers to the real numbers with $\omega(n) \to \infty$ as $n \to \infty$ such that every finite
set $A$ of positive integers contains a subset $B \subseteq A$ with $x + y \notin B$ for all
$x, y \in B$ (a sum-free subset) and $|B| \ge |A|/3 + \omega(|A|)$.

Bedert proves more: every $n$-element set of integers contains a sum-free subset of size at least
$n/3 + c \log \log n$ for an absolute constant $c > 0$. This answers Green's Problem 1.

## Sources

- Benjamin Bedert, Large sum-free subsets of sets of integers via L¹-estimates for trigonometric series, arXiv:2502.08624v1, https://arxiv.org/abs/2502.08624v1.

Stated but not proved: `MathlibExt.Combinatorics.GreenProblem1LargeSumFreeWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/GreenProblem1LargeSumFreeWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GreenProblem1LargeSumFreeWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/large-sum-free-subsets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large sum-free subsets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/large-sum-free-subsets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/large-sum-free-subsets)
