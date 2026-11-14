---
declaration: lemma
origin: cited
lean: dirichletKernel_eq, partialFourierSum_eq_conv_dirichletKernel
statement: formalized
proof: formalized
---

# Dirichlet kernel

We have for every $2\pi$-periodic bounded measurable $f$ and every $N\ge 0$

$$
S_Nf(x)=\frac 1{2\pi}\int_{0}^{2\pi}f(y) K_N(x-y)\, dy
$$

where $K_N$ is the $2\pi$-periodic continuous function of ${\mathbb{R}}$ given by

$$
\sum_{n=-N}^N e^{in x'}\, .\qquad\text{(14)}
$$

We have for $e^{ix'}\neq 1$ that

$$
K_N(x')=\frac{e^{iNx'}}{1-e^{-ix'}}
+\frac {e^{-iNx'}}{1-e^{ix'}} \, .\qquad\text{(15)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have by definitions and interchanging sum and integral

$$
S_Nf(x)=\sum_{n=-N}^N \widehat{f}_n e^{inx}
$$

$$
=\sum_{n=-N}^N \frac 1{2\pi}\int_{0}^{2\pi}
f(x) e^{in(x-y)}\, dy
$$

$$
=\frac 1{2\pi}\int_{0}^{2\pi}
f(y) \sum_{n=-N}^N e^{in(x-y)}\, dy\, .\qquad\text{(16)}
$$

This proves the first statement of the lemma. By a telescoping sum, we have for every $x'\in {\mathbb{R}}$

$$
\left( e^{\frac 12 ix'}-e^{-\frac 12 ix'}\right) \sum_{n=-N}^N e^{inx'}= e^{(N+\frac 12) ix'}-e^{-(N+\frac 12) ix'}\, .
$$

If $e^{ix'}\neq 1$, the first factor on the left-hand side is not $0$ and we may divide by this factor to obtain

$$
\sum_{n=-N}^N e^{inx'}= \frac{e^{i(N+\frac 1 2)x'}}{e^{\frac 12 ix'}-e^{-\frac 12ix'}}
-\frac{e^{-i(N+\frac 1 2)x'}}{e^{\frac 12 ix'}-e^{-\frac 12ix'}}
=\frac{e^{iNx'}}{1-e^{-ix'}}
+\frac {e^{-iNx'}}{1-e^{ix'}}\, .
$$

This proves the second part of the lemma.

## Lean

Formalized as [`dirichletKernel_eq`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dirichletKernel_eq), [`partialFourierSum_eq_conv_dirichletKernel`](https://fpvandoorn.github.io/carleson/docs/find/#doc/partialFourierSum_eq_conv_dirichletKernel).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8341](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8341)
