---
declaration: lemma
origin: cited
lean: partialFourierSum_bound
statement: formalized
proof: formalized
---

# partial Fourier sum bound

Let $g:{\mathbb{R}}\to{\mathbb{C}}$ be a measurable $2\pi$-periodic function such that for some $\delta>0$ and every $x\in{\mathbb{R}}$,

$$
|g(x)|\le \delta \,.
$$

Then for every $x\in [0,2\pi]$ and $N>0$,

$$
|S_N g(x)| \le \frac{1}{2\pi} (Tg(x) + T\bar{g}(x)) + \pi\delta.
$$

## Depends on

- [Dirichlet kernel](../part-01/dirichlet-kernel.md)
- [Dirichlet kernel - Hilbert kernel relation](dirichlet-hilbert.md)

## Proof

Let $x\in [0,2\pi]$ and $N>0$. We have with [Dirichlet kernel](../part-01/dirichlet-kernel.md)

$$
|S_N g(x)| = \frac{1}{2\pi} \left| \int_0^{2\pi} g(y) K_N(x-y) \, dy\right|\,.
$$

We use $2\pi$-periodicity of $g$ and $K_N$ to shift the domain of integration to obtain

$$
= \frac{1}{2\pi} \left|\int_{x-\pi}^{x+\pi} g(y) K_N(x-y) \, dy\right|\,.
$$

Using the triangle inequality, we split this as

$$
\le \frac{1}{2\pi} \left|\int_{x-\pi}^{x+\pi} g(y) \left(K_N(x-y) - \max(|x-y|,0) K_N(x-y)\right) \, dy \right|\qquad\text{(38)}
$$

$$
+ \frac{1}{2\pi} \left|\int_{x-\pi}^{x+\pi} g(y) \max(|x-y|,0) K_N(x-y) \, dy\right|\,.\qquad\text{(39)}
$$

Note that all integrals are well defined, since $K_N$ is by [(14)](../part-01/dirichlet-kernel.md) bounded by $2N+1$. Using that

$$
\max(|x-y|,0) K_N(x-y) = e^{-iN(x-y)}\kappa(x-y) + \overline{e^{-iN(x-y)}\kappa(x-y)} \,,\qquad\text{(40)}
$$

[Dirichlet kernel - Hilbert kernel relation](dirichlet-hilbert.md) and [(41)](partial-fourier-sums-of-small.md), we bound (38) by

$$
\frac{1}{2\pi} \int_{x-\pi}^{x+\pi} |g(y)| \left|K_N(x-y) - e^{-iN(x-y)}\kappa(x-y) + \overline{e^{-iN(x-y)}\kappa(x-y)}\right|\, dy
\le \pi\delta \,.
$$

By dominated convergence and since $\kappa(x-y) = 0$ for $|x-y| > 1$, (39) equals

$$
\frac{1}{2\pi} \lim_{r \to 0^+} \left| \int_{r < |x-y| < 1} g(y) \max(|x-y|,0) K_N(x-y) \, dy\right|\,.
$$

We bound the limit by a supremum and rewrite using (40),

$$
\le \frac{1}{2\pi} \sup_{r > 0} \left| \int_{r < |x-y| < 1} g(y) \left(e^{-iN(x-y)}\kappa(x-y) + \overline{e^{-iN(x-y)}\kappa(x-y)}\right) \, dy\right|
$$

Using the triangle inequality, we further bound this by

$$
\begin{alignedat}{3}
\le&&&\frac{1}{2\pi} \sup_{r > 0} \left| \int_{r < |x-y| < 1} g(y) e^{-iNy} \kappa(x-y) \, dy\right| \\
&+ &&\frac{1}{2\pi} \sup_{r > 0} \left| \int_{r < |x-y| < 1} \overline{g}(y) e^{-iNy} \kappa(x-y) \, dy\right|\,.
\end{alignedat}
$$

By the definition [(9)](../part-01/real-carleson.md) of $T$, this is

$$
\le \frac{1}{2\pi} (Tg(x) + T\bar{g}(x))\,.
$$

## Lean

Formalized as [`partialFourierSum_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/partialFourierSum_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9057](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9057)
