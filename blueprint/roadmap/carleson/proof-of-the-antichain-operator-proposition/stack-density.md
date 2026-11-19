---
declaration: lemma
origin: cited
lean: Antichain.stack_density
statement: formalized
proof: formalized
---

# stack density

Let ${\vartheta} \in {\Theta}$, $N\ge 0$ and $L\in \mathcal{D}$. Then

$$
\sum_{{\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}:{\mathcal{I}}({\mathfrak p})=L}\mu(E({\mathfrak p})\cap G)\le 2^{a(N+5)}\operatorname{\operatorname{dens}}_1(\mathfrak{A})\mu(L)\, .\qquad\text{(47)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let ${\vartheta},N,L$ be given and set

$$
\mathfrak{A}':=\{{\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}:{\mathcal{I}}({\mathfrak p})=L\}\, .
$$

Let ${\mathfrak p}\in\mathfrak{A}'$. We have by Definition [(26)](../proof-of-metric-space-carleson-overview/README.md) using $\lambda=2$ and the squeezing property [(15)](../proof-of-metric-space-carleson-overview/README.md)

$$
\mu(E({\mathfrak p})\cap G)\le \mu(E_2(2, {\mathfrak p}))\le 2^{a}\operatorname{\operatorname{dens}}_1(\mathfrak{A}')\mu(L)\, .\qquad\text{(48)}
$$

By the covering property [(11)](../introduction/README.md), applied $N+4$ times, there is a collection ${\Theta}'$ of at most $2^{a(N+4)}$ elements such that

$$
B_{{\mathfrak p}}({\vartheta}, 2^{N+1})\subset \bigcup_{{\vartheta}'\in {\Theta}'}
B_{{\mathfrak p}}({\vartheta}', 0.2)\, .\qquad\text{(49)}
$$

As each ${\mathcal{Q}}({\mathfrak p}')$ with ${\mathfrak p}'\in \mathfrak{A}'$ is contained in the left-hand-side of (49) by definition (because ${\mathcal{I}}({\mathfrak p}') = {\mathcal{I}}({\mathfrak p}))$, it is in at least one $B_{{\mathfrak p}}({\vartheta}', 0.2)$ with ${\vartheta}'\in {\Theta}'$.

For two different ${\mathfrak p}',{\mathfrak p}''\in \mathfrak{A}'$, we have by [(13)](../proof-of-metric-space-carleson-overview/README.md) that ${\Omega}({\mathfrak p}')$ and ${\Omega}({\mathfrak p}'')$ are disjoint and thus by the squeezing property [(15)](../proof-of-metric-space-carleson-overview/README.md) we have for every ${\vartheta}'\in {\Theta}'$

$$
{\vartheta}'\not\in B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}'), 0.2)\cap
B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}''), 0.2)\, .
$$

Hence at most one of ${\mathcal{Q}}({\mathfrak p}')$ and ${\mathcal{Q}}({\mathfrak p}'')$ is in $B_{{\mathfrak p}}({\vartheta}', 0.2)$. It follows that there are at most $2^{a(N+4)}$ elements in $\mathfrak{A}'$. Adding (48) over $\mathfrak{A}'$ proves (47).

## Lean

Formalized as [`Antichain.stack_density`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Antichain.stack_density).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4093](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4093)
