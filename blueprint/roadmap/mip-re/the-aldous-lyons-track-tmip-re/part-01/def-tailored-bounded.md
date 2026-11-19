---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.IsBounded, MIPRE.Tailored.TailoredVerifier.Within
statement: formalized
---

# $\lambda$-bounded tailored verifiers, and budgets; II:1800

$\mathsf{V}$ is *$\lambda$-bounded* when, for every $n \geq 2$, the sampler's dimension and the running times of the three programs are at most $n^\lambda$ — the running times read as in Definition [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md), at degree $\lambda$ in the size of the input — the lengths $\mathcal{L}$ outputs are at most $n^\lambda$, and $\left\vert {\mathsf{V}} \right\vert \leq \lambda$. The answer-length calculator outputs in unary, as in the paper, but its running time is bounded relative to the size of its input, which is not bounded by $n^\lambda$; so the running time does not bound the lengths by $n^\lambda$, and that bound is a clause of its own. A verifier is *within a budget* at index $n$ when the same quantities are bounded by the budget's.

## Depends on

- [Tailored normal form verifier; II:1758](def-tailored-verifier.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.IsBounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.IsBounded), [`MIPRE.Tailored.TailoredVerifier.Within`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.Within).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 355](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L355)
