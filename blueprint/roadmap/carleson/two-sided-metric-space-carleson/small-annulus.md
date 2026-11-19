---
declaration: lemma
origin: cited
lean: small_annulus_right, small_annulus_left
statement: formalized
proof: formalized
---

# small annulus

Let $f:X\to{\mathbb{C}}$ be a bounded measurable function supported on a set of finite measure. Let $x\in X$ and $R>0$. Then, for all $\epsilon>0$, there exists some $\delta>0$ such that

$$
\left| \int_{R\lt \rho(x,y)\lt R+\delta} K(x,y) f(y) \, d\mu(y) \right| \le \epsilon
$$

and

$$
\left| \int_{R-\delta\lt \rho(x,y)\lt R} K(x,y) f(y) \, d\mu(y) \right| \le \epsilon \,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We only prove the second inequality, the first one is analogous. Note that the integrand is bounded in $X\setminus B(x,\frac{R}{2})$. So for $0\lt \delta\le\frac{R}{2}$,

$$
\begin{aligned}
&\left| \int_{R-\delta\lt \rho(x,y)\lt R} K(x,y) f(y) \, d\mu(y) \right| \\
\le &\frac{2^{a^3}}{\mu(B(x,\frac{R}{2}))} \, \sup_{y\in X}|f(x)| \cdot \mu(\{y\in X: R-\delta\lt \rho(x,y)\lt R\}).
\end{aligned}
$$

By continuity from above of $\mu$, the right factor becomes arbitrarily small as $\delta\rightarrow 0$. Thus, for small enough $\delta$, the whole expression is $\le\epsilon$.

## Lean

Formalized as [`small_annulus_right`](https://fpvandoorn.github.io/carleson/docs/find/#doc/small_annulus_right), [`small_annulus_left`](https://fpvandoorn.github.io/carleson/docs/find/#doc/small_annulus_left).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7425](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7425)
