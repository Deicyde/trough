---
declaration: lemma
origin: cited
lean: Exchangeability.DeFinetti.ViaMartingale.finite_product_formula
statement: formalized
---

# Finite product formula

Under contractability, for every strictly monotone selection $k : \mathrm{Fin}\,m \to \mathbb{N}$ and any kernel $\nu$ satisfying the per-coordinate bridge [Conditional law of $X_n$ equals directing measure](lem-conditional-law-eq-directingmeasure.md):

$$
\mathrm{Measure.map}\,(\omega \mapsto (i \mapsto X_{k\,i}(\omega)))\,\mu
\,=\, \mu.\mathrm{bind}\,(\omega \mapsto \mathrm{Measure.pi}\,(\lambda\, i,\, \nu(\omega))).
$$

This is the martingale route's analogue of the L²/Koopman [Conditional independence extension](../../common-ending/comparing-the-two-endings/thm-condindep-extension.md): it bundles the rectangle $\pi$-system extension and the $\mathrm{Measure.map} = \mathrm{bind}$ identification into one step driven by per-coordinate conditional expectations.

## Depends on

- [Finite level factorization](lem-finite-level-factorization.md)
- [Tail factorization from future](lem-tail-factorization.md)
- [Conditional law of $X_n$ equals directing measure](lem-conditional-law-eq-directingmeasure.md)

## Lean

Stated as [`Exchangeability.DeFinetti.ViaMartingale.finite_product_formula`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.ViaMartingale.finite_product_formula); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 258](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L258)
