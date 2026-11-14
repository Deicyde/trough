---
declaration: definition
origin: cited
lean: MIPRE.LowDegree.IsSelfDualBasis, MIPRE.LowDegree.IsNormalBasis
statement: formalized
---

# Self-dual and normal bases

Let $K / \mathbb{F}$ be a finite extension of finite fields, $q = \left\vert {\mathbb{F}} \right\vert$. A basis $(e_i)$ of $K$ over $\mathbb{F}$ is *self-dual* when its Gram matrix for the trace form is the identity, $\mathrm{tr}_{K / \mathbb{F}}(e_i e_j) = \delta_{ij}$, and *normal* when its vectors are the Frobenius orbit $\alpha, \alpha^q, \alpha^{q^2}, \ldots$ of a single element $\alpha \in K$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.LowDegree.IsSelfDualBasis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.IsSelfDualBasis), [`MIPRE.LowDegree.IsNormalBasis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LowDegree.IsNormalBasis).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6278](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6278)
