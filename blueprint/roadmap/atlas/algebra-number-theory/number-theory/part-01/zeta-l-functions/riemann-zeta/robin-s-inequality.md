---
declaration: section
origin: cited
lean: MetaMathlibExt.robin_criterion_for_riemann_hypothesis, MetaMathlibExt.robinExceptionalSet, MetaMathlibExt.robinExceptionalSet_eq_empty_of_le, MetaMathlibExt.card_robinExceptionalSet_isBigO_div_log_log, MetaMathlibExt.card_robinExceptionalSet_isBigO_div_sqrt_log, MetaMathlibExt.card_robinExceptionalSet_isBigO_rpow, MetaMathlibExt.harmonicExtension, MetaMathlibExt.harmonicExtension_zero
statement: formalized
---

# Robin's inequality

31 results, 4 proved and 27 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html).

## Robin's criterion for the Riemann hypothesis

The Riemann hypothesis holds if and only if
$\sigma(n) < e^{\gamma}\, n \log\log n$ for every natural number $n > 5040$, where $\sigma(n)$ is
the sum of the positive divisors of $n$, $\gamma$ is the Euler–Mascheroni constant, and
$\log$ is the natural logarithm.

## Sources

- Sadegh Nazardonyavi and Semyon Yakubovich, "Extremely Abundant Numbers and the Riemann Hypothesis", Journal of Integer Sequences 17 (2014), Article 14.2.8, abstract, lines 77–80, attributed there to Robin, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Nazar/nazar4.tex>.

Stated but not proved: `MetaMathlibExt.robin_criterion_for_riemann_hypothesis` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinCriterionWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinCriterionWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-criterion-for-riemann-hypothesis).

## Robin exceptional set

For a real number $x$, the Robin exceptional set up to $x$ is the
set of natural numbers $n$ with $7! = 5040 < n \le x$ that fail Robin's inequality, that is,
with $\sigma(n) \ge e^\gamma n \log\log n$, where $\sigma(n)$ is the sum of the divisors of $n$
and $\gamma$ is the Euler–Mascheroni constant. Its cardinality is the counting function $N_R(x)$.

## Sources

- Florian Luca and Patrick Solé, *On Robin's Inequality*, INTEGERS 25 (2025), Article A8, Section 1.

Formalized by `MetaMathlibExt.robinExceptionalSet`, a definition declared in [WantedExt/NumberTheory/RobinExceptionalCountWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinExceptionalCountWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-exceptional-set).

## The Robin exceptional set is empty up to $7!$

For every real $x \le 7! = 5040$, the
Robin exceptional set up to $x$ is empty; that is, its cardinality $N_R(x)$ is $0$.

## Sources

- Florian Luca and Patrick Solé, *On Robin's Inequality*, INTEGERS 25 (2025), Article A8, Section 1 (definition of `N_R(x)`).

Formalized by `MetaMathlibExt.robinExceptionalSet_eq_empty_of_le`, a theorem declared in [WantedExt/NumberTheory/RobinExceptionalCountWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinExceptionalCountWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-exceptional-set-eq-empty-of-le).

## Failures of Robin's inequality number $O(x/\log\log x)$

Let $N_R(x)$ be the number of
elements of the Robin exceptional set up to $x$. Then $N_R(x) = O(x / \log\log x)$ as the real
number $x$ tends to infinity.

## Sources

- Florian Luca and Patrick Solé, *On Robin's Inequality*, INTEGERS 25 (2025), Article A8, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_robinExceptionalSet_isBigO_div_log_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinExceptionalCountWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinExceptionalCountWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#card-robin-exceptional-set-is-big-o-div).

## Failures of Robin's inequality number $O(x/\sqrt{\log x})$

Let $N_R(x)$ be the number
of elements of the Robin exceptional set up to $x$. Then $N_R(x) = O(x / \sqrt{\log x})$ as the
real number $x$ tends to infinity.

## Sources

- Florian Luca and Patrick Solé, *On Robin's Inequality*, INTEGERS 25 (2025), Article A8, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_robinExceptionalSet_isBigO_div_sqrt_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinExceptionalCountWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinExceptionalCountWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#card-robin-exceptional-set-is-big-o-div-2).

## Failures of Robin's inequality number $O(x^\varepsilon)$

Let $N_R(x)$ be the number of
elements of the Robin exceptional set up to $x$. For every real $\varepsilon > 0$,
$N_R(x) = O(x^\varepsilon)$ as the real number $x$ tends to infinity.

## Sources

- Florian Luca and Patrick Solé, *On Robin's Inequality*, INTEGERS 25 (2025), Article A8, Theorem 3.

Stated but not proved: `MetaMathlibExt.card_robinExceptionalSet_isBigO_rpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinExceptionalCountWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinExceptionalCountWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#card-robin-exceptional-set-is-big-o-rpow).

## The real extension of the harmonic numbers

For a real number $x$, let

$$H(x) = \int_0^1 \frac{t^x - 1}{t - 1}\,dt,$$

where $t^x$ is the real power and the integral is the Lebesgue integral over $[0, 1]$, taken to be
$0$ when the integrand is not integrable.

This extends the harmonic numbers: $H(n) = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$ for every
natural number $n$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Section 3.1 (definition of `H(x)`).

Formalized by `MetaMathlibExt.harmonicExtension`, a definition declared in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-extension).

## The real extension of the harmonic numbers vanishes at zero

The real extension
$H(x) = \int_0^1 \frac{t^x - 1}{t - 1}\,dt$ of the harmonic numbers satisfies $H(0) = 0$.

## Sources

- Assani, Chester, and Paschal, INTEGERS 26 (2026), Article A86, Section 3.1 (definition of `H(x)`).

Formalized by `MetaMathlibExt.harmonicExtension_zero`, a theorem declared in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-extension-zero).

## The real extension agrees with the harmonic numbers

Let
$H(x) = \int_0^1 \frac{t^x - 1}{t - 1}\,dt$ for real $x$ be the real extension of the harmonic
numbers. For every natural number $n$, $H(n) = H_n$, where $H_n = \sum_{i=1}^n 1/i$ is the
$n$-th harmonic number.

## Sources

- Assani, Chester, and Paschal, INTEGERS 26 (2026), Article A86, Section 3.1 ("`H(n) = H_n` for all `n ∈ ℕ`").

Stated but not proved: `MetaMathlibExt.harmonicExtension_natCast` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-extension-nat-cast).

## Rosser–Schoenfeld and Dusart bounds for the $k$-th prime

Let $p_k$ be the $k$-th prime
($p_1 = 2$) and $\log$ the natural logarithm. For every natural number $k \ge 6$,

$$k(\log k + \log \log k - 1) < p_k < k(\log k + \log \log k).$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 1, equation (3).

Stated but not proved: `MetaMathlibExt.nth_prime_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#nth-prime-bounds).

## Lower bound for the double logarithm of a primorial divided by one of its primes

Let
$p_\ell$ be the $\ell$-th prime ($p_1 = 2$) and $\log$ the natural logarithm. For natural numbers
$k \ge 99$ and $j$ with $1 \le j \le k + 1$, let $m = p_1 p_2 \cdots p_{k+1} / p_j$. Then

$$\log \log m > \log\bigl((k+1)(\log(k+1) + \log \log(k+1) - 1) \log 2.51 - \log p_j\bigr).$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 4.

Stated but not proved: `MetaMathlibExt.log_log_primorial_div_prime_gt` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#log-log-primorial-div-prime-gt).

## Robin's inequality for $n > 5040$ when one of $2, 3, 5$ does not divide $n$

Let
$\sigma(n)$ denote the sum of the divisors of $n$ and $\gamma$ the Euler–Mascheroni constant.
Let $p \in \{2, 3, 5\}$ and let $n > 5040$ be a natural number not divisible by $p$. Then Robin's
inequality $\sigma(n) < e^{\gamma} n \log \log n$ holds.

The paper prints Robin's inequality as $\sigma(n) < e^{\gamma} \log \log n$, dropping the factor
$n$; the standard form, which the paper uses in Section 2, is formalized.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 4.

Stated but not proved: `MetaMathlibExt.robin_inequality_of_not_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-inequality-of-not-dvd).

## Robin's inequality for $2^k n$ with $n$ odd and large

Let $\sigma(N)$ denote the sum of
the divisors of $N$ and $\gamma$ the Euler–Mascheroni constant. Let $k \ge 1$ and let $n$ be an
odd natural number with $n > b(k) = e^{e^{\sqrt{2.51(2^{k+1} - 1)/e^{\gamma}}}} / 2^k$. Then
Robin's inequality $\sigma(2^k n) < e^{\gamma} 2^k n \log \log (2^k n)$ holds.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 5, equation (12).

Stated but not proved: `MetaMathlibExt.robin_inequality_two_pow_mul_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-inequality-two-pow-mul-odd).

## Robin's inequality for $2n$ with $n \ge 620$ odd and for primorials above $30$

Let
$\sigma(N)$ denote the sum of the divisors of $N$ and $\gamma$ the Euler–Mascheroni constant. For
every odd natural number $n \ge 620$, Robin's inequality
$\sigma(2n) < e^{\gamma} \cdot 2n \log \log (2n)$ holds. For every natural number $m$ whose
primorial $m\# = \prod_{p \le m,\ p \text{ prime}} p$ exceeds $30$, Robin's inequality
$\sigma(m\#) < e^{\gamma} \, m\# \log \log (m\#)$ holds.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Corollary 2.

Stated but not proved: `MetaMathlibExt.robin_inequality_two_mul_odd_and_primorial` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-inequality-two-mul-odd-and-primori).

## Robin's inequality for $2^k n > 5040$ with $n$ odd under a bound on $k$, and for $21$-free $n > 5040$

**Robin's inequality for $2^k n > 5040$ with $n$ odd under a bound on $k$, and for $21$-free
$n > 5040$.** Let $\sigma(N)$ denote the sum of the divisors of $N$ and $\gamma$ the
Euler–Mascheroni constant, and let $C = 10^{10^{13.11485}}$. First, let $k \ge 1$ be such that
$2^k \tilde b(k) = e^{e^{(0.0168(2^{k+1} - 1)/e^{\gamma})^{1/3}}} < C$. Then for every odd natural
number $n$ with $2^k n > 5040$, Robin's inequality
$\sigma(2^k n) < e^{\gamma} 2^k n \log \log (2^k n)$ holds. Second, for every natural number
$n > 5040$ that is $21$-free (no prime $p$ satisfies $p^{21} \mid n$), Robin's inequality
$\sigma(n) < e^{\gamma} n \log \log n$ holds.

The paper omits $> 5040$; as printed the claims fail at $2 \cdot 3 = 6$ and at the $21$-free
$n = 12$, and its proof treats exactly the range $2^k n > 5041$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 7.

Stated but not proved: `MetaMathlibExt.robin_inequality_two_pow_mul_odd_and_twentyOne_free` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-inequality-two-pow-mul-odd-and-twe).

## Robin's inequality holds on a set of natural density one

Let $\sigma(n)$ be the sum of
the divisors of $n$, $\gamma$ the Euler–Mascheroni constant and $\log$ the natural logarithm. The
proportion of the integers $n$ with $1 \le n \le N$ that satisfy Robin's inequality
$\sigma(n) < e^{\gamma} n \log \log n$ tends to $1$ as $N \to \infty$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 8.

Stated but not proved: `MetaMathlibExt.robin_inequality_density_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#robin-inequality-density-one).

## Upper bound $H(x) < \log x + \gamma + 1/(2x)$

With $H$ the real extension of the harmonic
numbers, $\log$ the natural logarithm and $\gamma$ the Euler–Mascheroni constant, every real
$x \ge 1$ satisfies $H(x) < \log x + \gamma + \frac{1}{2x}$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 6.

Stated but not proved: `MetaMathlibExt.harmonicExtension_lt_log_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-extension-lt-log-add).

## Logarithmic upper bound for $H(x)$ with a $\pi^2$ correction

With $H$ the real extension of
the harmonic numbers and $\log$ the natural logarithm, every real $x \ge 4$ satisfies

$$H(x) < \frac{2 \log x}{1 + 6/(\pi^2 x)}.$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 7.

Stated but not proved: `MetaMathlibExt.harmonicExtension_lt_two_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-extension-lt-two-log).

## Upper bounds for harmonic numbers and for the logarithm of their real extension

Let
$H_m = 1 + \frac{1}{2} + \cdots + \frac{1}{m}$ be the $m$-th harmonic number, $H(x)$ the real
extension $\int_0^1 \frac{t^x - 1}{t - 1}\,dt$ of the harmonic numbers, and $\log$ the natural
logarithm. Then $H_{n+1} \le n / \log n$ for every natural number $n > 1$, and
$\log H(x) \le x / (2 \log x)$ for every real number $x \ge 4$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 8.

Stated but not proved: `MetaMathlibExt.harmonic_succ_le_and_log_harmonicExtension_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-succ-le-and-log-harmonic-extens).

## Upper bound for $H(x) \log H(x)$

With $H$ the real extension of the harmonic numbers and
$\log$ the natural logarithm, every real $x \ge 4$ satisfies

$$H(x) \log H(x) < \frac{x^2}{x + 6/\pi^2}.$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 9.

Stated but not proved: `MetaMathlibExt.harmonicExtension_mul_log_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-extension-mul-log-lt).

## Lower bound for the derivative $H'(x)$

With $H$ the real extension of the harmonic numbers
and $\log$ the natural logarithm, every real $x \ge 4$ satisfies

$$H'(x) > \frac{H(x) \log H(x)}{x^2}.$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 10.

Stated but not proved: `MetaMathlibExt.harmonicExtension_mul_log_div_sq_lt_deriv` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#harmonic-extension-mul-log-div-sq-lt-der).

## Monotonicity of $e^{H(x)} \log H(x) / x$

With $H$ the real extension of the harmonic
numbers and $\log$ the natural logarithm, the function $g(x) = e^{H(x)} \log H(x) / x$ is
non-decreasing on $[4, \infty)$: $g(x) \le g(y)$ whenever $4 \le x \le y$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Proposition 2.

Stated but not proved: `MetaMathlibExt.exp_harmonicExtension_mul_log_div_monotoneOn` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#exp-harmonic-extension-mul-log-div-monot).

## Monotonicity of $e^{H_n} \log H_n / n$

With $H_n = \sum_{i=1}^n 1/i$ the $n$-th harmonic
number and $\log$ the natural logarithm, the sequence $e^{H_n} \log H_n / n$ is non-decreasing
for $n \ge 1$: its value at $m$ is at most its value at $n$ whenever $1 \le m \le n$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Corollary 3.

Stated but not proved: `MetaMathlibExt.exp_harmonic_mul_log_div_monotoneOn` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#exp-harmonic-mul-log-div-monotone-on).

## A least counterexample to the Kaneko–Lagarias inequality is superabundant

Let
$\sigma(n)$ be the sum of the divisors of $n$, $H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$ the
$n$-th harmonic number and $\log$ the natural logarithm. Let $n_0 > 60$ be a natural number for
which the Kaneko–Lagarias inequality $\sigma(n_0) < e^{H_{n_0}} \log H_{n_0}$ fails, while
$\sigma(n) < e^{H_n} \log H_n$ holds for every natural number $n$ with $60 < n < n_0$. Then $n_0$
is superabundant: $\sigma(m)/m < \sigma(n_0)/n_0$ for every natural number $m$ with $1 \le m < n_0$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 9.

Stated but not proved: `MetaMathlibExt.least_kaneko_lagarias_counterexample_superabundant` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#least-kaneko-lagarias-counterexample-sup).

## Robin's inequality implies the Kaneko–Lagarias inequality

Let $\sigma(n)$ be the sum of
the divisors of $n$, $\gamma$ the Euler–Mascheroni constant, $\log$ the natural logarithm and
$H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$ the $n$-th harmonic number. For every natural
number $n$, if Robin's inequality $\sigma(n) < e^{\gamma} n \log \log n$ holds, then so does the
Kaneko–Lagarias inequality $\sigma(n) < e^{H_n} \log H_n$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 10.

Stated but not proved: `MetaMathlibExt.kaneko_lagarias_of_robin` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#kaneko-lagarias-of-robin).

## Mertens-type bound for a product over the first primes with one prime omitted

Let
$p_\ell$ be the $\ell$-th prime ($p_1 = 2$), $\log$ the natural logarithm and $B \approx 0.2615$
the Meissel–Mertens constant. For all natural numbers $k$ and $j$ with $1 \le j \le k + 1$,

$$\prod_{1 \le \ell \le k+1,\ \ell \ne j} \frac{p_\ell + 1}{p_\ell} \le
\log(p_{k+1}) \exp\Bigl(B - \frac{1}{p_j} + \frac{5}{\log p_{k+1}}\Bigr).$$

In the source this constant is called $c_1$, cited there from Tenenbaum's Theorem 1.10.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 2.

Stated but not proved: `MetaMathlibExt.prod_succ_div_prime_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#prod-succ-div-prime-le).

## Explicit bound for a product over the first primes with one prime omitted

Let $p_\ell$ be
the $\ell$-th prime ($p_1 = 2$), $\log$ the natural logarithm and $B$ the Meissel–Mertens constant.
For natural numbers $k \ge 6$ and $j$ with $1 \le j \le k + 1$, put
$U = (k+1)(\log(k+1) + \log \log(k+1))$ and $L = (k+1)(\log(k+1) + \log \log(k+1) - 1)$. Then

$$\prod_{1 \le \ell \le k+1,\ \ell \ne j} \frac{p_\ell + 1}{p_\ell} <
\log U \cdot \exp\Bigl(B - \frac{1}{p_j} + \frac{5}{\log L}\Bigr).$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 3.

Stated but not proved: `MetaMathlibExt.prod_succ_div_prime_lt_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#prod-succ-div-prime-lt-bound).

## Eventual bound for $C(k)B(k)$ by an explicit logarithm

Let $p_\ell$ denote the $\ell$-th
prime ($p_1 = 2$), $\log$ the natural logarithm, $\gamma$ the Euler–Mascheroni constant and $c_1$
the Meissel–Mertens constant. For $j \in \{1, 2, 3\}$ and $k \in \mathbb{N}$ put
$L(k) = (k+1)(\log(k+1) + \log\log(k+1))$, $L^-(k) = (k+1)(\log(k+1) + \log\log(k+1) - 1)$ and

$$C(k) = \log L(k) \cdot \exp\Bigl(c_1 - \frac{1}{p_j} + \frac{5}{\log L^-(k)}\Bigr),
\qquad B(k) = \prod_{\substack{1 \le \ell \le k+1 \\ \ell \ne j}} \frac{p_\ell^2}{p_\ell^2 - 1}.$$

Then there is $K \in \mathbb{N}$ such that for every $k \ge K$,

$$C(k)\,B(k) < e^{\gamma} \log\bigl(L^-(k) \log 2.51 - \log p_j\bigr).$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Proposition 1.

Stated but not proved: `MetaMathlibExt.exists_bound_mul_prod_sq_lt_exp_eulerMascheroni_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#exists-bound-mul-prod-sq-lt-exp-euler-ma).

## Eventual bound for $C(k)B(k)$ by $e^\gamma \log\log$ of a primorial quotient

Let $p_\ell$
denote the $\ell$-th prime ($p_1 = 2$), $\log$ the natural logarithm, $\gamma$ the
Euler–Mascheroni constant, $c_1$ the Meissel–Mertens constant and $p\#$ the product of all primes
at most $p$. For $j \in \{1, 2, 3\}$ and $k \in \mathbb{N}$ put
$L(k) = (k+1)(\log(k+1) + \log\log(k+1))$, $L^-(k) = (k+1)(\log(k+1) + \log\log(k+1) - 1)$ and

$$C(k) = \log L(k) \cdot \exp\Bigl(c_1 - \frac{1}{p_j} + \frac{5}{\log L^-(k)}\Bigr),
\qquad B(k) = \prod_{\substack{1 \le \ell \le k+1 \\ \ell \ne j}} \frac{p_\ell^2}{p_\ell^2 - 1}.$$

Then there is $K \in \mathbb{N}$ such that for every $k \ge K$,

$$C(k)\,B(k) < e^{\gamma} \log\log\frac{p_{k+1}\#}{p_j}.$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Theorem 2.

Stated but not proved: `MetaMathlibExt.exists_bound_mul_prod_sq_lt_exp_eulerMascheroni_mul_log_log` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#exists-bound-mul-prod-sq-lt-exp-euler-ma-2).

## The factor $\hat C(k)$ is below $1.525$

Let $\log$ be the natural logarithm. For every
natural number $k \ge 13042$, with $L^-(k) = (k+1)(\log(k+1) + \log\log(k+1) - 1)$,

$$\hat C(k) = \exp\Bigl(\frac{5}{\log L^-(k)}\Bigr) < 1.525.$$

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 5.

Stated but not proved: `MetaMathlibExt.exp_five_div_log_bound_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#exp-five-div-log-bound-lt).

## Bounds for $\sigma(n)/n$ over primes avoiding $p_j$

For $\ell \ge 1$ let $p_\ell$ be the
$\ell$-th prime, so that $p_1 = 2$. Let $1 \le j \le k$, let $q_1 < \cdots < q_k$ be primes
different from $p_j$, let $\alpha_1, \dots, \alpha_k \ge 1$, and put
$n = \prod_{i=1}^k q_i^{\alpha_i}$. Let $\sigma(n)$ be the sum of the divisors of $n$ and let
$\varphi$ be Euler's totient function. Then

$$
\frac{\sigma(n)}{n} < \prod_{i=1}^k \frac{q_i}{q_i - 1} = \frac{n}{\varphi(n)} \le
\prod_{1 \le \ell \le k + 1,\ \ell \ne j} \frac{p_\ell}{p_\ell - 1}.
$$

The paper prints the last inequality as strict; it is an equality when the $q_i$ are exactly the
first $k$ primes other than $p_j$ (for example $j = k = 1$ and $n = 3$, where both sides are
$3/2$), and the proof ($p_i \le q_i$) gives $\le$.

## Sources

- Idris Assani, Aiden Chester, and Alex Paschal, *On Robin's Inequality and the Kaneko-Lagarias Inequality*, INTEGERS 26 (2026), Article A86, Lemma 1.

Stated but not proved: `MetaMathlibExt.sigma_div_lt_totient_ratio_le_prod_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RobinKanekoLagariasWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html#sigma-div-lt-totient-ratio-le-prod-prime).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Robin's inequality](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/robin-s-inequality)
