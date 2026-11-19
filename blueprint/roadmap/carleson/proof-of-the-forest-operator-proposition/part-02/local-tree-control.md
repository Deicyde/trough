---
declaration: lemma
origin: cited
lean: TileStructure.Forest.local_tree_control
statement: formalized
proof: formalized
---

# local tree control

For all $J \in \mathcal{J}'$ and all bounded $g$ with bounded support

$$
\sup_{B^\circ{}(J)} |T_{\mathfrak{T}(\mathfrak{u}_2)\setminus\mathfrak{S}}^* g| \le 2^{104a^3} \inf_J M_{\mathcal{B},1}|g|
$$

## Depends on

- [limited scale impact](limited-scale-impact.md)

## Proof

By the triangle inequality and since $T_{{\mathfrak p}}^* g = \mathbf{1}_{B({\mathrm{c}}({\mathfrak p}), 5D^{{\mathrm{s}}({\mathfrak p})})} T_{{\mathfrak p}}^* g$, we have

$$
\sup_{B^\circ{}(J)} |T_{{\mathfrak T}({\mathfrak u}_2) \setminus\mathfrak{S}}^* g|
\leq \sup_{B^\circ{}(J)} \sum_{\substack{{\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}\\ B({\mathcal{I}}({\mathfrak p})) \cap B^\circ(J) \ne \emptyset}} |T_{{\mathfrak p}}^*g|\,.
$$

By [limited scale impact](limited-scale-impact.md), this is at most

$$
\sum_{s = s(J)}^{s(J) + 3} \sum_{\substack{{\mathfrak p} \in {\mathfrak P}, {\mathrm{s}}({\mathfrak p}) = s\\ B({\mathcal{I}}({\mathfrak p})) \cap B^\circ(J) \ne \emptyset}} \sup_{B^\circ{}(J)} |T_{{\mathfrak p}}^* g|\,.\qquad\text{(52)}
$$

If $x \in E({\mathfrak p})$ and $B({\mathcal{I}}({\mathfrak p})) \cap B^\circ(J) \ne \emptyset$, then

$$
B(c(J), 16D^{{\mathrm{s}}({\mathfrak p})}) \subset B(x, 32 D^{{\mathrm{s}}({\mathfrak p})})\,,
$$

by [(10)](../../proof-of-metric-space-carleson-overview/README.md) and the triangle inequality. Using the doubling property [(5)](../../introduction/README.md), it follows that

$$
\mu(B(x, D^{{\mathrm{s}}({\mathfrak p})})) \ge 2^{-5a} \mu(B(c(J), 16D^{{\mathrm{s}}({\mathfrak p})}))\,.
$$

Using [(25)](../part-01/README.md), [(66)](../../proof-of-metric-space-carleson-overview/kernel-summand.md) and that $a \ge 4$, we bound (52) by

$$
2^{103a^3}\sum_{s = s(J)}^{s(J) + 3} \sum_{\substack{{\mathfrak p} \in {\mathfrak P}, {\mathrm{s}}({\mathfrak p}) = s\\B({\mathcal{I}}({\mathfrak p})) \cap B^\circ(J) \ne \emptyset}} \frac{1}{\mu(B(c(J), 16 D^s)} \int_{E({\mathfrak p})} |g| \, \mathrm{d}\mu\,.
$$

For each $I \in \mathcal{D}$, the sets $E({\mathfrak p})$ for ${\mathfrak p} \in {\mathfrak P}$ with ${\mathcal{I}}({\mathfrak p}) = I$ are pairwise disjoint by [(19)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md) and [(13)](../../proof-of-metric-space-carleson-overview/README.md). Further, if $B({\mathcal{I}}({\mathfrak p})) \cap B^\circ(J) \ne \emptyset$ and ${\mathrm{s}}({\mathfrak p}) \ge s(J)$, then $E({\mathfrak p}) \subset B(c(J), 16 D^{{\mathrm{s}}({\mathfrak p})})$. Thus the last display is bounded by

$$
2^{103a^3}\sum_{s = s(J)}^{s(J) + 3} \frac{1}{\mu(B(c(J), 16 D^s))} \int_{B(c(J), 16 D^s)} |g| \, \mathrm{d}\mu\,.
$$

$$
\le \inf_{x' \in J} 2^{103a^3 +2} M_{\mathcal{B}, 1} |g|\,.
$$

The lemma follows since $a \ge 4$.

## Lean

Formalized as [`TileStructure.Forest.local_tree_control`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.local_tree_control).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5743](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5743)
