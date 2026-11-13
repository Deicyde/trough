---
declaration: section
origin: cited
lean: MetaMathlibExt.vanSchooten_general, MetaMathlibExt.vanSchooten
statement: formalized
proof: formalized
---

# Van Schooten's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/van-schooten-s-theorem/index.html).

## Van Schooten's theorem

Let $A$, $B$, $C$, $P$ and $O$ be points of the Euclidean plane
$\mathbb{R}^2$ and let $r > 0$. Suppose that $AB = BC = CA$, that $A$, $B$, $C$ and $P$ lie
on the circle of radius $r$ about $O$, and that $CP > AP$ and $CP > BP$. Then
$PA + PB = PC$.

No hypothesis that $P$ differs from $A$, $B$ or $C$ is needed.

Formalized by `MetaMathlibExt.vanSchooten_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/VanSchooten.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/VanSchooten.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/van-schooten-s-theorem/index.html#van-schooten-general).

## Van Schooten's theorem with distinctness hypotheses

Let $A$, $B$, $C$, $P$ and $O$ be
points of the Euclidean plane $\mathbb{R}^2$ and let $r > 0$. Suppose that $AB = BC = CA$,
that $A$, $B$, $C$ and $P$ lie on the circle of radius $r$ about $O$, that $P \ne A$,
$P \ne B$ and $P \ne C$, and that $CP > AP$ and $CP > BP$. Then $PA + PB = PC$.

In the source, $P$ is a point on the arc $AB$ of the circumcircle not containing $C$; here that
condition is expressed by $CP > AP$ and $CP > BP$.

## Sources

- https://en.wikipedia.org/wiki/Van_Schooten%27s_theorem. It follows from `vanSchooten_general`; the hypotheses `P ≠ A`, `P ≠ B` and `P ≠ C` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.vanSchooten`, a theorem declared in [MathlibExt/Geometry/Euclidean/VanSchooten.lean, line 402](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/VanSchooten.lean#L402). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/van-schooten-s-theorem/index.html#van-schooten).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van Schooten's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/van-schooten-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/van-schooten-s-theorem)
