---
declaration: proposition
origin: cited
lean: WienerIkeharaInterval
statement: formalized
proof: formalized
---

# Wiener-Ikehara in an interval

For any closed interval $I \subset (0,+\infty)$, we have

$$
\sum_{n=1}^\infty f(n) 1_I( \frac{n}{x} ) = A x |I|  + o(x).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Smoothed Wiener-Ikehara](wienerikeharasmooth.md)

## Proof

Use Lemma [Smooth Urysohn lemma](smooth-ury.md) to bound $1_I$ above and below by smooth compactly supported functions whose integral is close to the measure of $|I|$, and use the non-negativity of $f$.

## Lean

Formalized as [`WienerIkeharaInterval`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/WienerIkeharaInterval).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/Wiener.lean)
