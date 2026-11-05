---
article_id: af_ef0679783f8802be4f017db9
concept: char_dvd_card_solutions
---

The **Chevalley–Warning theorem** says that a polynomial equation over a
[finite field](trough:Mathlib.FieldTheory.Finite.Basic) whose degree is smaller
than its number of variables has a number of solutions divisible by the
[characteristic](trough:CharP) of the field. It turns a bound on degrees into a
congruence on a count, and so yields existence results directly: if such an
equation has one obvious solution, the count cannot be $1$, so it has another.
This is the standard route to the fact that every quadratic form in three or more
variables over a finite field has a nontrivial zero, and to the
[Erdős–Ginzburg–Ziv theorem](trough:ZMod.erdos_ginzburg_ziv) of additive
combinatorics.

## Statement

Let $K$ be a finite field with $q$ elements and characteristic $p$; then
[$p$ is prime and $q$ is a power of $p$](lean:FiniteField.card). Let $f$ be a
[polynomial](trough:MvPolynomial) in $n$ variables $x_1, \dots, x_n$ with
coefficients in $K$, and let $d$ be its
[total degree](lean:MvPolynomial.totalDegree), the largest degree of a monomial
occurring in $f$. If $d < n$, then
[$p$ divides the number of points $x \in K^n$ with $f(x) = 0$](lean:char_dvd_card_solutions).

The same conclusion holds for several polynomials at once. If $f_1, \dots, f_r$
have total degrees $d_1, \dots, d_r$ with

$$d_1 + d_2 + \cdots + d_r < n,$$

then [$p$ divides the number of common zeros of $f_1, \dots, f_r$ in $K^n$](lean:char_dvd_card_solutions_of_sum_lt)
(see [the version for a family of polynomials](trough:char_dvd_card_solutions_of_sum_lt)).
The single-polynomial statement is the case $r = 1$.

## Examples

- **A sum of three squares.** Over the field with $3$ elements, the equation
  $x^2 + y^2 + z^2 = 0$ has degree $2 < 3$. Each square is $0$ or $1$, so a
  solution has either all coordinates zero ($1$ point) or all coordinates nonzero
  ($2^3 = 8$ points), for $9$ solutions in total, a multiple of $3$.
- **Nontrivial zeros.** If $f$ has no constant term and degree less than $n$, then
  $f(0, \dots, 0) = 0$, so the number of zeros is a positive multiple of $p$, hence
  at least $p \ge 2$, and $f$ has a zero other than the origin. In particular every
  [quadratic form](trough:QuadraticForm) in at least three variables over a finite
  field has a nontrivial zero.
- **The degree bound is sharp.** For $n \ge 1$ the product $x_1 x_2 \cdots x_n$ has degree
  exactly $n$. Its zeros are the points with some coordinate zero, so there are
  $q^n - (q-1)^n$ of them, which is congruent to $\pm 1$ modulo $p$ because
  $q \equiv 0 \pmod p$. So the hypothesis $d < n$ cannot be weakened to $d \le n$:
  the conclusion can fail when $d = n$.

## Proof

The argument works with values in $K$ and compares them with the count at the end.

**An indicator polynomial.** For every nonzero $a \in K$,
[$a^{q-1} = 1$](lean:FiniteField.pow_card_sub_one_eq_one), the finite-field form of
[Fermat's little theorem](trough:ZMod.pow_card_sub_one_eq_one). So $1 - a^{q-1}$
equals $1$ when $a = 0$ and $0$ otherwise. Hence the polynomial

$$F = \prod_{i=1}^{r} \bigl(1 - f_i^{\,q-1}\bigr)$$

takes the value $1$ at common zeros of the $f_i$ and $0$ elsewhere, and the sum of
$F(x)$ over all $x \in K^n$ is the number $N$ of common zeros, read as an element
of $K$.

**Power sums vanish.** For $0 \le k < q - 1$,
[the sum of $a^k$ over all $a \in K$ is $0$](lean:FiniteField.sum_pow_lt_card_sub_one)
(with $0^0 = 1$, the case $k = 0$ is the sum of $q$ ones). A monomial
$x_1^{e_1} \cdots x_n^{e_n}$ of total degree less than $(q-1)n$ has some exponent
$e_j < q - 1$, and summing over the coordinate $x_j$ first makes its total sum
vanish. Therefore
[every polynomial of total degree less than $(q-1)n$ sums to $0$ over $K^n$](lean:MvPolynomial.sum_eval_eq_zero).

**Conclusion.** The total degree of $F$ is at most
$(q-1)(d_1 + \cdots + d_r)$, which is less than $(q-1)n$. So $N = 0$ in $K$, and
since [a natural number maps to $0$ in a ring of characteristic $p$ exactly when $p$ divides it](lean:CharP.cast_eq_zero_iff),
$p$ divides $N$.

## Consequences and generalizations

- **[Erdős–Ginzburg–Ziv theorem](trough:ZMod.erdos_ginzburg_ziv).** For every
  positive integer $m$,
  [any $2m - 1$ integers, repetitions allowed, include $m$ whose sum is divisible by $m$](lean:Int.erdos_ginzburg_ziv).
  For $m = p$ prime, given integers $a_1, \dots, a_{2p-1}$, the proof applies the
  theorem for two polynomials to $\sum_i x_i^{p-1} = 0$ and
  $\sum_i a_i x_i^{p-1} = 0$ (coefficients read modulo $p$) in $2p - 1$ variables
  over the field with $p$ elements; the general case follows by induction on the
  prime factors of $m$.
- **Lower bound.** Warning's second theorem adds that if the $f_i$ have at least
  one common zero and $d_1 + \cdots + d_r < n$, then they have at least
  $q^{\,n - (d_1 + \cdots + d_r)}$ common zeros.
- **Higher divisibility.** The Ax–Katz theorem sharpens the congruence: for polynomials of
  positive degree, the number of common zeros is divisible by $q^{\mu}$, where $\mu$ is the least integer that
  is at least $(n - d_1 - \cdots - d_r)/\max_i d_i$. Under the Chevalley–Warning
  hypothesis $\mu \ge 1$, so even $q$ divides the count.

## In Mathlib

Mathlib indexes the variables by an arbitrary finite type rather than by
$1, \dots, n$, so $n$ is the number of elements of that type and points are
functions from it to $K$. The characteristic enters as any natural number $p$ for
which $K$ has characteristic $p$; for a finite field this forces $p$ to be prime,
so the statement is the classical one. The total degree of the zero polynomial is
$0$, where many texts leave it undefined or set it to $-\infty$; this is harmless: when $f = 0$ and $n \ge 1$ every one
of the $q^n$ points is a zero, and $p$ divides $q^n$. Besides the single-polynomial
form, Mathlib proves the theorem for a family of polynomials indexed by a finite
set, for a family indexed by a finite type, and
[for a pair of polynomials](lean:char_dvd_card_solutions_of_add_lt), the form its
proof of the Erdős–Ginzburg–Ziv theorem uses.

## Depends on

- [Finite fields](trough:Mathlib.FieldTheory.Finite.Basic)
- [Characteristic p](trough:CharP)
- [Polynomial in several indeterminates](trough:MvPolynomial)

## Proof depends on

- [Fermat's little theorem](trough:ZMod.pow_card_sub_one_eq_one)
