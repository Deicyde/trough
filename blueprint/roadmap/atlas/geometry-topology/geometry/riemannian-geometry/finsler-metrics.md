---
declaration: section
origin: cited
lean: Manifold.FinslerMetric, Manifold.FinslerMetric.IsReversible, Manifold.FinslerMetric.edist, Manifold.FinslerMetric.IsGeodesicOnWithSpeed, Manifold.FinslerMetric.IsGeodesic, Manifold.FinslerMetric.IsClosedGeodesic, Manifold.FinslerMetric.euclidean, Manifold.FinslerMetric.euclidean_isReversible
statement: formalized
proof: formalized
---

# Finsler metrics

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html).

## Manifold

## Finsler metric

Let $M$ be a $C^\infty$ manifold (possibly with boundary or corners)
modelled on a finite-dimensional real normed space $E$, so that each tangent space $T_xM$ is $E$.
A $C^\infty$ Finsler metric on $M$ is a continuous function $F : TM \to \mathbb{R}$ that is
$C^\infty$ off the zero section, satisfies $F(x, v) > 0$ for every $x \in M$ and every nonzero
$v \in T_xM$, is positively homogeneous of degree one on each fiber, that is
$F(x, cv) = c\,F(x, v)$ for all $x \in M$, $v \in T_xM$ and real $c > 0$, and is strongly convex:
for every $x \in M$ and all nonzero $v, w \in E$, the second derivative at $v$ of the function
$u \mapsto F(x, u)^2$ on $E$ satisfies $D^2\big(F(x, \cdot)^2\big)(v)(w, w) > 0$.

## Sources

- Bao–Chern–Shen, *An Introduction to Riemann–Finsler Geometry*, §1.1, where $F$ takes values in $[0, \infty)$ and the Hessian is that of $F^2/2$.

Formalized by `Manifold.FinslerMetric`, a structure declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#finsler-metric).

## Reversible Finsler metric

A Finsler metric $F$ on a manifold $M$ is reversible if
$F(x, -v) = F(x, v)$ for every point $x \in M$ and every tangent vector $v \in T_xM$.

Formalized by `Manifold.FinslerMetric.IsReversible`, a definition declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#is-reversible).

## Forward Finsler distance

Let $F$ be a Finsler metric on a manifold $M$. The forward
Finsler distance from $x \in M$ to $y \in M$ is the value in $[0, \infty]$

$$
d_F(x, y) = \inf_\gamma \int_0^1 F(\gamma(t), \gamma'(t))\, dt,
$$

the infimum over all $C^1$ paths $\gamma : [0, 1] \to M$ from $x$ to $y$; it is $\infty$ when
there is no such path.

It is not symmetric unless $F$ is reversible.

## Sources

- Bao–Chern–Shen, *An Introduction to Riemann–Finsler Geometry*, §6.2. The formula is that of Mathlib's `riemannianEDist` with `‖v‖ₑ` replaced by `F v`.

Formalized by `Manifold.FinslerMetric.edist`, a definition declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#edist).

## Finsler geodesic of given speed on a set of times

Let $F$ be a Finsler metric on a
manifold $M$ with forward distance $d_F$, let $\gamma : \mathbb{R} \to M$ be a curve, let
$s \subseteq \mathbb{R}$ be a set of times and let $c \ge 0$ be a real number. Then $\gamma$ is a
geodesic of speed $c$ of $F$ on $s$ if for every $t \in s$ there is $\varepsilon > 0$ such that
$d_F(\gamma(t_1), \gamma(t_2)) = c\,(t_2 - t_1)$ for all $t_1, t_2 \in s$ with $t_1 \le t_2$,
$|t_1 - t| < \varepsilon$ and $|t_2 - t| < \varepsilon$.

Formalized by `Manifold.FinslerMetric.IsGeodesicOnWithSpeed`, a definition declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#is-geodesic-on-with-speed).

## Finsler geodesic

Let $F$ be a Finsler metric on a manifold $M$. A curve
$\gamma : \mathbb{R} \to M$ is a geodesic of $F$ if there is a real number $c \ge 0$ such that
$\gamma$ is a geodesic of speed $c$ of $F$ on all of $\mathbb{R}$.

Formalized by `Manifold.FinslerMetric.IsGeodesic`, a definition declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#is-geodesic).

## Closed Finsler geodesic

Let $F$ be a Finsler metric on a manifold $M$. A curve
$\gamma : \mathbb{R} \to M$ is a closed geodesic of $F$ if it is a geodesic of $F$, it is periodic
with some period $T > 0$, that is $\gamma(t + T) = \gamma(t)$ for all real $t$, and it is not
constant: $\gamma(t_1) \ne \gamma(t_2)$ for some real $t_1, t_2$.

Formalized by `Manifold.FinslerMetric.IsClosedGeodesic`, a definition declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#is-closed-geodesic).

## Euclidean Finsler metric

Let $V$ be a finite-dimensional real inner product space,
viewed as a smooth manifold whose tangent spaces are $V$ itself. The Euclidean Finsler metric on
$V$ is $F(x, v) = \|v\|$ for $x \in V$ and $v \in T_xV = V$.

Formalized by `Manifold.FinslerMetric.euclidean`, a definition declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#euclidean).

## The Euclidean Finsler metric is reversible

For every finite-dimensional real inner
product space $V$, the Euclidean Finsler metric $F(x, v) = \|v\|$ on $V$ is reversible:
$F(x, -v) = F(x, v)$ for all $x, v \in V$.

Formalized by `Manifold.FinslerMetric.euclidean_isReversible`, a theorem declared in [MathlibExt/Geometry/Manifold/Finsler.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Finsler.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html#euclidean-is-reversible).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finsler metrics](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/finsler-metrics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/finsler-metrics)
