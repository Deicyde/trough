---
declaration: section
origin: cited
lean: MetaMathlibExt.angle_bisector_theorem_general, MetaMathlibExt.angle_bisector_theorem, MetaMathlibExt.angle_bisector_converse_general, MetaMathlibExt.angle_bisector_converse
statement: formalized
proof: formalized
---

# Angle bisector theorem

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/angle-bisector-theorem/index.html).

## Angle bisector theorem without distinctness hypotheses

Let $A$, $B$, $C$, $D$ be points of
a Euclidean affine space (a metric affine space over a real inner product space) with $A$, $B$, $C$
affinely independent, so that $ABC$ is a nondegenerate triangle. If $D$ lies strictly between $B$
and $C$ and $\angle BAD = \angle DAC$ (unoriented angles), then $BD / DC = AB / AC$.

The hypotheses $A \ne B$, $A \ne C$ and $A \ne D$ of the usual statement are not needed: they
follow from the others.

Formalized by `MetaMathlibExt.angle_bisector_theorem_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/AngleBisector.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/AngleBisector.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/angle-bisector-theorem/index.html#angle-bisector-theorem-general).

## Angle bisector theorem

Let $A$, $B$, $C$, $D$ be points of a Euclidean affine space (a
metric affine space over a real inner product space) with $A$, $B$, $C$ affinely independent, so
that $ABC$ is a nondegenerate triangle, and with $A \ne B$, $A \ne C$ and $A \ne D$. If $D$ lies
strictly between $B$ and $C$ and $\angle BAD = \angle DAC$ (unoriented angles), then
$BD / DC = AB / AC$.

## Sources

- https://en.wikipedia.org/wiki/Angle_bisector_theorem. It follows from `angle_bisector_theorem_general`; the hypotheses `hAB`, `hAC` and `hAD` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.angle_bisector_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/AngleBisector.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/AngleBisector.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/angle-bisector-theorem/index.html#angle-bisector-theorem).

## Converse of the angle bisector theorem without distinctness hypotheses

Let $A$, $B$, $C$,
$D$ be points of a Euclidean affine space (a metric affine space over a real inner product space)
with $A$, $B$, $C$ affinely independent, so that $ABC$ is a nondegenerate triangle. If $D$ lies on
the closed segment $BC$ and $BD / DC = AB / AC$, then $\angle BAD = \angle DAC$ (unoriented
angles), that is, $D$ lies on the internal bisector of the angle at $A$.

The hypotheses $A \ne B$, $A \ne C$ and $A \ne D$ of the usual statement are not needed: they
follow from the others.

Formalized by `MetaMathlibExt.angle_bisector_converse_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/AngleBisector.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/AngleBisector.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/angle-bisector-theorem/index.html#angle-bisector-converse-general).

## Converse of the angle bisector theorem

Let $A$, $B$, $C$, $D$ be points of a Euclidean
affine space (a metric affine space over a real inner product space) with $A$, $B$, $C$ affinely
independent, so that $ABC$ is a nondegenerate triangle, and with $A \ne B$, $A \ne C$ and
$A \ne D$. If $D$ lies on the closed segment $BC$ and $BD / DC = AB / AC$, then
$\angle BAD = \angle DAC$ (unoriented angles), that is, $D$ lies on the internal bisector of the
angle at $A$.

## Sources

- https://en.wikipedia.org/wiki/Angle_bisector_theorem. It follows from `angle_bisector_converse_general`; the hypotheses `hAB`, `hAC` and `hAD` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.angle_bisector_converse`, a theorem declared in [MathlibExt/Geometry/Euclidean/AngleBisector.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/AngleBisector.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/angle-bisector-theorem/index.html#angle-bisector-converse).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Angle bisector theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/angle-bisector-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/angle-bisector-theorem)
