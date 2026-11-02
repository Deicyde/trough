---
declaration: theorem
origin: cited
lean: chebyshev_asymptotic_pnt
statement: formalized
proof: formalized
---

# Prime number theorem in AP

If $a\ (q)$ is a primitive residue class, then one has

$$
\sum_{p \leq x: p = a\ (q)} \log p = \frac{x}{\phi(q)} + o(x).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [WeakPNT-AP](../../first-approach-wiener-ikehara-tauberian-theorem/the-prime-number-theorem-in-arithmetic-progressi/weakpnt-ap.md)
- [chebyshev-asymptotic](../chebyshev-asymptotic.md)

## Proof

This is a routine modification of the proof of Theorem [chebyshev-asymptotic](../chebyshev-asymptotic.md).

## Lean

Formalized as [`chebyshev_asymptotic_pnt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/chebyshev_asymptotic_pnt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
