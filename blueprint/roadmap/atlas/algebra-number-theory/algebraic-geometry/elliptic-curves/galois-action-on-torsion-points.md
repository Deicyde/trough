---
declaration: section
origin: cited
lean: MetaMathlibExt.galAlgEquiv, MetaMathlibExt.galPointHom, MetaMathlibExt.galAlgEquiv_mul, MetaMathlibExt.galAlgEquiv_inv, MetaMathlibExt.galToAlgHom_comp, MetaMathlibExt.galPointHom_apply_one, MetaMathlibExt.galPointHom_apply_mul, MetaMathlibExt.torsionPts
statement: formalized
proof: formalized
---

# Galois action on torsion points

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html).

## Galois elements as automorphisms of $\overline{\mathbb{Q}}$

Each element $\sigma$ of
the absolute Galois group $G_{\mathbb{Q}}$ of $\mathbb{Q}$ is regarded as the
$\mathbb{Q}$-algebra automorphism $\sigma$ of the algebraic closure $\overline{\mathbb{Q}}$ of
$\mathbb{Q}$. Since $G_{\mathbb{Q}}$ is by definition the group of $\mathbb{Q}$-algebra
automorphisms of $\overline{\mathbb{Q}}$, this map is the identity.

Formalized by `MetaMathlibExt.galAlgEquiv`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-alg-equiv).

## Galois action on the points of a Weierstrass curve

Let $W$ be a Weierstrass curve over
$\mathbb{Q}$ and let $W(\overline{\mathbb{Q}})$ be the group of nonsingular points of $W$ with
coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity. For $\sigma$ in the absolute Galois group $G_{\mathbb{Q}}$, this is the homomorphism
of additive groups $W(\overline{\mathbb{Q}}) \to W(\overline{\mathbb{Q}})$ that sends the point
$(x, y)$ to $(\sigma(x), \sigma(y))$ and fixes the point at infinity.

For each natural number $p$, restricting this action to the $p$-torsion points gives the mod-$p$
Galois representation.

Formalized by `MetaMathlibExt.galPointHom`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-point-hom).

## Galois elements as automorphisms of $\overline{\mathbb{Q}}$ respect products

For all
$\sigma, \tau$ in the absolute Galois group $G_{\mathbb{Q}}$ of $\mathbb{Q}$, the
$\mathbb{Q}$-algebra automorphism of the algebraic closure $\overline{\mathbb{Q}}$ attached to
$\sigma\tau$ is the composite of the automorphisms attached to $\sigma$ and to $\tau$, with the
one attached to $\tau$ applied first.

The equality holds by definition.

Formalized by `MetaMathlibExt.galAlgEquiv_mul`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-alg-equiv-mul).

## Galois elements as automorphisms of $\overline{\mathbb{Q}}$ respect inverses

For every
$\sigma$ in the absolute Galois group $G_{\mathbb{Q}}$ of $\mathbb{Q}$, the $\mathbb{Q}$-algebra
automorphism of the algebraic closure $\overline{\mathbb{Q}}$ attached to $\sigma^{-1}$ is the
inverse of the automorphism attached to $\sigma$.

The equality holds by definition.

Formalized by `MetaMathlibExt.galAlgEquiv_inv`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-alg-equiv-inv).

## Galois automorphisms compose as algebra maps

Let $\overline{\mathbb{Q}}$ be the algebraic
closure of $\mathbb{Q}$. For all $\sigma, \tau$ in the absolute Galois group $G_{\mathbb{Q}}$ of
$\mathbb{Q}$, the $\mathbb{Q}$-algebra homomorphism
$\overline{\mathbb{Q}} \to \overline{\mathbb{Q}}$ underlying the product $\sigma\tau$ is the
composite $\sigma \circ \tau$ of the $\mathbb{Q}$-algebra homomorphisms underlying $\sigma$
and $\tau$.

Formalized by `MetaMathlibExt.galToAlgHom_comp`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-to-alg-hom-comp).

## The identity acts trivially on points

Let $W$ be a Weierstrass curve over $\mathbb{Q}$
and let $W(\overline{\mathbb{Q}})$ be the group of nonsingular points of $W$ with coordinates in
the algebraic closure $\overline{\mathbb{Q}}$, together with the point at infinity. For $\sigma$
in the absolute Galois group $G_{\mathbb{Q}}$ and $P \in W(\overline{\mathbb{Q}})$, let
$\sigma \cdot P$ be the point obtained by applying $\sigma$ to the coordinates of $P$ (the point
at infinity is fixed). Then $1 \cdot P = P$ for every $P \in W(\overline{\mathbb{Q}})$, where
$1$ is the identity of $G_{\mathbb{Q}}$.

Formalized by `MetaMathlibExt.galPointHom_apply_one`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-point-hom-apply-one).

## The Galois action on points is compatible with multiplication

Let $W$ be a Weierstrass
curve over $\mathbb{Q}$ and let $W(\overline{\mathbb{Q}})$ be the group of nonsingular points of
$W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity. For $\sigma$ in the absolute Galois group $G_{\mathbb{Q}}$ and
$P \in W(\overline{\mathbb{Q}})$, let $\sigma \cdot P$ be the point obtained by applying $\sigma$
to the coordinates of $P$ (the point at infinity is fixed). Then for all
$\sigma, \tau \in G_{\mathbb{Q}}$ and every $P \in W(\overline{\mathbb{Q}})$,
$(\sigma\tau) \cdot P = \sigma \cdot (\tau \cdot P)$.

Formalized by `MetaMathlibExt.galPointHom_apply_mul`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-point-hom-apply-mul).

## The $p$-torsion subgroup

Let $W$ be a Weierstrass curve over $\mathbb{Q}$, let $p$ be a
natural number, and let $W(\overline{\mathbb{Q}})$ be the group of nonsingular points of $W$ with
coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at infinity.
The $p$-torsion subgroup $W[p]$ is the subgroup of points $P \in W(\overline{\mathbb{Q}})$ with
$pP = 0$.

When $W$ is an elliptic curve $E$, this is the group usually written $E[p]$.

Formalized by `MetaMathlibExt.torsionPts`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#torsion-pts).

## Membership in the $p$-torsion subgroup

Let $W$ be a Weierstrass curve over $\mathbb{Q}$,
let $p$ be a natural number, let $W(\overline{\mathbb{Q}})$ be the group of nonsingular points of
$W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity, and let $W[p]$ be its $p$-torsion subgroup. A point $x \in W(\overline{\mathbb{Q}})$
lies in $W[p]$ if and only if $p x = 0$, where $p x$ is the sum of $p$ copies of $x$ and $0$ is
the point at infinity.

Formalized by `MetaMathlibExt.mem_torsionPts_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#mem-torsion-pts-iff).

## The Galois action preserves $p$-torsion points

Let $W$ be a Weierstrass curve over
$\mathbb{Q}$, let $p$ be a natural number, let $W(\overline{\mathbb{Q}})$ be the group of
nonsingular points of $W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$,
together with the point at infinity, and let $W[p]$ be its subgroup of points $P$ with $pP = 0$.
For $\sigma$ in the absolute Galois group $G_{\mathbb{Q}}$ and $P \in W(\overline{\mathbb{Q}})$,
let $\sigma \cdot P$ be the point obtained by applying $\sigma$ to the coordinates of $P$ (the
point at infinity is fixed). Then for every $\sigma \in G_{\mathbb{Q}}$ and every $x \in W[p]$,
the point $\sigma \cdot x$ lies in $W[p]$.

Formalized by `MetaMathlibExt.galPointHom_mem`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-point-hom-mem).

## Galois action on $p$-torsion points

Let $W$ be a Weierstrass curve over $\mathbb{Q}$,
let $p$ be a natural number, let $W(\overline{\mathbb{Q}})$ be the group of nonsingular points of
$W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity, and let $W[p]$ be its subgroup of points $P$ with $pP = 0$. For $\sigma$ in the
absolute Galois group $G_{\mathbb{Q}}$, this is the homomorphism of additive groups
$W[p] \to W[p]$ that sends the point $(x, y)$ to $(\sigma(x), \sigma(y))$ and fixes the point at
infinity.

Formalized by `MetaMathlibExt.galTorsionHom`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-torsion-hom).

## Linear Galois action on $W(p)$

Let $W$ be a Weierstrass curve over $\mathbb{Q}$,
$p$ a natural number, $W(\overline{\mathbb{Q}})$ the group of nonsingular points of $W$ with
coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity, and $W[p]$ its $p$-torsion subgroup; it is a $\mathbb{Z}/p\mathbb{Z}$-module because
$p$ annihilates it. For $\sigma$ in the absolute Galois group $G_{\mathbb{Q}}$ of $\mathbb{Q}$,
this is the $\mathbb{Z}/p\mathbb{Z}$-linear map $W[p] \to W[p]$, $x \mapsto \sigma(x)$, where
$\sigma$ acts on points through their coordinates.

Formalized by `MetaMathlibExt.galLinearMap`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-linear-map).

## The linear Galois action on $W(p)$ is the action on points

Let $W$ be a Weierstrass
curve over $\mathbb{Q}$, $p$ a natural number, $W(\overline{\mathbb{Q}})$ the group of nonsingular
points of $W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the
point at infinity, and $W[p]$ its $p$-torsion subgroup. For every $\sigma$ in the absolute Galois
group $G_{\mathbb{Q}}$ of $\mathbb{Q}$ and every $x \in W[p]$, the image of $x$ under the
$\mathbb{Z}/p\mathbb{Z}$-linear action of $\sigma$ on $W[p]$ is the point $\sigma(x)$ given by the
Galois action of $\sigma$ on all of $W(\overline{\mathbb{Q}})$.

Formalized by `MetaMathlibExt.galLinearMap_apply`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-linear-map-apply).

## The identity acts trivially on $W(p)$

Let $W$ be a Weierstrass curve over $\mathbb{Q}$,
$p$ a natural number, $W(\overline{\mathbb{Q}})$ the group of nonsingular points of $W$ with
coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity, and $W[p]$ its $p$-torsion subgroup. Under the $\mathbb{Z}/p\mathbb{Z}$-linear action
of the absolute Galois group of $\mathbb{Q}$ on $W[p]$, the identity element maps every
$x \in W[p]$ to $x$.

Formalized by `MetaMathlibExt.galLinearMap_one_apply`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-linear-map-one-apply).

## The linear Galois action on $W(p)$ respects products

Let $W$ be a Weierstrass curve
over $\mathbb{Q}$, $p$ a natural number, $W(\overline{\mathbb{Q}})$ the group of nonsingular
points of $W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the
point at infinity, and $W[p]$ its $p$-torsion subgroup. For $\sigma$ in the absolute Galois group
$G_{\mathbb{Q}}$ of $\mathbb{Q}$ and $x \in W[p]$, write $\sigma \cdot x$ for the image of $x$
under the $\mathbb{Z}/p\mathbb{Z}$-linear action of $\sigma$ on $W[p]$. Then for all
$\sigma, \tau \in G_{\mathbb{Q}}$ and every $x \in W[p]$,
$(\sigma\tau) \cdot x = \sigma \cdot (\tau \cdot x)$.

Formalized by `MetaMathlibExt.galLinearMap_mul_apply`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-linear-map-mul-apply).

## Galois automorphisms act bijectively on $W(p)$

Let $W$ be a Weierstrass curve over
$\mathbb{Q}$, $p$ a natural number, $W(\overline{\mathbb{Q}})$ the group of nonsingular points of
$W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity, and $W[p]$ its $p$-torsion subgroup. For every $\sigma$ in the absolute Galois group
$G_{\mathbb{Q}}$ of $\mathbb{Q}$, the $\mathbb{Z}/p\mathbb{Z}$-linear map by which $\sigma$ acts
on $W[p]$ is bijective.

The action of $\sigma^{-1}$ is a two-sided inverse.

Formalized by `MetaMathlibExt.galLinearMap_bijective`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-linear-map-bijective).

## Galois automorphisms as linear automorphisms of $W(p)$

Let $W$ be a Weierstrass curve
over $\mathbb{Q}$, $p$ a natural number, $W(\overline{\mathbb{Q}})$ the group of nonsingular
points of $W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the
point at infinity, and $W[p]$ its $p$-torsion subgroup. For $\sigma$ in the absolute Galois group
$G_{\mathbb{Q}}$ of $\mathbb{Q}$, this is the $\mathbb{Z}/p\mathbb{Z}$-linear map
$x \mapsto \sigma(x)$ on $W[p]$, where $\sigma$ acts on points through their coordinates, viewed
as a linear automorphism of $W[p]$ (the map is bijective).

Formalized by `MetaMathlibExt.galLinearEquiv`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-linear-equiv).

## The mod-$p$ Galois representation

Let $W$ be a Weierstrass curve over $\mathbb{Q}$, let
$p$ be a natural number, let $W(\overline{\mathbb{Q}})$ be the group of nonsingular points of $W$
with coordinates in the algebraic closure $\overline{\mathbb{Q}}$, together with the point at
infinity, and let $W[p]$ be its subgroup of points $P$ with $pP = 0$, viewed as a
$\mathbb{Z}/p\mathbb{Z}$-module. The mod-$p$ Galois representation is the group homomorphism
from the absolute Galois group $G_{\mathbb{Q}}$ to the group of $\mathbb{Z}/p\mathbb{Z}$-linear
automorphisms of $W[p]$ that sends $\sigma$ to the map $(x, y) \mapsto (\sigma(x), \sigma(y))$,
which fixes the point at infinity.

When $W$ is an elliptic curve $E$, this is the representation usually written $\rho_{E,p}$.

Formalized by `MetaMathlibExt.galRep`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-rep).

## Determinant character of the mod-$p$ Galois representation

Let $W$ be a Weierstrass
curve over $\mathbb{Q}$, let $p$ be a natural number, let $W(\overline{\mathbb{Q}})$ be the group
of nonsingular points of $W$ with coordinates in the algebraic closure $\overline{\mathbb{Q}}$,
together with the point at infinity, and let $W[p]$ be its $p$-torsion subgroup, viewed as a
$\mathbb{Z}/p\mathbb{Z}$-module. Let $\rho$ be the mod-$p$ Galois representation of the absolute
Galois group $G_{\mathbb{Q}}$ of $\mathbb{Q}$ on $W[p]$. Its determinant character is the group
homomorphism $G_{\mathbb{Q}} \to (\mathbb{Z}/p\mathbb{Z})^\times$ sending $\sigma$ to the
determinant of the $\mathbb{Z}/p\mathbb{Z}$-linear automorphism $\rho(\sigma)$ of $W[p]$.

The determinant does not depend on a choice of basis, so no basis of $W[p]$ is fixed. The
definition is unconditional: if $W[p]$ has no finite basis over $\mathbb{Z}/p\mathbb{Z}$, the
character is constantly $1$.

Formalized by `MetaMathlibExt.galDetHom`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/GaloisRepresentation.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html#gal-det-hom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Galois action on torsion points](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/elliptic-curves/galois-action-on-torsion-points)
