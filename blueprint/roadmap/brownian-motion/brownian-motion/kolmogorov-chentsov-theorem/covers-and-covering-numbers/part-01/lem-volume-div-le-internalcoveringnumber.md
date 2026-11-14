---
declaration: lemma
origin: cited
lean: Metric.measure_div_le_coveringNumber
statement: formalized
proof: formalized
---

# volume_div_le_internalCoveringNumber

If $0 < \varepsilon$ then $\frac{V(A)}{V(B_\varepsilon)} \le N^{int}_\varepsilon(A)$.

## Depends on

- [Internal covering number](def-internalcoveringnumber.md)

## Proof depends on

- [volume_le_externalCoveringNumber_mul](lem-volume-le-externalcoveringnumber-mul.md)
- [externalCoveringNumber_le_internalCoveringNumber](lem-externalcoveringnumber-le-internalcoveringnu.md)

## Proof

We have $\frac{V(A)}{V(B_\varepsilon)} \le N^{ext}_\varepsilon(A)$ by Lemma [volume_le_externalCoveringNumber_mul](lem-volume-le-externalcoveringnumber-mul.md) and $N^{ext}_\varepsilon(A) \le N^{int}_\varepsilon(A)$ by Lemma [externalCoveringNumber_le_internalCoveringNumber](lem-externalcoveringnumber-le-internalcoveringnu.md).

## Lean

Formalized as [`Metric.measure_div_le_coveringNumber`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.measure_div_le_coveringNumber).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 222](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L222)
