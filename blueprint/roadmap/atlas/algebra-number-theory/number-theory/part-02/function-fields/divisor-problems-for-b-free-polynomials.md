---
declaration: section
origin: cited
lean: MetaMathlibExt.monicDirichletConv, MetaMathlibExt.monicDirichletConv_one, MetaMathlibExt.monic_perron_formula, MetaMathlibExt.monicDirichletConv_mul_of_completelyMultiplicative, MetaMathlibExt.monic_sum_moebius_div_norm, MetaMathlibExt.monic_sum_moebius_mul_natDegree_div_norm, MetaMathlibExt.monic_count_natDegree_le, MetaMathlibExt.monic_sum_divisorCount_natDegree_le
statement: formalized
---

# Divisor problems for B-free polynomials

53 results, 28 proved and 25 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html).

## Dirichlet convolution over monic divisors

Let $F$ be a field. The Dirichlet convolution
of functions $\alpha$ and $\beta$ from $F[T]$ to $\mathbb{C}$ is the function $\alpha * \beta$
given at $f \in F[T]$ by

$$(\alpha * \beta)(f) = \sum_{g \text{ monic},\ g \mid f} \alpha(g)\, \beta(f/g),$$

the sum running over the monic divisors $g$ of $f$.

When $f = 0$ every monic polynomial divides $f$; the sum is then the sum of its nonzero terms if
there are finitely many, and $0$ otherwise.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of the Dirichlet convolution.

Formalized by `MetaMathlibExt.monicDirichletConv`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-dirichlet-conv).

## Dirichlet convolution at $1$

Let $F$ be a field and let $\alpha$ and $\beta$ be functions
from $F[T]$ to $\mathbb{C}$. Their Dirichlet convolution over monic divisors satisfies
$(\alpha * \beta)(1) = \alpha(1) \beta(1)$, since the only monic divisor of $1$ is $1$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of the Dirichlet convolution.

Formalized by `MetaMathlibExt.monicDirichletConv_one`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-dirichlet-conv-one).

## Perron's formula for monic polynomials over a finite field

Let $F$ be a finite field, let
$a$ be a complex-valued function on $F[T]$, and let $\rho$ be a real number with $0 < \rho < 1$ such
that the series $\sum_f |a(f)| \rho^{\deg f}$ over all monic $f \in F[T]$ converges. Put
$A(u) = \sum_f a(f) u^{\deg f}$, the sum again over all monic $f$. Then for every natural number
$n$, with the circle $|u| = \rho$ traversed counterclockwise,

$$\sum_{f \text{ monic},\ \deg f \le n} a(f) = \frac{1}{2 \pi i} \oint_{|u| = \rho}
\frac{A(u)}{u^n (1 - u)} \, \frac{du}{u}.$$

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 1 (Perron's Formula).

Stated but not proved: `MetaMathlibExt.monic_perron_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-perron-formula).

## Dirichlet convolution of completely multiplicative functions at a product

Let $F$ be a
field and let $\alpha, \beta : F[T] \to \mathbb{C}$ be completely multiplicative, that is,
monoid homomorphisms from the multiplicative monoid of $F[T]$ to $\mathbb{C}$. Write
$\gamma = \alpha * \beta$ for their Dirichlet convolution over monic divisors and $\mu$ for the
Möbius function. Then for all monic $f, g \in F[T]$,

$$\gamma(fg) = \sum_{\ell} \mu(\ell) \alpha(\ell) \beta(\ell) \gamma(f/\ell) \gamma(g/\ell),$$

where $\ell$ runs over the monic common divisors of $f$ and $g$.

Every completely multiplicative function on monic polynomials extends to such a homomorphism (send
nonzero constants to $1$ and $0$ to $0$), and only values at monic polynomials enter.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 2.

Stated but not proved: `MetaMathlibExt.monicDirichletConv_mul_of_completelyMultiplicative` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-dirichlet-conv-mul-of-completely-m).

## Möbius sum over the monic divisors of a polynomial over a finite field

Let $F$ be a finite
field with $q$ elements and let $\mu$ be the Möbius function of $F[T]$. For every monic
$f \in F[T]$,

$$\sum_{g \text{ monic},\ g \mid f} \frac{\mu(g)}{q^{\deg g}} =
\prod_{P \text{ monic irreducible},\ P \mid f} \left(1 - \frac{1}{q^{\deg P}}\right).$$

The right side is $\Phi(f) / q^{\deg f}$, where $\Phi$ is Euler's totient function on $F[T]$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 6; `Φ` as defined after Theorem 3.

Stated but not proved: `MetaMathlibExt.monic_sum_moebius_div_norm` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-sum-moebius-div-norm).

## Degree-weighted Möbius sum over the monic divisors of a polynomial over a finite field

Let
$F$ be a finite field with $q$ elements and let $\mu$ be the Möbius function of $F[T]$. For every
monic $f \in F[T]$,

$$\sum_{g \text{ monic},\ g \mid f} \frac{\mu(g) \deg g}{q^{\deg g}} =
\prod_{P \mid f} \left(1 - \frac{1}{q^{\deg P}}\right)
\sum_{P \mid f} \frac{\deg P}{1 - q^{\deg P}},$$

where in the product and in the sum $P$ runs over the monic irreducible divisors of $f$.

The product is $\Phi(f) / q^{\deg f}$, where $\Phi$ is Euler's totient function on $F[T]$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 7; `Φ` as defined after Theorem 3.

Stated but not proved: `MetaMathlibExt.monic_sum_moebius_mul_natDegree_div_norm` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-sum-moebius-mul-nat-degree-div-nor).

## Number of monic polynomials of bounded degree

Let $F$ be a finite field with $q$
elements and let $N$ be a natural number. The number of monic polynomials in $F[T]$ of degree at
most $N$ is $(q^{N+1} - 1)/(q - 1)$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Proposition 4, case `h = 1`, `m = 1`.

Stated but not proved: `MetaMathlibExt.monic_count_natDegree_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-count-nat-degree-le).

## Summatory divisor function for monic polynomials over a finite field

Let $F$ be a finite
field with $q$ elements. For monic $f \in F[T]$, the Dirichlet convolution $(1 * 1)(f)$ of the
constant function $1$ with itself is the number of monic divisors of $f$. Then for every natural
number $N$,

$$\sum_{f \text{ monic},\ \deg f \le N} (1 * 1)(f) =
\frac{(N + 1) q^{N + 2} - (N + 2) q^{N + 1} + 1}{(q - 1)^2}.$$

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Proposition 4, case `h = 2`, `m = 1`.

Stated but not proved: `MetaMathlibExt.monic_sum_divisorCount_natDegree_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-sum-divisor-count-nat-degree-le).

## Norm of a polynomial over a finite field

Let $F$ be a finite field with $q$ elements. The
norm of a nonzero $f \in F[T]$ is the real number $|f| = q^{\deg f}$, and $|0| = 0$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of the norm.

Formalized by `MetaMathlibExt.fqNorm`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#fq-norm).

## The norm of a nonzero polynomial

Let $F$ be a finite field with $q$ elements. For every
nonzero $f \in F[T]$, the norm of $f$ is $|f| = q^{\deg f}$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of the norm.

Formalized by `MetaMathlibExt.fqNorm_of_ne_zero`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#fq-norm-of-ne-zero).

## Multiplicativity of the norm

Let $F$ be a finite field with $q$ elements, and let
$|f| = q^{\deg f}$ be the norm of a nonzero $f \in F[T]$. For all nonzero $f, g \in F[T]$,
$|fg| = |f| \, |g|$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of the norm.

Formalized by `MetaMathlibExt.fqNorm_mul`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#fq-norm-mul).

## Monic polynomials of degree zero

Let $F$ be a field. A polynomial $f \in F[T]$ is monic
of degree at most $0$ if and only if $f = 1$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 2, the set `M_{≤ 0}`.

Formalized by `MetaMathlibExt.monic_natDegree_le_zero_iff`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-nat-degree-le-zero-iff).

## $B_\kappa$-free polynomials

Let $F$ be a field and let $\kappa$ assign a natural number to
each polynomial in $F[T]$. A polynomial $f \in F[T]$ is $B_\kappa$-free when $P^{\kappa(P)}$ does
not divide $f$ for any monic irreducible $P \in F[T]$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `B_κ`-free polynomials.

Formalized by `MetaMathlibExt.IsBFree`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#is-bfree).

## The polynomial $1$ is $B_\kappa$-free

Let $F$ be a field and let $\kappa$ assign to each
polynomial in $F[T]$ a natural number, with $\kappa(P) \ne 0$ for every monic irreducible $P$.
Then $1$ is $B_\kappa$-free: $P^{\kappa(P)}$ does not divide $1$ for any monic irreducible $P$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `B_κ`-free polynomials.

Formalized by `MetaMathlibExt.isBFree_one`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#is-bfree-one).

## The minimal exponent $\kappa_{\min}$

Let $F$ be a field and let $\kappa$ be a function
from $F[T]$ to the natural numbers. Then $\kappa_{\min}$ is the minimum of $\kappa(P)$ over all
monic irreducible polynomials $P \in F[T]$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `κ_min`.

Formalized by `MetaMathlibExt.kappaMin`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#kappa-min).

## $\kappa_{\min}$ is a lower bound for $\kappa$

Let $F$ be a field, let $\kappa$ assign a
natural number to each polynomial in $F[T]$, and let $\kappa_{\min}$ be the minimum of $\kappa(P)$
over the monic irreducible $P \in F[T]$. Then $\kappa_{\min} \le \kappa(P)$ for every monic
irreducible $P \in F[T]$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `κ_min`.

Formalized by `MetaMathlibExt.kappaMin_le`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#kappa-min-le).

## The $\kappa$-power of a polynomial

Let $F$ be a field and let $\kappa$ be a function
from $F[T]$ to the natural numbers. For nonzero $f \in F[T]$ and a monic irreducible $P$, write
$\nu_P(f)$ for the multiplicity of $P$ in $f$. The $\kappa$-power of $f$ is
$f^\kappa = \prod_P P^{\nu_P(f)\, \kappa(P)}$, the product over the monic irreducible $P$ dividing
$f$; it does not depend on the leading coefficient of $f$. For $f = 0$ the product is empty and
$0^\kappa = 1$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `f ^ κ`.

Formalized by `MetaMathlibExt.kappaPow`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#kappa-pow).

## The $\kappa$-power of $1$

Let $F$ be a field and let $\kappa$ be a function from $F[T]$
to the natural numbers. Then the $\kappa$-power of the constant polynomial $1$ is $1^\kappa = 1$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `f ^ κ`.

Formalized by `MetaMathlibExt.kappaPow_one`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#kappa-pow-one).

## The $\kappa$-power of a monic irreducible polynomial

Let $F$ be a field and let $\kappa$
be a function from $F[T]$ to the natural numbers. For every monic irreducible $P \in F[T]$, the
$\kappa$-power of $P$ is $P^\kappa = P^{\kappa(P)}$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `f ^ κ`.

Formalized by `MetaMathlibExt.kappaPow_of_irreducible`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#kappa-pow-of-irreducible).

## The $h$-fold divisor function

Let $F$ be a field and $h$ a natural number. For
$f \in F[T]$, $d_h(f)$ is the number of $h$-tuples $(g_1, \dots, g_h)$ of monic polynomials in
$F[T]$ with $g_1 \cdots g_h = f$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `d_h`.

Formalized by `MetaMathlibExt.monicDivisorCount`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-divisor-count).

## The divisor functions at $1$

Let $F$ be a field and $h$ a natural number. Then
$d_h(1) = 1$, where $d_h(f)$ is the number of $h$-tuples of monic polynomials in $F[T]$ whose
product is $f$: the only such tuple for $f = 1$ has every entry equal to $1$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `d_h`.

Formalized by `MetaMathlibExt.monicDivisorCount_one`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-divisor-count-one).

## The divisor function $d_0$ vanishes away from $1$

Let $F$ be a field and let $f \in F[T]$
with $f \ne 1$. Then $d_0(f) = 0$, where $d_h(f)$ is the number of $h$-tuples of monic
polynomials in $F[T]$ whose product is $f$: the only $0$-tuple is the empty one, whose product
is $1$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `d_h`.

Formalized by `MetaMathlibExt.monicDivisorCount_zero_of_ne_one`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-divisor-count-zero-of-ne-one).

## The divisor function $d_1$ on monic polynomials

Let $F$ be a field. For every monic
$f \in F[T]$, $d_1(f) = 1$, where $d_h(f)$ is the number of $h$-tuples of monic polynomials in
$F[T]$ whose product is $f$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `d_h`.

Formalized by `MetaMathlibExt.monicDivisorCount_one_left`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-divisor-count-one-left).

## Shifted partial sums of a Dirichlet convolution

Let $F$ be a field, let
$\alpha, \beta \colon F[T] \to \mathbb{C}$, let $\alpha * \beta$ be their Dirichlet convolution
over monic divisors, let $f \in F[T]$ and let $n$ be a natural number. Then
$S_f[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n) = \sum_g (\alpha * \beta)(fg)$, the sum over the monic $g \in F[T]$ with
$\deg f + \deg g \le n$, where $\deg 0 = 0$. This is the paper's sum over $g$ of degree at most
$n - \deg f$.

The sum is a finitary sum: it is $0$ when infinitely many of its terms are nonzero, which can
happen only for infinite $F$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, eq. (3).

Formalized by `MetaMathlibExt.monicConvShiftedSum`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-conv-shifted-sum).

## Shifted partial sums vanish below $\deg f$

Let $F$ be a field, let
$\alpha, \beta \colon F[T] \to \mathbb{C}$ and let $f \in F[T]$. For every natural number
$n < \deg f$, the shifted partial sum of the Dirichlet convolution satisfies
$S_f[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n) = 0$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, eq. (3).

Formalized by `MetaMathlibExt.monicConvShiftedSum_of_lt`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-conv-shifted-sum-of-lt).

## Partial sums of a Dirichlet convolution over monic polynomials

Let $F$ be a field, let
$\alpha, \beta \colon F[T] \to \mathbb{C}$, and let $\alpha * \beta$ be their Dirichlet
convolution over monic divisors. For an integer $n$,
$D[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n) = \sum_g (\alpha * \beta)(g)$, the sum over the monic $g \in F[T]$ of degree
at most $n$. For $n < 0$ the sum is empty, so $D[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n) = 0$; this is how the paper's
Lemma 3 uses $D$ at $n - \deg(f \ell)$.

The sum is a finitary sum: it is $0$ when infinitely many of its terms are nonzero, which can
happen only for infinite $F$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `D[α, β](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n)`.

Formalized by `MetaMathlibExt.monicConvPartialSum`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-conv-partial-sum).

## $D(\alpha, \beta)$ vanishes at negative arguments

Let $F$ be a field and let
$\alpha, \beta \colon F[T] \to \mathbb{C}$. For every integer $n < 0$, the partial sum of the
Dirichlet convolution of $\alpha$ and $\beta$ satisfies $D[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n) = 0$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `D[α, β](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n)`.

Formalized by `MetaMathlibExt.monicConvPartialSum_of_neg`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-conv-partial-sum-of-neg).

## The partial sum $D(\alpha, \beta)(0)$

Let $F$ be a field and let
$\alpha, \beta \colon F[T] \to \mathbb{C}$. The partial sum of the Dirichlet convolution of
$\alpha$ and $\beta$ at $0$ is $D[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/0) = \alpha(1)\, \beta(1)$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `D[α, β](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n)`.

Formalized by `MetaMathlibExt.monicConvPartialSum_zero`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-conv-partial-sum-zero).

## Weighted convolution sum

Let $F$ be a field, let $\gamma, \alpha, \beta$ be functions from
$F[T]$ to $\mathbb{C}$, and write $\alpha * \beta$ for the monic Dirichlet convolution of $\alpha$
and $\beta$. For a natural number $n$, let $M_{\le n}$ be the set of monic polynomials in $F[T]$ of
degree at most $n$. The weighted convolution sum is

$$D(\gamma, \alpha, \beta; n) = \sum_{f \in M_{\le n}} \gamma(f)\,(\alpha * \beta)(f).$$

When $F$ is infinite and this sum has infinitely many nonzero terms, its value is taken to be $0$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `D[γ, α, β](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n)`.

Formalized by `MetaMathlibExt.weightedMonicConvSum`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#weighted-monic-conv-sum).

## The weighted convolution sum at degree zero

Let $F$ be a field and let
$\gamma, \alpha, \beta$ be functions from $F[T]$ to $\mathbb{C}$, and write $\alpha * \beta$ for
the monic Dirichlet convolution. The weighted convolution sum $D(\gamma, \alpha, \beta; 0)$, the
sum of $\gamma(f)\,(\alpha * \beta)(f)$ over the monic $f \in F[T]$ of degree at most $0$, equals
$\gamma(1)\,\alpha(1)\,\beta(1)$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 3, definition of `D[γ, α, β](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n)`.

Formalized by `MetaMathlibExt.weightedMonicConvSum_zero`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#weighted-monic-conv-sum-zero).

## Shifted partial sums for completely multiplicative functions

Let $F$ be a finite field
and let $\alpha, \beta \colon F[T] \to \mathbb{C}$ be completely multiplicative, that is, monoid
homomorphisms from the multiplicative monoid of $F[T]$ to $\mathbb{C}$. Write $\mu$ for the Möbius
function of $F[T]$. For $f \in F[T]$, a natural number $n$ and an integer $k$, write
$S_f[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n)$ and $D[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/k)$ for the shifted partial sums and the partial
sums of the Dirichlet convolution of $\alpha$ and $\beta$ over monic divisors, where
$D[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/k) = 0$ for $k < 0$. Then for every monic $f \in F[T]$ and every natural number
$n$,

$$S_f[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n) = \sum_{d \mid f} \alpha(d)\, \beta(f/d) \sum_{\ell \mid d} \mu(\ell)\,
\beta(\ell)\, D[\alpha, \beta](n - \deg(f \ell)),$$

where $d$ runs over the monic divisors of $f$, $\ell$ over the monic divisors of $d$, and
$n - \deg(f \ell)$ is computed in the integers.

The paper states this for every $f \in F[T]$, monic or not; its proof applies Lemma 2, which needs
$f$ monic.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 3.

Stated but not proved: `MetaMathlibExt.monicConvShiftedSum_eq_of_completelyMultiplicative` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-conv-shifted-sum-eq-of-completely).

## Weighted convolution sums as sums of shifted sums

Let $F$ be a finite field and let
$\gamma, \alpha, \beta$ be functions from $F[T]$ to $\mathbb{C}$. Write $\alpha * \beta$ for the
monic Dirichlet convolution, $\mu$ for the Möbius function of $F[T]$, and $\lambda = \gamma * \mu$.
For a natural number $n$ let $M_{\le n}$ be the set of monic polynomials in $F[T]$ of degree at
most $n$, let $D(\gamma, \alpha, \beta; n) = \sum_{f \in M_{\le n}} \gamma(f)\,(\alpha * \beta)(f)$
and, for monic $f$, let
$S_f(\alpha, \beta; n) = \sum_{g \text{ monic},\ \deg f + \deg g \le n} (\alpha * \beta)(fg)$.
Then

$$D(\gamma, \alpha, \beta; n) = \sum_{f \in M_{\le n}} \lambda(f)\, S_f(\alpha, \beta; n).$$

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 4.

Stated but not proved: `MetaMathlibExt.weightedMonicConvSum_eq_sum_shifted` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#weighted-monic-conv-sum-eq-sum-shifted).

## Camargo's identity over $F(T)$

Let $F$ be a finite field and let $\mu$ be the Möbius
function of $F[T]$. For functions $\alpha, \beta \colon F[T] \to \mathbb{C}$ let
$(\alpha * \beta)(f) = \sum_{g \mid f} \alpha(g) \beta(f/g)$, over monic divisors $g$, be their
Dirichlet convolution, and let $D[\alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/k)$ be the sum of $(\alpha * \beta)(g)$ over the
monic $g$ of degree at most $k$, which is $0$ for $k < 0$. For a further function $\gamma$ let
$D[\gamma, \alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n)$ be the sum of $\gamma(f) (\alpha * \beta)(f)$ over the monic $f$ of
degree at most $n$. Suppose $\alpha$ and $\beta$ are completely multiplicative, that is,
$\alpha(1) = 1$ and $\alpha(f g) = \alpha(f) \alpha(g)$ for all $f, g \in F[T]$, and likewise for
$\beta$, and let $\gamma \colon F[T] \to \mathbb{C}$ be arbitrary. Then for every natural number
$n$,

$$D[\gamma, \alpha, \beta](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/n) = \sum_{f \text{ monic},\ \deg f \le n} (\gamma * \mu)(f)
\sum_{d \mid f} \alpha(d) \beta(f/d) \sum_{\ell \mid d} \mu(\ell) \beta(\ell) \,
D[\alpha, \beta](n - \deg(f \ell)),$$

where $d$ runs over the monic divisors of $f$ and $\ell$ over the monic divisors of $d$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 6.

Stated but not proved: `MetaMathlibExt.weightedMonicConvSum_eq_of_completelyMultiplicative` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#weighted-monic-conv-sum-eq-of-completely).

## Convolution of the $B_\kappa$-free indicator with the Möbius function

Let $F$ be a field
and let $\kappa$ assign a natural number to each polynomial in $F[T]$, with $\kappa(P) \ne 0$ for
every monic irreducible $P \in F[T]$. Let $\mathbf{1}_{B_\kappa} \colon F[T] \to \mathbb{C}$ be
the indicator function of the $B_\kappa$-free polynomials, let $\mu$ be the Möbius function of
$F[T]$, and write $r^\kappa$ for the $\kappa$-power of a polynomial $r$. Then for every monic
$f \in F[T]$, the Dirichlet convolution of $\mathbf{1}_{B_\kappa}$ and $\mu$ over monic divisors
satisfies

$$(\mathbf{1}_{B_\kappa} * \mu)(f) = \sum_{r} \mu(r),$$

the sum running over the monic $r \in F[T]$ with $r^\kappa = f$.

There is at most one such $r$, so the right side is $\mu(r)$ if $f = r^\kappa$ for a monic $r$,
and $0$ if there is no such $r$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 5.

Stated but not proved: `MetaMathlibExt.monicDirichletConv_bFreeIndicator_moebius` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#monic-dirichlet-conv-b-free-indicator-mo).

## Bound on the Möbius sum over κ-th powers

Let $F$ be a finite field with $q$ elements and
let $\kappa$ assign a natural number to each polynomial in $F[T]$, with $\kappa(P) \ge 2$ for
every monic irreducible $P$. Let $\kappa_{\min}$ be the minimum of $\kappa(P)$ over the monic
irreducible $P$, and for monic $r = \prod_P P^{\nu_P}$ write
$r^\kappa = \prod_P P^{\nu_P \kappa(P)}$. Then for every natural number $N \ge 1$,

$$
\Bigl|\sum_{r} \mu(r) \sum_{f \mid r^\kappa} \sum_{\ell \mid f} \mu(\ell)\Bigr| \le
q^{N/\kappa_{\min}},
$$

where $r$ runs over the monic polynomials with $\deg r^\kappa \le N$, $f$ and $\ell$ run over monic
divisors, $\mu$ is the Möbius function, and the exponent $N/\kappa_{\min}$ is a real number.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 8, eq. (6).

Stated but not proved: `MetaMathlibExt.abs_sum_moebius_kappaPow_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#abs-sum-moebius-kappa-pow-le).

## Divisor-count bound over $\kappa$-th powers of monic polynomials

Let $F$ be a finite
field with $q$ elements and let $\kappa$ assign a natural number to each polynomial in $F[T]$,
with $\kappa(P) \ge 2$ for every monic irreducible $P$. For monic $r = \prod_P P^{\nu_P}$ write
$r^\kappa = \prod_P P^{\nu_P \kappa(P)}$, and let $\kappa_{\min}$ be the minimum of $\kappa(P)$
over the monic irreducible $P$. Then for every $\varepsilon > 0$, as $N \to \infty$,

$$\sum_{r \text{ monic},\ \deg r^\kappa \le N} \ \sum_{f \mid r^\kappa} \ \sum_{\ell \mid f} 1 =
O\left(q^{(1/\kappa_{\min} + \varepsilon) N}\right),$$

where $f$ runs over the monic divisors of $r^\kappa$ and $\ell$ over the monic divisors of $f$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Lemma 8, eq. (7).

Stated but not proved: `MetaMathlibExt.sum_divisors_kappaPow_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#sum-divisors-kappa-pow-is-big-o).

## Euler-product asymptotic with the $(h-1)$-divisor function over $\kappa$-th powers

Let
$F$ be a finite field with $q$ elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let
$\mu$ be the Möbius function of $F[T]$. Let $\kappa$ assign a natural number to each polynomial in
$F[T]$, with $\kappa(P) \ge 2$ for every monic irreducible $P$. For monic $r = \prod_P P^{\nu_P}$
write $r^\kappa = \prod_P P^{\nu_P \kappa(P)}$, and let $\kappa_{\min}$ be the minimum of
$\kappa(P)$ over the monic irreducible $P$. Let $m \in F[T]$ be monic, let $h \ge 1$, let
$d_{h-1}$ be the $(h-1)$-divisor function, and put $C_P = \binom{h + \kappa(P) - 1}{\kappa(P)}$.
Then for every $\varepsilon > 0$, as $N \to \infty$,

$$\sum_{\substack{r \text{ monic},\ \deg r^\kappa \le N \\ \gcd(r, m) = 1}}
\frac{\mu(r)}{|r^\kappa|} \sum_{f \mid r^\kappa} d_{h-1}(f) \sum_{g \mid f} \frac{\mu(g)}{|g|} =
\prod_{P \nmid m} \left(1 - \frac{1}{|P|^{\kappa(P)}}
\left(C_P + \frac{1}{|P|} (1 - C_P)\right)\right) +
O\left(q^{(1/\kappa_{\min} + \varepsilon - 1)(N + 1)}\right),$$

where $f$ runs over the monic divisors of $r^\kappa$, $g$ over the monic divisors of $f$, and $P$
over the monic irreducible polynomials not dividing $m$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Proposition 1.

Stated but not proved: `MetaMathlibExt.sum_moebius_kappaPow_divisorCount_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#sum-moebius-kappa-pow-divisor-count-is-b).

## Euler-product asymptotic for a degree-weighted Möbius sum over $\kappa$-th powers

Let
$F$ be a finite field with $q$ elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let
$\mu$ be the Möbius function of $F[T]$. Let $\kappa$ assign a natural number to each polynomial in
$F[T]$, with $\kappa(P) \ge 2$ for every monic irreducible $P$. For monic $r = \prod_P P^{\nu_P}$
write $r^\kappa = \prod_P P^{\nu_P \kappa(P)}$, and let $\kappa_{\min}$ be the minimum of
$\kappa(P)$ over the monic irreducible $P$. Let $m \in F[T]$ be monic. Then for every
$\varepsilon > 0$, as $N \to \infty$,

$$\sum_{\substack{r \text{ monic},\ \deg r^\kappa \le N \\ \gcd(r, m) = 1}}
\frac{\mu(r)}{|r^\kappa|} \sum_{f \mid r^\kappa} \sum_{g \mid f} \frac{\mu(g) \deg g}{|g|} =
\prod_{P \nmid m} \left(1 - \frac{\kappa(P) + 1}{|P|^{\kappa(P)}} +
\frac{\kappa(P)}{|P|^{\kappa(P) + 1}}\right)
\sum_{P \nmid m} \frac{\kappa(P) \deg P}{|P|^{\kappa(P) + 1} - |P| (\kappa(P) + 1) + \kappa(P)} +
O\left(q^{(1/\kappa_{\min} + \varepsilon - 1)(N + 1)}\right),$$

where $f$ runs over the monic divisors of $r^\kappa$, $g$ over the monic divisors of $f$, and $P$
in the product and in the sum over the monic irreducible polynomials not dividing $m$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Proposition 2.

Stated but not proved: `MetaMathlibExt.sum_moebius_kappaPow_moebius_natDegree_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#sum-moebius-kappa-pow-moebius-nat-degree).

## Euler-product asymptotic for a Möbius sum weighted by $\deg r^\kappa$

Let $F$ be a finite
field with $q$ elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let $\mu$ be the
Möbius function of $F[T]$. Let $\kappa$ assign a natural number to each polynomial in $F[T]$, with
$\kappa(P) \ge 2$ for every monic irreducible $P$. For monic $r = \prod_P P^{\nu_P}$ write
$r^\kappa = \prod_P P^{\nu_P \kappa(P)}$, and let $\kappa_{\min}$ be the minimum of $\kappa(P)$
over the monic irreducible $P$. Let $m \in F[T]$ be monic. Then for every $\varepsilon > 0$, as
$N \to \infty$,

$$\sum_{\substack{r \text{ monic},\ \deg r^\kappa \le N \\ \gcd(r, m) = 1}}
\frac{\mu(r) \deg r^\kappa}{|r^\kappa|} \sum_{f \mid r^\kappa} \sum_{g \mid f} \frac{\mu(g)}{|g|}
= -\prod_{P \nmid m} \left(1 - \frac{\kappa(P) + 1}{|P|^{\kappa(P)}} +
\frac{\kappa(P)}{|P|^{\kappa(P) + 1}}\right)
\sum_{P \nmid m} \frac{\kappa(P) \deg P \, (|P| (\kappa(P) + 1) - \kappa(P))}
{|P|^{\kappa(P) + 1} - |P| (\kappa(P) + 1) + \kappa(P)} +
O\left(q^{(1/\kappa_{\min} + \varepsilon - 1)(N + 1)}\right),$$

where $f$ runs over the monic divisors of $r^\kappa$, $g$ over the monic divisors of $f$, and $P$
in the product and in the sum over the monic irreducible polynomials not dividing $m$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Proposition 3.

Stated but not proved: `MetaMathlibExt.sum_moebius_natDegree_kappaPow_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#sum-moebius-nat-degree-kappa-pow-is-big).

## Character sums of the $h$-divisor function over monic polynomials

Let $F$ be a finite
field with $q$ elements, let $m \in F[T]$ be monic, and let $\chi$ be a non-principal Dirichlet
character modulo $m$: a multiplicative character of $F[T]/(m)$, vanishing off the units, other
than the principal one, evaluated at $f \in F[T]$ through the class of $f$ modulo $m$. Let
$h \ge 1$ be a natural number and let $d_h$ be the $h$-divisor function, so that $d_h(f)$ is the
number of $h$-tuples of monic polynomials with product $f$. Then for every natural number $N$,

$$\left| \sum_{f \text{ monic},\ \deg f \le N} \chi(f) \, d_h(f) \right| \le
(\sqrt{q} + 1)^{h (\deg m - 1)}.$$

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Proposition 5; `χ^{(h)}` as in eq. (8).

Stated but not proved: `MetaMathlibExt.norm_sum_mulChar_divisorCount_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#norm-sum-mul-char-divisor-count-le).

## The $B_\kappa$-free divisor sum

Let $F$ be a field, let $\kappa$ assign a natural number
to each polynomial in $F[T]$, and let $h$ and $N$ be natural numbers. Then
$\tilde D_{B_\kappa,h}(N)$ is the sum of $d_h(f)$ over the monic $B_\kappa$-free polynomials
$f \in F[T]$ of degree at most $N$, where $d_h(f)$ is the number of $h$-tuples of monic
polynomials with product $f$, and $f$ is $B_\kappa$-free when $P^{\kappa(P)}$ does not divide $f$
for any monic irreducible $P$.

The sum is meant for finite $F$; if it has infinitely many nonzero terms, its value is $0$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `D̃_{B_κ,h}(N)`.

Formalized by `MetaMathlibExt.bFreeDivisorSum`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 563](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L563). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum).

## The $B_\kappa$-free divisor sum at degree zero

Let $F$ be a field and let $\kappa$ assign
to each polynomial in $F[T]$ a natural number, with $\kappa(P) \ne 0$ for every monic irreducible
$P$. Call $f \in F[T]$ $B_\kappa$-free when $P^{\kappa(P)}$ does not divide $f$ for any monic
irreducible $P$, let $d_h(f)$ be the number of $h$-tuples of monic polynomials with product $f$,
and let $\tilde D_{B_\kappa,h}(N)$ be the sum of $d_h(f)$ over the $B_\kappa$-free monic
$f \in F[T]$ of degree at most $N$. Then $\tilde D_{B_\kappa,h}(0) = 1$ for every natural number
$h$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `D̃_{B_κ,h}(N)`.

Formalized by `MetaMathlibExt.bFreeDivisorSum_zero`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 571](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L571). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-zero).

## B-free divisor sum in an arithmetic progression

For a field $F$, a function
$\kappa : F[T] \to \mathbb{N}$, natural numbers $h$ and $N$, and $a, m \in F[T]$, the natural
number $\tilde D_{\kappa,h}(N, a, m)$ is the sum of $d_h(f)$ over the monic $B_\kappa$-free
$f \in F[T]$ of degree at most $N$ with $f \equiv a \pmod m$, that is, with $m$ dividing $f - a$.
Here $d_h(f)$ is the number of $h$-tuples of monic polynomials with product $f$, and $f$ is
$B_\kappa$-free when no $P^{\kappa(P)}$ with $P$ monic irreducible divides it. The sum is finite
when $F$ is finite; it is taken to be $0$ if infinitely many of its terms are nonzero.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `D̃_{B_κ,h}(N, a, m)`.

Formalized by `MetaMathlibExt.bFreeDivisorSumMod`, a definition declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-mod).

## The progression sum modulo 1 is the full sum

Let $F$ be a field, let
$\kappa : F[T] \to \mathbb{N}$, and let $h$ and $N$ be natural numbers. Write
$\tilde D_{\kappa,h}(N)$ for the sum of $d_h(f)$ over the monic $B_\kappa$-free $f \in F[T]$ of
degree at most $N$, and for $a, m \in F[T]$ write $\tilde D_{\kappa,h}(N, a, m)$ for the same sum
restricted to the $f$ with $f \equiv a \pmod m$. Here $d_h(f)$ is the number of $h$-tuples of
monic polynomials with product $f$, $f$ is $B_\kappa$-free when no $P^{\kappa(P)}$ with $P$ monic
irreducible divides it, and a sum with infinitely many nonzero terms is taken to be $0$. Then
for every $a \in F[T]$, $\tilde D_{\kappa,h}(N, a, 1) = \tilde D_{\kappa,h}(N)$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Section 1, definition of `D̃_{B_κ,h}(N, a, m)`.

Formalized by `MetaMathlibExt.bFreeDivisorSumMod_one`, a theorem declared in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-mod-one).

## Asymptotic count of B-free polynomials

Let $F$ be a finite field with $q$ elements, write
$|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let $\kappa$ assign a natural number to each
polynomial in $F[T]$, with $\kappa(P) \ge 2$ for every monic irreducible $P$; let $\kappa_{\min}$
be the minimum of $\kappa(P)$ over the monic irreducible $P$. Let $\tilde D_{\kappa,1}(N)$ be the
sum of $d_1(f)$ (which is $1$ for monic $f$) over the monic $B_\kappa$-free $f$ of degree at most
$N$, where $f$ is $B_\kappa$-free when no $P^{\kappa(P)}$ with $P$ monic irreducible divides it.
Then for every $\varepsilon > 0$,

$$
\tilde D_{\kappa,1}(N) - \frac{q^N}{1 - 1/q} \prod_P \bigl(1 - |P|^{-\kappa(P)}\bigr) =
O\bigl(q^{(1/\kappa_{\min} + \varepsilon) N}\bigr)
$$

as $N \to \infty$, the product running over the monic irreducible $P$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 1, first formula.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSum_one_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-one-is-big-o).

## Asymptotic for the $B_\kappa$-free sum of the divisor function

Let $F$ be a finite field
with $q$ elements and let $\kappa$ assign to each polynomial in $F[T]$ a natural number, with
$\kappa(P) \ge 2$ for every monic irreducible $P$. A polynomial $f$ is $B_\kappa$-free when
$P^{\kappa(P)}$ does not divide $f$ for any monic irreducible $P$; $d_2(f)$ is the number of
ordered pairs of monic polynomials with product $f$; $\tilde D_{B_\kappa,2}(N)$ is the sum of
$d_2(f)$ over the $B_\kappa$-free monic $f$ of degree at most $N$; $\kappa_{\min}$ is the minimum
of $\kappa(P)$ over the monic irreducible $P$; and for a monic irreducible $P$ we write
$\kappa_P = \kappa(P)$ and $|P| = q^{\deg P}$ for its norm. Then for every $\varepsilon > 0$, as
$N \to \infty$,

$$
\tilde D_{B_\kappa,2}(N) = \frac{q^N}{1 - 1/q}
\prod_P \left( 1 - \frac{\kappa_P + 1}{|P|^{\kappa_P}} + \frac{\kappa_P}{|P|^{\kappa_P + 1}} \right)
\left( N + 1 - \frac{1}{q - 1} +
\sum_P \frac{\kappa_P (\kappa_P + 1) \deg(P) (|P| - 1)}{|P|^{\kappa_P + 1} - |P| (\kappa_P + 1) +
\kappa_P} \right) + O\left( q^{(1/\kappa_{\min} + \varepsilon) N} \right),
$$

where the product and the sum run over the monic irreducible polynomials $P$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 1, second formula.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSum_two_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-two-is-big-o).

## Asymptotic for B-free divisor sums when h is at most 2

Let $F$ be a finite field with $q$
elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let $\kappa$ assign a natural
number to each polynomial in $F[T]$, with $\kappa(P) \ge 2$ for every monic irreducible $P$. Let
$h \in \{1, 2\}$ and let $\tilde D_{\kappa,h}(N)$ be the sum of $d_h(f)$ over the monic
$B_\kappa$-free $f$ of degree at most $N$, where $d_h(f)$ is the number of $h$-tuples of monic
polynomials with product $f$, and $f$ is $B_\kappa$-free when no $P^{\kappa(P)}$ with $P$ monic
irreducible divides it. Put $C_P = \binom{h + \kappa(P) - 1}{\kappa(P)}$ and

$$
M(N) = \frac{q^N N^{h-1}}{1 - 1/q}
\prod_P \Bigl(1 - |P|^{-\kappa(P)} \bigl(C_P + |P|^{-1} (1 - C_P)\bigr)\Bigr),
$$

the product running over the monic irreducible $P$. Then
$\tilde D_{\kappa,h}(N) - M(N) = O(M(N)/N)$ as $N \to \infty$.

The paper states this for every $h \ge 1$, but its main term is not correct for $h \ge 3$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 2, cases `h = 1, 2`.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSum_isBigO_of_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-is-big-o-of-le-two).

## Asymptotic count of B-free polynomials in an arithmetic progression

Let $F$ be a finite
field with $q$ elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let $\kappa$
assign a natural number to each polynomial in $F[T]$, with $\kappa(P) \ge 2$ for every monic
irreducible $P$; let $\kappa_{\min}$ be the minimum of $\kappa(P)$ over the monic irreducible $P$.
Let $m \ne 0$ and $a$ be polynomials in $F[T]$ with $a$ coprime to $m$, and let
$\tilde D_{\kappa,1}(N, a, m)$ be the sum of $d_1(f)$ (which is $1$ for monic $f$) over the monic
$B_\kappa$-free $f$ of degree at most $N$ with $f \equiv a \pmod m$, where $f$ is $B_\kappa$-free
when no $P^{\kappa(P)}$ with $P$ monic irreducible divides it. Then for every $\varepsilon > 0$,

$$
\tilde D_{\kappa,1}(N, a, m) -
\frac{q^N}{(1 - 1/q) \, |m|} \prod_{P \nmid m} \bigl(1 - |P|^{-\kappa(P)}\bigr) =
O\bigl(q^{(1/\kappa_{\min} + \varepsilon) N}\bigr)
$$

as $N \to \infty$, the product running over the monic irreducible $P$ not dividing $m$.

The paper's statement does not list the hypothesis $m \ne 0$; it is implicit, since $m$ is the
modulus of a progression.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 3, first formula.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSumMod_one_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-mod-one-is-big-o).

## Asymptotic for the B-free divisor function in an arithmetic progression

Let $F$ be a
finite field with $q$ elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let
$\kappa$ assign a natural number to each polynomial in $F[T]$, with $\kappa(P) \ge 2$ for every
monic irreducible $P$; let $\kappa_{\min}$ be the minimum of $\kappa(P)$ over the monic
irreducible $P$. Let $m \ne 0$ and $a$ be polynomials in $F[T]$ with $a$ coprime to $m$, and let
$\tilde D_{\kappa,2}(N, a, m)$ be the sum of $d_2(f)$ over the monic $B_\kappa$-free $f$ of degree
at most $N$ with $f \equiv a \pmod m$, where $d_2(f)$ is the number of pairs of monic polynomials
with product $f$, and $f$ is $B_\kappa$-free when no $P^{\kappa(P)}$ with $P$ monic irreducible
divides it. Writing $\kappa$ for $\kappa(P)$ inside sums and products over $P$, put

$$
M(N) = \frac{q^N}{(1 - 1/q) \, |m|} \prod_{P \mid m} \Bigl(1 - \frac{1}{|P|}\Bigr)
\prod_{P \nmid m} \Bigl(1 - \frac{\kappa + 1}{|P|^{\kappa}} + \frac{\kappa}{|P|^{\kappa + 1}}\Bigr)
\times \Bigl(N + 1 - \frac{1}{q - 1} + 2 \sum_{P \mid m} \frac{\deg P}{|P| - 1} +
\sum_{P \nmid m}
\frac{\kappa (\kappa + 1) \deg P \, (|P| - 1)}{|P|^{\kappa + 1} - |P| (\kappa + 1) + \kappa}\Bigr),
$$

where $P$ runs over the monic irreducible polynomials dividing, respectively not dividing, $m$.
Then for every $\varepsilon > 0$,
$\tilde D_{\kappa,2}(N, a, m) - M(N) = O\bigl(q^{(1/\kappa_{\min} + \varepsilon) N}\bigr)$ as
$N \to \infty$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 3, second formula; `Φ` as defined after Theorem 3.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSumMod_two_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-mod-two-is-big-o).

## Asymptotic for B-free divisor sums in progressions when h is at most 2

Let $F$ be a
finite field with $q$ elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let
$\kappa$ assign a natural number to each polynomial in $F[T]$, with $\kappa(P) \ge 2$ for every
monic irreducible $P$. Let $m \ne 0$ and $a$ be polynomials in $F[T]$ with $a$ coprime to $m$, let
$h \in \{1, 2\}$, and let $\tilde D_{\kappa,h}(N, a, m)$ be the sum of $d_h(f)$ over the monic
$B_\kappa$-free $f$ of degree at most $N$ with $f \equiv a \pmod m$, where $d_h(f)$ is the number
of $h$-tuples of monic polynomials with product $f$, and $f$ is $B_\kappa$-free when no
$P^{\kappa(P)}$ with $P$ monic irreducible divides it. Put
$C_P = \binom{h + \kappa(P) - 1}{\kappa(P)}$ and

$$
M(N) = \frac{q^N N^{h-1}}{(h-1)!} \cdot
\frac{\bigl(\prod_{P \mid m} (1 - 1/|P|)\bigr)^{h-1}}{|m| \, (1 - 1/q)}
\prod_{P \nmid m} \Bigl(1 - |P|^{-\kappa(P)} \bigl(C_P + |P|^{-1} (1 - C_P)\bigr)\Bigr),
$$

the products running over the monic irreducible $P$ dividing, respectively not dividing, $m$.
Then $\tilde D_{\kappa,h}(N, a, m) - M(N) = O(M(N)/N)$ as $N \to \infty$.

The paper states this for every $h \ge 1$, but its main term is not correct for $h \ge 3$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 4, cases `h = 1, 2`; `Φ` as defined after Theorem 3.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSumMod_isBigO_of_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-mod-is-big-o-of-le-tw).

## Divisor sums over $B_\kappa$-free polynomials in short intervals

Let $F$ be a finite field
with $q$ elements and let $\kappa$ assign to each polynomial in $F[T]$ a natural number, with
$\kappa(P) \ge 2$ for every monic irreducible $P$. Suppose that $\kappa$ is symmetric:
$\kappa(P^*) = \kappa(P)$ for every monic irreducible $P$ with $P(0) \ne 0$, where $P^*$ is the
monic scalar multiple of $T^{\deg P} P(1/T)$. Let $h \ge 1$ be an integer, let $c$ be a real
number with $c > (h + 2/\kappa_{\min})/(h + 2)$, and let $\varepsilon > 0$. Then there is a constant
$C$ such that for every sufficiently large $N$, every monic $A \in F[T]$ of degree $N$ and every
integer $\Delta$ with $cN \le \Delta \le N - 2$,

$$
\left| \tilde N_{B_\kappa,h}(A, \Delta) - q^{-(N - \Delta - 1)} \left( \tilde D_{B_\kappa,h}(N) -
\tilde D_{B_\kappa,h}(N - 1) \right) \right| \le
C q^{h (N - \Delta)/2 + (1/\kappa_{\min} + \varepsilon) N}.
$$

Here $\tilde N_{B_\kappa,h}(A, \Delta)$ is the sum of $d_h(f)$ over the $B_\kappa$-free
$f \in F[T]$ with $\deg(f - A) \le \Delta$ (where $\deg 0 = -\infty$), $d_h(f)$ is the number of
$h$-tuples of monic polynomials with product $f$, $\tilde D_{B_\kappa,h}(N)$ is the sum of $d_h(f)$
over the $B_\kappa$-free monic $f$ of degree at most $N$, and $\kappa_{\min}$ is the minimum of
$\kappa(P)$ over the monic irreducible $P$.

The paper's $\kappa(P^*)$ leaves $P^*$ unnormalized and undefined for $P = T$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 5, general formula.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSum_shortInterval` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-short-interval).

## B-free polynomials in short intervals

Let $F$ be a finite field with $q$ elements, write
$|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let $\kappa$ assign a natural number to each
polynomial in $F[T]$, with $\kappa(P) \ge 2$ for every monic irreducible $P$; let $\kappa_{\min}$
be the minimum of $\kappa(P)$ over the monic irreducible $P$. Assume $\kappa$ is symmetric:
$\kappa(P^*) = \kappa(P)$ for every monic irreducible $P$ with $P(0) \ne 0$, where $P^*$ is the
monic scalar multiple of the reversed polynomial $T^{\deg P} P(1/T)$. Let
$c > (1 + 2/\kappa_{\min})/3$ and $\varepsilon > 0$. Then there is a constant $C$ such that for
all sufficiently large $N$, every monic $A \in F[T]$ of degree $N$ and every natural number
$\Delta$ with $cN \le \Delta \le N - 2$,

$$
\Bigl|\sum_f d_1(f) - q^{\Delta + 1} \prod_P \bigl(1 - |P|^{-\kappa(P)}\bigr)\Bigr| \le
C q^{(N - \Delta)/2 + (1/\kappa_{\min} + \varepsilon) N},
$$

where $f$ runs over the $B_\kappa$-free $f \in F[T]$ with $f = A$ or $\deg(f - A) \le \Delta$,
$d_1(f)$ is $1$ if $f$ is monic and $0$ otherwise, $f$ is $B_\kappa$-free when no $P^{\kappa(P)}$
with $P$ monic irreducible divides it, and $P$ runs over the monic irreducible polynomials.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 5, case `h = 1`.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSum_shortInterval_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 763](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-short-interval-one).

## The B-free divisor function in short intervals

Let $F$ be a finite field with $q$
elements, write $|f| = q^{\deg f}$ for nonzero $f \in F[T]$, and let $\kappa$ assign a natural
number to each polynomial in $F[T]$, with $\kappa(P) \ge 2$ for every monic irreducible $P$; let
$\kappa_{\min}$ be the minimum of $\kappa(P)$ over the monic irreducible $P$. Assume $\kappa$ is
symmetric: $\kappa(P^*) = \kappa(P)$ for every monic irreducible $P$ with $P(0) \ne 0$, where $P^*$
is the monic scalar multiple of the reversed polynomial $T^{\deg P} P(1/T)$. Let
$c > (2 + 2/\kappa_{\min})/4$ and $\varepsilon > 0$. Then there is a constant $C$ such that for
all sufficiently large $N$, every monic $A \in F[T]$ of degree $N$ and every natural number
$\Delta$ with $cN \le \Delta \le N - 2$,

$$
\Bigl|\sum_f d_2(f) - q^{\Delta + 1}
\prod_P \Bigl(1 - \frac{\kappa + 1}{|P|^{\kappa}} + \frac{\kappa}{|P|^{\kappa + 1}}\Bigr)
\Bigl(N + 1 + \sum_P
\frac{\kappa \deg P \, (\kappa + 1) (|P| - 1)}{|P|^{\kappa + 1} - |P| (\kappa + 1) + \kappa}\Bigr)
\Bigr| \le C q^{N - \Delta + (1/\kappa_{\min} + \varepsilon) N},
$$

where $f$ runs over the $B_\kappa$-free $f \in F[T]$ with $f = A$ or $\deg(f - A) \le \Delta$,
$d_2(f)$ is the number of pairs of monic polynomials with product $f$, $f$ is $B_\kappa$-free when
no $P^{\kappa(P)}$ with $P$ monic irreducible divides it, $P$ runs over the monic irreducible
polynomials, and $\kappa$ stands for $\kappa(P)$.

## Sources

- Habib Jaber and Matilde Lalín, *Dirichlet Convolutions and Divisor Problems over B-Free Polynomials over Function Fields*, INTEGERS 26 (2026), Article A80, Theorem 5, case `h = 2`.

Stated but not proved: `MetaMathlibExt.bFreeDivisorSum_shortInterval_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BFreeDirichletConvolutionFqTWanted.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html#b-free-divisor-sum-short-interval-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisor problems for B-free polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/function-fields/divisor-problems-for-b-free-polynomials)
