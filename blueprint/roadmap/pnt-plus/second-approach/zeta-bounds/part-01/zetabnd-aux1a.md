---
declaration: lemma
origin: cited
lean: ZetaBnd_aux1a
statement: formalized
proof: formalized
---

# ZetaBnd-aux1a

For any $0 < a < b$ and $s \in \mathbb{C}$ with $\sigma=\Re(s)>0$,

$$
\int_a^b \left|\frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx\right|
\le \frac{a^{-\sigma}-b^{-\sigma}}{\sigma}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Apply the triangle inequality

$$
\left|\int_a^b \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx\right|
\le \int_a^b \frac{1}{x^{\sigma+1}} \, dx,
$$

and evaluate the integral.

## Lean

Formalized as [`ZetaBnd_aux1a`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaBnd_aux1a).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaBounds.lean)
