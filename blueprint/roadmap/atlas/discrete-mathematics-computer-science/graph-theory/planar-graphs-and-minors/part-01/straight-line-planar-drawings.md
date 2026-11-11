---
declaration: section
origin: cited
lean: SimpleGraph.Segment, SimpleGraph.IsPlanar
statement: formalized
proof: formalized
---

# Straight-line planar drawings

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/straight-line-planar-drawings/index.html).

## Closed segment in the plane

For points $a$ and $b$ of $\mathbb{R}^2$, the closed segment
from $a$ to $b$ is the set of points $a + t(b - a)$ with $t \in \mathbb{R}$ and $0 \le t \le 1$.

Formalized by `SimpleGraph.Segment`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Planarity.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Planarity.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/straight-line-planar-drawings/index.html#segment).

## Straight-line planar graph

A simple graph $G$ with vertex set $V$ is straight-line
planar if either $V$ is empty or there is an injective map $f$ from $V$ to $\mathbb{R}^2$
such that, for any two different edges $vw$ and $xy$ of $G$, the closed segment from $f(v)$
to $f(w)$ and the closed segment from $f(x)$ to $f(y)$ meet only in points of
$\{f(v), f(w)\} \cap \{f(x), f(y)\}$.

Formalized by `SimpleGraph.IsPlanar`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Planarity.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Planarity.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/straight-line-planar-drawings/index.html#is-planar).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Straight-line planar drawings](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/straight-line-planar-drawings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/straight-line-planar-drawings)
