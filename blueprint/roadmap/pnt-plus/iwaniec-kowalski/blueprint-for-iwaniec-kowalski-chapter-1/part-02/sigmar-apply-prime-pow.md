---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sigmaR_apply_prime_pow
statement: formalized
proof: formalized
---

# sigmaR-apply-prime-pow

For a prime power, we have that $\sigma^R_s(p^i)=\sum_{j=0}^ip^{js}$.

## Depends on

- [sigmaR](../part-01/sigmar.md)

## Proof depends on

- [sigmaR-apply](sigmar-apply.md)

## Proof

Note that $d\mid p^i$ implies that $d=p^j$ with $0\leq j\leq i$. Thus,

$$
\sigma^R_s(p^i)=\sum_{d\mid p^i}d^s=\sum_{j=0}^i(p^j)^s=\sum_{j=0}^ip^{js}.
$$

## Lean

Formalized as [`ArithmeticFunction.sigmaR_apply_prime_pow`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sigmaR_apply_prime_pow).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
