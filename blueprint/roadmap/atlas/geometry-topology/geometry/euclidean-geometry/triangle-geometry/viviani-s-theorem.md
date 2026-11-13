---
declaration: section
origin: cited
lean: MetaMathlibExt.viviani_general, MetaMathlibExt.viviani
statement: formalized
proof: formalized
---

# Viviani's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/viviani-s-theorem/index.html).

## Viviani's theorem

Let $A$, $B$, $C$ be points of the Euclidean plane $\mathbb{R}^2$ with
$AB = BC = CA$, and let $P$ be a point of the interior of the convex hull of
$\lbrace A, B, C \rbrace$. Then the sum of the distances from $P$ to the lines $AB$, $BC$ and
$CA$ equals the distance from $A$ to the line $BC$, the altitude of the triangle.

No positivity hypothesis on the side length is needed: since $P$ is an interior point, the
points $A$, $B$, $C$ are affinely independent, so the triangle is nondegenerate.

Proof: Following the barycentric-coordinate area decomposition in Wikipedia, "Viviani's theorem"
(Proof section), we express the three distances as barycentric weights times a common height.

## Sources

- https://en.wikipedia.org/wiki/Viviani%27s_theorem.

Formalized by `MetaMathlibExt.viviani_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/Viviani.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/Viviani.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/viviani-s-theorem/index.html#viviani-general).

## Viviani's theorem with a positive side length

Let $A$, $B$, $C$ be points of the
Euclidean plane $\mathbb{R}^2$ with $AB = BC = CA$ and $AB > 0$, and let $P$ be a point of the
interior of the convex hull of $\lbrace A, B, C \rbrace$. Then the sum of the distances from
$P$ to the lines $AB$, $BC$ and $CA$ equals the distance from $A$ to the line $BC$, the
altitude of the triangle.

The hypothesis $AB > 0$ is not needed: Viviani's theorem gives the same conclusion without it.

Formalized by `MetaMathlibExt.viviani`, a theorem declared in [MathlibExt/Geometry/Euclidean/Viviani.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/Viviani.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/viviani-s-theorem/index.html#viviani).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Viviani's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/viviani-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/viviani-s-theorem)
