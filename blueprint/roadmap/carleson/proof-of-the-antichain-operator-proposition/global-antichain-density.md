---
declaration: lemma
origin: cited
lean: Antichain.global_antichain_density
statement: formalized
proof: formalized
---

# global antichain density

Let ${\vartheta}\in Q(X)$ and let $N\ge 0$ be an integer. Then we have

$$
\sum_{{\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}}\mu(E({\mathfrak p})\cap G)
\le
2^{101a^3+Na}\operatorname{\operatorname{dens}}_1(\mathfrak{A})\mu\left(\cup_{{\mathfrak p}\in\mathfrak{A}}I_{{\mathfrak p}}\right)\, .\qquad\text{(51)}
$$

## Depends on

- [stack density](stack-density.md)
- [local antichain density](local-antichain-density.md)

## Proof

Fix ${\vartheta}$ and $N$. Let $\mathfrak{A}'$ be the set of ${\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}$ such that ${\mathcal{I}}({\mathfrak p})\cap G$ is not empty and $s({\mathfrak p}) > -S$. Let $\mathfrak{A}_{-S}$ be the set of ${\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}$ such that ${\mathcal{I}}({\mathfrak p})\cap G$ is not empty and $s({\mathfrak p}) = -S$ Then we have

$$
\sum_{{\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}}\mu(E({\mathfrak p})\cap G) =
\sum_{{\mathfrak p}\in\mathfrak{A}'}\mu(E({\mathfrak p})\cap G) + \sum_{{\mathfrak p}\in\mathfrak{A}_{-S}}\mu(E({\mathfrak p})\cap G)
$$

We start by estimating the contribution of $\mathfrak{A}_{-S}$. Let $\mathcal{L}_{-S}$ be the collection of dyadic cubes ${\mathcal{I}}({\mathfrak p})$ with ${\mathfrak p} \in \mathfrak{A}_{-S}$. They all have scale $-S$, by definition of $\mathcal{L}_{-S}$, and hence they are pairwise disjoint by the dyadic property [(8)](../proof-of-metric-space-carleson-overview/README.md). We write

$$
\sum_{{\mathfrak p}\in\mathfrak{A}_{-S}}\mu(E({\mathfrak p})\cap G)
= \sum_{L \in \mathcal{L}_{-S}} \sum_{{\mathfrak p}\in\mathfrak{A}_{-S}, {\mathcal{I}}({\mathfrak p}) = L} \mu(E({\mathfrak p})\cap G),
$$

and using [stack density](stack-density.md), we estimate

$$
\le 2^{a(N+5)} \operatorname{\operatorname{dens}}_1(\mathfrak{A}) \sum_{L \in \mathcal{L}_{-S}} \mu(L)
\le 2^{a(N+5)} \operatorname{\operatorname{dens}}_1(\mathfrak{A}) \mu\left(\cup_{{\mathfrak p}\in\mathfrak{A}}I_{{\mathfrak p}}\right).\qquad\text{(52)}
$$

We turn to $\mathfrak{A}'$. Let $\mathcal{L}$ be the collection of dyadic cubes $I\in\mathcal{D}$ such that $I \le {\mathcal{I}}({\mathfrak p})$ for some ${\mathfrak p}\in\mathfrak{A}'$ and such that ${\mathcal{I}}({\mathfrak p})\not \subset I$ for all ${\mathfrak p}\in\mathfrak{A}'$. By [(7)](../proof-of-metric-space-carleson-overview/README.md), for each ${\mathfrak p} \in \mathfrak{A}'$ and each $x\in {\mathcal{I}}({\mathfrak p})\cap G$, there is $I\in \mathcal{D}$ with $s(I)=-S$ and $x\in I$. By [(8)](../proof-of-metric-space-carleson-overview/README.md), we have $I\subset {\mathcal{I}}({\mathfrak p})$. Since for all ${\mathfrak p}' \in \mathfrak{A}'$ we have $s({\mathfrak p}') > -S$, we have $I \in \mathcal{L}$. Hence

$$
{\mathcal{I}}({\mathfrak p})\subset \bigcup\{I\in \mathcal{D}: s(I)=-S, I\subset {\mathcal{I}}({\mathfrak p})\}\subset \bigcup \mathcal{L}\, .
$$

As each $I\in \mathcal{L}$ satisfies $I\subset {\mathcal{I}}({\mathfrak p})$ for some ${\mathfrak p}$ in $\mathfrak{A'}$, we conclude

$$
\bigcup\mathcal{L}=\bigcup_{{\mathfrak p} \in \mathfrak{A}'}{\mathcal{I}}({\mathfrak p})\, .
$$

Let $\mathcal{L}^*$ be the set of maximal elements in $\mathcal{L}$ with respect to set inclusion. By [(8)](../proof-of-metric-space-carleson-overview/README.md), the elements in $\mathcal{L}^*$ are pairwise disjoint and we have

$$
\bigcup\mathcal{L}^*=\bigcup_{{\mathfrak p} \in \mathfrak{A}'}{\mathcal{I}}({\mathfrak p})\, .\qquad\text{(53)}
$$

Using the partition (53) into elements of $\mathcal{L}$ in (54), it suffices to show for each $L\in \mathcal{L}^*$

$$
\sum_{{\mathfrak p}\in\mathfrak{A}'}\mu(E({\mathfrak p})\cap G \cap L)
\le
2^{101a^3+aN}
\operatorname{\operatorname{dens}}_1(\mathfrak{A})\mu(L)\,.\qquad\text{(54)}
$$

Fix $L\in \mathcal{L}^*$. By definition of $\mathcal{L}^*$, there exists an element ${\mathfrak p}'\in \mathfrak{A}'$ such that $L\subset {\mathcal{I}}({\mathfrak p}')$. Pick such an element ${\mathfrak p}'$ in $\mathfrak{A}$ with minimal ${\mathrm{s}}({\mathfrak p}')$. As ${\mathcal{I}}({\mathfrak p}')\not \subset L$ by definition of $L$, we have with [(8)](../proof-of-metric-space-carleson-overview/README.md) that $s(L)< {\mathrm{s}}({\mathfrak p}')$. In particular $s(L)\lt S$, thus $L \ne I_0$ and hence by [(9)](../proof-of-metric-space-carleson-overview/README.md) there exists a cube $J \in \mathcal{D}$ with $L \subsetneq J$. By [(7)](../proof-of-metric-space-carleson-overview/README.md), there is an $L'\in \mathcal{D}$ with $s(L')=s(L)+1$ and $L \le L'$. By [(8)](../proof-of-metric-space-carleson-overview/README.md), we have $L\subset L'$.

We split the left-hand side of (54) as

$$
\sum_{{\mathfrak p}\in\mathfrak{A}':{\mathcal{I}}({\mathfrak p})=L'}\mu(E({\mathfrak p})\cap G\cap L)\qquad\text{(55)}
$$

$$
+
\sum_{{\mathfrak p}\in\mathfrak{A}':{\mathcal{I}}({\mathfrak p})\neq L'}\mu(E({\mathfrak p})\cap G\cap L)\, ,\qquad\text{(56)}
$$

We first estimate (55) with [stack density](stack-density.md) by

$$
\le \sum_{{\mathfrak p}\in\mathfrak{A}':{\mathcal{I}}({\mathfrak p})=L'}\mu(E({\mathfrak p})\cap G\cap L')\le 2^{a(N+5)}\operatorname{\operatorname{dens}}_1(\mathfrak{A})\mu(L')\, .\qquad\text{(57)}
$$

We turn to (56). Consider the element ${\mathfrak p}'\in \mathfrak{A}'$ as above with $L\subset {\mathcal{I}}({\mathfrak p}')$ and $s(L)<{\mathrm{s}}({\mathfrak p}')$. As $L\subset L'$ and $s(L')=s(L)+1$, we conclude with the dyadic property that $L'\subset {\mathcal{I}}({\mathfrak p}')$. By maximality of $L$, we have $L'\not\in \mathcal{L}$. This together with the existence of the given ${\mathfrak p}'\in \mathfrak{A}$ with $L'\subset {\mathcal{I}}({\mathfrak p}')$ shows by definition of $\mathcal{L}$ that there exists ${\mathfrak p}''\in \mathfrak{A}'$ with ${\mathcal{I}}({\mathfrak p}'')\subset L'$.

If ${\mathcal{I}}({\mathfrak p}'') = L'$, then we set ${\mathfrak p}_{{\vartheta}} = {\mathfrak p}''$ and note that as ${\mathfrak p}'' \in \mathfrak{A}_{{\vartheta},N}$

$$
{\vartheta} \in B({\mathcal{Q}}({\mathfrak p}''), 2^{N+1})\, .
$$

If ${\mathcal{I}}({\mathfrak p}'') \ne L'$, then it follows that $s({\mathfrak p}'') < s(L')$. By the covering property [(13)](../proof-of-metric-space-carleson-overview/README.md), there exists a unique ${\mathfrak p}_{{\vartheta}}$ with

$$
{\mathcal{I}}({\mathfrak p}_{{\vartheta}})=L'
$$

such that ${\vartheta}\in {\Omega}({\mathfrak p}_{{\vartheta}})$. We take this as the definition of ${\mathfrak p}_{\vartheta}$ in this case. Note that

$$
{\vartheta}\in B({\mathcal{Q}}({\mathfrak p}_{{\vartheta}}), 1)
$$

so by [tile reach](tile-reach.md), we conclude

$$
2^{N+3}{\mathfrak p}'' \lesssim 2^{N+3}{\mathfrak p}_{{\vartheta}} \, .
$$

This clearly also holds in the case ${\mathcal{I}}({\mathfrak p}'') = L'$, since then ${\mathfrak p}'' = {\mathfrak p}_{\vartheta}$. Furthermore, in both cases it also holds that

$$
{\vartheta}\in B_{{\mathfrak p}_{{\vartheta}}}({\mathcal{Q}}({\mathfrak p}_{{\vartheta}}), 2^{N+1}).
$$

As ${\mathfrak p}''\in \mathfrak{A}'$, we have by Definition [(26)](../proof-of-metric-space-carleson-overview/README.md) of $\operatorname{\operatorname{dens}}_1$ that

$$
\mu(E_2(2^{N+3}, {\mathfrak p}_{{\vartheta}}))\le 2^{Na+3a}\operatorname{\operatorname{dens}}_1(\mathfrak{A}) {\mu(L')}\, .\qquad\text{(58)}
$$

Now let ${\mathfrak p}$ be any tile in the summation set in (56), that is, ${\mathfrak p}\in \mathfrak{A}'$ and ${\mathcal{I}}({\mathfrak p})\neq L'$. Then ${\mathcal{I}}({\mathfrak p})\cap L\neq \emptyset$. It follows by the dyadic property [(8)](../proof-of-metric-space-carleson-overview/README.md) and the definition of $L$ that $L\subset {\mathcal{I}}({\mathfrak p})$ and $L\neq {\mathcal{I}}({\mathfrak p})$. By the dyadic property [(8)](../proof-of-metric-space-carleson-overview/README.md), we have $s(L)<{\mathrm{s}}({\mathfrak p})$ and thus $s(L')\le {\mathrm{s}}({\mathfrak p})$. By the dyadic property [(8)](../proof-of-metric-space-carleson-overview/README.md) again, we have $L'\subset {\mathcal{I}}({\mathfrak p})$. As $L'\neq {\mathcal{I}}({\mathfrak p})$, we conclude $s(L)<{\mathrm{s}}({\mathfrak p})$. By [local antichain density](local-antichain-density.md), we can thus estimate (56) by

$$
\sum_{{\mathfrak p}\in\mathfrak{A}':{\mathcal{I}}({\mathfrak p})\neq L'}\mu(E({\mathfrak p})\cap G\cap L')
\le \mu (E_2(2^{N+3},{\mathfrak p}_{{\vartheta}}))\, .\qquad\text{(59)}
$$

With the decomposition in (55) and (56) and the estimates (57), [(50)](local-antichain-density.md), (58) we obtain the estimate

$$
\sum_{{\mathfrak p}\in\mathfrak{A}'}\mu(E({\mathfrak p})\cap G \cap L)
\le (2^{a(N+5)}+2^{Na+3a})\operatorname{\operatorname{dens}}_1(\mathfrak{A})\mu(L')\,.\qquad\text{(60)}
$$

Using $s(L')=s(L)+1$ and $D=2^{100a^2}$ and the squeezing property [(10)](../proof-of-metric-space-carleson-overview/README.md) and the doubling property [(5)](../introduction/README.md) $100a^2+4$ times , we obtain

$$
\mu(L')\le 2^{100a^3+4a}\mu(L)\, .
$$

Inserting in (60), adding the estimate (52) and using $a\ge 4$ gives (54). This completes the proof of the lemma.

## Lean

Formalized as [`Antichain.global_antichain_density`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Antichain.global_antichain_density).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4186](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4186)
