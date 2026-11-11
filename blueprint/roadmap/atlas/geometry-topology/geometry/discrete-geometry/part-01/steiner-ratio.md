---
declaration: section
origin: cited
lean: MathlibExt.Geometry.SteinerRatio.Plane, MathlibExt.Geometry.SteinerRatio.edgeLength, MathlibExt.Geometry.SteinerRatio.totalLength, MathlibExt.Geometry.SteinerRatio.spanningTreeLengths, MathlibExt.Geometry.SteinerRatio.steinerTreeLengths, MathlibExt.Geometry.SteinerRatio.mstLength, MathlibExt.Geometry.SteinerRatio.steinerLength, MathlibExt.Geometry.SteinerRatio.steinerLength_le_mstLength
statement: formalized
---

# Steiner ratio

12 results, 10 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html).

## The Euclidean plane of the Steiner ratio problem

The space $\mathbb{R}^2$ with the
Euclidean distance, in which the point sets of the Steiner ratio problem lie.

Formalized by `MathlibExt.Geometry.SteinerRatio.Plane`, an abbreviation declared in [MathlibExt/Geometry/SteinerRatio.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#plane).

## Length of an edge

For points $x$ and $y$ of the Euclidean plane, the length of the
unordered pair $\{x, y\}$ is the Euclidean distance between $x$ and $y$.

Formalized by `MathlibExt.Geometry.SteinerRatio.edgeLength`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#edge-length).

## Total length of a graph on points of the plane

For a finite set $V$ of points in the
Euclidean plane and a simple graph $G$ with vertex set $V$, the total length of $G$ is the sum,
over all edges $\{x, y\}$ of $G$, of the Euclidean distance between $x$ and $y$.

Formalized by `MathlibExt.Geometry.SteinerRatio.totalLength`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#total-length).

## Lengths of spanning trees

For a finite set $V$ of points in the Euclidean plane, this is
the set of real numbers $\ell$ such that some tree with vertex set $V$ has total length $\ell$,
the total length being the sum of the Euclidean lengths of its edges.

Formalized by `MathlibExt.Geometry.SteinerRatio.spanningTreeLengths`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#spanning-tree-lengths).

## Lengths of Steiner trees

For a finite set $V$ of points in the Euclidean plane, this is
the set of real numbers $\ell$ such that, for some finite set $W$ of points of the plane
containing $V$, some tree with vertex set $W$ has total length $\ell$. The points of $W$
outside $V$ are the Steiner points.

Formalized by `MathlibExt.Geometry.SteinerRatio.steinerTreeLengths`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#steiner-tree-lengths).

## Minimum spanning tree length

For a finite set $V$ of points in the Euclidean plane, the
minimum spanning tree length of $V$ is the infimum of the total lengths of the trees with
vertex set $V$. For nonempty $V$ this set of lengths is finite and nonempty, so the infimum
is a minimum; for empty $V$ the value is $0$ by convention.

Formalized by `MathlibExt.Geometry.SteinerRatio.mstLength`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#mst-length).

## Steiner minimal tree length

For a finite set $V$ of points in the Euclidean plane, the
Steiner length of $V$ is the infimum of the total lengths of the trees whose vertex set is a
finite set of points of the plane containing $V$. This set of lengths is nonempty and bounded
below by $0$, so the infimum exists.

Formalized by `MathlibExt.Geometry.SteinerRatio.steinerLength`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#steiner-length).

## The Steiner length is at most the minimum spanning tree length

For every nonempty
finite set $V$ of points in the Euclidean plane, the Steiner minimal tree length of $V$ is at
most the minimum spanning tree length of $V$: allowing Steiner points never increases the
optimal length.

Formalized by `MathlibExt.Geometry.SteinerRatio.steinerLength_le_mstLength`, a theorem declared in [MathlibExt/Geometry/SteinerRatio.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#steiner-length-le-mst-length).

## The Steiner ratio of the Euclidean plane

The Steiner ratio constant is the infimum,
over all finite sets $V$ of at least two points in the Euclidean plane $\mathbb{R}^2$, of the
ratio of the Steiner minimal tree length of $V$ to the minimum spanning tree length of $V$.

Formalized by `MathlibExt.Geometry.SteinerRatio.steinerRatioConstant`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#steiner-ratio-constant).

## Gilbert–Pollak conjecture

The Steiner ratio of the Euclidean plane, that is, the
infimum of the ratio of the Steiner minimal tree length to the minimum spanning tree length
over all finite sets of at least two points in the plane, equals $\sqrt{3}/2$.

The vertices of an equilateral triangle have ratio exactly $\sqrt{3}/2$, so the conjecture
says that no finite set of at least two points in the plane has a smaller ratio.

Formalized by `MathlibExt.Geometry.SteinerRatio.GilbertPollakConjecture`, a definition declared in [MathlibExt/Geometry/SteinerRatio.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/SteinerRatio.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#gilbert-pollak-conjecture).

## Gilbert–Pollak upper bound for the Steiner ratio

The Steiner ratio constant, the infimum
over finite sets $V$ of at least two points in the Euclidean plane of the length of a Steiner
minimal tree for $V$ divided by the length of a minimum spanning tree of $V$, is at most
$\sqrt{3}/2$.

## Sources

- Gilbert and Pollak, *Steiner minimal trees* (1968): the equilateral triangle gives the upper bound `√3 / 2`.

Stated but not proved: `MathlibExt.Geometry.SteinerRatioWanted.gilbertPollakUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/Geometry/SteinerRatioWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SteinerRatioWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#gilbert-pollak-upper-bound-wanted).

## Chung–Graham lower bound for the Steiner ratio

The Steiner ratio constant, the infimum
over finite sets $V$ of at least two points in the Euclidean plane of the length of a Steiner
minimal tree for $V$ divided by the length of a minimum spanning tree of $V$, is at least $0.824$.

## Sources

- Chung and Graham (1985), via the catalogue's best unconditional published lower bound `0.824` before the conditional 2026 computer-assisted rows.

Stated but not proved: `MathlibExt.Geometry.SteinerRatioWanted.chungGrahamLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/Geometry/SteinerRatioWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/SteinerRatioWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html#chung-graham-lower-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Steiner ratio](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/steiner-ratio)
