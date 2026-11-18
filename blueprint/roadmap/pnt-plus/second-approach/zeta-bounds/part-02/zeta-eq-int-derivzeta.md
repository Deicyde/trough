---
declaration: lemma
origin: cited
lean: Zeta_eq_int_derivZeta
statement: formalized
proof: formalized
---

# Zeta-eq-int-derivZeta

For any $t\ne0$ (so we don't pass through the pole), and $\sigma_1 < \sigma_2$,

$$
\int_{\sigma_1}^{\sigma_2}\zeta'(\sigma + it) dt =
\zeta(\sigma_2+it) - \zeta(\sigma_1+it).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is the fundamental theorem of calculus.

## Lean

Formalized as [`Zeta_eq_int_derivZeta`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Zeta_eq_int_derivZeta).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaBounds.lean)
