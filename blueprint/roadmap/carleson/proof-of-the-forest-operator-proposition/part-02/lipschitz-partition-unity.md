---
declaration: lemma
origin: cited
lean: TileStructure.Forest.sum_χ, TileStructure.Forest.χ_le_indicator, TileStructure.Forest.dist_χ_le
statement: formalized
proof: formalized
---

# Lipschitz partition unity

There exists a family of functions $\chi_J$, $J \in \mathcal{J}'$ such that

$$
\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} = \sum_{J \in \mathcal{J}'} \chi_J\,,\qquad\text{(36)}
$$

and for all $J \in \mathcal{J}'$ and all $y,y' \in {\mathcal{I}}({\mathfrak u}_1)$

$$
0 \leq \chi_J(y) \leq \mathbf{1}_{B(J)}(y)\,,\qquad\text{(37)}
$$

$$
|\chi_J(y) - \chi_J(y')| \le 2^{227a^3} \frac{\rho(y,y')}{D^{s(J)}}\,.\qquad\text{(38)}
$$

## Depends on

- [dyadic partition 1](dyadic-partition-1.md)
- [moderate scale change](moderate-scale-change.md)

## Proof

*Proof of Lipschitz partition unity.* For each cube $J \in \mathcal{J}$ let

$$
\tilde\chi_J(y) = \mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)}(y)\max\{0, 8 - D^{-s(J)} \rho(y, c(J))\}\,,
$$

and set

$$
a(y) = \sum_{J \in \mathcal{J}'} \tilde \chi_J(y)\,.
$$

We define

$$
\chi_J(y) := \frac{\tilde \chi_J(y)}{a(y)}\,.
$$

Then, due to [(35)](../../proof-of-metric-space-carleson-overview/README.md) and [(35)](README.md), the properties (36) and (37) are clearly true. Estimate (38) follows from (37) if $y, y' \notin B(J)$. Thus we can assume that $y \in B(J)$. We have by the triangle inequality

$$
|\chi_J(y) - \chi_J(y')| \le \frac{|\tilde \chi_J(y) - \tilde \chi_J(y')|}{a(y)} + \frac{\tilde \chi_J(y')|a(y) - a(y')|}{a(y)a(y')}
$$

Since $\tilde \chi_J(z) \ge 4$ for all $z \in B(c(J),4D^{s(J)}) \supset J$ and by [dyadic partition 1](dyadic-partition-1.md), we have that $a(z) \ge 4$ for all $z \in {\mathcal{I}}({\mathfrak u}_1)$. So we can estimate the above further by

$$
\le 2^{-2}(|\tilde \chi_J(y) - \tilde \chi_J(y')| + \tilde \chi_J(y')|a(y) - a(y')|)\,.
$$

If $y' \notin B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})})$ then the second summand vanishes. Else, we can estimate the above, using also that $|\tilde \chi_J(y')| \le 8$, by

$$
\le 2^{-2} |\tilde \chi_J(y) - \tilde \chi_J(y')| + 2 \sum_{\substack{J' \in \mathcal{J}'\\ B(J') \cap B(J) \ne \emptyset}}|\tilde \chi_{J'}(y) - \tilde \chi_{J'} (y')|\,.
$$

By the triangle inequality, we have for all dyadic cubes $I$

$$
|\tilde \chi_I(y) - \tilde \chi_I(y')| \le \rho(y, y') D^{-s(I)}\,.
$$

Using this above, we obtain

$$
|\chi_J(y) - \chi_J(y')| \le \rho(y,y') \Big( \frac{1}{4} D^{-s(J)} + 2 \sum_{\substack{J' \in \mathcal{J}'\\ B(J') \cap B(J) \ne \emptyset}} D^{-s(J')}\Big)\,.
$$

By [moderate scale change](moderate-scale-change.md), this is at most

$$
\frac{\rho(y,y')}{D^{s(J)}} \left( \frac{1}{4} + 2D |\{J' \in \mathcal{J}' \ : \ B(J') \cap B(J) \ne \emptyset\}|\right)\,.
$$

By [(10)](../../proof-of-metric-space-carleson-overview/README.md) and [dyadic partition 1](dyadic-partition-1.md), the balls $B(c(J'), \frac{1}{4} D^{s(J')})$ are pairwise disjoint. By the triangle inequality and [moderate scale change](moderate-scale-change.md), each such ball for $J'$ in the set of the last display is contained in

$$
B(c(J), 9 D^{s(J) + 1})\,.
$$

By the doubling property [(5)](../../introduction/README.md), we further have

$$
\mu(B(c(J), 9 D^{s(J) + 1})) \le 2^{200a^3 + 7a} \mu\Big(B(c(J'), \frac{1}{4}D^{s(J')})\Big)
$$

for each such ball. Thus

$$
|\{J' \in \mathcal{J}' \ : \ B(J') \cap B(J) \ne \emptyset\}| \le 2^{200a^3 + 7a}\,.
$$

Recalling that $D=2^{100a^2}$, we obtain

$$
\frac{1}{4} + 2D |\{J' \in \mathcal{J}' \ : \ B(J') \cap B(J) \ne \emptyset\}|\leq 2^{200a^3 + 100a^2 + 7a + 2}.
$$

Since $a\ge 4$, (38) follows.

## Lean

Formalized as [`TileStructure.Forest.sum_χ`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.sum_χ), [`TileStructure.Forest.χ_le_indicator`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.χ_le_indicator), [`TileStructure.Forest.dist_χ_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.dist_χ_le).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5424](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5424)
