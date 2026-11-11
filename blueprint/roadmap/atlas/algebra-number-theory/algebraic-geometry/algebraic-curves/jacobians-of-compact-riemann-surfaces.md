---
declaration: section
origin: cited
lean: MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.genus, MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.genus_eq_zero_iff_homeo, MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian, MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve, MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve_contMDiff, MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve_self, MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve_inj, MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pushforward
statement: formalized
---

# Jacobians of compact Riemann surfaces

17 results, 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html).

## Jacobian Challenge

## Genus of a compact Riemann surface

For a compact Riemann surface $X$, that is, a compact
connected Hausdorff space with a complex-analytic atlas modelled on $\mathbb{C}$, the genus of $X$
is a natural number.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.genus` is written with `def_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#genus).

## A compact Riemann surface has genus zero iff it is a sphere

Let $X$ be a compact
Riemann surface, that is, a compact connected Hausdorff space with a complex-analytic atlas
modelled on $\mathbb{C}$. The genus of $X$ is $0$ if and only if $X$ is homeomorphic to the unit
sphere in Euclidean space $\mathbb{R}^3$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.genus_eq_zero_iff_homeo` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#genus-eq-zero-iff-homeo).

## Jacobian of a compact Riemann surface

For a compact Riemann surface $X$, that is, a
compact connected Hausdorff space with a complex-analytic atlas modelled on $\mathbb{C}$, the
Jacobian $J(X)$ of $X$ is a type in the same universe as $X$.

Separate wanted instances make $J(X)$ a compact Hausdorff commutative complex Lie group modelled
on $\mathbb{C}^g$, where $g$ is the genus of $X$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian` is written with `def_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#jacobian).

## Abel–Jacobi map

Let $X$ be a compact Riemann surface with Jacobian $J(X)$. Each point
$P \in X$ gives a map $X \to J(X)$, the Abel–Jacobi map based at $P$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve` is written with `def_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#of-curve).

## The Abel–Jacobi map is holomorphic

Let $X$ be a compact Riemann surface of genus $g$,
and let $J(X)$ be its Jacobian, a complex manifold modelled on $\mathbb{C}^g$. For every point
$P \in X$, the Abel–Jacobi map $X \to J(X)$ based at $P$ is holomorphic.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve_contMDiff` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#of-curve-cont-mdiff).

## The Abel–Jacobi map sends the base point to zero

Let $X$ be a compact Riemann surface
with Jacobian $J(X)$, an abelian group. For every point $P \in X$, the Abel–Jacobi map
$X \to J(X)$ based at $P$ sends $P$ to $0$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve_self` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#of-curve-self).

## The Abel–Jacobi map is injective in positive genus

Let $X$ be a compact Riemann surface
with Jacobian $J(X)$, and let $P \in X$. If the genus of $X$ is positive, then the Abel–Jacobi map
$X \to J(X)$ based at $P$ is injective.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.ofCurve_inj` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#of-curve-inj).

## Pushforward on Jacobians

Let $X$ and $Y$ be compact Riemann surfaces, that is, compact,
connected, Hausdorff complex-analytic manifolds of dimension one, and write $J(X)$ for the
Jacobian of $X$, an abelian group with a topology. For a holomorphic map $f : X \to Y$, the
pushforward $f_*$ is a continuous group homomorphism from $J(X)$ to $J(Y)$. It is meant to be
the homomorphism induced by $f$; its properties are stated separately.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pushforward` is written with `def_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pushforward).

## The pushforward on Jacobians is holomorphic

Let $X$ and $Y$ be compact Riemann surfaces,
that is, compact, connected, Hausdorff complex-analytic manifolds of dimension one, of genera
$g_X$ and $g_Y$. The Jacobian $J(X)$ of $X$ is a complex-analytic manifold modeled on
$\mathbb{C}^{g_X}$, and likewise $J(Y)$ on $\mathbb{C}^{g_Y}$. For every holomorphic map
$f : X \to Y$, the pushforward $f_* : J(X) \to J(Y)$ is holomorphic.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pushforward_contMDiff` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pushforward-cont-mdiff).

## Pushforward along the identity

Let $X$ be a compact Riemann surface, that is, a compact,
connected, Hausdorff complex-analytic manifold of dimension one, and write $J(X)$ for its
Jacobian. For every $P \in J(X)$, the pushforward of $P$ along the identity map of $X$ is $P$:
$(\mathrm{id}_X)_*(P) = P$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pushforward_id_apply` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pushforward-id-apply).

## Pushforward respects composition

Let $X$, $Y$ and $Z$ be compact Riemann surfaces, that
is, compact, connected, Hausdorff complex-analytic manifolds of dimension one, and write $J(X)$
for the Jacobian of $X$. For all holomorphic maps $f : X \to Y$ and $g : Y \to Z$ and every
$P \in J(X)$, the pushforwards satisfy $(g \circ f)_*(P) = g_*(f_*(P))$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pushforward_comp_apply` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pushforward-comp-apply).

## Pullback on Jacobians

Let $X$ and $Y$ be compact Riemann surfaces, that is, compact,
connected, Hausdorff complex-analytic manifolds of dimension one, and write $J(X)$ for the
Jacobian of $X$, an abelian group with a topology. For a holomorphic map $f : X \to Y$, the
pullback $f^*$ is a continuous group homomorphism from $J(Y)$ to $J(X)$. It is meant to be the
zero map when $f$ is constant and the usual pullback along $f$ otherwise; its properties are
stated separately.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pullback` is written with `def_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pullback).

## The pullback map on Jacobians is holomorphic

Let $X$ and $Y$ be compact Riemann surfaces
of genus $g_X$ and $g_Y$, with Jacobians $J(X)$ and $J(Y)$, complex manifolds modelled on
$\mathbb{C}^{g_X}$ and $\mathbb{C}^{g_Y}$. For every holomorphic map $f : X \to Y$, the induced
pullback map $f^* : J(Y) \to J(X)$ is holomorphic.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pullback_contMDiff` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pullback-cont-mdiff).

## Pullback along the identity

Let $X$ be a compact Riemann surface, that is, a compact,
connected, Hausdorff complex-analytic manifold of dimension one, and write $J(X)$ for its
Jacobian. For every $P \in J(X)$, the pullback of $P$ along the identity map of $X$ is $P$:
$(\mathrm{id}_X)^*(P) = P$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pullback_id_apply` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pullback-id-apply).

## Pullback on Jacobians is compatible with composition

Let $X$, $Y$ and $Z$ be compact
Riemann surfaces, and for a holomorphic map $h$ between compact Riemann surfaces write $h^*$ for
the induced pullback map on Jacobians. For all holomorphic maps $f : X \to Y$ and $g : Y \to Z$
and every point $P$ of the Jacobian $J(Z)$, we have $(g \circ f)^*(P) = f^*(g^*(P))$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pullback_comp_apply` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pullback-comp-apply).

## Degree of a holomorphic map

Let $X$ and $Y$ be compact Riemann surfaces, that is,
compact connected Hausdorff spaces with a complex-analytic atlas modelled on $\mathbb{C}$. Every
holomorphic map $f : X \to Y$ has a degree, which is a natural number.

The intended value is $0$ when $f$ is constant and the usual degree of $f$ otherwise.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.degree` is written with `def_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#degree).

## Pushforward of a pullback is multiplication by the degree

Let $X$ and $Y$ be compact
Riemann surfaces, that is, compact, connected, Hausdorff complex-analytic manifolds of dimension
one, and write $J(Y)$ for the Jacobian of $Y$, an abelian group. For every holomorphic map
$f : X \to Y$ and every $P \in J(Y)$, the pushforward along $f$ of the pullback of $P$ along $f$
is $\deg(f) \cdot P$, where the degree $\deg(f)$ is a natural number:
$f_*(f^*(P)) = \deg(f) \cdot P$.

## Sources

- https://leanprover.zulipchat.com/#narrow/stream/583336-Autoformalization/topic/Jacobian%20challenge. Problem `jacobian_challenge_diffgeo` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.JacobianChallengeWanted.JacobianChallenge.Jacobian.pushforward_pullback` is written with `theorem_wanted` in [WantedExt/Geometry/JacobianChallengeWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/JacobianChallengeWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html#pushforward-pullback).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobians of compact Riemann surfaces](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/algebraic-curves/jacobians-of-compact-riemann-surfaces)
