---
declaration: corollary
origin: cited
lean: prime_between
statement: formalized
proof: formalized
---

# prime-between

For every $\varepsilon>0$, there is a prime between $x$ and $(1+\varepsilon)x$ for all sufficiently large $x$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pi-alt](pi-alt.md)

## Proof

Use Corollary [pi-alt](pi-alt.md) to show that $\pi((1+\varepsilon)x) - \pi(x)$ goes to infinity as $x \to \infty$.

## Lean

Formalized as [`prime_between`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/prime_between).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
