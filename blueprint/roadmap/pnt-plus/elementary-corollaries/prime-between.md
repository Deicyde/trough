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

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/Consequences.lean)
