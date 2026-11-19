---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: Metric.HasCoveringExponent.subset
---

# hasBoundedInternalCoveringNumber_subset

If $A$ has bounded internal covering number with constant $c>0$ and exponent $d>0$, then for all $B \subseteq A$, $B$ has bounded internal covering number with constant $2^d c$ and exponent $d$.

## Depends on

- [Bounded internal covering number](../part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [internalCoveringNumber_subset_le](../part-01/lem-internalcoveringnumber-subset-le.md)

## Proof

$$
\begin{aligned}
N^{int}_\varepsilon(B)
&\le N^{int}_{\varepsilon/2}(A)
\le c (\varepsilon/2)^{-d}
= 2^d c \varepsilon^{-d}
\: .
\end{aligned}
$$

## Lean

Formalized as [`Metric.HasCoveringExponent.subset`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.HasCoveringExponent.subset).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 311](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L311)
