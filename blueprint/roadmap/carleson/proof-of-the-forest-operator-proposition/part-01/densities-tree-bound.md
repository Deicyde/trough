---
declaration: lemma
origin: cited
lean: TileStructure.Forest.density_tree_bound1, TileStructure.Forest.density_tree_bound2
statement: formalized
proof: formalized
---

# densities tree bound

Let ${\mathfrak u} \in {\mathfrak U}$. Then for all bounded $f$ with bounded support and bounded $g$ supported on $G$ we have

$$
\left|\int_X \bar g \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p} }f \, \mathrm{d}\mu \right| \le 2^{181a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))^{1/2} \|f\|_2\|g\|_2\,.\qquad\text{(17)}
$$

If additionally $\text{support}(f) \subseteq F$, then we have

$$
\left| \int_X \bar g \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p} }f\, \mathrm{d}\mu \right| \le 2^{282a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))^{1/2} \operatorname{\operatorname{dens}}_2({\mathfrak T}({\mathfrak u}))^{1/2} \|f\|_2\|g\|_2\,.\qquad\text{(18)}
$$

## Depends on

- [tree projection estimate](tree-projection-estimate.md)
- [local dens1 tree bound](local-dens1-tree-bound.md)
- [local dens2 tree bound](local-dens2-tree-bound.md)

## Proof

*Proof of densities tree bound.* Denote

$$
\mathcal{E}({\mathfrak u}) = \bigcup_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} E({\mathfrak p})\,.
$$

Then we have

$$
\left| \int_X \bar g \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f \, \mathrm{d}\mu \right| = \left| \int_X \overline{ g\mathbf{1}_{\mathcal{E}({\mathfrak u})}} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}f) \, \mathrm{d}\mu \right|\,.
$$

By [tree projection estimate](tree-projection-estimate.md), this is bounded by

$$
\le 2^{130a^3}\|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|\|_2 \|P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))} |\mathbf{1}_{\mathcal{E}({\mathfrak u})}g|\|_2\,.\qquad\text{(19)}
$$

We bound the two factors separately. We have

$$
\|P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))} |\mathbf{1}_{\mathcal{E}({\mathfrak u})}g|\|_2 = \left( \sum_{L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))} \frac{1}{\mu(L)} \left(\int_{L \cap \mathcal{E}({\mathfrak u})} |g(y)| \, \mathrm{d}\mu(y)\right)^2 \right)^{1/2}\,.
$$

By Cauchy-Schwarz and [local dens1 tree bound](local-dens1-tree-bound.md) this is at most

$$
\le \left( \sum_{L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))} 2^{101a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u})) \int_{L \cap \mathcal{E}({\mathfrak u})} |g(y)|^2 \, \mathrm{d}\mu(y) \right)^{1/2}\,.
$$

Since cubes $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$ are pairwise disjoint by [dyadic partitions](dyadic-partitions.md), this is

$$
\le 2^{51 a^3} \operatorname{\operatorname{dens}}_1({\mathfrak T}({\mathfrak u}))^{1/2} \|g\|_2\,.\qquad\text{(20)}
$$

Similarly, we have

$$
\|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|\|_2 = \left( \sum_{J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))} \frac{1}{\mu(J)} \left(\int_J |f(y)| \, \mathrm{d}\mu(y)\right)^2 \right)^{1/2}\,.\qquad\text{(21)}
$$

By Cauchy-Schwarz, this is

$$
\le \left( \sum_{J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))} \int_J |f(y)|^2 \, \mathrm{d}\mu(y) \right)^{1/2}\,.
$$

Since cubes in $\mathcal{J}({\mathfrak T}({\mathfrak u}))$ are pairwise disjoint by [dyadic partitions](dyadic-partitions.md), this is at most

$$
\|f\|_2\,.\qquad\text{(22)}
$$

Combining (19), (20) and (22) gives (17).

If $f \le \mathbf{1}_F$ then $f = f\mathbf{1}_F$, so

$$
\left( \sum_{J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))} \frac{1}{\mu(J)} \left(\int_J |f(y)| \, \mathrm{d}\mu(y)\right)^2 \right)^{1/2}
$$

$$
=\left(\sum_{J \in \mathcal{J}({\mathfrak T}({\mathfrak u}))} \frac{1}{\mu(J)} \left(\int_{J \cap F} |f(y)| \, \mathrm{d}\mu(y)\right)^2 \right)^{1/2}\,.
$$

We estimate as before, using now [local dens2 tree bound](local-dens2-tree-bound.md) and Cauchy-Schwarz, and obtain that this is

$$
\le 2^{101a^3} \operatorname{\operatorname{dens}}_2({\mathfrak T}({\mathfrak u}))^{1/2} \|f\|_2\,.
$$

Combining this with (19) and (20) gives (18).

## Lean

Formalized as [`TileStructure.Forest.density_tree_bound1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.density_tree_bound1), [`TileStructure.Forest.density_tree_bound2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.density_tree_bound2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4957](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4957)
