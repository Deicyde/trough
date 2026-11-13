---
declaration: section
origin: cited
lean: SimpleGraph.fracCliqueNumber, SimpleGraph.fracChromaticNumber, MetaMathlibExt.FracColouring.IsRegular
statement: formalized
proof: formalized
---

# Fractional coloring

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/fractional-coloring/index.html).

## Fractional clique number

Let $X$ be a graph with finite vertex set $V(X)$. A
*fractional clique* of $X$ is a function $f \colon V(X) \to \mathbb{R}$ with $f(v) \ge 0$ for
every vertex $v$, such that $\sum_{v \in S} f(v) \le 1$ for every independent set $S$ of $X$. The
*weight* of $f$ is $\sum_{v \in V(X)} f(v)$. The *fractional clique number* $\omega^*(X)$ of $X$
is the supremum of the weights of all fractional cliques of $X$.

Formalized by `SimpleGraph.fracCliqueNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/LPRelaxations/FractionalClique.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/LPRelaxations/FractionalClique.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/fractional-coloring/index.html#frac-clique-number).

## Fractional chromatic number

Let $X$ be a graph with finite vertex set $V(X)$. A
*fractional colouring* of $X$ assigns to each set $S$ of vertices of $X$ a real weight
$f(S) \ge 0$, with $f(S) = 0$ unless $S$ is independent, such that $\sum_{S \ni x} f(S) \ge 1$
for every vertex $x$ of $X$, the sum running over all sets of vertices containing $x$. The
*weight* of $f$ is the sum of $f(S)$ over all sets $S$ of vertices of $X$. The *fractional
chromatic number* $\chi^*(X)$ of $X$ is the infimum of the weights of all fractional colourings
of $X$.

Since $f$ vanishes off the independent sets, a fractional colouring is the same as a nonnegative
function on the independent sets of $X$, and both sums run over independent sets only.

Formalized by `SimpleGraph.fracChromaticNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/LPRelaxations/FractionalColouring.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/LPRelaxations/FractionalColouring.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/fractional-coloring/index.html#frac-chromatic-number).

## Regular fractional colouring

Let $X$ be a finite simple graph. A fractional colouring
of $X$ assigns to each set $S$ of vertices of $X$ a real weight $f(S) \ge 0$, with $f(S) = 0$
unless $S$ is independent, such that $\sum_{S \ni x} f(S) \ge 1$ for every vertex $x$, the sum
running over all sets of vertices containing $x$. The fractional colouring $f$ is *regular* if
$\sum_{S \ni x} f(S) = 1$ for every vertex $x$ of $X$. Since $f$ vanishes off the independent
sets, this is the sum of $f$ over the independent sets of $X$ containing $x$.

Formalized by `MetaMathlibExt.FracColouring.IsRegular`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/LPRelaxations/FractionalColouring.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/AlgebraicGraphTheory/LPRelaxations/FractionalColouring.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/fractional-coloring/index.html#is-regular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fractional coloring](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/fractional-coloring/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/fractional-coloring)
