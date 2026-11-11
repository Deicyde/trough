---
declaration: section
origin: cited
lean: MetaMathlibExt.polyBernoulliPoly, MetaMathlibExt.polyBernoulliPoly_zero, MetaMathlibExt.polyBernoulliPoly_zero_index, MetaMathlibExt.sum_stirling_harmonic_eq_bernoulli, MetaMathlibExt.sum_bernoulli_harmonic_power_identity, MetaMathlibExt.sum_bernoulli_one_sub_two_pow, MetaMathlibExt.sum_bernoulli_eq_polyBernoulli, MetaMathlibExt.sum_prime_mul_bernoulli_mod_prime
statement: formalized
---

# Bernoulli identities via Stirling and harmonic numbers

11 results, 3 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html).

## Poly-Bernoulli polynomials

For a natural number $n$, an integer $k$ and a rational number
$x$, the poly-Bernoulli polynomial of degree $n$ and order $k$ at $x$ is the rational number

$$B_n^{(k)}(x) = \sum_{i=0}^{n} \binom{n}{i} B_i^{(k)} x^{n-i},$$

where $B_i^{(k)}$ are the poly-Bernoulli numbers.

These are the coefficients of the generating function
$\frac{\mathrm{Li}_k(1-e^{-t})}{1-e^{-t}} e^{xt} = \sum_{n \ge 0} B_n^{(k)}(x) \frac{t^n}{n!}$,
which is how the source defines them.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, definition of poly-Bernoulli polynomials before Corollary 3.

Formalized by `MetaMathlibExt.polyBernoulliPoly`, a definition declared in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#poly-bernoulli-poly).

## Poly-Bernoulli polynomials at zero

For every natural number $n$ and every integer $k$, the
poly-Bernoulli polynomial of degree $n$ and order $k$ evaluated at $0$ equals the
poly-Bernoulli number of index $n$ and order $k$: $B_n^{(k)}(0) = B_n^{(k)}$.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, definition of poly-Bernoulli polynomials before Corollary 3.

Formalized by `MetaMathlibExt.polyBernoulliPoly_zero`, a theorem declared in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#poly-bernoulli-poly-zero).

## Poly-Bernoulli polynomials of degree zero

For every integer $k$ and every rational number
$x$, the poly-Bernoulli polynomial of degree $0$ and order $k$ satisfies $B_0^{(k)}(x) = 1$.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, definition of poly-Bernoulli polynomials before Corollary 3.

Formalized by `MetaMathlibExt.polyBernoulliPoly_zero_index`, a theorem declared in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#poly-bernoulli-poly-zero-index).

## Bernoulli numbers from Stirling and harmonic numbers

Let $j < n$ be natural numbers. Write
${n \brace k}$ for the Stirling numbers of the second kind, ${k \brack j}$ for the unsigned
Stirling numbers of the first kind (the number of permutations of $k$ elements with exactly $j$
cycles), $H_k = \sum_{i=1}^{k} 1/i$ for the harmonic numbers (so $H_0 = 0$), and $B_m$ for the
Bernoulli numbers, normalized so that $B_1 = -1/2$. Then, in the rational numbers,

$$
\sum_{k=j}^{n} (-1)^{k-j} {n \brace k} {k \brack j} H_k
= \left(\binom{n}{j} - 1\right) \frac{B_{n-j}}{n-j}.
$$

The paper also covers the diagonal case $n = j$, reading the right-hand side as a limit (both
sides are then $H_j$); that case is not included here.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Theorem 1, equation (5).

Stated but not proved: `MetaMathlibExt.sum_stirling_harmonic_eq_bernoulli` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#sum-stirling-harmonic-eq-bernoulli).

## A Bernoulli–harmonic power-sum identity

Let $B_j$ denote the Bernoulli numbers with
$B_1 = -\tfrac12$, and let $H_m = \sum_{i=1}^{m} 1/i$ denote the harmonic numbers. For all
positive integers $n$ and $m$,

$$\sum_{j=1}^{n} \left(\binom{n}{j} - 1\right) \frac{B_j}{j} m^{n-j} =
m^n (H_m - H_n) - \sum_{j=1}^{m} \frac{(m-j)^n}{j}.$$

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Corollary 1, equation (11).

Stated but not proved: `MetaMathlibExt.sum_bernoulli_harmonic_power_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#sum-bernoulli-harmonic-power-identity).

## A weighted Bernoulli sum with factors $1 - 2^j$

Let $B_j$ denote the Bernoulli numbers
with $B_1 = -\tfrac12$. For every positive integer $n$,

$$\sum_{j=1}^{n} \left(\binom{n}{j} + 1\right) \frac{B_j}{j} \left(1 - 2^j\right) = 1.$$

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Corollary 2, equation (14).

Stated but not proved: `MetaMathlibExt.sum_bernoulli_one_sub_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#sum-bernoulli-one-sub-two-pow).

## Sums of Bernoulli numbers via poly-Bernoulli polynomials

Let $B_j$ denote the Bernoulli
numbers with $B_1 = -\tfrac12$, let $B_n^{(2)}$ denote the poly-Bernoulli numbers of order $2$,
and let $B_n^{(2)}(x)$ denote the poly-Bernoulli polynomials of order $2$. For every natural
number $n \ge 2$,

$$\sum_{j=0}^{n} B_j = B_n^{(2)}(1) + B_n - B_n^{(2)} - 1.$$

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Corollary 3.

Stated but not proved: `MetaMathlibExt.sum_bernoulli_eq_polyBernoulli` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#sum-bernoulli-eq-poly-bernoulli).

## The congruence $\sum_{j=0}^{p} pB_j \equiv -1 \pmod p$

Let $B_j$ denote the Bernoulli
numbers with $B_1 = -\tfrac12$. For every odd prime $p$, the rational number
$S = \sum_{j=0}^{p} p B_j$ has denominator not divisible by $p$, and its residue modulo $p$ (its
numerator times the inverse of its denominator in $\mathbb{Z}/p\mathbb{Z}$) equals $-1$.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Corollary 4, equation (23).

Stated but not proved: `MetaMathlibExt.sum_prime_mul_bernoulli_mod_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#sum-prime-mul-bernoulli-mod-prime).

## The congruence $\sum_{j=0}^{p-3} B_j \equiv -1 \pmod p$

Let $B_j$ denote the Bernoulli
numbers with $B_1 = -\tfrac12$. For every prime $p \ge 5$, the rational number
$S = B_0 + B_1 + \dots + B_{p-3}$ has denominator not divisible by $p$, and its residue modulo
$p$ (its numerator times the inverse of its denominator in $\mathbb{Z}/p\mathbb{Z}$) equals $-1$.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Corollary 4, equation (24).

Stated but not proved: `MetaMathlibExt.sum_bernoulli_to_prime_sub_three_mod_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#sum-bernoulli-to-prime-sub-three-mod-pri).

## The congruence $\sum_{j=0}^{p} E_j(0) \equiv 3/2 \pmod p$

Let $E_j(x)$ denote the Euler
polynomials. For every odd prime $p$, the rational number $S = E_0(0) + E_1(0) + \dots + E_p(0)$
has denominator not divisible by $p$, and its residue modulo $p$ (its numerator times the
inverse of its denominator in $\mathbb{Z}/p\mathbb{Z}$) equals $3 \cdot 2^{-1}$.

The values $E_j(0)$ are the Euler numbers of the source; they come from the generating function
$2e^{xt}/(e^t + 1)$ and begin $1, -\tfrac12, 0, \tfrac14$.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Corollary 4, equation (25).

Stated but not proved: `MetaMathlibExt.sum_euler_eval_zero_mod_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#sum-euler-eval-zero-mod-prime).

## The congruence $p\sum_{j=0}^{p} B_j/(p-j+1) \equiv -1 \pmod p$

Let $B_j$ denote the
Bernoulli numbers with $B_1 = -\tfrac12$. For every odd prime $p$, the rational number

$$S = p \sum_{j=0}^{p} \frac{B_j}{p-j+1}$$

has denominator not divisible by $p$, and its residue modulo $p$ (its numerator times the
inverse of its denominator in $\mathbb{Z}/p\mathbb{Z}$) equals $-1$.

## Sources

- Levent Kargın and Merve Mutluer, *A New Expression for the Bernoulli Numbers and Its Applications*, INTEGERS 26 (2026), Article A120, Corollary 4, equation (26).

Stated but not proved: `MetaMathlibExt.prime_mul_sum_bernoulli_div_mod_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BernoulliStirlingHarmonicWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html#prime-mul-sum-bernoulli-div-mod-prime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernoulli identities via Stirling and harmonic numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/bernoulli-numbers/bernoulli-identities-via-stirling-and-harmonic-n)
