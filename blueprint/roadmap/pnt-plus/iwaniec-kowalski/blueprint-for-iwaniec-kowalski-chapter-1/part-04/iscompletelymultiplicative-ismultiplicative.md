---
declaration: theorem
origin: cited
lean: ArithmeticFunction.IsCompletelyMultiplicative.isMultiplicative
statement: formalized
proof: formalized
---

# IsCompletelyMultiplicative.isMultiplicative

A function that is completely multiplicative is also multiplicative.

## Depends on

- [IsCompletelyMultiplicative](iscompletelymultiplicative.md)

## Proof

Let $f$ be a completely multiplicative function. To show that $f$ is multiplicative, we need to verify that $f(1) = 1$ and that $f(ab) = f(a)f(b)$ for all coprime natural numbers $a$ and $b$. Since $f$ is completely multiplicative, we have $f(1) = 1$ by definition. For coprime $a$ and $b$, we can write $ab$ as a product of prime factors, and since $f$ is completely multiplicative, it will factor as the product of the values of $f$ at those prime factors. This means that $f(ab) = f(a)f(b)$ for coprime $a$ and $b$, which shows that $f$ is multiplicative.

## Lean

Formalized as [`ArithmeticFunction.IsCompletelyMultiplicative.isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.IsCompletelyMultiplicative.isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
