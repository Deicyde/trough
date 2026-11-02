---
declaration: theorem
origin: cited
lean: WeakPNT_AP
statement: formalized
proof: formalized
---

# WeakPNT-AP

If $q ≥ 1$ and $a$ is coprime to $q$, we have

$$
\sum_{n \leq x: n = a\ (q)} \Lambda(n) = \frac{x}{\varphi(q)} + o(x).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Wiener-Ikehara Theorem (2)](../removing-the-chebyshev-hypothesis/wienerikehara2.md)
- [WeakPNT-AP-prelim](weakpnt-ap-prelim.md)
- [Wiener-Ikehara Theorem (1)](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/wienerikehara.md)

## Proof

Apply Theorem [Wiener-Ikehara Theorem (1)](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/wienerikehara.md) (or Theorem [Wiener-Ikehara Theorem (2)](../removing-the-chebyshev-hypothesis/wienerikehara2.md) to avoid checking the Chebyshev condition) using Proposition [WeakPNT-AP-prelim](weakpnt-ap-prelim.md).

## Lean

Formalized as [`WeakPNT_AP`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/WeakPNT_AP).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
