---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GraphRestrictedSumProductErdosProblem808Wanted.restrictedSumProductAlongGraphs, MathlibExt.Combinatorics.GraphRestrictedSumProductErdosProblem808Wanted.restrictedSumProductAlongGraphs_refuted
statement: formalized
---

# Sums and products along graphs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-and-products-along-graphs/index.html).

## Erdős Problem 808 (sums and products along graphs)

The statement that for all real
numbers $c > 0$ and $\varepsilon > 0$ and all sufficiently large natural numbers $n$ the following
holds. Let $A$ be a set of $n$ positive integers and let $E$ be a finite set of pairs $(a, b)$ with
$a, b \in A$ and $a < b$ (the edges of a graph on $A$) such that $|E| \ge n^{1+c}$. Write
$A +_E A = \{a + b : (a, b) \in E\}$ and $A \cdot_E A = \{ab : (a, b) \in E\}$. Then
$\max(|A +_E A|, |A \cdot_E A|) \ge n^{1+c-\varepsilon}$.

Formalized by `MathlibExt.Combinatorics.GraphRestrictedSumProductErdosProblem808Wanted.restrictedSumProductAlongGraphs`, a definition declared in [WantedExt/Combinatorics/GraphRestrictedSumProductErdosProblem808Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GraphRestrictedSumProductErdosProblem808Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-and-products-along-graphs/index.html#restricted-sum-product-along-graphs).

## Erdős Problem 808 is false

There are real numbers $c > 0$ and $\varepsilon > 0$ such
that for infinitely many natural numbers $n$ there are a set $A$ of $n$ positive integers and a
finite set $E$ of pairs $(a, b)$ with $a, b \in A$ and $a < b$ (the edges of a graph on $A$)
such that $|E| \ge n^{1+c}$ and
$\max(|\{a + b : (a, b) \in E\}|, |\{ab : (a, b) \in E\}|) < n^{1+c-\varepsilon}$.

Alon, Ruzsa and Solymosi constructed, for arbitrarily large $n$, sets of $n$ integers with
graphs of $n^{5/3 - o(1)}$ edges along which both the sums and the products take at most
$n^{4/3 + o(1)}$ values, and counterexamples in $\mathbb{N}$ for every $0 < c < 1$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #808, https://www.erdosproblems.com/808 (status DISPROVED); resolution: N. Alon, I. Ruzsa and J. Solymosi, Sums, products and ratios along the edges of a graph, Publ. Mat. 64 (2020), 143-155, Theorem 3: for arbitrarily large m_0 there are a set A of m ≥ m_0 integers and a graph on A with Ω(m^{5/3}/log^{1/3} m) edges such that |A +_G A| + |A ·_G A| = O((m log m)^{4/3}), refuting their Conjecture 2 (the strong Erdős-Szemerédi conjecture); the construction takes A = {uw/v} for positive integers u, v, w scaled by a common denominator, so A consists of positive integers; Theorem 4 gives counterexamples A ⊂ ℕ for every 0 < c < 1, https://web.math.princeton.edu/~nalon/PDFS/sumprodrat7.pdf.

Stated but not proved: `MathlibExt.Combinatorics.GraphRestrictedSumProductErdosProblem808Wanted.restrictedSumProductAlongGraphs_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/GraphRestrictedSumProductErdosProblem808Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GraphRestrictedSumProductErdosProblem808Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-and-products-along-graphs/index.html#restricted-sum-product-along-graphs-refu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums and products along graphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-and-products-along-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/sums-and-products-along-graphs)
