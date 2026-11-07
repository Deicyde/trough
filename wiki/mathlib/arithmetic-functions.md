An **arithmetic function** is a function defined on the positive integers, usually
with integer, real or complex values, that records some arithmetic property of its
argument: the number of divisors of $n$, the sum of those divisors, or the count of
integers up to $n$ coprime to $n$. Arithmetic functions are among the basic objects of
elementary and analytic number theory. A product on them, Dirichlet convolution,
mirrors the multiplicative structure of the integers, and through Dirichlet series
it connects divisor sums with analytic functions such as the Riemann zeta function.

## Definition

Let $R$ be a semiring; for most of this article $R$ is a commutative [ring](trough:Ring), often $\mathbb{Z}$, $\mathbb{R}$ or $\mathbb{C}$. An arithmetic function with values in $R$ is
a function $f$ from the positive integers to $R$. Mathlib formalizes this as
a function from the natural numbers to $R$ that takes the value $0$ at $0$.

Two arithmetic functions are added pointwise. Their **Dirichlet convolution** is

$$(f * g)(n) = \sum_{ab = n} f(a)\,g(b) = \sum_{d \mid n} f(d)\,g(n/d),$$

the sum of $f(a)\,g(b)$ over all factorizations $n = ab$ into positive integers.
The neutral element for convolution is the function $\varepsilon$ with
$\varepsilon(1) = 1$ and $\varepsilon(n) = 0$ for $n \neq 1$.
With these operations,
the arithmetic functions with values in $R$ form a semiring;
when $R$ is a commutative ring they form a commutative ring, the Dirichlet ring.
Over a commutative ring, $f$ has an inverse under convolution exactly when $f(1)$ is a unit of $R$.
The inverse $g$ is computed recursively from $g(1) = f(1)^{-1}$ and

$$g(n) = -f(1)^{-1} \sum_{d \mid n,\ d < n} f(n/d)\,g(d) \qquad (n > 1),$$

and this function satisfies $f * g = \varepsilon$.

An arithmetic function $f$ is **multiplicative** if
$f(1) = 1$ and $f(mn) = f(m)\,f(n)$ whenever $m$ and $n$ are coprime,
that is, whenever their [greatest common divisor](trough:GCDMonoid.gcd) is $1$.
It is completely multiplicative if $f(1) = 1$ and $f(mn) = f(m)\,f(n)$ for all $m$ and $n$.

## Examples

- The constant function $\zeta$, with $\zeta(n) = 1$ for every positive $n$, and the
  identity function $\mathrm{id}(n) = n$, which is multiplicative.
- The divisor functions $\sigma_k(n) = \sum_{d \mid n} d^k$, defined for each natural number $k$. Here
  $\sigma_0(n)$ is the number of divisors of $n$ and $\sigma_1(n)$ their sum. Writing
  $\mathrm{id}_k(n) = n^k$, one has $\sigma_k = \zeta * \mathrm{id}_k$,
  so each $\sigma_k$ is multiplicative.
- [Euler's totient function](trough:Nat.totient) $\varphi$ satisfies
  $\varphi(mn) = \varphi(m)\,\varphi(n)$ for coprime $m$ and $n$ and
  $\sum_{d \mid n} \varphi(d) = n$, that is, $\varphi * \zeta = \mathrm{id}$.
- The functions $\Omega(n)$, the number of prime factors of $n$ counted with multiplicity,
  and $\omega(n)$, the number of distinct prime factors. They turn products into sums:
  $\Omega(mn) = \Omega(m) + \Omega(n)$ for all positive $m$ and $n$,
  while $\omega(mn) = \omega(m) + \omega(n)$ for coprime $m$ and $n$.
- The Möbius function $\mu$, where
  $\mu(n) = 0$ if $n$ is divisible by the square of a prime, and otherwise $\mu(n) = (-1)^k$ with $k$ the number of prime factors of $n$.
  It is multiplicative.
- The von Mangoldt function $\Lambda$, where
  $\Lambda(n) = \log p$ if $n$ is a power $p^k$ of a prime $p$ with $k \ge 1$, and $\Lambda(n) = 0$ otherwise,
  with $\log$ the [natural logarithm](trough:Real.log). For every positive $n$,
  $\sum_{d \mid n} \Lambda(d) = \log n$.

## Properties

**Multiplicative functions.** A multiplicative function is determined by its values at
[prime](trough:Prime) powers: for $n \ge 1$ with [prime factorization](trough:Nat.primeFactorsList_unique) $n = p_1^{k_1} \cdots p_r^{k_r}$,
$f(n) = f(p_1^{k_1}) \cdots f(p_r^{k_r})$.
Hence two multiplicative functions are equal exactly when they agree at every prime power.
Over a commutative ring, the convolution of two multiplicative functions is multiplicative.
This is how one proves that $\sigma_k$ is multiplicative, and it reduces many identities
between multiplicative functions to a check at prime powers.

**Möbius inversion.** The Möbius function is the convolution inverse of $\zeta$:
$\mu * \zeta = \varepsilon$ over any ring. Unwinding the convolution,
$\sum_{d \mid n} \mu(d)$ equals $1$ for $n = 1$ and $0$ for $n > 1$. Convolving with $\mu$ or with
$\zeta$ therefore undoes the other, which gives the Möbius inversion formula: for
functions $f$ and $g$ on the positive integers with values in a ring,
$g(n) = \sum_{d \mid n} f(d)$ for every positive $n$ if and only if $f(n) = \sum_{ab = n} \mu(a)\,g(b)$ for every positive $n$.
Applied to the totient identity above it gives $\varphi(n) = \sum_{d \mid n} \mu(d)\, n/d$.
Writing $\log$ also for the arithmetic function $n \mapsto \log n$, the von Mangoldt identity reads
$\Lambda * \zeta = \log$, and inversion gives
$\Lambda = \mu * \log$.

**Dirichlet series.** To a complex-valued arithmetic function $f$ one attaches the
Dirichlet series

$$L(f, s) = \sum_{n=1}^{\infty} \frac{f(n)}{n^s}.$$

Convolution becomes multiplication: at every complex $s$ where both series converge absolutely,
$L(f * g, s) = L(f, s)\,L(g, s)$. The series of $\zeta$ is the Riemann zeta
function, so the identity $\mu * \zeta = \varepsilon$ says that the series of $\mu$ is the
reciprocal of the zeta function for real part of $s$ greater than $1$.

## Related concepts

The Dirichlet ring is an analogue of the ring of [formal power series](trough:PowerSeries): there the
coefficients of a product are summed over pairs of indices with a given sum, here over
pairs with a given product. By unique factorization, sending $n = \prod_p p^{k_p}$ to the monomial
$\prod_p x_p^{k_p}$ identifies the Dirichlet ring over a commutative ring $R$ with a ring of formal
power series over $R$ in countably many variables $x_p$, one for each prime $p$.
Dirichlet characters are completely multiplicative arithmetic functions, and their
Dirichlet series are the Dirichlet $L$-functions.

## In Mathlib

Mathlib takes the domain to be all natural numbers and forces the value at $0$ to be $0$,
so that an arithmetic function is a function on the natural numbers rather than on the
positive integers; the convolution only ever evaluates its factors at positive integers.
The values may lie in any type with a zero, and each operation asks only for the structure
it needs: pointwise addition needs an additive monoid, convolution a semiring. Standard
functions are defined with their natural codomain, $\zeta$, $\sigma_k$, $\Omega$ and $\omega$ with natural
number values, $\mu$ with integer values and $\Lambda$ with real values, and are carried into other
rings by coercion, which is why the identity $\mu * \zeta = \varepsilon$ is proved over the integers
first and then over every ring. Being multiplicative is a property of a function rather
than a separate structure. Euler's totient function is defined as a plain function on the
natural numbers rather than as an arithmetic function, so the identity $\varphi * \zeta = \mathrm{id}$
appears in Mathlib only as the divisor sum above. Dirichlet series are defined for arbitrary complex sequences,
ignoring the term at $0$, and convolution of sequences is obtained by passing through
arithmetic functions.

## Depends on

- [Natural number](trough:Nat)
- [Prime numbers](trough:Prime)
- [Greatest common divisor](trough:GCDMonoid.gcd)
- [Ring](trough:Ring)
