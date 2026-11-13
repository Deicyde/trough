---
declaration: section
origin: cited
lean: CovariantDerivative.extendCurvature, CovariantDerivative.extendCurvature_antisymm, CovariantDerivative.extendRicci, Manifold.riemannCurvature, Manifold.riemannCurvature_antisymm, Manifold.sectionalCurvature, Manifold.sectionalCurvature_smul_right, Manifold.sectionalCurvature_self
statement: formalized
proof: formalized
---

# Curvature of Riemannian manifolds

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html).

## Curvature expression of a covariant derivative on extensions

Let $\nabla$ be a covariant
derivative on a vector bundle $V$ over a manifold $M$, let $x \in M$, let $u, v \in T_x M$ and let
$\sigma \in V_x$. Let $X$ and $Y$ be the vector fields on $M$ whose coordinates in the preferred
local trivialization of $TM$ at $x$ are constant, equal to those of $u$ and $v$, on the base set
of that trivialization, with a fixed but unspecified value at each point outside it; let $S$ be
the section of $V$ obtained in the same way from $\sigma$ and the preferred local trivialization
of $V$ at $x$. The curvature expression of $\nabla$ at $x$ on $u$, $v$, $\sigma$ is the vector

$$R(u, v)\sigma = \nabla_u (\nabla_Y S) - \nabla_v (\nabla_X S) - \nabla_{[X, Y](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/x)} S \in V_x,$$

where $\nabla_Y S$ is the section $y \mapsto \nabla_{Y(y)} S$ and $[X, Y]$ is the Lie bracket.

When $\nabla$ sends $C^2$ sections to $C^1$ sections (for instance the Levi-Civita connection of a
$C^\infty$ metric), this is the curvature tensor
$R(X, Y) = \nabla_X \nabla_Y - \nabla_Y \nabla_X - \nabla_{[X, Y]}$ applied to $u$, $v$, $\sigma$,
and it does not depend on the extensions. For other connections it can depend on values of
$\nabla$ that the axioms of a covariant derivative leave unconstrained.

Formalized by `CovariantDerivative.extendCurvature`, a definition declared in [MathlibExt/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#extend-curvature).

## Antisymmetry of the curvature expression

For every covariant derivative $\nabla$ on a
vector bundle $V$ over a manifold $M$, every $x \in M$, all $u, v \in T_x M$ and every
$\sigma \in V_x$, the curvature expression $R$ of $\nabla$ on extensions satisfies
$R(u, v)\sigma = -R(v, u)\sigma$.

Formalized by `CovariantDerivative.extendCurvature_antisymm`, a theorem declared in [MathlibExt/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#extend-curvature-antisymm).

## Ricci contraction of the curvature expression

Let $M$ be a manifold modelled on a
finite-dimensional normed space over a nontrivially normed field $\mathbb{K}$, let $\nabla$ be a
covariant derivative on the tangent bundle of $M$, let $R$ be its curvature expression on
extensions, let $x \in M$ and let $v, w \in T_x M$. With $e_1, \dots, e_n$ the fixed basis of
$T_x M$ chosen for every finite-dimensional space and $e_1^*, \dots, e_n^*$ its coordinate
functionals, the Ricci contraction is

$$\operatorname{Ric}(v, w) = \sum_{i=1}^n e_i^*(R(e_i, v) w) \in \mathbb{K},$$

the trace of $z \mapsto R(z, v) w$ computed in that basis (Lang, *Lecture Notes on Riemannian
Geometry*, Def. 2.7). No metric is involved.

When $z \mapsto R(z, v) w$ is linear, as it is for a connection that sends $C^2$ sections to $C^1$
sections, this is its trace and does not depend on the basis.

Formalized by `CovariantDerivative.extendRicci`, a definition declared in [MathlibExt/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/VectorBundle/CovariantDerivative/Curvature.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#extend-ricci).

## Riemann curvature endomorphism

For a point $x$ of a $C^\infty$ Riemannian manifold $(M, g)$
with Levi-Civita connection $\nabla$, and tangent vectors $u, v, w \in T_x M$,

$$R(u, v) w = (\nabla_X \nabla_Y W - \nabla_Y \nabla_X W - \nabla_{[X, Y]} W)(x),$$

where $X$, $Y$, $W$ are the vector fields extending $u$, $v$, $w$ that have constant coordinates
in the preferred chart at $x$. Since the Levi-Civita connection of a $C^\infty$ metric is
$C^\infty$, this is the textbook curvature endomorphism and does not depend on the extensions.

This is the sign convention of [Lang, Def. 2.1] and [Gud, Def. 8.8]; the opposite sign convention
is also common.

Formalized by `Manifold.riemannCurvature`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#riemann-curvature).

## Antisymmetry of the Riemann curvature

Let $(M, g)$ be a $C^\infty$ Riemannian manifold.
Its Riemann curvature endomorphism $R$ is antisymmetric in its first two arguments:
$R(u, v) w = -R(v, u) w$ for every point $x \in M$ and all tangent vectors $u, v, w \in T_x M$.

Formalized by `Manifold.riemannCurvature_antisymm`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#riemann-curvature-antisymm).

## Sectional curvature

Let $(M, g)$ be a $C^\infty$ Riemannian manifold modeled on a
finite-dimensional real space (boundary and corners allowed), with Riemann curvature
endomorphism $R$, and let $x \in M$. The sectional curvature of tangent vectors
$u, v \in T_x M$ is

$$K(u, v) = \frac{\langle R(u, v) v, u \rangle}{\|u\|^2 \|v\|^2 - \langle u, v \rangle^2},$$

the sectional curvature of the plane spanned by $u$ and $v$ when they are linearly independent
([Lang, Def. 2.4], [Gud, Def. 8.14]). When $u$ and $v$ are linearly dependent the denominator
vanishes and $K(u, v)$ is $0$ by definition.

With the sign convention used here for $R$, the round unit sphere has $K = 1$.

Formalized by `Manifold.sectionalCurvature`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#sectional-curvature).

## Sectional curvature vanishes on a vector and a multiple of it

Let $(M, g)$ be a
$C^\infty$ Riemannian manifold modeled on a finite-dimensional real space (boundary and corners
allowed), and let $x \in M$, $u \in T_x M$ and $c \in \mathbb{R}$. Then the sectional curvature
at $x$ satisfies $K(u, cu) = 0$: the denominator $\|u\|^2 \|cu\|^2 - \langle u, cu \rangle^2$ of
its defining formula vanishes, and the quotient is then $0$ by definition.

Formalized by `Manifold.sectionalCurvature_smul_right`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#sectional-curvature-smul-right).

## Sectional curvature vanishes on equal vectors

For every point $x$ of a $C^\infty$
Riemannian manifold $(M, g)$ and every tangent vector $u \in T_x M$, the sectional curvature formula
$K$ gives $K(u, u) = 0$: its denominator $\|u\|^2 \|u\|^2 - \langle u, u \rangle^2$ vanishes, where
$\langle \cdot, \cdot \rangle$ and $\|\cdot\|$ are the inner product and norm on $T_x M$ given by
$g$, and a quotient by $0$ is taken to be $0$.

Formalized by `Manifold.sectionalCurvature_self`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#sectional-curvature-self).

## Ricci curvature

For a point $x$ of a $C^\infty$ Riemannian manifold $(M, g)$ and tangent
vectors $v, w \in T_x M$, the Ricci curvature is
$\operatorname{Ric}_x(v, w) = \sum_i e_i^*(R(e_i, v) w)$, where $R$ is the Riemann curvature
endomorphism of the Levi-Civita connection of $g$, $(e_i)$ is a fixed basis of $T_x M$ and
$(e_i^*)$ is its dual basis; the contraction itself uses no metric. Since $z \mapsto R(z, v) w$ is
linear, this is its trace and does not depend on the basis ([Lang, Def. 2.7]). The unit
$n$-sphere has $\operatorname{Ric} = (n - 1) g$.

Formalized by `Manifold.ricci`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#ricci).

## Scalar curvature

The scalar curvature of a $C^\infty$ Riemannian manifold $(M, g)$ at a
point $x$ is $\sum_i \operatorname{Ric}_x(e_i, e_i)$, the metric trace of the Ricci curvature
$\operatorname{Ric}$, where $(e_i)$ is a fixed orthonormal basis of $T_x M$ ([Gud, Def. 8.32]).
The unit $n$-sphere has scalar curvature $n (n - 1)$.

Formalized by `Manifold.scalarCurvature`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#scalar-curvature).

## Sectional curvature bounded below

A $C^\infty$ Riemannian manifold $M$ has sectional
curvature at least $k \in \mathbb{R}$ when $K(u, v) \ge k$ for every point $x \in M$ and all
linearly independent tangent vectors $u, v \in T_x M$, where $K(u, v)$ is the sectional curvature
of the plane spanned by $u$ and $v$.

Formalized by `Manifold.SectionalCurvatureGE`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#sectional-curvature-ge).

## Sectional curvature bounded above

A $C^\infty$ Riemannian manifold $M$ has sectional
curvature at most $k \in \mathbb{R}$ when $K(u, v) \le k$ for every point $x \in M$ and all
linearly independent tangent vectors $u, v \in T_x M$, where $K(u, v)$ is the sectional curvature
of the plane spanned by $u$ and $v$.

Formalized by `Manifold.SectionalCurvatureLE`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#sectional-curvature-le).

## Ricci curvature bounded below

A $C^\infty$ Riemannian manifold $(M, g)$ has Ricci curvature
at least $k \in \mathbb{R}$, written $\operatorname{Ric} \ge k g$, when
$\operatorname{Ric}_x(v, v) \ge k \|v\|^2$ for every point $x \in M$ and every tangent vector
$v \in T_x M$, where $\operatorname{Ric}$ is the Ricci curvature and $\|v\|$ is the norm of $v$
given by $g$.

Formalized by `Manifold.RicciGE`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#ricci-ge).

## Scalar curvature bounded below

A $C^\infty$ Riemannian manifold $M$ has scalar curvature at
least $k \in \mathbb{R}$ when its scalar curvature at every point $x \in M$ is at least $k$.

Formalized by `Manifold.ScalarCurvatureGE`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#scalar-curvature-ge).

## Einstein metric

A $C^\infty$ Riemannian manifold $(M, g)$ is Einstein when there is a real
constant $\lambda$ such that $\operatorname{Ric}_x(v, w) = \lambda \, g_x(v, w)$ for every point
$x \in M$ and all tangent vectors $v, w \in T_x M$, where $\operatorname{Ric}$ is the Ricci
curvature ([Lang], Einstein manifolds). Ricci-flat is the case $\lambda = 0$.

Formalized by `Manifold.IsEinstein`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Curvature.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#is-einstein).

## Extending a tangent vector of a normed space gives a constant vector field

Let $F$ be a
normed space over a nontrivially normed field, viewed as a manifold modelled on itself, so that
each tangent space of $F$ is $F$. For every point $x \in F$, tangent vector $u \in T_xF$ and point
$y \in F$, the extension of $u$ to a vector field on $F$ (built from the trivialization of the
tangent bundle at $x$) has value $u$ at $y$.

Formalized by `FiberBundle.extend_model_space`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#extend-model-space).

## Extensions of tangent vectors of a normed space are differentiable

Let $F$ be a normed
space over a nontrivially normed field, viewed as a manifold modelled on itself. For every point
$x \in F$, tangent vector $u \in T_xF$ and point $y \in F$, the extension of $u$ to a vector field
on $F$ (built from the trivialization of the tangent bundle at $x$), viewed as a map from $F$ to
its tangent bundle, is differentiable at $y$, not only at the base point $x$.

Formalized by `FiberBundle.mdifferentiableAt_extend_model_space`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#mdifferentiable-at-extend-model-space).

## Lie brackets of extended tangent vectors of a normed space vanish

Let $F$ be a normed
space over a nontrivially normed field, viewed as a manifold modelled on itself. For points
$x, x' \in F$ and tangent vectors $a \in T_xF$ and $b \in T_{x'}F$, let $X$ and $Y$ be the
extensions of $a$ and $b$ to vector fields on $F$ (built from the trivializations of the tangent
bundle at $x$ and at $x'$). Then the Lie bracket $[X, Y]$ vanishes at every point $y \in F$.

Formalized by `VectorField.mlieBracket_extend_model_space`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#mlie-bracket-extend-model-space).

## The Levi-Civita connection of Euclidean space kills constant vector fields

Let $F$ be a
finite-dimensional real inner product space with the Riemannian metric given by its inner product
on every tangent space, and let $\nabla$ be its Levi-Civita connection. For every point $x \in F$
and tangent vector $w \in T_xF$, let $W$ be the extension of $w$ to a vector field on $F$ (built
from the trivialization of the tangent bundle at $x$; it is the constant vector field with value
$w$). Then the covariant derivative $\nabla W$ at every point $y \in F$ is the zero map.

Formalized by `CovariantDerivative.leviCivitaConnection_extend_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#levi-civita-connection-extend-vector-spa).

## Euclidean space is flat

Let $F$ be a finite-dimensional real inner product space with the
Riemannian metric given by its inner product on every tangent space. For every point $x \in F$
and all tangent vectors $u, v, w \in T_xF$, the Riemann curvature endomorphism $R$ of $F$ at $x$
satisfies $R(u, v)w = 0$.

Formalized by `Manifold.riemannCurvature_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#riemann-curvature-vector-space).

## Euclidean space has zero sectional curvature

Let $F$ be a finite-dimensional real inner
product space with the Riemannian metric given by its inner product on every tangent space. For
every point $x \in F$ and all tangent vectors $u, v \in T_xF$, the sectional curvature $K(u, v)$
of $F$ at $x$ is $0$.

Formalized by `Manifold.sectionalCurvature_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#sectional-curvature-vector-space).

## Euclidean space is Ricci-flat

Let $F$ be a finite-dimensional real inner product space
with the Riemannian metric given by its inner product on every tangent space. For every point
$x \in F$ and all tangent vectors $v, w \in T_xF$, the Ricci curvature $\mathrm{Ric}(v, w)$ of $F$
at $x$ is $0$.

Formalized by `Manifold.ricci_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#ricci-vector-space).

## Euclidean space has zero scalar curvature

Let $F$ be a finite-dimensional real inner
product space with the Riemannian metric given by its inner product on every tangent space. For
every point $x \in F$, the scalar curvature of $F$ at $x$ is $0$.

Formalized by `Manifold.scalarCurvature_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/VectorSpace.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html#scalar-curvature-vector-space).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Curvature of Riemannian manifolds](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry/curvature-of-riemannian-manifolds)
