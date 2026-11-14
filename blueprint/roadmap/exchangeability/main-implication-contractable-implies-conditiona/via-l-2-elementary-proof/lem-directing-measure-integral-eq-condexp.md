---
declaration: lemma
origin: cited
lean: Exchangeability.DeFinetti.ViaL2.directing_measure_integral_eq_condExp
statement: formalized
---

# Directing-measure integral equals conditional expectation

For a bounded measurable function $f$, the integral $\int f \, d\nu(\omega)$ against the directing measure equals $\mathbb{E}[f \circ X_0 \mid \mathcal{T}](\omega)$ almost everywhere. This is the shape consumed by the shared common-ending step.

## Depends on

- [Directing measure equals condExpKernel push-forward](thm-directing-measure-ae-eq-condexpkernel-map.md)

## Lean

Stated as [`Exchangeability.DeFinetti.ViaL2.directing_measure_integral_eq_condExp`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.ViaL2.directing_measure_integral_eq_condExp); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 388](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L388)
