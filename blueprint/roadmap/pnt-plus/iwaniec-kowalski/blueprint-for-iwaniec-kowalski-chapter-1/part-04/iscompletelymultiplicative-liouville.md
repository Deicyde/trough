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

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
