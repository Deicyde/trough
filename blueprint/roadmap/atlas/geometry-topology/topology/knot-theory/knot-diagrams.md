---
declaration: section
origin: cited
lean: MathlibExt.Topology.Knot.RegularProjection.DartDiagram, MathlibExt.Topology.Knot.RegularProjection.DartDiagram.Dart, MathlibExt.Topology.Knot.RegularProjection.DartDiagram.crossingCount, MathlibExt.Topology.Knot.RegularProjection.DartDiagram.rot, MathlibExt.Topology.Knot.RegularProjection.DartDiagram.opposite, MathlibExt.Topology.Knot.RegularProjection.DartDiagram.isOver, MathlibExt.Topology.Knot.RegularProjection.DartDiagram.pairPerm, MathlibExt.Topology.Knot.RegularProjection.DartDiagram.rotPerm
statement: formalized
proof: formalized
---

# Knot diagrams

64 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html).

## Regular Projection

## Dart diagram

A dart diagram consists of a finite set $V$ of crossings, a
fixed-point-free involution $\mathrm{pair}$ of the set $V \times \{0, 1, 2, 3\}$ of darts, and a
natural number counting isolated crossingless components.

Darts $0, 1, 2, 3$ at a crossing are read in counterclockwise order, darts $0$ and $2$ form the
over-strand and darts $1$ and $3$ the under-strand, and $\mathrm{pair}$ glues darts across edge
segments. The structure does not by itself assert planarity.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram`, a structure declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#dart-diagram).

## Darts of a dart diagram

The darts of a dart diagram $D$ with crossing set $V$ are the
pairs $(v, i)$ with $v \in V$ and $i \in \{0, 1, 2, 3\}$; the dart $(v, i)$ is the $i$-th
incident half-edge at the crossing $v$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.Dart`, an abbreviation declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#dart).

## Number of crossings of a dart diagram

The crossing count of a dart diagram $D$ is the
number of vertices of $D$, each vertex being one crossing.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.crossingCount`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-count).

## Rotation of a dart

For a dart diagram $D$, the rotation of a dart $(v, i)$ of $D$, with
$v$ a crossing and $i \in \mathbb{Z}/4$, is the dart $(v, i + 1)$: one step counterclockwise
around the crossing $v$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.rot`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#rot).

## Opposite dart

For a dart diagram $D$ and a dart $d = (v, i)$ of $D$, the opposite dart
is obtained by rotating $d$ twice counterclockwise around its crossing $v$; it is the dart
$(v, i + 2)$, with labels taken modulo $4$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.opposite`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#opposite).

## Over-strand darts

The four darts at a crossing of a dart diagram carry the labels
$0, 1, 2, 3$ in cyclic order. A dart lies on the over-strand at its crossing when its label is
$0$ or $2$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.isOver`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-over).

## Edge-pairing permutation

For a dart diagram $D$, the edge-pairing permutation is the
edge-pairing involution of $D$ regarded as a permutation of the darts of $D$; it is its own
inverse.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.pairPerm`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#pair-perm).

## Rotation permutation of darts

For a dart diagram $D$, the rotation permutation is the
permutation of the darts of $D$ sending a dart $(v, i)$, with $v$ a crossing and
$i \in \mathbb{Z}/4$, to $(v, i + 1)$; its inverse sends $(v, i)$ to $(v, i - 1)$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.rotPerm`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#rot-perm).

## Opposite-dart permutation

For a dart diagram $D$, the opposite-dart permutation of the
darts of $D$ is the square of the quarter-turn rotation permutation: it sends the dart $(v, i)$
at crossing $v$ to the dart $(v, i + 2)$, with labels taken modulo $4$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.oppositePerm`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#opposite-perm).

## Strand traversal step

For a dart diagram $D$ and a dart $d$ of $D$, the next dart
after $d$ is the dart opposite $\mathrm{pair}(d)$ at its crossing, where $\mathrm{pair}$ is
the edge-pairing involution of $D$: cross the edge segment at $d$, then go straight through
the crossing reached.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.next`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#next).

## Strand traversal permutation

For a dart diagram $D$, the strand traversal permutation
of the darts of $D$ is the edge-pairing permutation followed by the opposite-dart permutation:
it sends a dart $d$ to the dart opposite $\mathrm{pair}(d)$ at its crossing, where
$\mathrm{pair}$ is the edge-pairing involution of $D$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.nextPerm`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#next-perm).

## A traversal step stays in its strand cycle

Let $D$ be a dart diagram, and for a dart
$d$ of $D$ let $\operatorname{next}(d)$ be the dart reached from $d$ by crossing its edge
segment and then going straight through the next crossing. Then for every dart $d$ of $D$, the
darts $d$ and $\operatorname{next}(d)$ lie in the same cycle of the strand traversal
permutation of $D$, the permutation of the darts of $D$ that sends each dart $e$ to
$\operatorname{next}(e)$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.sameCycle_next`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#same-cycle-next).

## Alternating dart diagrams

A dart diagram is alternating when, for every dart $d$, the
dart $\operatorname{next}(d)$, reached from $d$ by crossing its edge segment and going straight
through the next crossing, has the opposite over/under status to $d$. In other words, consecutive
crossings on every strand have opposite over/under status.

Crossingless components impose no condition.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.IsAlternating`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-alternating).

## Same component relation on darts

For a dart diagram $D$, two darts of $D$ lie in the
same component when they are related by the equivalence relation on darts generated by
$d \sim \operatorname{pair}(d)$, crossing an edge segment, and $d \sim \operatorname{opposite}(d)$,
going straight through a crossing.

The oriented traversal $\operatorname{next}$ traverses every component twice, once in each
orientation, so the cycles of the traversal permutation are not themselves the components.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.SameComponent`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#same-component).

## Strand-connectivity relation on darts

For a dart diagram $D$, this is the equivalence
relation on the darts of $D$ generated by relating each dart $d$ to its partner across an edge
segment and to the opposite dart of $d$ at the same crossing. Two darts are related exactly when
they lie on the same unoriented strand component.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.componentSetoid`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#component-setoid).

## A traversal step stays in the same component

For every dart $d$ of a dart diagram $D$,
the dart $\operatorname{next}(d)$ reached by one step of strand traversal lies in the same
component as $d$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.sameComponent_next`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#same-component-next).

## Number of components of a dart diagram

The number of components of a dart diagram $D$ is
the number of classes of darts of $D$ under unoriented strand connectivity, plus the recorded
number of isolated crossingless components of $D$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.componentCount`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#component-count).

## Isolated components are counted in the component count

For every dart diagram $D$,
the number of isolated crossingless components recorded in $D$ is at most the number of
components of $D$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.isolated_le_componentCount`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#isolated-le-component-count).

## Empty dart diagram

For a natural number $k$, the empty dart diagram with $k$ isolated
components has no crossings, hence no darts, and records $k$ isolated crossingless components.

It is alternating, since the alternating condition is vacuous when there are no darts.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.DartDiagram.empty`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#empty).

## Euclidean plane

The space $\mathbb{R}^2$ with its Euclidean inner product and norm, the
target plane of the fixed standard projection frame.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.R2`, an abbreviation declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#r2).

## Standard projection to the plane

The standard projection sends a point
$x = (x_0, x_1, x_2)$ of Euclidean 3-space to the point $(x_0, x_1)$ of the Euclidean plane,
forgetting the third coordinate.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.plane`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#plane).

## Height in the standard projection frame

The height of a point
$x = (x_1, x_2, x_3)$ of Euclidean 3-space is its third coordinate $x_3$.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.height`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#height).

## Parameter point

For a natural number $n$, a parameter point consists of a component
index $i \in \{0, \dots, n-1\}$ and a real parameter $t$ with $0 \le t < 2\pi$, the fundamental
half-open period. It represents the point at parameter $t$ of component $i$ of a parametrized
link with $n$ components.

Formalized by `MathlibExt.Topology.Knot.RegularProjection.ParamPoint`, a structure declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#param-point).

## Point of a link at a parameter point

For a parametrized link $L$ with components
$\gamma_0, \dots, \gamma_{n-1} \colon \mathbb{R} \to \mathbb{R}^3$ and a parameter point
$a = (i, t)$, with $i < n$ and $t \in [0, 2\pi)$, the point of $L$ at $a$ is
$\gamma_i(t) \in \mathbb{R}^3$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.point`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#point).

## Projected curve of a link component

For a parametrized link $L$ with components
$\gamma_0, \dots, \gamma_{n-1} \colon \mathbb{R} \to \mathbb{R}^3$ and $i < n$, the projected curve
of component $i$ is the map $\mathbb{R} \to \mathbb{R}^2$, $t \mapsto \pi(\gamma_i(t))$, where
$\pi(x_0, x_1, x_2) = (x_0, x_1)$ is the standard projection forgetting the third coordinate.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.projCurve`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#proj-curve).

## Projected point of a link at a parameter point

For a parametrized link $L$ with
components $\gamma_0, \dots, \gamma_{n-1} \colon \mathbb{R} \to \mathbb{R}^3$ and a parameter point
$a = (i, t)$, with $i < n$ and $t \in [0, 2\pi)$, the projected point of $L$ at $a$ is
$\pi(\gamma_i(t)) \in \mathbb{R}^2$, where $\pi(x_0, x_1, x_2) = (x_0, x_1)$ forgets the third
coordinate.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.projPoint`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#proj-point).

## Projected tangent vector

Let $L$ be a parametrized link and let $a$ be a parameter point
of $L$, given by a component $i$ and a parameter $t$. The projected tangent vector of $L$ at $a$
is the vector of $\mathbb{R}^2$ obtained by applying the standard projection
$(x, y, z) \mapsto (x, y)$ to the derivative $\gamma_i'(t)$ of the curve $\gamma_i$ of the
$i$-th component of $L$ at $t$.

This is the projection of the ambient derivative; it is not defined as the derivative of the
projected curve.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.tangent`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#tangent).

## Height of a parameter point

For a parametrized link $L$ with $n$ components and a
parameter point $a$ of $L$, the height of $L$ at $a$ is the height (the third coordinate) of
the point of Euclidean 3-space that $a$ represents on $L$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.heightAt`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#height-at).

## Double points of a link projection

For an oriented labeled parametrized link $L$ with
$n$ components, the double-point set of $L$ is the set of points $p$ of the plane $\mathbb{R}^2$
for which there are two distinct parameter points of $L$ (each a component index together with a
parameter in $[0, 2\pi)$) whose images under the standard projection, which forgets the third
coordinate, both equal $p$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.doublePointSet`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#double-point-set).

## Regular projections

Let $L$ be a parametrized link; a parameter point of $L$ is a
component of $L$ together with a parameter in $[0, 2\pi)$. The standard projection of $L$ to the
plane, which forgets the third coordinate, is regular when the following hold: at every parameter
point, the projection of the velocity vector of the component curve is nonzero; the double-point
set is finite; no three pairwise distinct parameter points have the same projection; and at any
two distinct parameter points with the same projection, the projected velocity vectors are
linearly independent over $\mathbb{R}$.

The condition records no diagram, crossing labels or over/under data. The heights at two distinct
parameter points with the same projection always differ, because each component is injective on
a period and the components are pairwise disjoint.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.IsRegularProjection`, a structure declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-regular-projection).

## Points with the same projection have different heights

Let $L$ be a parametrized link
with $n$ components. If two distinct parameter points $a \ne b$ of $L$ have the same projected
point, then the heights of $L$ at $a$ and at $b$ are different.

This is forced by component injectivity in one period and pairwise disjoint component traces;
over/under is therefore derived from the parametrization rather than chosen.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.heightAt_ne_of_projPoint_eq_of_ne`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#height-at-ne-of-proj-point-eq-of-ne).

## Crossings of a link projection

Let $L$ be a parametrized link with $n$ components. A
crossing of $L$ is a point of the double-point set of $L$, that is, a point $p$ of the plane
$\mathbb{R}^2$ such that two distinct parameter points of $L$ both have image $p$ under the
standard projection forgetting the third coordinate.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.Crossing`, an abbreviation declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing).

## Crossing count of a regular projection

For a parametrized link $L$ whose standard
projection is regular, the crossing count of $L$ is the number of crossings of the projection,
that is, the number of points of its double-point set.

Regularity guarantees that the double-point set is finite, and the value does not depend on the
chosen proof of regularity.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingCount`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-count-2).

## Double points have exactly two preimages

Let $L$ be a parametrized link with $n$
components whose standard projection is regular, and let $p$ be a point of the double-point set
of $L$. Then there are parameter points $a \ne b$ of $L$ whose projected points are both $p$, and
every parameter point of $L$ whose projected point is $p$ is $a$ or $b$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.exists_pair_of_mem_doublePointSet`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#exists-pair-of-mem-double-point-set).

## Being the over-strand preimage of a crossing

Let $L$ be a parametrized link and $p$ a
crossing of its standard projection to the plane. A parameter point $a$ of $L$ is an over point
of $p$ when $a$ projects to $p$ and every other parameter point that projects to $p$ has strictly
smaller height than $a$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.IsOverPoint`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-over-point).

## Being the under-strand preimage of a crossing

Let $L$ be a parametrized link and $p$ a
crossing of its standard projection to the plane. A parameter point $a$ of $L$ is an under point
of $p$ when $a$ projects to $p$ and every other parameter point that projects to $p$ has strictly
greater height than $a$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.IsUnderPoint`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-under-point).

## The over-strand preimage exists and is unique

Let $L$ be a parametrized link with $n$
components whose standard projection is regular, and let $p$ be a crossing of that projection.
There is exactly one parameter point $a$ of $L$ that is an over-strand preimage of $p$: the
projected point of $a$ is $p$, and every other parameter point whose projected point is $p$ has
height strictly less than the height of $a$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.existsUnique_isOverPoint`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#exists-unique-is-over-point).

## The under-strand preimage exists and is unique

Let $L$ be a parametrized link with $n$
components whose standard projection is regular, and let $p$ be a crossing of that projection.
There is exactly one parameter point $a$ of $L$ that is an under-strand preimage of $p$: the
projected point of $a$ is $p$, and every other parameter point whose projected point is $p$ has
height strictly greater than the height of $a$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.existsUnique_isUnderPoint`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#exists-unique-is-under-point).

## Over-strand preimage of a crossing

Let $L$ be a parametrized link with $n$ components
whose standard projection is regular, and let $p$ be a crossing of that projection. The
over-strand preimage of $p$ is the unique parameter point $a$ of $L$ that projects to $p$ and
such that every other parameter point projecting to $p$ has strictly smaller height than $a$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.overPoint`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#over-point).

## Under-strand preimage of a crossing

Let $L$ be a parametrized link whose standard
projection is regular, and let $p$ be a crossing of this projection. The under-strand preimage
of $p$ is the unique parameter point $a$ of $L$ that projects to $p$ and whose height is strictly
less than the height of every other parameter point projecting to $p$; the height of a parameter
point is the third coordinate of the corresponding point of $L$ in $\mathbb{R}^3$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.underPoint`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#under-point).

## Over and under preimages differ

Let $L$ be a parametrized link whose standard projection
is regular, and let $p$ be a crossing of this projection. Then the under-strand preimage of $p$
and the over-strand preimage of $p$ are distinct parameter points of $L$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.underPoint_ne_overPoint`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#under-point-ne-over-point).

## The under-strand lies strictly below the over-strand

Let $L$ be a parametrized link with
$n$ components whose standard projection is regular, and let $p$ be a crossing of that
projection. The height of $L$ at the under-strand preimage of $p$ is strictly less than its
height at the over-strand preimage of $p$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.heightAt_underPoint_lt_overPoint`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#height-at-under-point-lt-over-point).

## The over-strand preimage lies over its crossing

Let $L$ be a parametrized link whose
standard projection is regular, and let $p$ be a crossing of $L$, that is, a point of the
double-point set of its projection. Then the projected point of the over-strand parameter point
at $p$ is $p$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.projPoint_overPoint`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#proj-point-over-point).

## The under-strand preimage lies over its crossing

Let $L$ be a parametrized link whose
standard projection is regular, and let $p$ be a crossing of $L$, that is, a point of the
double-point set of its projection. Then the projected point of the under-strand parameter point
at $p$ is $p$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.projPoint_underPoint`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#proj-point-under-point).

## The over and under preimages exhaust a crossing

Let $L$ be a parametrized link with $n$
components whose standard projection is regular, and let $p$ be a crossing of that projection.
Every parameter point of $L$ whose projected point is $p$ is either the over-strand preimage or
the under-strand preimage of $p$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.eq_overPoint_or_eq_underPoint_of_projPoint_eq`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#eq-over-point-or-eq-under-point-of-proj).

## A crossing-free regular projection has crossing count zero

If a parametrized link $L$ has
a regular standard projection whose double-point set is empty, then the crossing count of $L$ is
$0$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingCount_eq_zero_of_doublePointSet_eq_empty`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-count-eq-zero-of-double-point-s).

## A regular projection with a crossing has positive crossing count

If a parametrized link
$L$ has a regular standard projection with at least one crossing, then the crossing count of $L$
is positive.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingCount_pos_of_crossing`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-count-pos-of-crossing).

## Crossing number of a link

For an oriented labeled parametrized link $L$ with $n$
components, the crossing number of $L$ is the infimum in $\mathbb{N} \cup \{\infty\}$, over all
parametrized links $L'$ with $n$ components that are ambient isotopic to $L$ and whose standard
projection to the plane is regular, of the number of crossings (double points) of that
projection of $L'$. It is $\infty$ when no such $L'$ exists.

Changing the projection direction is absorbed by varying the representative over its isotopy
class.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingNumber`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-number).

## Regular projections of isotopic links bound the crossing number

Let $L$ and $L'$ be
oriented labeled parametrized links with $n$ components, with $L'$ ambient isotopic to $L$, and
suppose the standard projection of $L'$ to the plane is regular. Then the crossing number of $L$
is at most the number of crossings of this projection of $L'$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingNumber_le_of_isotopic_of_isRegularProjection`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-number-le-of-isotopic-of-is-reg).

## A link's own regular projection bounds its crossing number

If the standard projection of
an oriented labeled parametrized link $L$ to the plane is regular, then the crossing number of
$L$ is at most the number of crossings of this projection.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingNumber_le_self_of_isRegularProjection`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 603](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L603). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-number-le-self-of-is-regular-pr).

## Finiteness of the crossing number

Let $L$ and $L'$ be oriented labeled parametrized links
with $n$ components. If $L'$ is ambient isotopic to $L$ and the standard projection of $L'$ to
the plane is regular, then the crossing number of $L$ is finite.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingNumber_lt_top_of_isotopic_of_isRegularProjection`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-number-lt-top-of-isotopic-of-is).

## The crossing number is an isotopy invariant

If two parametrized links $L_1$ and $L_2$ with
$n$ components are isotopic, then $L_1$ and $L_2$ have the same crossing number.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingNumber_eq_of_isotopic`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-number-eq-of-isotopic).

## Crossing number zero from a crossing-free representative

Let $L$ and $L'$ be parametrized
links with $n$ components such that $L'$ is isotopic to $L$. If the standard projection of $L'$ is
regular and its double-point set is empty, then the crossing number of $L$ is $0$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.crossingNumber_eq_zero_of_isotopic_of_doublePointSet_eq_empty`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 638](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L638). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#crossing-number-eq-zero-of-isotopic-of-d).

## Crossing preimages

A parameter point $a$ of a parametrized link $L$ (a component of $L$
together with a parameter in $[0, 2\pi)$) is a crossing preimage when its image under the
standard projection to the plane lies in the double-point set of $L$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.IsCrossingPreimage`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-crossing-preimage).

## Over/under status at a crossing preimage

Let $L$ be a parametrized link whose standard
projection to the plane is regular, and let $a$ be a crossing preimage of $L$. The over/under
status at $a$ is true when $a$ is the over-strand preimage of the crossing at the projection of
$a$, that is, the preimage of that crossing of greatest height, and false otherwise.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.isOverAt`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 656](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L656). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-over-at).

## The two preimages of a crossing have opposite status

Let $L$ be a parametrized link
whose standard projection to the plane is regular. If $a \ne b$ are crossing preimages of $L$ with
the same projection, then the over/under status at $a$ differs from the over/under status at $b$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.isOverAt_ne_of_ne_of_projPoint_eq`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-over-at-ne-of-ne-of-proj-point-eq).

## Open arc on the parameter circle

Let $a$, $b$, $c$ be parameter points with parameters
$s$, $u$, $t \in [0, 2\pi)$ respectively. Then $c$ lies in the open counterclockwise arc from $a$
to $b$ when $s < t < u$ in case $s < u$, and when $s < t$ or $t < u$ in case $u \le s$. Only the
parameters are compared; the components of $a$, $b$, $c$ play no role.

Formalized by `MathlibExt.Topology.Knot.Euclidean.inOpenArc`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#in-open-arc).

## Cyclically adjacent crossing preimages

Let $L$ be an oriented labeled parametrized link,
with each component parametrized by $t \in [0, 2\pi)$. Two distinct parameter points $a$ and $b$
of $L$ on the same component are cyclically adjacent, in this order, when both are crossing
preimages (they project to double points of the standard projection) and no crossing preimage on
that component lies in the open arc from $a$ to $b$ in the direction of increasing parameter,
wrapping around from $2\pi$ to $0$ when the parameter of $b$ is smaller than that of $a$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.CyclicallyAdjacent`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#cyclically-adjacent).

## Alternating regular projections

Let $L$ be a parametrized link whose standard projection
to the plane is regular. The projection is alternating when, for any two cyclically adjacent
crossing preimages $a$ and $b$ of $L$ (distinct, on the same component, with no other crossing
preimage of that component in the open arc of parameters from $a$ to $b$), the over/under status
at $a$ differs from the over/under status at $b$.

A component with at most one crossing preimage imposes no condition.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.IsAlternatingProjection`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 722](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L722). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-alternating-projection).

## Crossingless regular projections are alternating

Let $L$ be a parametrized link whose
standard projection to the plane is regular. If the double-point set of this projection is empty,
then the projection is alternating.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.isAlternatingProjection_of_doublePointSet_eq_empty`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#is-alternating-projection-of-double-poin).

## Links admitting an alternating diagram

A parametrized link $L$ with $n$ components admits
an alternating diagram when there is a parametrized link $L'$ isotopic to $L$ whose standard
projection is regular and alternating.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.AdmitsAlternatingDiagram`, a definition declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#admits-alternating-diagram).

## Admitting an alternating diagram is an isotopy invariant

Let $L_1$ and $L_2$ be
parametrized links with $n$ components. If $L_1$ is isotopic to $L_2$ and $L_1$ admits an
alternating diagram, then $L_2$ admits an alternating diagram.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.AdmitsAlternatingDiagram.of_isotopic`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 747](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L747). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#of-isotopic).

## Links with a crossing-free regular projection admit alternating diagrams

If a
parametrized link $L$ has a regular standard projection whose double-point set is empty, then
$L$ admits an alternating diagram.

The witness is $L$ itself, whose projection is alternating vacuously since it has no crossings.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.admitsAlternatingDiagram_of_doublePointSet_eq_empty`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 756](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L756). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#admits-alternating-diagram-of-double-poi).

## The projected trace is the union of the projected components

For a parametrized link
$L$ with $n$ components, the union over all components $i$ of the images of the projected curves
of $L$ equals the image of the trace of $L$ under the standard projection to the plane.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.iUnion_range_projCurve`, a theorem declared in [MathlibExt/Topology/Knot/RegularProjection.lean, line 765](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/RegularProjection.lean#L765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html#i-union-range-proj-curve).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knot diagrams](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knot-diagrams/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/knot-theory/knot-diagrams)
