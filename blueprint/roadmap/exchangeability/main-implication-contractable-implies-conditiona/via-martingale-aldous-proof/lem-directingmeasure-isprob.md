---
declaration: lemma
origin: cited
lean: Exchangeability.DeFinetti.ViaMartingale.directingMeasure_isProb
statement: formalized
---

# Directing measure is probability measure

The directing measure $\nu(\omega)(B) = \mathbb{E}[\mathbf{1}_{X_0 \in B} \mid \mathcal{T}](\omega)$ is a probability measure for every $\omega$ (the bound is pointwise, not merely a.e., via mathlib's `isProbability_condExpKernel`).

## Depends on

- [Tail $\sigma$-algebra](../../foundations/sigma-algebra-infrastructure/def-tailsigma.md)

## Lean

Stated as [`Exchangeability.DeFinetti.ViaMartingale.directingMeasure_isProb`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.ViaMartingale.directingMeasure_isProb); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 229](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L229)
