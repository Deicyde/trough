---
declaration: lemma
origin: cited
lean: Tile.correlation, Tile.mem_ball_of_correlation_ne_zero, Tile.correlation_kernel_bound
statement: formalized
proof: formalized
---

# correlation kernel bound

Let $-S\le s_1\le s_2\le S$ and let $x_1,x_2\in X$. Define

$$
\varphi(y) := \overline{K_{s_1}(x_1, y)}
K_{s_2}(x_2, y) \, .
$$

If $\varphi(y)\neq 0$, then

$$
y\in B(x_1, D^{s_1})\, .\qquad\text{(29)}
$$

Moreover, we have with $\tau = 1/a$

$$
\|\varphi\|_{C^\tau(B(x_1, 2 D^{s_1}))}\le
\frac{2^{231 a^3}}{\mu(B(x_1, D^{s_1}))\mu(B(x_2, D^{s_2}))}
\, .\qquad\text{(30)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $\varphi(y)$ is not zero, then $K_{s_1}(x_1, y)$ is not zero and thus [(65)](../proof-of-metric-space-carleson-overview/kernel-summand.md) gives (29).

We next have for $y$ with [(66)](../proof-of-metric-space-carleson-overview/kernel-summand.md)

$$
|\varphi(y)|\le
\frac{2^{204 a^3}}{\mu(B(x_1, D^{s_1}))\mu(B(x_2, D^{s_2}))}\qquad\text{(31)}
$$

and for $y'\neq y$ additionally with [(67)](../proof-of-metric-space-carleson-overview/kernel-summand.md)

$$
|\varphi(y)-\varphi(y')|
$$

$$
\le
|K_{s_1}(x_1,y)-K_{s_1}(x_1,y'))||
K_{s_2}(x_2, y)|
$$

$$
+|K_{s_1}(x_1, y')|
|K_{s_2}(x_2, y) - K_{s_2}(x_2, y'))|
$$

$$
\le \frac{2^{229 a^3}}{\mu(B(x_1, D^{s_1}))\mu(B(x_2, D^{s_2}))}
\left(\left(\frac{ \rho(y,y')}{D^{s_1}}\right)^{1/a}+
\left(\frac{ \rho(y,y')}{D^{s_2}}\right)^{1/a}\right)
$$

$$
\le \frac{2^{230 a^3}}{\mu(B(x_1, D^{s_1}))\mu(B(x_2, D^{s_2}))}
\left(\frac{ \rho(y,y')}{D^{s_1}}\right)^{1/a}\,.\qquad\text{(32)}
$$

Adding the estimates (31) and (32) gives (30). This proves the lemma.

## Lean

Formalized as [`Tile.correlation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Tile.correlation), [`Tile.mem_ball_of_correlation_ne_zero`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Tile.mem_ball_of_correlation_ne_zero), [`Tile.correlation_kernel_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Tile.correlation_kernel_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3772](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3772)
