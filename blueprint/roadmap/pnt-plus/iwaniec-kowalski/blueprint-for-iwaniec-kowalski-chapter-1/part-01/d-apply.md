---
declaration: theorem
origin: cited
lean: ArithmeticFunction.d_apply
statement: formalized
proof: formalized
---

# d apply

(1.25) in Iwaniec-Kowalski: a formula for $d_k$ for all $n$.

## Depends on

- [d](d.md)

## Proof depends on

- [d apply prime pow](d-apply-prime-pow.md)
- [d isMultiplicative](d-ismultiplicative.md)

## Proof

The function $d_k$ is multiplicative, so to compute $d_k(n)$ for a general natural number $n$, we can factor $n$ into its prime power decomposition: $n = p_1^{a_1} p_2^{a_2} ... p_m^{a_m}$. Since $d_k$ is multiplicative, we have:

$$
d_k(n) = d_k(p_1^{a_1}) \cdot d_k(p_2^{a_2}) \cdot ... \cdot d_k(p_m^{a_m})
$$

Using the explicit formula for prime powers from the previous theorem, we can substitute to get:

$$
d_k(n) = \prod_{i=1}^{m} (a_i + k - 1).choose (k - 1)
$$

This gives us a complete formula for $d_k(n)$ in terms of the prime factorization of $n$.

## Lean

Formalized as [`ArithmeticFunction.d_apply`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.d_apply).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
