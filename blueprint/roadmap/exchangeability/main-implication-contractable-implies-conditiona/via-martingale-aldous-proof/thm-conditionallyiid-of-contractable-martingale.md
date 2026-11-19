---
declaration: theorem
origin: cited
lean: Exchangeability.DeFinetti.conditionallyIID_of_contractable
statement: formalized
---

# Contractable implies Conditionally i.i.d. (via Martingale)

If $(X_n)$ is contractable, then it is conditionally i.i.d. The directing kernel $\nu(\omega)(B) = \mathbb{E}[\mathbf{1}_{X_0 \in B} \mid \mathcal{T}](\omega)$ is constructed from the tail $\sigma$-algebra, identified per-coordinate by [Conditional law of $X_n$ equals directing measure](lem-conditional-law-eq-directingmeasure.md), and lifted to the joint law by [Finite product formula](lem-finite-product-formula.md) — bypassing the L²/Koopman common-ending step.

## Depends on

- [Contractable sequence](../../foundations/core-definitions/def-contractable.md)
- [Conditionally i.i.d. sequence](../../foundations/core-definitions/def-conditionallyiid.md)
- [Extreme members equal on tail](lem-extreme-members-equal.md)
- [Block coordinate conditional independence](lem-block-coord-condindep.md)
- [Directing measure is probability measure](lem-directingmeasure-isprob.md)
- [Directing measure measurability](lem-directingmeasure-measurable.md)
- [Conditional law of $X_n$ equals directing measure](lem-conditional-law-eq-directingmeasure.md)
- [Finite product formula](lem-finite-product-formula.md)

## Lean

Stated as [`Exchangeability.DeFinetti.conditionallyIID_of_contractable`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.conditionallyIID_of_contractable); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 276](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L276)
