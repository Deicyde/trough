---
declaration: section
origin: cited
lean: ArithmeticFunction.sigmaR, ArithmeticFunction.sigmaR_apply, ArithmeticFunction.sigmaR_apply_one, ArithmeticFunction.sigmaR_zero_apply, ArithmeticFunction.sigmaR_natCast_apply
statement: formalized
proof: formalized
---

# Divisor-power sums

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums/index.html).

## Divisor-power sum with complex exponent

For a complex number $s$, $\sigma_s$ is the
complex-valued arithmetic function with $\sigma_s(n) = \sum_{d \mid n} d^s$ for every natural
number $n \ge 1$, where $d^s$ is the complex power, and $\sigma_s(0) = 0$.

Formalized by `ArithmeticFunction.sigmaR`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums/index.html#sigma-r).

## Divisor-sum formula for the complex-exponent divisor sum

For every natural number $n$
and complex number $s$, the divisor-power sum $\sigma_s$ with complex exponent $s$ satisfies
$\sigma_s(n) = \sum_{d \mid n} d^s$, the sum running over the positive divisors $d$ of $n$; for
$n = 0$ the sum is empty, so $\sigma_s(0) = 0$.

Formalized by `ArithmeticFunction.sigmaR_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums/index.html#sigma-r-apply).

## The complex-exponent divisor sum at one

For every complex number $s$, the divisor-power
sum $\sigma_s(n) = \sum_{d \mid n} d^s$ with complex exponent $s$ satisfies $\sigma_s(1) = 1$.

Formalized by `ArithmeticFunction.sigmaR_apply_one`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums/index.html#sigma-r-apply-one).

## The complex-exponent divisor sum at exponent zero counts divisors

Let
$\sigma_s(n) = \sum_{d \mid n} d^s$ be the divisor-power sum with complex exponent $s$. For
every natural number $n$, $\sigma_0(n)$ equals the number of positive divisors of $n$, with the
convention that $0$ has no divisors, so that $\sigma_0(0) = 0$.

Formalized by `ArithmeticFunction.sigmaR_zero_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums/index.html#sigma-r-zero-apply).

## Natural exponents give the classical divisor function

For all natural numbers $k$ and
$n$, the value at $n$ of the complex-exponent divisor sum $\sum_{d \mid n} d^s$ with $s = k$
equals the natural number $\sigma_k(n) = \sum_{d \mid n} d^k$, viewed as a complex number.

Formalized by `ArithmeticFunction.sigmaR_natCast_apply`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/SigmaR.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums/index.html#sigma-r-nat-cast-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisor-power sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/divisor-power-sums)
