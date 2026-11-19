---
declaration: lemma
origin: cited
lean: MIPRE.obsOf, MIPRE.stateDist_obsOf_le
statement: formalized
proof: formalized
---

# From POVM elements to generalized observables

Let $\{A^x_a\}$ and $\{B^x_a\}$ be POVMs with a common outcome set ${\mathcal{A}}$, and let $\alpha_a$ be coefficients of unit modulus. If $A^x_a \approx_\delta B^x_a$ then the generalized observables $A^x = \sum_a \alpha_a A^x_a$ and $B^x = \sum_a \alpha_a B^x_a$ satisfy $A^x \approx_{\left\vert {{\mathcal{A}}} \right\vert \delta} B^x$.

## Depends on

- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)

## Proof depends on

- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)

## Proof

Triangle inequality over the outcomes, then Cauchy–Schwarz against the constant $1$: $(\sum_a t_a)^2 \leq \left\vert {{\mathcal{A}}} \right\vert \sum_a t_a^2$. Unit modulus is more than the proof uses; the formalized hypothesis is $\left\vert {\alpha_a} \right\vert \leq 1$, and the constant $\left\vert {{\mathcal{A}}} \right\vert$ is exact rather than an $O(\cdot)$.

## Lean

Formalized as [`MIPRE.obsOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.obsOf), [`MIPRE.stateDist_obsOf_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateDist_obsOf_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2072](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2072)
