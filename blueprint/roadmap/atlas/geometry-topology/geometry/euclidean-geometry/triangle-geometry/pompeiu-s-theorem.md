---
declaration: section
origin: cited
lean: MetaMathlibExt.pompeiu_general, MetaMathlibExt.pompeiu
statement: formalized
proof: formalized
---

# Pompeiu's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/pompeiu-s-theorem/index.html).

## Pompeiu's theorem

Write $XY$ for the Euclidean distance between points $X$ and $Y$ of the
Euclidean plane $\mathbb{R}^2$. Let $A$, $B$, $C$ be points of the plane with $AB = BC = CA$ and
$AB > 0$, so that $ABC$ is an equilateral triangle, and let $P$ be any point of the plane. Then
$PA \le PB + PC$, $PB \le PC + PA$ and $PC \le PA + PB$; that is, $PA$, $PB$, $PC$ are the side
lengths of a (possibly degenerate) triangle.

Formalized by `MetaMathlibExt.pompeiu_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/Pompeiu.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/Pompeiu.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/pompeiu-s-theorem/index.html#pompeiu-general).

## Pompeiu's theorem for a point other than a vertex

Write $XY$ for the Euclidean distance
between points $X$ and $Y$ of the Euclidean plane $\mathbb{R}^2$. Let $A$, $B$, $C$ be points of
the plane with $AB = BC = CA$ and $AB > 0$, so that $ABC$ is an equilateral triangle, and let $P$
be a point of the plane with $P \ne A$, $P \ne B$ and $P \ne C$. Then $PA \le PB + PC$,
$PB \le PC + PA$ and $PC \le PA + PB$; that is, $PA$, $PB$, $PC$ are the side lengths of a
(possibly degenerate) triangle.

The hypothesis that $P$ is not a vertex is not needed: the conclusion holds for every point $P$
of the plane.

## Sources

- https://en.wikipedia.org/wiki/Pompeiu%27s_theorem.

Formalized by `MetaMathlibExt.pompeiu`, a theorem declared in [MathlibExt/Geometry/Euclidean/Pompeiu.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/Pompeiu.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/pompeiu-s-theorem/index.html#pompeiu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pompeiu's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/pompeiu-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/pompeiu-s-theorem)
