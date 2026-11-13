---
declaration: section
origin: cited
lean: Manifold.riemannianGradient, Manifold.inner_riemannianGradient, Manifold.riemannianGradient_eq_iff, Manifold.norm_riemannianGradient, Manifold.hessian, Manifold.riemannianGradient_vectorSpace, Manifold.hessian_vectorSpace, Manifold.hessian_vectorSpace_eq_fderiv_fderiv
statement: formalized
proof: formalized
---

# Riemannian gradient and Hessian

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html).

## Riemannian gradient

Let $M$ be a $C^1$ manifold modelled on a complete real normed
space, with a Riemannian metric, and let $f : M \to \mathbb{R}$ and $x \in M$. The Riemannian
gradient $\operatorname{grad} f(x) = (df_x)^\sharp \in T_xM$ is the image of the differential
$df_x$ of $f$ at $x$ under the inverse of the Riesz isomorphism
$T_xM \to (T_xM)^*$, $w \mapsto \langle w, \cdot \rangle$, given by the metric at $x$. It is the
unique tangent vector with $\langle \operatorname{grad} f(x), v \rangle = df_x(v)$ for all
$v \in T_xM$.

Formalized by `Manifold.riemannianGradient`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#riemannian-gradient).

## Pairing of the Riemannian gradient with a tangent vector

Let $M$ be a $C^1$ manifold
modelled on a complete real normed space, with a Riemannian metric $\langle \cdot, \cdot \rangle$,
and let $f : M \to \mathbb{R}$, $x \in M$ and $v \in T_xM$. Then
$\langle \operatorname{grad} f(x), v \rangle = df_x(v)$, where $\operatorname{grad} f(x)$ is the
Riemannian gradient of $f$ at $x$ and $df_x$ is the differential of $f$ at $x$.

Formalized by `Manifold.inner_riemannianGradient`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#inner-riemannian-gradient).

## Characterization of the Riemannian gradient

Let $M$ be a $C^1$ manifold modelled on a
complete real normed space, with a Riemannian metric $\langle \cdot, \cdot \rangle$, and let
$f : M \to \mathbb{R}$, $x \in M$ and $w \in T_xM$. Then the Riemannian gradient
$\operatorname{grad} f(x)$ equals $w$ if and only if $\langle w, v \rangle = df_x(v)$ for every
$v \in T_xM$, where $df_x$ is the differential of $f$ at $x$.

Formalized by `Manifold.riemannianGradient_eq_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#riemannian-gradient-eq-iff).

## Norm of the Riemannian gradient

Let $M$ be a $C^1$ manifold modelled on a complete real
normed space, with a Riemannian metric, and let $f : M \to \mathbb{R}$ and $x \in M$. With $T_xM$
normed by the metric at $x$, the norm of the Riemannian gradient $\operatorname{grad} f(x)$ equals
the operator norm of the differential $df_x : T_xM \to \mathbb{R}$ of $f$ at $x$:
$\|\operatorname{grad} f(x)\| = \|df_x\|$. This is the quantity $|\nabla f|(x)$.

Formalized by `Manifold.norm_riemannianGradient`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#norm-riemannian-gradient).

## Covariant Hessian

Let $M$ be a smooth manifold modelled on a finite-dimensional real
normed space, with a smooth Riemannian metric and its Levi-Civita connection $\nabla$. For
$f : M \to \mathbb{R}$, a point $x \in M$ and tangent vectors $u, v \in T_xM$, let $V$ be the
extension of $v$ to a vector field with constant coordinates in the preferred chart at $x$, so
that $V(x) = v$. The Hessian of $f$ at $x$ is the real number

$$\nabla^2 f(u, v) = d\big(y \mapsto df_y(V(y))\big)_x(u) - df_x(\nabla_u V),$$

that is, $u(Vf) - df_x(\nabla_u V)$, where $df_y$ is the differential of $f$ at $y$.

This is the textbook Hessian $\nabla^2 f = \nabla(df)$, $\nabla^2 f(u, v) = (\nabla_u df)(v)$
(Lee, *Introduction to Riemannian Manifolds*, 2nd ed., GTM 176, Ch. 4), taken as a function of two tangent vectors.

Formalized by `Manifold.hessian`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#hessian).

## The Riemannian gradient on a Hilbert space

Let $F$ be a real Hilbert space, viewed as
a Riemannian manifold with the metric given by its inner product, and let $f : F \to \mathbb{R}$
and $x \in F$. Identifying the tangent space at $x$ with $F$, the Riemannian gradient of $f$ at
$x$ is the Hilbert-space gradient $\nabla f(x)$, the unique vector with
$\langle \nabla f(x), w \rangle = Df(x)(w)$ for all $w \in F$, where $Df(x)$ is the Fréchet
derivative of $f$ at $x$.

Formalized by `Manifold.riemannianGradient_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#riemannian-gradient-vector-space).

## The Hessian on Euclidean space as an iterated directional derivative

Let $F$ be a
finite-dimensional real inner product space, viewed as a Riemannian manifold with the metric
given by its inner product, let $f : F \to \mathbb{R}$ and let $x \in F$. For all tangent vectors
$u, v$ at $x$, identified with vectors of $F$, the Hessian of $f$ at $x$ is the derivative at $x$
in direction $u$ of the function $y \mapsto Df(y)(v)$, where $Df(y)$ is the Fréchet derivative of
$f$ at $y$: $\nabla^2 f(u, v) = D\big(y \mapsto Df(y)(v)\big)(x)(u)$.

A Fréchet derivative that does not exist is taken to be $0$, so no hypothesis on $f$ is
needed.

Formalized by `Manifold.hessian_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#hessian-vector-space).

## The Hessian on Euclidean space is the second derivative

Let $F$ be a finite-dimensional
real inner product space, viewed as a Riemannian manifold with the metric given by its inner
product, let $f : F \to \mathbb{R}$ and let $x \in F$. If the Fréchet derivative
$y \mapsto Df(y)$ of $f$ is differentiable at $x$, then for all tangent vectors $u, v$ at $x$,
identified with vectors of $F$, the Hessian of $f$ at $x$ is the second Fréchet derivative:
$\nabla^2 f(u, v) = D^2 f(x)(u)(v)$, where $D^2 f(x)$ is the derivative of $Df$ at $x$.

Formalized by `Manifold.hessian_vectorSpace_eq_fderiv_fderiv`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Hessian.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html#hessian-vector-space-eq-fderiv-fderiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemannian gradient and Hessian](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry/riemannian-gradient-and-hessian)
