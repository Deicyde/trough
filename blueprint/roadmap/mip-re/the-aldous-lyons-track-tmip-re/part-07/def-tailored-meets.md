---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.MeetsAt
statement: formalized
---

# A tailored verifier meeting a tailored game

A tailored verifier $\mathsf{V}$ *meets* a tailored game $G$ on questions $X$ at an index $n$ along a bijection $e$ from $X$ to the questions of $\mathsf{V}$ at $n$ when its sampler's distribution at $n$ is $G$'s weights along $e$, its answer-length calculator outputs $G$'s readable and linear lengths at every question $e(x)$, and its linear-constraints processor outputs $G$'s constraints at every pair $(e(x), e(y))$ and pair of readable answers.

## Depends on

- [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)
- [Tailored game; II:1243](../part-01/def-tailored-game.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.MeetsAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.MeetsAt).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3483](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3483)
