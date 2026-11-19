---
declaration: lemma
origin: cited
lean: continuous_dirichletApprox, periodic_dirichletApprox, approxHilbertTransform_eq_dirichletApprox, dist_dirichletApprox_le
statement: formalized
proof: formalized
---

# Dirichlet approximation

Let $0\lt r<1$. Let $N$ be the smallest integer larger than $\frac 1r$. There is a $2\pi$-periodic continuous function ${L'}$ on ${\mathbb{R}}$ that satisfies for all $0\le x\le 2\pi$ and all $2\pi$-periodic bounded measurable functions $f$ on ${\mathbb{R}}$

$$
L_Nf(x)=\frac 1{2\pi}\int_{0}^{2\pi}f(y) {L'}(x-y)\, dy\,.\qquad\text{(29)}
$$

Moreover, for all $-\pi \le x \le \pi$,

$$
\left|L'(x)-\mathbf{1}_{\{y:\, r<|y|<1\}} \kappa(x)\right|\le 12 k_r(x)\, .\qquad\text{(30)}
$$

## Depends on

- [Dirichlet kernel](dirichlet-kernel.md)
- [lower secant bound](lower-secant-bound.md)

## Proof

We have by definition and [Dirichlet kernel](dirichlet-kernel.md)

$$
L_Ng(x)=
\frac 1N\sum_{n=0}^{N-1}
\int_0^{2\pi} e^{-i(N+n)x} K_{N+n}(x-y) e^{i(N+n)y}g(y)
\, dy \, .
$$

This is of the form (29) with the continuous function

$$
{L'}(x)= \frac 1N\sum_{n=0}^{N-1}
K_{N+n}(x) e^{-i(N+n)x}\, .
$$

With [(14)](dirichlet-kernel.md) of [Dirichlet kernel](dirichlet-kernel.md) we have $|K_N(x)|\le 2N+1$ for every $x$ and thus

$$
|{L'}(x)|\le \frac 1N\sum_{n=0}^{N-1}
(2N+2n+1) \le 4N\le 2^3 r^{-1}\, .\qquad\text{(31)}
$$

Therefore, for $|x|\in [0, r)\cup (1, \pi]$, we have

$$
\left|L'(x)-\mathbf{1}_{\{y:\, r<|y|<1\}}(x)\kappa(x)\right|=|L'(x)|\leq 2^{3} r^{-1}.\qquad\text{(32)}
$$

This proves (30) for $|x|\in [0, r)$ since $k_r(x)=r^{-1}$ in this case.

For $e^{ix}\neq 1$ one may use the expression [(15)](dirichlet-kernel.md) for $K_N$ in [Dirichlet kernel](dirichlet-kernel.md) to obtain

$$
{L'}(x)= \frac 1N\sum_{n=0}^{N-1}
\left(\frac{e^{i(N+n)x}}{1-e^{-ix}}
+\frac {e^{-i(N+n)x}}{1-e^{ix}}\right) e^{i(N+n)x}
$$

$$
= \frac 1N\sum_{n=0}^{N-1}
\left(\frac{e^{i2(N+n)x}}{1-e^{-ix}}
+\frac {1}{1-e^{ix}}\right)
$$

$$
= \frac{1}{1-e^{ix}} +
\frac 1N \frac {e^{i2Nx}}{1-e^{-ix}}
\sum_{n=0}^{N-1}
{e^{i2nx}}\qquad\text{(33)}
$$

and thus

$$
{L'}(x) -\mathbf{1}_{\{y:\, r<|y|<1\}}\kappa(x)=L''(x)+ \frac{1-\mathbf{1}_{{\{y:\, r<|y|<1\}}}(x)(1-|x|)}{1-e^{ix}},\qquad\text{(34)}
$$

where

$$
L''(x):=\frac 1N \frac {e^{i2Nx}}{1-e^{-ix}}
\sum_{n=0}^{N-1}
{e^{i2nx}}.
$$

For $x\in [-\pi, r]\cup [r, \pi]$, we have using [lower secant bound](lower-secant-bound.md) that

$$
\left|\frac{1-\mathbf{1}_{{\{y:\, r<|y|<1\}}}(x)(1-|x|)}{1-e^{ix}} \right|=\left|\frac{\min(|x|, 1)}{1-e^{ix}} \right|\leq \frac{2\min(|x|, 1)}{|x|}
$$

$$
\leq 2\cdot 1\leq 2 k_r(x).\qquad\text{(35)}
$$

Next, we need to estimate $L''(x)$. If the real part of $e^{ix}$ is negative, we have

$$
1\le |1-e^{-ix}|\le 2\, .
$$

and hence

$$
|L''(x)|\le
\frac 1N
\sum_{n=0}^{N-1}
1=1\le 1+\frac r{|1-e^{ix}|^2}\, .\qquad\text{(36)}
$$

If the real part of $e^{ix}$ is positive and in particular while still $e^{ix}\neq \pm 1$, then we have by telescoping

$$
(1-e^{2ix})
\sum_{n=0}^{N-1}
{e^{i2nx}}=1-e^{i2Nx}\, .
$$

As $e^{2ix}\neq 1$, we may divide by $1-e^{2ix}$ and insert this into (33) to obtain

$$
L''(x)=
\frac 1N \frac {e^{i2Nx}}{1-e^{-ix}}
\frac{1-e^{i2Nx}}{1-e^{2ix}}\, .
$$

Hence, using the nonnegativity of the real part of $e^{ix}$

$$
|L''(x)|
\le \frac 2 N \frac {1}{|1-e^{ix}|}
\frac{1}{|1-e^{2ix}|}
$$

$$
= \frac 2 N \frac {1}{|1-e^{ix}|^2}
\frac{1}{|1+e^{ix}|}\le
\frac {2r}{|1-e^{ix}|^2}\le 2 \left(1+\frac {r}{|1-e^{ix}|^2}\right)\qquad\text{(37)}
$$

Moreover, for $|x| \in [r, \pi]$, one checks easily that

$$
1+\frac {r}{|1-e^{ix}|^2} \leq 5 k_r(x).
$$

Therefore, (36) and (37) show that, in this range of $x$,

$$
|L''(x)| \le 10 k_r(x).
$$

Together with (35), this prove (30) for $|x| \in [r, \pi]$. As the range $|x| \in [0,r)$ is covered by (32), this completes the proof of the lemma.

## Lean

Formalized as [`continuous_dirichletApprox`](https://fpvandoorn.github.io/carleson/docs/find/#doc/continuous_dirichletApprox), [`periodic_dirichletApprox`](https://fpvandoorn.github.io/carleson/docs/find/#doc/periodic_dirichletApprox), [`approxHilbertTransform_eq_dirichletApprox`](https://fpvandoorn.github.io/carleson/docs/find/#doc/approxHilbertTransform_eq_dirichletApprox), [`dist_dirichletApprox_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dist_dirichletApprox_le).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8751](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8751)
