---
declaration: theorem
origin: cited
lean: ArithmeticFunction.isCompletelyMultiplicative_liouville
statement: formalized
---

# isCompletelyMultiplicative liouville

The Liouville function is completely multiplicative.

## Depends on

- [liouville](liouville.md)
- [IsCompletelyMultiplicative](iscompletelymultiplicative.md)

## Proof

The Liouville function $\lambda(n)$ is defined as $(-1)^{\Omega(n)}$, where $\Omega(n)$ counts the total number of prime factors of $n$ with multiplicity. To show that $\lambda$ is completely multiplicative, we need to verify that $\lambda(1) = 1$ and that $\lambda(ab) = \lambda(a)\lambda(b)$ for all natural numbers $a$ and $b$.

## Lean

Stated as [`ArithmeticFunction.isCompletelyMultiplicative_liouville`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.isCompletelyMultiplicative_liouville); the blueprint marks no proof of it as formalized.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
