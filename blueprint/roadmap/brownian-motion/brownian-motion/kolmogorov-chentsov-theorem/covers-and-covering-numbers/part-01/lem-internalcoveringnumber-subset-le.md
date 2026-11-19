---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: Metric.coveringNumber_subset_le
---

# internalCoveringNumber_subset_le

For $B \subseteq A$, $N^{int}_\varepsilon(B) \le N^{int}_{\varepsilon/2}(A)$.

## Depends on

- [Internal covering number](def-internalcoveringnumber.md)

## Proof depends on

- [internalCoveringNumber_le_packingNumber](lem-internalcoveringnumber-le-packingnumber.md)
- [packingNumber_two_le_externalCoveringNumber](lem-packingnumber-two-le-externalcoveringnumber.md)
- [externalCoveringNumber_mono](lem-externalcoveringnumber-mono.md)
- [externalCoveringNumber_le_internalCoveringNumber](lem-externalcoveringnumber-le-internalcoveringnu.md)

## Proof

$$
\begin{aligned}
N^{int}_\varepsilon(B)
&\le P_{\varepsilon}(B)
\le N^{ext}_{\varepsilon/2}(B)
\le N^{ext}_{\varepsilon/2}(A)
\le N^{int}_{\varepsilon/2}(A)
\: .
\end{aligned}
$$

## Lean

Formalized as [`Metric.coveringNumber_subset_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.coveringNumber_subset_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 127](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L127)
