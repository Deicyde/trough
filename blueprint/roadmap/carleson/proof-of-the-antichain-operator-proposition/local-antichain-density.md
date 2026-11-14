---
declaration: lemma
origin: cited
lean: Antichain.local_antichain_density, Antichain.Ep_inter_G_inter_Ip'_subset_E2
statement: formalized
proof: formalized
---

# local antichain density

Let ${\vartheta}\in{\Theta}$ and $N$ be an integer. Let ${\mathfrak p}_{{\vartheta}}$ be a tile with ${\vartheta}\in B_{{\mathfrak p}_{{\vartheta}}}({\mathcal{Q}}({\mathfrak p}_{{\vartheta}}), 2^{N+1})$. Then we have

$$
\sum_{{\mathfrak p}\in\mathfrak{A}_{{\vartheta},N}: {\mathrm{s}}({\mathfrak p}_{{\vartheta}})<{\mathrm{s}}({\mathfrak p})}\mu(E({\mathfrak p})\cap G \cap {\mathcal{I}}({\mathfrak p}_{{\vartheta}}))
\le \mu (E_2(2^{N+3},{\mathfrak p}_{{\vartheta}}))
\, .\qquad\text{(50)}
$$

## Depends on

- [tile disjointness](tile-disjointness.md)
- [tile reach](tile-reach.md)

## Proof

Let ${\mathfrak p}$ be any tile in $\mathfrak{A}_{{\vartheta},N}$ with ${\mathrm{s}}({\mathfrak p}_{{\vartheta}})<{\mathrm{s}}({\mathfrak p})$. By definition of $E$, the tile contributes zero to the sum on the left-hand side of (50) unless ${\mathcal{I}}({\mathfrak p})\cap {\mathcal{I}}({\mathfrak p}_{{\vartheta}}) \neq \emptyset$, which we may assume. With ${\mathrm{s}}({\mathfrak p}_{{\vartheta}})<{\mathrm{s}}({\mathfrak p})$ and the dyadic property [(8)](../proof-of-metric-space-carleson-overview/README.md) we conclude ${\mathcal{I}}({\mathfrak p}_{{\vartheta}})\subset {\mathcal{I}}({\mathfrak p})$. We conclude from ${\mathfrak p} \in \mathfrak{A}_{{\vartheta},N}$ that

$$
{\vartheta} \in B_{\mathfrak p}({\mathcal{Q}}({\mathfrak p}), 2^{N+1})\, .
$$

With [tile reach](tile-reach.md) and the assumption on ${\mathfrak p}_{\vartheta}$, we conclude

$$
2^{N+3}{\mathfrak p}_{{\vartheta}} \lesssim 2^{N+3}{\mathfrak p} \, .
$$

By Definition [(25)](../proof-of-metric-space-carleson-overview/README.md) of $E_2$, we conclude

$$
E({\mathfrak p})\cap G \cap {\mathcal{I}}({\mathfrak p}_{{\vartheta}}) \subset E_2(2^{N+3},{\mathfrak p}_{{\vartheta}})\, .
$$

Using disjointedness of the various $E({\mathfrak p})$ with ${\mathfrak p}\in \mathfrak{A}$ by [tile disjointness](tile-disjointness.md), we obtain (50). This proves the lemma.

## Lean

Formalized as [`Antichain.local_antichain_density`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Antichain.local_antichain_density), [`Antichain.Ep_inter_G_inter_Ip'_subset_E2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Antichain.Ep_inter_G_inter_Ip'_subset_E2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4146](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4146)
