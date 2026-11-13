---
declaration: section
origin: cited
lean: MetaMathlibExt.minusculePolynomialA, MetaMathlibExt.minusculePolynomialA_one, MetaMathlibExt.minusculePolynomialA_two, MetaMathlibExt.minusculePolynomialA_three, MetaMathlibExt.minusculePolynomialA_isRealRooted, MetaMathlibExt.minusculePolynomialA_interlaces_succ, MetaMathlibExt.minusculePolynomialA_coeff_logConcave, MetaMathlibExt.minusculePolynomialA_gamma_positive
statement: formalized
---

# Minuscule polynomials of type A

19 results, 4 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html).

## Type-A minuscule polynomial

For a natural number $n$, the type-A minuscule polynomial
$N_n(x)$ is the polynomial with rational coefficients

$$N_n(x) = \frac{1}{4n + 2} \sum_{k=1}^{n-1} k (n - k) \binom{2n + 2}{2k + 1} x^k.$$

For $n = 0$ the sum is empty, so $N_0 = 0$.

## Sources

- Ming-Jian Ding and Jiang Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, definition (1.1) (arXiv:2308.16782v3, equation (1.1)).

Formalized by `MetaMathlibExt.minusculePolynomialA`, a definition declared in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a).

## The minuscule polynomial $N_1$ vanishes

The type-A minuscule polynomial $N_1(x)$ is the
zero polynomial.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, table of `N_n(x)` after (1.1).

Formalized by `MetaMathlibExt.minusculePolynomialA_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-one).

## The minuscule polynomial $N_2$

The type-A minuscule polynomial $N_2(x)$ equals $2x$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, table of `N_n(x)` after (1.1).

Formalized by `MetaMathlibExt.minusculePolynomialA_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-two).

## The minuscule polynomial $N_3$

The type-A minuscule polynomial $N_3(x)$ equals
$8x + 8x^2$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, table of `N_n(x)` after (1.1).

Formalized by `MetaMathlibExt.minusculePolynomialA_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-three).

## Real-rootedness of the minuscule polynomials

For every natural number $n$, the type-A
minuscule polynomial $N_n$, viewed as a complex polynomial, is real-rooted: every element of its
multiset of roots is real.

The paper states this for positive $n$; for $n \le 1$ the polynomial $N_n$ is $0$, whose multiset
of roots is taken to be empty.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Theorem 5 (first part).

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_isRealRooted` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-is-real-rooted).

## Interlacing of consecutive minuscule polynomials

Let $n \ge 2$. There are nonzero real
numbers $c, d$ and real numbers $r_0 \le \dots \le r_{n-1}$ and $s_0 \le \dots \le s_{n-2}$ such
that the type-A minuscule polynomials factor over $\mathbb{R}$ as
$N_{n+1}(x) = c \prod_{i=0}^{n-1} (x - r_i)$ and $N_n(x) = d \prod_{j=0}^{n-2} (x - s_j)$, and
$r_j \le s_j \le r_{j+1}$ for every $j$ with $0 \le j \le n - 2$.

This is the interlacing $N_n \preceq N_{n+1}$, relation (1.2) of the paper written in increasing
order.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Theorem 5 (second part).

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_interlaces_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-interlaces-succ).

## Log-concavity of the coefficients of the minuscule polynomials

Let $N_{n,k}$ be the
coefficient of $x^k$ in the type-A minuscule polynomial $N_n(x)$. For all natural numbers $n$
and $k$, $N_{n,k-1} N_{n,k+1} \le N_{n,k}^2$, where for $k = 0$ the index $k - 1$ is read as $0$.

The cases outside $n \ge 1$, $1 \le k \le n - 1$ hold because the coefficients involved vanish.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Corollary 7.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_coeff_logConcave` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-coeff-log-concave).

## Gamma-positivity of the minuscule polynomials

For every natural number $n$ there are
non-negative integers $\gamma_{n,0}, \dots, \gamma_{n,\lfloor n/2 \rfloor}$ such that the type-A
minuscule polynomial $N_n$ satisfies
$N_n(x) = \sum_{k=0}^{\lfloor n/2 \rfloor} \gamma_{n,k}\, x^k (1 + x)^{n-2k}$.

For $n = 0$ this holds with every $\gamma_{0,k} = 0$, since $N_0 = 0$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Corollary 8.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_gamma_positive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-gamma-positive).

## Binomial closed form of the minuscule polynomials

For every natural number $n$, the
type-A minuscule polynomial $N_n$ satisfies the identity of polynomials with rational
coefficients
$16x\, N_n(x^2) = 2(n+1)x \bigl((1+x)^{2n} + (1-x)^{2n}\bigr) -
\bigl((1+x)^{2n+2} - (1-x)^{2n+2}\bigr)$.

Dividing by $16x$ gives $N_n(x^2) = \frac{n+1}{8} \bigl((1+x)^{2n} + (1-x)^{2n}\bigr) -
\frac{1}{16x} \bigl((1+x)^{2n+2} - (1-x)^{2n+2}\bigr)$; both sides vanish at $n = 0$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Proposition 9.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_comp_sq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-comp-sq).

## Exponential generating function of the minuscule polynomials

For all real numbers $x$
and $z$ with $x \ne 0$, the series $\sum_{n \ge 0} N_n(x^2)\, z^n / n!$ built from the type-A
minuscule polynomials $N_n$ has sum
$\frac{2x(1+x)^2 z - 1 - x^2}{16x} e^{(1+x)^2 z} +
\frac{2x(1-x)^2 z + 1 + x^2}{16x} e^{(1-x)^2 z}$.

The sum starts at $n = 0$, where $N_0 = 0$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Proposition 10.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_egf` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-egf).

## Bourn–Erickson formula for the minuscule polynomials at one

For every integer $n \ge 1$,
the type-A minuscule polynomial $N_n$ satisfies $N_n(1) = (n - 1)\, 2^{2n-3}$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Corollary 11.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_eval_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-eval-one).

## Bender's central limit theorem for polynomials with non-positive real zeros

For each
natural number $n$ let $r_{n,0}, \dots, r_{n,n-1}$ be non-negative real numbers, and let $a(n,k)$
be the coefficient of $x^k$ in the real polynomial $A_n(x) = \prod_{i\lt n} (x + r_{n,i})$. Put
$\mu_n = \sum_{i\lt n} 1/(1 + r_{n,i})$ and $\sigma_n^2 = \sum_{i\lt n} r_{n,i}/(1 + r_{n,i})^2$, and let
$\sigma_n \ge 0$ be the square root of $\sigma_n^2$. Then for every $n$,
$\sum_{k=0}^{n} k\, a(n,k) / \sum_{k=0}^{n} a(n,k) = \mu_n$ and
$\sum_{k=0}^{n} (k - \mu_n)^2 a(n,k) / \sum_{k=0}^{n} a(n,k) = \sigma_n^2$. Moreover, if
$\sigma_n^2 \to \infty$ as $n \to \infty$, then for every real $x$,
$\sum_{0 \le k \le n,\ k \le \mu_n + x \sigma_n} a(n,k) / \sum_{k=0}^{n} a(n,k)$ tends to $\Phi(x)$
as $n \to \infty$, where $\Phi$ is the distribution function of the standard normal distribution.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Lemma 12 (Bender, Theorem 2).

Stated but not proved: `MetaMathlibExt.bender_asymptotic_normality` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#bender-asymptotic-normality).

## Asymptotic normality of the coefficients of the minuscule polynomials

Let $N_{n,k}$ be
the coefficient of $x^k$ in the type-A minuscule polynomial $N_n(x)$, and let
$\sigma_n = \sqrt{(n^2 - n - 2)/(8(n - 1))}$. Then for every real $x$, the sum of the
coefficients $N_{n,k}$ over $0 \le k < n$ with $k \le n/2 + x \sigma_n$, divided by $N_n(1)$,
tends to $\Phi(x)$ as $n \to \infty$, where $\Phi$ is the distribution function of the standard
normal distribution.

The centring $n/2$ and the scale $\sigma_n^2$ are the mean and the variance of the coefficient
distribution $k \mapsto N_{n,k}/N_n(1)$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Theorem 13.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_asymptotically_normal` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-asymptotically-no).

## $x$-log-concavity of the minuscule polynomials

Let $N_n$ denote the type-A minuscule
polynomial. For all natural numbers $n$ and $k$, the coefficient of $x^k$ in
$N_n(x)^2 - N_{n+1}(x) N_{n-1}(x)$ is non-negative, where $N_{n-1}$ is read as $N_0$ when $n = 0$.

For $n \le 1$ the polynomial is $0$ since $N_0 = N_1 = 0$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Theorem 14.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_x_logConcave` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-x-log-concave).

## Total positivity of the coefficient matrix of the minuscule polynomials

Let $N_{n,k}$
be the coefficient of $x^k$ in the type-A minuscule polynomial $N_n(x)$. The infinite real matrix
$[N_{n,k}]_{n,k \ge 1}$, whose entry in row $i$ and column $j$ ($i, j \ge 0$) is
$N_{i+1,j+1}$, has nonnegative minors: every square submatrix obtained by choosing finitely many
rows and finitely many columns, each in increasing order, has nonnegative determinant.

The matrix vanishes on and above its diagonal, since $N_n$ has degree at most $n - 1$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Theorem 19.

Stated but not proved: `MetaMathlibExt.minusculePolynomialA_coeffMatrix_hasNonnegativeMinors` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#minuscule-polynomial-a-coeff-matrix-has).

## Craven–Csordas characterization of multiplier $n$-sequences

Let $n$ be a natural number
and $t_0, t_1, \dots$ real numbers. Say a real polynomial splits over $\mathbb{R}$ if it is a
constant times a product of linear factors $x - r$ with $r$ real (the zero polynomial splits).
Then the following are equivalent: for every real polynomial $\sum_k a_k x^k$ of degree at most
$n$ that splits over $\mathbb{R}$, the polynomial $\sum_{k=0}^n a_k t_k x^k$ splits over
$\mathbb{R}$; and the polynomial $\sum_{k=0}^n \binom{n}{k} t_k x^k$ splits over $\mathbb{R}$ and
its roots are either all $\ge 0$ or all $\le 0$.

Only $t_0, \dots, t_n$ matter.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Lemma 3 (Craven and Csordas, Theorem 3.7).

Stated but not proved: `MetaMathlibExt.multiplier_n_sequence_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#multiplier-n-sequence-iff).

## Pólya–Schur characterization of multiplier sequences

Let $t_0, t_1, \dots$ be
non-negative real numbers. Say a real polynomial splits over $\mathbb{R}$ if it is a constant
times a product of linear factors $x - r$ with $r$ real (the zero polynomial splits). Then the
following are equivalent: for every real polynomial $\sum_k a_k x^k$ that splits over
$\mathbb{R}$, the polynomial $\sum_k a_k t_k x^k$ splits over $\mathbb{R}$; and for every
$n \ge 1$, the polynomial $\sum_{k=0}^n \binom{n}{k} t_k x^k$ splits over $\mathbb{R}$ and its
roots are either all $\ge 0$ or all $\le 0$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Lemma 18 (Pólya and Schur).

Stated but not proved: `MetaMathlibExt.multiplier_sequence_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#multiplier-sequence-iff).

## Aissen–Schoenberg–Whitney–Edrei theorem

Let $a_0, a_1, \dots$ be non-negative real
numbers with $a_0 \ne 0$. All minors of the infinite lower-triangular Toeplitz matrix
$(a_{n-k})_{n,k \ge 0}$, with zeros above the diagonal, are non-negative (that is, the sequence is
a Pólya frequency sequence) if and only if there are a real $\gamma \ge 0$, non-negative reals
$\alpha_0, \alpha_1, \dots$ and $\beta_0, \beta_1, \dots$ with
$\sum_i (\alpha_i + \beta_i) < \infty$, and a real $\varepsilon > 0$ such that for every real $x$
with $|x| < \varepsilon$ the series $\sum_{n \ge 0} a_n x^n$ converges to
$a_0 e^{\gamma x} \prod_{i \ge 0} (1 + \alpha_i x) / \prod_{i \ge 0} (1 - \beta_i x)$.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Lemma 16 (Schoenberg–Edrei Theorem, Karlin p. 154).

Stated but not proved: `MetaMathlibExt.polyaFrequency_iff_hasSum_edrei_product` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#polya-frequency-iff-has-sum-edrei-produc).

## Pólya–Schur transcendental characterization of multiplier sequences

Let
$t_0, t_1, \dots$ be non-negative real numbers with $t_0 \ne 0$. Say a real polynomial splits
over $\mathbb{R}$ if it is a constant times a product of linear factors $x - r$ with $r$ real
(the zero polynomial splits). Then the following are equivalent: for every real polynomial
$\sum_k a_k x^k$ that splits over $\mathbb{R}$, the polynomial $\sum_k a_k t_k x^k$ splits over
$\mathbb{R}$; and there are a real $\gamma \ge 0$ and non-negative reals
$\alpha_0, \alpha_1, \dots$ with $\sum_i \alpha_i < \infty$ such that for every real $x$ the series
$\sum_{n \ge 0} t_n x^n / n!$ converges to $t_0 e^{\gamma x} \prod_{i \ge 0} (1 + \alpha_i x)$.

Convergence at every real $x$ encodes that the exponential generating function is entire.

## Sources

- Ding and Zeng, *Some New Results on the Minuscule Polynomials of Type A*, Journal of Integer Sequences 28 (2025), Article 25.1.2, Lemma 17 (Pólya and Schur, PS14 p. 93).

Stated but not proved: `MetaMathlibExt.multiplier_sequence_iff_hasSum_exp_mul_tprod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MinusculePolynomialWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html#multiplier-sequence-iff-has-sum-exp-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minuscule polynomials of type A](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/minuscule-polynomials-of-type-a)
