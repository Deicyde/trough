---
declaration: section
origin: cited
lean: MetaMathlibExt.calzado_sum_inv_totient_fifth_to_half_tendsto, MetaMathlibExt.calzado_sum_inv_totient_near_sqrt_isBigO, MetaMathlibExt.calzado_sieve_euler_product_asymp, MetaMathlibExt.calzado_shifted_primes_sifted_multiple_le, MetaMathlibExt.calzado_shifted_primes_sifted_asymp, MetaMathlibExt.calzado_shifted_primes_sifted_multiple_le_sifted, MetaMathlibExt.calzado_selberg_upper_bound_sieve, MetaMathlibExt.calzado_linear_sieve
statement: formalized
---

# Sieving shifted primes and the parity problem

9 results, 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html).

## Reciprocal totients of the primes between $x^{1/5}$ and $x^{1/2}$

As the real number $x$
tends to infinity, the sum of $1/\varphi(p)$ over the primes $p$ with $x^{1/5} < p \le x^{1/2}$
tends to $\log(5/2)$, where $\varphi$ is Euler's totient function.

The paper prints the limit as $0.916\ldots$; the exact value $\log(5/2) = 0.91629\ldots$ is
forced by Mertens' theorem.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 1.

Stated but not proved: `MetaMathlibExt.calzado_sum_inv_totient_fifth_to_half_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-sum-inv-totient-fifth-to-half-te).

## Reciprocal totients of the primes just below $x^{1/2}$

For every real $B > 0$ there is a
constant $C$ such that for all sufficiently large real $x$, the sum of $1/\varphi(p)$ over the
primes $p$ with $x^{1/2} (\log x)^{-B} < p \le x^{1/2}$ is at most $C \log\log x / \log x$, where
$\varphi$ is Euler's totient function.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 1.

Stated but not proved: `MetaMathlibExt.calzado_sum_inv_totient_near_sqrt_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-sum-inv-totient-near-sqrt-is-big).

## Size of the Euler product of a sieve of dimension $k$

Let $P$ be a set of primes, $k > 0$
a real number, and $\omega$ a real-valued function on the natural numbers with
$0 \le \omega(p) < p$ for $p \in P$. Suppose there is a constant $C_0$ with
$|\sum_{p \in P,\ t \le p < z} \omega(p) \log p / p - k \log(z/t)| \le C_0$ for all real $t$ and
$z$ with $2 \le t \le z$. Then there are constants $c > 0$ and $C > 0$ such that for every real
$z \ge 2$, $c / (\log z)^k \le \prod_{p \in P,\ p < z} (1 - \omega(p)/p) \le C / (\log z)^k$.

The constants depend on $\omega$ and $P$, not only on $k$.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 3.

Stated but not proved: `MetaMathlibExt.calzado_sieve_euler_product_asymp` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-sieve-euler-product-asymp).

## Upper bound for sifted shifted primes divisible by a large prime

Let $a$ be a nonzero
even integer. For real $x$ and a prime $\ell$ let $S_\ell(x)$ be the number of primes $n \le x$
such that $\ell$ divides $n + a$ and no prime $q < x^{1/5}$ divides $n + a$. There is a constant
$C$ such that for all sufficiently large $x$ and every prime $\ell$ with
$x^{1/5} < \ell \le x^{1/2}$, $S_\ell(x) \le C x / (\varphi(\ell) (\log x)^2)$, where $\varphi$ is
Euler's totient function.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 4.

Stated but not proved: `MetaMathlibExt.calzado_shifted_primes_sifted_multiple_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-shifted-primes-sifted-multiple-l).

## Order of magnitude of the sifted shifted primes

Let $a$ be a nonzero even integer, and
for real $x$ let $S(x)$ be the number of primes $n \le x$ such that no prime $q < x^{1/5}$ divides
$n + a$. There are constants $0 < C_1 < C_2$ such that
$C_1 x / (\log x)^2 < S(x) < C_2 x / (\log x)^2$ for all sufficiently large $x$.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 6.

Stated but not proved: `MetaMathlibExt.calzado_shifted_primes_sifted_asymp` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-shifted-primes-sifted-asymp).

## Relative bound for sifted shifted primes divisible by a large prime

Let $a$ be a nonzero
even integer. For real $x$ let $S(x)$ be the number of primes $n \le x$ such that no prime
$q < x^{1/5}$ divides $n + a$, and for a prime $\ell$ let $S_\ell(x)$ be the number of those $n$
for which moreover $\ell$ divides $n + a$. There is a constant $C$ such that for all sufficiently
large $x$ and every prime $\ell$ with $x^{1/5} < \ell \le x^{1/2}$,
$S_\ell(x) \le C S(x) / \varphi(\ell)$, where $\varphi$ is Euler's totient function.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 6.

Stated but not proved: `MetaMathlibExt.calzado_shifted_primes_sifted_multiple_le_sifted` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-shifted-primes-sifted-multiple-l-2).

## Selberg's upper bound sieve

For all real numbers $\kappa > 0$ and $C_0$ there is a
constant $C$ with the following property. Let $P$ be a set of primes, $\omega$ a non-negative
multiplicative arithmetic function with $\omega(p) < p$ for $p \in P$, $A$ a finite multiset of
positive integers, and $X > 0$ and $z \ge 2$ real numbers such that
$|\sum_{p \in P,\ t \le p < z} \omega(p) \log p / p - \kappa \log(z/t)| \le C_0$ for every real
$t$ with $2 \le t \le z$. Write $P(z) = \prod_{p \in P,\ p < z} p$, let $S$ be the number of
elements of $A$ coprime to $P(z)$ and $\#A_d$ the number of elements of $A$ divisible by $d$, both
counted with multiplicity, and let $\nu(d)$ be the number of distinct prime factors of $d$. Then
$S \le X e^{\gamma\kappa} \Gamma(\kappa + 1) \prod_{p \in P,\ p < z} (1 - \omega(p)/p)
(1 + C / \log z) + \sum_{d \mid P(z),\ d < z^2} 3^{\nu(d)} |\#A_d - \omega(d) X / d|$,
where $\gamma$ is the Euler–Mascheroni constant.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 2.

Stated but not proved: `MetaMathlibExt.calzado_selberg_upper_bound_sieve` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-selberg-upper-bound-sieve).

## Rosser–Iwaniec linear sieve

Let $\gamma$ be the Euler–Mascheroni constant, $C_0$ a real
number, and $F, f \colon \mathbb{R} \to \mathbb{R}$ functions continuous on $(0, \infty)$ with
$F(s) = 2e^{\gamma}/s$ for $0 < s \le 3$ and $f(s) = 0$ for $0 < s \le 2$, such that
$u \mapsto uF(u)$ has derivative $f(s - 1)$ at every $s > 3$ and $u \mapsto uf(u)$ has derivative
$F(s - 1)$ at every $s > 2$. Then $f(s) = 2e^{\gamma}\log(s - 1)/s$ for $2 \le s \le 4$, and there
is a constant $C > 0$ with the following property. Let $P$ be a set of primes, $\omega$ a
non-negative multiplicative arithmetic function with $\omega(p) < p$ for $p \in P$, $A$ a finite
multiset of positive integers, and $X > 0$ and $2 \le z \le y$ real numbers such that
$\sum_{p \in P,\ t \le p < z} \omega(p) \log p / p \le \log(z/t) + C_0$ for every real $t$ with
$2 \le t \le z$. Write $P(z) = \prod_{p \in P,\ p < z} p$,
$V(z) = \prod_{p \in P,\ p < z} (1 - \omega(p)/p)$ and $s = \log y / \log z$; let $S$ be the number
of elements of $A$ coprime to $P(z)$ and $\#A_d$ the number of elements of $A$ divisible by $d$,
both counted with multiplicity; and let
$R = \sum_{d \mid P(z),\ d < y} |\#A_d - \omega(d) X / d|$. Then
$S \le X V(z) (F(s) + C e^{-s} (\log y)^{-1/3}) + R$ and
$X V(z) (f(s) - C e^{-s} (\log y)^{-1/3}) - R \le S$.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Lemma 5.

Stated but not proved: `MetaMathlibExt.calzado_linear_sieve` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-linear-sieve).

## Lower bound for primes $n$ with $n + a$ prime, up to a sieve error

Let $a$ be a nonzero
even integer, and call a prime $n$ admissible at level $x$ if no prime $q < x^{1/5}$ divides
$n + a$. For a prime $p$ and real $x$ let
$\bar\Delta_p(x) = \#\{n \le x \text{ admissible} : n \equiv -a \pmod p\} -
\#\{n \le x \text{ admissible} : \gcd(n, p) = 1\} / \varphi(p)$, where $\varphi$ is Euler's
totient function. There is $C > 0$ such that for every real $B > 0$ and all sufficiently large
real $x$, the number of primes $n \le x$ with $n + a > 0$ and $n + a$ prime is at least
$C x / (\log x)^2 - \sum_p \bar\Delta_p(x)$, the sum running over the primes $p$ with
$x^{1/5} < p \le x^{1/2} (\log x)^{-B}$.

## Sources

- Angel Calzado, *A Bombieri-Vinogradov Result to Address the Parity Problem*, INTEGERS 26 (2026), Article A117, Theorem 2.

Stated but not proved: `MetaMathlibExt.calzado_shifted_primes_prime_count_lower` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimeCounting/CalzadoParitySieveWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html#calzado-shifted-primes-prime-count-lower).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sieving shifted primes and the parity problem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/sieve-methods/sieving-shifted-primes-and-the-parity-problem)
