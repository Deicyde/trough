---
declaration: section
origin: cited
lean: MetaMathlibExt.arithmeticDerivative, MetaMathlibExt.arithmeticDerivative_zero, MetaMathlibExt.arithmeticDerivative_one, MetaMathlibExt.arithmeticDerivative_prime, MetaMathlibExt.arithmeticDerivative_eq_sum_of_subset, MetaMathlibExt.arithmeticDerivative_mul
statement: formalized
proof: formalized
---

# Arithmetic derivative

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html).

## Arithmetic derivative

For a natural number $n$, the arithmetic derivative of $n$ is

$$D(n) = \sum_{p} \nu_p(n) \cdot \frac{n}{p},$$

where the sum runs over the prime factors $p$ of $n$ and $\nu_p(n)$ is the exponent of $p$ in
the prime factorization of $n$. Since $0$ and $1$ have no prime factors, $D(0) = D(1) = 0$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2, equation (2).

Formalized by `MetaMathlibExt.arithmeticDerivative`, a definition declared in [MathlibExt/NumberTheory/ArithmeticDerivative.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticDerivative.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html#arithmetic-derivative).

## Arithmetic derivative of zero

The arithmetic derivative of $0$ is $0$: $D(0) = 0$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2.

Formalized by `MetaMathlibExt.arithmeticDerivative_zero`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticDerivative.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticDerivative.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html#arithmetic-derivative-zero).

## Arithmetic derivative of one

The arithmetic derivative of $1$ is $0$: $D(1) = 0$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2.

Formalized by `MetaMathlibExt.arithmeticDerivative_one`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticDerivative.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticDerivative.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html#arithmetic-derivative-one).

## Arithmetic derivative of a prime

For every prime $p$, the arithmetic derivative of $p$
is $1$: $D(p) = 1$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2.

Formalized by `MetaMathlibExt.arithmeticDerivative_prime`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticDerivative.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticDerivative.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html#arithmetic-derivative-prime).

## Arithmetic derivative over a superset of the prime factors

Let $n$ be a natural number
and let $s$ be a finite set of natural numbers containing every prime factor of $n$. Then the
arithmetic derivative of $n$ is $D(n) = \sum_{p \in s} \nu_p(n) \cdot (n / p)$, where $\nu_p(n)$
is the exponent of $p$ in the prime factorization of $n$ (zero when $p$ is not a prime factor
of $n$) and $n / p$ is division in the natural numbers, rounded down.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2, equation (2).

Formalized by `MetaMathlibExt.arithmeticDerivative_eq_sum_of_subset`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticDerivative.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticDerivative.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html#arithmetic-derivative-eq-sum-of-subset).

## Leibniz rule for the arithmetic derivative

For all natural numbers $m$ and $n$, the
arithmetic derivative $D$ satisfies $D(mn) = D(m)\,n + m\,D(n)$.

## Sources

- Zachary P. Bradshaw, *On a Family of Solutions to Arithmetic Differential Equations Involving the Collatz Map*, Journal of Integer Sequences 28 (2025), Article 25.1.8, Section 2, equation (1).

Formalized by `MetaMathlibExt.arithmeticDerivative_mul`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticDerivative.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticDerivative.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html#arithmetic-derivative-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic derivative](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/arithmetic-derivative)
