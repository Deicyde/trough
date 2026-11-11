---
declaration: section
origin: cited
lean: Manifold.unitTangentBundle, Manifold.IsGeodesicVelocityCurve, Manifold.IsGeodesicFlow, Manifold.IsUnitGeodesicFlow, Manifold.isGeodesicVelocityCurve_vectorSpace_iff, Manifold.isGeodesicFlow_vectorSpace_iff, Manifold.isUnitGeodesicFlow_vectorSpace_iff
statement: formalized
proof: formalized
---

# Geodesic flow

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html).

## Unit tangent bundle of a Riemannian manifold

The unit tangent bundle `SM` of a Riemannian manifold `(M, g)`: the tangent vectors whose
norm for the installed metric on their fiber is `1`, as a set of `TangentBundle I M` with the
subspace topology. Source: Burns-Matveev, ETDS 41 (2021), §1 ("the unit tangent bundle ... is
denoted by SM").

Formalized by `Manifold.unitTangentBundle`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html#unit-tangent-bundle).

## Geodesic velocity curves

Let $M$ be a $C^2$ manifold (boundary and corners allowed)
modeled on a finite-dimensional real space, with a $C^1$ Riemannian metric
$\langle \cdot, \cdot \rangle$ and Levi-Civita connection $\nabla$. A curve
$u : \mathbb{R} \to TM$, with base curve $\gamma$ ($\gamma(t)$ is the base point of $u(t)$), is a
geodesic velocity curve when for every $t \in \mathbb{R}$: $\gamma$ is differentiable at $t$ with
velocity $\gamma'(t) = u(t)$; and for every vector field $W$ on $M$ that is differentiable at
$\gamma(t)$, the function $s \mapsto \langle u(s), W(\gamma(s)) \rangle$ has derivative
$\langle u(t), \nabla_{u(t)} W \rangle$ at $t$.

The second condition is the weak form of the geodesic equation $\nabla_{\gamma'} \gamma' = 0$:
by metric compatibility, $\frac{d}{dt} \langle \gamma', W \circ \gamma \rangle =
\langle \nabla_{\gamma'} \gamma', W \rangle + \langle \gamma', \nabla_{\gamma'} W \rangle$, and the
values $W(\gamma(t))$ exhaust the tangent space. The two conditions force $\gamma$ to be $C^2$ in
charts, where the weak form is equivalent to $\nabla_{\gamma'} \gamma' = 0$; no further
smoothness of the curve is assumed.

Formalized by `Manifold.IsGeodesicVelocityCurve`, a structure declared in [MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html#is-geodesic-velocity-curve).

## Geodesic flow on the tangent bundle

Let $M$ be a $C^2$ manifold (boundary and corners
allowed) modeled on a finite-dimensional real space, with a $C^1$ Riemannian metric $g$. A
family of maps $\varphi_t : TM \to TM$, $t \in \mathbb{R}$, is a geodesic flow of $g$ when
$\varphi_0(v) = v$ for every $v \in TM$, $\varphi_{t+s}(v) = \varphi_t(\varphi_s(v))$ for all
$t, s \in \mathbb{R}$ and $v \in TM$, and for every $v \in TM$ the orbit $t \mapsto \varphi_t(v)$
is a geodesic velocity curve. Then $\varphi_t(v) = \gamma_v'(t)$ for a geodesic $\gamma_v$ with
initial velocity $v$.

The definition characterizes the flow and does not assert that one exists or is unique. For a
$C^\infty$ metric on a boundaryless manifold, uniqueness is classical, and the global flow exists
when the metric is also complete. No continuity, smoothness or conservation of speed is assumed.

Formalized by `Manifold.IsGeodesicFlow`, a structure declared in [MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html#is-geodesic-flow).

## Geodesic flow on the unit tangent bundle

Let $M$ be a $C^2$ manifold (boundary and
corners allowed) modeled on a finite-dimensional real space, with a $C^1$ Riemannian metric $g$
and unit tangent bundle $SM$. A family of maps $\varphi_t : SM \to SM$, $t \in \mathbb{R}$, is a
geodesic flow on $SM$ when $\varphi_0(v) = v$ for every $v \in SM$,
$\varphi_{t+s}(v) = \varphi_t(\varphi_s(v))$ for all $t, s \in \mathbb{R}$ and $v \in SM$, and
for every $v \in SM$ the orbit $t \mapsto \varphi_t(v)$, viewed as a curve in $TM$, is a
geodesic velocity curve. This is the geodesic flow $\varphi_t$ on $SM$ of Burns–Matveev §1:
the orbit of $v$ is the velocity curve of a unit-speed geodesic $\gamma_v$ with initial
velocity $v$.

The definition characterizes the flow and does not assert that one exists or is unique. For a
$C^\infty$ metric on a boundaryless manifold, uniqueness is classical, and the global flow exists
when the metric is also complete. No continuity, smoothness or conservation of speed is assumed.

Formalized by `Manifold.IsUnitGeodesicFlow`, a structure declared in [MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html#is-unit-geodesic-flow).

## Geodesic velocity curves in Euclidean space

Let $F$ be a finite-dimensional real inner
product space, viewed as a Riemannian manifold with the metric given by its inner product, and
identify each tangent space of $F$ with $F$, so that a point of the tangent bundle $TF$ is a pair
$(x, v)$ with $x, v \in F$. A curve $t \mapsto u(t) = (x(t), v(t))$ in $TF$, defined for all real
$t$, is the velocity curve of a geodesic if and only if, for every real $t$,
$x(t) = x(0) + t\,v(0)$ and $v(t) = v(0)$.

Formalized by `Manifold.isGeodesicVelocityCurve_vectorSpace_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow/VectorSpace.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow/VectorSpace.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html#is-geodesic-velocity-curve-vector-space).

## The geodesic flow of Euclidean space is the straight-line flow

Let $F$ be a
finite-dimensional real inner product space, viewed as a Riemannian manifold with the metric given
by its inner product, and identify each tangent space of $F$ with $F$, so that a point of the
tangent bundle $TF$ is a pair $(x, v)$ with $x, v \in F$. A family of maps
$\varphi_t \colon TF \to TF$, $t \in \mathbb{R}$, is a geodesic flow on $TF$ if and only if
$\varphi_t(x, v) = (x + t v, v)$ for every real $t$ and every $(x, v) \in TF$.

Formalized by `Manifold.isGeodesicFlow_vectorSpace_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow/VectorSpace.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow/VectorSpace.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html#is-geodesic-flow-vector-space-iff).

## The unit geodesic flow of Euclidean space is the straight-line flow

Let $F$ be a
finite-dimensional real inner product space, viewed as a Riemannian manifold with the metric given
by its inner product, and identify each tangent space of $F$ with $F$, so that a point of the
tangent bundle is a pair $(x, v)$ with $x, v \in F$, and the unit tangent bundle $SF$ consists of
the pairs with $\|v\| = 1$. A family of maps $\varphi_t \colon SF \to SF$, $t \in \mathbb{R}$, is
a geodesic flow on $SF$ if and only if $\varphi_t(x, v) = (x + t v, v)$ for every real $t$ and
every $(x, v) \in SF$.

Formalized by `Manifold.isUnitGeodesicFlow_vectorSpace_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow/VectorSpace.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/GeodesicFlow/VectorSpace.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html#is-unit-geodesic-flow-vector-space-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geodesic flow](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/geodesic-flow/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/geodesic-flow)
