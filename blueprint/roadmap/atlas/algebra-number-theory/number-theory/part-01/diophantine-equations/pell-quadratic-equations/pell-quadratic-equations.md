---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MarkoffGraphWanted.Combinatorics.dvd_card_connectedComponent_markoffGraph, FibonacciNormEquation.fibonacci_norm_eq_one_or_neg_one_iff
statement: formalized
---

# Pell and quadratic Diophantine equations: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/index.html).

Pell and negative Pell equations, norm equations, Pythagorean triples, Markov triples and quadratic equations in two or three variables.

## Chen's theorem for Markoff graphs

Let $p > 3$ be a prime. The Markoff graph over
$\mathbb{Z}/p\mathbb{Z}$ has as vertices the nonzero triples $(x_0, x_1, x_2)$ of elements of
$\mathbb{Z}/p\mathbb{Z}$ with $x_0^2 + x_1^2 + x_2^2 = 3 x_0 x_1 x_2$, and two distinct
triples are adjacent when one is obtained from the other by a Vieta involution, which replaces
one coordinate $x_i$ by $3 x_j x_k - x_i$ and keeps the other two coordinates $x_j$, $x_k$,
where $\{i, j, k\} = \{0, 1, 2\}$. Every connected component of this graph has a number of
vertices divisible by $p$.

## Sources

- https://link.springer.com/article/10.1007/s00222-025-01346-9. Problem `dvd_card_connectedComponent_markoffGraph` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.MarkoffGraphWanted.Combinatorics.dvd_card_connectedComponent_markoffGraph` is written with `theorem_wanted` in [WantedExt/Combinatorics/MarkoffGraphWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MarkoffGraphWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/index.html#dvd-card-connected-component-markoff-gra).

## Integer solutions of $x^2 - xy - y^2 = \pm 1$

For integers $x$ and $y$, we have
$x^2 - xy - y^2 = 1$ or $x^2 - xy - y^2 = -1$ if and only if there are an integer $n$ and a
sign $s \in \{1, -1\}$ with $x = s F_n$ and $y = s F_{n-1}$. Here $(F_n)_{n \in \mathbb{Z}}$
is the Fibonacci sequence extended to all integers by $F_0 = 0$, $F_1 = 1$ and
$F_{n+2} = F_{n+1} + F_n$ for every integer $n$.

## Sources

- Bahar Demirtürk and Refik Keskin, “Integer Solutions of Some Diophantine Equations via Fibonacci and Lucas Numbers”, Journal of Integer Sequences 12 (2009), Article 09.8.7, Theorem 1.2 at source lines 171–175, https://cs.uwaterloo.ca/journals/JIS/VOL12/Demirturk/demirturk3.tex.

Formalized by `FibonacciNormEquation.fibonacci_norm_eq_one_or_neg_one_iff`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/FibonacciNormEquation.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/FibonacciNormEquation.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/index.html#fibonacci-norm-eq-one-or-neg-one-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pell and quadratic Diophantine equations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations)
