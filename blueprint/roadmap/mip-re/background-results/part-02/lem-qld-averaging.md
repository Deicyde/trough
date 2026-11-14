---
declaration: lemma
origin: cited
lean: MIPRE.stateSqNorm_avg_le
statement: formalized
proof: formalized
---

# Averaging preserves closeness

Let $A^x \approx_\delta B^x$ on average over $x \sim \mu$, and let $\alpha_x$ be coefficients with $\left\vert {\alpha_x} \right\vert \leq 1$. Then $\mathop{\mathbb{E}}_x \alpha_x A^x \approx_\delta \mathop{\mathbb{E}}_x \alpha_x B^x$.

## Depends on

- [State-dependent POVM distance](../../foundations/part-02/def-state-distance.md)

## Proof depends on

- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)

## Proof

Triangle inequality and Jensen. Note the hypothesis is $\left\vert {\alpha_x} \right\vert \leq 1$, not $\left\vert {\alpha_x} \right\vert = 1$: the lemma is used with genuinely contractive coefficients. The $\delta$ is preserved exactly, with no constant: the triangle inequality gives $\left\| {\mathop{\mathbb{E}}_x \alpha_x (A^x - B^x)|\psi\rangle} \right\| \leq \mathop{\mathbb{E}}_x \left\| {(A^x - B^x)|\psi\rangle} \right\|$ and Jensen for the square root gives $\mathop{\mathbb{E}}_x \sqrt{f(x)} \leq \sqrt{\mathop{\mathbb{E}}_x f(x)}$, which is the $\mu$-probability case of `MIPRE.sum_mul_sqrt_le`.

## Lean

Formalized as [`MIPRE.stateSqNorm_avg_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.stateSqNorm_avg_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2049](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2049)
