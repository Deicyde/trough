---
declaration: lemma
origin: cited
lean: TileStructure.Forest.local_dens1_tree_bound
statement: formalized
proof: formalized
---

# local dens1 tree bound

Let ${\mathfrak u} \in {\mathfrak U}$ and $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$. Then

$$
\mu(L \cap G \cap \bigcup_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} E({\mathfrak p})) \le 2^{101a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u})) \mu(L)\,.\qquad\text{(23)}
$$

## Depends on

- [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)

## Proof

*Proof of local dens1 tree bound.* If the set on the right hand side is empty, then (23) holds. If not, then there exists ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ with $L \cap {\mathcal{I}}({\mathfrak p}) \ne \emptyset$.

Suppose first that there exists such ${\mathfrak p}$ with ${\mathrm{s}}({\mathfrak p}) \le s(L)$. Then by [(8)](../../proof-of-metric-space-carleson-overview/README.md) ${\mathcal{I}}({\mathfrak p}) \subset L$, which gives by the definition of $\mathcal{L}({\mathfrak T}({\mathfrak u}))$ that $s(L) = -S$ and hence $L = {\mathcal{I}}({\mathfrak p})$. Let ${\mathfrak q} \in {\mathfrak T}({\mathfrak u})$ with $E({\mathfrak q}) \cap L \ne \emptyset$. Since $s(L) = -S \le {\mathrm{s}}({\mathfrak q})$ it follows from [(8)](../../proof-of-metric-space-carleson-overview/README.md) that ${\mathcal{I}}({\mathfrak p}) = L \subset {\mathcal{I}}({\mathfrak q})$. We have then by [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)

$$
\begin{aligned}
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak q})) &\le d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u})) + d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak q}), {\mathcal{Q}}({\mathfrak u}))\\
&\le d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u})) + d_{{\mathfrak q}}({\mathcal{Q}}({\mathfrak q}), {\mathcal{Q}}({\mathfrak u}))\,.
\end{aligned}
$$

Using that ${\mathfrak p}, {\mathfrak q} \in {\mathfrak T}({\mathfrak u})$ and [(30)](../../proof-of-metric-space-carleson-overview/README.md), this is at most $8$. Using again the triangle inequality and [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md), we obtain that for each $q \in B_{{\mathfrak q}}({\mathcal{Q}}({\mathfrak q}), 1)$

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), q) \le d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak q})) + d_{{\mathfrak q}}({\mathcal{Q}}({\mathfrak q}), q) \le 9\,.
$$

Thus $L \cap G \cap E({\mathfrak q}) \subset E_2(9, {\mathfrak p})$. We obtain

$$
\mu(L \cap G \cap \bigcup_{{\mathfrak q} \in {\mathfrak T}({\mathfrak u})} E({\mathfrak q})) \le \mu(E_2(9, {\mathfrak p}))\,.
$$

By the definition of $\operatorname{\operatorname{dens}}_1$, this is bounded by

$$
9^a \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u})) \mu({\mathcal{I}}({\mathfrak p})) =9^a \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u})) \mu(L)\,.
$$

Since $a \ge 4$, (23) follows in this case.

Now suppose that for each ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ with $L \cap E({\mathfrak p}) \ne \emptyset$, we have ${\mathrm{s}}({\mathfrak p}) > s(L)$. Since there exists at least one such ${\mathfrak p}$, there exists in particular at least one cube $L'' \in \mathcal{D}$ with $L \subset L''$ and $s(L'') > s(L)$. By [(7)](../../proof-of-metric-space-carleson-overview/README.md), there exists $L' \in \mathcal{D}$ with $L \subset L'$ and $s(L') = s(L) + 1$. By the definition of $\mathcal{L}({\mathfrak T}({\mathfrak u}))$ there exists a tile ${\mathfrak p}'' \in {\mathfrak T}({\mathfrak u})$ with ${\mathcal{I}}({\mathfrak p}'') \subset L'$.

It suffices to show that there exists a tile ${\mathfrak p}' \in {\mathfrak P}({\mathfrak T}({\mathfrak u}))$ with ${\mathcal{I}}({\mathfrak p}') = L'$, $d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak u})) < 4$ and $9{\mathfrak p}'' \lesssim 9{\mathfrak p}'$. For then, let ${\mathfrak q} \in {\mathfrak T}({\mathfrak u})$ with $L \cap E({\mathfrak q}) \ne \emptyset$. As shown above, this implies ${\mathrm{s}}({\mathfrak q}) \ge s(L')$, so by [(8)](../../proof-of-metric-space-carleson-overview/README.md) $L' \subset {\mathcal{I}}({\mathfrak q})$. If $q \in B_{{\mathfrak q}}({\mathcal{Q}}({\mathfrak q}), 1)$, then by a similar calculation as above, using the triangle inequality, [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) and [(30)](../../proof-of-metric-space-carleson-overview/README.md), we obtain

$$
d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), q) \le d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak q})) + d_{{\mathfrak q}}({\mathcal{Q}}({\mathfrak q}), q) \le 9\,.
$$

Thus $L \cap G \cap E({\mathfrak q}) \subset E_2(9, {\mathfrak p}')$. We deduce using the definition [(26)](../../proof-of-metric-space-carleson-overview/README.md) of $\operatorname{\operatorname{dens}}_1$

$$
\mu(L \cap G \cap \bigcup_{{\mathfrak q} \in {\mathfrak T}({\mathfrak u})} E({\mathfrak q})) \le \mu(E_2(9, {\mathfrak p}')) \le 9^a \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u})) \mu(L')\,.
$$

Using the doubling property [(5)](../../introduction/README.md), [(10)](../../proof-of-metric-space-carleson-overview/README.md), and $a \ge 4$ this is estimated by

$$
9^a 2^{100a^3 + 5a}\operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u})) \mu(L) \le 2^{101 a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))\mu(L)\,.
$$

To show existence of ${\mathfrak p}'$ with the given properties, if ${\mathcal{I}}({\mathfrak p}'') = L'$ we can take ${\mathfrak p}' = {\mathfrak p}''$, which satisfies the distance property by [(30)](../../proof-of-metric-space-carleson-overview/README.md) and the other properties trivially. Otherwise, let ${\mathfrak p}'$ be the unique tile such that ${\mathcal{I}}({\mathfrak p}') = L'$ and such that $\Omega({\mathfrak u}) \cap \Omega({\mathfrak p}') \ne \emptyset$. Since ${\mathcal{I}}({\mathfrak p}') \subset {\mathcal{I}}({\mathfrak p})$ and ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$, we have ${\mathfrak p}' \in {\mathfrak P}({\mathfrak T}({\mathfrak u}))$. Since by [(30)](../../proof-of-metric-space-carleson-overview/README.md) ${\mathrm{s}}({\mathfrak p}') = s(L') \le {\mathrm{s}}({\mathfrak p}) < {\mathrm{s}}({\mathfrak u})$, we have by [(8)](../../proof-of-metric-space-carleson-overview/README.md) and [(14)](../../proof-of-metric-space-carleson-overview/README.md) that $\Omega({\mathfrak u}) \subset \Omega({\mathfrak p}')$, and hence the distance property. $9{\mathfrak p}'' \lesssim 9{\mathfrak p}'$ follows by the triangle inequality, [(30)](../../proof-of-metric-space-carleson-overview/README.md), [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) and [(15)](../../proof-of-metric-space-carleson-overview/README.md). This completes the proof.

## Lean

Formalized as [`TileStructure.Forest.local_dens1_tree_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.local_dens1_tree_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4976](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4976)
