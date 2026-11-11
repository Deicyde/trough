---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.K5FreeTriangleFreeSubsetWanted.conjecture, MathlibExt.Combinatorics.K5FreeTriangleFreeSubsetWanted.conjecture_refuted, MathlibExt.GraphTheory.ErdosProblem22Wanted.conjecture, MathlibExt.GraphTheory.ErdosProblem22Wanted.test_bot, MathlibExt.GraphTheory.ErdosProblem22Wanted.conjecture_holds
statement: formalized
---

# Ramsey–Turán theory

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory/index.html).

## EP-533: linear triangle-free sets in dense $K_5$-free graphs

The conjecture states that
for every real $\delta > 0$ there is a real $c > 0$ such that, for all sufficiently large $n$,
every $K_5$-free simple graph on $n$ vertices with at least $\delta n^2$ edges has a
triangle-free set of at least $c n$ vertices (a set of vertices no three of which are pairwise
adjacent).

Formalized by `MathlibExt.Combinatorics.K5FreeTriangleFreeSubsetWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/K5FreeTriangleFreeSubsetWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/K5FreeTriangleFreeSubsetWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory/index.html#conjecture).

## EP-533 is false: dense $K_5$-free graphs without linear triangle-free sets

There is a real
$\delta > 0$ such that for every real $c > 0$ there are infinitely many $n$ for which some
$K_5$-free simple graph on $n$ vertices has at least $\delta n^2$ edges and yet has no
triangle-free set of at least $c n$ vertices (a set of vertices no three of which are pairwise
adjacent). In other words, the EP-533 conjecture fails.

Balogh and Lenz (2011) first gave $K_5$-free graphs of positive density with no linear
triangle-free set; Liu, Reiher, Sharifzadeh and Staden (Theorem 1.1 with $p = 3$, $\ell = 1$)
give $K_5$-free graphs on $2n$ vertices with $(1/3 - o(1))n^2$ edges whose largest
triangle-free set has $o(n)$ vertices, refuting $\delta = 1/24$.

## Sources

- Hong Liu, Christian Reiher, Maryam Sharifzadeh and Katherine Staden, Geometric constructions for Ramsey–Turán theory, J. Eur. Math. Soc. 28 (2026), arXiv:2103.10423, https://arxiv.org/abs/2103.10423.

Stated but not proved: `MathlibExt.Combinatorics.K5FreeTriangleFreeSubsetWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/K5FreeTriangleFreeSubsetWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/K5FreeTriangleFreeSubsetWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory/index.html#conjecture-refuted).

## Ramsey–Turán problem for $K_4$ (Erdős Problem 22)

For a graph $G$ write $\alpha(G)$ for
its independence number and $e(G)$ for its number of edges, and call $G$ $K_4$-free if it has no
four pairwise adjacent vertices. The statement is the conjunction of the following four
assertions.

(i) For every real $\varepsilon > 0$ and all sufficiently large $n$, there is a $K_4$-free graph
$G$ on $n$ vertices with $\alpha(G) \le \varepsilon n$ and $e(G) \ge n^2/8$.

(ii) (Szemerédi's upper bound.) For every real $\varepsilon > 0$ there is a real $\delta > 0$ such
that, for all sufficiently large $n$, every $K_4$-free graph $G$ on $n$ vertices with
$\alpha(G) \le \delta n$ satisfies $e(G) \le (1/8 + \varepsilon) n^2$.

(iii) (Bollobás–Erdős lower bound.) For all real $\varepsilon > 0$ and $\delta > 0$ and all
sufficiently large $n$, there is a $K_4$-free graph $G$ on $n$ vertices with
$\alpha(G) \le \delta n$ and $e(G) \ge (1/8 - \varepsilon) n^2$.

(iv) (Fox–Loh–Zhao quantitative form.) There is a real $C > 0$ such that, for all sufficiently
large $n$, there is a $K_4$-free graph $G$ on $n$ vertices with $e(G) \ge n^2/8$ and
$\alpha(G) \le C n (\log \log n)^{3/2} / (\log n)^{1/2}$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem22Wanted.conjecture`, a definition declared in [WantedExt/GraphTheory/ErdosProblem22Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem22Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory/index.html#conjecture-2).

## The empty graph meets the Ramsey–Turán edge bound for $K_4$

For every natural number $n$
and every real $\varepsilon > 0$, the empty graph on $n$ vertices has no four pairwise adjacent
vertices, and its number of edges (namely $0$) is at most $(1/8 + \varepsilon) n^2$.

Formalized by `MathlibExt.GraphTheory.ErdosProblem22Wanted.test_bot`, a theorem declared in [WantedExt/GraphTheory/ErdosProblem22Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem22Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory/index.html#test-bot).

## Resolution of Erdős Problem 22 (Fox–Loh–Zhao)

For a graph $G$ write $\alpha(G)$ for its
independence number and $e(G)$ for its number of edges, and call $G$ $K_4$-free if it has no four
pairwise adjacent vertices. All four of the following assertions hold.

(i) For every real $\varepsilon > 0$ and all sufficiently large $n$, there is a $K_4$-free graph
$G$ on $n$ vertices with $\alpha(G) \le \varepsilon n$ and $e(G) \ge n^2/8$.

(ii) (Szemerédi's upper bound.) For every real $\varepsilon > 0$ there is a real $\delta > 0$ such
that, for all sufficiently large $n$, every $K_4$-free graph $G$ on $n$ vertices with
$\alpha(G) \le \delta n$ satisfies $e(G) \le (1/8 + \varepsilon) n^2$.

(iii) (Bollobás–Erdős lower bound.) For all real $\varepsilon > 0$ and $\delta > 0$ and all
sufficiently large $n$, there is a $K_4$-free graph $G$ on $n$ vertices with
$\alpha(G) \le \delta n$ and $e(G) \ge (1/8 - \varepsilon) n^2$.

(iv) (Fox–Loh–Zhao quantitative form.) There is a real $C > 0$ such that, for all sufficiently
large $n$, there is a $K_4$-free graph $G$ on $n$ vertices with $e(G) \ge n^2/8$ and
$\alpha(G) \le C n (\log \log n)^{3/2} / (\log n)^{1/2}$.

## Sources

- Jacob Fox, Po-Shen Loh, and Yufei Zhao, The critical window for the classical Ramsey-Turán problem, Combinatorica 35 (2015), 435–476.

Stated but not proved: `MathlibExt.GraphTheory.ErdosProblem22Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/ErdosProblem22Wanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/ErdosProblem22Wanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramsey–Turán theory](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-ramsey-theory/ramsey-tur-n-theory)
