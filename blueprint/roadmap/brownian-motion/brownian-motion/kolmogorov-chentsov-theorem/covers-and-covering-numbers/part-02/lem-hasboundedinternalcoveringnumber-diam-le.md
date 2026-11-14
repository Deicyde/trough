---
declaration: lemma
origin: cited
lean: Metric.HasCoveringExponent.ediam_le
statement: formalized
proof: formalized
---

# hasBoundedInternalCoveringNumber_diam_le

If $A$ has bounded internal covering number with constant $c>0$ and exponent $d>0$, then $\mathrm{diam}(A) \le c^{1/d}$.

## Depends on

- [Bounded internal covering number](../part-01/def-hasboundedinternalcoveringnumber.md)

## Proof

If $\mathrm{diam}(A) = 0$ there is nothing to prove. Otherwise $A$ is nonempty, so any cover of $A$ has at least one element, and applying the covering condition with $\varepsilon = \mathrm{diam}(A)$ gives $1 \le N^{int}_{\mathrm{diam}(A)}(A) \le c \, \mathrm{diam}(A)^{-d}$, hence $\mathrm{diam}(A)^d \le c$.

## Lean

Formalized as [`Metric.HasCoveringExponent.ediam_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.HasCoveringExponent.ediam_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 330](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L330)
