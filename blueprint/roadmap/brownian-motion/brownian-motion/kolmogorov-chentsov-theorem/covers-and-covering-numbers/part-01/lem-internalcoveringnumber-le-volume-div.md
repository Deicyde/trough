---
declaration: lemma
origin: cited
lean: Metric.coveringNumber_le_measure_div
statement: formalized
proof: formalized
---

# internalCoveringNumber_le_volume_div

If $0 < \varepsilon < \infty$ then $N^{int}_\varepsilon(A) \le \frac{V(A + B_{\varepsilon/2})}{V(B_{\varepsilon/2})}$.

## Depends on

- [Internal covering number](def-internalcoveringnumber.md)

## Proof depends on

- [packingNumber_mul_le_volume](lem-packingnumber-mul-le-volume.md)
- [internalCoveringNumber_le_packingNumber](lem-internalcoveringnumber-le-packingnumber.md)

## Proof

We have $N^{int}_\varepsilon(A) \le P_\varepsilon(A)$ by Lemma [internalCoveringNumber_le_packingNumber](lem-internalcoveringnumber-le-packingnumber.md) and $P_\varepsilon(A) \le \frac{V(A + B_{\varepsilon/2})}{V(B_{\varepsilon/2})}$ by Lemma [packingNumber_mul_le_volume](lem-packingnumber-mul-le-volume.md).

## Lean

Formalized as [`Metric.coveringNumber_le_measure_div`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.coveringNumber_le_measure_div).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 235](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L235)
