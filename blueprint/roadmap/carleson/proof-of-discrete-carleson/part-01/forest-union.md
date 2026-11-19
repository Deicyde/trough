---
declaration: lemma
origin: cited
lean: forest_union
statement: formalized
proof: formalized
---

# forest union

Let

$$
{\mathfrak P}_1 =\bigcup_{k\ge 0}\bigcup_{n\ge k}
\bigcup_{0\le j\le 2n+3}{\mathfrak C}_5(k,n,j)
$$

For all $f:X\to {\mathbb{C}}$ with $|f|\le \mathbf{1}_F$ we have

$$
\int_{G \setminus G'} \left|\sum_{{\mathfrak p} \in {\mathfrak P}_1} T_{{\mathfrak p}} f \right|\, \mathrm{d}\mu \le \frac{2^{441a^3}}{(q-1)^4} \mu(G)^{1 - \frac{1}{q}} \mu(F)^{\frac{1}{q}}\,.\qquad\text{(25)}
$$

## Depends on

- [forest operator](../../proof-of-metric-space-carleson-overview/forest-operator.md)
- [C dens1](../part-02/c-dens1.md)
- [C6 forest](../part-02/c6-forest.md)
- [forest geometry](../part-02/forest-geometry.md)
- [forest convex](../part-02/forest-convex.md)
- [forest separation](../part-02/forest-separation.md)
- [forest inner](../part-02/forest-inner.md)
- [forest stacking](../part-02/forest-stacking.md)

## Proof

*Proof of forest union.* We first fix $k,n, j$. By [(20)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md) and [(19)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md), we have that $\mathbf{1}_{{\mathcal{I}}({\mathfrak p})} T_{{\mathfrak p}}f(x) = T_{{\mathfrak p}}f(x)$ and hence $\mathbf{1}_{G \setminus G'} T_{{\mathfrak p}}f(x)= 0$ for all ${\mathfrak p} \in {\mathfrak C}_5(k,n,j) \setminus {\mathfrak C}_6(k,n,j)$. Thus it suffices to estimate the contribution of the sets ${\mathfrak C}_6(k,n,j)$. By [forest stacking](../part-02/forest-stacking.md), we can decompose ${\mathfrak U}_3(k,n,j)$ as a disjoint union of at most $4n + 12$ collections ${\mathfrak U}_4(k,n,j,l)$, $1 \le l \le 4n+12$, each satisfying

$$
\sum_{{\mathfrak u} \in {\mathfrak U}_4(k,n,j,l)} \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} \le 2^n\,.
$$

By Lemmas [forest geometry](../part-02/forest-geometry.md), [forest convex](../part-02/forest-convex.md), [forest separation](../part-02/forest-separation.md), [forest inner](../part-02/forest-inner.md) and [C dens1](../part-02/c-dens1.md), the pairs

$$
({\mathfrak U}_4(k,n,j,l), \mathfrak{T}_2|_{{\mathfrak U}_4(k,n,j,l)})
$$

are $n$-forests for each $k,n,j,l$, and by [C6 forest](../part-02/c6-forest.md), we have

$$
{\mathfrak C}_6(k,n,j) = \bigcup_{l = 1}^{4n + 12} \bigcup_{{\mathfrak u} \in {\mathfrak U}_4(k,n,j,l)} \mathfrak{T}_2({\mathfrak u})\,.
$$

Since ${\mathcal{I}}({\mathfrak p}) \not\subset G_1$ for all ${\mathfrak p} \in {\mathfrak C}_6(k,n,j)$, we have ${\mathfrak C}_6(k,n,j) \cap {\mathfrak P}_{F,G} = \emptyset$ and hence

$$
\operatorname{\operatorname{dens}}_2(\bigcup_{{\mathfrak u} \in {\mathfrak U}_4(k,n,j,l)} \mathfrak{T}_2({\mathfrak u})) \le 2^{2a + 5} \frac{\mu(F)}{\mu(G)}\,.
$$

Using the triangle inequality according to the splitting by $k,n,j$ and $l$ in (25) and applying [forest operator](../../proof-of-metric-space-carleson-overview/forest-operator.md) to each term, we obtain the estimate

$$
\sum_{k \ge 0}\sum_{n \ge k} (2n+3)(4n+12) 2^{440a^3}2^{-(1-\frac{1}{q})n}(2^{2a+5} \frac{\mu(F)}{\mu(G)})^{\frac{1}{q} - \frac{1}{2}} \|f\|_2 \|\mathbf{1}_{G\setminus G'}\|_2
$$

for the left hand side of (25). Since $|f| \le \mathbf{1}_F$, we have $\|f\|_2 \le \mu(F)^{1/2}$, and we have $\|\mathbf{1}_{G\setminus G'}\|_2 \le \mu(G)^{1/2}$. We get a bound

$$
2^{440a^3} \mu(F)^{\frac{1}{q}} \mu(G)^{1
-\frac{1}{q}} 2^{2a+5}\sum_{k \ge 0}\sum_{n \ge k}(2n+3)(4n+12) 2^{-(1-\frac{1}{q})n}\,.
$$

Interchanging the order of summation, the last factor equals

$$
2^{2a+5} \sum_{n \ge 0} (2n+3)(4n+12) (n+1) 2^{-\frac{q-1}{q}n}\,.
$$

Up to an explicit constant, the sum is bounded by $\sum n^3 2^{-\frac{q-1}{q}n}$, which is at most some constant times $1/(q-1)^4$ by comparing to an integral. Since $a \ge 4$, this is overall bounded by $2^{a^3}/(q-1)^4$, which completes the proof of the lemma.

## Lean

Formalized as [`forest_union`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_union).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2139](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2139)
