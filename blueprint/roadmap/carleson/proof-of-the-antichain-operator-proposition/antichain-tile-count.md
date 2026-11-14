---
declaration: lemma
origin: cited
lean: Antichain.tile_count
statement: formalized
proof: formalized
---

# antichain tile count

Set $p:=4a^4$. For every ${\vartheta}\in{\Theta}$ and every antichain $\mathfrak{A}$ we have

$$
\Big\|\sum_{{\mathfrak p}\in\mathfrak{A}}(1+d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\vartheta}))^{-1/(2a^2+a^3)}\mathbf{1}_{E({\mathfrak p})}\mathbf{1}_G\Big\|_{p}\qquad\text{(26)}
$$

$$
\le
2^{5a}\operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}\mu\left(\cup_{{\mathfrak p}\in\mathfrak{A}}I_{{\mathfrak p}}\right)^{\frac 1p}\, .
$$

## Depends on

- [global antichain density](global-antichain-density.md)

## Proof

*Proof of antichain tile count.* Using that $\mathfrak{A}$ is the disjoint union of the $\mathfrak{A}_{{\vartheta},N}$ with $N\ge 0$, we estimate the left-hand side (26) with the triangle inequality by

$$
\le \sum_{N\ge 0} \left\|\sum_{{\mathfrak p}\in \mathfrak{A}_{{\vartheta},N}} 2^{-N/(2a^2+a^3)}\mathbf{1}_{E({\mathfrak p})} \mathbf{1}_G\right\|_{p}\qquad\text{(27)}
$$

We consider each individual term in this sum and estimate its $p$-th power. Using that for each $x\in X$ by [tile disjointness](tile-disjointness.md) there is at most one ${\mathfrak p}\in \mathfrak{A}$ with $x\in E({\mathfrak p})$, we have

$$
\left\|\sum_{{\mathfrak p}\in \mathfrak{A}_{{\vartheta},N}} 2^{-N/(2a^2+a^3)}\mathbf{1}_{E({\mathfrak p})} \mathbf{1}_G\right\|_{p}^p
$$

$$
=\int\Big(\sum_{{\mathfrak p}\in \mathfrak{A}_{{\vartheta},N}}2^{-N/(2a^2+a^3)}\mathbf{1}_{E({\mathfrak p})\cap G}(x)\Big)^p\, d\mu(x)
$$

$$
=\int\sum_{{\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}}2^{-pN/(2a^2+a^3)}\mathbf{1}_{E({\mathfrak p})\cap G}(x)\, d\mu(x)
$$

$$
= 2^{-pN/(2a^2+a^3)} \sum_{{\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}}\mu(E({\mathfrak p})\cap G)
$$

Using [global antichain density](global-antichain-density.md), we estimate the last display by

$$
\le 2^{-pN/(2a^2+a^3)+101a^3+Na}\operatorname{\operatorname{dens}}_1(\mathfrak{A})\mu\left(\cup_{{\mathfrak p}\in\mathfrak{A}}{\mathcal{I}}({\mathfrak p})\right)\qquad\text{(28)}
$$

Using that $a\ge 4$ and since $p = 4a^4$, we have

$$
pN/(2a^2+a^3)\ge 4a^4N/(3a^3) \ge Na+N\, .
$$

Hence we have for (28) the upper bound

$$
\le 2^{101a^3-N}\operatorname{\operatorname{dens}}_1(\mathfrak{A})\mu\left(\cup_{{\mathfrak p}\in\mathfrak{A}}{\mathcal{I}}({\mathfrak p})\right)\, .
$$

Taking the $p$-th root and summing over $N\ge 0$ gives for (27) the upper bound

$$
\le \left(\sum_{N\ge 0} 2^{-N/p}\right)2^{101a^3/p}\operatorname{\operatorname{dens}}_1(\mathfrak{A})^{{\frac{1}{p}}}\mu\left(\cup_{{\mathfrak p}\in\mathfrak{A}}{\mathcal{I}}({\mathfrak p})\right)^{{\frac{1}{p}}}
$$

$$
= \left(1-2^{-1/p}\right)^{-1} 2^{101a^3/p} \operatorname{\operatorname{dens}}_1(\mathfrak{A})^{\frac 1p}\mu\left(\cup_{{\mathfrak p}\in\mathfrak{A}}{\mathcal{I}}({\mathfrak p})\right)^{\frac 1p}\, .
$$

Using that $p = 4a^4$ and $a \ge 4$, this proves the lemma.

## Lean

Formalized as [`Antichain.tile_count`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Antichain.tile_count).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3731](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3731)
