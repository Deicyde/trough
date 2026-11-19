---
declaration: lemma
origin: cited
lean: tree_count
statement: formalized
proof: formalized
---

# tree count

Let $k,n,j\ge 0$. We have for every $x\in X$

$$
\sum_{{\mathfrak u}\in {\mathfrak U}_1(k,n,j)} \mathbf{1}_{{\mathcal{I}}({\mathfrak u})}(x)
\le 2^{-j}
2^{9a} \sum_{\mathfrak{m}\in \mathfrak{M}(k,n)}
\mathbf{1}_{{\mathcal{I}}(\mathfrak{m})}(x)
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $x\in X$. For each ${\mathfrak u}\in {\mathfrak U}_1(k,n,j)$ with $x\in {\mathcal{I}}({\mathfrak u})$, as ${\mathfrak u} \in {\mathfrak C}_1(k,n,j)$, there are at least $2^{j}$ elements $\mathfrak{m}\in \mathfrak{M}(k,n)$ with $100{\mathfrak u} \lesssim \mathfrak{m}$ and in particular $x\in {\mathcal{I}}(\mathfrak{m})$. Hence

$$
\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}(x)
\le 2^{-j}\sum_{\mathfrak{m} \in \mathfrak{M}(k,n): 100{\mathfrak u}\lesssim \mathfrak{m}} \mathbf{1}_{{\mathcal{I}}(\mathfrak{m})}(x)\, .\qquad\text{(34)}
$$

Conversely, for each $\mathfrak{m}\in \mathfrak{M}(k,n)$ with $x\in {\mathcal{I}}(\mathfrak{m})$, let ${\mathfrak U}(\mathfrak{m})$ be the set of ${\mathfrak u}\in {\mathfrak U}_1(k,n,j)$ with $x\in {\mathcal{I}}({\mathfrak u})$ and $100{\mathfrak u} \lesssim \mathfrak{m}$. Summing (34) over ${\mathfrak u}$ and counting the pairs $({\mathfrak u},\mathfrak{m})$ with $100{\mathfrak u} \lesssim \mathfrak{m}$ differently gives

$$
\sum_{{\mathfrak u}\in {\mathfrak U}_1(k,n,j)} \mathbf{1}_{{\mathcal{I}}({\mathfrak u})}(x)
\le 2^{-j}\sum_{\mathfrak{m} \in \mathfrak{M}(k,n)}
\sum_{{\mathfrak u} \in {\mathfrak U}(\mathfrak{m})} \mathbf{1}_{{\mathcal{I}}(\mathfrak{m})}(x)\, .\qquad\text{(35)}
$$

We estimate the number of elements in ${\mathfrak U}(\mathfrak{m})$. Let ${\mathfrak u} \in {\mathfrak U}(\mathfrak{m})$. Then by definition of ${\mathfrak U}(\mathfrak{m})$

$$
d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}),{\mathcal{Q}}(\mathfrak{m}))\le 100\, .\qquad\text{(36)}
$$

If ${\mathfrak u}'$ is a further element in ${\mathfrak U}(\mathfrak{m})$ with ${\mathfrak u}\neq {\mathfrak u}'$, then

$$
{\mathcal{Q}}(\mathfrak{m})
\in B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}),100)\cap B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'),100)\ .
$$

By the last display and definition of ${\mathfrak U}_1(k,n,j)$, none of ${\mathcal{I}}({\mathfrak u})$, ${\mathcal{I}}({\mathfrak u}')$ is strictly contained in the other. As both contain $x$, we have ${\mathcal{I}}({\mathfrak u})={\mathcal{I}}({\mathfrak u}')$. We then have $d_{{\mathfrak u}}=d_{{\mathfrak u}'}$.

By [(15)](../../proof-of-metric-space-carleson-overview/README.md), the balls $B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}),0.2)$ and $B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}'),0.2)$ are contained respectively in ${\Omega}({\mathfrak u})$ and ${\Omega}({\mathfrak u}')$ and thus are disjoint by [(13)](../../proof-of-metric-space-carleson-overview/README.md). By (36) and the triangle inequality, both balls are contained in $B_{{\mathfrak u}}({\mathcal{Q}}(\mathfrak{m}), 100.2)$.

By [(11)](../../introduction/README.md) applied nine times, there is a collection of at most $2^{9a}$ balls of radius $0.2$ with respect to the metric $d_{{\mathfrak u}}$ which cover the ball $B_{{\mathfrak u}}({\mathcal{Q}}(\mathfrak{m}),100.2)$. Let $B'$ be a ball in this cover. As the center of $B'$ can be in at most one of the disjoint balls $B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}),0.2)$ and $B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}'),0.2)$, the ball $B'$ can contain at most one of the points ${\mathcal{Q}}({\mathfrak u})$, ${\mathcal{Q}}({\mathfrak u}')$.

Hence the image of ${\mathfrak U}(\mathfrak{m})$ under ${\mathcal{Q}}$ has at most $2^{9a}$ elements; since ${\mathcal{Q}}$ is injective on ${\mathfrak U}(\mathfrak{m})$, the same is true of ${\mathfrak U}(\mathfrak{m})$. Inserting this into (35) proves the lemma.

## Lean

Formalized as [`tree_count`](https://fpvandoorn.github.io/carleson/docs/find/#doc/tree_count).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2444](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2444)
