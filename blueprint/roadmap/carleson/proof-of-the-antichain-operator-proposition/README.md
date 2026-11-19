# Proof of the Antichain Operator Proposition

Let an antichain $\mathfrak{A}$ and functions $f$, $g$ as in [antichain operator](../proof-of-metric-space-carleson-overview/antichain-operator.md) be given. We prove [(28)](../proof-of-metric-space-carleson-overview/antichain-operator.md) in The density arguments as the geometric mean of two inequalities, each involving one of the two densities. One of these two inequalities will need a careful estimate formulated in [tile correlation](tile-correlation.md) of the $TT^*$ correlation between two tile operators. [tile correlation](tile-correlation.md) will be proven in Proof of the Tile Correlation Lemma.

The summation of the contributions of these individual correlations will require a geometric [antichain tile count](antichain-tile-count.md) counting the relevant tile pairs. [antichain tile count](antichain-tile-count.md) will be proven in Subsection Proof of the Antichain Tile Count Lemma.

## The density arguments

We begin with the following crucial disjointedness property of the sets $E({\mathfrak p})$ with ${\mathfrak p} \in \mathfrak{A}$.

- [tile disjointness](tile-disjointness.md)

Let $\mathcal{B}$ be the collection of balls

$$
B({\mathrm{c}}({\mathfrak p}), 8D^{{\mathrm{s}}({\mathfrak p})})
$$

with ${\mathfrak p}\in \mathfrak{A}$ and recall the definition of $M_{\mathcal{B}}$ from Definition [48](../proof-of-metric-space-carleson-overview/README.md).

- [maximal bound antichain](maximal-bound-antichain.md)

Set

$$
\tilde{q}=\frac {2q}{1+q}\,.
$$

Since $1< q\le 2$, we have $1\lt \tilde{q}\lt q\le 2$.

- [dens2 antichain](dens2-antichain.md)
- [dens1 antichain](dens1-antichain.md)

The following basic $TT^*$ estimate will be proved in Proof of the Tile Correlation Lemma.

- [tile correlation](tile-correlation.md)

The following lemma will be proved in Proof of the Antichain Tile Count Lemma.

- [antichain tile count](antichain-tile-count.md)

From these lemmas it is easy to prove [antichain operator](../proof-of-metric-space-carleson-overview/antichain-operator.md).

*Proof of antichain operator: shown with [antichain operator](../proof-of-metric-space-carleson-overview/antichain-operator.md).*

## Proof of the Tile Correlation Lemma

The next lemma prepares an application of [Holder van der Corput](../proof-of-metric-space-carleson-overview/holder-van-der-corput.md).

- [correlation kernel bound](correlation-kernel-bound.md)

The following auxiliary statement about the support of $T_{\mathfrak p}^*g$ will be used repeatedly.

- [tile range support](tile-range-support.md)

The next lemma is a geometric estimate for two tiles.

- [tile-uncertainty](tile-uncertainty.md)

We now prove [tile correlation](tile-correlation.md).

*Proof of tile correlation: shown with [tile correlation](tile-correlation.md).*

## Proof of the Antichain Tile Count Lemma

- [tile reach](tile-reach.md)

For ${\vartheta} \in {\Theta}$ and $N\ge 0$ define

$$
\mathfrak{A}_{{\vartheta},N}:=\{{\mathfrak p}\in\mathfrak{A}: 2^{N}\le 1+d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\vartheta}) < 2^{N+1}\} \, .\qquad\text{(46)}
$$

- [stack density](stack-density.md)
- [local antichain density](local-antichain-density.md)
- [global antichain density](global-antichain-density.md)

We turn to the proof of [antichain tile count](antichain-tile-count.md).

*Proof of antichain tile count: shown with [antichain tile count](antichain-tile-count.md).*
