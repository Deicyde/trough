---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MaximalSumFreeSetsCountErdosProblem877Wanted.maximalSumFreeCount, MathlibExt.Combinatorics.MaximalSumFreeSetsCountErdosProblem877Wanted.maximalSumFreeCountSmall, MathlibExt.Combinatorics.MaximalSumFreeSetsCountErdosProblem877Wanted.maximalSumFreeCountSmall_holds, MathlibExt.Combinatorics.SumFreeSubsetCountErdosProblem748Wanted.sumFreeCount, MathlibExt.Combinatorics.SumFreeSubsetCountErdosProblem748Wanted.sumFreeCountExponent, MathlibExt.Combinatorics.SumFreeSubsetCountErdosProblem748Wanted.sumFreeCountExponent_holds
statement: formalized
---

# Number of sum-free sets

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html).

## Number of maximal sum-free subsets of $\{1, \dots, n\}$

For a natural number $n$,
$f_m(n)$ is the number of sets $A \subseteq \{1, \dots, n\}$ that are sum-free, meaning
$x + y \notin A$ for all $x, y \in A$ (including $x = y$), and maximal with this property:
every sum-free set $B$ with $A \subseteq B \subseteq \{1, \dots, n\}$ equals $A$.

Formalized by `MathlibExt.Combinatorics.MaximalSumFreeSetsCountErdosProblem877Wanted.maximalSumFreeCount`, a definition declared in [WantedExt/Combinatorics/MaximalSumFreeSetsCountErdosProblem877Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MaximalSumFreeSetsCountErdosProblem877Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html#maximal-sum-free-count).

## Erdős Problem 877 on maximal sum-free sets

Let $f_m(n)$ be the number of maximal
sum-free subsets of $\{1, \dots, n\}$. This is the statement, asked by Cameron and Erdős, that
$f_m(n) / 2^{n/2} \to 0$ as $n \to \infty$, that is, $f_m(n) = o(2^{n/2})$.

Formalized by `MathlibExt.Combinatorics.MaximalSumFreeSetsCountErdosProblem877Wanted.maximalSumFreeCountSmall`, a definition declared in [WantedExt/Combinatorics/MaximalSumFreeSetsCountErdosProblem877Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MaximalSumFreeSetsCountErdosProblem877Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html#maximal-sum-free-count-small).

## Maximal sum-free subsets of $\{1, \dots, n\}$ number $o(2^{n/2})$

Let $f_m(n)$ be the
number of maximal sum-free subsets of $\{1, \dots, n\}$. Then $f_m(n) / 2^{n/2} \to 0$ as
$n \to \infty$, that is, $f_m(n) = o(2^{n/2})$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #877, https://www.erdosproblems.com/877 (status PROVED); resolution: T. Łuczak and T. Schoen, On the number of maximal sum-free sets, Proc. Amer. Math. Soc. 129 (2001), 2205-2207, abstract: {1, 2, …, n} contains at most 2^{n/2 - 2^{-28} n} maximal sum-free subsets, provided n is large enough; erdosproblems.com/877: this resolves the question, and Balogh, Liu, Sharifzadeh and Treglown later proved f_m(n) = 2^{(1/4 + o(1)) n}, https://doi.org/10.1090/S0002-9939-00-05815-9.

Stated but not proved: `MathlibExt.Combinatorics.MaximalSumFreeSetsCountErdosProblem877Wanted.maximalSumFreeCountSmall_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MaximalSumFreeSetsCountErdosProblem877Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MaximalSumFreeSetsCountErdosProblem877Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html#maximal-sum-free-count-small-holds).

## Number of sum-free subsets of $\{1, \dots, n\}$

For a natural number $n$, $f(n)$ is the
number of sets $A \subseteq \{1, \dots, n\}$ that are sum-free, meaning that there are no
$a, b, c \in A$ with $a = b + c$ (the case $b = c$ included). The empty set is counted.

Formalized by `MathlibExt.Combinatorics.SumFreeSubsetCountErdosProblem748Wanted.sumFreeCount`, a definition declared in [WantedExt/Combinatorics/SumFreeSubsetCountErdosProblem748Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumFreeSubsetCountErdosProblem748Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html#sum-free-count).

## Erdős Problem 748 on the number of sum-free sets

Let $f(n)$ be the number of sum-free
subsets of $\{1, \dots, n\}$. This is the statement that $\log_2 f(n) / n \to 1/2$ as
$n \to \infty$, that is, $f(n) = 2^{(1 + o(1)) n / 2}$.

Formalized by `MathlibExt.Combinatorics.SumFreeSubsetCountErdosProblem748Wanted.sumFreeCountExponent`, a definition declared in [WantedExt/Combinatorics/SumFreeSubsetCountErdosProblem748Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumFreeSubsetCountErdosProblem748Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html#sum-free-count-exponent).

## Sum-free subsets of $\{1, \dots, n\}$ number $2^{(1 + o(1)) n / 2}$

Let $f(n)$ be the
number of sum-free subsets of $\{1, \dots, n\}$, that is, of sets $A \subseteq \{1, \dots, n\}$
with no $a, b, c \in A$ satisfying $a = b + c$ (the case $b = c$ included). Then
$\log_2 f(n) / n \to 1/2$ as $n \to \infty$, that is, $f(n) = 2^{(1 + o(1)) n / 2}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #748, https://www.erdosproblems.com/748 (status PROVED); resolution: B. Green, The Cameron-Erdős conjecture, Bull. London Math. Soc. 36 (2004), 769-778; A. A. Sapozhenko, The Cameron-Erdős conjecture, Dokl. Akad. Nauk 393 (2003), 749-752, abstract of arXiv:math/0304058 (Green): the number of sum-free subsets of {1, …, N} is O(2^{N/2}); erdosproblems.com/748: true, in fact f(n) ≪ 2^{n/2} (Green; Sapozhenko), with the trivial lower bound from subsets of the upper half, https://arxiv.org/abs/math/0304058.

Stated but not proved: `MathlibExt.Combinatorics.SumFreeSubsetCountErdosProblem748Wanted.sumFreeCountExponent_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SumFreeSubsetCountErdosProblem748Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SumFreeSubsetCountErdosProblem748Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html#sum-free-count-exponent-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Number of sum-free sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/number-of-sum-free-sets)
