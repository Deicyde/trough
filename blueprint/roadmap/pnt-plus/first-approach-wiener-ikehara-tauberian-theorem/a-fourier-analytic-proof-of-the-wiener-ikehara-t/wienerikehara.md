---
declaration: corollary
origin: cited
lean: WienerIkeharaTheorem'
statement: formalized
proof: formalized
---

# Wiener-Ikehara Theorem (1)

We have

$$
\sum_{n\leq x} f(n) = A x + o(x).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Wiener-Ikehara in an interval](wienerikeharainterval.md)

## Proof

Apply the preceding proposition with $I = [\varepsilon,1]$ and then send $\varepsilon$ to zero (using [(1)](README.md) to control the error).

## Lean

Formalized as [`WienerIkeharaTheorem'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/WienerIkeharaTheorem').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
