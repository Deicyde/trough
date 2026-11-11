---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.OddDistanceGraphInfiniteChromaticWanted.ODGIC.OddDistanceGraph, MathlibExt.GraphTheory.OddDistanceGraphInfiniteChromaticWanted.ODGIC.OddDistanceChromaticInfinite, MathlibExt.GraphTheory.OddDistanceGraphInfiniteChromaticWanted.OddDistanceChromaticInfinite_holds
statement: formalized
---

# Odd distance graph

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/odd-distance-graph/index.html).

## The odd distance graph

## Odd distance graph

The odd distance graph is the simple graph on the Euclidean plane
$\mathbb{R}^2$ in which two points $x$ and $y$ are adjacent when their Euclidean distance is an
odd integer.

Formalized by `MathlibExt.GraphTheory.OddDistanceGraphInfiniteChromaticWanted.ODGIC.OddDistanceGraph`, a definition declared in [WantedExt/GraphTheory/OddDistanceGraphInfiniteChromaticWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/OddDistanceGraphInfiniteChromaticWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/odd-distance-graph/index.html#odd-distance-graph).

## Infinite chromatic number of the odd distance graph

The proposition that the odd distance
graph on $\mathbb{R}^2$ has infinite chromatic number, that is, has no proper colouring with
finitely many colours.

Formalized by `MathlibExt.GraphTheory.OddDistanceGraphInfiniteChromaticWanted.ODGIC.OddDistanceChromaticInfinite`, a definition declared in [WantedExt/GraphTheory/OddDistanceGraphInfiniteChromaticWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/OddDistanceGraphInfiniteChromaticWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/odd-distance-graph/index.html#odd-distance-chromatic-infinite).

## Davies' odd distance theorem

The odd distance graph on the Euclidean plane $\mathbb{R}^2$,
in which two points are adjacent when their distance is an odd integer, has infinite chromatic
number: it has no proper colouring with finitely many colours.

Davies proves (Theorem 1) that every finite colouring of the plane has a monochromatic pair of
points at odd integer distance.

## Sources

- James Davies, Odd distances in colourings of the plane, Geometric and Functional Analysis 34 (2024) 19-31, arXiv:2209.15598, https://arxiv.org/abs/2209.15598.

Stated but not proved: `MathlibExt.GraphTheory.OddDistanceGraphInfiniteChromaticWanted.OddDistanceChromaticInfinite_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/OddDistanceGraphInfiniteChromaticWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GraphTheory/OddDistanceGraphInfiniteChromaticWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/odd-distance-graph/index.html#odd-distance-chromatic-infinite-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Odd distance graph](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-coloring/part-01/odd-distance-graph/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-coloring/part-01/odd-distance-graph)
