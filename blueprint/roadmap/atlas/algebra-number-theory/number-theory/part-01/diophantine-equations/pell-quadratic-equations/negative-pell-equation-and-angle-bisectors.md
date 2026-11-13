---
declaration: section
origin: cited
lean: MetaMathlibExt.negPellFundY, MetaMathlibExt.negPellFundX, MetaMathlibExt.negPellFund_spec, MetaMathlibExt.negPellFundY_le, MetaMathlibExt.negPellFund_two, MetaMathlibExt.negPellF, MetaMathlibExt.negPellG, MetaMathlibExt.negPellF_zero_negPellG_zero
statement: formalized
---

# Negative Pell equation and angle bisectors

48 results, 18 proved and 30 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html).

## Second coordinate of the fundamental negative Pell solution

For a natural number $d$,
$Y$ is the least positive integer $y$ such that $x^2 - d y^2 = -1$ for some integer $x$, and
$Y = 0$ when there is no such $y$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23)-(24).

Formalized by `MetaMathlibExt.negPellFundY`, a definition declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-fund-y).

## First coordinate of the fundamental negative Pell solution

For a natural number $d$, let
$Y$ be the least positive integer $y$ such that $x^2 - d y^2 = -1$ for some integer $x$, or $0$
if there is no such $y$. Then $X = \lfloor \sqrt{d Y^2 - 1} \rfloor$, where $d Y^2 - 1$ is read
as $0$ when $d Y^2 = 0$. So $X$ is the nonnegative integer with $X^2 - d Y^2 = -1$ when a solution
exists, and $X = 0$ otherwise.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23)-(24).

Formalized by `MetaMathlibExt.negPellFundX`, a definition declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-fund-x).

## The fundamental negative Pell solution solves the equation

Let $d$ be a natural number
such that $x^2 - d y^2 = -1$ has a solution in a natural number $x$ and a positive integer $y$.
Then the fundamental solution $(X, Y)$, the one with the least positive $y$, satisfies $Y > 0$
and $X^2 + 1 = d Y^2$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (24).

Formalized by `MetaMathlibExt.negPellFund_spec`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-fund-spec).

## Minimality of the fundamental negative Pell solution

Let $d$ be a natural number and let
$Y$ be the second coordinate of its fundamental negative Pell solution. If $y$ is a positive
integer such that $x^2 - d y^2 = -1$ for some natural number $x$, then $Y \le y$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (24).

Formalized by `MetaMathlibExt.negPellFundY_le`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-fund-y-le).

## The fundamental solution of the negative Pell equation for d = 2

The least positive
integer $y$ such that $x^2 - 2 y^2 = -1$ for some integer $x$ is $Y = 1$, and the corresponding
first coordinate is $X = 1$; that is, the fundamental solution for $d = 2$ is $(1, 1)$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23)-(24).

Formalized by `MetaMathlibExt.negPellFund_two`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-fund-two).

## First coordinates of the powers of the fundamental negative Pell solution

For a natural
number $d$, let $Y$ be the least positive integer $y$ such that $x^2 - d y^2 = -1$ for some
integer $x$, let $X$ be the nonnegative integer with $X^2 - d Y^2 = -1$, and set $X = Y = 0$
when there is no such $y$. In the ring $\mathbb{Z}[\sqrt{d}]$ of formal expressions
$a + b \sqrt{d}$ with $a, b \in \mathbb{Z}$ and $(\sqrt{d})^2 = d$, put
$\varepsilon = X + Y \sqrt{d}$. For $n \ge 0$, $f_n$ is the integer such that
$\varepsilon^n = f_n + g_n \sqrt{d}$ for some integer $g_n$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23).

Formalized by `MetaMathlibExt.negPellF`, a definition declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-f).

## Second coordinates of the powers of the fundamental negative Pell solution

For a natural
number $d$, let $Y$ be the least positive integer $y$ such that $x^2 - d y^2 = -1$ for some
integer $x$, let $X$ be the nonnegative integer with $X^2 - d Y^2 = -1$, and set $X = Y = 0$
when there is no such $y$. In the ring $\mathbb{Z}[\sqrt{d}]$ of formal expressions
$a + b \sqrt{d}$ with $a, b \in \mathbb{Z}$ and $(\sqrt{d})^2 = d$, put
$\varepsilon = X + Y \sqrt{d}$. For $n \ge 0$, $g_n$ is the integer such that
$\varepsilon^n = f_n + g_n \sqrt{d}$ for some integer $f_n$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23).

Formalized by `MetaMathlibExt.negPellG`, a definition declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-g).

## Initial values of the negative Pell sequences

For every natural number $d$, the
sequences $f_n$ and $g_n$ of the negative Pell equation $x^2 - d y^2 = -1$ satisfy $f_0 = 1$ and
$g_0 = 0$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23).

Formalized by `MetaMathlibExt.negPellF_zero_negPellG_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-f-zero-neg-pell-g-zero).

## Recurrence for the negative Pell sequences

Let $d$ be a natural number, let $(X, Y)$ be the
solution of $x^2 - d y^2 = -1$ in natural numbers with least positive $Y$ (with $X = Y = 0$ if
there is none), and define integers $f_n, g_n$ by $(X + Y\sqrt{d})^n = f_n + g_n\sqrt{d}$,
computed formally with $(\sqrt{d})^2 = d$. Then for every $n \ge 0$,

$$f_{n+1} = f_n X + d g_n Y, \qquad g_{n+1} = f_n Y + g_n X.$$

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23).

Formalized by `MetaMathlibExt.negPell_succ`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-succ).

## The negative Pell sequences for d = 2 at n = 1

Let $(X, Y)$ be the solution of
$x^2 - 2y^2 = -1$ in natural numbers with the least positive $Y$, and for each $n$ let $f_n$ and
$g_n$ be the integers with $(X + Y\sqrt 2)^n = f_n + g_n \sqrt 2$. Then $f_1 = g_1 = 1$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5, (23).

Formalized by `MetaMathlibExt.negPellF_two_one`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-f-two-one).

## Angle bisectors satisfy the bisector equation

Let $a, b, c$ be real numbers with
$|a| \ne |b|$ and $c \ne 0$, and suppose that the lines $y = cx$ and $y = -c^{-1} x$ both bisect
the angles between the lines $y = ax$ and $y = bx$, that is,

$$
\frac{|a - c|}{\sqrt{a^2 + 1}} = \frac{|b - c|}{\sqrt{b^2 + 1}} \quad\text{and}\quad
\frac{|a + c^{-1}|}{\sqrt{a^2 + 1}} = \frac{|b + c^{-1}|}{\sqrt{b^2 + 1}}.
$$

Then $(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1)$.

A line $y = sx$ bisects the angles between $y = ax$ and $y = bx$ exactly when the point $(1, s)$
is equidistant from both lines, that is, when $|a - s| / \sqrt{a^2 + 1} = |b - s| / \sqrt{b^2 + 1}$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 1(a).

Stated but not proved: `MetaMathlibExt.bisector_slope_equation` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-slope-equation).

## Rational solutions of the bisector equation

Let $a, b, c$ be rational numbers with
$|a| \ne |b|$ and $(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1)$. Then there are a square-free
natural number $d > 0$ and rational numbers $a_2, b_2$ with $a^2 - d a_2^2 = -1$ and
$b^2 - d b_2^2 = -1$ such that either $a_2 + b_2 \ne 0$ and
$c = (a b_2 + a_2 b) / (a_2 + b_2)$, or $b_2 - a_2 \ne 0$ and $c = (a b_2 - a_2 b) / (b_2 - a_2)$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 1(b).

Stated but not proved: `MetaMathlibExt.bisector_equation_rat_solution` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-rat-solution).

## Symmetries of the bisector equation

Let $a, b, c$ be real numbers with
$(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1)$. Then the triples $(-a, -b, -c)$ and $(b, a, c)$
satisfy the same equation, and so does $(a, b, -c^{-1})$ when $c \ne 0$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 2(a).

Stated but not proved: `MetaMathlibExt.bisector_equation_symm` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-symm).

## No nontrivial integer solutions of the bisector equation with $a = 0$ or $b = 0$

Let
$a, b, c$ be integers with $a = 0$ or $b = 0$ and
$(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1)$. Then $|a| = |b|$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 2(b).

Stated but not proved: `MetaMathlibExt.bisector_equation_int_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-int-zero).

## Integer solutions of the bisector equation

For a natural number $d > 1$ such that
$x^2 - d y^2 = -1$ has an integer solution, let $(X, Y)$ be its solution in positive integers
with $Y$ least, and define integers $f^{(d)}_k$ and $g^{(d)}_k$ by
$f^{(d)}_k + g^{(d)}_k \sqrt{d} = (X + Y \sqrt{d})^k$ for natural numbers $k$. Let $a, b, c$ be
integers with $|a| \ne |b|$ and

$$(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1).$$

Then there is $s \in \{1, -1\}$ such that one of the following holds: there are a square-free
natural number $d > 1$ for which $x^2 - d y^2 = -1$ has an integer solution and natural numbers
$m, n > 0$ such that $(a, b, c)$ or $(b, a, c)$ equals

$$s \left(f^{(d)}_{(2m-1)(2n-1)}, \ f^{(d)}_{(2m-1)(2n+1)}, \
g^{(d)}_{(2m-1) 2n} / g^{(d)}_{2m-1}\right);$$

or there is a natural number $n > 0$ such that $(a, b, c)$ or $(b, a, c)$ equals

$$s \left(f^{(2)}_{2n-1}, \ -f^{(2)}_{2n+1}, \ f^{(2)}_{2n}\right).$$

Here $g^{(d)}_{(2m-1) 2n} / g^{(d)}_{2m-1}$ is the integer quotient; the division is exact.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 3.

Stated but not proved: `MetaMathlibExt.bisector_equation_int_solution` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-int-solution).

## Bisector-equation solutions from the negative Pell sequences

Let $d > 1$ be a natural
number such that $x^2 - d y^2 = -1$ has an integer solution, let $(X, Y)$ be its solution in
positive integers with $Y$ least, and define integers $f_k$ and $g_k$ by
$f_k + g_k \sqrt{d} = (X + Y \sqrt{d})^k$ for natural numbers $k$. Let $m, n > 0$ be natural
numbers and put $a = f_{(2m-1)(2n-1)}$, $b = f_{(2m-1)(2n+1)}$ and
$c = g_{(2m-1) 2n} / g_{2m-1}$. Then $g_{2m-1}$ divides $g_{(2m-1) 2n}$, so $c$ is an integer, and

$$(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1).$$

## Sources

- converse of Theorem 3 for Form (9); the square-freeness of $d$ is not needed here.
- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 3, converse for (9).

Stated but not proved: `MetaMathlibExt.bisector_equation_form_nine` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-form-nine).

## Bisector-equation solutions from the powers of $1 + \sqrt{2}$

The least solution of
$x^2 - 2 y^2 = -1$ in positive integers is $(1, 1)$; define integers $f_k$ and $g_k$ by
$f_k + g_k \sqrt{2} = (1 + \sqrt{2})^k$ for natural numbers $k$. For every natural number $n > 0$,
the integers $a = f_{2n-1}$, $b = -f_{2n+1}$ and $c = f_{2n}$ satisfy

$$(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1).$$

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 3, converse for (10).

Stated but not proved: `MetaMathlibExt.bisector_equation_form_ten` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-form-ten).

## Finitely many classes of solutions of a general Pell equation

Let $d > 0$ be an integer
that is not a perfect square, let $\varepsilon$ be the fundamental solution of $x^2 - dy^2 = 1$,
viewed as a unit of $\mathbb{Z}[\sqrt d]$, and let $z \ne 0$ be an integer such that
$x^2 - dy^2 = z$ has an integral solution. Then there is a finite set $S$ of integral solutions
$(a, b)$ of $x^2 - dy^2 = z$ such that every integral solution $(x, y)$ satisfies
$x + y\sqrt d = \pm \varepsilon^n (a + b\sqrt d)$ in $\mathbb{Z}[\sqrt d]$ for some $(a, b) \in S$,
some sign and some $n \in \mathbb{Z}$.

The paper uses the fundamental unit of norm $\pm 1$; the powers of $\varepsilon$ are among its
powers, so this form implies the paper's.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 6 (quoting its reference [4, Corollary 3.5]).

Stated but not proved: `MetaMathlibExt.generalPell_finitely_many_classes` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#general-pell-finitely-many-classes).

## Rational solvability of the negative Pell equation

For a positive squarefree integer
$d$, the equation $x^2 - d y^2 = -1$ has a rational solution if and only if no prime divisor of
$d$ is congruent to $3$ modulo $4$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 5.

Stated but not proved: `MetaMathlibExt.negPell_rat_solvable_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-rat-solvable-iff).

## Basic properties of the negative Pell sequences

Let $d > 1$ be a natural number such that
$x^2 - d y^2 = -1$ has an integral solution, let $(X, Y)$ be its solution in natural numbers with
least positive $Y$, and define integers $f_n, g_n$ by $(X + Y\sqrt{d})^n = f_n + g_n\sqrt{d}$.
Then $f_n^2 - d g_n^2 = (-1)^n$ for every $n \ge 0$, the sequence $(g_n)_{n \ge 0}$ is strictly
increasing, the sequence $(f_n)_{n \ge 1}$ is strictly increasing, and, with the real numbers
$\varepsilon = X + Y\sqrt{d}$ and $\varepsilon' = X - Y\sqrt{d}$, for every $n \ge 0$

$$f_n = \frac{\varepsilon^n + \varepsilon'^n}{2},$$



$$g_n = \frac{\varepsilon^n - \varepsilon'^n}{2\sqrt{d}}.$$

The sequence $(f_n)_{n \ge 0}$ is not strictly increasing when $d = 2$, since $f_0 = f_1 = 1$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 5.

Stated but not proved: `MetaMathlibExt.negPell_sequences_basic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-sequences-basic).

## Addition and doubling formulas for the negative Pell sequences

Let $d$ be a natural
number such that $x^2 - dy^2 = -1$ has an integral solution, let $(X, Y)$ be the solution of
$x^2 - dy^2 = -1$ in natural numbers with the least positive $Y$, and let $f_n$ and $g_n$ be the
integers defined by $f_0 = 1$, $g_0 = 0$, $f_{n+1} = X f_n + dY g_n$ and
$g_{n+1} = Y f_n + X g_n$, so that $(X + Y\sqrt d)^n = f_n + g_n \sqrt d$. Then for all natural
numbers $n \le m$,

$$
\begin{aligned}
f_{m+n} &= f_m f_n + d g_m g_n, & g_{m+n} &= f_m g_n + g_m f_n, \\
f_{m-n} &= (-1)^n (f_m f_n - d g_m g_n), & g_{m-n} &= (-1)^{n+1} (f_m g_n - g_m f_n), \\
f_{2n} &= f_n^2 + d g_n^2, & g_{2n} &= 2 f_n g_n.
\end{aligned}
$$

The paper also assumes $d > 1$; this is not needed.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 6.

Stated but not proved: `MetaMathlibExt.negPell_addition_formulas` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-addition-formulas).

## Sum and difference formulas for the negative Pell sequences

Let $d$ be a natural number
such that $x^2 - d y^2 = -1$ has an integral solution, let $(X, Y)$ be its solution in natural
numbers with least positive $Y$, and define integers $f_n, g_n$ by
$(X + Y\sqrt{d})^n = f_n + g_n\sqrt{d}$, computed formally with $(\sqrt{d})^2 = d$. Let $m > n$
be natural numbers. If $n$ is even, then

$$f_{m+n} + f_{m-n} = 2 f_m f_n, \qquad f_{m+n} - f_{m-n} = 2 d g_m g_n,$$



$$g_{m+n} + g_{m-n} = 2 g_m f_n, \qquad g_{m+n} - g_{m-n} = 2 f_m g_n;$$

if $n$ is odd, then

$$f_{m+n} + f_{m-n} = 2 d g_m g_n, \qquad f_{m+n} - f_{m-n} = 2 f_m f_n,$$



$$g_{m+n} + g_{m-n} = 2 f_m g_n, \qquad g_{m+n} - g_{m-n} = 2 g_m f_n.$$

The source also assumes $d > 1$, which is not needed.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 7.

Stated but not proved: `MetaMathlibExt.negPell_sum_difference_formulas` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-sum-difference-formulas).

## Comparison of the negative Pell sequences

Let $d > 1$ be a natural number such that
$x^2 - d y^2 = -1$ has an integer solution, let $(X, Y)$ be its fundamental solution (the one with
$X, Y > 0$ and $Y$ least), and write $(X + Y \sqrt{d})^n = f_n + g_n \sqrt{d}$. Then for every
$n \ge 0$, $g_n \le f_n$, with equality if and only if $d = 2$ and $n = 1$.

Only the first sentence of the source's corollary is stated here: its second sentence, printed as
$f_1 \ge d - 1$ with a displaced square root sign, fails when read literally at $d = 5$, where
$f_1 = 2$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Corollary 2, first sentence.

Stated but not proved: `MetaMathlibExt.negPellG_le_negPellF` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-g-le-neg-pell-f).

## Coprimality of the negative Pell sequences

Let $d > 1$ be a natural number such that
$x^2 - d y^2 = -1$ has an integral solution, let $(X, Y)$ be its solution in natural numbers with
least positive $Y$, and define integers $f_n, g_n$ by $(X + Y\sqrt{d})^n = f_n + g_n\sqrt{d}$.
Then for every $n > 0$, $\gcd(d, f_n) = 1$ and $\gcd(f_n, g_n) = 1$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 11(a).

Stated but not proved: `MetaMathlibExt.negPell_gcd_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-gcd-eq-one).

## Coprimality of negative Pell terms whose indices have an even ratio

Let $d > 1$ be a
natural number such that $x^2 - dy^2 = -1$ has an integral solution, let $(X, Y)$ be the solution
of $x^2 - dy^2 = -1$ in natural numbers with the least positive $Y$, and for each $n$ let $f_n$
and $g_n$ be the integers with $(X + Y\sqrt d)^n = f_n + g_n \sqrt d$. If $0 < n \le m$ are
natural numbers such that $n$ divides $m$ and $m / n$ is even, then $\gcd(f_m, f_n) = 1$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 11(b).

Stated but not proved: `MetaMathlibExt.negPellF_gcd_of_even_quotient` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-f-gcd-of-even-quotient).

## Divisibility between terms of the negative Pell sequence

Let $d > 1$ be a natural
number such that $x^2 - dy^2 = -1$ has an integral solution, let $(X, Y)$ be the solution of
$x^2 - dy^2 = -1$ in natural numbers with the least positive $Y$, and for each $n$ let $f_n$ and
$g_n$ be the integers with $(X + Y\sqrt d)^n = f_n + g_n \sqrt d$. For natural numbers
$0 < n \le m$, $f_n$ divides $f_m$ if and only if either $d = 2$ and $n = 1$, or $n$ divides $m$
and $m / n$ is odd.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 11(c).

Stated but not proved: `MetaMathlibExt.negPellF_dvd_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-f-dvd-iff).

## Divisibility of the second coordinates of negative Pell powers

Let $d > 1$ be a natural
number such that $x^2 - d y^2 = -1$ has an integer solution, let $(X, Y)$ be its fundamental
solution (the one with $X, Y > 0$ and $Y$ least), and write
$(X + Y \sqrt{d})^n = f_n + g_n \sqrt{d}$. For natural numbers $0 < n \le m$, $g_n$ divides $g_m$
if and only if $n$ divides $m$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 11(d).

Stated but not proved: `MetaMathlibExt.negPellG_dvd_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#neg-pell-g-dvd-iff).

## $|x^2 - d y^2|$ is never $2 \bmod 4$ when $d \equiv 1 \pmod 4$

Let $d$ and $z$ be integers
with $d \equiv 1 \pmod 4$ and $z \equiv 2 \pmod 4$. Then $|x^2 - d y^2| \ne z$ for all integers $x$
and $y$.

## Sources

- the source's hypothesis $z > 1$ is not needed. The second sentence of part (a) (on $S(d)$ and $l_2$) is not stated here.
- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Lemma 1(a), first sentence.

Formalized by `MetaMathlibExt.abs_sq_sub_mul_sq_ne_of_two_mod_four`, a theorem declared in [MathlibExt/NumberTheory/GeneralPellBisectors.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralPellBisectors.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#abs-sq-sub-mul-sq-ne-of-two-mod-four).

## Solutions of |x² − dy²| = z are even when d ≡ 1 and z ≡ 4 (mod 8)

Let $d$ and $z$ be
integers with $d \equiv 1 \pmod 8$ and $z \equiv 4 \pmod 8$. If integers $x$ and $y$ satisfy
$|x^2 - dy^2| = z$, then $x$ and $y$ are both even.

The paper also assumes $z > 1$; this is not needed. The second sentence of part (c) of the
paper's lemma, on the fundamental unit, is not stated here.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Lemma 1(c), first sentence.

Stated but not proved: `MetaMathlibExt.even_of_abs_sq_sub_mul_sq_four_mod_eight` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#even-of-abs-sq-sub-mul-sq-four-mod-eight).

## Solutions of |x² − dy²| = z are even when d ≡ 5 and z ≡ 0 (mod 8)

Let $d$ and $z$ be
integers with $d \equiv 5 \pmod 8$ and $z \equiv 0 \pmod 8$. If integers $x$ and $y$ satisfy
$|x^2 - dy^2| = z$, then $x$ and $y$ are both even.

The paper also assumes $z > 1$; this is not needed.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Lemma 1(d).

Stated but not proved: `MetaMathlibExt.even_of_abs_sq_sub_mul_sq_zero_mod_eight` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#even-of-abs-sq-sub-mul-sq-zero-mod-eight).

## Primes with strictly primitive representations

For an integer $d$, $S(d)$ is the set of
primes $p$ for which there is an integer $l > 0$ such that $|x^2 - d y^2| = p^l$ has a strictly
primitive integral solution, that is, integers $x, y$ with $x$ and $d y$ coprime.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Notation 2.

Formalized by `MetaMathlibExt.strictPrimitivePrimes`, a definition declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-primes).

## Strictly primitive exponent

Let $d$ be an integer and $p$ a natural number, and let
$S(d)$ be the set of primes $q$ for which $|x^2 - d y^2| = q^l$ has a strictly primitive integral
solution (integers $x, y$ with $x$ and $d y$ coprime) for some integer $l > 0$. If $p \in S(d)$,
then $l_p$ is the least integer $l > 0$ such that $|x^2 - d y^2| = p^l$ has a strictly primitive
integral solution; if $p \notin S(d)$, then $l_p = 0$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Notation 2.

Formalized by `MetaMathlibExt.strictPrimitiveExponent`, a definition declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-exponent).

## Vanishing of the strictly primitive exponent

Let $d$ be an integer and let $S(d)$ be the
set of primes $p$ for which $|x^2 - d y^2| = p^l$ has a strictly primitive integral solution
($x$ and $d y$ coprime) for some integer $l > 0$. Let $l_p$ be the least such $l$ when
$p \in S(d)$, and $l_p = 0$ otherwise. Then $l_p = 0$ for every natural number $p \notin S(d)$,
in particular for every $p$ that is not prime.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Notation 2.

Formalized by `MetaMathlibExt.strictPrimitiveExponent_of_not_mem`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-exponent-of-not-mem).

## The strictly primitive exponent is attained

Let $d$ be an integer and let $S(d)$ be the
set of primes $p$ for which $|x^2 - d y^2| = p^l$ has a strictly primitive integral solution
($x$ and $d y$ coprime) for some integer $l > 0$; for $p \in S(d)$ let $l_p$ be the least such
$l$. Then for every $p \in S(d)$, $l_p > 0$ and $|x^2 - d y^2| = p^{l_p}$ has a strictly
primitive integral solution.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Notation 2.

Formalized by `MetaMathlibExt.strictPrimitiveExponent_spec`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-exponent-spec).

## Minimality of the strictly primitive exponent

Let $d$ be an integer and let $S(d)$ be the
set of primes $p$ for which $|x^2 - d y^2| = p^l$ has a strictly primitive integral solution
($x$ and $d y$ coprime) for some integer $l > 0$; for $p \in S(d)$ let $l_p$ be the least such
$l$. If $p \in S(d)$ and $l > 0$ is an integer for which $|x^2 - d y^2| = p^l$ has a strictly
primitive integral solution, then $l_p \le l$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Notation 2.

Formalized by `MetaMathlibExt.strictPrimitiveExponent_le`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-exponent-le).

## $7$ is a strictly primitive prime for $d = 2$

The prime $7$ belongs to $S(2)$, the set of
primes $p$ for which $|x^2 - 2 y^2| = p^l$ has a strictly primitive integral solution ($x$ and
$2 y$ coprime) for some integer $l > 0$. A witness is $3^2 - 2 \cdot 1^2 = 7$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Notation 2.

Formalized by `MetaMathlibExt.seven_mem_strictPrimitivePrimes_two`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#seven-mem-strict-primitive-primes-two).

## The strictly primitive exponent of 7 for d = 2

For $d = 2$ and $p = 7$, the strictly
primitive exponent $l_7$ equals $1$: the least integer $l > 0$ such that $|x^2 - 2 y^2| = 7^l$ has
an integral solution with $x$ and $2 y$ coprime exists and equals $1$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Notation 2.

Formalized by `MetaMathlibExt.strictPrimitiveExponent_two_seven`, a theorem declared in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-exponent-two-seven).

## Pythagorean parametrization of rational solutions of the bisector equation

Let $a, b, c$
be rational numbers with $|a| \ne |b|$ and $(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1)$, and suppose
that $a^2 + 1$ and $b^2 + 1$ are squares of rational numbers. Then there are integers $l, m, n$ with
$|l| \ne |m|$, $l m \ne n^2$ and $l m n \ne 0$ such that

$$a = \frac{l^2 - n^2}{2 l n}, \qquad b = \frac{m^2 - n^2}{2 m n},$$

and

$$c = \frac{l m - n^2}{(l + m) n} \qquad \text{or} \qquad c = -\frac{(l + m) n}{l m - n^2}.$$

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 1(i).

Stated but not proved: `MetaMathlibExt.bisector_equation_rat_solution_pythagorean` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-rat-solution-pythagore).

## Parametric rational solutions of the bisector equation

Let $l, m, n$ be integers with
$|l| \ne |m|$, $l m \ne n^2$ and $l m n \ne 0$, and put

$$a = \frac{l^2 - n^2}{2 l n}, \qquad b = \frac{m^2 - n^2}{2 m n}.$$

Then each of the rational numbers

$$c = \frac{l m - n^2}{(l + m) n} \qquad \text{and} \qquad c = -\frac{(l + m) n}{l m - n^2}$$

satisfies $(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1)$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 1, converse for (2).

Stated but not proved: `MetaMathlibExt.bisector_equation_form_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-form-two).

## Rational solutions of the bisector equation for square-free $d > 1$

Let $d > 1$ be a
square-free integer and let $a, b, c$ be rational numbers with $|a| \ne |b|$ and

$$(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1).$$

Suppose there are rational numbers $u, v$ with $a^2 - d u^2 = -1$ and $b^2 - d v^2 = -1$. Then
there are rational numbers $a_2, b_2$ with $a^2 - d a_2^2 = -1$ and $b^2 - d b_2^2 = -1$ such
that either $a_2 + b_2 \ne 0$ and $c = (a b_2 + a_2 b) / (a_2 + b_2)$, or $a b_2 + a_2 b \ne 0$
and $c = -(a_2 + b_2) / (a b_2 + a_2 b)$.

In terms of $\alpha = a + a_2 \sqrt{d}$ and $\beta = b + b_2 \sqrt{d}$, which have norm $-1$, and
the conjugation $'$ of $\mathbb{Q}(\sqrt{d})$, the first quotient is
$(\alpha\beta - (\alpha\beta)') / (\alpha + \beta - (\alpha + \beta)')$.

## Sources

- the theorem's second part (the factorization of $\alpha, \beta$ through $\eta$, $\xi_p$ and $S(d)$) is not stated here.
- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 1(ii), first sentence.

Stated but not proved: `MetaMathlibExt.bisector_equation_rat_solution_negPell` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-rat-solution-neg-pell).

## Bisector-equation solutions from two solutions of $x^2 - d y^2 = -1$

Let $d$ be an integer
and let $a, a_2, b, b_2$ be rational numbers with $a^2 - d a_2^2 = -1$ and $b^2 - d b_2^2 = -1$.
If $a_2 + b_2 \ne 0$, then $c = (a b_2 + a_2 b) / (a_2 + b_2)$ satisfies

$$(a - c)^2 (b^2 + 1) = (b - c)^2 (a^2 + 1),$$

and if $a b_2 + a_2 b \ne 0$, then $c = -(a_2 + b_2) / (a b_2 + a_2 b)$ satisfies it as well.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 1, converse for (3).

Stated but not proved: `MetaMathlibExt.bisector_equation_form_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#bisector-equation-form-three).

## Products of strictly primitive solutions

Let $d > 1$ be a square-free integer. Write
elements of $\mathbb{Z}[\sqrt{d}]$ as $u + v\sqrt{d}$ with integers $u, v$, and let
$N(u + v\sqrt{d}) = u^2 - d v^2$ be the norm. Let $p_1, \dots, p_r$ be distinct primes and
$n_1, \dots, n_r$ natural numbers, and suppose that each $a_i = u_i + v_i\sqrt{d}$ satisfies
$|N(a_i)| = p_i^{n_i}$ with $u_i$ and $d v_i$ coprime. Then $a = a_1 \cdots a_r = u + v\sqrt{d}$
satisfies $|N(a)| = p_1^{n_1} \cdots p_r^{n_r}$ with $u$ and $d v$ coprime; that is, $a$ gives a
strictly primitive solution of $|x^2 - d y^2| = p_1^{n_1} \cdots p_r^{n_r}$.

The sign $\pm$ in the source's equation (13) is dropped; negation preserves both conclusions.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 3(a).

Stated but not proved: `MetaMathlibExt.strictlyPrimitive_prod` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strictly-primitive-prod).

## Powers of strictly primitive solutions

Let $d > 1$ be a square-free integer, $p$ an odd
prime, and $m, n > 0$ natural numbers. Write elements of $\mathbb{Z}[\sqrt{d}]$ as $u + v\sqrt{d}$
with integers $u, v$, and let $N(u + v\sqrt{d}) = u^2 - d v^2$ be the norm. If
$a = u + v\sqrt{d}$ satisfies $|N(a)| = p^m$ with $u$ and $d v$ coprime, then
$a^n = u' + v'\sqrt{d}$ satisfies $|N(a^n)| = p^{mn}$ with $u'$ and $d v'$ coprime; that is, $a^n$
gives a strictly primitive solution of $|x^2 - d y^2| = p^{mn}$.

The source states this without $p \ne 2$, and it fails for $p = 2$: for $d = 3$ and
$a = 1 + \sqrt{3}$ we have $N(a) = -2$, but $a^2 = 4 + 2\sqrt{3}$ and $\gcd(4, 6) = 2$. The sign
$\pm$ in the source's equation (14) is dropped.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 3(b).

Stated but not proved: `MetaMathlibExt.strictlyPrimitive_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strictly-primitive-pow).

## Negating the value of a strictly primitive solution

Let $d > 1$ be a square-free integer
such that $x^2 - d y^2 = -1$ has an integral solution, and let $z \ne 0$ be an integer. If
$x^2 - d y^2 = z$ has an integral solution with $x$ and $d y$ coprime, then so does
$x^2 - d y^2 = -z$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Proposition 4.

Stated but not proved: `MetaMathlibExt.strictlyPrimitive_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strictly-primitive-neg).

## Strictly primitive solutions modulo p and splitting of p

Let $d > 1$ be a square-free
integer, let $K$ be a number field of degree $2$ over $\mathbb{Q}$ containing an element $s$ with
$s^2 = d$ (so $K = \mathbb{Q}(\sqrt d)$), and let $p$ be a prime such that $p \ne 2$, or
$d \equiv 1 \pmod 8$, or $d \equiv 2 \pmod 4$. Then there are integers $x, y$ with $x$ and $dy$
coprime and $p \mid x^2 - dy^2$ if and only if $p$ splits in $K$, that is, exactly two prime
ideals of the ring of integers of $K$ lie over $p$.

In the paper's terms: $|x^2 - dy^2| = z$ has a strictly primitive integral solution for some
multiple $z$ of $p$ exactly when $p$ splits. The paper requires only $p \ne 2$ or
$d \not\equiv 5 \pmod 8$; for $d \equiv 3 \pmod 4$ and $p = 2$ its statement fails: for $d = 3$,
$(x, y) = (1, 1)$ gives $|1 - 3| = 2$ with $\gcd(1, 3) = 1$, while $2$ ramifies in
$\mathbb{Q}(\sqrt 3)$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 7.

Stated but not proved: `MetaMathlibExt.exists_strictlyPrimitive_dvd_iff_split` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#exists-strictly-primitive-dvd-iff-split).

## Strictly primitive primes are the split primes

Let $d > 1$ be a square-free integer, let
$K$ be any number field of degree $2$ over $\mathbb{Q}$ containing an element $s$ with $s^2 = d$,
and let $\mathcal{O}_K$ be its ring of integers. Suppose that $d \equiv 1 \pmod 8$, or that
$d \equiv 5 \pmod 8$ and every unit of $\mathcal{O}_K$ lies in $\mathbb{Z}[s]$, or that
$d \equiv 2 \pmod 4$. Then $S(d)$, the set of primes $p$ for which $|x^2 - d y^2| = p^l$ has an
integral solution with $x$ and $d y$ coprime for some integer $l > 0$, is the set of primes $p$
that split in $K$, that is, for which exactly two prime ideals of $\mathcal{O}_K$ lie over
$p\mathbb{Z}$.

Every unit of $\mathcal{O}_K$ lies in $\mathbb{Z}[s]$ exactly when the fundamental unit $\eta$ of
$K$ does, since the units are $\pm \eta^n$. The source also lists $d \equiv 3 \pmod 4$, where the
statement fails: $2 \in S(3)$ because $|1^2 - 3 \cdot 1^2| = 2$, but $2$ ramifies in
$\mathbb{Q}(\sqrt{3})$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 8(a).

Stated but not proved: `MetaMathlibExt.strictPrimitivePrimes_eq_split` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-primes-eq-split).

## Strictly primitive primes are 2 and the split primes

Let $d > 1$ be a square-free
integer, let $K$ be any number field of degree $2$ over $\mathbb{Q}$ containing an element $s$
with $s^2 = d$, and let $\mathcal{O}_K$ be its ring of integers. Suppose that $d \equiv 5 \pmod 8$
and that some unit of $\mathcal{O}_K$ does not lie in $\mathbb{Z}[s]$ (equivalently, the
fundamental unit of $K$ does not lie in $\mathbb{Z}[s]$). Then $S(d)$, the set of primes $p$ for
which $|x^2 - d y^2| = p^l$ has an integral solution with $x$ and $d y$ coprime for some integer
$l > 0$, consists of $2$ together with the primes $p$ that split in $K$, that is, for which
exactly two prime ideals of $\mathcal{O}_K$ lie over $p\mathbb{Z}$.

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Theorem 8(b).

Stated but not proved: `MetaMathlibExt.strictPrimitivePrimes_eq_split_insert_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-primes-eq-split-insert).

## The strictly primitive exponent is at most the class number

Let $d > 1$ be a squarefree
integer with $d \equiv 2$ or $d \equiv 3 \pmod 4$, and let $K$ be a number field of degree $2$
containing a square root of $d$ (so $K \cong \mathbb{Q}(\sqrt{d})$). Let $S(d)$ be the set of
primes $p$ for which $|x^2 - d y^2| = p^l$ has a strictly primitive integral solution ($x$ and
$d y$ coprime) for some integer $l > 0$, and for $p \in S(d)$ let $l_p$ be the least such $l$.
Then $l_p \le h_K$ for every $p \in S(d)$, where $h_K$ is the class number of $K$.

The source states this for all squarefree $d > 1$ except $d \equiv 1 \pmod 4$ with $p = 2$. For
$d \equiv 5 \pmod 8$ that is false: $\mathbb{Q}(\sqrt{37})$ has class number $1$, but $l_3 = 3$
for $d = 37$, since $8^2 - 37 \cdot 1^2 = 27$ while $|x^2 - 37 y^2| = 3$ and $|x^2 - 37 y^2| = 9$
have no strictly primitive solutions (the elements of norm $\pm 3$ and $\pm 9$ generating
primitive ideals are $(5 \pm \sqrt{37}) / 2$ and $(31 \pm 5\sqrt{37}) / 2$ times units, and all
units lie in $\mathbb{Z}[\sqrt{37}]$).

## Sources

- Takashi Hirotsu, *General Pell's Equations and Angle Bisectors between Planar Lines with Rational Slopes*, INTEGERS 24 (2024), Article A111, Corollary 1.

Stated but not proved: `MetaMathlibExt.strictPrimitiveExponent_le_classNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralPellBisectorsWanted.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html#strict-primitive-exponent-le-class-numbe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Negative Pell equation and angle bisectors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/negative-pell-equation-and-angle-bisectors)
