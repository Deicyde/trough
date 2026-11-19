---
declaration: lemma
origin: cited
lean: Metric.packingNumber_mul_le_measure
statement: formalized
proof: formalized
---

# packingNumber_mul_le_volume

$P_\varepsilon(A) V(B_{\varepsilon/2}) \le V(A + B_{\varepsilon/2})$.

## Depends on

- [Packing number](def-packingnumber.md)

## Proof depends on

- [le_volume_of_isSeparated](lem-le-volume-of-isseparated.md)

## Proof

$P_\varepsilon(A)$ is the supremum of $\vert S \vert$ over the $\varepsilon$-separated sets $S \subseteq A$. Apply Lemma [le_volume_of_isSeparated](lem-le-volume-of-isseparated.md) to each of them.

## Lean

Formalized as [`Metric.packingNumber_mul_le_measure`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.packingNumber_mul_le_measure).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 209](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L209)
