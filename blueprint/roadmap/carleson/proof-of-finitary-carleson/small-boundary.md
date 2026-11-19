---
declaration: lemma
origin: cited
lean: small_boundary
statement: formalized
proof: formalized
---

# small boundary

Let $K = 2^{4a+1}$. For each $-S+K\le k\le S$ and $y\in Y_k$ we have

$$
\sum_{z\in Y_{k-K}: (z,k-K|y,k)}\mu(I_3(z,k-K)) \le \frac 12 \mu(I_3(y,k))\,.\qquad\text{(18)}
$$

## Depends on

- [transitive boundary](transitive-boundary.md)

## Proof

Let $K$ be as in the lemma. Let $-S+K\le k\le S$ and $y\in Y_k$.

Pick $k'$ so that $k-K\le k'\le k$. For each $y''\in Y_{k-K}$ with $(y'',k-K| y,k)$, by [cover by cubes](cover-by-cubes.md) and [dyadic property](dyadic-property.md), there is a unique $y'\in Y_{k'}$ such that

$$
I_3(y'',k-K)\subset I_3(y',k')\subset I_3(y,k)\, .\qquad\text{(19)}
$$

Using [transitive boundary](transitive-boundary.md), $(y',k'|y,k)$.

We conclude using the disjointedness property of [basic grid structure](basic-grid-structure.md) that

$$
\sum_{y'': (y'',k-K|y,k)}\mu(I_3(y'',k-K))
\le
\sum_{y': (y',k'|y,k)}
\mu(I_3(y',k')) \, .\qquad\text{(20)}
$$

Adding over $k-K\lt k'\le k$, and using

$$
\mu(I_3(y',k'))\le 2^{4a} \mu(B(y', \frac 14 D^{k'}))
$$

from the doubling property [(5)](../introduction/README.md) and [(12)](basic-grid-structure.md) gives

$$
K\sum_{y'': (y'',k-K|y,k)}
\mu(I_3(y'',k-K))\qquad\text{(21)}
$$

$$
\le 2^{4a} \sum_{k-K\lt k'\le k}
\left[ \sum_{y': (y',k'|y,k)}
\mu(B(y', \frac 14 D^{k'}))\right]\qquad\text{(22)}
$$

Each ball $B(y', \frac 14 D^{k'})$ occurring in (22) is contained in $I_3(y',k')$ by [(12)](basic-grid-structure.md) and in turn contained in $I_3(y,k)$ by (19). Assume for the moment all these balls are pairwise disjoint. Then by additivity of the measure,

$$
K\sum_{y'': (y'',k-K|y,k)}
\mu(I_3(y'',k-K))
\le 2^{4a}
\mu(I_3(y,k))\,
$$

which by $K=2^{4a+1}$ implies (18).

It thus remains to prove that the balls occurring in (22) are pairwise disjoint. Let $(u,l)$ and $(u',l')$ be two parameter pairs occurring in the sum of (22) and let $B(u, \frac 14 D^l)$ and $B({u'}, \frac 14 D^{l'})$ be the corresponding balls. If $l=l'$, then the balls are equal or disjoint by [(12)](basic-grid-structure.md) and [(10)](basic-grid-structure.md) of [basic grid structure](basic-grid-structure.md). Assume then without loss of generality that $l'\lt l$. Towards a contradiction, assume that

$$
B(u, \frac 14 D^l)\cap B({u'}, \frac 14 D^{l'})\neq \emptyset\qquad\text{(23)}
$$

As $(u',l'|y,k)$, there is a point $x$ in $X\setminus I_3(y,k)$ with $\rho(x,u')<6D^{l'}$. Using $D>25$, we conclude from the triangle inequality and (23) that $x\in B(u,\frac 12D^l)$. However, $B(u,\frac 12 D^l)\subset I_3(u,l)$, and $I_3(u,l)\subset I_3(y,k)$, a contradiction to $x\not\in I_3(y,k)$. This proves the lemma.

## Lean

Formalized as [`small_boundary`](https://fpvandoorn.github.io/carleson/docs/find/#doc/small_boundary).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1569](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1569)
