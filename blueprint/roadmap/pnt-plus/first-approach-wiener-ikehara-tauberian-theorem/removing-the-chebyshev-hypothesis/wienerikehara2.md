---
declaration: theorem
origin: cited
lean: WienerIkeharaTheorem''
statement: formalized
proof: formalized
---

# Wiener-Ikehara Theorem (2)

We have

$$
\sum_{n\leq x} f(n) = A x + o(x).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [auto-cheby](auto-cheby.md)
- [Wiener-Ikehara Theorem (1)](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/wienerikehara.md)

## Proof

Use Corollary [auto-cheby](auto-cheby.md) to remove the Chebyshev hypothesis in Theorem [Wiener-Ikehara Theorem (1)](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/wienerikehara.md).

## Lean

Formalized as [`WienerIkeharaTheorem''`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/WienerIkeharaTheorem'').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
