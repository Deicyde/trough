---
declaration: section
origin: cited
lean: MetaMathlibExt.binomialProduct, MetaMathlibExt.coeff_binomialProduct, MetaMathlibExt.constantCoeff_binomialProduct, MetaMathlibExt.exists_polynomial_quotient_of_extension, MetaMathlibExt.exists_orthogonal_of_orthogonal_over_extension, MetaMathlibExt.binomialProduct_X_pow_mul_inv_pow, MetaMathlibExt.binomialProduct_inv_one_sub, MetaMathlibExt.binomialProduct_rational
statement: formalized
---

# Binomial convolutions of rational power series

15 results, 3 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html).

## Binomial (Hurwitz) product of power series

Let $K$ be a commutative ring. The binomial
product of formal power series $A = \sum_n a_n X^n$ and $B = \sum_n b_n X^n$ in $K[[X]]$ is the
power series $\sum_n c_n X^n$ with $c_n = \sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k}$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, equation (1).

Formalized by `MetaMathlibExt.binomialProduct`, a definition declared in [MathlibExt/RingTheory/PowerSeries/BinomialProduct.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/BinomialProduct.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product).

## Coefficients of the binomial product

Let $K$ be a commutative ring and let
$A = \sum_n a_n X^n$ and $B = \sum_n b_n X^n$ be formal power series over $K$. For every natural
number $n$, the coefficient of $X^n$ in the binomial product of $A$ and $B$ is
$\sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k}$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, equation (1).

Formalized by `MetaMathlibExt.coeff_binomialProduct`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/BinomialProduct.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/BinomialProduct.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#coeff-binomial-product).

## Constant coefficient of the binomial product

Let $K$ be a commutative ring. For formal
power series $A$ and $B$ over $K$, the constant coefficient of the binomial product of $A$ and
$B$ is the product of the constant coefficients of $A$ and $B$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, equation (1).

Formalized by `MetaMathlibExt.constantCoeff_binomialProduct`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/BinomialProduct.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/BinomialProduct.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#constant-coeff-binomial-product).

## Rationality of power series descends from field extensions

Let $F$ be a field, let $G$ be
a field extension of $F$ (a field with an $F$-algebra structure), and let $A$ be a power series
over $F$. If there are polynomials $p$, $q$ over $G$ with $q \ne 0$ and $A q = p$, where $A$ is
viewed as a power series over $G$, then there are polynomials $P$, $Q$ over $F$ with $Q \ne 0$ and
$A Q = P$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Theorem 1 (`jis-2024-24.1.3-thm-1`).

Stated but not proved: `MetaMathlibExt.exists_polynomial_quotient_of_extension` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#exists-polynomial-quotient-of-extension).

## Orthogonal vectors descend from field extensions

Let $F$ be a field, let $G$ be a field
extension of $F$ (a field with an $F$-algebra structure), let $n \in \mathbb{N}$ and let
$S \subseteq F^n$. If some nonzero $t \in G^n$ satisfies $\sum_{i=1}^n s_i t_i = 0$ in $G$ for
every $s \in S$, then some nonzero $u \in F^n$ satisfies $\sum_{i=1}^n s_i u_i = 0$ for every
$s \in S$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Lemma 3 (`jis-2024-24.1.3-lem-3`).

Stated but not proved: `MetaMathlibExt.exists_orthogonal_of_orthogonal_over_extension` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#exists-orthogonal-of-orthogonal-over-ext).

## Binomial product of shifted powers of geometric series

For every field $K$ of
characteristic $0$, all $j, k \in \mathbb{N}$ and all $\alpha, \beta \in K$,

$$\frac{x^j}{(1 - \alpha x)^{j+1}} \odot \frac{x^k}{(1 - \beta x)^{k+1}} =
\binom{j + k}{j} \frac{x^{j+k}}{(1 - (\alpha + \beta) x)^{j+k+1}},$$

where $\odot$ is the binomial product.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Lemma 4 (`jis-2024-24.1.3-lem-4`).

Stated but not proved: `MetaMathlibExt.binomialProduct_X_pow_mul_inv_pow` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product-x-pow-mul-inv-pow).

## Binomial product with a geometric series

For every field $K$ of characteristic $0$, every
power series $A(x)$ over $K$ and every $\beta \in K$,

$$A(x) \odot \frac{1}{1 - \beta x} = \frac{1}{1 - \beta x} A\left(\frac{x}{1 - \beta x}\right),$$

where $\odot$ is the binomial product and $A(x/(1 - \beta x))$ is the substitution of the series
$x/(1 - \beta x)$, which has zero constant term, into $A$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Corollary 5 (`jis-2024-24.1.3-cor-5`).

Stated but not proved: `MetaMathlibExt.binomialProduct_inv_one_sub` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product-inv-one-sub).

## Binomial products of proper rational series

Let $K$ be a field of characteristic $0$, let
$\alpha_1, \dots, \alpha_m, \beta_1, \dots, \beta_n \in K$, not necessarily distinct or nonzero,
and let $R$, $S$ be polynomials over $K$ with $\deg R < m$ and $\deg S < n$. If $A$, $B$ are power
series over $K$ with $A(x) \prod_{i=1}^m (1 - \alpha_i x) = R(x)$ and
$B(x) \prod_{j=1}^n (1 - \beta_j x) = S(x)$, then there is a polynomial $T$ over $K$ with
$\deg T < mn$ such that

$$(A \odot B)(x) \prod_{i=1}^m \prod_{j=1}^n \bigl(1 - (\alpha_i + \beta_j) x\bigr) = T(x),$$

where $\odot$ is the binomial product.

Here $\deg 0 = -\infty$, so $T = 0$ when $mn = 0$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Theorem 6 (`jis-2024-24.1.3-thm-6`).

Stated but not proved: `MetaMathlibExt.binomialProduct_rational` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product-rational).

## Binomial products of arbitrary rational series

Let $K$ be a field of characteristic $0$,
let $\alpha_1, \dots, \alpha_m$ and $\beta_1, \dots, \beta_n$ be nonzero elements of $K$, and let
$R$, $S$ be polynomials over $K$. Let $A$, $B$ be power series over $K$ with
$A(x) \prod_{i=1}^m (1 - \alpha_i x) = R(x)$ and $B(x) \prod_{j=1}^n (1 - \beta_j x) = S(x)$.
Put $u = \max(d_R + 1 - m, 0)$ and $v = \max(d_S + 1 - n, 0)$, where $d_R$ and $d_S$ are the
degrees of $R$ and $S$, the zero polynomial counting as degree $0$. Then there is a polynomial
$T$ over $K$ of degree less than $(u + m)(v + n)$ such that

$$(A \odot B)(x) \Big(\prod_{i=1}^m (1 - \alpha_i x)\Big)^{v}
\Big(\prod_{j=1}^n (1 - \beta_j x)\Big)^{u} \prod_{i=1}^m \prod_{j=1}^n (1 - (\alpha_i + \beta_j) x)
= T(x),$$

where $\odot$ is the binomial product.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Corollary 7 (`jis-2024-24.1.3-cor-7`).

Stated but not proved: `MetaMathlibExt.binomialProduct_rational_general` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product-rational-general).

## Binomial product with a monomial

For every field $K$ of characteristic $0$, every
$m \in \mathbb{N}$ and every power series $A(x)$ over $K$,

$$x^m \odot A(x) = \frac{x^m}{m!} \frac{d^m}{dx^m}\bigl(x^m A(x)\bigr),$$

where $\odot$ is the binomial product and $d/dx$ is the formal derivative.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Lemma 8 (`jis-2024-24.1.3-lem-8`).

Stated but not proved: `MetaMathlibExt.binomialProduct_X_pow` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product-x-pow).

## Resultant identity for pairwise sums

Let $K$ be a field of characteristic $0$, let
$m, n \ge 0$ be integers, and let $\alpha_1, \dots, \alpha_m$ and $\beta_1, \dots, \beta_n$ be
elements of $K$. Regard $f(y) = \prod_{i=1}^{m} (1 - y - \alpha_i x)$ and
$g(y) = \prod_{j=1}^{n} (y - \beta_j x)$ as polynomials in $y$ with coefficients in $K[x]$,
and let $\operatorname{Res}_{m,n}(f, g)$ be the determinant of their Sylvester matrix formed with
the formal degrees $m$ and $n$. Then in $K[x]$

$$
\prod_{i=1}^{m} \prod_{j=1}^{n} \bigl(1 - (\alpha_i + \beta_j)x\bigr)
= (-1)^{mn} \operatorname{Res}_{m,n}(f, g).
$$

With $U(x) = \prod_{i=1}^{m} (1 - \alpha_i x)$ and $V(x) = \prod_{j=1}^{n} (1 - \beta_j x)$, these
are $f(y) = (1 - y)^m U(x / (1 - y))$ and $g(y) = y^n V(x / y)$, the form used in the source.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Theorem 10 (`jis-2024-24.1.3-thm-10`).

Stated but not proved: `MetaMathlibExt.prod_one_sub_add_eq_resultant` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#prod-one-sub-add-eq-resultant).

## Binomial square of the Lucas generating function

Let $K$ be a field of characteristic
$0$, let $a, b \in K$, and let $g(x) = \sum_{n \ge 0} G_n x^n$ be a power series over $K$ with
$g(x)(1 - ax - bx^2) = 2 - ax$. Then

$$g \odot g = \frac{2}{1 - ax} + g(2x),$$

where $\odot$ is the binomial product, and
$\sum_{k=0}^{n} \binom{n}{k} G_k G_{n-k} = 2a^n + 2^n G_n$ for every $n \ge 0$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Theorem 11 (`jis-2024-24.1.3-thm-11`).

Stated but not proved: `MetaMathlibExt.binomialProduct_lucasV_generatingFunction` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product-lucas-v-generating-func).

## Binomial products of series with a cubic denominator

Let $K$ be a field of characteristic
$0$, let $A, B, C \in K$ with $C \ne 0$, and let $D(x) = 1 + Ax + Bx^2 + Cx^3$. Suppose that
$D(x) = \prod_{i=1}^{3} (1 - \alpha_i x)$ with $\alpha_1, \alpha_2, \alpha_3 \in K$ and that
$2\alpha_i \ne \alpha_j + \alpha_k$ whenever $i, j, k \in \{1, 2, 3\}$ are not all equal. Let $r$
and $s$ be power series over $K$ such that $r D$ and $s D$ are polynomials of degree less than $3$.
Then there are polynomials $u$, $v$ over $K$ of degree at most $2$ such that

$$r \odot s = \frac{u(x)}{D(2x)} + \frac{1}{1 + Ax} \odot \frac{v(x)}{D(-x)},$$

where $\odot$ is the binomial product.

The second term uses the factor $1/(1 + Ax)$; with $1/(1 - Ax)$ in its place the statement already
fails for the tribonacci series $x/(1 - x - x^2 - x^3)$, where $A = -1$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Theorem 12 (`jis-2024-24.1.3-thm-12`).

Stated but not proved: `MetaMathlibExt.binomialProduct_cubic_denominator` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#binomial-product-cubic-denominator).

## Hadamard products of rational series

Let $K$ be a field of characteristic $0$, let
$\alpha_1, \dots, \alpha_m, \beta_1, \dots, \beta_n \in K$, and let $A = \sum_k a_k x^k$ and
$B = \sum_k b_k x^k$ be power series over $K$ such that $A(x) \prod_{i=1}^m (1 - \alpha_i x)$ and
$B(x) \prod_{j=1}^n (1 - \beta_j x)$ are polynomials. Then their Hadamard product
$A * B = \sum_k a_k b_k x^k$ has the property that
$(A * B)(x) \prod_{i=1}^m \prod_{j=1}^n (1 - \alpha_i \beta_j x)$ is a polynomial. Moreover, call a
power series $f$ over $K$ proper if $f Q = P$ for some polynomials $P$, $Q$ over $K$ with
$Q(0) \ne 0$ and $\deg P < \deg Q$. If $A$ and $B$ are proper, then so is $A * B$.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Theorem 13 (`jis-2024-24.1.3-thm-13`).

Stated but not proved: `MetaMathlibExt.hadamardProduct_rational` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#hadamard-product-rational).

## Resultant identity for pairwise products

Let $K$ be a field of characteristic $0$, let
$m, n \ge 0$ be integers, and let $\alpha_1, \dots, \alpha_m$ and $\beta_1, \dots, \beta_n$ be
elements of $K$. Regard $f(y) = \prod_{i=1}^{m} (1 - \alpha_i y)$ and
$g(y) = \prod_{j=1}^{n} (y - \beta_j x)$ as polynomials in $y$ with coefficients in $K[x]$,
and let $\operatorname{Res}_{m,n}(f, g)$ be the determinant of their Sylvester matrix formed with
the formal degrees $m$ and $n$. Then in $K[x]$

$$
\prod_{i=1}^{m} \prod_{j=1}^{n} (1 - \alpha_i \beta_j x) = (-1)^{mn} \operatorname{Res}_{m,n}(f, g).
$$

With $U(x) = \prod_{i=1}^{m} (1 - \alpha_i x)$ and $V(x) = \prod_{j=1}^{n} (1 - \beta_j x)$, these
are $f(y) = U(y)$ and $g(y) = y^n V(x / y)$, the form used in the source.

## Sources

- Ira M. Gessel and Ishan Kar, *Binomial Convolutions for Rational Power Series*, Journal of Integer Sequences 27 (2024), Article 24.1.3, Theorem 14 (`jis-2024-24.1.3-thm-14`).

Stated but not proved: `MetaMathlibExt.prod_one_sub_mul_eq_resultant` is written with `theorem_wanted` in [WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/PowerSeries/BinomialConvolutionRationalWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html#prod-one-sub-mul-eq-resultant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial convolutions of rational power series](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/binomial-convolutions-of-rational-power-series)
