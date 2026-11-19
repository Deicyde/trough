---
declaration: proposition
origin: cited
lean: forest_operator
statement: formalized
proof: formalized
---

# forest operator

For any $n\ge 0$ and any $n$-forest $({\mathfrak U},{\mathfrak T})$ we have for all $f,g: X \to \mathbb{C}$ with $|f| \le \mathbf{1}_F$ and $|g| \le \mathbf{1}_G$

$$
| \int \overline{g(x)} \sum_{{\mathfrak u}\in {\mathfrak U}} \sum_{{\mathfrak p}\in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f(x) \, \mathrm{d}\mu(x)|
$$

$$
\le
2^{440a^3}2^{-\frac{q-1}{q} n} \operatorname{\operatorname{dens}}_2\left(\bigcup_{{\mathfrak u}\in {\mathfrak U}}{\mathfrak T}({\mathfrak u})\right)^{\frac{1}{q}-\frac{1}{2}} \|f\|_2 \|g\|_2 \,.
$$

## Depends on

- [forest row decomposition](../proof-of-the-forest-operator-proposition/part-02/forest-row-decomposition.md)
- [row bound](../proof-of-the-forest-operator-proposition/part-02/row-bound.md)
- [row correlation](../proof-of-the-forest-operator-proposition/part-02/row-correlation.md)
- [disjoint row support](../proof-of-the-forest-operator-proposition/part-02/disjoint-row-support.md)

## Proof

*Proof of forest operator.* By [(25)](../proof-of-the-forest-operator-proposition/part-01/README.md), we have for each $j$

$$
T_{\mathfrak{R}_j}^*g = \sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g = \sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* \mathbf{1}_{E_j} g = T_{\mathfrak{R}_j}^* \mathbf{1}_{E_j} g\,.
$$

Hence, by [forest row decomposition](../proof-of-the-forest-operator-proposition/part-02/forest-row-decomposition.md) and the triangle inequality,

$$
\left\|\sum_{{\mathfrak u} \in {\mathfrak U}} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T^*_{{\mathfrak p}} g\right\|_2^2 = \left\|\sum_{j = 1}^{2^n} T^*_{\mathfrak{R}_{j}} g\right\|_2^2 = \left\|\sum_{j=1}^{2^n} T^*_{\mathfrak{R}_{j}} \mathbf{1}_{E_j} g\right\|_2^2
$$

$$
= \int_X \left|\sum_{j=1}^{2^n} T^*_{\mathfrak{R}_{j}} \mathbf{1}_{E_j} g\right|^2 \, \mathrm{d}\mu
$$

$$
\le \sum_{j=1}^{2^n} \|T_{\mathfrak{R}_j}^* \mathbf{1}_{E_j} g\|_2^2 + \sum_{j =1}^{2^n} \sum_{\substack{j' = 1\\j' \ne j}}^{2^n} \left| \int_X \overline{ T_{\mathfrak{R}_j}^* \mathbf{1}_{E_j} g} T_{\mathfrak{R}_{j'}}^* \mathbf{1}_{E_{j'}} g \right| \, \mathrm{d}\mu\,.
$$

We use [row bound](../proof-of-the-forest-operator-proposition/part-02/row-bound.md) to estimate each term in the first sum, and [row correlation](../proof-of-the-forest-operator-proposition/part-02/row-correlation.md) to bound each term in the second sum:

$$
\le 2^{566a^3-n} \sum_{j = 1}^{2^n} \|\mathbf{1}_{E_j} g\|_2^2 + 2^{876a^3-4n}\sum_{j=1}^{2^n}\sum_{j' = 1}^{2^n} \|\mathbf{1}_{E_j} g\|_2 \|\mathbf{1}_{E_{j'}}g\|_2\,.
$$

By Cauchy-Schwarz in the second two sums, this is at most

$$
2^{876a^3} (2^{-n} + 2^{n}2^{-4n}) \sum_{j = 1}^n \|\mathbf{1}_{E_j} g\|_2^2\,,
$$

and by disjointedness of the sets $E_j$, this is at most

$$
2^{877a^3 - n} \|g\|_2^2\,.
$$

Taking square roots, it follows that for all $g$

$$
\left\|\sum_{{\mathfrak u} \in {\mathfrak U}} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g\right\|_2 \le 2^{439a^3-\frac{n}{2}} \|g\|_2\,.\qquad\text{(36)}
$$

On the other hand, we have by disjointedness of the sets $E_j$ from [disjoint row support](../proof-of-the-forest-operator-proposition/part-02/disjoint-row-support.md) and the triangle inequality

$$
\left\|\mathbf{1}_G \sum_{{\mathfrak u} \in {\mathfrak U}} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f\right\|_2^2 = \left\|\sum_{j=1}^{2^n} \mathbf{1}_{E_j} \mathbf{1}_G T_{\mathfrak{R}_{j}} f\right\|_2^2 \le \sum_{j = 1}^{2^n} \|\mathbf{1}_{E_j} \mathbf{1}_G T_{\mathfrak{R}_{j}} f\|_2^2 \le \sum_{j = 1}^{2^n} \|\mathbf{1}_G T_{\mathfrak{R}_{j}} f\|_2^2\,.
$$

Now with $|f| \le \mathbf{1}_F$ and [row bound](../proof-of-the-forest-operator-proposition/part-02/row-bound.md) we obtain

$$
\| \mathbf{1}_G T_{\mathfrak{R}_j} f \|_2^2 = \left| \int_X \overline{\mathbf{1}_G T_{\mathfrak{R}_j} f} T_{\mathfrak{R}_j} f \right| = \left| \int_X \overline{T_{\mathfrak{R}_j}^* \mathbf{1}_G T_{\mathfrak{R}_j} f} \mathbf{1}_F f \right|
$$

$$
\le \|f\|_2 \| \mathbf{1}_F T_{\mathfrak{R}_j}^* \mathbf{1}_G T_{\mathfrak{R}_j} f \|_2 \le 2^{283a^3-n/2} \operatorname{\operatorname{dens}}_2(\bigcup_{{\mathfrak u}\in {\mathfrak U}}{\mathfrak T}({\mathfrak u}))^{1/2} \| \mathbf{1}_G T_{\mathfrak{R}_j} f \|_2 \|f\|_2.
$$

Dividing this last inequality by the finite $\| \mathbf{1}_G T_{\mathfrak{R}_j} f \|_2$, substituting back and taking square roots we get

$$
\left\|\mathbf{1}_G \sum_{{\mathfrak u} \in {\mathfrak U}} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f\right\|_2 \le 2^{283a^3} \operatorname{\operatorname{dens}}_2(\bigcup_{{\mathfrak u}\in {\mathfrak U}}{\mathfrak T}({\mathfrak u}))^{\frac{1}{2}} 2^{-\frac{n}{2}} (\sum_{j = 1}^{2^n} \|f\|_2^2)^{\frac{1}{2}}
$$

$$
= 2^{283a^3} \operatorname{\operatorname{dens}}_2(\bigcup_{{\mathfrak u}\in {\mathfrak U}}{\mathfrak T}({\mathfrak u}))^{\frac{1}{2}} \|f\|_2\,.\qquad\text{(37)}
$$

forest operator follows by taking the product of the $(2 - \frac{2}{q})$-th power of (36) and the $(\frac{2}{q} - 1)$-st power of (37).

## Lean

Formalized as [`forest_operator`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_operator).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 702](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L702)
