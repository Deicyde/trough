---
declaration: lemma
origin: cited
lean: Exchangeability.DeFinetti.ViaMartingale.condExp_indicator_eq_of_contractable
statement: formalized
---

# Conditional expectation of indicator equals under contractability

For contractable sequences and $k \le m$: $\mathbb{E}[\mathbf{1}_{X_k \in B} \mid \mathcal{F}_m] = \mathbb{E}[\mathbf{1}_{X_m \in B} \mid \mathcal{F}_m]$ a.s.

## Depends on

- [Contractable distribution equality](lem-contractable-dist-eq.md)
- [Future filtration](../../foundations/sigma-algebra-infrastructure/def-futurefiltration.md)

## Lean

Stated as [`Exchangeability.DeFinetti.ViaMartingale.condExp_indicator_eq_of_contractable`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.ViaMartingale.condExp_indicator_eq_of_contractable); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 163](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L163)
