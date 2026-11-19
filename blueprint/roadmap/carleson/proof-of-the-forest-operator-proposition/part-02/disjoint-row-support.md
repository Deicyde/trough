---
declaration: lemma
origin: cited
lean: TileStructure.Forest.pairwiseDisjoint_rowSupport
statement: formalized
proof: formalized
---

# disjoint row support

The sets $E_j$, $1 \le j \le 2^n$ are pairwise disjoint.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose that ${\mathfrak p} \in {\mathfrak T}({\mathfrak u})$ and ${\mathfrak p}' \in {\mathfrak T}({\mathfrak u}')$ with ${\mathfrak u} \ne {\mathfrak u}'$ and $x \in E({\mathfrak p}) \cap E({\mathfrak p}')$. Suppose without loss of generality that ${\mathrm{s}}({\mathfrak p}) \le {\mathrm{s}}({\mathfrak p}')$. Then $x \in {\mathcal{I}}({\mathfrak p}) \cap {\mathcal{I}}({\mathfrak p}') \subset {\mathcal{I}}({\mathfrak u}')$. By [(8)](../../proof-of-metric-space-carleson-overview/README.md) it follows that ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u}')$. By [(34)](../../proof-of-metric-space-carleson-overview/README.md), it follows that

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}')) > 2^{Z(n+1)}\,.
$$

By the triangle inequality. [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) and [(30)](../../proof-of-metric-space-carleson-overview/README.md) it follows that

$$
\begin{aligned}
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak p}')) &\ge d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}')) - d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak u}'))\\
&> 2^{Z(n+1)} - d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\mathcal{Q}}({\mathfrak u}'))\\
&\ge 2^{Z(n+1)} - 4\,.
\end{aligned}
$$

Since $Z \ge 3$ by [(3)](../../proof-of-metric-space-carleson-overview/README.md), it follows that ${\mathcal{Q}}({\mathfrak p}') \notin B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 1)$, so $\Omega({\mathfrak p}') \not\subset \Omega({\mathfrak p})$ by [(15)](../../proof-of-metric-space-carleson-overview/README.md). Hence, by [(14)](../../proof-of-metric-space-carleson-overview/README.md), $\Omega({\mathfrak p}) \cap \Omega({\mathfrak p}') = \emptyset$. But if $x \in E({\mathfrak p}) \cap E({\mathfrak p}')$ then $Q(x) \in \Omega({\mathfrak p}) \cap \Omega({\mathfrak p}')$. This is a contradiction, and the lemma follows.

## Lean

Formalized as [`TileStructure.Forest.pairwiseDisjoint_rowSupport`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.pairwiseDisjoint_rowSupport).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6374](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6374)
