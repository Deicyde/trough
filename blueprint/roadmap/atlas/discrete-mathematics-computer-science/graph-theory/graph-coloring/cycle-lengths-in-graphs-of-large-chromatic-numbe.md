---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem751Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem751Wanted.conjecture_refuted, MathlibExt.GraphTheory.ErdosProblem57Wanted.conjecture, MathlibExt.GraphTheory.ErdosProblem57Wanted.conjecture_holds, MathlibExt.GraphTheory.ErdosProblem63Wanted.conjecture, MathlibExt.GraphTheory.ErdosProblem63Wanted.conjecture_holds
statement: formalized
---

# Cycle lengths in graphs of large chromatic number

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html).

## Erdős Problem 751

The statement that both of the following hold:
(i) for every natural number $k$ there is a simple graph $G$ with chromatic number $4$ in
which any two distinct cycle lengths of $G$ differ by at least $k$; (ii) for all natural numbers
$k$ and $g$ there is a simple graph $G$ with chromatic number $4$ and girth at least $g$ in which
any two distinct cycle lengths of $G$ differ by at least $k$.

Formalized by `MathlibExt.Combinatorics.ErdosProblem751Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem751Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem751Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html#conjecture).

## Erdős Problem 751 is false

It is not the case that both of the following hold:
(i) for every natural number $k$ there is a simple graph $G$ with chromatic number $4$ in
which any two distinct cycle lengths of $G$ differ by at least $k$; (ii) for all natural numbers
$k$ and $g$ there is a simple graph $G$ with chromatic number $4$ and girth at least $g$ in which
any two distinct cycle lengths of $G$ differ by at least $k$.

## Sources

- J. A. Bondy and A. Vince, Cycles in a graph whose lengths differ by one or two, Journal of Graph Theory 27 (1998), 11-15, https://doi.org/10.1002/(SICI)1097-0118(199801)27:1%3C11::AID-JGT3%3E3.0.CO;2-J; Jun Gao, Qingyi Huo, Chun-Hung Liu, and Jie Ma, A unified proof of conjectures on cycle lengths in graphs, arXiv:1904.08126v3, https://arxiv.org/abs/1904.08126v3.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem751Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem751Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem751Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html#conjecture-refuted).

## Odd cycle lengths and infinite chromatic number (Erdős Problem 57)

Let $G$ be a graph on
an arbitrary vertex set that has no proper colouring with finitely many colours. Then the family
$(1/\ell)$, indexed by the odd cycle lengths $\ell$ of $G$ (the odd numbers $\ell$ such that $G$
contains a cycle of length $\ell$), is not summable; that is, $\sum_\ell 1/\ell = \infty$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem57Wanted.conjecture`, a definition declared in [WantedExt/GraphTheory/ErdosProblem57Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem57Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html#conjecture-2).

## Resolution of the Erdős–Hajnal odd cycle problem (Liu–Montgomery)

Let $G$ be a graph on
an arbitrary vertex set that has no proper colouring with finitely many colours. Then the family
$(1/\ell)$, indexed by the odd cycle lengths $\ell$ of $G$ (the odd numbers $\ell$ such that $G$
contains a cycle of length $\ell$), is not summable; that is, $\sum_\ell 1/\ell = \infty$.

## Sources

- Hong Liu and Richard Montgomery, A solution to Erdős and Hajnal's odd cycle problem, arXiv:2010.15802 (J. Amer. Math. Soc., doi:10.1090/jams/1018), https://arxiv.org/abs/2010.15802.

Stated but not proved: `MathlibExt.GraphTheory.ErdosProblem57Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/ErdosProblem57Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem57Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html#conjecture-holds).

## Statement of Erdős Problem 63

The proposition that every simple graph $G$ with infinite
chromatic number has cycles of length $2^n$ for infinitely many $n$: for every natural number
$N$ there is some $n \ge N$ such that $G$ contains a cycle of length $2^n$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem63Wanted.conjecture`, a definition declared in [WantedExt/GraphTheory/ErdosProblem63Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem63Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html#conjecture-3).

## Erdős Problem 63 (Liu–Montgomery)

Every simple graph $G$ with infinite chromatic number has
cycles of length $2^n$ for infinitely many $n$: for every natural number $N$ there is some
$n \ge N$ such that $G$ contains a cycle of length $2^n$.

## Sources

- Liu–Montgomery [LiMo20], per erdosproblems.com/63, https://www.erdosproblems.com/63.

Stated but not proved: `MathlibExt.GraphTheory.ErdosProblem63Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/ErdosProblem63Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/ErdosProblem63Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html#conjecture-holds-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cycle lengths in graphs of large chromatic number](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/cycle-lengths-in-graphs-of-large-chromatic-numbe)
