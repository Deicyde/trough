---
declaration: section
origin: cited
lean: MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.Plane, MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.period, MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.velocity, MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.det2, MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.signedArea, MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.IsPositiveSimpleClosedUnitSpeedCurve, MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.IsTangentAngleLift, MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.signedCurvature
statement: formalized
---

# Hopf's Umlaufsatz

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html).

## Euclidean plane for the Umlaufsatz

The Euclidean plane is the space $\mathbb{R}^2$ of
pairs of real numbers with the Euclidean inner product and norm.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.Plane`, an abbreviation declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#plane).

## Parameter period for the Umlaufsatz

The parameter period of the closed curves in the
Hopf Umlaufsatz is the real number $2\pi$.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.period`, a definition declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#period).

## Velocity of a plane curve

For a curve $r : \mathbb{R} \to \mathbb{R}^2$ in the Euclidean
plane and $t \in \mathbb{R}$, the velocity of $r$ at $t$ is its derivative $r'(t) \in \mathbb{R}^2$,
taken to be $0$ where $r$ is not differentiable.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.velocity`, a definition declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#velocity).

## Planar determinant for the Umlaufsatz

For vectors $u = (u_0, u_1)$ and
$v = (v_0, v_1)$ in the Euclidean plane $\mathbb{R}^2$, $\det(u, v) = u_0 v_1 - u_1 v_0$, the
signed area of the parallelogram spanned by $u$ and $v$.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.det2`, a definition declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#det2).

## Signed area of a closed plane curve

For a curve $r : \mathbb{R} \to \mathbb{R}^2$, the
signed area is $\frac{1}{2}\int_0^{2\pi} \det(r(t), r'(t))\,dt$, where $r'$ is the velocity of
$r$ and $\det(u, v) = u_0 v_1 - u_1 v_0$ (Green's normalization). Its sign fixes the orientation
convention.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.signedArea`, a definition declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#signed-area).

## Positively oriented simple closed unit-speed curve

A curve
$r : \mathbb{R} \to \mathbb{R}^2$ in the Euclidean plane is a positively oriented simple closed
unit-speed curve when it is continuously differentiable, periodic with period $2\pi$, injective on
$[0, 2\pi)$, has velocity of norm $\lVert r'(t) \rVert = 1$ for every $t \in \mathbb{R}$, and has
positive signed area $\frac{1}{2}\int_0^{2\pi} \det(r(t), r'(t))\,dt > 0$, where
$\det(u, v) = u_0 v_1 - u_1 v_0$.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.IsPositiveSimpleClosedUnitSpeedCurve`, a structure declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#is-positive-simple-closed-unit-speed-cur).

## Tangent-angle lift

For a curve $r : \mathbb{R} \to \mathbb{R}^2$ in the Euclidean plane,
a function $\alpha : \mathbb{R} \to \mathbb{R}$ is a tangent-angle lift of $r$ when $\alpha$ is
continuously differentiable and the velocity of $r$ satisfies
$r'(t) = (\cos \alpha(t), \sin \alpha(t))$ for every $t \in \mathbb{R}$.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.IsTangentAngleLift`, a structure declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#is-tangent-angle-lift).

## Signed curvature

For a function $\alpha : \mathbb{R} \to \mathbb{R}$ and
$t \in \mathbb{R}$, the signed curvature of $\alpha$ at $t$ is the derivative $\alpha'(t)$, taken
to be $0$ where $\alpha$ is not differentiable at $t$.

When $\alpha$ is a tangent-angle lift of a unit-speed plane curve, this is the signed curvature
of the curve at $t$.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.signedCurvature`, a definition declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#signed-curvature).

## Total signed curvature of a tangent-angle lift

For a function
$\alpha : \mathbb{R} \to \mathbb{R}$, the total signed curvature is $\int_0^{2\pi} \alpha'(t)\,dt$,
the integral of the signed curvature $\alpha'$ over one parameter period $[0, 2\pi]$.

Formalized by `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.totalCurvature`, a definition declared in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#total-curvature).

## Hopf's Umlaufsatz

Let $r : \mathbb{R} \to \mathbb{R}^2$ be a positively oriented simple
closed unit-speed plane curve: $r$ is continuously differentiable and $2\pi$-periodic, injective
on $[0, 2\pi)$, satisfies $\lVert r'(t) \rVert = 1$ for all $t$, and has positive signed area
$\frac{1}{2}\int_0^{2\pi} \det(r(t), r'(t))\,dt > 0$, where $\det(u, v) = u_0 v_1 - u_1 v_0$.
Let $\alpha : \mathbb{R} \to \mathbb{R}$ be a continuously differentiable tangent-angle lift of
$r$, that is, $r'(t) = (\cos \alpha(t), \sin \alpha(t))$ for all $t$. Then the total signed
curvature over one period is $2\pi$: $\int_0^{2\pi} \alpha'(t)\,dt = 2\pi$.

## Sources

- H. Hopf, *Über die Drehung der Tangenten...*, Compositio Math. 2 (1935). Knill, §170. Problem `hopf_umlaufsatz` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.HopfUmlaufsatzWanted.Geometry.HopfUmlaufsatz.hopf_umlaufsatz` is written with `theorem_wanted` in [WantedExt/Geometry/HopfUmlaufsatzWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HopfUmlaufsatzWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html#hopf-umlaufsatz).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hopf's Umlaufsatz](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/curves-and-surfaces/hopf-s-umlaufsatz)
