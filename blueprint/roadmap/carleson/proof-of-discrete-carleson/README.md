# Proof of discrete Carleson

Let a grid structure $(\mathcal{D}, c, s)$ and a tile structure $({\mathfrak P}, {\mathcal{I}}, {\Omega}, {\mathcal{Q}})$ for this grid structure be given. In Organisation of the tiles, we decompose the set ${\mathfrak P}$ of tiles into subsets. Each subset will be controlled by one of three methods. The guiding principle of the decomposition is to be able to apply the forest estimate of [forest operator](../proof-of-metric-space-carleson-overview/forest-operator.md) to the final subsets defined in (20). This application is done in Proof of the Forest Union Lemma. The miscellaneous subsets along the construction of the forests will either be thrown into exceptional sets, which are defined and controlled in Proof of the Exceptional Sets Lemma, or will be controlled by the antichain estimate of [antichain operator](../proof-of-metric-space-carleson-overview/antichain-operator.md), which is done in Proof of the Forest Complement Lemma. Auxiliary lemmas contains some auxiliary lemmas needed for the proofs in Subsections Proof of the Forest Union Lemma-Proof of the Forest Complement Lemma.

## Organisation of the tiles

In the following definitions, $k, n$, and $j$ will be nonnegative integers. Define $\mathcal{C}(G,k)$ to be the set of $I\in \mathcal{D}$ such that there exists a $J\in \mathcal{D}$ with $I\subset J$ and

$$
{\mu(G \cap J)} > 2^{-k-1}{\mu(J)}\, ,\qquad\text{(1)}
$$

but there does not exist a $J\in \mathcal{D}$ with $I\subset J$ and

$$
{\mu(G \cap J)} > 2^{-k}{\mu(J)}\,.\qquad\text{(2)}
$$

Let

$$
{\mathfrak P}(k)=\{{\mathfrak p}\in {\mathfrak P} \ : \ {\mathcal{I}}({\mathfrak p})\in \mathcal{C}(G,k)\}\qquad\text{(3)}
$$

Define ${\mathfrak{M}}(k,n)$ to be the set of ${\mathfrak p} \in {\mathfrak P}(k)$ such that

$$
\mu({E_1}({\mathfrak p})) > 2^{-n} \mu({\mathcal{I}}({\mathfrak p}))\qquad\text{(4)}
$$

and there does not exist ${\mathfrak p}'\in {\mathfrak P}(k)$ with ${\mathfrak p}'\neq {\mathfrak p}$ and ${\mathfrak p}\le {\mathfrak p}'$ such that

$$
\mu({E_1}({\mathfrak p}')) > 2^{-n} \mu({\mathcal{I}}({\mathfrak p}')).\qquad\text{(5)}
$$

Define for a collection ${\mathfrak P}'\subset {\mathfrak P}(k)$

$$
\operatorname{\operatorname{dens}}_k' ({\mathfrak P}'):= \sup_{{\mathfrak p}'\in {\mathfrak P}'}\sup_{\lambda \geq 2} \lambda^{-a} \sup_{{\mathfrak p} \in {\mathfrak P}(k): \lambda {\mathfrak p}' \lesssim \lambda {\mathfrak p}}
\frac{\mu({E}_2(\lambda, {\mathfrak p}))}{\mu({\mathcal{I}}({\mathfrak p}))}\,.\qquad\text{(6)}
$$

Sorting by density, we define

$$
{\mathfrak C}(k,n):=\{{\mathfrak p}\in {\mathfrak P}(k) \ : \
2^{4a}2^{-n}< \operatorname{\operatorname{dens}}_k'(\{{\mathfrak p}\}) \le
2^{4a}2^{-n+1}\}\,.\qquad\text{(7)}
$$

Following Fefferman (fefferman), we define for ${\mathfrak p} \in {\mathfrak C}(k,n)$

$$
\mathfrak{B}({\mathfrak p}) := \{ \mathfrak{m} \in \mathfrak{M}(k,n) \ : \ 100 {\mathfrak p} \lesssim \mathfrak{m}\}\qquad\text{(8)}
$$

and

$$
{\mathfrak C}_1(k,n,j) := \{{\mathfrak p} \in {\mathfrak C}(k,n) \ : \ 2^{j} \leq |\mathfrak{B}({\mathfrak p})| < 2^{j+1}\}\,.\qquad\text{(9)}
$$

and

$$
{\mathfrak L}_0(k,n) := \{{\mathfrak p} \in {\mathfrak C}(k,n) \ : \ |\mathfrak{B}({\mathfrak p})| <1\}\,.\qquad\text{(10)}
$$

Together with the following removal of minimal layers, the splitting into ${\mathfrak C}_1(k,n,j)$ will lead to a separation of trees. Define recursively for $0\le l\le Z(n+1)$

$$
{\mathfrak L}_1(k,n,j,l)\qquad\text{(11)}
$$

to be the set of minimal elements with respect to $\le$ in

$$
{\mathfrak C}_1(k,n,j)\setminus \bigcup_{0\le l'\lt l}
{\mathfrak L}_1(k,n,j,l')\, .
$$

Define

$$
{\mathfrak C}_2(k,n,j):= {\mathfrak C}_1(k,n,j)\setminus \bigcup_{0\le l'\le Z(n+1)}
{\mathfrak L}_1(k,n,j,l')\, .\qquad\text{(12)}
$$

The remaining tile organization will be relative to prospective tree tops, which we define now. Define

$$
{\mathfrak U}_1(k,n,j)\qquad\text{(13)}
$$

to be the set of all ${\mathfrak u} \in {\mathfrak C}_1(k,n,j)$ such that for all ${\mathfrak p} \in {\mathfrak C}_1(k,n,j)$ with ${\mathcal{I}}({\mathfrak u})$ strictly contained in ${\mathcal{I}}({\mathfrak p})$ we have $B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 100) \cap B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),100) = \emptyset$.

We first remove the pairs that are outside the immediate reach of any of the prospective tree tops. Define

$$
{\mathfrak L}_2(k,n,j)\qquad\text{(14)}
$$

to be the set of all ${\mathfrak p}\in {\mathfrak C}_2(k,n,j)$ such that there does not exist ${\mathfrak u}\in {\mathfrak U}_1(k,n,j)$ with ${\mathcal{I}}({\mathfrak p})\neq {\mathcal{I}}({\mathfrak u})$ and $2{\mathfrak p}\lesssim {\mathfrak u}$. Define

$$
{\mathfrak C}_3(k,n,j):={\mathfrak C}_2(k,n,j)
\setminus {\mathfrak L}_2(k,n,j)\, .\qquad\text{(15)}
$$

We next remove the maximal layers. Define recursively for $0 \le l \le Z(n+1)$

$$
{\mathfrak L}_3(k,n,j,l)\qquad\text{(16)}
$$

to be the set of all maximal elements with respect to $\le$ in

$$
{\mathfrak C}_3(k,n,j) \setminus \bigcup_{0 \le l' < l} {\mathfrak L}_3(k,n,j,l')\,.
$$

Define

$$
{\mathfrak C}_4(k,n,j):={\mathfrak C}_3(k,n,j)
\setminus \bigcup_{0 \le l \le Z(n+1)} {\mathfrak L}_3(k,n,j,l)\,.\qquad\text{(17)}
$$

Finally, we remove the boundary pairs relative to the prospective tree tops. Define

$$
\mathcal{L}({\mathfrak u})\qquad\text{(18)}
$$

to be the set of all $I \in \mathcal{D}$ with $I \subset {\mathcal{I}}({\mathfrak u})$ and $s(I) = {\mathrm{s}}({\mathfrak u}) - Z(n+1) - 1$ and

$$
B(c(I), 8 D^{s(I)})\not \subset {\mathcal{I}}({\mathfrak u})\, .
$$

Define

$$
{\mathfrak L}_4(k,n,j)\qquad\text{(19)}
$$

to be the set of all ${\mathfrak p}\in {\mathfrak C}_4(k,n,j)$ such that there exists ${\mathfrak u}\in {\mathfrak U}_1(k,n,j)$ with ${\mathcal{I}}({\mathfrak p}) \subset \bigcup \mathcal{L}({\mathfrak u})$, and define

$$
{\mathfrak C}_5(k,n,j):={\mathfrak C}_4(k,n,j)
\setminus {\mathfrak L}_4(k,n,j)\, .\qquad\text{(20)}
$$

We define three exceptional sets. The first exceptional set $G_1$ takes into account the ratio of the measures of $F$ and $G$. Define ${\mathfrak P}_{F,G}$ to be the set of all ${\mathfrak p}\in {\mathfrak P}$ with

$$
\operatorname{\operatorname{dens}}_2(\{{\mathfrak p}\})> 2^{2a+5}\frac{\mu(F)}{\mu(G)}\,.
$$

Define

$$
G_1:=\bigcup_{{\mathfrak p}\in {\mathfrak P}_{F,G} }{\mathcal{I}}({\mathfrak p})\, .\qquad\text{(21)}
$$

For an integer $\lambda\ge 0$, define $A(\lambda,k,n)$ to be the set of all $x\in X$ such that

$$
\sum_{{\mathfrak p} \in \mathfrak{M}(k,n)}\mathbf{1}_{{\mathcal{I}}({\mathfrak p})}(x)>\lambda 2^{n+1}\qquad\text{(22)}
$$

and define

$$
G_2:=
\bigcup_{k\ge 0}\bigcup_{k\le n}
A(2n+6,k,n)\, .\qquad\text{(23)}
$$

Define

$$
G_3 :=
\bigcup_{k\ge 0}\, \bigcup_{n \geq k}\,
\bigcup_{0\le j\le 2n+3}
\bigcup_{{\mathfrak p} \in {\mathfrak L}_4 (k,n,j)}
{\mathcal{I}}({\mathfrak p})\, .\qquad\text{(24)}
$$

Define $G'=G_1\cup G_2 \cup G_3$. The following bound of the measure of $G'$ will be proven in Proof of the Exceptional Sets Lemma.

## [exceptional set to C2 convex](part-01/README.md)

- [exceptional set](part-01/exceptional-set.md)
- [forest union](part-01/forest-union.md)
- [forest complement](part-01/forest-complement.md)
- [first exception](part-01/first-exception.md)
- [dense cover](part-01/dense-cover.md)
- [pairwise disjoint](part-01/pairwise-disjoint.md)
- [dyadic union](part-01/dyadic-union.md)
- [John Nirenberg](part-01/john-nirenberg.md)
- [second exception](part-01/second-exception.md)
- [top tiles](part-01/top-tiles.md)
- [tree count](part-01/tree-count.md)
- [boundary exception](part-01/boundary-exception.md)
- [third exception](part-01/third-exception.md)
- [wiggle order 1](part-01/wiggle-order-1.md)
- [wiggle order 2](part-01/wiggle-order-2.md)
- [wiggle order 3](part-01/wiggle-order-3.md)
- [P convex](part-01/p-convex.md)
- [C convex](part-01/c-convex.md)
- [C1 convex](part-01/c1-convex.md)
- [C2 convex](part-01/c2-convex.md)

## [C3 convex to L1 L3 antichain](part-02/README.md)

- [C3 convex](part-02/c3-convex.md)
- [C4 convex](part-02/c4-convex.md)
- [C5 convex](part-02/c5-convex.md)
- [dens compare](part-02/dens-compare.md)
- [C dens1](part-02/c-dens1.md)
- [relation geometry](part-02/relation-geometry.md)
- [equivalence relation](part-02/equivalence-relation.md)
- [C6 forest](part-02/c6-forest.md)
- [forest geometry](part-02/forest-geometry.md)
- [forest convex](part-02/forest-convex.md)
- [forest separation](part-02/forest-separation.md)
- [forest inner](part-02/forest-inner.md)
- [forest stacking](part-02/forest-stacking.md)
- [antichain decomposition](part-02/antichain-decomposition.md)
- [L0 antichain](part-02/l0-antichain.md)
- [L2 antichain](part-02/l2-antichain.md)
- [L1 L3 antichain](part-02/l1-l3-antichain.md)
