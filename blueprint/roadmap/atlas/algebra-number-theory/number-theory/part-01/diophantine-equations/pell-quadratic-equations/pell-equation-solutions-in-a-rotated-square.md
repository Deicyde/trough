---
declaration: section
origin: cited
lean: MetaMathlibExt.pellU, MetaMathlibExt.pellV, MetaMathlibExt.pellU_zero, MetaMathlibExt.pellV_zero, MetaMathlibExt.pell_solutions_eq_signed_powers, MetaMathlibExt.pellU_pellV_natCast, MetaMathlibExt.pell_inverse_closed_form, MetaMathlibExt.pell_inverse_floor
statement: formalized
---

# Pell equation solutions in a rotated square

19 results, 8 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html).

## The Pell interpolation function u

For integers $D$, $\alpha$, $\beta$, the function
$u : \mathbb{R} \to \mathbb{R}$ is
$u(x) = ((\alpha + \beta\sqrt D)^x + (\alpha - \beta\sqrt D)^x)/2$, where $\sqrt D$ is the real
square root (zero when $D < 0$) and $(\cdot)^x$ is the real power.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Section 1, Equation (1.3).

Formalized by `MetaMathlibExt.pellU`, a definition declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-u).

## The Pell interpolation function v

For integers $D$, $\alpha$, $\beta$, the function
$v : \mathbb{R} \to \mathbb{R}$ is
$v(x) = ((\alpha + \beta\sqrt D)^x - (\alpha - \beta\sqrt D)^x)/(2\sqrt D)$, where $\sqrt D$ is the
real square root (zero when $D < 0$), $(\cdot)^x$ is the real power and division by zero gives
$0$; in particular $v$ is identically $0$ when $D \le 0$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Section 1, Equation (1.4).

Formalized by `MetaMathlibExt.pellV`, a definition declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-v).

## Value of the Pell interpolation function u at 0

For all integers $D$, $\alpha$, $\beta$,
the function $u(x) = ((\alpha + \beta\sqrt D)^x + (\alpha - \beta\sqrt D)^x)/2$ of a real
variable $x$ satisfies $u(0) = 1$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Section 1, Equation (1.3).

Formalized by `MetaMathlibExt.pellU_zero`, a theorem declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-u-zero).

## Value of the Pell interpolation function v at 0

For all integers $D$, $\alpha$, $\beta$,
the function $v(x) = ((\alpha + \beta\sqrt D)^x - (\alpha - \beta\sqrt D)^x)/(2\sqrt D)$ of a real
variable $x$, where $\sqrt D$ is the real square root (zero when $D < 0$) and division by zero
gives $0$, satisfies $v(0) = 0$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Section 1, Equation (1.4).

Formalized by `MetaMathlibExt.pellV_zero`, a theorem declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-v-zero).

## Pell solutions are signed powers of the fundamental solution

Let $D$ be an integer and
let $(\alpha, \beta)$ be a fundamental solution of $x^2 - Dy^2 = 1$, that is, an integer solution
with $\alpha > 1$ and $\beta > 0$ such that $\alpha \le x$ for every integer solution $(x, y)$ with
$x > 1$ (one exists only when $D$ is positive and not a square). For $n \ge 0$ let $u_n, v_n$ be
the integers with $u_n + v_n\sqrt D = (\alpha + \beta\sqrt D)^n$. Then integers $x, y$ satisfy
$x^2 - Dy^2 = 1$ if and only if $x = i\,u_n$ and $y = j\,v_n$ for some integer $n \ge 0$ and some
signs $i, j \in \{1, -1\}$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Proposition 1.1.

Stated but not proved: `MetaMathlibExt.pell_solutions_eq_signed_powers` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-solutions-eq-signed-powers).

## The Pell interpolation functions agree with the solution sequence at natural numbers

Let
$D$ be an integer and let $(\alpha, \beta)$ be a fundamental solution of $x^2 - Dy^2 = 1$, that
is, an integer solution with $\alpha > 1$ and $\beta > 0$ such that $\alpha \le x$ for every
integer solution $(x, y)$ with $x > 1$ (one exists only when $D$ is positive and not a square).
For $n \ge 0$ let $u_n, v_n$ be the integers with $u_n + v_n\sqrt D = (\alpha + \beta\sqrt D)^n$,
and for real $t$ let $u(t) = ((\alpha + \beta\sqrt D)^t + (\alpha - \beta\sqrt D)^t)/2$ and
$v(t) = ((\alpha + \beta\sqrt D)^t - (\alpha - \beta\sqrt D)^t)/(2\sqrt D)$. Then $u(n) = u_n$ and
$v(n) = v_n$ for every natural number $n$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Proposition 1.2.

Stated but not proved: `MetaMathlibExt.pellU_pellV_natCast` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-u-pell-v-nat-cast).

## Closed form for inverting the sum of the Pell interpolating functions

Let $D$ be an
integer, let $(\alpha, \beta)$ be the fundamental solution of the Pell equation $X^2 - D Y^2 = 1$,
put $\varepsilon = \alpha + \beta \sqrt{D}$ and $\bar\varepsilon = \alpha - \beta \sqrt{D}$, and let
$u(t) = (\varepsilon^t + \bar\varepsilon^t) / 2$ and
$v(t) = (\varepsilon^t - \bar\varepsilon^t) / (2 \sqrt{D})$ for real $t$. For every real $x \ge 1$,
put $z = (D x - \sqrt{D x^2 - D + 1}) / (D - 1)$ and
$g = \log(z + \sqrt{z^2 - 1}) / \log \varepsilon$. Then $g \ge 0$ and $u(g) + v(g) = x$.

Here $\log(z + \sqrt{z^2 - 1})$ is $\cosh^{-1}(z)$ written in logarithmic form.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Theorem 2.2, Equation (2.1).

Stated but not proved: `MetaMathlibExt.pell_inverse_closed_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-inverse-closed-form).

## Floor of the inverse of the sum of the Pell interpolating functions

Let $D$ be an
integer, let $(\alpha, \beta)$ be the fundamental solution of the Pell equation $X^2 - D Y^2 = 1$,
put $\varepsilon = \alpha + \beta \sqrt{D}$ and $\bar\varepsilon = \alpha - \beta \sqrt{D}$, and let
$u(s) = (\varepsilon^s + \bar\varepsilon^s) / 2$ and
$v(s) = (\varepsilon^s - \bar\varepsilon^s) / (2 \sqrt{D})$ for real $s$. If $x \ge 1$ and $t \ge 0$
are real numbers with $u(t) + v(t) = x$, then
$\lfloor t \rfloor = \lfloor (\log \lfloor x \rfloor + C) / \log \varepsilon \rfloor$, where
$C = \log(2 \sqrt{D} / (1 + \sqrt{D}))$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Theorem 2.3, Equation (2.5).

Stated but not proved: `MetaMathlibExt.pell_inverse_floor` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-inverse-floor).

## Pell solutions in a closed rotated square

Let $D$ be an integer and let $(\alpha, \beta)$
be a fundamental solution of $x^2 - Dy^2 = 1$, that is, an integer solution with $\alpha > 1$
and $\beta > 0$ such that $\alpha \le x$ for every integer solution $(x, y)$ with $x > 1$ (one
exists only when $D$ is positive and not a square). For $n \ge 0$ let $u_n, v_n$ be the
integers with $u_n + v_n\sqrt D = (\alpha + \beta\sqrt D)^n$, and for real $t$ let
$u(t) = ((\alpha + \beta\sqrt D)^t + (\alpha - \beta\sqrt D)^t)/2$ and
$v(t) = ((\alpha + \beta\sqrt D)^t - (\alpha - \beta\sqrt D)^t)/(2\sqrt D)$. For real $\lambda$
let $Q(\lambda)$ be the set of integer pairs $(x, y)$ with $x^2 - Dy^2 = 1$ and
$|x| + |y| \le \lambda$. If $\lambda < 1$, then $Q(\lambda)$ is empty. If $\lambda \ge 1$, then
for every real $t \ge 0$ with $u(t) + v(t) = \lambda$, the set $Q(\lambda)$ consists of the pairs
$(i\,u_n, j\,v_n)$ with $i, j \in \{1, -1\}$ and integers $0 \le n \le t$, and it has exactly
$2 + 4\lfloor t \rfloor$ elements.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.pell_solutions_in_rotated_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-solutions-in-rotated-square).

## Explicit count of Pell solutions in a closed rotated square

Let $D$ be an integer and let
$(\alpha, \beta)$ be a fundamental solution of $x^2 - Dy^2 = 1$, that is, an integer solution
with $\alpha > 1$ and $\beta > 0$ such that $\alpha \le x$ for every integer solution $(x, y)$ with
$x > 1$ (one exists only when $D$ is positive and not a square). For $n \ge 0$ let $u_n, v_n$ be
the integers with $u_n + v_n\sqrt D = (\alpha + \beta\sqrt D)^n$. For real $\lambda$ let
$Q(\lambda)$ be the set of integer pairs $(x, y)$ with $x^2 - Dy^2 = 1$ and
$|x| + |y| \le \lambda$. If $\lambda < 1$, then $Q(\lambda)$ is empty. If $\lambda \ge 1$, let
$m = \left\lfloor \left(\log\lfloor\lambda\rfloor + \log\frac{2\sqrt D}{1 + \sqrt D}\right) /
\log(\alpha + \beta\sqrt D) \right\rfloor$; then $Q(\lambda)$ consists of the pairs
$(i\,u_n, j\,v_n)$ with $i, j \in \{1, -1\}$ and integers $0 \le n \le m$, and $Q(\lambda)$ has
exactly $2 + 4m$ elements.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Corollary 2.4.

Stated but not proved: `MetaMathlibExt.pell_solutions_in_rotated_square_explicit` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-solutions-in-rotated-square-explici).

## Shifted real Pell solutions eventually lie in the closed quadrants

Let $D$ be an integer
and let $(\alpha, \beta)$ be a fundamental solution of $X^2 - DY^2 = 1$, that is, an integer
solution with $\alpha > 1$ and $\beta > 0$ such that $\alpha \le X$ for every integer solution
$(X, Y)$ with $X > 1$ (one exists only when $D$ is positive and not a square). For real $x$ let
$u(x) = ((\alpha + \beta\sqrt D)^x + (\alpha - \beta\sqrt D)^x)/2$ and
$v(x) = ((\alpha + \beta\sqrt D)^x - (\alpha - \beta\sqrt D)^x)/(2\sqrt D)$, and for integers $a$,
$b$ and signs $i, j \in \{1, -1\}$ let $R_{i,j}(x) = (i\,u(x) + a, j\,v(x) + b)$. Then there is a
real $x_0$ such that for every real $x \ge x_0$ the point $R_{1,1}(x)$ lies in the closed first
quadrant $\{X \ge 0, Y \ge 0\}$, $R_{-1,1}(x)$ in the closed second quadrant
$\{X \le 0, Y \ge 0\}$, $R_{-1,-1}(x)$ in the closed third quadrant $\{X \le 0, Y \le 0\}$ and
$R_{1,-1}(x)$ in the closed fourth quadrant $\{X \ge 0, Y \le 0\}$.

The points $R_{i,j}(x)$ are real solutions of the shifted Pell equation
$(X - a)^2 - D(Y - b)^2 = 1$. The printed statement of the source swaps the third and fourth
quadrants; this statement follows the reading of the source's proof.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Proposition 3.1.

Stated but not proved: `MetaMathlibExt.pell_shifted_real_solutions_eventually_in_quadrants` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shifted-real-solutions-eventually-i).

## Largest intercept norm of a shifted Pell curve

Let $D > 0$, $a \ne 0$ and $b$ be
integers. The intercepts of the shifted Pell curve $(x - a)^2 - D (y - b)^2 = 1$ with the axes
are $(a \pm \sqrt{1 + D b^2}, 0)$ and $(0, b \pm \sqrt{(a^2 - 1) / D})$, with $L^1$ norms
$|a \pm \sqrt{1 + D b^2}|$ and $|b \pm \sqrt{(a^2 - 1) / D}|$. The largest of these four norms
is $|a| + \sqrt{1 + D b^2}$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Proposition 3.2.

Stated but not proved: `MetaMathlibExt.pell_shifted_intercepts_max` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shifted-intercepts-max).

## The $L^1$ norm along a shifted Pell curve

For integers $D$, $\alpha$, $\beta$, $a$, $b$,
$i$ and $j$, put $\varepsilon = \alpha + \beta \sqrt{D}$ and
$\bar\varepsilon = \alpha - \beta \sqrt{D}$, and let
$u(x) = (\varepsilon^x + \bar\varepsilon^x) / 2$ and
$v(x) = (\varepsilon^x - \bar\varepsilon^x) / (2 \sqrt{D})$ for real $x$. The function $f_{i,j}$
is defined on the reals by $f_{i,j}(x) = |i u(x) + a| + |j v(x) + b|$.

No condition is placed on the integers: $\sqrt{s} = 0$ for $s < 0$, a quotient by $0$ is $0$, and
for real $c < 0$ the power $c^x$ means $|c|^x \cos(\pi x)$, while $0^0 = 1$ and $0^x = 0$ for
$x \ne 0$.

In the source, $(\alpha, \beta)$ is the fundamental solution of $X^2 - D Y^2 = 1$,
$i, j \in \{1, -1\}$, and $f_{i,j}(x)$ is the $L^1$ norm of the real solution
$R_{i,j}(x) = (i u(x) + a, j v(x) + b)$ of the shifted Pell equation
$(X - a)^2 - D (Y - b)^2 = 1$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Section 3, definition of `f_{i,j}`.

Formalized by `MetaMathlibExt.pellShiftedNorm`, a definition declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shifted-norm).

## Value at zero of the shifted Pell norm function

Let $D$, $\alpha$, $\beta$, $a$, $b$,
$i$ and $j$ be integers. Put $\varepsilon = \alpha + \beta \sqrt{D}$ and
$\bar\varepsilon = \alpha - \beta \sqrt{D}$, let
$u(x) = (\varepsilon^x + \bar\varepsilon^x) / 2$ and
$v(x) = (\varepsilon^x - \bar\varepsilon^x) / (2 \sqrt{D})$ for real $x$, and let
$f_{i,j}(x) = |i u(x) + a| + |j v(x) + b|$. Then $f_{i,j}(0) = |i + a| + |b|$.

Here $\sqrt{s} = 0$ for $s < 0$, a quotient by $0$ is $0$, and $c^0 = 1$ for every real $c$; no
condition is placed on the integers.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Section 3, definition of `f_{i,j}`.

Formalized by `MetaMathlibExt.pellShiftedNorm_zero`, a theorem declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shifted-norm-zero).

## The bound $K$ for the shifted Pell equation

For integers $D$, $a$ and $b$, the constant
attached to the shifted Pell equation $(x - a)^2 - D (y - b)^2 = 1$ is the real number
$K = |a| + \max(|b| + 1, \sqrt{1 + D b^2})$, where $\sqrt{s}$ is taken to be $0$ for $s < 0$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Theorem 3.3, definition of `K`.

Formalized by `MetaMathlibExt.pellShiftBound`, a definition declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shift-bound).

## The bound $K$ of the unshifted Pell equation

For every integer $D$, the constant
$K = |a| + \max(|b| + 1, \sqrt{1 + D b^2})$ with $a = b = 0$ equals $1$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Theorem 3.3, definition of `K`.

Formalized by `MetaMathlibExt.pellShiftBound_zero_zero`, a theorem declared in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shift-bound-zero-zero).

## The shifted Pell norm function at zero is at most the bound

Let $D$, $\alpha$, $\beta$,
$a$ and $b$ be integers and let $i, j \in \{1, -1\}$. Put $\varepsilon = \alpha + \beta \sqrt{D}$
and $\bar\varepsilon = \alpha - \beta \sqrt{D}$, let
$u(x) = (\varepsilon^x + \bar\varepsilon^x) / 2$ and
$v(x) = (\varepsilon^x - \bar\varepsilon^x) / (2 \sqrt{D})$ for real $x$, let
$f_{i,j}(x) = |i u(x) + a| + |j v(x) + b|$ and let $K = |a| + \max(|b| + 1, \sqrt{1 + D b^2})$.
Then $f_{i,j}(0) \le K$.

Here $\sqrt{s} = 0$ for $s < 0$, a quotient by $0$ is $0$, and $c^0 = 1$ for every real $c$; no
further condition is placed on the integers.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Lemma 3.5.

Stated but not proved: `MetaMathlibExt.pellShiftedNorm_zero_le_pellShiftBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shifted-norm-zero-le-pell-shift-bou).

## The shifted Pell norm function is at most the bound up to its last crossing

Let $D$ be
an integer, let $(\alpha, \beta)$ be the fundamental solution of the Pell equation
$X^2 - D Y^2 = 1$, put $\varepsilon = \alpha + \beta \sqrt{D}$ and
$\bar\varepsilon = \alpha - \beta \sqrt{D}$, and let
$u(x) = (\varepsilon^x + \bar\varepsilon^x) / 2$ and
$v(x) = (\varepsilon^x - \bar\varepsilon^x) / (2 \sqrt{D})$ for real $x$. Let $a$ and $b$ be
integers, let $i, j \in \{1, -1\}$, let $f_{i,j}(x) = |i u(x) + a| + |j v(x) + b|$, let
$K = |a| + \max(|b| + 1, \sqrt{1 + D b^2})$ and let $x_1 = \sup \{y \ge 0 : f_{i,j}(y) = K\}$.
Then $f_{i,j}(x) \le K$ for every real $x$ with $0 \le x \le x_1$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Lemma 3.6.

Stated but not proved: `MetaMathlibExt.pellShiftedNorm_le_pellShiftBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shifted-norm-le-pell-shift-bound).

## The shifted Pell norm function is increasing past its last crossing of the bound

Let $D$
be an integer, let $(\alpha, \beta)$ be the fundamental solution of the Pell equation
$X^2 - D Y^2 = 1$, put $\varepsilon = \alpha + \beta \sqrt{D}$ and
$\bar\varepsilon = \alpha - \beta \sqrt{D}$, and let
$u(x) = (\varepsilon^x + \bar\varepsilon^x) / 2$ and
$v(x) = (\varepsilon^x - \bar\varepsilon^x) / (2 \sqrt{D})$ for real $x$. Let $a$ and $b$ be
integers, let $i, j \in \{1, -1\}$, let $f_{i,j}(x) = |i u(x) + a| + |j v(x) + b|$, let
$K = |a| + \max(|b| + 1, \sqrt{1 + D b^2})$ and let $x_1 = \sup \{y \ge 0 : f_{i,j}(y) = K\}$.
Then $f_{i,j}(x) = u(x) + v(x) + i a + j b$ for every real $x \ge x_1$, the function $f_{i,j}$ is
strictly increasing on $[x_1, \infty)$, and $f_{i,j}$ maps $[x_1, \infty)$ bijectively onto
$[K, \infty)$.

## Sources

- Kun Yi Ong and Eddie Shahril Bin Ismail, *Integer Solutions of Pell Equation in a Closed Rotated Square Region*, INTEGERS 25 (2025), Article A112, Lemma 3.7.

Stated but not proved: `MetaMathlibExt.pellShiftedNorm_bijOn_Ici` is written with `theorem_wanted` in [WantedExt/NumberTheory/PellRotatedSquareWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PellRotatedSquareWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html#pell-shifted-norm-bij-on-ici).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pell equation solutions in a rotated square](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pell-equation-solutions-in-a-rotated-square)
