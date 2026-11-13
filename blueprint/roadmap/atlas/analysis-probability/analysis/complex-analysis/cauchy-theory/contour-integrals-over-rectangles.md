---
declaration: section
origin: cited
lean: Complex.integral_div_add_sq, Complex.odd_integral_eq_zero, Complex.vertical_side_one_div, Complex.horiz_diff_one_div, Complex.boundary_rect_one_div, Complex.boundary_rect_one_div_outside, RectilinearRectangle, RectilinearRectangle.ofBounds
statement: formalized
proof: formalized
---

# Contour integrals over rectangles

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html).

## Arctangent integral

For real numbers $a$, $b$ and $d$ with $d \ne 0$,
$\int_a^b \frac{d}{x^2 + d^2}\,dx = \arctan\frac{b}{d} - \arctan\frac{a}{d}$.

Formalized by `Complex.integral_div_add_sq`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral-div-add-sq).

## Integral of an odd function over a symmetric interval

If $f : \mathbb{R} \to \mathbb{R}$
satisfies $f(-x) = -f(x)$ for every real $x$, then $\int_{-T}^{T} f(x)\,dx = 0$ for every real
$T$.

Formalized by `Complex.odd_integral_eq_zero`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#odd-integral-eq-zero).

## Integral of $1/(c + iy)$ over a symmetric interval

For real numbers $c \ne 0$ and
$T \ge 0$, $\int_{-T}^{T} \frac{1}{c + iy}\,dy = 2\arctan(T/c)$, where the integrand is complex
valued and the integral is taken over the real variable $y$.

Formalized by `Complex.vertical_side_one_div`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#vertical-side-one-div).

## Difference of horizontal integrals of the reciprocal

Let $a \le b$ and $T \ne 0$ be
real numbers. Then
$\int_a^b \frac{dx}{x - iT} - \int_a^b \frac{dx}{x + iT}
= 2i\left(\arctan\frac{b}{T} - \arctan\frac{a}{T}\right)$.

Formalized by `Complex.horiz_diff_one_div`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#horiz-diff-one-div).

## Rectangle integral of $1/s$ around the origin

Let $a, b, T$ be real numbers with
$a < 0 < b$ and $T > 0$. Then

$$\int_a^b \frac{dx}{x - iT} - \int_a^b \frac{dx}{x + iT} +
i \left( \int_{-T}^{T} \frac{dy}{b + iy} - \int_{-T}^{T} \frac{dy}{a + iy} \right) = 2\pi i,$$

that is, the integral of $1/s$ over the positively oriented boundary of the rectangle with
corners $a - iT$ and $b + iT$ equals $2\pi i$.

Formalized by `Complex.boundary_rect_one_div`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-rect-one-div).

## Rectangle integral of $1/s$ with the pole outside

Let $a, b, T$ be real numbers with
$0 < a \le b$ and $T > 0$. Then

$$\int_a^b \frac{dx}{x - iT} - \int_a^b \frac{dx}{x + iT} +
i \left( \int_{-T}^{T} \frac{dy}{b + iy} - \int_{-T}^{T} \frac{dy}{a + iy} \right) = 0,$$

that is, the integral of $1/s$ over the positively oriented boundary of the rectangle with
corners $a - iT$ and $b + iT$ vanishes.

Formalized by `Complex.boundary_rect_one_div_outside`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-rect-one-div-outside).

## Rectilinear rectangle

A rectilinear rectangle is an axis-parallel rectangle in the complex
plane, recorded by an ordered pair of complex numbers $z$ and $w$, its first and second corner,
which are opposite corners of the rectangle.

Degenerate rectangles, in which $z$ and $w$ have the same real part or the same imaginary part, are
allowed. The corners and their order determine the orientation of the boundary integral over the
rectangle, and the boundary integral over a degenerate rectangle is zero.

Formalized by `RectilinearRectangle`, a structure declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#rectilinear-rectangle).

## Rectangle with given coordinate bounds

For real numbers $x_0, x_1, y_0, y_1$, this is the
rectilinear rectangle whose first corner is $x_0 + i y_0$ and whose second corner is
$x_1 + i y_1$.

Formalized by `RectilinearRectangle.ofBounds`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#of-bounds).

## Carrier of an axis-parallel rectangle

For an axis-parallel rectangle with opposite
corners $z$ and $w$, its carrier is the closed rectangle of all $u \in \mathbb{C}$ such that
$\operatorname{Re} u$ lies in the closed interval with endpoints $\operatorname{Re} z$ and
$\operatorname{Re} w$, and $\operatorname{Im} u$ lies in the closed interval with endpoints
$\operatorname{Im} z$ and $\operatorname{Im} w$.

Formalized by `RectilinearRectangle.carrier`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#carrier).

## Boundary integral over a rectangle

Let $E$ be a complex Banach space and let $R$ be a
rectilinear rectangle with first corner $z$ and second corner $w$. The boundary integral of a
function $f : \mathbb{C} \to E$ over $R$ is

$$\int_{\operatorname{Re} z}^{\operatorname{Re} w} f(x + i \operatorname{Im} z)\,dx -
\int_{\operatorname{Re} z}^{\operatorname{Re} w} f(x + i \operatorname{Im} w)\,dx +
i \int_{\operatorname{Im} z}^{\operatorname{Im} w} f(\operatorname{Re} w + iy)\,dy -
i \int_{\operatorname{Im} z}^{\operatorname{Im} w} f(\operatorname{Re} z + iy)\,dy,$$

where each integral is an oriented Bochner interval integral, so $\int_a^b = -\int_b^a$.

The corner order determines the sign; when $\operatorname{Re} z \le \operatorname{Re} w$ and
$\operatorname{Im} z \le \operatorname{Im} w$ this is the integral of $f$ over the positively
oriented boundary of the rectangle.

Formalized by `RectilinearRectangle.boundaryIntegral`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral).

## Cauchy–Goursat theorem for rectangles

Let $E$ be a complex Banach space, let $R$ be a
rectilinear rectangle and let $f : \mathbb{C} \to E$ be complex differentiable on the closed
rectangle spanned by the corners of $R$ (the carrier of $R$). Then the boundary integral of $f$
over $R$ is $0$.

Formalized by `RectilinearRectangle.boundaryIntegral_eq_zero`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral-eq-zero).

## Gluing rectangles along a horizontal side

Let $E$ be a complex Banach space, let
$f : \mathbb{C} \to E$ and let $x_0, x_1, y_0, y_1, y_2$ be real numbers such that the maps
$y \mapsto f(x_0 + iy)$ and $y \mapsto f(x_1 + iy)$ are continuous on $\mathbb{R}$. For real
$a, b, c, d$ write $R(a, b, c, d)$ for the rectangle with corners $a + ic$ and $b + id$. Then the
boundary integral of $f$ over $R(x_0, x_1, y_0, y_2)$ equals the sum of the boundary integrals of
$f$ over $R(x_0, x_1, y_0, y_1)$ and over $R(x_0, x_1, y_1, y_2)$.

No ordering of $y_0, y_1, y_2$ is assumed: the common horizontal side cancels and the vertical
integrals concatenate as oriented integrals.

Formalized by `RectilinearRectangle.boundaryIntegral_ofBounds_horizontal_concat`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral-of-bounds-horizontal-c).

## Gluing rectangles along a vertical side

Let $E$ be a complex Banach space, let
$f : \mathbb{C} \to E$ and let $x_0, x_1, x_2, y_0, y_1$ be real numbers such that the maps
$x \mapsto f(x + iy_0)$ and $x \mapsto f(x + iy_1)$ are continuous on $\mathbb{R}$. For real
$a, b, c, d$ write $R(a, b, c, d)$ for the rectangle with corners $a + ic$ and $b + id$. Then the
boundary integral of $f$ over $R(x_0, x_2, y_0, y_1)$ equals the sum of the boundary integrals of
$f$ over $R(x_0, x_1, y_0, y_1)$ and over $R(x_1, x_2, y_0, y_1)$.

No ordering of $x_0, x_1, x_2$ is assumed: the common vertical side cancels and the horizontal
integrals concatenate as oriented integrals.

Formalized by `RectilinearRectangle.boundaryIntegral_ofBounds_vertical_concat`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral-of-bounds-vertical-con).

## Cauchy kernel with the pole outside a rectangle

Let $R$ be a rectilinear rectangle and
let $w$ be a complex number that does not lie in the closed rectangle spanned by the corners of
$R$ (the carrier of $R$). Then the boundary integral of $z \mapsto 1/(z - w)$ over $R$ is $0$.

Formalized by `RectilinearRectangle.boundaryIntegral_inv_sub_eq_zero_of_not_mem_carrier`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral-inv-sub-eq-zero-of-not).

## Rectangle integral of $1/z$ around the origin

Let $a, b, T$ be real numbers with
$a < 0 < b$ and $T > 0$. Then the boundary integral of $z \mapsto 1/z$ over the rectangle with
corners $a - iT$ and $b + iT$ equals $2\pi i$.

Formalized by `RectilinearRectangle.boundaryIntegral_ofBounds_inv_eq_two_pi_mul_I`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral-of-bounds-inv-eq-two-p).

## Translating the Cauchy kernel to the origin

For all real numbers $x_0, x_1, y_0, y_1$ and
every complex number $w$, the boundary integral of $z \mapsto 1/(z - w)$ over the rectangle with
corners $x_0 + iy_0$ and $x_1 + iy_1$ equals the boundary integral of $z \mapsto 1/z$ over the
rectangle with corners $(x_0 - \operatorname{Re} w) + i(y_0 - \operatorname{Im} w)$ and
$(x_1 - \operatorname{Re} w) + i(y_1 - \operatorname{Im} w)$.

Formalized by `RectilinearRectangle.boundaryIntegral_ofBounds_inv_sub_eq_translate`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 518](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L518). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral-of-bounds-inv-sub-eq-t).

## Rectangle integral of the Cauchy kernel at an interior point

Let $x_0, x_1, y_0, y_1$ be
real numbers and let $w$ be a complex number with $x_0 < \operatorname{Re} w < x_1$ and
$y_0 < \operatorname{Im} w < y_1$. Then the boundary integral of $z \mapsto 1/(z - w)$ over the
rectangle with corners $x_0 + iy_0$ and $x_1 + iy_1$ equals $2\pi i$.

Formalized by `RectilinearRectangle.boundaryIntegral_ofBounds_inv_sub_eq_two_pi_mul_I`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#boundary-integral-of-bounds-inv-sub-eq-t-2).

## Rectilinear cycle

A rectilinear cycle is a finitely supported function from rectilinear
rectangles to $\mathbb{Z}$, that is, a finite formal sum $\sum_r n_r\, r$ of rectilinear
rectangles $r$ with integer coefficients $n_r$, read as the corresponding integer combination of
oriented rectangle boundaries.

A negative coefficient reverses the orientation of the corresponding boundary.

Formalized by `RectilinearCycle`, an abbreviation declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#rectilinear-cycle).

## The cycle of a single rectangle

For a rectilinear rectangle $r$, this is the rectilinear
cycle in which $r$ has coefficient $1$ and every other rectangle has coefficient $0$, that is, the
boundary of $r$ with the orientation given by its corner order.

Formalized by `RectilinearCycle.ofRectangle`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 628](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#of-rectangle).

## Contour integral over a rectilinear cycle

Let $E$ be a complex Banach space and
$f : \mathbb{C} \to E$. For a rectilinear cycle $\Gamma$, a finite formal sum $\sum_r n_r\, r$ of
rectangles $r$ with integer coefficients $n_r$, the contour integral of $f$ over $\Gamma$ is
$\sum_r n_r \int_{\partial r} f$, where $\int_{\partial r} f$ is the boundary integral of $f$
over the oriented rectangle $r$.

Formalized by `RectilinearCycle.integral`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral).

## Additivity of the contour integral in the cycle

Let $E$ be a complex Banach space and
$f : \mathbb{C} \to E$. For rectilinear cycles $\Gamma$ and $\Lambda$, the contour integral of
$f$ over $\Gamma + \Lambda$ equals the integral of $f$ over $\Gamma$ plus the integral of $f$
over $\Lambda$.

Formalized by `RectilinearCycle.integral_add`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral-add).

## Reversing a cycle negates its integral

For every rectilinear cycle $\Gamma$, every
complex Banach space $E$ and every function $f : \mathbb{C} \to E$, the contour integral of $f$
over $-\Gamma$ is the negative of the contour integral of $f$ over $\Gamma$.

Formalized by `RectilinearCycle.integral_neg`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral-neg).

## Integral over a difference of cycles

For rectilinear cycles $\Gamma$ and $\Lambda$, a
complex Banach space $E$ and a function $f : \mathbb{C} \to E$, the contour integral of $f$ over
$\Gamma - \Lambda$ equals the contour integral of $f$ over $\Gamma$ minus the contour integral of
$f$ over $\Lambda$.

Formalized by `RectilinearCycle.integral_sub`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral-sub).

## Contour integration as an additive map

Let $E$ be a complex Banach space and
$f : \mathbb{C} \to E$. The map sending a rectilinear cycle $\Gamma$ to the contour integral of
$f$ over $\Gamma$ is an additive group homomorphism from rectilinear cycles to $E$.

Formalized by `RectilinearCycle.integralAddHom`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 675](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L675). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral-add-hom).

## Rectangle filling supported in a set

Let $G \subseteq \mathbb{C}$. A rectilinear cycle
$\Gamma$, read as a filling by rectangles, is supported in $G$ when, for every rectangle $r$ whose
coefficient in $\Gamma$ is nonzero, the closed carrier of $r$ is contained in $G$.

Formalized by `RectilinearCycle.FillingSupportedIn`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#filling-supported-in).

## Cauchy–Goursat theorem for rectilinear cycles

Let $E$ be a complex Banach space, let
$G \subseteq \mathbb{C}$, and let $f : \mathbb{C} \to E$ be complex differentiable on $G$. If
$\Gamma$ is a rectilinear cycle whose rectangle filling is supported in $G$, that is, the closed
rectangle of every rectangle occurring in $\Gamma$ with nonzero coefficient is contained in $G$,
then the contour integral of $f$ over $\Gamma$ is $0$.

Formalized by `RectilinearCycle.integral_eq_zero_of_fillingSupportedIn`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral-eq-zero-of-filling-supported-in).

## Rectilinear cycles homologous in a set

Let $G \subseteq \mathbb{C}$. Two rectilinear
cycles $\Gamma$ and $\Lambda$ are homologous in $G$ when the rectangle filling of
$\Gamma - \Lambda$ is supported in $G$: every rectangle with nonzero coefficient in
$\Gamma - \Lambda$ has its closed carrier contained in $G$.

Formalized by `RectilinearCycle.HomologousIn`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 719](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L719). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#homologous-in).

## Homologous rectilinear cycles have equal integrals

Let $E$ be a complex Banach space,
let $G \subseteq \mathbb{C}$, and let $f : \mathbb{C} \to E$ be complex differentiable on $G$. If
$\Gamma$ and $\Lambda$ are rectilinear cycles that are homologous in $G$, that is, the closed
rectangle of every rectangle occurring in $\Gamma - \Lambda$ with nonzero coefficient is contained
in $G$, then the contour integral of $f$ over $\Gamma$ equals the contour integral of $f$ over
$\Lambda$.

Formalized by `RectilinearCycle.integral_eq_of_homologousIn`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 724](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L724). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#integral-eq-of-homologous-in).

## Index of a rectilinear cycle

For a rectilinear cycle $\Gamma$ and a point
$w \in \mathbb{C}$, the index of $\Gamma$ about $w$ is
$\frac{1}{2\pi i}\int_\Gamma \frac{dz}{z - w}$, the contour integral over $\Gamma$ of
$z \mapsto (z - w)^{-1}$, multiplied by $(2\pi i)^{-1}$.

With the conventions $0^{-1} = 0$ and that a non-integrable integral is $0$, the formula also
has a value when $w$ lies on the boundary of a rectangle occurring in $\Gamma$; no geometric
winding-number claim is made there.

Formalized by `RectilinearCycle.index`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#index-2).

## Winding index as an additive map

For a fixed point $w \in \mathbb{C}$, the map sending a
rectilinear cycle $\Gamma$ to its index about $w$ is an additive group homomorphism from
rectilinear cycles to $\mathbb{C}$.

Formalized by `RectilinearCycle.indexAddHom`, a definition declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 754](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L754). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#index-add-hom).

## Rectangle index vanishes outside the rectangle

For an axis-parallel rectangle $r$ and a
point $w \in \mathbb{C}$ outside the closed carrier of $r$, the index about $w$ of the cycle
consisting of the boundary of $r$ is $0$.

Formalized by `RectilinearCycle.index_ofRectangle_eq_zero_of_not_mem_carrier`, a theorem declared in [MathlibExt/Analysis/Complex/RectilinearCycle.lean, line 771](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/RectilinearCycle.lean#L771). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html#index-of-rectangle-eq-zero-of-not-mem-ca).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Contour integrals over rectangles](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/contour-integrals-over-rectangles)
