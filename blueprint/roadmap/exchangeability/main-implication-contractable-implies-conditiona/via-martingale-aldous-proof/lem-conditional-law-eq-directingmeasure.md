---
declaration: lemma
origin: cited
lean: Exchangeability.DeFinetti.ViaMartingale.conditional_law_eq_directingMeasure
statement: formalized
---

# Conditional law of $X_n$ equals directing measure

Per-coordinate identification: for every $n$ and every Borel $B$, $(\omega \mapsto \nu(\omega)(B).\mathrm{toReal}) \, =^{\mu\text{-a.e.}} \, \mathbb{E}[\mathbf{1}_B \circ X_n \mid \mathcal{T}]$. This is the bridge condition consumed by [Finite product formula](lem-finite-product-formula.md) below.

## Depends on

- [Extreme members equal on tail](lem-extreme-members-equal.md)
- [Contractable sequence](../../foundations/core-definitions/def-contractable.md)

## Lean

Stated as [`Exchangeability.DeFinetti.ViaMartingale.conditional_law_eq_directingMeasure`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.ViaMartingale.conditional_law_eq_directingMeasure); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 247](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L247)
