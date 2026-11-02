---
declaration: theorem
origin: cited
lean: chebyshev_asymptotic
statement: formalized
proof: formalized
---

# chebyshev-asymptotic

One has

$$
\sum_{p \leq x} \log p = x + o(x).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [WeakPNT](../first-approach-wiener-ikehara-tauberian-theorem/weak-pnt/weakpnt.md)

## Proof

From the prime number theorem we already have

$$
\sum_{n \leq x} \Lambda(n) = x + o(x)
$$

so it suffices to show that

$$
\sum_{j \geq 2} \sum_{p^j \leq x} \log p = o(x).
$$

Only the terms with $j \leq \log x / \log 2$ contribute, and each $j$ contributes at most $\sqrt{x} \log x$ to the sum, so the left-hand side is $O( \sqrt{x} \log^2 x ) = o(x)$ as required.

## Lean

Formalized as [`chebyshev_asymptotic`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/chebyshev_asymptotic).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
