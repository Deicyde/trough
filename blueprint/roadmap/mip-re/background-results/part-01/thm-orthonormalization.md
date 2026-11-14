---
declaration: theorem
origin: cited
lean: MIPRE.Orthonormalization.povm_orthogonalization_finDim
statement: formalized
---

# Orthonormalization

Let $\mathcal{M}$ be a von Neumann algebra on a finite-dimensional Hilbert space, let $\varphi$ be a normal state on $\mathcal{M}$, and let $\{M_a\}_{a \in {\mathcal{A}}}$ be a POVM in $\mathcal{M}$ that is $\varepsilon$-nearly projective:

$$
\varphi\Bigl( \sum_{a \in {\mathcal{A}}} M_a^2 \Bigr) > 1 - \varepsilon\;.
$$

Then there is a projective measurement $\{P_a\}_{a \in {\mathcal{A}}}$ in $\mathcal{M}$ with

$$
\varphi\Bigl( \sum_{a \in {\mathcal{A}}} (M_a - P_a)^*(M_a - P_a) \Bigr) < 9\varepsilon\;.
$$

The same holds, on average, for a family $\{M^x_a\}$ indexed by $x \sim \mu$, by applying it to $\varphi$ averaged over $x$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`MIPRE.Orthonormalization.povm_orthogonalization_finDim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.povm_orthogonalization_finDim); the blueprint marks no proof of it as formalized.

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 249](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L249)
