---
declaration: section
origin: cited
lean: MetaMathlibExt.sectorLatticePoints, MetaMathlibExt.zero_mem_sectorLatticePoints, MetaMathlibExt.IsQuadraticPackingPolynomial, MetaMathlibExt.IsQuadraticPackingPolynomial.exists_nat_eq, MetaMathlibExt.sectorStaircase, MetaMathlibExt.zero_mem_sectorStaircase_zero, MetaMathlibExt.staircaseFirstHeight, MetaMathlibExt.staircaseFirstHeight_zero
statement: formalized
---

# Quadratic packing polynomials

19 results, 10 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html).

## Lattice points of a sector

For a real number $\alpha$, let
$S(\alpha) = \{(x, y) \in \mathbb{R}^2 : 0 \le y \le \alpha x\}$ be the sector of slope
$\alpha$. Its lattice points are $I(\alpha) = S(\alpha) \cap \mathbb{Z}^2$, viewed as a subset
of $\mathbb{R}^2$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Section 1 (definition of `S(α)` and `I(α)`).

Formalized by `MetaMathlibExt.sectorLatticePoints`, a definition declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#sector-lattice-points).

## The origin is a lattice point of every sector

For every real number $\alpha$, the
origin $(0, 0)$ lies in the set $I(\alpha)$ of lattice points of the sector of slope $\alpha$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Section 1 (definition of `I(α)`).

Formalized by `MetaMathlibExt.zero_mem_sectorLatticePoints`, a theorem declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#zero-mem-sector-lattice-points).

## Quadratic packing polynomial

A real function $P(x, y)$ of two real variables is a
quadratic packing polynomial (QPP) on a set $S \subseteq \mathbb{R}^2$ if it is a polynomial of
total degree two, that is, $P(x, y) = a x^2 + b x y + c y^2 + d x + e y + f$ for some real
$a, b, c, d, e, f$ with $a, b, c$ not all zero, and $P$ maps $S$ bijectively onto the set
$\mathbb{N}_0 = \{0, 1, 2, \dots\}$ of natural numbers.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Definition 1.

Formalized by `MetaMathlibExt.IsQuadraticPackingPolynomial`, a definition declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#is-quadratic-packing-polynomial).

## Quadratic packing polynomials take natural-number values

If $P$ is a quadratic packing
polynomial on a set $S \subseteq \mathbb{R}^2$, then for every point $(x, y) \in S$ the value
$P(x, y)$ is a natural number.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Definition 1.

Formalized by `MetaMathlibExt.IsQuadraticPackingPolynomial.exists_nat_eq`, a theorem declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#exists-nat-eq).

## Staircases of a rational sector

For natural numbers $m, n, i$, let
$l = \gcd(m - 1, n)$. The $i$-th staircase of the sector of slope $n/m$ is
$J_i = \{(x, y) \in I(n/m) : nx - (m - 1)y = li\}$, where $I(n/m)$ is the set of lattice points
of that sector.

If $m = 0$, the slope $n/m$ is read as $0$ and $l$ as $\gcd(0, n) = n$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Section 2 (definition of the staircases `J_i`).

Formalized by `MetaMathlibExt.sectorStaircase`, a definition declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#sector-staircase).

## The origin lies on the zeroth staircase

For all natural numbers $m, n$, the origin
$(0, 0)$ lies on the staircase $J_0$ of the sector of slope $n/m$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Section 2 (definition of the staircases `J_i`).

Formalized by `MetaMathlibExt.zero_mem_sectorStaircase_zero`, a theorem declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#zero-mem-sector-staircase-zero).

## First height of a staircase

For natural numbers $m, n, i$, the first height $\bar y_i$
of the staircase $J_i$ of the sector of slope $n/m$ is the least $y$-coordinate of a point of
$J_i$, that is, the height of its first step; it is $0$ if $J_i$ is empty.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Section 3 (definition of `ȳ_i`).

Formalized by `MetaMathlibExt.staircaseFirstHeight`, a definition declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#staircase-first-height).

## The zeroth staircase starts at height zero

For all natural numbers $m, n$, the first
height of the staircase $J_0$ of the sector of slope $n/m$ is $\bar y_0 = 0$; indeed the origin
lies on $J_0$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Section 3 (definition of `ȳ_i`).

Formalized by `MetaMathlibExt.staircaseFirstHeight_zero`, a theorem declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#staircase-first-height-zero).

## Step difference

For natural numbers $m, n$ and a real function $P(x, y)$ of two real
variables, let $l = \gcd(m \mathbin{\dot-} 1, n)$, where $m \mathbin{\dot-} 1$ is subtraction
truncated at $0$ (so $l = n$ when $m = 0$). The step difference of $P$ for the sector of slope
$n/m$ is $k = P((m - 1)/l, n/l) - P(0, 0)$, with $m - 1$ here the real difference and division
by $l = 0$ read as $0$: the change $P(x + (m - 1)/l, y + n/l) - P(x, y)$ of $P$ between
consecutive steps of a staircase of the sector, evaluated at the base point $(0, 0)$.

For every polynomial of Stanton's form (Theorem 2 of the source) this difference does not
depend on the base point, which is how the source defines $k$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Section 2 (definition of `k`).

Formalized by `MetaMathlibExt.consecutiveStepDifference`, a definition declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#consecutive-step-difference).

## Step difference of the slope-$12/7$ example

Let
$P(x, y) = 6(x - y/2)(x - y/2 - 3/2) + x + y + 2$. For $m = 7$ and $n = 12$ (the sector of
slope $12/7$), the step difference of $P$ is $k = 3$: with $l = \gcd(6, 12) = 6$, one has
$P(1, 2) - P(0, 0) = 3$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Example 10.

Formalized by `MetaMathlibExt.consecutiveStepDifference_example_twelve_sevenths`, a theorem declared in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#consecutive-step-difference-example-twel).

## Form of a quadratic packing polynomial on a sector (Gjaldbæk)

Let $\alpha > 0$ be a real
number and let $P$ be a quadratic packing polynomial on the lattice sector $I(\alpha)$. Then there
are integers $A, B, C, D, E, F$ with $A > 0$, $B^2 = AC$ and $\alpha = A/(1 - B)$ such that for
all real $x, y$

$$P(x, y) = \tfrac{A}{2} x(x - 1) + Bxy + \tfrac{C}{2} y(y - 1) + Dx + Ey + F.$$

In particular $\alpha$ is rational.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Theorem 1.

Stated but not proved: `MetaMathlibExt.quadraticPackingPolynomial_sector_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#quadratic-packing-polynomial-sector-form).

## Stanton's form of a quadratic packing polynomial on a rational sector

Let $m, n$ be
coprime positive integers and let $P$ be a quadratic packing polynomial on the lattice points
$I(n/m)$ of the sector of slope $n/m$. Then $n$ divides $(m - 1)^2$, and there are integers
$D, E, F$ such that for all real $x, y$

$$
P(x, y) = \frac{n}{2} \left(x - \frac{m - 1}{n} y\right)^2 + \left(D - \frac{n}{2}\right) x +
  \left(E - \frac{(m - 1)^2}{2n}\right) y + F.
$$

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Theorem 2.

Stated but not proved: `MetaMathlibExt.quadraticPackingPolynomial_rational_sector_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#quadratic-packing-polynomial-rational-se).

## The slope-$12/7$ example on the sheared sector

Let $M(x, y) = (x - y/2, y)$ and let
$\hat I(12/7) = M(I(12/7))$ be the image under $M$ of the lattice points $I(12/7)$ of the sector
of slope $12/7$. Then $\hat P(x, y) = 6x(x - 3/2) + x + \frac{3}{2} y + 2$ is a quadratic
packing polynomial on $\hat I(12/7)$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Example 10 and Figure 3.

Stated but not proved: `MetaMathlibExt.isQuadraticPackingPolynomial_sheared_example_twelve_sevenths` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#is-quadratic-packing-polynomial-sheared).

## First step value and sheared form of a quadratic packing polynomial

Let $m, n$ be
coprime positive integers, let $l = \gcd(m - 1, n)$, and let $P$ be a quadratic packing
polynomial on the lattice points $I(n/m)$ of the sector of slope $n/m$ whose step difference
for $m, n$ is a positive integer $k$. Put $F = P(0, 0)$ and
$\hat P(x, y) = P(x + \frac{m - 1}{n} y, y)$, and let $\bar y_k$ be the height of the first step
of the $k$-th staircase of the sector. Then $\hat P(k/(n/l), \bar y_k) = F + k$, and for all
real $x, y$ one has $\hat P(x, y) = \frac{n}{2} x (x - 1) + D x + \frac{k}{n/l} y + F$ with
$D = n/l - (kl - n)/2 - \bar y_k$.

The step difference is taken as a natural number; by Theorem 1 of the source it is an integer
for every quadratic packing polynomial.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Lemma 1.

Stated but not proved: `MetaMathlibExt.quadraticPackingPolynomial_first_step_value` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#quadratic-packing-polynomial-first-step).

## Staircase congruence for quadratic packing polynomials

Let $m, n$ be positive coprime
integers, let $P$ be a quadratic packing polynomial on the lattice sector $I(n/m)$, and suppose
that the step difference of $P$ equals a positive integer $k$. Then for every natural number
$i$, every point $p$ of the staircase $J_i$ and every point $q$ of the staircase $J_{i+k}$, the
difference $P(q) - P(p)$ is an integer multiple of $k$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Lemma 2.

Stated but not proved: `MetaMathlibExt.quadraticPackingPolynomial_staircase_congruence` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#quadratic-packing-polynomial-staircase-c).

## Height of the first step of the k-th staircase

Let $m, n$ be positive coprime integers
and $l = \gcd(m - 1, n)$, let $P$ be a quadratic packing polynomial on the lattice sector
$I(n/m)$, and suppose that the step difference of $P$ equals a positive integer $k$. Then the
first height of the staircase $J_k$ is $\bar y_k = n/l - 1$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Lemma 3.

Stated but not proved: `MetaMathlibExt.quadraticPackingPolynomial_staircaseFirstHeight` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#quadratic-packing-polynomial-staircase-f).

## Sheared criterion for quadratic packing polynomials

Let $m, n$ be coprime positive
integers, let $l = \gcd(m - 1, n)$, and assume that $n/l$ divides $l$. Let $k$ be a positive
integer with $k \equiv (m - 1)/l \pmod{n/l}$, let $F$ be a real number, and let
$\hat P(x, y) = \frac{n}{2} x \left(x - \frac{k}{n/l}\right) + x + \frac{k}{n/l} y + F$. Let
$M(x, y) = (x - \frac{m - 1}{n} y, y)$ and let $\hat I(n/m) = M(I(n/m))$ be the image under $M$
of the lattice points $I(n/m)$ of the sector of slope $n/m$. Then $\hat P$ is a quadratic
packing polynomial on $\hat I(n/m)$ if and only if
$\{\hat P(i/(n/l), \bar y_i) : 0 \le i < k\} = \{0, 1, \dots, k - 1\}$, where $\bar y_i$ is the
height of the first step of the $i$-th staircase of the sector of slope $n/m$.

The divisibility $n/l \mid l$ is a standing assumption of the source, made explicit here.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Lemma 4.

Stated but not proved: `MetaMathlibExt.isQuadraticPackingPolynomial_sheared_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#is-quadratic-packing-polynomial-sheared-2).

## Constant term of a quadratic packing polynomial on a rational sector

Let $m, n$ be
coprime positive integers, let $l = \gcd(m - 1, n)$, and let $P$ be a quadratic packing
polynomial on the lattice points $I(n/m)$ of the sector of slope $n/m$. If the step difference
of $P$ for $m, n$ is a positive integer $k$, then $P(0, 0) = \frac{l^2}{n} (k - 1)(k + 1)/12$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Lemma 5.

Stated but not proved: `MetaMathlibExt.quadraticPackingPolynomial_constant_term` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#quadratic-packing-polynomial-constant-te).

## Step-difference form of a quadratic packing polynomial on a rational sector

Let $m, n$
be coprime positive integers, let $l = \gcd(m - 1, n)$, and let $P$ be a quadratic packing
polynomial on the lattice points $I(n/m)$ of the sector of slope $n/m$ whose step difference
for $m, n$ is a positive integer $k$. Then $n/l$ divides $l$, $k \equiv (m - 1)/l \pmod{n/l}$,
and for all real $x, y$ one has $P(x + \frac{m - 1}{n} y, y) =
\frac{n}{2} x \left(x - \frac{k}{n/l}\right) + x + \frac{k}{n/l} y + P(0, 0)$.

## Sources

- Brandt and Gjaldbæk, *Classification of Quadratic Packing Polynomials on Sectors of R^2*, INTEGERS 25 (2025), Article A81, Proposition 1.

Stated but not proved: `MetaMathlibExt.quadraticPackingPolynomial_necessary_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticPackingPolynomialsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html#quadratic-packing-polynomial-necessary-f).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadratic packing polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/quadratic-packing-polynomials)
