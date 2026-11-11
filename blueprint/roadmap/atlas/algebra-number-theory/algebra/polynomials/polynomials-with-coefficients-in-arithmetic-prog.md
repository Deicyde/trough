---
declaration: section
origin: cited
lean: MetaMathlibExt.perron_irreducible, MetaMathlibExt.arithProgPoly_irreducible, MetaMathlibExt.arithProgPoly_four_not_mul_quadratics, MetaMathlibExt.arithProgPoly_irreducible_of_primitiveRoot, MetaMathlibExt.arithProgPoly_mul_sub_one_sq, MetaMathlibExt.arithProgPoly_root_pow_eq, MetaMathlibExt.arithProgPoly_eq3_existsUnique_pos, MetaMathlibExt.arithProgPoly_root_norm_le
statement: formalized
---

# Polynomials with coefficients in arithmetic progression

14 results, 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html).

## Perron's irreducibility criterion

Let $f = x^n + a_{n-1} x^{n-1} + \cdots + a_0$ be a
monic polynomial in $\mathbb{Z}[x]$ of degree $n \ge 1$ with $a_0 \neq 0$ and
$|a_{n-1}| > 1 + \sum_{i=0}^{n-2} |a_i|$. Then $f$ is irreducible in $\mathbb{Z}[x]$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Theorem 1 (Perron's criterion, quoted from the paper's reference [6]).

Stated but not proved: `MetaMathlibExt.perron_irreducible` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#perron-irreducible).

## Irreducibility of polynomials with coefficients in an arithmetic progression

Let
$m \ge 2$ and let $a$, $d$ be coprime positive integers with $m^2 d^2 < 8a$. Then the polynomial
$a x^m + (a + d) x^{m-1} + \cdots + (a + (m - 1)d) x + (a + md)$ is irreducible in
$\mathbb{Z}[x]$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Theorem 2.

Stated but not proved: `MetaMathlibExt.arithProgPoly_irreducible` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-irreducible).

## The arithmetic-progression quartic is not a product of two quadratics

Let $a$, $d$ be
coprime integers with $0 < d \le a$. Then the polynomial
$a x^4 + (a + d) x^3 + (a + 2d) x^2 + (a + 3d) x + (a + 4d)$ is not the product of two
polynomials of degree $2$ in $\mathbb{Z}[x]$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Theorem 4.

Stated but not proved: `MetaMathlibExt.arithProgPoly_four_not_mul_quadratics` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-four-not-mul-quadratics).

## Irreducibility when $d$ has a primitive-root prime factor

Let $m \ge 2$ with $m + 1$
prime, and let $a$, $d$ be coprime positive integers. Suppose $d$ has a prime divisor $p$ that is
not divisible by $m + 1$ and whose residue modulo $m + 1$ has multiplicative order $m$ (that is,
$p$ is a primitive root modulo $m + 1$). Then the polynomial
$a x^m + (a + d) x^{m-1} + \cdots + (a + (m - 1)d) x + (a + md)$ is irreducible in
$\mathbb{Z}[x]$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Proposition 6.

Stated but not proved: `MetaMathlibExt.arithProgPoly_irreducible_of_primitiveRoot` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-irreducible-of-primitive).

## The arithmetic-progression polynomial times $(x - 1)^2$

For all natural numbers $m$, $a$,
$d$, the polynomial $A_m(x) = \sum_{i=0}^{m} (a + id) x^{m-i}$ satisfies, in $\mathbb{Z}[x]$,

$$A_m(x)(x - 1)^2 = a x^{m+2} - (a - d) x^{m+1} - (a + (m + 1)d) x + (a + md).$$

The source assumes $m$, $a$, $d$ positive.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Lemma 1.

Stated but not proved: `MetaMathlibExt.arithProgPoly_mul_sub_one_sq` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-mul-sub-one-sq).

## Power identity at the roots of an arithmetic-progression polynomial

Let $m$ and $a$
be natural numbers, let $d$ be a positive integer, and let
$A_m(x) = a x^m + (a + d) x^{m-1} + \cdots + (a + md)$, that is,
$A_m(x) = \sum_{i=0}^{m} (a + id) x^{m-i} \in \mathbb{Z}[x]$. If $z \in \mathbb{C}$ is a root of
$A_m$ or $z = 1$, then

$$z^{m+1} = \frac{(a + (m + 1)d) z - (a + md)}{a z - (a - d)}.$$

With the paper's notation $a_n = a + (n - 1)d$ this reads
$z^{m+1} = (a_{m+2} z - a_{m+1}) / (a_1 z - a_0)$. The denominator does not vanish at such $z$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Lemma 1, equation (2).

Stated but not proved: `MetaMathlibExt.arithProgPoly_root_pow_eq` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-root-pow-eq).

## The auxiliary equation has a unique positive root, which exceeds $1$

Let $m \ge 2$ and
let $a$, $d$ be integers with $0 < d \le a$. Then the equation
$a x^{m+2} + (a - d) x^{m+1} - (a + (m + 1)d) x - (a + md) = 0$ has exactly one positive real
solution, and every positive real solution $x$ satisfies $x > 1$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Proposition 1.

Stated but not proved: `MetaMathlibExt.arithProgPoly_eq3_existsUnique_pos` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-eq3-exists-unique-pos).

## Bound on the zeros of the arithmetic-progression polynomial

Let $m \ge 2$, let $a$, $d$
be integers with $0 < d \le a$, and let $\lambda > 0$ be a real number with
$a \lambda^{m+2} + (a - d) \lambda^{m+1} - (a + (m + 1)d) \lambda - (a + md) = 0$. Then every
complex zero $z$ of $A_m(x) = a x^m + (a + d) x^{m-1} + \cdots + (a + md)$ satisfies
$|z| \le \lambda$, and $|z| = \lambda$ only if $z = -\lambda$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Proposition 2.

Stated but not proved: `MetaMathlibExt.arithProgPoly_root_norm_le` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-root-norm-le).

## Lower bound on a power of the auxiliary root

Let $m \ge 2$, let $a$, $d$ be integers with
$0 < d \le a$, and let $\lambda > 0$ be a real number with
$a \lambda^{m+2} + (a - d) \lambda^{m+1} - (a + (m + 1)d) \lambda - (a + md) = 0$. Then
$a + md < a \lambda^m$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Lemma 2.

Stated but not proved: `MetaMathlibExt.arithProgPoly_lam_pow_gt` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-lam-pow-gt).

## A rational lower bound for $(1 + mx)^{1/m}$

For every natural number $m \ge 2$ and every
real $x > 0$,

$$\frac{2 + (m + 1)x}{2 + (m - 1)x} < (1 + mx)^{1/m}.$$

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Lemma 3.

Stated but not proved: `MetaMathlibExt.one_add_mul_rpow_inv_gt` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#one-add-mul-rpow-inv-gt).

## Strict upper bound on floors at powers of the auxiliary root

Let $m \ge 2$, let $a$, $d$
be natural numbers with $d > 0$ and $(m + 1)d < 2a$, and let $\lambda > 0$ be a real number with
$a \lambda^{m+2} + (a - d) \lambda^{m+1} - (a + (m + 1)d) \lambda - (a + md) = 0$. Then
$\lfloor a \lambda^p \rfloor < a + pd$ for every integer $p$ with $1 \le p \le m - 1$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Proposition 4.

Stated but not proved: `MetaMathlibExt.arithProgPoly_floor_lam_pow_lt` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-floor-lam-pow-lt).

## Exact floor at a power of the auxiliary root (single exponent)

Let $m \ge 2$, let $a$,
$d$ be positive integers, and let $p$ be an integer with $1 \le p \le m - 1$ and
$p(m - p)d^2 < 2a$. If $\lambda > 0$ is a real number with
$a \lambda^{m+2} + (a - d) \lambda^{m+1} - (a + (m + 1)d) \lambda - (a + md) = 0$, then
$\lfloor a \lambda^p \rfloor = a + pd - 1$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Proposition 5.

Stated but not proved: `MetaMathlibExt.arithProgPoly_floor_lam_pow_eq` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-floor-lam-pow-eq).

## Exact floors at powers of the auxiliary root (all exponents)

Let $m \ge 2$, let $a$, $d$
be positive integers with $m^2 d^2 < 8a$, and let $\lambda > 0$ be a real number with
$a \lambda^{m+2} + (a - d) \lambda^{m+1} - (a + (m + 1)d) \lambda - (a + md) = 0$. Then
$\lfloor a \lambda^p \rfloor = a + pd - 1$ for every integer $p$ with $1 \le p \le m - 1$.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Proposition 5, second statement.

Stated but not proved: `MetaMathlibExt.arithProgPoly_floor_lam_pow_eq_of_eight` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-floor-lam-pow-eq-of-eigh).

## Reducible quadratics with coefficients in an arithmetic progression

Let $d \ge 2$ be an
integer and, for a positive integer $a$, let $A_2(x) = ax^2 + (a + d)x + (a + 2d)$ in
$\mathbb{Z}[x]$. There is a positive integer $a$ coprime to $d$ for which $A_2$ is not
irreducible in $\mathbb{Z}[x]$ if and only if every prime divisor of $d$ is congruent to $1$
modulo $3$. In that case the number of positive integers $a$ coprime to $d$ for which $A_2$ is
not irreducible is exactly $2^{n-1}$, where $n$ is the number of distinct prime divisors of $d$.

Both hypotheses matter: without coprimality, $a = d = 7$ gives $A_2(x) = 7(x^2 + 2x + 3)$, which
is not irreducible in $\mathbb{Z}[x]$; and for $d = 1$ the prime condition holds vacuously while
$A_2$ is irreducible for every $a \ge 1$, its discriminant $-3a^2 - 6a + 1$ being negative.

## Sources

- Hiroaki Kakuma, *Irreducibility of Polynomials with Coefficients in a Positive Arithmetic Progression*, INTEGERS 26 (2026), Article A92, Theorem 3.

Stated but not proved: `MetaMathlibExt.arithProgPoly_two_reducible_iff` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/Polynomial/ArithmeticProgressionIrreducibleWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html#arith-prog-poly-two-reducible-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomials with coefficients in arithmetic progression](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/polynomials-with-coefficients-in-arithmetic-prog)
