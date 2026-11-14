---
navigation: transparent
---

# dyadic partition 1 to disjoint row support

To simplify the notation, we will write at various places throughout the proof of Lemmas [correlation distant tree parts](../part-01/correlation-distant-tree-parts.md) and [correlation near tree parts](../part-01/correlation-near-tree-parts.md) for a subset ${\mathfrak C} \subset {\mathfrak P}$

$$
T_{{\mathfrak C}} f := \sum_{{\mathfrak p} \in {\mathfrak C}} T_{{\mathfrak p}} f\,, \quad\quad T_{{\mathfrak C}}^* g := \sum_{{\mathfrak p}\in{\mathfrak C}} T_{{\mathfrak p}}^* g\,.
$$

## Proof of the Tiles with large separation Lemma

[correlation distant tree parts](../part-01/correlation-distant-tree-parts.md) follows from the van der Corput estimate in [Holder van der Corput](../../proof-of-metric-space-carleson-overview/holder-van-der-corput.md). We apply this proposition in The van der Corput estimate. To prepare this application, we first, in A partition of unity, construct a suitable partition of unity, and show then, in Hölder estimates for adjoint tree operators the Hölder estimates needed to apply [Holder van der Corput](../../proof-of-metric-space-carleson-overview/holder-van-der-corput.md).

### A partition of unity

Define

$$
\mathcal{J}' = \{J \in \mathcal{J}(\mathfrak{S}) \ : \ J \subset {\mathcal{I}}({\mathfrak u}_1)\}\,.
$$

- [dyadic partition 1](dyadic-partition-1.md)

For cubes $J \in \mathcal{D}$, denote

$$
B(J) := B(c(J), 8D^{s(J)}).\qquad\text{(35)}
$$

The main result of this subsubsection is the following.

- [Lipschitz partition unity](lipschitz-partition-unity.md)

In the proof, we will use the following auxiliary lemma.

- [moderate scale change](moderate-scale-change.md)

*Proof of Lipschitz partition unity: shown with [Lipschitz partition unity](lipschitz-partition-unity.md).*

### Hölder estimates for adjoint tree operators

Let $g_1, g_2:X \to \mathbb{C}$ be bounded with bounded support. Define for $J \in \mathcal{J}'$

$$
h_J(y) := \chi_J(y)\cdot(e({\mathcal{Q}}({\mathfrak u}_1)(y)) T_{{\mathfrak T}({\mathfrak u}_1)}^* g_1(y)) \cdot \overline{(e({\mathcal{Q}}({\mathfrak u}_2)(y)) T_{{\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}}^* g_2(y))}\,.\qquad\text{(41)}
$$

The main result of this subsubsection is the following $\tau$-Hölder estimate for $h_J$, where $\tau = 1/a$.

- [Holder correlation tree](holder-correlation-tree.md)

We will prove this lemma at the end of this section, after establishing several auxiliary results.

We begin with the following Hölder continuity estimate for adjoints of operators associated to tiles.

- [Holder correlation tile](holder-correlation-tile.md)

Recall that

$$
B(J) := B(c(J), 8D^{s(J)}).
$$

We also denote

$$
B'(J) := B(c(J), 16D^{s(J)}),
$$

$$
B^\circ{}(J) := B(c(J), \frac{1}{8}D^{s(J)})\, .
$$

- [limited scale impact](limited-scale-impact.md)
- [local tree control](local-tree-control.md)
- [scales impacting interval](scales-impacting-interval.md)
- [global tree control 1](global-tree-control-1.md)
- [global tree control 2](global-tree-control-2.md)

*Proof of Holder correlation tree: shown with [Holder correlation tree](holder-correlation-tree.md).*

### The van der Corput estimate

- [lower oscillation bound](lower-oscillation-bound.md)

Now we are ready to prove [correlation distant tree parts](../part-01/correlation-distant-tree-parts.md).

*Proof of correlation distant tree parts: shown with [correlation distant tree parts](../part-01/correlation-distant-tree-parts.md).*

## Proof of The Remaining Tiles Lemma

We define

$$
\mathcal{J}' = \{J \in \mathcal{J}({\mathfrak T}({\mathfrak u}_1)) \, : \, J \subset {\mathcal{I}}({\mathfrak u}_1)\}\,,
$$

note that this is different from the $\mathcal{J}'$ defined in the previous subsection.

- [dyadic partition 2](dyadic-partition-2.md)

[correlation near tree parts](../part-01/correlation-near-tree-parts.md) follows from the following key estimate.

- [bound for tree projection](bound-for-tree-projection.md)

We prove this lemma below. First, we deduce [correlation near tree parts](../part-01/correlation-near-tree-parts.md).

*Proof of correlation near tree parts: shown with [correlation near tree parts](../part-01/correlation-near-tree-parts.md).*

We need two more auxiliary lemmas before we prove [bound for tree projection](bound-for-tree-projection.md).

- [thin scale impact](thin-scale-impact.md)
- [square function count](square-function-count.md)

*Proof of bound for tree projection: shown with [bound for tree projection](bound-for-tree-projection.md).*

## Forests

In this subsection, we complete the proof of [forest operator](../../proof-of-metric-space-carleson-overview/forest-operator.md) from the results of the previous subsections.

Define an $n$-row to be an $n$-forest $({\mathfrak U}, {\mathfrak T})$, i.e. satisfying conditions [(30)](../../proof-of-metric-space-carleson-overview/README.md) - [(35)](../../proof-of-metric-space-carleson-overview/README.md), such that in addition the sets ${\mathcal{I}}({\mathfrak u}), {\mathfrak u} \in {\mathfrak U}$ are pairwise disjoint.

- [forest row decomposition](forest-row-decomposition.md)

We pick a decomposition of the forest $({\mathfrak U}, {\mathfrak T})$ into $2^n$ $n$-rows

$$
({\mathfrak U}_j, {\mathfrak T}_j) := ({\mathfrak U}_j, {\mathfrak T}|_{{\mathfrak U}_j})
$$

as in [forest row decomposition](forest-row-decomposition.md). To save some space in the proofs of the remaining lemmas in this section we will write

$$
T_{{\mathfrak C}} = \sum_{{\mathfrak p} \in {\mathfrak C}} T_{{\mathfrak p}},\qquad T_{{\mathfrak C}}^* = \sum_{{\mathfrak p} \in {\mathfrak C}} T_{{\mathfrak p}}^*,
$$

$$
T_{\mathfrak{R}_j} = \sum_{{\mathfrak u} \in {\mathfrak U}_j} T_{{\mathfrak T}({\mathfrak u})},\qquad T_{\mathfrak{R}_j}^* = \sum_{{\mathfrak u} \in {\mathfrak U}_j} T_{{\mathfrak T}({\mathfrak u})}^*.
$$

- [row bound](row-bound.md)
- [row correlation](row-correlation.md)

Define for $1 \le j \le 2^n$

$$
E_j := \bigcup_{{\mathfrak u} \in {\mathfrak U}_j} \bigcup_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} E({\mathfrak p})\,.
$$

- [disjoint row support](disjoint-row-support.md)

Now we prove [forest operator](../../proof-of-metric-space-carleson-overview/forest-operator.md).

*Proof of forest operator: shown with [forest operator](../../proof-of-metric-space-carleson-overview/forest-operator.md).*
