---
declaration: theorem
origin: cited
lean: Exchangeability.DeFinetti.conditionallyIID_of_contractable_viaL2
statement: formalized
---

# Contractable implies Conditionally i.i.d. (via L$^2$)

If $(X_n)$ is contractable (and real-valued), then it is conditionally i.i.d. **Scope note:** the L$^2$ route is currently stated for real-valued sequences via the Stieltjes-based directing-measure construction; extending it to general standard Borel targets would require a measure-disintegration replacement for the Stieltjes step.

## Depends on

- [Contractable sequence](../../foundations/core-definitions/def-contractable.md)
- [Conditionally i.i.d. sequence](../../foundations/core-definitions/def-conditionallyiid.md)
- [L$^2$ contractability bound](lem-l2-bound.md)
- [Weighted sums converge in L$^1$](thm-weighted-sums-l1.md)
- [Directing measure is probability (L$^2$ version)](lem-directing-measure-isprob-l2.md)
- [Directing measure equals condExpKernel push-forward](thm-directing-measure-ae-eq-condexpkernel-map.md)
- [Directing-measure integral equals conditional expectation](lem-directing-measure-integral-eq-condexp.md)
- [Conditional independence extension](../../common-ending/comparing-the-two-endings/thm-condindep-extension.md)

## Lean

Stated as [`Exchangeability.DeFinetti.conditionallyIID_of_contractable_viaL2`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.conditionallyIID_of_contractable_viaL2); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 407](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L407)
