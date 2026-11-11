---
declaration: section
origin: cited
lean: MetaMathlibExt.naiveHeight_lower_bound_of_unit_coeff, MetaMathlibExt.naiveHeight_lower_bound_of_special_coeff, MetaMathlibExt.naiveHeight_lt_sqrt_mul_naiveHeight_x_rpow, MetaMathlibExt.naiveHeight_gt_of_small_linear_coeff
statement: formalized
---

# Heights of rational points on elliptic curves

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/heights-of-rational-points-on-elliptic-curves/index.html).

## Height lower bounds on $y^2 = x^3 + ax + b$ when $a = \pm 1$ or $b = \pm 1$

Let
$a, b \in \mathbb{Z}$ with $4a^3 + 27b^2 \ne 0$, and for $u, v \in \mathbb{Q}$ let
$H(u, v) = \max(|U|, |V|, |W|)$, where $U, V, W$ are coprime integers with
$(U : V : W) = (u : v : 1)$. Consider the rational solutions $(u, v)$ of $v^2 = u^3 + au + b$.
(a) If $a = \pm 1$ and $b \notin \{0, 1, -1\}$, every solution has $H(u, v) \ge (|b|/5)^{1/3}$.
(b) If $a \notin \{0, 1, -1\}$ and $b = -1$, every solution has $H(u, v) \ge (|a|/5)^{1/3}$.
(c) If $a \notin \{0, 1, -1\}$ and $b = 1$, every solution with $H(u, v) < (|a|/5)^{1/3}$ is
$(0, 1)$ or $(0, -1)$.

## Sources

- Dimitrios Poulakis, *Lower Bounds for the Height of Rational Points of Elliptic Curves*, INTEGERS 25 (2025), Article A66, Theorem 2.

Stated but not proved: `MetaMathlibExt.naiveHeight_lower_bound_of_unit_coeff` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/heights-of-rational-points-on-elliptic-curves/index.html#naive-height-lower-bound-of-unit-coeff).

## Height lower bounds on $y^2 = x^3 + ax + b$ when $b = \pm a$, $b = 0$ or $a = 0$

Let
$a, b \in \mathbb{Z}$ with $4a^3 + 27b^2 \ne 0$, and for $u, v \in \mathbb{Q}$ let
$H(u, v) = \max(|U|, |V|, |W|)$, where $U, V, W$ are coprime integers with
$(U : V : W) = (u : v : 1)$. Consider the rational solutions $(u, v)$ of $v^2 = u^3 + au + b$.
(a) If $b = a$, every solution has $H(u, v) \ge (|a|/4)^{1/3}$.
(b) If $b = -a$, every solution with $H(u, v) < (|a|/4)^{1/3}$ is $(1, 1)$ or $(1, -1)$.
(c) If $b = 0$, every solution with $H(u, v) < (|a|/4)^{1/3}$ is $(0, 0)$.
(d) If $a = 0$, every solution has $H(u, v) \ge (|b|/3)^{1/3}$.

In (b) the points $(1, \pm 1)$ and the point at infinity need not form a subgroup of order
three: for $a = 5$, doubling $(1, 1)$ gives $(14, -53)$.

## Sources

- Dimitrios Poulakis, *Lower Bounds for the Height of Rational Points of Elliptic Curves*, INTEGERS 25 (2025), Article A66, Theorem 3.

Stated but not proved: `MetaMathlibExt.naiveHeight_lower_bound_of_special_coeff` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/heights-of-rational-points-on-elliptic-curves/index.html#naive-height-lower-bound-of-special-coef).

## Height of a point on $y^2 = x^3 + ax - b$ versus the height of its $x$-coordinate

Let
$a, b \in \mathbb{Z}$ with $a \ne 0$, $b > 0$ and $4a^3 + 27b^2 \ne 0$. For $u \in \mathbb{Q}$
let $H(u) = \max(|u_0|, u_1)$, where $u = u_0/u_1$ in lowest terms with $u_1 > 0$, and for
$u, v \in \mathbb{Q}$ let $H(u, v) = \max(|U|, |V|, |W|)$, where $U, V, W$ are coprime integers
with $(U : V : W) = (u : v : 1)$. Then every rational solution $(u, v)$ of
$v^2 = u^3 + au - b$ satisfies $H(u, v) < \sqrt{1 + |a|}\, H(u)^{3/2}$.

## Sources

- Dimitrios Poulakis, *Lower Bounds for the Height of Rational Points of Elliptic Curves*, INTEGERS 25 (2025), Article A66, Lemma 4.

Stated but not proved: `MetaMathlibExt.naiveHeight_lt_sqrt_mul_naiveHeight_x_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/heights-of-rational-points-on-elliptic-curves/index.html#naive-height-lt-sqrt-mul-naive-height-x).

## Height lower bound on $y^2 = x^3 + ax + b$ when $|a|$ is small

Let $a, b \in \mathbb{Z}$
with $ab \ne 0$ and $4a^3 + 27b^2 \ne 0$, let $\lVert p \rVert = \sqrt{2 + a^2 + b^2}$, and suppose
$1 + |a| < \lVert p \rVert^{1/2}/1.782$. For $u, v \in \mathbb{Q}$ let
$H(u, v) = \max(|U|, |V|, |W|)$, where $U, V, W$ are coprime integers with
$(U : V : W) = (u : v : 1)$. Then every rational solution $(u, v)$ of $v^2 = u^3 + au + b$ with
$uv \ne 0$ satisfies $H(u, v) > \lVert p \rVert^{1/6}/1.634$.

## Sources

- Dimitrios Poulakis, *Lower Bounds for the Height of Rational Points of Elliptic Curves*, INTEGERS 25 (2025), Article A66, Corollary 1.

Stated but not proved: `MetaMathlibExt.naiveHeight_gt_of_small_linear_coeff` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EllipticCurveNaiveHeightLowerBoundsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/heights-of-rational-points-on-elliptic-curves/index.html#naive-height-gt-of-small-linear-coeff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heights of rational points on elliptic curves](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/heights-of-rational-points-on-elliptic-curves/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-geometry/heights-of-rational-points-on-elliptic-curves)
