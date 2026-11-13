---
declaration: section
origin: cited
lean: MetaMathlibExt.cuspFormNormalizedCoeff, MetaMathlibExt.cuspFormNormalizedCoeff_one, MetaMathlibExt.IsNormalizedHeckeEigenform, MetaMathlibExt.IsNormalizedHeckeEigenform.normalizedCoeff_prime_sq, MetaMathlibExt.rankinSelbergCoeff, MetaMathlibExt.rankinSelbergCoeff_apply, MetaMathlibExt.rankinSelbergCoeff_one, MetaMathlibExt.rankinSelbergCoeff_prime
statement: formalized
---

# Rankin–Selberg coefficients in arithmetic progressions

15 results, 8 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html).

## Normalized Fourier coefficients of a cusp form

Let $f$ be a cusp form of weight
$k \in \mathbb{Z}$ for $\mathrm{SL}_2(\mathbb{Z})$, with $q$-expansion
$f(z) = \sum_{n \ge 0} a_f(n) e(nz)$, where $e(z) = e^{2\pi i z}$. For each natural number $n$,
the normalized Fourier coefficient of $f$ is the complex number
$\lambda_f(n) = a_f(n) / n^{(k-1)/2}$, where $n^{(k-1)/2}$ is the real power.

At $n = 0$ the real power follows $0^0 = 1$ and $0^s = 0$ for $s \ne 0$, and division by $0$
gives $0$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Section 1 (Fourier expansion of `f ∈ H_k^*`).

Formalized by `MetaMathlibExt.cuspFormNormalizedCoeff`, a definition declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#cusp-form-normalized-coeff).

## Normalized cusp form coefficient at one

Let $f$ be a cusp form of weight
$k \in \mathbb{Z}$ for $\mathrm{SL}_2(\mathbb{Z})$, with $q$-expansion
$f(z) = \sum_{n \ge 0} a_f(n) e^{2\pi i n z}$, and let $\lambda_f$ be its normalized Fourier
coefficients. Then $\lambda_f(1) = a_f(1)$, the coefficient of $e^{2\pi i z}$ in the
$q$-expansion of $f$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Section 1.

Formalized by `MetaMathlibExt.cuspFormNormalizedCoeff_one`, a theorem declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#cusp-form-normalized-coeff-one).

## Normalized Hecke eigenform

Let $f$ be a cusp form of weight $k \in \mathbb{Z}$ for
$\mathrm{SL}_2(\mathbb{Z})$, with normalized Fourier coefficients $\lambda_f$. Then $f$ is a
normalized Hecke eigenform when $\lambda_f(1) = 1$ and, for all positive integers $m$ and $n$,
$\lambda_f(m) \lambda_f(n) = \sum_{d \mid \gcd(m, n)} \lambda_f(mn/d^2)$, the sum running over the
positive divisors $d$ of $\gcd(m, n)$. The set of these forms is denoted $H_k^*$.

At level one this is equivalent to $f$ being a simultaneous eigenform of all Hecke operators
normalized by $a_f(1) = 1$, where $f(z) = \sum_{n \ge 0} a_f(n) e^{2\pi i n z}$ is the
$q$-expansion of $f$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Section 1, Equation (1).

Formalized by `MetaMathlibExt.IsNormalizedHeckeEigenform`, a definition declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#is-normalized-hecke-eigenform).

## Hecke relation at the square of a prime

Let $f$ be a normalized Hecke eigenform of weight
$k \in \mathbb{Z}$ for $\mathrm{SL}_2(\mathbb{Z})$, with normalized Fourier coefficients
$\lambda_f$. Then $\lambda_f(p)^2 = \lambda_f(p^2) + 1$ for every prime $p$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Equation (1) with `m = n = p`.

Formalized by `MetaMathlibExt.IsNormalizedHeckeEigenform.normalizedCoeff_prime_sq`, a theorem declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#normalized-coeff-prime-sq).

## Rankin–Selberg coefficients

Let $f$ be a cusp form of weight $k \in \mathbb{Z}$ for
$\mathrm{SL}_2(\mathbb{Z})$, with normalized Fourier coefficients $\lambda_f$. The Rankin–Selberg
coefficients of $f$ form the arithmetic function $\lambda_{f \times f}$ with
$\lambda_{f \times f}(0) = 0$ and, for $n \ge 1$,
$\lambda_{f \times f}(n) = \sum_{l^2 m = n} \lambda_f(m)^2$, the sum running over the pairs of
positive integers $(l, m)$ with $l^2 m = n$; equivalently, $\lambda_{f \times f}(n)$ is the sum of
$\lambda_f(n/d)^2$ over the positive divisors $d$ of $n$ that are perfect squares.

These are the Dirichlet coefficients of
$L(f \times f, s) = \zeta(2s) \sum_{n \ge 1} \lambda_f(n)^2 n^{-s}$. The $w$-th power of
$\lambda_{f \times f}$ under Dirichlet convolution is denoted $\lambda_{w, f \times f}$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Section 1 (definition of `λ_{f×f}` and `λ_{w,f×f}`).

Formalized by `MetaMathlibExt.rankinSelbergCoeff`, a definition declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#rankin-selberg-coeff).

## Rankin–Selberg coefficients as a sum over square divisors

Let $f$ be a cusp form of
weight $k \in \mathbb{Z}$ for $\mathrm{SL}_2(\mathbb{Z})$, with normalized Fourier coefficients
$\lambda_f$ and Rankin–Selberg coefficients $\lambda_{f \times f}$. For every natural number $n$,
$\lambda_{f \times f}(n) = \sum_d \lambda_f(n/d)^2$, where $d$ runs over the positive divisors of
$n$ that are perfect squares (so the sum is empty when $n = 0$).

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Section 1.

Formalized by `MetaMathlibExt.rankinSelbergCoeff_apply`, a theorem declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#rankin-selberg-coeff-apply).

## Rankin–Selberg coefficient at one

Let $f$ be a cusp form of weight $k \in \mathbb{Z}$ for
$\mathrm{SL}_2(\mathbb{Z})$, with normalized Fourier coefficients $\lambda_f$ and Rankin–Selberg
coefficients $\lambda_{f \times f}$. Then $\lambda_{f \times f}(1) = \lambda_f(1)^2$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Section 1.

Formalized by `MetaMathlibExt.rankinSelbergCoeff_one`, a theorem declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#rankin-selberg-coeff-one).

## Rankin–Selberg coefficients at primes

Let $f$ be a cusp form of weight $k \in \mathbb{Z}$
for $\mathrm{SL}_2(\mathbb{Z})$, with normalized Fourier coefficients $\lambda_f$ and
Rankin–Selberg coefficients $\lambda_{f \times f}$. Then $\lambda_{f \times f}(p) = \lambda_f(p)^2$
for every prime $p$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Section 1.

Formalized by `MetaMathlibExt.rankinSelbergCoeff_prime`, a theorem declared in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#rankin-selberg-coeff-prime).

## Sums of squared normalized coefficients at perfect powers in arithmetic progressions

Let
$f$ be a normalized Hecke eigenform of weight $k \in \mathbb{Z}$ for $\mathrm{SL}_2(\mathbb{Z})$,
with normalized Fourier coefficients $\lambda_f$, let $j \ge 2$ be an integer, and put
$\delta = 92/597$ if $j = 2$ and $\delta = 92/(69(j-1)(j+3) + 247)$ if $j \ge 3$. Then there are
real numbers $c_q > 0$, one for each prime $q$, with the following property: for every
$\varepsilon > 0$ there is a real constant $C$ such that for every prime $q$, every natural
number $l$ coprime to $q$ and every real $x \ge 1$ with $q \le x^{3\delta/4}$,
$\bigl|\sum_{n} \lambda_f(n^j)^2 - c_q x / \varphi(q)\bigr| \le
C q x^{1 - 3\delta/2 + \varepsilon}$, where $n$ runs over the integers $1 \le n \le x$ with
$n \equiv l \pmod q$ and $\varphi$ is Euler's totient function.

Hua quotes this result from Zou et al. [52, Theorem 1]. The constant $c_q$ is allowed to depend
on $q$, a weaker reading of the printed main term, whose constant does not depend on $q$; the
constant $C$ depends only on $f$, $j$ and $\varepsilon$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.sum_cuspFormNormalizedCoeff_pow_sq_arithmeticProgression` is written with `theorem_wanted` in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#sum-cusp-form-normalized-coeff-pow-sq-ar).

## Hua's theorem on squared Rankin–Selberg coefficients in arithmetic progressions

Let $f$
be a level-one cusp form of weight $k$ that is a normalized Hecke eigenform, let
$\lambda_{f\times f}$ be its Rankin–Selberg coefficients, let $\varphi$ be Euler's totient
function, and put $\eta = 23/261$. There are real polynomials $P_q$, one for each prime $q$, each
of degree $1$ with positive leading coefficient, such that for every $\varepsilon > 0$ there is a
constant $C$ with

$$
\Bigl|\sum_{\substack{1 \le n \le x \\ n \equiv l \ (\mathrm{mod}\ q)}} \lambda_{f\times f}(n)^2 -
\frac{x}{\varphi(q)}\,P_q(\log x)\Bigr| \le C\,q\,x^{1 - 3\eta/2 + \varepsilon}
$$

for every prime $q$, every natural number $l$ coprime to $q$ and every real $x \ge 1$ with
$q \le x^{\eta}$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Theorem 1.2.

Stated but not proved: `MetaMathlibExt.sum_rankinSelbergCoeff_sq_arithmeticProgression` is written with `theorem_wanted` in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#sum-rankin-selberg-coeff-sq-arithmetic-p).

## Sums of Rankin–Selberg convolution powers in arithmetic progressions

Let $f$ be a
normalized Hecke eigenform of weight $k \in \mathbb{Z}$ for $\mathrm{SL}_2(\mathbb{Z})$, with
Rankin–Selberg coefficients $\lambda_{f \times f}$, let $w \ge 2$ be an integer, write
$\lambda_{w, f \times f}$ for the $w$-fold Dirichlet convolution power of $\lambda_{f \times f}$,
and put $\vartheta_w = 92/(247w + 10)$. Then there are real polynomials $P_q$, one for each prime
$q$, each of degree $w - 1$ with positive leading coefficient, with the following property: for
every $\varepsilon > 0$ there is a real constant $C$ such that for every prime $q$, every natural
number $l$ coprime to $q$ and every real $x \ge 1$ with $q \le x^{\vartheta_w}$,
$\bigl|\sum_{n} \lambda_{w, f \times f}(n) - (x / \varphi(q)) P_q(\log x)\bigr| \le
C q x^{1 - 3\vartheta_w/2 + \varepsilon}$, where $n$ runs over the integers $1 \le n \le x$ with
$n \equiv l \pmod q$, $\varphi$ is Euler's totient function and $\log$ is the natural logarithm.

The printed hypothesis $q \ll x^{\vartheta_w}$ is read as $q \le x^{\vartheta_w}$, and the
polynomial is allowed to depend on $q$; the constant $C$ depends only on $f$, $w$ and
$\varepsilon$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Theorem 1.3.

Stated but not proved: `MetaMathlibExt.sum_rankinSelbergCoeff_pow_arithmeticProgression` is written with `theorem_wanted` in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#sum-rankin-selberg-coeff-pow-arithmetic).

## Sums of squared Rankin–Selberg coefficients twisted by a primitive character

Let $f$ be
a level-one cusp form of weight $k$ that is a normalized Hecke eigenform, let
$\lambda_{f\times f}$ be its Rankin–Selberg coefficients, and put $\eta = 23/261$. For every
$\varepsilon > 0$ there is a constant $C$ such that for every prime $q$, every primitive Dirichlet
character $\chi$ modulo $q$ and every real $x \ge 1$ with $q \le x^{\eta}$,

$$
\Bigl|\sum_{1 \le n \le x} \lambda_{f\times f}(n)^2\,\chi(n)\Bigr| \le
C\,q\,x^{1 - 3\eta/2 + \varepsilon}.
$$

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Proposition 3.1.

Stated but not proved: `MetaMathlibExt.sum_rankinSelbergCoeff_sq_mul_primitive_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#sum-rankin-selberg-coeff-sq-mul-primitiv).

## Sums of squared Rankin–Selberg coefficients twisted by the principal character

Let $f$ be
a level-one cusp form of weight $k$ that is a normalized Hecke eigenform, let
$\lambda_{f\times f}$ be its Rankin–Selberg coefficients, and for a prime $q$ let $\chi_0$ be the
principal Dirichlet character modulo $q$. There are real polynomials $P_q$, one for each prime
$q$, each of degree $1$ with positive leading coefficient, such that for every $\varepsilon > 0$
there is a constant $C$ with

$$
\Bigl|\sum_{1 \le n \le x} \lambda_{f\times f}(n)^2\,\chi_0(n) - x\,P_q(\log x)\Bigr| \le
C\,x^{179/209 + \varepsilon}
$$

for every prime $q$ and every real $x \ge q$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Proposition 3.2.

Stated but not proved: `MetaMathlibExt.sum_rankinSelbergCoeff_sq_mul_principal_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#sum-rankin-selberg-coeff-sq-mul-principa).

## Sums of Rankin–Selberg convolution powers twisted by a primitive character

Let $f$ be a
level-one cusp form of weight $k$ that is a normalized Hecke eigenform, let $\lambda_{f\times f}$
be its Rankin–Selberg coefficients, let $w \ge 2$, let $\lambda_{w,f\times f}$ be the $w$-th
power of $\lambda_{f\times f}$ under Dirichlet convolution, and put
$\vartheta_w = 92/(247w + 10)$. For every $\varepsilon > 0$ there is a constant $C$ such that for
every prime $q$, every primitive Dirichlet character $\chi$ modulo $q$ and every real $x \ge 1$
with $q \le x^{\vartheta_w}$,

$$
\Bigl|\sum_{1 \le n \le x} \lambda_{w,f\times f}(n)\,\chi(n)\Bigr| \le
C\,q\,x^{1 - 3\vartheta_w/2 + \varepsilon}.
$$

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Proposition 4.1.

Stated but not proved: `MetaMathlibExt.sum_rankinSelbergCoeff_pow_mul_primitive_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#sum-rankin-selberg-coeff-pow-mul-primiti).

## Sums of Rankin–Selberg convolution powers twisted by the principal character

Let $f$ be a
level-one cusp form of weight $k$ that is a normalized Hecke eigenform, let $\lambda_{f\times f}$
be its Rankin–Selberg coefficients, let $w \ge 2$, let $\lambda_{w,f\times f}$ be the $w$-th
power of $\lambda_{f\times f}$ under Dirichlet convolution, and for a prime $q$ let $\chi_0$ be
the principal Dirichlet character modulo $q$. There are real polynomials $P_q$, one for each
prime $q$, each of degree $w - 1$, such that for every $\varepsilon > 0$ there is a constant $C$
with

$$
\Bigl|\sum_{1 \le n \le x} \lambda_{w,f\times f}(n)\,\chi_0(n) - x\,P_q(\log x)\Bigr| \le
C\,x^{1 - 210/(317w + 115) + \varepsilon}
$$

for every prime $q$ and every real $x \ge q$.

## Sources

- Guodong Hua, *The General Divisor Problem of Cusp Form Coefficients over Arithmetic Progressions*, INTEGERS 24 (2024), Article A3, Proposition 4.2.

Stated but not proved: `MetaMathlibExt.sum_rankinSelbergCoeff_pow_mul_principal_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HuaCuspFormDivisorProblemWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html#sum-rankin-selberg-coeff-pow-mul-princip).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rankin–Selberg coefficients in arithmetic progressions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/rankin-selberg-coefficients-in-arithmetic-progre)
