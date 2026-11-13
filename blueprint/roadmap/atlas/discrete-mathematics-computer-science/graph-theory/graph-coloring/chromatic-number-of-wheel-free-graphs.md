---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.hasInducedWheel, MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.wheelFree, MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.largeChromaticTriangleFreeWheelFree, MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.largeChromaticTriangleFreeWheelFree_holds
statement: formalized
---

# Chromatic number of wheel-free graphs

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-wheel-free-graphs/index.html).

## Induced wheels

A simple graph $G$ has an induced wheel if there are a natural
number $\ell \ge 4$, distinct vertices $r_0, \dots, r_{\ell-1}$ of $G$ (the rim) and a vertex
$h$ of $G$ (the hub) with $h \ne r_i$ for every $i$, such that for all $i, j < \ell$ the
vertices $r_i$ and $r_j$ are adjacent in $G$ exactly when $i - j \equiv \pm 1 \pmod{\ell}$,
and $h$ is adjacent to $r_i$, $r_j$ and $r_k$ for some pairwise distinct $i, j, k < \ell$.
The hub may have further neighbours on the rim.

## Sources

- James Davies, *Triangle-free graphs with large chromatic number and no induced wheel*, arXiv:2104.05907v3, page 1, defining paragraph, https://arxiv.org/pdf/2104.05907v3.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.hasInducedWheel`, a definition declared in [WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-wheel-free-graphs/index.html#has-induced-wheel).

## Wheel-free graphs

A simple graph $G$ is wheel-free if it has no induced wheel, that
is, no induced cycle of length at least four together with a vertex outside the cycle that is
adjacent to at least three vertices of the cycle.

## Sources

- James Davies, arXiv:2104.05907v3, page 1, wheel definition, https://arxiv.org/pdf/2104.05907v3.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.wheelFree`, a definition declared in [WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-wheel-free-graphs/index.html#wheel-free).

## Triangle-free wheel-free graphs of large chromatic number (proposition)

This is the
proposition that for every positive integer $k$ there are a natural number $n$ and a simple
graph $G$ on the vertex set $\{0, \dots, n - 1\}$ such that $G$ contains no triangle, $G$ is
wheel-free (it has no induced wheel) and the chromatic number of $G$ is at least $k$.

Since $G$ is finite, its chromatic number is finite.

## Sources

- Davies, arXiv:2104.05907v3, Corollary 2, page 1; the finite constructions are given on pages 5 and 6, https://arxiv.org/pdf/2104.05907v3.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.largeChromaticTriangleFreeWheelFree`, a definition declared in [WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-wheel-free-graphs/index.html#large-chromatic-triangle-free-wheel-free).

## Davies's theorem on triangle-free wheel-free graphs

For every positive integer $k$
there are a natural number $n$ and a simple graph $G$ on the vertex set $\{0, \dots, n - 1\}$
such that $G$ contains no triangle, $G$ is wheel-free (it has no induced wheel) and the
chromatic number of $G$ is at least $k$.

## Sources

- James Davies, arXiv:2104.05907v3, Corollary 2, page 1, https://arxiv.org/pdf/2104.05907v3.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.DaviesWheelFreeChromaticWanted.largeChromaticTriangleFreeWheelFree_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SimpleGraph/DaviesWheelFreeChromaticWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-wheel-free-graphs/index.html#large-chromatic-triangle-free-wheel-free-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chromatic number of wheel-free graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-wheel-free-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/graph-coloring/part-01/chromatic-number-of-wheel-free-graphs)
