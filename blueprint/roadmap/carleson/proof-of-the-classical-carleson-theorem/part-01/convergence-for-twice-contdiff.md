---
declaration: lemma
origin: cited
lean: fourierConv_ofTwiceDifferentiable
statement: formalized
proof: formalized
---

# convergence-for-twice-contdiff

Let $f:{\mathbb{R}} \to {\mathbb{C}}$ be $2\pi$-periodic and twice continuously differentiable. Then

$$
\sup_{x\in [0,2\pi]} |f(x) - S_Nf(x)| \rightarrow 0
$$

as $N \rightarrow \infty$.

## Depends on

- [fourier-coeff-derivative](fourier-coeff-derivative.md)
- [convergence-of-coeffs-summable](convergence-of-coeffs-summable.md)

## Proof

By [Lemma convergence-of-coeffs-summable](convergence-of-coeffs-summable.md), it suffices to show that the Fourier coefficients $\widehat{f}_n$ are summable. Applying [Lemma fourier-coeff-derivative](fourier-coeff-derivative.md) twice and using the fact that $f''$ is continuous and thus bounded on $[0,2\pi]$ , we compute

$$
\sum_{n\in {\mathbb{Z}}} |\widehat{f}_n| = |\widehat{f}_0| + \sum_{n\in {\mathbb{Z}} \setminus \{0\}} \frac {1}{n^2} |\widehat{f''}_n|
\le |\widehat{f}_0| + \left(\sup_{x\in [0,2\pi]} |f(x)| \right) \cdot \sum_{n\in {\mathbb{Z}} \setminus \{0\}} \frac {1}{n^2}
< \infty.
$$

## Lean

Formalized as [`fourierConv_ofTwiceDifferentiable`](https://fpvandoorn.github.io/carleson/docs/find/#doc/fourierConv_ofTwiceDifferentiable).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8545](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8545)
