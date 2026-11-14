---
declaration: lemma
origin: cited
lean: TileStructure.Forest.boundary_operator_bound
statement: formalized
proof: formalized
---

# boundary operator bound

For all ${\mathfrak u} \in {\mathfrak U}$ and all bounded functions $f$ with bounded support

$$
\|S_{1,{\mathfrak u}}f\|_2 \le 2^{12a} \|f\|_2\,.\qquad\text{(15)}
$$

## Depends on

- [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md)
- [boundary overlap](boundary-overlap.md)

## Proof

*Proof of boundary operator bound.* Note that by definition, $S_{1,{\mathfrak u}}f$ is a finite sum of indicator functions of cubes $I \in \mathcal{D}$ for each locally integrable $f$, and hence is bounded, has bounded support and is integrable. Let $g$ be another function with the same three properties. Then $\bar g S_{1,{\mathfrak u}}f$ is integrable, and we have

$$
\Bigg|\int \bar g(y) S_{1,{\mathfrak u}}f(y) \, \mathrm{d}\mu(y)\Bigg|
$$

$$
\begin{gathered}
= \Bigg|\sum_{I\in\mathcal{D}} \frac{1}{\mu(B(c(I), 16 D^{s(I)}))} \int_I \bar g(y) \, \mathrm{d}\mu(y)\\
\times \sum_{\substack{J\in \mathcal{J}({\mathfrak T}({\mathfrak u}))\,:\,J\subseteq B(c(I), 16 D^{s(I)})\\s(J)\le s(I)}} D^{(s(J)-s(I))/a}\int_J |f(y)| \,\mathrm{d}\mu(y)\Bigg|
\end{gathered}
$$

$$
\begin{gathered}
\le \sum_{I\in\mathcal{D}} \frac{1}{\mu(B(c(I), 16D^{s(I)}))} \int_{B(c(I), 16D^{s(I)})} | g(y)| \, \mathrm{d}\mu(y)\\ \times \sum_{\substack{J\in \mathcal{J}({\mathfrak T}({\mathfrak u}))\,:\,J\subseteq B(c(I), 16 D^{s(I)})\\ s(J) \le s(I)}} D^{(s(J)-s(I))/a}\int_J |f(y)| \,\mathrm{d}\mu(y)\,.
\end{gathered}
$$

Changing the order of summation and using $J \subset B(c(I), 16 D^{s(I)})$ to bound the first average integral by $M_{\mathcal{B},1}|g|(y)$ for any $y \in J$, we obtain

$$
\begin{aligned}
\le \sum_{J\in\mathcal{J}({\mathfrak T}({\mathfrak u}))}\int_J|f(y)| M_{\mathcal{B},1}|g|(y) \, \mathrm{d}\mu(y) \sum_{\substack{I \in \mathcal{D} \, : \, J\subset B(c(I),16 D^{s(I)})\\ s(I) \ge s(J)}} D^{(s(J)-s(I))/a}.\qquad\text{(16)}\end{aligned}
$$

By [boundary overlap](boundary-overlap.md), there are at most $2^{9a}$ cubes $I$ at each scale satisfying the inclusion $J \subset B(c(I),16D^{s(I)})$. Since $D^{-1/a}\le\frac12$, $(1 - D^{-1/a})^{-1} \le 2$. Using this estimate for the sum of the geometric series, we conclude that (16) is at most

$$
2^{9a+1} \sum_{J\in\mathcal{J}({\mathfrak T}({\mathfrak u}))}\int_J|f(y)| M_{\mathcal{B},1}|g|(y) \, \mathrm{d}\mu(y)\,.
$$

The collection $\mathcal{J}$ is a partition of $\bigcup_{I \in \mathcal{D}} I$, so this equals

$$
2^{9a+1} \int_X|f(y)| M_{\mathcal{B},1}|g|(y) \, \mathrm{d}\mu(y)\,.
$$

Using Cauchy-Schwarz and [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md), we conclude

$$
\left|\int \bar g S_{1,{\mathfrak u}}f \, \mathrm{d}\mu \right| \le 2^{12a} \|g\|_2\|f\|_2\,.
$$

The lemma now follows by choosing $g = S_{1,{\mathfrak u}}f$ and dividing on both sides by the finite $\|S_{1,{\mathfrak u}}f\|_2$.

## Lean

Formalized as [`TileStructure.Forest.boundary_operator_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.boundary_operator_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4724](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4724)
