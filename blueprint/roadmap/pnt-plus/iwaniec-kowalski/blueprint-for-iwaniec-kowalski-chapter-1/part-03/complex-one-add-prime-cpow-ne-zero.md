---
declaration: theorem
origin: cited
lean: ArithmeticFunction.Complex.one_add_prime_cpow_ne_zero
statement: formalized
proof: formalized
---

# Complex.one-add-prime-cpow-ne-zero

For $1\lt \Re(s)$ and $p$ prime, we have that $1+p^{-s}\neq 0$. The naming convention is to mimic

```
Complex.one_sub_prime_cpow_ne_zero
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose for contradiction $1+p^{-s}=0$, then $|p^{-s}|=1$. However, this can not happen per

```
Complex.norm_prime_cpow_le_one_half
```

## Lean

Formalized as [`ArithmeticFunction.Complex.one_add_prime_cpow_ne_zero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.Complex.one_add_prime_cpow_ne_zero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
