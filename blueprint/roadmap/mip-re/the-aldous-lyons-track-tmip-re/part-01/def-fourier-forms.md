---
declaration: definition
origin: cited
lean: MIPRE.Tailored.bitSign, MIPRE.Tailored.fourierFactor, MIPRE.Tailored.fourierProj, MIPRE.Tailored.obsChar, MIPRE.Tailored.dotBit
statement: formalized
---

# The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006

For $k$ commuting involutions $U_1, \dots, U_k$ of a complex $\ast$-algebra — the *observable form* of a measurement with outcomes in $\mathbb{F}_2^k$ — the *representation form* is the homomorphism $\alpha \mapsto U^\alpha = \prod_i U_i^{\alpha_i}$ on $\mathbb{F}_2^k$, and the *projective form* is the Fourier transform

$$
P_a \;=\; \prod_{i=1}^{k} \tfrac12\bigl({I} + (-1)^{a_i}\, U_i\bigr), \qquad a \in \mathbb{F}_2^k.
$$

The inner product $\langle \alpha, a\rangle = \sum_i \alpha_i a_i$ is taken over $\mathbb{F}_2$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.Tailored.bitSign`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.bitSign), [`MIPRE.Tailored.fourierFactor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.fourierFactor), [`MIPRE.Tailored.fourierProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.fourierProj), [`MIPRE.Tailored.obsChar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.obsChar), [`MIPRE.Tailored.dotBit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.dotBit).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 70](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L70)
