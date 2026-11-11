---
declaration: section
origin: cited
lean: ArithmeticFunction.dedekindPsi, ArithmeticFunction.dedekindPsi_eq_prod_factorization, ArithmeticFunction.dedekindPsi_prime_pow, ArithmeticFunction.isMultiplicative_dedekindPsi, ArithmeticFunction.dedekindPsi_mul_prod_primeFactors, ArithmeticFunction.dedekindPsi_eq_rational_prod
statement: formalized
proof: formalized
---

# Dedekind psi function

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html).

## Dedekind psi function

The Dedekind psi function $\psi$ is the arithmetic function with
values in $\mathbb{N}$ given by $\psi(0) = 0$ and, for $n > 0$,

$$
\psi(n) = \prod_{p^k \parallel n} p^{k-1} (p + 1),
$$

the product running over the primes $p$ dividing $n$, with $p^k$ the exact power of $p$ dividing
$n$.

Formalized by `ArithmeticFunction.dedekindPsi`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html#dedekind-psi).

## Dedekind psi function as a product over prime powers

For every natural number $n \ne 0$,
the Dedekind psi function $\psi$ satisfies

$$
\psi(n) = \prod_{p^k \parallel n} p^{k-1} (p + 1),
$$

the product running over the primes $p$ dividing $n$, with $p^k$ the exact power of $p$ dividing
$n$.

Formalized by `ArithmeticFunction.dedekindPsi_eq_prod_factorization`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html#dedekind-psi-eq-prod-factorization).

## Dedekind psi function at prime powers

For every prime $p$ and every natural number
$k > 0$, the Dedekind psi function $\psi$ satisfies $\psi(p^k) = p^{k-1} (p + 1)$.

Formalized by `ArithmeticFunction.dedekindPsi_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html#dedekind-psi-prime-pow).

## Multiplicativity of the Dedekind psi function

The Dedekind psi function $\psi$ is
multiplicative: $\psi(1) = 1$ and $\psi(mn) = \psi(m) \psi(n)$ for all coprime natural numbers
$m$ and $n$.

Formalized by `ArithmeticFunction.isMultiplicative_dedekindPsi`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html#is-multiplicative-dedekind-psi).

## Cleared-denominator product formula for the Dedekind psi function

For every natural
number $n \ne 0$, the Dedekind psi function $\psi$ satisfies

$$
\psi(n) \prod_{p \mid n} p = n \prod_{p \mid n} (p + 1),
$$

both products running over the prime divisors $p$ of $n$.

Formalized by `ArithmeticFunction.dedekindPsi_mul_prod_primeFactors`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html#dedekind-psi-mul-prod-prime-factors).

## Product formula for the Dedekind psi function

For every natural number $n \ne 0$, the
Dedekind psi function $\psi$ satisfies, as an identity of rational numbers,

$$
\psi(n) = n \prod_{p \mid n} \Bigl(1 + \frac{1}{p}\Bigr),
$$

the product running over the prime divisors $p$ of $n$.

Formalized by `ArithmeticFunction.dedekindPsi_eq_rational_prod`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/DedekindPsi.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html#dedekind-psi-eq-rational-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dedekind psi function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/dedekind-psi-function)
