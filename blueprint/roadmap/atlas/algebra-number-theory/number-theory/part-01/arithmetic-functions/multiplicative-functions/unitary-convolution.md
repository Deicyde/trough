---
declaration: section
origin: cited
lean: Nat.unitaryDivisors_prime_pow, Nat.mul_mem_unitaryDivisors_mul, Nat.gcd_mem_unitaryDivisors_of_mem_mul, MetaMathlibExt.powOmega, MetaMathlibExt.powOmega_apply, MetaMathlibExt.powOmega_one, MetaMathlibExt.powOmega_prime_pow, MetaMathlibExt.isCompletelyMultiplicative_powOmega
statement: formalized
proof: formalized
---

# Unitary convolution

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html).

## Unitary divisors of a prime power

For every prime $p$ and every natural number $m$, the
unitary divisors of $p^m$, that is, the divisors $d$ of $p^m$ with $\gcd(d, p^m/d) = 1$, are
exactly $1$ and $p^m$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `Nat.unitaryDivisors_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#unitary-divisors-prime-pow).

## Products of unitary divisors of coprime numbers

Let $m$ and $n$ be coprime natural
numbers. If $a$ is a unitary divisor of $m$ and $b$ is a unitary divisor of $n$, then $ab$ is a
unitary divisor of $mn$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `Nat.mul_mem_unitaryDivisors_mul`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#mul-mem-unitary-divisors-mul).

## Gcd with a coprime factor preserves unitary divisors

Let $m$ and $n$ be coprime natural
numbers. If $d$ is a unitary divisor of $mn$, then $\gcd(d, m)$ is a unitary divisor of $m$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `Nat.gcd_mem_unitaryDivisors_of_mem_mul`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#gcd-mem-unitary-divisors-of-mem-mul).

## The arithmetic function $c^{\Omega}$

Let $R$ be a monoid with zero and let $c \in R$. This
is the arithmetic function $c^{\Omega}$ with values in $R$ given by $c^{\Omega}(0) = 0$ and
$c^{\Omega}(n) = c^{\Omega(n)}$ for $n \ge 1$, where $\Omega(n)$ is the number of prime factors of
$n$ counted with multiplicity. It is completely multiplicative.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 2.

Formalized by `MetaMathlibExt.powOmega`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#pow-omega).

## Value of $c^{\Omega}$ at a positive integer

Let $R$ be a monoid with zero, let $c \in R$,
and let $c^{\Omega}$ be the arithmetic function with values in $R$ that is $0$ at $0$ and
$c^{\Omega(n)}$ at each $n \ge 1$, where $\Omega(n)$ is the number of prime factors of $n$ counted
with multiplicity. For every natural number $n \ne 0$, its value at $n$ is $c^{\Omega(n)}$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 2.

Formalized by `MetaMathlibExt.powOmega_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#pow-omega-apply).

## Value of $c^{\Omega}$ at $1$

Let $R$ be a monoid with zero, let $c \in R$, and let
$c^{\Omega}$ be the arithmetic function with values in $R$ that is $0$ at $0$ and $c^{\Omega(n)}$ at
each $n \ge 1$, where $\Omega(n)$ is the number of prime factors of $n$ counted with multiplicity.
Its value at $1$ is $1$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 2.

Formalized by `MetaMathlibExt.powOmega_one`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#pow-omega-one).

## Value of $c^{\Omega}$ at prime powers

Let $R$ be a monoid with zero, let $c \in R$, and
let $c^{\Omega}$ be the arithmetic function with values in $R$ that is $0$ at $0$ and
$c^{\Omega(n)}$ at each $n \ge 1$, where $\Omega(n)$ is the number of prime factors of $n$ counted
with multiplicity. For every prime $p$ and every natural number $m$, its value at $p^m$ is $c^m$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 2.

Formalized by `MetaMathlibExt.powOmega_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#pow-omega-prime-pow).

## Complete multiplicativity of $c^{\Omega}$

Let $R$ be a monoid with zero and $c \in R$.
Let $c^{\Omega}$ be the arithmetic function $n \mapsto c^{\Omega(n)}$ for $n \ge 1$, where
$\Omega(n)$ is the number of prime factors of $n$ counted with multiplicity. Then $c^{\Omega}$ is
completely multiplicative: for all natural numbers $m$ and $n$, its value at $mn$ is the product
of its values at $m$ and at $n$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 2.

Formalized by `MetaMathlibExt.isCompletelyMultiplicative_powOmega`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#is-completely-multiplicative-pow-omega).

## Multiplicativity of $c^{\Omega}$

Let $R$ be a monoid with zero and $c \in R$. The
arithmetic function $n \mapsto c^{\Omega(n)}$ for $n \ge 1$, where $\Omega(n)$ is the number of
prime factors of $n$ counted with multiplicity, is multiplicative.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 2.

Formalized by `MetaMathlibExt.isMultiplicative_powOmega`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#is-multiplicative-pow-omega).

## Unitary convolution

Let $R$ be a semiring. The unitary convolution of two arithmetic
functions $f$ and $g$ with values in $R$ is the arithmetic function $f \sqcup g$ given by
$(f \sqcup g)(n) = \sum_{d \parallel n} f(d)\, g(n/d)$, where the sum runs over the unitary divisors
$d$ of $n$: for $n \ge 1$ these are the divisors $d$ of $n$ with $\gcd(d, n/d) = 1$, and $0$ has
no unitary divisors. In particular $(f \sqcup g)(0) = 0$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.unitaryConv`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#unitary-conv).

## Unitary convolution as a sum over unitary divisors

Let $R$ be a semiring and let $f$ and
$g$ be arithmetic functions with values in $R$. For every natural number $n$, their unitary
convolution $f \sqcup g$ satisfies $(f \sqcup g)(n) = \sum_{d \parallel n} f(d)\, g(n/d)$, where the
sum runs over the unitary divisors $d$ of $n$: for $n \ge 1$ these are the divisors $d$ of $n$
with $\gcd(d, n/d) = 1$, and for $n = 0$ there are none, so the sum is $0$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.unitaryConv_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#unitary-conv-apply).

## Unitary convolution at $1$

Let $R$ be a semiring and let $f$ and $g$ be arithmetic
functions with values in $R$. Their unitary convolution $f \sqcup g$, defined by
$(f \sqcup g)(n) = \sum_{d \parallel n} f(d)\, g(n/d)$ over the unitary divisors $d$ of $n$,
satisfies $(f \sqcup g)(1) = f(1)\, g(1)$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.unitaryConv_one`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#unitary-conv-one).

## Unitary convolution at prime powers

Let $R$ be a semiring and let $f$ and $g$ be
arithmetic functions with values in $R$. For every prime $p$ and every natural number $m \ge 1$,
their unitary convolution $f \sqcup g$ satisfies
$(f \sqcup g)(p^m) = f(1)\, g(p^m) + f(p^m)\, g(1)$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.unitaryConv_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#unitary-conv-prime-pow).

## The unitary convolution of multiplicative functions is multiplicative

Let $R$ be a
commutative semiring. If $f$ and $g$ are multiplicative arithmetic functions with values in $R$,
then their unitary convolution $f \sqcup g$, given by $(f \sqcup g)(n) = \sum_{d} f(d)\, g(n/d)$
with $d$ running over the unitary divisors of $n$, is multiplicative.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3 (`(𝓜, ⊔)` is a group).

Formalized by `MetaMathlibExt.isMultiplicative_unitaryConv`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#is-multiplicative-unitary-conv).

## Multiplicative function with prescribed values at prime powers

Let $R$ be a commutative
monoid with zero and let $g : \mathbb{N} \to R$. This is the arithmetic function $f$ with values
in $R$ given by $f(0) = 0$ and $f(n) = \prod_{p \mid n} g(v_p(n))$ for $n \ge 1$, where the product
runs over the primes $p$ dividing $n$ and $v_p(n)$ is the exponent of $p$ in $n$. It is
multiplicative, it takes the value $g(m)$ at every prime power $p^m$ with $m \ge 1$, and its value
at $1$ is the empty product $1$, so $g(0)$ never enters.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3 (a multiplicative function is determined by its values at the prime powers).

Formalized by `MetaMathlibExt.multiplicativeOfPrimePowers`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#multiplicative-of-prime-powers).

## Value of the function with prescribed prime-power values

Let $R$ be a commutative monoid
with zero, let $g : \mathbb{N} \to R$, and let $n \ne 0$ be a natural number. The multiplicative
function with value $g(m)$ at every prime power $p^m$ with $m \ge 1$ takes the value
$\prod_{q \mid n} g(v_q(n))$ at $n$, where $q$ runs over the primes dividing $n$ and $v_q(n)$ is
the exponent of $q$ in the factorization of $n$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.multiplicativeOfPrimePowers_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#multiplicative-of-prime-powers-apply).

## The function with prescribed prime-power values is $1$ at $1$

Let $R$ be a commutative
monoid with zero and $g : \mathbb{N} \to R$. The multiplicative function with prime-power values
$g$, given by $n \mapsto \prod_{q \mid n} g(v_q(n))$ for $n \ge 1$ (with $q$ running over the
primes dividing $n$ and $v_q(n)$ the exponent of $q$ in $n$), takes the value $1$ at $n = 1$,
whatever $g(0)$ is.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.multiplicativeOfPrimePowers_one`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#multiplicative-of-prime-powers-one).

## The function with prescribed prime-power values at a prime power

Let $R$ be a
commutative monoid with zero and $g : \mathbb{N} \to R$. For every prime $p$ and every $m \ge 1$,
the multiplicative function with prime-power values $g$, given by
$n \mapsto \prod_{q \mid n} g(v_q(n))$ for $n \ge 1$ (with $q$ running over the primes dividing
$n$ and $v_q(n)$ the exponent of $q$ in $n$), takes the value $g(m)$ at $p^m$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.multiplicativeOfPrimePowers_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#multiplicative-of-prime-powers-prime-pow).

## Multiplicativity of the function with prescribed prime-power values

Let $R$ be a
commutative monoid with zero and $g : \mathbb{N} \to R$. The arithmetic function
$n \mapsto \prod_{q \mid n} g(v_q(n))$ for $n \ge 1$, where $q$ runs over the primes dividing $n$
and $v_q(n)$ is the exponent of $q$ in $n$, is multiplicative.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3.

Formalized by `MetaMathlibExt.isMultiplicative_multiplicativeOfPrimePowers`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#is-multiplicative-multiplicative-of-prim).

## A multiplicative function with prescribed prime-power values

Let $R$ be a
commutative monoid with zero, let $g : \mathbb{N} \to R$, and let $f$ be a multiplicative
arithmetic function with values in $R$. If $f(p^m) = g(m)$ for every prime $p$ and every
$m \ge 1$, then $f$ is the multiplicative function with prime-power values $g$, that is, the
arithmetic function $n \mapsto \prod_{q \mid n} g(v_q(n))$ for $n \ge 1$, where $q$ runs over the
primes dividing $n$ and $v_q(n)$ is the exponent of $q$ in $n$.

## Sources

- Emil Daniel Schwab, *Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution*, Journal of Integer Sequences 28 (2025), Article 25.1.7, Section 1.3 (a multiplicative function is determined by its values at the prime powers).

Formalized by `MetaMathlibExt.eq_multiplicativeOfPrimePowers`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/UnitaryConvolution.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html#eq-multiplicative-of-prime-powers).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unitary convolution](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/unitary-convolution)
