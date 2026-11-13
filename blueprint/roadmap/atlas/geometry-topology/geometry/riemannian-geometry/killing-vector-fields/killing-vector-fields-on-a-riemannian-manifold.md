---
declaration: section
origin: cited
lean: Manifold.IsKillingVectorField, Manifold.IsKillingVectorField.inner_leviCivitaConnection_self, Manifold.isKillingVectorField_iff_inner_leviCivitaConnection_self, Manifold.mvfderiv_inner_sub_inner_mlieBracket, Manifold.isKillingVectorField_iff_mvfderiv_inner, Manifold.isKillingVectorField_zero, Manifold.IsKillingVectorField.add, Manifold.IsKillingVectorField.const_smul
statement: formalized
proof: formalized
---

# Killing vector fields on a Riemannian manifold

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html).

## Killing vector field

Let $M$ be a finite-dimensional smooth manifold, possibly with
boundary or corners, with a smooth Riemannian metric $g = \langle \cdot, \cdot \rangle$ and its
Levi-Civita connection $\nabla$. A vector field $X$ on $M$ is a Killing vector field if $X$ is
smooth and satisfies Killing's equation: for every point $x \in M$ and all tangent vectors
$u, v \in T_x M$,

$$\langle \nabla_u X, v \rangle + \langle u, \nabla_v X \rangle = 0.$$

In index notation this is $\nabla_i X_j + \nabla_j X_i = 0$, and it is equivalent to the
vanishing of the Lie derivative $L_X g$ of the metric. Smoothness is part of the definition, as
in the textbook definition.

## Sources

- Burns and Matveev (2021), §10.2, for motivation: a Killing field $V$ gives the linear first integral $\xi \mapsto g(V, \xi)$ of geodesic flow.

Formalized by `Manifold.IsKillingVectorField`, a structure declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#is-killing-vector-field).

## Killing's equation on the diagonal

Let $X$ be a Killing vector field on a smooth
Riemannian manifold $M$ with Levi-Civita connection $\nabla$. Then
$\langle \nabla_u X, u \rangle = 0$ for every point $x \in M$ and every tangent vector
$u \in T_x M$: a Killing field preserves lengths infinitesimally.

Formalized by `Manifold.IsKillingVectorField.inner_leviCivitaConnection_self`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#inner-levi-civita-connection-self).

## Killing fields via the diagonal of Killing's equation

Let $M$ be a smooth Riemannian
manifold with Levi-Civita connection $\nabla$. A vector field $X$ on $M$ is a Killing vector
field if and only if $X$ is smooth and $\langle \nabla_u X, u \rangle = 0$ for every point
$x \in M$ and every tangent vector $u \in T_x M$.

The converse direction is a polarization argument.

Formalized by `Manifold.isKillingVectorField_iff_inner_leviCivitaConnection_self`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#is-killing-vector-field-iff-inner-levi-c).

## The Lie derivative of the metric via the Levi-Civita connection

Let $M$ be a smooth
manifold modeled on a finite-dimensional real normed space (possibly with corners), with a smooth
Riemannian metric $g = \langle \cdot, \cdot \rangle$ and Levi-Civita connection $\nabla$, and let
$X$, $Y$, $Z$ be vector fields on $M$ that are differentiable at a point $x$. Write $[\cdot, \cdot]$
for the Lie bracket of vector fields and $X_x \langle Y, Z \rangle$ for the derivative at $x$ of
the function $y \mapsto \langle Y_y, Z_y \rangle$ in the direction $X_x$. Then

$$
X_x \langle Y, Z \rangle - \langle [X, Y]_x, Z_x \rangle - \langle Y_x, [X, Z]_x \rangle
= \langle \nabla_{Y_x} X, Z_x \rangle + \langle Y_x, \nabla_{Z_x} X \rangle.
$$

The left-hand side is $(\mathcal{L}_X g)(Y, Z)$ at $x$.

Formalized by `Manifold.mvfderiv_inner_sub_inner_mlieBracket`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#mvfderiv-inner-sub-inner-mlie-bracket).

## Killing fields are those with vanishing Lie derivative of the metric

Let $M$ be a smooth
Riemannian manifold with metric $g = \langle \cdot, \cdot \rangle$. A vector field $X$ on $M$ is
a Killing vector field if and only if $X$ is smooth and, for every point $x \in M$ and all vector
fields $Y$ and $Z$ on $M$ that are differentiable at $x$,

$$X_x \langle Y, Z \rangle - \langle [X, Y]_x, Z_x \rangle - \langle Y_x, [X, Z]_x \rangle = 0,$$

where $X_x \langle Y, Z \rangle$ is the derivative at $x$ of the function
$y \mapsto \langle Y_y, Z_y \rangle$ in the direction $X_x$, and $[X, Y]$ is the Lie bracket.
The left-hand side is $(L_X g)(Y, Z)$ at $x$, where $L_X g$ is the Lie derivative of $g$ along
$X$.

Formalized by `Manifold.isKillingVectorField_iff_mvfderiv_inner`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#is-killing-vector-field-iff-mvfderiv-inn).

## The zero field is Killing

On a smooth Riemannian manifold, the zero vector field is a
Killing vector field.

Formalized by `Manifold.isKillingVectorField_zero`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#is-killing-vector-field-zero).

## Sum of Killing fields

On a smooth Riemannian manifold, the sum $X + Y$ of two Killing
vector fields $X$ and $Y$ is a Killing vector field.

Formalized by `Manifold.IsKillingVectorField.add`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#add).

## Real multiples of Killing fields

On a smooth Riemannian manifold, if $X$ is a Killing
vector field and $c$ is a real number, then $c X$ is a Killing vector field.

Formalized by `Manifold.IsKillingVectorField.const_smul`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#const-smul).

## Space of Killing vector fields

For a smooth Riemannian manifold $M$, the Killing vector
fields on $M$ form a real linear subspace of the real vector space of all (not necessarily
continuous) vector fields on $M$.

Formalized by `Manifold.killingVectorFields`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#killing-vector-fields).

## Membership in the space of Killing fields

A vector field $X$ on a smooth Riemannian
manifold $M$ lies in the space of Killing vector fields on $M$ if and only if $X$ is a Killing
vector field.

Formalized by `Manifold.mem_killingVectorFields`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#mem-killing-vector-fields).

## Extensionality for Killing fields

Two elements $a$ and $b$ of the space of
Killing vector fields on a smooth Riemannian manifold $M$ that agree at every point
$x \in M$ are equal.

Formalized by `Manifold.killingVectorFields.ext`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Killing/Basic.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html#ext).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Killing vector fields on a Riemannian manifold](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry/killing-vector-fields/killing-vector-fields-on-a-riemannian-manifold)
