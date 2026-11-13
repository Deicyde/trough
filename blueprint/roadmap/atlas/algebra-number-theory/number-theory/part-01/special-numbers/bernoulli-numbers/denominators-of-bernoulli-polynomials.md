---
declaration: section
origin: cited
lean: MetaMathlibExt.kellner_sondow_bernoulli_denom, MetaMathlibExt.polynomialDenominator_bernoulli_zero, MetaMathlibExt.bernoulliDiffDenominator, MetaMathlibExt.bernoulliDiffDenominator_small, MetaMathlibExt.bernoulliDiffDenominatorCoprimePart, MetaMathlibExt.bernoulliDiffDenominatorCoprimePart_small, MetaMathlibExt.bernoulliDiffDenominatorLargePart, MetaMathlibExt.bernoulliDiffDenominatorLargePart_small
statement: formalized
---

# Denominators of Bernoulli polynomials

25 results, 12 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html).

## Kellner–Sondow factorization of the denominators of Bernoulli polynomials

Let $B_k$
denote the $k$-th Bernoulli number, with $B_1 = -1/2$, let
$B_n(x) = \sum_{k=0}^{n} \binom{n}{k} B_k x^{n-k}$ be the $n$-th Bernoulli polynomial, and let
$D_n$ be the least common multiple of the denominators of its nonzero coefficients. For a prime
$p$, let $s_p(N)$ denote the sum of the base-$p$ digits of a natural number $N$. Then for every
$n \ge 1$, $D_n$ is the product of three factors: the product of the primes $p \le n + 1$ with
$p \nmid n + 1$ and $s_p(n+1) \ge p$; the product of the primes $p \le n + 1$ with $p \mid n + 1$
and $s_p(n+1) \ge p$; and the product of the primes $p \le n + 1$ with $p \mid n + 1$ and
$s_p(n+1) < p$.

## Sources

- Bernd C. Kellner, "On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients," Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem `thm:triple`, lines 351–358, <https://cs.uwaterloo.ca/journals/JIS/VOL27/Kellner/kell2.tex>, restating B. C. Kellner and J. Sondow, "On Carmichael and polygonal numbers, Bernoulli polynomials, and sums of base-p digits," Integers 21 (2021), Theorem 3.1. Factor definitions `eq:ddprod2` at lines 341–346.

Formalized by `MetaMathlibExt.kellner_sondow_bernoulli_denom`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/KellnerSondowBernoulliDenominator.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/KellnerSondowBernoulliDenominator.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#kellner-sondow-bernoulli-denom).

## The Bernoulli polynomial $B_0(x)$ has denominator one

The Bernoulli polynomial
$B_0(x) = 1$ has denominator $\operatorname{denom}(B_0(x)) = 1$. In the source's notation
$\mathfrak{D}_n = \operatorname{denom}(B_n(x))$, this is the convention $\mathfrak{D}_0 = 1$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2, after Theorem 7.

Formalized by `MetaMathlibExt.polynomialDenominator_bernoulli_zero`, a theorem declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#polynomial-denominator-bernoulli-zero).

## Denominator of $B_n(x) - B_n$

For a natural number $n$ and a prime $p$, let $s_p(n)$ be
the sum of the base-$p$ digits of $n$. Define
$\mathbb{D}_n = \prod_{p \text{ prime},\ s_p(n) \ge p} p$, the product of all primes $p$ with
$s_p(n) \ge p$; every such prime satisfies $p \le n$, so the product is finite.

By a theorem of Kellner (2017, Section 5), for $n \ge 1$ the number $\mathbb{D}_n$ is the
denominator of $B_n(x) - B_n$, where $B_n(x)$ is the $n$-th Bernoulli polynomial and $B_n$ the
$n$-th Bernoulli number.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2, equation (2.3) (`eq:ddprod`); OEIS A195441.

Formalized by `MetaMathlibExt.bernoulliDiffDenominator`, a definition declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator).

## First values of $\mathbb{D}_n$

For a natural number $n$ let $\mathbb{D}_n$ be the product
of the primes $p$ whose base-$p$ digit sum $s_p(n)$ satisfies $s_p(n) \ge p$. Then
$(\mathbb{D}_1, \mathbb{D}_2, \dots, \mathbb{D}_{10}) = (1, 1, 2, 1, 6, 2, 6, 3, 10, 2)$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2 (displayed values of `𝔻_n`).

Formalized by `MetaMathlibExt.bernoulliDiffDenominator_small`, a theorem declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-small).

## Kellner's product $\mathbb{D}^\perp_n$ over primes not dividing $n$

For
$n \in \mathbb{N}$, write $s_p(n)$ for the sum of the base-$p$ digits of $n$. The number
$\mathbb{D}^\perp_n$ is the product of all primes $p$ with $p \nmid n$ and $s_p(n) \ge p$; every
such prime satisfies $p \le n$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2, equation (2.8) (`eq:ddprod2`); OEIS A324370.

Formalized by `MetaMathlibExt.bernoulliDiffDenominatorCoprimePart`, a definition declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-coprime-part).

## Small values of $\mathbb{D}^\perp_n$

Write $s_p(n)$ for the sum of the base-$p$ digits
of $n$, and let $\mathbb{D}^\perp_n$ be the product of the primes $p$ with $p \nmid n$ and
$s_p(n) \ge p$. Then $\mathbb{D}^\perp_1 = 1$, $\mathbb{D}^\perp_2 = 1$,
$\mathbb{D}^\perp_3 = 2$, $\mathbb{D}^\perp_5 = 6$ and $\mathbb{D}^\perp_9 = 10$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2, equation (2.8).

Formalized by `MetaMathlibExt.bernoulliDiffDenominatorCoprimePart_small`, a theorem declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-coprime-part-2).

## Kellner's product $\mathbb{D}^+_n$ over primes above $\sqrt{n}$

For $n \in \mathbb{N}$,
write $s_p(n)$ for the sum of the base-$p$ digits of $n$. The number $\mathbb{D}^+_n$ is the
product of all primes $p$ with $p > \sqrt{n}$ (that is, $p^2 > n$) and $s_p(n) \ge p$; every
such prime satisfies $p \le n$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 1, equation (1.4) (`eq:ddp`).

Formalized by `MetaMathlibExt.bernoulliDiffDenominatorLargePart`, a definition declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-large-part).

## Small values of $\mathbb{D}^+_n$

Write $s_p(n)$ for the sum of the base-$p$ digits of
$n$, and let $\mathbb{D}^+_n$ be the product of the primes $p$ with $p^2 > n$ and
$s_p(n) \ge p$. Then $\mathbb{D}^+_4 = 1$, $\mathbb{D}^+_5 = 3$ and $\mathbb{D}^+_9 = 5$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 1, equation (1.4).

Formalized by `MetaMathlibExt.bernoulliDiffDenominatorLargePart_small`, a theorem declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-large-part-sm).

## Indices of Bernoulli polynomials with integral $k$-th derivative

For $k \in \mathbb{N}$,
$\overline{\mathcal{S}}_k$ is the set of $n \ge 1$ such that the $k$-th derivative $B_n^{(k)}(x)$
of the Bernoulli polynomial $B_n(x)$ has only integer coefficients, that is, has denominator
equal to $1$. We write $\overline{\mathcal{S}}$ for $\overline{\mathcal{S}}_1$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 1 (`\overline{𝒮}`) and Section 3 (`\overline{𝒮}_k`).

Formalized by `MetaMathlibExt.bernoulliIntegralDerivativeIndices`, a definition declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-integral-derivative-indices).

## The derivative of $B_1(x)$ has integer coefficients

The Bernoulli polynomial
$B_1(x) = x - \tfrac{1}{2}$ has derivative $B_1'(x) = 1 \in \mathbb{Z}[x]$, so $1$ belongs to
the set $\overline{\mathcal{S}}$ of indices $n \ge 1$ for which $B_n'(x)$ has only integer
coefficients.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 1 (`1 ∈ 𝒮`).

Formalized by `MetaMathlibExt.one_mem_bernoulliIntegralDerivativeIndices_one`, a theorem declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#one-mem-bernoulli-integral-derivative-in).

## Product formula for the denominator of $B_n(x) - B_n$

Let $n \ge 1$, let $B_n(x)$ be
the $n$-th Bernoulli polynomial and $B_n = B_n(0)$ the $n$-th Bernoulli number, and write
$s_p(n)$ for the sum of the base-$p$ digits of $n$. Then $\mathbb{D}_n$, the product of the
primes $p$ with $s_p(n) \ge p$, equals the denominator of the polynomial $B_n(x) - B_n$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Section 2, definition of `𝔻_n` and equation (2.3), quoting Kellner (2017), Section 5.

Stated but not proved: `MetaMathlibExt.bernoulliDiffDenominator_eq_polynomialDenominator` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-eq-polynomial).

## Kellner's large-part conjecture

For a natural number $n$, let $\mathbb{D}^+_n$ be the
product of the primes $p > \sqrt{n}$ with $s_p(n) \ge p$, where $s_p(n)$ is the sum of the
base-$p$ digits of $n$. This definition is the proposition that $\mathbb{D}^+_n > 1$ for every
natural number $n > 192$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Conjecture 2 (i), quoting Kellner (2017), Conjectures 1, 2.

Formalized by `MetaMathlibExt.KellnerLargePartConjecture`, a definition declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#kellner-large-part-conjecture).

## Kellner's asymptotic conjecture on large prime factors

For $n \in \mathbb{N}$ let
$\mathbb{D}^{+}_n$ be the product of the primes $p > \sqrt{n}$ whose base-$p$ digit sum $s_p(n)$
satisfies $s_p(n) \ge p$, and let $\omega(m)$ be the number of distinct prime factors of $m$. The
conjecture asserts that there is a real number $\kappa > 1$ such that
$\omega(\mathbb{D}^{+}_n) \sim \kappa \sqrt{n} / \log n$ as $n \to \infty$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Conjecture 2 (ii), equation (1.6).

Formalized by `MetaMathlibExt.KellnerLargePartAsymptoticConjecture`, a definition declared in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#kellner-large-part-asymptotic-conjecture).

## Kellner's large-prime conjectures imply the Bernoulli derivative conjectures

For
$n \in \mathbb{N}$ let $\mathbb{D}^{+}_n$ be the product of the primes $p > \sqrt{n}$ whose
base-$p$ digit sum $s_p(n)$ satisfies $s_p(n) \ge p$, let $\omega(m)$ be the number of distinct
prime factors of $m$, and let $\overline{\mathcal{S}}$ be the set of $n \ge 1$ such that the
derivative $B_n'(x)$ of the Bernoulli polynomial $B_n(x)$ has integer coefficients. If
$\mathbb{D}^{+}_n > 1$ for every $n > 192$, then
$\overline{\mathcal{S}} = \{1, 2, 4, 6, 10, 12, 28, 30, 36, 60\}$. If there is a real number
$\kappa > 1$ with $\omega(\mathbb{D}^{+}_n) \sim \kappa \sqrt{n} / \log n$ as $n \to \infty$, then
$\overline{\mathcal{S}}$ is finite.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem 3 (`jis-2024-24.2.8-thm-3`).

Stated but not proved: `MetaMathlibExt.kellner_conjectures_imply_bernoulli_integral_derivative_conjectures` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#kellner-conjectures-imply-bernoulli-inte).

## Bordellès–Luca–Moree–Shparlinski asymptotic and finiteness of integral derivatives

For
$n \in \mathbb{N}$ let $\mathbb{D}^{+}_n$ be the product of the primes $p > \sqrt{n}$ whose
base-$p$ digit sum $s_p(n)$ satisfies $s_p(n) \ge p$, and let $\omega(m)$ be the number of
distinct prime factors of $m$. There is a real number $\kappa > 1$ with
$\omega(\mathbb{D}^{+}_n) \sim \kappa \sqrt{n} / \log n$ as $n \to \infty$, and the set of
$n \ge 1$ such that the derivative $B_n'(x)$ of the Bernoulli polynomial $B_n(x)$ has integer
coefficients is finite.

Bordellès, Luca, Moree and Shparlinski prove the asymptotic with $\kappa = 2$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Corollary 4, quoting Bordellès, Luca, Moree, and Shparlinski (2018), Corollary 1.6 (`jis-2024-24.2.8-cor-4`).

Stated but not proved: `MetaMathlibExt.kellnerLargePartAsymptoticConjecture_and_finite_integral_derivative` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#kellner-large-part-asymptotic-conjecture-2).

## Constraints on Bernoulli polynomials with integral derivative

Let $n \ge 1$ be such that
the derivative $B_n'(x)$ of the Bernoulli polynomial $B_n(x)$ has integer coefficients. Then
$n + 1$ is prime, and if $n \notin \{1, 2, 4, 6, 10, 12, 28, 30, 36, 60\}$, then $n > 10^7$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem 5 (`jis-2024-24.2.8-thm-5`).

Stated but not proved: `MetaMathlibExt.bernoulli_integral_derivative_succ_prime_and_large` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-integral-derivative-succ-prime).

## Denominators of Bernoulli polynomials are even

Let $n \ge 1$. Write $\mathfrak{D}_n$ for
the denominator of the Bernoulli polynomial $B_n(x)$, $\mathcal{D}_n$ for the denominator of
$S_n(x) = (B_{n+1}(x) - B_{n+1}) / (n + 1)$, where $B_{n+1}$ is the Bernoulli number,
$\operatorname{rad}(m)$ for the product of the primes dividing $m$, and $\mathbb{D}^{\perp}_n$ for
the product of the primes $p \nmid n$ whose base-$p$ digit sum $s_p(n)$ satisfies $s_p(n) \ge p$.
Then $\mathfrak{D}_n = \operatorname{rad}(\mathcal{D}_n)$; $\mathfrak{D}_n$ is even; some
coefficient of $B_n(x)$ is not an integer; $\mathbb{D}^{\perp}_n$ is even if $n \ge 3$ is odd;
and $\mathbb{D}^{\perp}_n$ is odd if $n = 1$ or $n$ is even.

Part (iii) of Corollary 8 is printed as "otherwise, $\mathbb{D}^{\perp}_n$ is even", which fails
at $n = 2$, where $\mathbb{D}^{\perp}_2 = 1$; the proof in the paper shows
$\mathbb{D}^{\perp}_1 = 1$ and $2 \nmid \mathbb{D}^{\perp}_n$ for even $n$, and the statement
above follows that proof.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Corollary 8 (`jis-2024-24.2.8-cor-8`).

Stated but not proved: `MetaMathlibExt.bernoulli_polynomial_denominator_rad_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-polynomial-denominator-rad-eve).

## Integrality of the derivative of a Bernoulli polynomial

Let $n \ge 1$, let $B_m(x)$
denote the $m$-th Bernoulli polynomial, write $s_p(n)$ for the sum of the base-$p$ digits of $n$,
and let $\mathbb{D}^\perp_n$ be the product of the primes $p$ with $p \nmid n$ and
$s_p(n) \ge p$. Then $B_n'(x)$ has integer coefficients if and only if $\mathbb{D}^\perp_n = 1$,
and $\mathbb{D}^\perp_n = 1$ if and only if the denominator of $B_{n-1}(x)$ equals the radical
$\operatorname{rad}(n)$. Moreover, if $B_n'(x)$ has integer coefficients, then $n + 1$ is prime.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem 9 (`jis-2024-24.2.8-thm-9`).

Stated but not proved: `MetaMathlibExt.bernoulli_derivative_integral_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-derivative-integral-iff).

## Indices with $\mathbb{D}_n = \operatorname{rad}(n + 1)$

Write $s_p(m)$ for the sum of
the base-$p$ digits of $m$, let $\mathbb{D}_m$ be the product of the primes $p$ with
$s_p(m) \ge p$, and let $\mathbb{D}^\perp_m$ be the product of the primes $p$ with $p \nmid m$
and $s_p(m) \ge p$. Let $\overline{\mathcal{R}}$ be the set of $n \ge 1$ with
$\mathbb{D}_n = \operatorname{rad}(n + 1)$, where $\operatorname{rad}$ denotes the radical. For
every $n \in \overline{\mathcal{R}}$, the number $n + 1$ is not prime; if $n$ is odd then
$\mathbb{D}^\perp_{n+1} = 1$; and if $n$ is even then $n = 2^e$ for some $e \ge 1$. Moreover,
the set $\overline{\mathcal{R}}$ is finite.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem 10 (`jis-2024-24.2.8-thm-10`).

Stated but not proved: `MetaMathlibExt.bernoulliDiffDenominator_eq_radical_succ_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-eq-radical-su).

## The odd radical conjecture implies the integral-derivative conjecture

For $n \ge 1$, let
$\mathbb{D}_n$ be the product of the primes $p$ with $s_p(n) \ge p$, where $s_p(n)$ is the sum of
the base-$p$ digits of $n$, and let $\operatorname{rad}(m)$ be the product of the distinct primes
dividing $m$. Let $\overline{\mathcal{S}}$ be the set of $n \ge 1$ such that the derivative
$B_n'(x)$ of the Bernoulli polynomial $B_n(x)$ has only integer coefficients. If the odd
integers $n \ge 1$ with $\mathbb{D}_n = \operatorname{rad}(n + 1)$ are exactly
$3, 5, 9, 11, 27, 29, 35, 59$, then
$\overline{\mathcal{S}} = \{1, 2, 4, 6, 10, 12, 28, 30, 36, 60\}$.

The hypothesis is Conjecture 11 of the source, about the set
$\overline{\mathcal{R}} = \{n \ge 1 : \mathbb{D}_n = \operatorname{rad}(n + 1)\}$, restricted to
odd $n$; the conclusion is Conjecture 1, and in particular $\overline{\mathcal{S}}$ is finite.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem 12 (`jis-2024-24.2.8-thm-12`).

Stated but not proved: `MetaMathlibExt.odd_radical_conjecture_implies_bernoulli_integral_derivative_conjecture` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#odd-radical-conjecture-implies-bernoulli).

## Denominators of higher derivatives of Bernoulli polynomials

For $m \ge 0$ let
$\mathfrak{D}_m$ be the denominator of the Bernoulli polynomial $B_m(x)$, and for $k \ge 1$ let
$\mathfrak{D}_n^{(k)}$ be the denominator of the $k$-th derivative $B_n^{(k)}(x)$ of $B_n(x)$.
Write $(n)_k = n(n-1)\cdots(n-k+1)$ for the falling factorial, $s_p(m)$ for the sum of the
base-$p$ digits of $m$, $\operatorname{rad}(n)$ for the product of the primes dividing $n$, and
$\mathbb{D}^{\perp}_m$ for the product of the primes $p \nmid m$ with $s_p(m) \ge p$. Let
$k, n \ge 1$. If $k \le n$, then

$$\mathfrak{D}_n^{(k)} = \frac{\mathfrak{D}_{n-k}}{\gcd(\mathfrak{D}_{n-k}, (n)_k)}
= \frac{\mathbb{D}^{\perp}_{n-k+1}}{\gcd(\mathbb{D}^{\perp}_{n-k+1}, (n)_{k-1})}
= \prod_{p \text{ prime},\ p \le n,\ p \nmid (n)_k,\ s_p(n-k+1) \ge p} p.$$

If $n < k$, then $\mathfrak{D}_n^{(k)} = 1$. No prime $p \le k$ divides $\mathfrak{D}_n^{(k)}$.
Finally, $\mathfrak{D}_n^{(1)} = \mathfrak{D}_{n-1} / \operatorname{rad}(n) = \mathbb{D}^{\perp}_n$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem 13 (`jis-2024-24.2.8-thm-13`).

Stated but not proved: `MetaMathlibExt.bernoulli_higher_derivative_denominator` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-higher-derivative-denominator).

## Finitely many Bernoulli polynomials have an integral $k$-th derivative

For $k \ge 1$ let
$\overline{\mathcal{S}}_k$ be the set of $n \ge 1$ such that the $k$-th derivative $B_n^{(k)}(x)$
of the Bernoulli polynomial $B_n(x)$ has integer coefficients. For every $k \ge 1$ the set
$\overline{\mathcal{S}}_k$ is finite and
$\overline{\mathcal{S}}_k \subseteq \overline{\mathcal{S}}_{k+1}$.

The paper writes $\subset$ for this inclusion; its proof gives inclusion, not strict inclusion.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Theorem 14 (`jis-2024-24.2.8-thm-14`).

Stated but not proved: `MetaMathlibExt.bernoulliIntegralDerivativeIndices_finite_and_mono` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-integral-derivative-indices-fi).

## Parity, radical divisibility and an lcm recursion for $\mathbb{D}_n$

Write $s_p(m)$ for
the sum of the base-$p$ digits of $m$, let $\mathbb{D}_m$ be the product of the primes $p$ with
$s_p(m) \ge p$, and let $\mathbb{D}^\perp_m$ be the product of the primes $p$ with $p \nmid m$
and $s_p(m) \ge p$. Let $n \ge 1$. Then $\mathbb{D}_n$ is odd if and only if $n = 2^e$ for some
$e \ge 0$. If $n + 1$ is not prime, then the radical $\operatorname{rad}(n + 1)$ divides both
$\mathbb{D}_n$ and $\mathbb{D}^\perp_n$. If $n \ge 3$ is odd, then
$\mathbb{D}_n = \operatorname{lcm}(\mathbb{D}_{n+1}, \operatorname{rad}(n + 1))$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Lemma 16 (`jis-2024-24.2.8-lem-16`).

Stated but not proved: `MetaMathlibExt.bernoulliDiffDenominator_parity_radical_lcm` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-parity-radica).

## The large-prime part divides the coprime part

Write $s_p(n)$ for the sum of the base-$p$
digits of $n$, let $\mathbb{D}^+_n$ be the product of the primes $p$ with $p^2 > n$ and
$s_p(n) \ge p$, and let $\mathbb{D}^\perp_n$ be the product of the primes $p$ with $p \nmid n$
and $s_p(n) \ge p$. Then $\mathbb{D}^+_n$ divides $\mathbb{D}^\perp_n$ for every $n \ge 1$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Lemma 17 (`jis-2024-24.2.8-lem-17`).

Stated but not proved: `MetaMathlibExt.bernoulliDiffDenominatorLargePart_dvd_coprimePart` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-large-part-dv).

## $\mathbb{D}^+_n$ eventually exceeds every fixed rising product

Write $s_p(n)$ for the sum
of the base-$p$ digits of $n$ and let $\mathbb{D}^+_n$ be the product of the primes $p$ with
$p^2 > n$ and $s_p(n) \ge p$. For every $k \ge 1$ there is $N$ such that
$\mathbb{D}^+_n > (n + 1)(n + 2) \cdots (n + k)$ for all $n > N$.

## Sources

- Bernd C. Kellner, *On the Finiteness of Bernoulli Polynomials Whose Derivative Has Only Integral Coefficients*, Journal of Integer Sequences 27 (2024), Article 24.2.8, Lemma 18 (`jis-2024-24.2.8-lem-18`).

Stated but not proved: `MetaMathlibExt.bernoulliDiffDenominatorLargePart_eventually_gt_descFactorial` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliDerivativeDenominatorWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html#bernoulli-diff-denominator-large-part-ev).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Denominators of Bernoulli polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/bernoulli-numbers/denominators-of-bernoulli-polynomials)
