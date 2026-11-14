---
declaration: lemma
origin: cited
lean: TileStructure.Forest.bound_for_tree_projection
statement: formalized
proof: formalized
---

# bound for tree projection

We have for all bounded $f$ with bounded support

$$
\|P_{\mathcal{J}'}|T_{{\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}}^* g_2|\|_2
\le 2^{102a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \|\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} M_{\mathcal{B},1} |g_2|\|_2
$$

## Depends on

- [adjoint tile support](../part-01/adjoint-tile-support.md)
- [overlap implies distance](../part-01/overlap-implies-distance.md)
- [dyadic partition 2](dyadic-partition-2.md)
- [thin scale impact](thin-scale-impact.md)
- [square function count](square-function-count.md)

## Proof

*Proof of bound for tree projection.* Expanding the definition of $P_{\mathcal{J}'}$, we have

$$
\|P_{\mathcal{J}'}|T_{{\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}}^* g_2|\|_2
$$

$$
= \left(\sum_{J \in \mathcal{J}'} \frac{1}{\mu(J)} \left(\int_J \left| \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}} T_{{\mathfrak p}}^* g_2(y) \right| \, \mathrm{d}\mu(y) \right)^2 \right)^{1/2}\,.
$$

By [adjoint tile support](../part-01/adjoint-tile-support.md), the innermost sum in the last display is $0$ if $J \cap B({\mathcal{I}}({\mathfrak p})) = \emptyset$. Then we split that sum according to the scale of ${\mathfrak p}$ relative to the scale of $J$. By [thin scale impact](thin-scale-impact.md), $s_1 \le s(J) - {\mathrm{s}}({\mathfrak p}) \le 2S$ with $s_1 := \lfloor\frac{Zn}{202a^3} - 2\rfloor$:

$$
= \left(\sum_{J \in \mathcal{J}'} \frac{1}{\mu(J)} \left(\int_J \left| \sum_{s=s_1}^{2S} \sum_{\substack{{\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}\\ {\mathrm{s}}({\mathfrak p}) = s(J) - s\\
J \cap B({\mathcal{I}}({\mathfrak p})) \ne \emptyset}} T_{{\mathfrak p}}^* g_2(y) \right| \, \mathrm{d}\mu(y) \right)^2 \right)^{1/2}\,.
$$

Then we apply the triangle inequality and Minkowski's inequality to get

$$
\le \sum_{s=s_1}^{2S} \left( \sum_{J \in \mathcal{J}'} \frac{1}{\mu(J)} \left(\int_J \sum_{\substack{{\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}\\ {\mathrm{s}}({\mathfrak p}) = s(J) - s\\
J \cap B({\mathcal{I}}({\mathfrak p})) \ne \emptyset}} |T_{{\mathfrak p}}^* g_2(y)| \, \mathrm{d}\mu(y) \right)^2\right)^{1/2}\,.\qquad\text{(56)}
$$

We have by [adjoint tile support](../part-01/adjoint-tile-support.md) and [(66)](../../proof-of-metric-space-carleson-overview/kernel-summand.md)

$$
|T_{{\mathfrak p}}^* g_2(y)| \le 2^{102a^3} \mathbf{1}_{B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})})}(y) \int_{E({\mathfrak p})} \frac{1}{\mu(B(x, D^{{\mathrm{s}}({\mathfrak p})}))} |g_2(x)| \, \mathrm{d}\mu(x)\,.
$$

Using the doubling property [(5)](../../introduction/README.md), it follows that

$$
\mu(B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})})) \le 2^{4a} \mu(B(x, D^{{\mathrm{s}}({\mathfrak p})}))\,.
$$

Thus, using also $a \ge 4$

$$
|T_{{\mathfrak p}}^* g_2(y)| \le 2^{102a^3+4a} \mathbf{1}_{B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})})}(y) \frac{1}{\mu(B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})}))} \int_{E({\mathfrak p})} |g_2(x)| \, \mathrm{d}\mu(x)\,.
$$

Since for each $I \in \mathcal{D}$ the sets $E({\mathfrak p}), {\mathfrak p} \in {\mathfrak P}(I)$ are disjoint, it follows that

$$
\int_J \sum_{\substack{{\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}\\ {\mathcal{I}}({\mathfrak p}) = I\\
J \cap B({\mathcal{I}}({\mathfrak p})) \ne \emptyset}} |T_{{\mathfrak p}}^* g_2(y)| \, \mathrm{d}\mu
$$

$$
\le 2^{102a^3+4a} \int_J \mathbf{1}_{B(I)} \frac{1}{\mu(B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})}))} \int_{B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})})} |g_2(x)| \, \mathrm{d}\mu(x)
$$

$$
\le 2^{102a^3+4a} \int_J M_{\mathcal{B},1} |g_2|(y) \mathbf{1}_{B(I)}(y) \, \mathrm{d}\mu(y)\,.
$$

By [overlap implies distance](../part-01/overlap-implies-distance.md), we have ${\mathcal{I}}({\mathfrak p}) \cap {\mathcal{I}}({\mathfrak u}_1) = \emptyset$ for all ${\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}$. Thus we can estimate (56) by

$$
2^{102a^3+4a} \sum_{s=s_1}^{2S} \left( \sum_{J \in \mathcal{J}'} \frac{1}{\mu(J)} \left(\int_J \sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap {\mathcal{I}}({\mathfrak u}_1) = \emptyset\\
J \cap B(I) \ne \emptyset}} M_{\mathcal{B},1} |g_2| \mathbf{1}_{B(I)} \, \mathrm{d}\mu \right)^2\right)^{1/2}\,,
$$

which is by Cauchy-Schwarz at most

$$
2^{102a^3+4a} \sum_{s=s_1}^{2S} \left( \sum_{J \in \mathcal{J}'} \int_J ( M_{\mathcal{B},1} |g_2|)^2 \, \mathrm{d}\mu \times
\frac{1}{\mu(J)} \int_J \left(\sum_{\substack{I \in \mathcal{D}, s(I) = s(J) - s\\ I \cap {\mathcal{I}}({\mathfrak u}_1) = \emptyset\\
J \cap B(I) \ne \emptyset}} \mathbf{1}_{B(I)}\right)^2 \, \mathrm{d}\mu \right)^{1/2}\,.\qquad\text{(57)}
$$

Using [square function count](square-function-count.md), we bound (57) by

$$
2^{102a^3+4a} \sum_{s=s_1}^{2S} \left(2^{14a+1} (8 D^{-s})^\kappa \sum_{J \in \mathcal{J}'} \int_J (M_{\mathcal{B},1} |g_2|)^2\right)^{1/2}\,,
$$

and since dyadic cubes in $\mathcal{J}'$ form a partition of ${\mathcal{I}}({\mathfrak u}_1)$ by [dyadic partition 2](dyadic-partition-2.md), $\kappa \le 1$ by [(2)](../../proof-of-metric-space-carleson-overview/README.md), and $a \ge 4$

$$
\le 2^{102a^3+11a+2} \sum_{s=s_1}^{2S} D^{-s\kappa/2} \|\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} M_{\mathcal{B},1} |g_2|\|_2
$$

$$
\le 2^{102a^3+11a+2} D^{-s_1 \kappa /2} \frac{1}{1 - D^{-\kappa/2}} \|\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} M_{\mathcal{B},1} |g_2|\|_2\,.
$$

By convexity of $t \mapsto D^{-t}$ and since $D \ge 2$, we have for all $0 \le t \le 1$

$$
D^{-t} \le 1 - t(1 - 1/D) \le 1 - \frac{1}{2}t\,.
$$

Using this for $t = \kappa/2$ and using that $s_1 = \frac{Zn}{202a^3} - 2$ and the definitions [(1)](../../proof-of-metric-space-carleson-overview/README.md) and [(2)](../../proof-of-metric-space-carleson-overview/README.md) of $\kappa$ and $D$

$$
\le 2^{102a^3+11a+2} 2^{-100a^2(\frac{Zn}{202a^3} - 3) \frac{\kappa}{2}} \frac{2}{\kappa} \|\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} M_{\mathcal{B},1} |g_2|\|_2
$$

$$
= 2^{102a^3+21a+4} 2^{150a^2\kappa} 2^{-\frac{100}{404a}Zn\kappa} \|\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} M_{\mathcal{B},1} |g_2|\|_2\,.
$$

Using the definition [(2)](../../proof-of-metric-space-carleson-overview/README.md) of $\kappa$ and $a \ge 4$, the lemma follows.

## Lean

Formalized as [`TileStructure.Forest.bound_for_tree_projection`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.bound_for_tree_projection).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6024](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6024)
