---
declaration: section
origin: cited
lean: PerronKernel.perronKernel, PerronKernel.continuous_perronKernel_integrand, PerronKernel.exp_sub_one_eq, PerronKernel.E1, PerronKernel.E1_zero, PerronKernel.E1_eq_div, PerronKernel.E1_sub_one_le, PerronKernel.E1_continuousAt_zero
statement: formalized
proof: formalized
---

# Perron's formula

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html).

## Truncated Perron kernel

For real numbers $y$, $c$ and $T$, the truncated Perron kernel is
the complex number

$$K(y, c, T) = \frac{1}{2\pi}\int_{-T}^{T} \frac{y^{c+it}}{c+it}\,dt,$$

where $y^s$ is the principal complex power of $y$ viewed as a complex number.

Writing $s = c + it$, this is $\frac{1}{2\pi i}\int_{c-iT}^{c+iT} \frac{y^s}{s}\,ds$ along the
vertical segment.

Formalized by `PerronKernel.perronKernel`, a definition declared in [MathlibExt/Analysis/PerronKernel.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-kernel).

## Continuity of the Perron kernel integrand

Let $y > 0$ and $c \ne 0$ be real numbers.
Then the function from $\mathbb{R}$ to $\mathbb{C}$ sending $t$ to $y^{c+it}/(c+it)$, where
$y^{c+it}$ is the complex power, is continuous.

Formalized by `PerronKernel.continuous_perronKernel_integrand`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#continuous-perron-kernel-integrand).

## Integral formula for $e^w - 1$

For every complex number $w$,

$$e^w - 1 = w \int_0^1 e^{tw}\,dt,$$

where $t$ ranges over the real interval $[0, 1]$.

Formalized by `PerronKernel.exp_sub_one_eq`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#exp-sub-one-eq).

## The averaging operator $E_1$

For a complex number $u$, define
$E_1(u) = \int_0^1 e^{tu}\,dt$, the integral being over real $t$ from $0$ to $1$.

Formalized by `PerronKernel.E1`, a definition declared in [MathlibExt/Analysis/PerronKernel.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1).

## Value of the averaging operator at zero

Let $E_1(u) = \int_0^1 e^{tu}\,dt$ for
$u \in \mathbb{C}$. Then $E_1(0) = 1$.

Formalized by `PerronKernel.E1_zero`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1-zero).

## The averaging operator as a difference quotient

Let $E_1(u) = \int_0^1 e^{tu}\,dt$ for
$u \in \mathbb{C}$. Then $E_1(u) = (e^u - 1)/u$ for every nonzero complex number $u$.

Formalized by `PerronKernel.E1_eq_div`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1-eq-div).

## Linear bound for the averaging operator near zero

Let $E_1(u) = \int_0^1 e^{tu}\,dt$ for
$u \in \mathbb{C}$. For every complex number $v$ with $|v| \le 1$, we have
$|E_1(v) - 1| \le |v|$.

Formalized by `PerronKernel.E1_sub_one_le`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1-sub-one-le).

## Continuity of the averaging operator at zero

The function
$E_1 : \mathbb{C} \to \mathbb{C}$ given by $E_1(u) = \int_0^1 e^{tu}\,dt$ is continuous at $0$.

Formalized by `PerronKernel.E1_continuousAt_zero`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1-continuous-at-zero).

## Continuity of the averaging operator

The function $E_1 : \mathbb{C} \to \mathbb{C}$ given
by $E_1(u) = \int_0^1 e^{tu}\,dt$ is continuous.

Formalized by `PerronKernel.E1_continuous`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1-continuous).

## Derivative of the averaging operator

Let $E_1(u) = \int_0^1 e^{tu}\,dt$ for
$u \in \mathbb{C}$. For every $x_0 \in \mathbb{C}$, the function $E_1$ has complex derivative
$\int_0^1 t\,e^{t x_0}\,dt$ at $x_0$.

Formalized by `PerronKernel.E1_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1-has-deriv-at).

## The averaging operator is entire

The function $E_1 : \mathbb{C} \to \mathbb{C}$ given by
$E_1(u) = \int_0^1 e^{tu}\,dt$ is complex differentiable at every point of $\mathbb{C}$.

Formalized by `PerronKernel.E1_differentiable`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#e1-differentiable).

## Perron remainder

For a real number $y$ and a complex number $s$, the Perron remainder is
$R_y(s) = \log y \cdot E_1(s \log y)$, where $E_1(u) = \int_0^1 e^{tu}\,dt$ is the averaging
operator and $\log$ is the real logarithm (extended by $\log 0 = 0$ and $\log y = \log |y|$ for
$y < 0$).

The function $R_y$ is entire, and for $y > 0$ it agrees with $(y^s - 1)/s$ for $s \neq 0$.

Formalized by `PerronKernel.perronRemainder`, a definition declared in [MathlibExt/Analysis/PerronKernel.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-remainder).

## The Perron remainder is entire

For a real number $y$, the Perron remainder is the
function $R_y(s) = \log y \int_0^1 e^{ts\log y}\,dt$ of $s \in \mathbb{C}$, where
$\log y = \log|y|$ for $y \ne 0$ and $\log 0 = 0$. For every real $y$, the function $R_y$ is
complex differentiable at every point of $\mathbb{C}$.

Formalized by `PerronKernel.perronRemainder_differentiable`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-remainder-differentiable).

## The Perron remainder as a difference quotient

For every real $y > 0$ and every complex
$s \neq 0$, the Perron remainder $R_y$ satisfies $R_y(s) = (y^s - 1)/s$, where
$y^s = e^{s \log y}$.

Formalized by `PerronKernel.perronRemainder_eq_div`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-remainder-eq-div).

## Slope of the Perron remainder at the origin

For every real $y$ and every complex
$h \neq 0$, the Perron remainder $R_y$ satisfies

$$\frac{R_y(h) - R_y(0)}{h} = (\log y)^2 \int_0^1 t \, E_1(t h \log y)\,dt,$$

where $E_1(u) = \int_0^1 e^{\tau u}\,d\tau$ is the averaging operator and $\log$ is the real
logarithm (extended by $\log 0 = 0$ and $\log y = \log |y|$ for $y < 0$).

Formalized by `PerronKernel.perronRemainder_slope`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-remainder-slope).

## Modulus of a complex power of a positive real

For every real $y > 0$ and every complex
number $s$, $|y^s| = \exp(\operatorname{Re}(s) \log y)$, where $y^s$ is the principal complex
power.

Formalized by `PerronKernel.norm_cpow_ofReal`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#norm-cpow-of-real).

## Splitting off the pole of the Perron kernel quotient

Let $y > 0$ be real and let
$s \ne 0$ be complex. Then $y^s/s = R_y(s) + 1/s$, where $R_y(s) = \log y \cdot E_1(s \log y)$
is the Perron remainder and $E_1(u) = \int_0^1 e^{tu}\,dt$.

Formalized by `PerronKernel.cpow_div_eq_remainder_add`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#cpow-div-eq-remainder-add).

## Integral of $\exp(Lx)$

For real numbers $L \ne 0$, $a$ and $b$,

$$\int_a^b \exp(Lx)\,dx = \frac{\exp(Lb) - \exp(La)}{L},$$

where the integral is oriented: $\int_a^b = -\int_b^a$ when $a > b$.

Formalized by `PerronKernel.integral_exp_mul`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#integral-exp-mul).

## Horizontal side bound for the Perron integrand when $y > 1$

Let $y > 1$, let $U > 0$,
$c > 0$ and $T > 0$ be real numbers, and let $\tau = T$ or $\tau = -T$. Then

$$\left|\int_{-U}^{c} \frac{y^{x+i\tau}}{x+i\tau}\,dx\right| \le \frac{\exp(c\log y)}{T\log y},$$

where $y^s = \exp(s \log y)$ is the principal complex power. The bound does not depend on $U$.

Formalized by `PerronKernel.horiz_side_bound_gt_one`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#horiz-side-bound-gt-one).

## Bound for the integral of $y^s/s$ along a vertical segment

Let $y, d, T$ be real numbers
with $y > 0$, $d \neq 0$ and $T > 0$, and write $y^s = e^{s \log y}$. Then

$$\left| \int_{-T}^{T} \frac{y^{d + it}}{d + it}\,dt \right| \le
2T \cdot \frac{e^{d \log y}}{|d|},$$

that is, at most $2T y^d/|d|$.

Formalized by `PerronKernel.vert_side_bound`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#vert-side-bound).

## Bound for the integral of $y^s/s$ along the left vertical side

Let $y, U, T$ be real
numbers with $y > 0$, $U > 0$ and $T > 0$, and write $y^s = e^{s \log y}$. Then

$$\left| \int_{-T}^{T} \frac{y^{-U + it}}{-U + it}\,dt \right| \le
2T \cdot \frac{e^{-U \log y}}{U},$$

that is, at most $2T y^{-U}/U$. This is the vertical segment bound at real part $-U$.

Formalized by `PerronKernel.vert_side_bound_left`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#vert-side-bound-left).

## Bound for the integral of $y^s/s$ along the right vertical side

Let $y, U, T$ be real
numbers with $y > 0$, $U > 0$ and $T > 0$, and write $y^s = e^{s \log y}$. Then

$$\left| \int_{-T}^{T} \frac{y^{U + it}}{U + it}\,dt \right| \le
2T \cdot \frac{e^{U \log y}}{U},$$

that is, at most $2T y^{U}/U$. This is the vertical segment bound at real part $U$.

Formalized by `PerronKernel.vert_side_bound_right`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#vert-side-bound-right).

## Rectangle integral of $y^s/s$ around the origin

Let $y, U, c, T$ be real numbers with
$y > 0$, $U > 0$, $c > 0$ and $T > 0$, and write $y^s = e^{s \log y}$. Then

$$\int_{-U}^{c} \frac{y^{x - iT}}{x - iT}\,dx - \int_{-U}^{c} \frac{y^{x + iT}}{x + iT}\,dx +
i \left( \int_{-T}^{T} \frac{y^{c + it}}{c + it}\,dt -
\int_{-T}^{T} \frac{y^{-U + it}}{-U + it}\,dt \right) = 2\pi i,$$

that is, the integral of $y^s/s$ over the positively oriented boundary of the rectangle with
corners $-U - iT$ and $c + iT$ equals $2\pi i$.

The identity holds for every $y > 0$; it is used to close the Perron contour to the left when
$y > 1$.

Formalized by `PerronKernel.rect_identity_gt_one`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#rect-identity-gt-one).

## Horizontal side bound for the Perron integrand on $(c, U)$

Let $y > 0$ with
$\log y \ne 0$, let $c \le U$ and $T > 0$ be real numbers, and let $\tau = T$ or $\tau = -T$.
Then

$$\left|\int_c^U \frac{y^{x+i\tau}}{x+i\tau}\,dx\right|
\le \frac{\exp(U\log y)-\exp(c\log y)}{T\log y},$$

where $y^s = \exp(s \log y)$ is the principal complex power.

No sign condition on $\log y$ is assumed.

Formalized by `PerronKernel.horiz_side_bound_exact`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#horiz-side-bound-exact).

## Rectangle integral of $y^s/s$ with the pole outside

Let $y, U, c, T$ be real numbers with
$y > 0$, $0 < c < U$ and $T > 0$, and write $y^s = e^{s \log y}$. Then

$$\int_{c}^{U} \frac{y^{x - iT}}{x - iT}\,dx - \int_{c}^{U} \frac{y^{x + iT}}{x + iT}\,dx +
i \left( \int_{-T}^{T} \frac{y^{U + it}}{U + it}\,dt -
\int_{-T}^{T} \frac{y^{c + it}}{c + it}\,dt \right) = 0,$$

that is, the integral of $y^s/s$ over the positively oriented boundary of the rectangle with
corners $c - iT$ and $U + iT$ vanishes.

The identity holds for every $y > 0$; it is used to close the Perron contour to the right when
$y < 1$.

Formalized by `PerronKernel.rect_identity_lt_one`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#rect-identity-lt-one).

## Truncated Perron bound for $y > 1$

Let $y > 1$, $c > 0$ and $T > 0$ be real numbers, and
let $K(y, c, T) = \frac{1}{2\pi}\int_{-T}^{T} \frac{y^{c+it}}{c+it}\,dt$ be the truncated Perron
kernel. Then

$$|K(y, c, T) - 1| \le \frac{\exp(c \log y)}{\pi T \log y}.$$

Here $y^s$ is the principal complex power.

Formalized by `PerronKernel.perron_bound_gt_one`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-bound-gt-one).

## Truncated Perron bound for $0 < y < 1$

Let $0 < y < 1$, $c > 0$ and $T > 0$ be real
numbers, and let $K(y, c, T) = \frac{1}{2\pi}\int_{-T}^{T} \frac{y^{c+it}}{c+it}\,dt$ be the
truncated Perron kernel. Then

$$|K(y, c, T)| \le \frac{\exp(c \log y)}{\pi T |\log y|}.$$

Here $y^s$ is the principal complex power.

Formalized by `PerronKernel.perron_bound_lt_one`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 930](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L930). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-bound-lt-one).

## Truncated Perron formula

Let $y > 0$ with $y \ne 1$, and let $c > 0$ and $T > 0$ be real
numbers. Let $K(y, c, T) = \frac{1}{2\pi}\int_{-T}^{T} \frac{y^{c+it}}{c+it}\,dt$ be the truncated
Perron kernel, and let $\delta(y) = 1$ if $y > 1$ and $\delta(y) = 0$ if $y < 1$. Then

$$|K(y, c, T) - \delta(y)| \le \frac{\exp(c \log y)}{\pi T |\log y|}.$$

Here $y^s$ is the principal complex power.

Formalized by `PerronKernel.perron_bound`, a theorem declared in [MathlibExt/Analysis/PerronKernel.lean, line 1085](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/PerronKernel.lean#L1085). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html#perron-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perron's formula](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/perron-s-formula)
