---
declaration: section
origin: cited
lean: ArithmeticFunction.jordanTotient, ArithmeticFunction.jordanTotient_zero, ArithmeticFunction.jordanTotient_apply_one, ArithmeticFunction.jordanTotient_eq_prod_factorization, ArithmeticFunction.jordanTotient_prime_pow, ArithmeticFunction.jordanTotient_prime, ArithmeticFunction.isMultiplicative_jordanTotient, ArithmeticFunction.jordanTotient_one_apply
statement: formalized
proof: formalized
---

# Jordan's totient function

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html).

## Jordan's totient function

For a natural number $k$, Jordan's totient function $J_k$ is
the arithmetic function with natural-number values given by $J_k(0) = 0$ and, for $n \ne 0$,

$$J_k(n) = \prod_{p \mid n} p^{k(v_p(n) - 1)} (p^k - 1),$$

where the product runs over the prime divisors $p$ of $n$ and $v_p(n)$ is the exponent of $p$
in the prime factorization of $n$.

For $k \ge 1$ and $n \ge 1$ this equals $n^k \prod_{p \mid n} (1 - p^{-k})$, the form in which the
function is usually defined.

## Sources

- Yuan He, *On the mean values of products of Dirichlet L-functions at positive integers*, arXiv:2310.18048v3, equation (1.7).

Formalized by `ArithmeticFunction.jordanTotient`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient).

## Jordan's totient at zero

For every natural number $k$, the Jordan totient function
satisfies $J_k(0) = 0$; this is the convention extending $J_k$ to $0$.

Formalized by `ArithmeticFunction.jordanTotient_zero`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-zero).

## Jordan's totient at one

For every natural number $k$, the Jordan totient function
satisfies $J_k(1) = 1$.

Formalized by `ArithmeticFunction.jordanTotient_apply_one`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-apply-one).

## Prime-factorization formula for Jordan's totient

For all natural numbers $k$ and
$n \neq 0$, the Jordan totient function satisfies

$$J_k(n) = \prod_{p \mid n} p^{k(v_p(n) - 1)} (p^k - 1),$$

where the product runs over the distinct primes $p$ dividing $n$ and $v_p(n)$ is the exponent of
$p$ in the prime factorization of $n$.

## Sources

- Yuan He, arXiv:2310.18048v3, equation (1.7), in integral form.

Formalized by `ArithmeticFunction.jordanTotient_eq_prod_factorization`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-eq-prod-factorization).

## Jordan's totient at prime powers

For every natural number $k$, every prime $p$ and every
integer $e \ge 1$, the Jordan totient function satisfies $J_k(p^e) = p^{k(e-1)}(p^k - 1)$.

Formalized by `ArithmeticFunction.jordanTotient_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-prime-pow).

## Jordan's totient at primes

For every natural number $k$ and every prime $p$, the Jordan
totient function satisfies $J_k(p) = p^k - 1$.

Formalized by `ArithmeticFunction.jordanTotient_prime`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-prime).

## Jordan's totient function is multiplicative

For every natural number $k$, the Jordan
totient function $J_k$ is multiplicative: $J_k(1) = 1$, and $J_k(mn) = J_k(m) J_k(n)$ for all
coprime natural numbers $m$ and $n$.

Formalized by `ArithmeticFunction.isMultiplicative_jordanTotient`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#is-multiplicative-jordan-totient).

## Jordan's totient of order one is Euler's totient

For every natural number $n$,
$J_1(n) = \varphi(n)$, where $J_1$ is the Jordan totient function $J_k$ with $k = 1$ and
$\varphi$ is Euler's totient function; at $n = 0$ both sides are $0$.

## Sources

- Yuan He, arXiv:2310.18048v3, equation (1.7).

Formalized by `ArithmeticFunction.jordanTotient_one_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-one-apply).

## Möbius sum for Jordan's totient

For all natural numbers $k$ and $n \neq 0$, the Jordan
totient function satisfies, as an identity of integers,

$$J_k(n) = \sum_{d \mid n} \mu(n/d)\, d^k,$$

where $d$ runs over the positive divisors of $n$ and $\mu$ is the Möbius function.

## Sources

- Yuan He, arXiv:2310.18048v3, equation (2.7), stated there for positive k; here k = 0 is also allowed.

Formalized by `ArithmeticFunction.jordanTotient_eq_sum_moebius`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-eq-sum-moebius).

## Cleared-denominator Euler product for Jordan's totient

For all natural numbers $k$ and
$n \neq 0$, the Jordan totient function satisfies

$$J_k(n) \prod_{p \mid n} p^k = n^k \prod_{p \mid n} (p^k - 1),$$

where both products run over the distinct primes $p$ dividing $n$.

## Sources

- Yuan He, arXiv:2310.18048v3, equation (1.7), with denominators cleared.

Formalized by `ArithmeticFunction.jordanTotient_mul_prod_primeFactors_pow`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-mul-prod-prime-factors-po).

## Euler product for Jordan's totient

For all natural numbers $k$ and $n \neq 0$, the Jordan
totient function satisfies, as an identity of rational numbers,

$$J_k(n) = n^k \prod_{p \mid n} \left(1 - \frac{1}{p^k}\right),$$

where the product runs over the distinct primes $p$ dividing $n$.

## Sources

- Yuan He, arXiv:2310.18048v3, equation (1.7), stated there for positive k; here k = 0 is also allowed.

Formalized by `ArithmeticFunction.jordanTotient_eq_rational_prod`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/JordanTotient.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html#jordan-totient-eq-rational-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jordan's totient function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/jordan-s-totient-function)
