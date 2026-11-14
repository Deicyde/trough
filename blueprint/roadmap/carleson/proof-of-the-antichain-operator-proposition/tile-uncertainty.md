---
declaration: lemma
origin: cited
lean: Tile.uncertainty
statement: formalized
proof: formalized
---

# tile-uncertainty

Let ${\mathfrak p}_1, {\mathfrak p}_2\in {\mathfrak P}$ with $B({\mathrm{c}}({\mathfrak p}_1),5D^{{\mathrm{s}}({\mathfrak p}_1)}) \cap B({\mathrm{c}}({\mathfrak p}_2),5D^{{\mathrm{s}}({\mathfrak p}_2)}) \ne \emptyset$ and ${\mathrm{s}}({{\mathfrak p}_1})\leq {\mathrm{s}}({{\mathfrak p}_2})$. For each $x_1\in E({\mathfrak p}_1)$ and $x_2\in E({\mathfrak p}_2)$ we have

$$
1+d_{{\mathfrak p}_1}({\mathcal{Q}}({\mathfrak p}_1), {\mathcal{Q}}({\mathfrak p}_2))\le
2^{8a}(1 + d_{B(x_1, D^{{\mathrm{s}}({\mathfrak p}_1)})}({Q}(x_1),{Q}(x_2)))\, .\qquad\text{(35)}
$$

## Depends on

- [monotone cube metrics](../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)
- [tile range support](tile-range-support.md)

## Proof

Let $i\in \{1,2\}$. By Definition [(19)](../proof-of-metric-space-carleson-overview/discrete-carleson.md) of $E$, we have ${Q}(x_i)\in {\Omega}({\mathfrak p}_i)$ With [(15)](../proof-of-metric-space-carleson-overview/README.md) we then conclude

$$
d_{{\mathfrak p}_i}({Q}(x_i),{\mathcal{Q}}({\mathfrak p}_i)) < 1\, .\qquad\text{(36)}
$$

We have by the triangle inequality and [(10)](../proof-of-metric-space-carleson-overview/README.md) that ${\mathcal{I}}({\mathfrak p}_1) \subset B({\mathrm{c}}({\mathfrak p}_2),14D^{{\mathrm{s}}({\mathfrak p}_2)})$. Thus, using again [(10)](../proof-of-metric-space-carleson-overview/README.md) and the doubling property [(8)](../introduction/README.md)

$$
d_{{\mathfrak p}_1}({Q}(x_2), {\mathcal{Q}}({\mathfrak p}_2)) \le 2^{6a} d_{{\mathfrak p}_2}({Q}(x_2), {\mathcal{Q}}({\mathfrak p}_2)) \le 2^{6a}\,.\qquad\text{(37)}
$$

By the triangle inequality, we obtain from (36) and (37)

$$
1+d_{{\mathfrak p}_1}({\mathcal{Q}}({\mathfrak p}_1), {\mathcal{Q}}({\mathfrak p}_2))\le 2 + 2^{6a} +d_{{\mathfrak p}_1}({Q}(x_1), {Q}(x_2))\, .\qquad\text{(38)}
$$

As $x_1\in {\mathcal{I}}({\mathfrak p}_1)$ by Definition [(19)](../proof-of-metric-space-carleson-overview/discrete-carleson.md) of $E$, we have by the squeezing property [(10)](../proof-of-metric-space-carleson-overview/README.md)

$$
d(x_1,{\mathrm{c}}({\mathfrak p}_1))\le 4D^{{\mathrm{s}}({\mathfrak p}_1)}
$$

and thus by [(10)](../proof-of-metric-space-carleson-overview/README.md) again and the triangle inequality

$$
{\mathcal{I}}({\mathfrak p}_1)\subset B(x_1,8D^{{\mathrm{s}}({\mathfrak p}_1)})\, .
$$

We thus estimate the right-hand side of (38) with monotonicity [(9)](../introduction/README.md) of the metrics $d_B$ by

$$
\le 2 + 2^{6a} + d_{B(x_1,8D^{{\mathrm{s}}({\mathfrak p}_1)})}({Q}(x_1), {Q}(x_2))\, .\qquad\text{(39)}
$$

This is further estimated by applying the doubling property [(8)](../introduction/README.md) three times by

$$
\le 2 + 2^{6a} +2^{3a}d_{B_1(x_1, D^{{\mathrm{s}}({\mathfrak p}_1)})}({Q}(x_1), {Q}(x_2))\, .\qquad\text{(40)}
$$

Now (35) follows with $a\ge 4$.

## Lean

Formalized as [`Tile.uncertainty`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Tile.uncertainty).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3866](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3866)
