---
declaration: section
origin: cited
lean: MathlibExt.Topology.Knot.Euclidean.ParametrizedKnot, MathlibExt.Topology.Knot.Euclidean.ParametrizedLink, MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy, MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy.id, MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy.symm, MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy.comp, MathlibExt.Topology.Knot.Euclidean.CircleReparam, MathlibExt.Topology.Knot.Euclidean.CircleReparam.id
statement: formalized
---

# Knots, links and ambient isotopy

70 results, 68 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html).

## Parametrized knot

An oriented parametrized smooth knot in Euclidean 3-space is a
$C^\infty$ curve $\gamma \colon \mathbb{R} \to \mathbb{R}^3$ that is $2\pi$-periodic
($\gamma(t + 2\pi) = \gamma(t)$ for all $t$), injective on $[0, 2\pi)$, and an immersion
($\gamma'(t) \neq 0$ for all $t$).

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedKnot`, a structure declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#parametrized-knot).

## Parametrized link

An oriented labeled parametrized smooth link with $n$ components
in Euclidean 3-space is a family $(\gamma_i)_{i < n}$ of parametrized knots whose traces
$\gamma_i(\mathbb{R})$ are pairwise disjoint.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink`, a structure declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#parametrized-link).

## Smooth ambient isotopy of Euclidean 3-space

A smooth ambient isotopy of
$\mathbb{R}^3$ consists of two families of maps $H_t, G_t \colon \mathbb{R}^3 \to \mathbb{R}^3$,
indexed by times $t \in \mathbb{R}$, such that $(t, x) \mapsto H_t(x)$ and
$(t, x) \mapsto G_t(x)$ are $C^\infty$ on $\mathbb{R} \times \mathbb{R}^3$, $G_t(H_t(x)) = x$
and $H_t(G_t(x)) = x$ for all $t$ and $x$, and $H_0$ is the identity.

Formalized by `MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy`, a structure declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ambient-isotopy).

## Identity ambient isotopy

The identity ambient isotopy of $\mathbb{R}^3$ has forward
and inverse families $H_t$ and $G_t$ equal to the identity map of $\mathbb{R}^3$ for every
time $t$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy.id`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#id).

## Inverse ambient isotopy

The inverse of an ambient isotopy with forward family $(H_t)$ and
inverse family $(H_t^{-1})$ is the ambient isotopy whose forward family is $(H_t^{-1})$ and whose
inverse family is $(H_t)$; at each time $t$ it is the inverse diffeomorphism of $H_t$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy.symm`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#symm).

## Composition of ambient isotopies

If $\Phi$ and $\Psi$ are smooth ambient isotopies of
$\mathbb{R}^3$ with forward families $H_t, H'_t$ and inverse families $G_t, G'_t$, their
composition (first $\Phi$, then $\Psi$, at the same time parameter) is the ambient isotopy
with forward family $H'_t \circ H_t$ and inverse family $G_t \circ G'_t$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.AmbientIsotopy.comp`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#comp).

## Orientation-preserving reparametrization of the circle

An orientation-preserving
smooth reparametrization of the circle is given by maps $f, g \colon \mathbb{R} \to \mathbb{R}$,
both $C^\infty$ and inverse to each other ($g(f(t)) = t$ and $f(g(t)) = t$ for all $t$), such
that $f(t + 2\pi) = f(t) + 2\pi$ and $g(t + 2\pi) = g(t) + 2\pi$ for all $t$, and $f$ is
strictly increasing. Here $f$ is a lift of the reparametrization and $g$ is a lift of its
inverse.

Formalized by `MathlibExt.Topology.Knot.Euclidean.CircleReparam`, a structure declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#circle-reparam).

## Identity reparametrization of the circle

The identity circle reparametrization has
lift and inverse lift both equal to the identity map of $\mathbb{R}$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.CircleReparam.id`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#id-2).

## Inverse circle reparametrization

The inverse of a circle reparametrization with lift
$f$ and inverse lift $f^{-1}$ is the circle reparametrization whose lift is $f^{-1}$ and whose
inverse lift is $f$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.CircleReparam.symm`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#symm-2).

## Composition of circle reparametrizations

If $\sigma$ and $\tau$ are circle
reparametrizations with lifts $f_\sigma, f_\tau$ and inverse lifts $g_\sigma, g_\tau$, their
composition (first $\sigma$, then $\tau$) is the circle reparametrization with lift
$f_\tau \circ f_\sigma$ and inverse lift $g_\sigma \circ g_\tau$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.CircleReparam.comp`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#comp-2).

## Isotopy of parametrized knots

Two parametrized knots $\gamma_1, \gamma_2$ in
$\mathbb{R}^3$ are isotopic (oriented ambient isotopy) if there are a smooth ambient isotopy
of $\mathbb{R}^3$ with forward family $H_t$ and an orientation-preserving reparametrization
of the circle with lift $f$ such that $H_1(\gamma_1(t)) = \gamma_2(f(t))$ for every
$t \in \mathbb{R}$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedKnot.Isotopic`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#isotopic).

## Isotopy of parametrized links

Two parametrized links in $\mathbb{R}^3$ with $n$
components $\gamma^1_i$ and $\gamma^2_i$ ($i < n$) are isotopic (oriented, labeled ambient
isotopy) if there are a single smooth ambient isotopy of $\mathbb{R}^3$ with forward family
$H_t$ and, for each $i < n$, an orientation-preserving reparametrization of the circle with
lift $f_i$, such that $H_1(\gamma^1_i(t)) = \gamma^2_i(f_i(t))$ for every $i < n$ and every
$t \in \mathbb{R}$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.Isotopic`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#isotopic-2).

## Trace of a parametrized link

The trace of a parametrized link $L$ in Euclidean 3-space
is the union of the images of its component curves: the set of all points $\gamma(t)$, where
$\gamma$ is a component of $L$ and $t \in \mathbb{R}$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.trace`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#trace).

## Total contour length of a parametrized link

Let $L$ be a parametrized link in
Euclidean 3-space with components $\gamma_1, \dots, \gamma_n$, each a $2\pi$-periodic curve.
The total contour length of $L$ is the sum over all components $\gamma_i$ of the contour
length of $\gamma_i$ on one period $[0, 2\pi]$. It is a value in $[0, \infty]$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.totalContourLength`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#total-contour-length).

## Ropelength ratio of a parametrized link

For a parametrized link $L$, the ropelength
ratio of $L$ is its total contour length divided by the thickness of its trace (the union of the
images of its components), a value in $[0, \infty]$ computed with the division of $[0, \infty]$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.ropelengthRatio`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ropelength-ratio).

## Ropelength of a parametrized link

For a parametrized link $L$ with $n$ components, the
ropelength of $L$ is the infimum, in $[0, \infty]$, of the ropelength ratios of all parametrized
links $L'$ with $n$ components that are isotopic to $L$. It is the ropelength of the oriented,
labeled ambient-isotopy type of $L$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.ropelength`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ropelength).

## Ropelength is at most the ratio of any isotopic link

Let $L$ and $L'$ be parametrized
links with $n$ components. If $L'$ is isotopic to $L$, then the ropelength of $L$ is at most
the ropelength ratio of $L'$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.ropelength_le_ratio_of_isotopic`, a theorem declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ropelength-le-ratio-of-isotopic).

## Ropelength is at most the ropelength ratio

For every parametrized link $L$ with $n$
components, the ropelength of $L$ is at most the ropelength ratio of $L$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.ropelength_le_ratio_self`, a theorem declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ropelength-le-ratio-self).

## Ropelength is an isotopy invariant

Let $L_1$ and $L_2$ be parametrized links with $n$
components. If $L_1$ is isotopic to $L_2$ (by an oriented, labeled ambient isotopy), then the
ropelength of $L_1$ equals the ropelength of $L_2$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedLink.ropelength_eq_of_isotopic`, a theorem declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ropelength-eq-of-isotopic).

## Parametrized knot as a one-component link

A parametrized knot $K$ determines the
parametrized link with one component, whose single component is $K$; the pairwise disjointness
condition holds trivially.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedKnot.toLink`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#to-link).

## Isotopic knots give isotopic one-component links

If $K_1$ and $K_2$ are parametrized
knots and $K_1$ is isotopic to $K_2$, then the one-component parametrized link of $K_1$ is
isotopic to the one-component parametrized link of $K_2$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedKnot.Isotopic.toLink`, a theorem declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#to-link-2).

## Ropelength of a parametrized knot

The ropelength of a parametrized knot $K$ is the
ropelength of the one-component parametrized link determined by $K$: the infimum, in
$[0, \infty]$, of the ropelength ratios of all one-component parametrized links that are
isotopic to the one-component link of $K$.

Formalized by `MathlibExt.Topology.Knot.Euclidean.ParametrizedKnot.ropelength`, a definition declared in [MathlibExt/Topology/Knot/EuclideanLink.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Knot/EuclideanLink.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ropelength-2).

## Euclidean space $\mathbb{R}^3$

The ambient space of the knots here is $\mathbb{R}^3$ with
its standard Euclidean inner product.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.R3`, an abbreviation declared in [WantedExt/Topology/ConwayKnotShared.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#r3).

## Oriented smooth knot

An oriented smooth knot in $\mathbb{R}^3$ is a smooth map
$\gamma : \mathbb{R} \to \mathbb{R}^3$ that is $2\pi$-periodic, injective on $[0, 2\pi)$, and an
immersion, meaning $\gamma'(t) \ne 0$ for every real $t$. The orientation is the one induced by
the parametrization.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.Knot`, a structure declared in [WantedExt/Topology/ConwayKnotShared.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#knot).

## Two-component link

An oriented two-component smooth link in $\mathbb{R}^3$ is a pair
$(K, L)$ of oriented smooth knots whose images in $\mathbb{R}^3$ are disjoint.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.TwoLink`, a structure declared in [WantedExt/Topology/ConwayKnotShared.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#two-link).

## Smooth ambient isotopy of $\mathbb{R}^3$

A smooth ambient isotopy of $\mathbb{R}^3$
consists of two families of maps $H_t, G_t \colon \mathbb{R}^3 \to \mathbb{R}^3$ indexed by
$t \in \mathbb{R}$ such that $(t, x) \mapsto H_t(x)$ and $(t, x) \mapsto G_t(x)$ are smooth
($C^\infty$) maps $\mathbb{R} \times \mathbb{R}^3 \to \mathbb{R}^3$, $G_t$ is a two-sided inverse
of $H_t$ for every $t$, and $H_0$ is the identity. In particular every $H_t$ is a
diffeomorphism of $\mathbb{R}^3$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.AmbientIsotopy`, a structure declared in [WantedExt/Topology/ConwayKnotShared.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#ambient-isotopy-2).

## Ambient isotopy of oriented knots

Let $K_1$ and $K_2$ be oriented knots, each given by
its $2\pi$-periodic parametrization. They are ambient-isotopic if there are a smooth ambient
isotopy $(\Phi_t)_{t \in \mathbb{R}}$ of $\mathbb{R}^3$ and an orientation-preserving smooth
reparametrization $\sigma$ of the circle such that $\Phi_1(K_1(t)) = K_2(\sigma(t))$ for every real
$t$. Here an orientation-preserving smooth reparametrization of the circle is a smooth, strictly
increasing bijection $\sigma : \mathbb{R} \to \mathbb{R}$ with smooth inverse such that
$\sigma(t + 2\pi) = \sigma(t) + 2\pi$ for every $t$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.Knot.Isotopic`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#isotopic-3).

## Ambient isotopy of oriented two-component links

Let $L = (K, J)$ and $L' = (K', J')$ be
oriented two-component links, each knot given by its $2\pi$-periodic parametrization. Then $L$
and $L'$ are ambient-isotopic if there are a smooth ambient isotopy $(\Phi_t)_{t \in \mathbb{R}}$
of $\mathbb{R}^3$ and orientation-preserving smooth reparametrizations $\sigma$, $\tau$ of the
circle such that $\Phi_1(K(t)) = K'(\sigma(t))$ and $\Phi_1(J(t)) = J'(\tau(t))$ for every real
$t$. Here an orientation-preserving smooth reparametrization of the circle is a smooth, strictly
increasing bijection $\sigma : \mathbb{R} \to \mathbb{R}$ with smooth inverse such that
$\sigma(t + 2\pi) = \sigma(t) + 2\pi$ for every $t$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.TwoLink.Isotopic`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#isotopic-4).

## Reflection in the $xy$-plane

The reflection of $\mathbb{R}^3$ through the $xy$-plane is
the map $(x, y, z) \mapsto (x, y, -z)$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.reflectZ`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#reflect-z).

## Chiral knot

Let $K \colon \mathbb{R} \to \mathbb{R}^3$ be an oriented smooth knot, and
let $\rho(x, y, z) = (x, y, -z)$ be the reflection of $\mathbb{R}^3$ through the $xy$-plane.
Call $\sigma \colon \mathbb{R} \to \mathbb{R}$ an orientation-preserving reparametrization of
the circle if it is a strictly increasing smooth bijection with smooth inverse satisfying
$\sigma(t + 2\pi) = \sigma(t) + 2\pi$ for all $t \in \mathbb{R}$, that is, the lift of an
orientation-preserving diffeomorphism of $\mathbb{R} / 2\pi\mathbb{Z}$. The knot $K$ is chiral
if there is no smooth ambient isotopy $(H_t)$ of $\mathbb{R}^3$ together with such a $\sigma$
satisfying $H_1(K(t)) = \rho(K(\sigma(t)))$ for all $t \in \mathbb{R}$. Equivalently, $K$ is
not ambient isotopic, as an oriented knot, to its mirror image $\rho \circ K$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.Knot.Chiral`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#chiral).

## Topological ambient isotopy

A topological ambient isotopy of $\mathbb{R}^3$ is a family of
maps $H_t : \mathbb{R}^3 \to \mathbb{R}^3$, indexed by $t \in \mathbb{R}$, together with a family
$G_t : \mathbb{R}^3 \to \mathbb{R}^3$ such that $(t, x) \mapsto H_t(x)$ and $(t, x) \mapsto G_t(x)$
are continuous, $G_t$ is a two-sided inverse of $H_t$ for every $t$ (so each $H_t$ is a
homeomorphism of $\mathbb{R}^3$), and $H_0$ is the identity.

The time domain is all of $\mathbb{R}$, but only $H_0$ and $H_1$ matter for the isotopy
relation.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.TopAmbientIsotopy`, a structure declared in [WantedExt/Topology/ConwayKnotShared.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#top-ambient-isotopy).

## Topological ambient isotopy of subsets

Two subsets $A$ and $B$ of $\mathbb{R}^3$ are
unoriented topologically ambient isotopic if there is a topological ambient isotopy $(H_t)$ of
$\mathbb{R}^3$ whose time-one map carries $A$ onto $B$, that is, $H_1(A) = B$.

"Unoriented" because this is a set-level relation that forgets any parametrization.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.Set.UnorientedTopAmbIsotopic`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#unoriented-top-amb-isotopic).

## Closed unit disk in the plane

The closed unit Euclidean disk
$\{(x, y) \in \mathbb{R} \times \mathbb{R} \mid x^2 + y^2 \le 1\}$, the source of the
parametrization of a slicing disk.

The disk and its boundary circle are written out by the equations $x^2 + y^2 \le 1$ and
$x^2 + y^2 = 1$ rather than as the closed unit ball and unit sphere of $\mathbb{R} \times
\mathbb{R}$. The product carries the sup norm, so that ball would be the square $[-1, 1]^2$ and
that sphere its boundary, which has corners. At a corner, no smooth map with injective
derivative can match a corner-free smooth knot as its boundary, so slice disks parametrized by
the square cannot exist, and every knot would fail to be smoothly slice.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.disk2`, an abbreviation declared in [WantedExt/Topology/ConwayKnotShared.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#disk2).

## Unit circle in the plane

The unit Euclidean circle
$\{(x, y) \in \mathbb{R} \times \mathbb{R} \mid x^2 + y^2 = 1\}$, the source of the boundary of
a slicing disk.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.circle1`, an abbreviation declared in [WantedExt/Topology/ConwayKnotShared.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#circle1).

## Closed upper half-space

The closed upper half-space in $\mathbb{R}^3 \times \mathbb{R}$
is the set $\mathbb{R}^3 \times [0, \infty)$ of points $(x, s)$ with $s \ge 0$.

We identify $\mathbb{R}^3 \times [0, \infty)$ with $B^4 \setminus \{\mathrm{pt}\}$, so slice
disks live here.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.upperHalf`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#upper-half).

## Model interior $2$-plane

The model interior $2$-plane in $\mathbb{R}^3 \times \mathbb{R}$
is the set of points $((x_1, x_2, x_3), t)$ with $x_2 = x_3 = 0$, where $x_1$ and $t$ are
arbitrary. It is the local model for interior local flatness of an embedded $2$-disk.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.modelPlane2`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#model-plane2).

## Model half-plane

The model half-plane is the set of pairs $((p_1, p_2, p_3), s)$ in
$\mathbb{R}^3 \times \mathbb{R}$ with $p_2 = p_3 = 0$ and $s \ge 0$. It is a copy of the closed
half-plane $\mathbb{R} \times [0, \infty)$, with coordinates $p_1$ and $s$, lying in the upper
half-space $s \ge 0$.

It is the local model for boundary local flatness of a properly embedded disk.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.modelHalfPlane2`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#model-half-plane2).

## Smoothly slice (smooth knot version)

Let
$\Delta = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 \le 1\}$ be the closed unit disk and
$C = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\}$ its boundary circle. A smooth knot $K$ is
smoothly slice if there is a smooth ($C^\infty$) map $f : \mathbb{R}^2 \to \mathbb{R}^3 \times
\mathbb{R}$ such that $f$ is injective on $\Delta$; for every $p \in \Delta$ the last coordinate
of $f(p)$ is nonnegative, and it is $0$ exactly when $p \in C$; the derivative of $f$ at every
point of $\Delta$ is injective; and the image of $C$ under the $\mathbb{R}^3$-component of $f$
is the image of $K$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.Knot.SmoothlySlice`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#smoothly-slice).

## Local flatness at an interior point

Let $q \in \mathbb{R}^3 \times \mathbb{R}$ and
$D : \mathbb{R}^2 \to \mathbb{R}^3 \times \mathbb{R}$. Write $\Delta = \{(x, y) : x^2 + y^2 \le 1\}$
for the closed unit disk and $P = \{((p_1, p_2, p_3), s) : p_2 = p_3 = 0\}$ for the model plane.
The image $D(\Delta)$ is locally flat at $q$ in the interior sense if there is a homeomorphism
$h : U \to V$ between open subsets $U$, $V$ of $\mathbb{R}^3 \times \mathbb{R}$ such that $q \in U$
and $h(U \cap D(\Delta)) = V \cap P$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.IsLocallyFlatInterior`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#is-locally-flat-interior).

## Local flatness at a boundary point

Let $q \in \mathbb{R}^3 \times \mathbb{R}$ and
$D : \mathbb{R}^2 \to \mathbb{R}^3 \times \mathbb{R}$. Write $\Delta = \{(x, y) : x^2 + y^2 \le 1\}$
for the closed unit disk, $H = \{(p, s) : s \ge 0\}$ for the closed upper half-space, and
$P = \{((p_1, p_2, p_3), s) : p_2 = p_3 = 0,\ s \ge 0\}$ for the model half-plane. The image
$D(\Delta)$ is locally flat at $q$ in the boundary sense if there is a homeomorphism $h : U \to V$
between open subsets $U$, $V$ of $\mathbb{R}^3 \times \mathbb{R}$ such that $q \in U$,
$h(U \cap H) = V \cap H$ and $h(U \cap D(\Delta)) = V \cap P$.

The chart is open in $\mathbb{R}^3 \times \mathbb{R}$ rather than in $H$: when the last coordinate
of $q$ is $0$, every open neighbourhood of $q$ leaves $H$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.IsLocallyFlatBoundary`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#is-locally-flat-boundary).

## Topologically slice (smooth knot version)

Write points of $\mathbb{R}^3 \times \mathbb{R}$
as $(x, s)$ with $x = (x_1, x_2, x_3)$. Let $H = \{(x, s) : s \ge 0\}$ be the closed upper
half-space, $P = \{(x, s) : x_2 = x_3 = 0\}$ the model plane and $P_+ = P \cap H$ the model
half-plane, and let $D^2 = \{(a, b) \in \mathbb{R}^2 : a^2 + b^2 \le 1\}$ and
$S^1 = \{(a, b) \in \mathbb{R}^2 : a^2 + b^2 = 1\}$. A smooth knot $K$ is topologically slice if
there is a continuous map $D : \mathbb{R}^2 \to \mathbb{R}^3 \times \mathbb{R}$, injective on
$D^2$, such that: for every $p \in D^2$ the last coordinate of $D(p)$ is nonnegative, and it is
$0$ exactly when $p \in S^1$; for every $p \in D^2 \setminus S^1$ there is a homeomorphism
$h : U \to V$ between open subsets of $\mathbb{R}^3 \times \mathbb{R}$ with $D(p) \in U$ and
$h(U \cap D(D^2)) = V \cap P$; for every $p \in S^1$ there is such a homeomorphism with
$D(p) \in U$, $h(U \cap H) = V \cap H$ and $h(U \cap D(D^2)) = V \cap P_+$; and the image of
$S^1$ under the $\mathbb{R}^3$-component of $D$ is the image of $K$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.Knot.TopologicallySlice`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#topologically-slice).

## Parametrization of a closed polyline

Let $v_0, \dots, v_{n-1}$ be a list of $n \ge 1$
points of $\mathbb{R}^3$. The polyline curve is the $n$-periodic map
$\gamma : \mathbb{R} \to \mathbb{R}^3$ with $\gamma(k + \alpha) = (1 - \alpha) v_k + \alpha v_{k+1}$
for integers $0 \le k < n$ and reals $0 \le \alpha < 1$, where indices are taken modulo $n$ (so
$v_n = v_0$). For the empty list the curve is constantly $0$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.plCurve`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#pl-curve).

## PL knot (closed polyline)

A PL knot is a list $v_0, \dots, v_{n-1}$ of points of
$\mathbb{R}^3$ with $n \ge 3$, viewed as the vertices, in order, of the closed polyline with edges
from $v_i$ to $v_{i+1}$ for $i < n - 1$ and from $v_{n-1}$ back to $v_0$.

Simplicity of the polyline (that it is an embedded closed curve) is not part of the data; it is
imposed as a separate condition.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.PLKnot`, a structure declared in [WantedExt/Topology/ConwayKnotShared.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#plknot).

## Image of a PL knot

Let $K$ be a PL knot with vertices $v_0, \dots, v_{n-1}$. Its image is
the subset of $\mathbb{R}^3$ traced by the closed polyline through these vertices: the image of the
half-open interval $[0, n)$ under the parametrization that sends $k + \alpha$, for an integer
$0 \le k < n$ and a real $0 \le \alpha < 1$, to $(1 - \alpha) v_k + \alpha v_{k+1}$, with indices
taken modulo $n$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.PLKnot.image`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#image).

## Simple PL knot

A PL knot $K$ with vertices $v_0, \dots, v_{n-1}$ is simple if its closed
polyline parametrization, which sends $k + \alpha$, for an integer $0 \le k < n$ and a real
$0 \le \alpha < 1$, to $(1 - \alpha) v_k + \alpha v_{k+1}$ (indices modulo $n$), is injective on
the half-open interval $[0, n)$.

Equivalently, the polyline is a simple closed curve: all vertices are distinct, non-adjacent
edges are disjoint, and adjacent edges meet only at their shared vertex.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.PLKnot.IsSimple`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#is-simple).

## Smooth representative of a PL knot

A smooth knot $J$ is a smooth representative of
the piecewise-linear knot $K$ if the image of $J$ and the image of $K$ are unoriented
topologically ambient isotopic in $\mathbb{R}^3$: some topological ambient isotopy $(H_t)$ of
$\mathbb{R}^3$ satisfies $H_1(\operatorname{im} J) = \operatorname{im} K$.

When the polyline $K$ is simple, both curves are tame, and this agrees with the usual relation
of having the same smooth/PL knot type.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.PLKnot.HasSmoothRepresentative`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#has-smooth-representative).

## Smoothly slice (PL knot version)

A PL knot $K$ is smoothly slice if there is a smooth
knot $J$ that is smoothly slice and is a smooth representative of $K$: for some topological
ambient isotopy $(H_t)$ of $\mathbb{R}^3$, the map $H_1$ carries the image of $J$ onto the image
(trace) of the polyline $K$.

Piccirillo's theorem that the Conway knot is not smoothly slice is stated with this notion.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.PLKnot.SmoothlySlice`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#smoothly-slice-2).

## Topologically slice (PL knot version)

A PL knot $K$ is topologically slice if there is a
smooth knot $J$ that is a smooth representative of $K$, meaning that the image of $J$ and the image
of $K$ are unoriented topologically ambient isotopic subsets of $\mathbb{R}^3$, and such that $J$
is topologically slice as a smooth knot.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.PLKnot.TopologicallySlice`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#topologically-slice-2).

## Point from three coordinates

For real numbers $x$, $y$, $z$, this is the point
$(x, y, z)$ of the Euclidean space $\mathbb{R}^3$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.BraidClosure.mkR3`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#mk-r3).

## Braid closure traversal state

A traversal state for tracing the closure of a braid
consists of the current strand position, a natural number, and the list of points of
$\mathbb{R}^3$ accumulated so far, in order, as vertices of the polyline.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.BraidClosure.State`, a structure declared in [WantedExt/Topology/ConwayKnotShared.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#state).

## Tracing a strand through one crossing

Let a traversal state consist of a current
strand position $p \in \mathbb{N}$ and a list of vertices in $\mathbb{R}^3$, let
$w \in \mathbb{Z}$ be a braid generator with $i = |w|$, and let
$z_{\mathrm{top}}, z_{\mathrm{bot}} \in \mathbb{R}$. Put
$z_{\mathrm{hi}} = z_{\mathrm{top}} - (z_{\mathrm{top}} - z_{\mathrm{bot}})/4$ and
$z_{\mathrm{lo}} = z_{\mathrm{bot}} + (z_{\mathrm{top}} - z_{\mathrm{bot}})/4$. The new state is
obtained by changing the position and appending the listed points, in order, to the vertex
list. If $p = i$ and $w > 0$, the new position is $i + 1$ and the points are
$(i, 1, z_{\mathrm{hi}})$, $(i + 1, 1, z_{\mathrm{lo}})$, $(i + 1, 0, z_{\mathrm{bot}})$. If
$p = i$ and $w \le 0$, the new position is $i + 1$ and the only point is
$(i + 1, 0, z_{\mathrm{bot}})$. If $p = i + 1$ and $w > 0$, the new position is $i$ and the
only point is $(i, 0, z_{\mathrm{bot}})$. If $p = i + 1$ and $w \le 0$, the new position is
$i$ and the points are $(i + 1, 1, z_{\mathrm{hi}})$, $(i, 1, z_{\mathrm{lo}})$,
$(i, 0, z_{\mathrm{bot}})$. Otherwise the position stays $p$ and the only point is
$(p, 0, z_{\mathrm{bot}})$.

The step is meant for $z_{\mathrm{bot}} < z_{\mathrm{top}}$, with the crossing in the slab
between these heights: the strand passing over is lifted to $y = 1$, and the strand passing
under stays at $y = 0$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.BraidClosure.applyCrossing`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#apply-crossing).

## Tracing a strand through a braid word

Given a traversal state $s$, a braid word
$w_0 w_1 \cdots w_{m-1}$ (a list of integers) and a starting index $k \in \mathbb{N}$, the
one-crossing step is applied to the state for each generator in turn, starting from $s$: the
generator $w_j$ is applied with top height $-(k + j)$ and bottom height $-(k + j + 1)$. The
result is the final state; for the empty word it is $s$.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.BraidClosure.applyWord`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#apply-word).

## One pass of the braid closure

Let $w$ be a braid word (a list of integers) of length $m$.
Starting from a traversal state, one pass applies the letters of $w$ in order as crossings, the
$k$-th letter (counting from $0$) occupying the slab $-(k+1) \le z \le -k$; this moves the state
to a strand position $p$ and appends the crossing vertices. It then appends the closure arc: the
vertices $(p, 100, -m)$ and $(p, 100, 0)$, followed by $(p, 0, 0)$ unless $p = 1$. The resulting
state has position $p$ and the extended vertex list.

When $p = 1$ the vertex $(1, 0, 0)$ is left out because the polyline starts there, so the closure
arc already returns to its first vertex.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.BraidClosure.onePass`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#one-pass).

## Iterated braid-closure passes

For a braid word $w$, a number $f$ of remaining passes and
a traversal state $S$, the iteration returns $S$ when $f = 0$. When $f > 0$ it applies one pass
of $w$ to $S$, obtaining a state $S'$; it returns $S'$ if the strand position of $S'$ is $1$, and
otherwise iterates on $S'$ with $f - 1$ passes remaining.

The bound $f$ guarantees termination. The braid closure on $n$ strands uses $f = n$, since at
most $n$ distinct strand positions are visited.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.BraidClosure.iterate`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#iterate).

## Polyline closure of a braid word

Let $n \in \mathbb{N}$, and let
$w = w_0 w_1 \cdots w_{m-1}$ be a braid word (a list of integers, where $i > 0$ stands for
$\sigma_i$ and $-i$ for $\sigma_i^{-1}$). If $m = 0$, the value is the junk list $(0, 0, 0)$,
$(1, 0, 0)$, $(0, 1, 0)$. Otherwise the value is a list of vertices in $\mathbb{R}^3$ tracing the
closure of $w$ as one polyline component. It starts at the vertex $(1, 0, 0)$ on strand position
$1$ and makes passes through the braid: in each pass the crossing $w_j$ occupies the slab between
heights $z = -(j + 1)$ and $z = -j$, with the strand passing over lifted to $y = 1$, and each
pass is followed by a closure arc through $y = 100$ back up to height $z = 0$. Tracing stops as
soon as a pass ends at position $1$, or after $n$ passes.

The layout is designed for words with $1 \le |w_j| \le n - 1$ for every $j$, where the strands
sit at the $x$-positions $1, \dots, n$; other words still yield a vertex list, but not a
meaningful one.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.braidClosure`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#braid-closure).

## Braid word for the Conway knot

The braid word
$\sigma_1^{-2} \sigma_2 \sigma_1^{-1} \sigma_2 \sigma_1^{-1} \sigma_3 \sigma_2^{-2} \sigma_3^{2}$
on $4$ strands, encoded as the list of integers $[-1, -1, 2, -1, 2, -1, 3, -2, -2, 3, 3]$, where
an entry $i > 0$ stands for the generator $\sigma_i$ and $-i$ for $\sigma_i^{-1}$. It has
length $11$ and writhe $-1$, and is a braid word for the Conway knot 11n34.

## Sources

- KnotInfo's `11n_34` record, `braid_notation` field. The Knot Atlas records a different but Markov-equivalent presentation for the same knot, `[1, 1, 2, -3, 2, 1, -3, -2, -2, -3, -3]` (which it labels `K11n34`, the mirror of the Conway knot); both representations agree on braid index 4, braid length 11, and writhe `-1`. Sliceness is mirror-invariant, so either braid word is a valid witness for `conway_knot_not_smoothly_slice`.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.conwayBraidWord`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#conway-braid-word).

## The Conway knot

The Conway knot 11n34 as a piecewise-linear closed polyline in
$\mathbb{R}^3$: its vertices are those of the polyline closure, on $4$ strands, of the braid word
$\sigma_1^{-2} \sigma_2 \sigma_1^{-1} \sigma_2 \sigma_1^{-1} \sigma_3 \sigma_2^{-2} \sigma_3^{2}$
for the Conway knot.

Formalized by `MathlibExt.Topology.ConwayKnotShared.KnotTheory.conwayKnot`, a definition declared in [WantedExt/Topology/ConwayKnotShared.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotShared.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#conway-knot).

## Knots as parametrized knots

A knot in $\mathbb{R}^3$, given by a smooth $2\pi$-periodic
immersion $\gamma : \mathbb{R} \to \mathbb{R}^3$ that is injective on $[0, 2\pi)$, is sent to the
parametrized knot with the same parametrization $\gamma$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.toParametrizedKnot`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#to-parametrized-knot).

## Parametrized knots as knots

A parametrized knot in $\mathbb{R}^3$, given by a smooth
$2\pi$-periodic immersion $\gamma : \mathbb{R} \to \mathbb{R}^3$ that is injective on
$[0, 2\pi)$, is sent to the knot with the same parametrization $\gamma$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.ofParametrizedKnot`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#of-parametrized-knot).

## Knots are the same as parametrized knots

Sending a knot in $\mathbb{R}^3$ to the
parametrized knot with the same parametrization is a bijection from knots to parametrized knots,
whose inverse sends a parametrized knot to the knot with the same parametrization.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.knotEquiv`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#knot-equiv).

## Conway-knot ambient isotopies as Euclidean ambient isotopies

An ambient isotopy of
$\mathbb{R}^3$ in the sense of the Conway knot statements, given by maps
$H_t : \mathbb{R}^3 \to \mathbb{R}^3$ for $t \in \mathbb{R}$ with $(t, x) \mapsto H_t(x)$ smooth
and $H_0 = \mathrm{id}$, and maps $G_t : \mathbb{R}^3 \to \mathbb{R}^3$ with
$(t, x) \mapsto G_t(x)$ smooth and $G_t \circ H_t = H_t \circ G_t = \mathrm{id}$ for every $t$,
is sent to the smooth ambient isotopy of Euclidean 3-space, in the sense of parametrized links,
with the same forward family $H$ and inverse family $G$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.toEuclideanAmbientIsotopy`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#to-euclidean-ambient-isotopy).

## Euclidean ambient isotopies as Conway-knot ambient isotopies

A smooth ambient isotopy
of Euclidean 3-space in the sense of parametrized links, given by maps
$H_t : \mathbb{R}^3 \to \mathbb{R}^3$ for $t \in \mathbb{R}$ with $(t, x) \mapsto H_t(x)$ smooth
and $H_0 = \mathrm{id}$, and maps $G_t : \mathbb{R}^3 \to \mathbb{R}^3$ with
$(t, x) \mapsto G_t(x)$ smooth and $G_t \circ H_t = H_t \circ G_t = \mathrm{id}$ for every $t$,
is sent to the ambient isotopy of $\mathbb{R}^3$ in the sense of the Conway knot statements with
the same forward family $H$ and inverse family $G$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.ofEuclideanAmbientIsotopy`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#of-euclidean-ambient-isotopy).

## Conway-knot circle reparametrizations as Euclidean ones

An orientation-preserving smooth
reparametrization of the circle in the sense of the Conway knot statements, given by a smooth
strictly increasing map $f : \mathbb{R} \to \mathbb{R}$ with smooth two-sided inverse $g$ such that
$f(t + 2\pi) = f(t) + 2\pi$ and $g(t + 2\pi) = g(t) + 2\pi$ for all $t$, is sent to the circle
reparametrization, in the sense of parametrized links, with the same lift $f$ and inverse
lift $g$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.toEuclideanCircleReparam`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#to-euclidean-circle-reparam).

## Euclidean circle reparametrizations as Conway-knot ones

A circle reparametrization in
the sense of parametrized links, given by a smooth strictly increasing map
$f : \mathbb{R} \to \mathbb{R}$ with smooth two-sided inverse $g$ such that
$f(t + 2\pi) = f(t) + 2\pi$ and $g(t + 2\pi) = g(t) + 2\pi$ for all $t$, is sent to the
orientation-preserving smooth reparametrization of the circle in the sense of the Conway knot
statements with the same lift $f$ and inverse lift $g$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.ofEuclideanCircleReparam`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#of-euclidean-circle-reparam).

## Isotopy of knots agrees with isotopy of parametrized knots

For all knots $K_1$ and
$K_2$ in $\mathbb{R}^3$, $K_1$ and $K_2$ are ambient isotopic if and only if the parametrized knots
with the same parametrizations as $K_1$ and $K_2$ are ambient isotopic as parametrized knots.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.knot_isotopic_iff`, a theorem declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#knot-isotopic-iff).

## Two-component links as labeled links

A two-component link in $\mathbb{R}^3$ with first
component $K$ and second component $L$ is sent to the labeled parametrized link with two
components whose component $0$ is the parametrized knot with the same parametrization as $K$ and
whose component $1$ is the parametrized knot with the same parametrization as $L$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.toParametrizedLink`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#to-parametrized-link).

## Labeled two-component links as two-component links

A labeled parametrized link with
two components $0$ and $1$ is sent to the two-component link in $\mathbb{R}^3$ whose first
component is the knot with the same parametrization as component $0$ and whose second component
is the knot with the same parametrization as component $1$.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.ofParametrizedLink`, a definition declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#of-parametrized-link).

## Two-component link isotopy agrees with labeled link isotopy

Let $L_1$ and $L_2$ be
oriented two-component smooth links in $\mathbb{R}^3$, and regard each as an oriented labeled
smooth link with two components, whose component $0$ is its first component and whose
component $1$ is its second. Then $L_1$ and $L_2$ are ambient isotopic, meaning that a single
smooth ambient isotopy carries each component of $L_1$ onto the corresponding component of
$L_2$ up to orientation-preserving reparametrizations of the circle, if and only if the
associated labeled links are ambient isotopic.

Formalized by `MathlibExt.Topology.ConwayKnotEuclideanBridge.twoLink_isotopic_iff`, a theorem declared in [WantedExt/Topology/ConwayKnotEuclideanBridge.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ConwayKnotEuclideanBridge.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#two-link-isotopic-iff).

## Non-isotopic two-component links exist

There exist two oriented smooth two-component
links $L_1$ and $L_2$ in $\mathbb{R}^3$ that are not ambient isotopic as oriented links with
ordered components: no ambient isotopy of $\mathbb{R}^3$ carries the first component of $L_1$ to
the first component of $L_2$ and the second component of $L_1$ to the second component of $L_2$,
each up to an orientation-preserving reparametrization of the circle.

## Sources

- Classical; see https://en.wikipedia.org/wiki/Linking_number. Problem `exists_nonisotopic_link` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.LinkingWanted.KnotTheory.exists_nonisotopic_link` is written with `theorem_wanted` in [WantedExt/Topology/LinkingWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/LinkingWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#exists-nonisotopic-link).

## Existence of non-isotopic knots

There are two oriented smooth knots $K_1$ and $K_2$ in
$\mathbb{R}^3$ that are not ambient-isotopic.

## Sources

- Classical; see https://en.wikipedia.org/wiki/Knot_invariant. Problem `exists_nonisotopic_knots` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.NonIsotopicKnotsWanted.KnotTheory.exists_nonisotopic_knots` is written with `theorem_wanted` in [WantedExt/Topology/NonIsotopicKnotsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/NonIsotopicKnotsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html#exists-nonisotopic-knots).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knots, links and ambient isotopy](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/knot-theory/knots-links-and-ambient-isotopy)
