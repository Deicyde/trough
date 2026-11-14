---
declaration: lemma
origin: cited
lean: dyadic_property
statement: formalized
proof: formalized
---

# dyadic property

Let $-S\le l\le k\le S$ and $y\in Y_k$ and $y'\in Y_l$ with $I_3(y',l)\cap I_3(y,k)\neq \emptyset$. Then

$$
I_3(y',l)\subset I_3(y,k).\qquad\text{(14)}
$$

## Depends on

- [basic grid structure](basic-grid-structure.md)
- [cover by cubes](cover-by-cubes.md)

## Proof

Let $l,k,y,y'$ be as in the lemma. Pick $x\in I_3(y',l)\cap I_3(y,k)$. Assume first $l=k$. By [(10)](basic-grid-structure.md) of [basic grid structure](basic-grid-structure.md), we conclude $y'=y$, and thus (14). Now assume $l\lt k$. By induction, we may assume that the statement of the lemma is proven for $k-1$ in place of $k$.

By [cover by cubes](cover-by-cubes.md), there is a $y''\in Y_{k-1}$ such that $x\in I_3(y'',k-1)$. By induction, we have $I_3(y',l)\subset I_3(y'',k-1)$. It remains to prove

$$
I_3(y'',k-1)\subset I_3(y,k).\qquad\text{(15)}
$$

We make a case distinction and assume first $x\in X_k$. By Definition [(9)](README.md), we have $x\in I_1(y,k)$. By Definition [(8)](README.md), there is a $v\in Y_{k-1}\cap B(y,D^k)$ with $x\in I_3(v,k-1)$. By [(10)](basic-grid-structure.md) of [basic grid structure](basic-grid-structure.md), we have $v=y''$. By Definition [(8)](README.md), we then have $I_3(y'',k-1)\subset I_1(y,k)$. Then (15) follows by Definition [(9)](README.md) in the given case.

Assume now the case $x\notin X_k$. By [(9)](README.md), we have $x\in I_2(y,k)$. Moreover, for any $u\lt y$ in $Y_k$, we have $x\not\in I_3(u,k)$. Let $u\lt y$. By transitivity of the order in $Y_k$, we conclude $x\not \in I_2(u,k)$. By [(8)](README.md) and the disjointedness property of [basic grid structure](basic-grid-structure.md), we have $I_3(y'',k-1)\cap I_2(u,k)= \emptyset$. Similarly, $I_3(y'',k-1)\cap I_1(u,k)= \emptyset$. Hence $I_3(y'',k-1)\cap I_3(u,k)=\emptyset$. As $u\lt y$ was arbitrary, we conclude with [(9)](README.md) the claim in the given case. This completes the proof of (15), and thus also (14).

## Lean

Formalized as [`dyadic_property`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dyadic_property).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1496](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1496)
