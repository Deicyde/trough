---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DivisorSumFreeSetLowerBoundWanted.IsDivisorSumFree, MathlibExt.Combinatorics.DivisorSumFreeSetLowerBoundWanted.conjecture, MathlibExt.Combinatorics.DivisorSumFreeSetLowerBoundWanted.conjecture_refuted
statement: formalized
---

# Divisor-sum-free sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/divisor-sum-free-sets/index.html).

## Divisor-sum-free sets

A finite set $S$ of natural numbers is divisor-sum-free if no
element $x \in S$ divides the sum of the elements of any nonempty subset of $S \setminus \{x\}$.

Formalized by `MathlibExt.Combinatorics.DivisorSumFreeSetLowerBoundWanted.IsDivisorSumFree`, a definition declared in [WantedExt/Combinatorics/DivisorSumFreeSetLowerBoundWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DivisorSumFreeSetLowerBoundWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/divisor-sum-free-sets/index.html#is-divisor-sum-free).

## Erdős Problem 131: large divisor-sum-free sets

The proposition that for every real
$\varepsilon > 0$ there is a natural number $N_0$ such that for every natural number $N \ge 1$ with
$N \ge N_0$ there is a set $S \subseteq \{1, \dots, N\}$ with $|S| > N^{1/2 - \varepsilon}$ that is
divisor-sum-free: no element $x \in S$ divides the sum of the elements of any nonempty subset of
$S \setminus \{x\}$.

Formalized by `MathlibExt.Combinatorics.DivisorSumFreeSetLowerBoundWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/DivisorSumFreeSetLowerBoundWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DivisorSumFreeSetLowerBoundWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/divisor-sum-free-sets/index.html#conjecture).

## Erdős Problem 131 has a negative answer

It is not true that for every real
$\varepsilon > 0$ there is a natural number $N_0$ such that for every natural number $N \ge 1$ with
$N \ge N_0$ there is a set $S \subseteq \{1, \dots, N\}$ with $|S| > N^{1/2 - \varepsilon}$ that is
divisor-sum-free, meaning that no element $x \in S$ divides the sum of the elements of any nonempty
subset of $S \setminus \{x\}$.

Let $F(N)$ be the largest size of a divisor-sum-free subset of $\{1, \dots, N\}$. Every
divisor-sum-free set is non-averaging, that is, none of its elements is the average of other
elements of the set (an element equal to the average of $k$ others divides their sum), and Pham
and Zakharov (arXiv:2410.14624) prove that the largest non-averaging subset of $\{1, \dots, N\}$
has size $N^{1/4 + o(1)}$, so $F(N) \le N^{1/4 + o(1)}$; erdosproblems.com/131 (checked
2026-10-22) records that this answers the question negatively. The page also links a formal proof
of $F(N) \le N^{1/5 + o(1)}$, which with Csaba's $F(N) \gg N^{1/5}$ would give the order of growth.

## Sources

- H. T. Pham and D. Zakharov, Sharp bound for the Erdős-Straus non-averaging set problem, arXiv:2410.14624 (2024), https://arxiv.org/abs/2410.14624.

Stated but not proved: `MathlibExt.Combinatorics.DivisorSumFreeSetLowerBoundWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/DivisorSumFreeSetLowerBoundWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DivisorSumFreeSetLowerBoundWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/divisor-sum-free-sets/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisor-sum-free sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/divisor-sum-free-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sum-free-sets/divisor-sum-free-sets)
