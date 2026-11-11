---
declaration: section
origin: cited
lean: MetaMathlibExt.squareThetaSeries, MetaMathlibExt.triangularThetaSeries, MetaMathlibExt.coeff_squareThetaSeries_small, MetaMathlibExt.coeff_triangularThetaSeries_small, MetaMathlibExt.isUnit_squareThetaSeries, MetaMathlibExt.isUnit_triangularThetaSeries, MetaMathlibExt.sumOfSquaresRepCount, MetaMathlibExt.sumOfTriangularRepCount
statement: formalized
---

# Representations by squares and triangular numbers

23 results, 12 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html).

## The square theta series

The square theta series is the formal power series
$\theta(q) = \sum_{m \in \mathbb{Z}} q^{m^2}$ in $\mathbb{Z}[[q]]$: for each $n \ge 0$, its
coefficient of $q^n$ is the number of integers $m$ with $m^2 = n$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.squareThetaSeries`, a definition declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#square-theta-series).

## Triangular theta series

The triangular theta series is the formal power series
$\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$ with integer coefficients: for each natural number $n$,
its coefficient of $q^n$ is the number of natural numbers $m$ with $m(m+1)/2 = n$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.triangularThetaSeries`, a definition declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#triangular-theta-series).

## First coefficients of the square theta series

In the square theta series
$\theta(q) = \sum_{m \in \mathbb{Z}} q^{m^2}$, the coefficients of $q^0$, $q^1$, $q^2$ and $q^4$ are
$1$, $2$, $0$ and $2$ respectively.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.coeff_squareThetaSeries_small`, a theorem declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#coeff-square-theta-series-small).

## First coefficients of the triangular theta series

In the triangular theta series
$\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$, the coefficients of $q^0$, $q^1$, $q^2$ and $q^3$ are $1$,
$1$, $0$ and $1$ respectively.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.coeff_triangularThetaSeries_small`, a theorem declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#coeff-triangular-theta-series-small).

## The square theta series is a unit

The square theta series
$\theta(q) = \sum_{m \in \mathbb{Z}} q^{m^2}$ is a unit of the ring $\mathbb{Z}[[q]]$ of formal
power series with integer coefficients, since its constant coefficient is $1$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.isUnit_squareThetaSeries`, a theorem declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#is-unit-square-theta-series).

## The triangular theta series is a unit

The triangular theta series
$\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$ is a unit of the ring $\mathbb{Z}[[q]]$ of formal power
series with integer coefficients, since its constant coefficient is $1$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.isUnit_triangularThetaSeries`, a theorem declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#is-unit-triangular-theta-series).

## Representation numbers for sums of squares

For an integer $k$ and a natural number $n$,
$r_k(n)$ is the coefficient of $q^n$ in $\theta(q)^k$, where
$\theta(q) = \sum_{m \in \mathbb{Z}} q^{m^2}$. Since $\theta$ has constant coefficient $1$, it is a
unit of $\mathbb{Z}[[q]]$, so $\theta^k$ is a power series for negative $k$ as well.

For $k \ge 1$, $r_k(n)$ is the number of ways to write $n$ as an ordered sum of $k$ squares of
integers.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.sumOfSquaresRepCount`, a definition declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-squares-rep-count).

## Representation numbers for sums of triangular numbers

For an integer $k$ and a natural
number $n$, $t_k(n)$ is the coefficient of $q^n$ in $\psi(q)^k$, where
$\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$. Since $\psi$ has constant coefficient $1$, it is a unit of
$\mathbb{Z}[[q]]$, so $\psi^k$ is a power series for negative $k$ as well.

For $k \ge 1$, $t_k(n)$ is the number of ways to write $n$ as an ordered sum of $k$ triangular
numbers $m(m+1)/2$ with $m \ge 0$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.sumOfTriangularRepCount`, a definition declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-triangular-rep-count).

## The one-square counts are the coefficients of the square theta series

For an integer $k$
and $n \ge 0$, let $r_k(n)$ be the coefficient of $q^n$ in $\theta(q)^k$, where $\theta$ is the
square theta series. Then for every $n \ge 0$, $r_1(n)$ equals the coefficient of $q^n$ in
$\theta(q)$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.sumOfSquaresRepCount_one`, a theorem declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-squares-rep-count-one).

## Triangular representation numbers with one summand

For an integer $k$, let $t_k(n)$ be the
coefficient of $q^n$ in $\psi(q)^k$, where $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$. Then for every
natural number $n$, $t_1(n)$ equals the coefficient of $q^n$ in $\psi(q)$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Section 1.

Formalized by `MetaMathlibExt.sumOfTriangularRepCount_one`, a theorem declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-triangular-rep-count-one).

## Divisibility of square representation counts by a large prime is periodic

For an integer
$k$ and $n \ge 0$, let $r_k(n)$ be the coefficient of $q^n$ in $\theta(q)^k$, where $\theta$ is the
square theta series; for $k \ge 1$ it is the number of representations of $n$ as an ordered sum of
$k$ squares of integers. Let $n \ge 1$ and $k \ge 1$ be integers and let $p$ be a prime with
$p \ge n + 1$. If $p$ divides $r_k(n)$, then $p$ divides $r_{k+jp}(n)$ for every integer $j$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 3.

Stated but not proved: `MetaMathlibExt.sumOfSquaresRepCount_add_mul_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-squares-rep-count-add-mul-prime).

## Prime divisibility of triangular representation numbers persists under prime shifts

For an
integer $k$, let $t_k(n)$ be the coefficient of $q^n$ in $\psi(q)^k$, where
$\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$. Let $n \ge 1$ and $k \ge 1$ be natural numbers and let $p$
be a prime with $p \ge n + 1$. If $p$ divides $t_k(n)$, then $p$ divides $t_{k+rp}(n)$ for every
integer $r$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 4.

Stated but not proved: `MetaMathlibExt.sumOfTriangularRepCount_add_mul_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-triangular-rep-count-add-mul-prim).

## Window congruence for sums of squares

For an integer $k$, let $r_k(n)$ be the coefficient
of $q^n$ in $\theta(q)^k$, where $\theta(q) = \sum_{m \in \mathbb{Z}} q^{m^2}$. Let $n \ge 1$, let
$p$ be an odd prime with $p - 1 \ge n + 1$, and let $s \ge p$ be an integer. Then $p$ divides
$\sum_{i=0}^{p-1} r_{s-i}(n)$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 5.

Stated but not proved: `MetaMathlibExt.sum_sumOfSquaresRepCount_window` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-sum-of-squares-rep-count-window).

## Window congruence for sums of triangular numbers

For an integer $k$, let $t_k(n)$ be the
coefficient of $q^n$ in $\psi(q)^k$, where $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$. Let $n \ge 1$,
let $p$ be an odd prime with $p - 1 \ge n + 1$, and let $s \ge p$ be an integer. Then $p$ divides
$\sum_{i=0}^{p-1} t_{s-i}(n)$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 6.

Stated but not proved: `MetaMathlibExt.sum_sumOfTriangularRepCount_window` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-sum-of-triangular-rep-count-window).

## Representability criterion from a window of counts

For an integer $k$ and $n \ge 0$, let
$r_k(n)$ and $t_k(n)$ be the coefficients of $q^n$ in $\theta(q)^k$ and $\psi(q)^k$, where $\theta$
and $\psi$ are the square and triangular theta series (units of $\mathbb{Z}[[q]]$). Let $n \ge 1$,
let $p$ be an odd prime with $p - 1 \ge n + 1$, and let $s$ be an integer. If $p$ does not divide
$r_{s-1}(n) + r_{s-2}(n) + \cdots + r_{s-(p-1)}(n)$, then $r_s(n) \ne 0$. Likewise, if $p$ does not
divide $t_{s-1}(n) + t_{s-2}(n) + \cdots + t_{s-(p-1)}(n)$, then $t_s(n) \ne 0$.

The source places no condition on $s$, so the statement is made for every integer $s$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 7.

Stated but not proved: `MetaMathlibExt.repCount_ne_zero_of_window` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#rep-count-ne-zero-of-window).

## Window criterion for representability by triangular numbers

For an integer $k$, let
$t_k(n)$ be the coefficient of $q^n$ in $\psi(q)^k$, where $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$.
Let $n \ge 1$ and let $p$ be an odd prime with $p - 1 \ge n + 1$. For every integer $s$, if $p$ does
not divide $\sum_{i=1}^{p-1} t_{s-i}(n)$, then $t_s(n) \ne 0$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 8.

Stated but not proved: `MetaMathlibExt.sumOfTriangularRepCount_ne_zero_of_window` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-triangular-rep-count-ne-zero-of-w).

## A prime between $p/2$ and $p$ divides the representation counts of $p$

For integers
$k, n \ge 1$, let $r_k(n)$ be the number of representations of $n$ as an ordered sum of $k$ squares
of integers and $t_k(n)$ the number of representations of $n$ as an ordered sum of $k$ triangular
numbers $m(m+1)/2$ with $m \ge 0$. Let $p$ be an odd prime and $\ell$ a prime with
$p/2 < \ell < p$. Then $\ell$ divides both $r_\ell(p)$ and $t_\ell(p)$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 11.

Stated but not proved: `MetaMathlibExt.prime_dvd_repCount_of_half_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#prime-dvd-rep-count-of-half-lt).

## Logarithmic coefficients of the triangular theta series

For a natural number $n$, let
$b_n$ be the rational number
$b_n = \sum_{d \mid n,\ n/d \text{ odd}} 1/d - \sum_{d \mid n,\ n/d \text{ even}} 1/d$, where $d$
runs over the positive divisors of $n$; for $n = 0$ the sums are taken to be empty, so $b_0 = 0$.

With $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$, the expansion
$\log \psi(q) = \sum_{m \ge 1} \log(1 - q^{2m}) - \sum_{m \ge 1} \log(1 - q^{2m-1})$ in the proof
of Theorem 2 shows that $b_n$ is the coefficient of $q^n$ in $\log \psi(q)$. The printed formula
of Theorem 2 has the parity condition on $d$ instead of $n/d$, which gives $b_2 = 1/2$ instead
of $-1/2$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 2 and its proof.

Formalized by `MetaMathlibExt.triangularLogCoeff`, a definition declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#triangular-log-coeff).

## First logarithmic coefficients of the triangular theta series

The logarithmic
coefficients $b_n$ of the triangular theta series satisfy $b_1 = 1$, $b_2 = -1/2$ and
$b_3 = 4/3$; this matches the expansion
$\log(1 + q + q^3 + \cdots) = q - q^2/2 + 4q^3/3 + \cdots$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 2 and its proof.

Formalized by `MetaMathlibExt.triangularLogCoeff_small`, a theorem declared in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#triangular-log-coeff-small).

## Composition formula for triangular representation numbers

For an integer $k$, let $t_k(n)$
be the coefficient of $q^n$ in $\psi(q)^k$, where $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$. For
$m \ge 1$ let
$b_m = \sum_{d \mid m,\ m/d \text{ odd}} 1/d - \sum_{d \mid m,\ m/d \text{ even}} 1/d$, the
coefficient of $q^m$ in $\log \psi(q)$. Then for every integer $k$ and natural number $n$,

$$t_k(n) = \sum_{(w_1, \dots, w_l)} \frac{k^l}{l!}\, b_{w_1} \cdots b_{w_l},$$

where the sum runs over all compositions $(w_1, \dots, w_l)$ of $n$, that is, all tuples of positive
integers with sum $n$, of every length $l$ (for $n = 0$, only the empty composition).

The source prints $b_m$ with the parity condition on $d$ instead of $m/d$; with that coefficient the
formula fails, giving $t_1(2) = 1$ although $t_1(2) = 0$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 2.

Stated but not proved: `MetaMathlibExt.sumOfTriangularRepCount_eq_sum_compositions` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-triangular-rep-count-eq-sum-compo).

## Recurrence for triangular representation numbers

For an integer $k$, let $t_k(n)$ be the
coefficient of $q^n$ in $\psi(q)^k$, where $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$. For $m \ge 1$
let $b_m = \sum_{d \mid m,\ m/d \text{ odd}} 1/d - \sum_{d \mid m,\ m/d \text{ even}} 1/d$, the
coefficient of $q^m$ in $\log \psi(q)$. Then for every integer $k$ and natural number $n$,

$$t_k(n + 1) = \sum_{j=0}^{n} \frac{k (j + 1)\, b_{j+1}}{n + 1}\, t_k(n - j).$$

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Corollary 1, second recurrence.

Stated but not proved: `MetaMathlibExt.sumOfTriangularRepCount_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-triangular-rep-count-succ).

## Integer zeros of the sums-of-squares counting polynomial

For an integer $k$ and $n \ge 0$,
let $r_k(n)$ be the coefficient of $q^n$ in $\theta(q)^k$, where $\theta$ is the square theta
series. For every $n \ge 0$ there is a polynomial $P(z) = \sum_i c_i z^i$ with integer
coefficients such that $P(z) = n! \, r_z(n)$ for every integer $z$, and every nonzero integer $k$
with $r_k(n) = 0$ divides $c_1$ and satisfies $|k| < 2 |c_i|^{1/(n-i)}$ for some $i$ with
$0 \le i < n$.

Equivalently, $|k| < 2 R_n$ with $R_n = \max_{0 \le i \le n-1} |c_i|^{1/(n-i)}$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 9.

Stated but not proved: `MetaMathlibExt.sumOfSquaresRepCount_integer_root` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-squares-rep-count-integer-root).

## Integer roots of triangular representation numbers

For an integer $k$, let $t_k(n)$ be the
coefficient of $q^n$ in $\psi(q)^k$, where $\psi(q) = \sum_{m \ge 0} q^{m(m+1)/2}$. For every
natural number $n$ there is a polynomial $P(z) = \sum_i a_i z^i$ with integer coefficients such that
$P(z) = n!\, t_z(n)$ for every integer $z$, and every nonzero integer $k$ with $t_k(n) = 0$ divides
$a_1$ and satisfies $|k| < 2 |a_i|^{1/(n-i)}$ for some $i < n$.

For $n \ge 1$ the bound says $|k| < 2 \max_{0 \le i \le n-1} |a_i|^{1/(n-i)}$.

## Sources

- Alegri and Christopher, *On Formulas, Recurrences, and Congruences for Representations of Integers as Sums of Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A93, Theorem 10.

Stated but not proved: `MetaMathlibExt.sumOfTriangularRepCount_integer_root` is written with `theorem_wanted` in [WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SquaresTriangularRepresentationsWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html#sum-of-triangular-rep-count-integer-root).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representations by squares and triangular numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-squares-and-triangular-number)
