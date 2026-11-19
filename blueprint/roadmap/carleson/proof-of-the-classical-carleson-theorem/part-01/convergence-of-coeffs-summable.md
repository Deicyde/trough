---
declaration: lemma
origin: cited
lean: hasSum_fourier_series_of_summable
statement: formalized
proof: formalized
---

# convergence-of-coeffs-summable

Let $f:{\mathbb{R}} \to {\mathbb{C}}$ such that

$$
\sum_{n\in {\mathbb{Z}}} |\widehat{f}_n| < \infty.
$$

Then

$$
\sup_{x\in [0,2\pi]} |f(x) - S_Nf(x)| \rightarrow 0
$$

as $N \rightarrow \infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is part of the Lean library.

## Lean

Formalized as [`hasSum_fourier_series_of_summable`](https://fpvandoorn.github.io/carleson/docs/find/#doc/hasSum_fourier_series_of_summable).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8525](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8525)
