---
declaration: lemma
origin: cited
lean: TileStructure.Forest.thin_scale_impact
statement: formalized
proof: formalized
---

# thin scale impact

If ${\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}$ and $J \in \mathcal{J'}$ with $B({\mathcal{I}}({\mathfrak p})) \cap B(J) \ne \emptyset$, then

$$
{\mathrm{s}}({\mathfrak p}) \le s(J) + 2 - \frac{Zn}{202a^3}\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose that ${\mathrm{s}}({\mathfrak p}) > s(J) + 2 -\frac{Zn}{202a^3} =: s(J) - s_1$. Then, we have $s_1 + 2 \ge 0$ so

$$
\rho({\mathrm{c}}({\mathfrak p}), c(J)) \le 8D^{s(J)}+8D^{{\mathrm{s}}({\mathfrak p})} \le 16 D^{{\mathrm{s}}({\mathfrak p}) + s_1 + 2}\,.
$$

There exists a tile ${\mathfrak q} \in {\mathfrak T}({\mathfrak u}_1)$. By [(30)](../../proof-of-metric-space-carleson-overview/README.md), it satisfies ${\mathcal{I}}({\mathfrak q}) \subsetneq {\mathcal{I}}({\mathfrak u}_1)$. Thus ${\mathcal{I}}({\mathfrak u}_1) \notin \mathcal{J}'$. It follows that $J \subsetneq {\mathcal{I}}({\mathfrak u}_1)$. By [(7)](../../proof-of-metric-space-carleson-overview/README.md) and [(8)](../../proof-of-metric-space-carleson-overview/README.md), there exists a cube $J' \in \mathcal{D}$ with $J \subset J'$ and $s(J') = s(J) + 1$. By definition of $\mathcal{J}'$, there exists a tile ${\mathfrak p}' \in {\mathfrak T}({\mathfrak u}_1)$ with

$$
{\mathcal{I}}({\mathfrak p}') \subset B(c(J'), 100 D^{s(J') + 1})\,.
$$

By the triangle inequality, the definition [(1)](../../proof-of-metric-space-carleson-overview/README.md) and $a \ge 4$, we have

$$
B(c(J'), 100 D^{s(J')+1}) \subset B({\mathrm{c}}({\mathfrak p}), 128 D^{{\mathrm{s}}({\mathfrak p}) + s_1 + 2})\,.
$$

Since ${\mathfrak p}' \in {\mathfrak T}({\mathfrak u}_1)$ and ${\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak u}_2)$, we have by [(34)](../../proof-of-metric-space-carleson-overview/README.md)

$$
d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak u}_2)) > 2^{Z(n+1)}\,.
$$

Hence, by [(30)](../../proof-of-metric-space-carleson-overview/README.md), the triangle inequality and using that by [(3)](../../proof-of-metric-space-carleson-overview/README.md) $Z(n+1) = 2^{12a}(n+1) \ge 3$

$$
d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) > 2^{Z(n+1)} - 4 \ge 2^{Z(n+1) - 1}\,.
$$

It follows that

$$
2^{Z(n+1)-1} \le d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \le d_{B({\mathrm{c}}({\mathfrak p}), 128 D^{{\mathrm{s}}({\mathfrak p}) + s_1+ 2})}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2))\,.
$$

Using [(8)](../../introduction/README.md), we obtain

$$
\le 2^{9a + 100a^3 (s_1+3)} d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2))\,.
$$

Since ${\mathfrak p}' \notin \mathfrak{S}$ this is bounded by

$$
\le 2^{9a + 100a^3 (s_1+3)} 2^{Zn/2}\,.
$$

Thus

$$
Z n/2 + Z - 1 \le 9a + 100a^3(s_1 + 3)\,,
$$

contradicting the definition of $s_1$.

## Lean

Formalized as [`TileStructure.Forest.thin_scale_impact`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.thin_scale_impact).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6058](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6058)
