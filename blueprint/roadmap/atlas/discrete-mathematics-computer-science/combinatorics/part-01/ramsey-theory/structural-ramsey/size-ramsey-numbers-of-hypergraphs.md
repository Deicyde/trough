---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.Arrows3, MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.ramsey3, MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.sizeRamsey3, MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.sizeRamseyEqualsBinomial, MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.sizeRamseyEqualsBinomial_refuted
statement: formalized
---

# Size Ramsey numbers of hypergraphs

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs/index.html).

## Hypergraph arrowing the complete 3-uniform hypergraph

Let $H$ be a family of subsets of
$\{0, \dots, N-1\}$ and let $n$ be a natural number. Then $H$ arrows $K_n^{(3)}$ when for every
colouring of the subsets of $\{0, \dots, N-1\}$ with two colours there exist an $n$-element set
$S \subseteq \{0, \dots, N-1\}$ and a colour such that every 3-element subset of $S$ belongs to
$H$ and has that colour.

Formalized by `MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.Arrows3`, a definition declared in [WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs/index.html#arrows3).

## Diagonal 3-uniform Ramsey number

For a natural number $n$, the Ramsey number
$r_3(n, n)$ is the least natural number $N$ such that for every colouring of the subsets of
$\{0, \dots, N-1\}$ with two colours there is an $n$-element set $S \subseteq \{0, \dots, N-1\}$
all of whose 3-element subsets have the same colour.

Formalized by `MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.ramsey3`, a definition declared in [WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs/index.html#ramsey3).

## 3-uniform size Ramsey number

For a natural number $n$, the size Ramsey number
$\hat r_3(n, n)$ is the least natural number $m$ such that for some $N$ there is a 3-uniform
hypergraph $H$ on $\{0, \dots, N-1\}$ with exactly $m$ edges that arrows $K_n^{(3)}$.

Formalized by `MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.sizeRamsey3`, a definition declared in [WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs/index.html#size-ramsey3).

## Dudek–Rödl size Ramsey question

The statement that for every natural number $n$ the
3-uniform size Ramsey number $\hat r_3(n, n)$ equals the binomial coefficient
$\binom{r_3(n, n)}{3}$, where $r_3(n, n)$ is the diagonal 3-uniform Ramsey number (AimPL Graph
Ramsey Theory, Problem 1.08).

Formalized by `MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.sizeRamseyEqualsBinomial`, a definition declared in [WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs/index.html#size-ramsey-equals-binomial).

## The Dudek–Rödl size Ramsey question has a negative answer

It is not true that for every
natural number $n$ the 3-uniform size Ramsey number $\hat r_3(n, n)$ equals the binomial
coefficient $\binom{r_3(n, n)}{3}$, where $r_3(n, n)$ is the diagonal 3-uniform Ramsey number.

McKay shows that the complete 3-uniform hypergraph $K_{13}^{(3)}$ on 13 vertices with one triple
removed cannot be 2-coloured without a monochromatic copy of the complete 3-uniform hypergraph
$K_4^{(3)}$ on 4 vertices; since $r_3(4, 4) = 13$ (McKay and Radziszowski, 1991, recalled in the
same paper) this gives $\hat r_3(4, 4) \le 285 < 286 = \binom{13}{3}$, "which answers Dudek et
al.'s question in the negative".

## Sources

- AimPL: Graph Ramsey Theory, Problem 1.08 [Andrzej Dudek] (Dudek–Rödl), http://aimpl.org/graphramsey/1/ (Question 2.2 of Dudek, La Fleur, Mubayi and Rödl, J. Graph Theory 86 (2017)); resolution: B. D. McKay, A class of Ramsey-extremal hypergraphs, Trans. Comb. 6 (2017), no. 3, 37-43, arXiv:1608.07762, abstract and Section 3 (last paragraph), https://toc.ui.ac.ir/article_21468.html.

Stated but not proved: `MathlibExt.Combinatorics.HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.sizeRamseyEqualsBinomial_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/HypergraphSizeRamseyBinomialAIMCombinatoricsProblem52Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs/index.html#size-ramsey-equals-binomial-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Size Ramsey numbers of hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/structural-ramsey/size-ramsey-numbers-of-hypergraphs)
