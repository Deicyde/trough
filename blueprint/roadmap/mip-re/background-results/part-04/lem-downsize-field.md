---
declaration: lemma
origin: cited
lean: MIPRE.LowDegree.coord_eq_trace, MIPRE.LowDegree.trace_mul_eq_dot
statement: formalized
proof: formalized
---

# Self-dual coordinates are trace pairings

Let $(e_i)$ be a self-dual basis of $K / \mathbb{F}$ and $\kappa(x)$ the coordinate vector of $x \in K$. Then

1. $\kappa(x)_i = \mathrm{tr}_{K/\mathbb{F}}(x e_i)$, and
2. $\mathrm{tr}_{K/\mathbb{F}}(xy) = \kappa(x) \cdot \kappa(y)$.

## Depends on

- [Self-dual and normal bases](def-self-dual-basis.md)

## Proof

For the first, expand $x = \sum_j \kappa(x)_j e_j$, multiply by $e_i$ and take the trace: self-duality kills every term but $j = i$. The second follows from the first by the same expansion, $\mathrm{tr}(xy) = \sum_j \kappa(x)_j \mathrm{tr}(e_j y) = \sum_j \kappa(x)_j \kappa(y)_j$.

## Lean

Formalized as [`MIPRE.LowDegree.coord_eq_trace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.coord_eq_trace), [`MIPRE.LowDegree.trace_mul_eq_dot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.trace_mul_eq_dot).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6288](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6288)
