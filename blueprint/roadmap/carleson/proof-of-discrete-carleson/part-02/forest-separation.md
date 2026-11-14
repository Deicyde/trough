---
declaration: lemma
origin: cited
lean: forest_separation
statement: formalized
proof: formalized
---

# forest separation

For each ${\mathfrak u},{\mathfrak u}'\in {\mathfrak U}_3(k,n,j)$ with ${\mathfrak u}\neq {\mathfrak u}'$ and each ${\mathfrak p} \in {\mathfrak T}_2({\mathfrak u})$ with ${\mathcal{I}}({\mathfrak p})\subset {\mathcal{I}}({\mathfrak u}')$ we have

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}')) > 2^{Z(n+1)}\,.
$$

## Depends on

- [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)

## Proof

By the definition [(12)](../README.md) of ${\mathfrak C}_2(k,n,j)$, there exists a tile ${\mathfrak p}' \in {\mathfrak C}_1(k,n,j)$ with ${\mathfrak p}' \le {\mathfrak p}$ and ${\mathrm{s}}({\mathfrak p}') \le {\mathrm{s}}({\mathfrak p})- Z(n+1)$. By [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) we have

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}')) \ge 2^{95a Z(n+1)} d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}'))\,.
$$

By [(39)](../part-01/wiggle-order-3.md) we have $2{\mathfrak p}' \lesssim 2{\mathfrak p}$, so by transitivity of $\lesssim$ there exists $\mathfrak{v} \sim {\mathfrak u}$ with $2{\mathfrak p}' \lesssim \mathfrak{v}$ and ${\mathcal{I}}({\mathfrak p}') \ne {\mathcal{I}}(\mathfrak{v})$. Since ${\mathfrak u}, {\mathfrak u}'$ are not equivalent under $\sim$, we have $\mathfrak{v} \not \sim {\mathfrak u}'$, thus $10{\mathfrak p}' \not\lesssim {\mathfrak u}'$. This implies that there exists $q \in B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 1) \setminus B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), 10)$.

From ${\mathfrak p}' \le {\mathfrak p}$, ${\mathcal{I}}({\mathfrak p}') \subset {\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u}')$ and [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) it then follows that

$$
\begin{aligned}
&\quad d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}'))\\
&\ge -d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak p}')) + d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), q) - d_{{\mathfrak p}'}(q, {\mathcal{Q}}({\mathfrak u}'))\\
&\ge -d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak p}')) + d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), q) - d_{{\mathfrak u}'}(q, {\mathcal{Q}}({\mathfrak u}'))\\
&> -1 + 10 - 1 = 8\,.
\end{aligned}
$$

The lemma follows by combining the two displays with the fact that $95 a \ge 1$.

## Lean

Formalized as [`forest_separation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_separation).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3108](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3108)
