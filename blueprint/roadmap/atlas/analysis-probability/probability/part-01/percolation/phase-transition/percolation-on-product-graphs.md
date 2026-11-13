---
declaration: section
origin: cited
lean: MathlibExt.Probability.ProductBondPercolation.intLine, MathlibExt.Probability.ProductBondPercolation.prodGraph, MathlibExt.Probability.ProductBondPercolation.configGraph, MathlibExt.Probability.ProductBondPercolation.cluster, MathlibExt.Probability.ProductBondPercolation.bernoulliLaw, MathlibExt.Probability.ProductBondPercolation.AlmostSurely, MathlibExt.Probability.ProductBondPercolation.openSubgraph, MathlibExt.Probability.ProductBondPercolation.gcluster
statement: formalized
proof: formalized
---

# Percolation on product graphs

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html).

## The integer line graph

The integer line is the simple graph on $\mathbb{Z}$ in which
$m$ and $n$ are adjacent exactly when $|m - n| = 1$.

Formalized by `MathlibExt.Probability.ProductBondPercolation.intLine`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#int-line).

## The product graph $G \times \mathbb{Z}$

For a simple graph $G$ on $V$, the graph
$G \times \mathbb{Z}$ is the box product of $G$ with the integer line: its vertex set is
$V \times \mathbb{Z}$, and $(v, m)$ and $(w, n)$ are adjacent exactly when either $v$ and $w$
are adjacent in $G$ and $m = n$, or $v = w$ and $|m - n| = 1$.

Formalized by `MathlibExt.Probability.ProductBondPercolation.prodGraph`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#prod-graph).

## Open subgraph of the product graph

Let $G$ be a simple graph on $V$, let
$G \times \mathbb{Z}$ denote the box product of $G$ with the integer line, and let $\omega$
assign true or false to every unordered pair of points of $V \times \mathbb{Z}$. The open
subgraph of $G \times \mathbb{Z}$ determined by $\omega$ is the simple graph on
$V \times \mathbb{Z}$ in which $a$ and $b$ are adjacent exactly when they are adjacent in
$G \times \mathbb{Z}$ and $\omega(\{a, b\})$ is true.

Formalized by `MathlibExt.Probability.ProductBondPercolation.configGraph`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#config-graph).

## Open cluster in the product graph

Let $G$ be a simple graph on $V$, let
$G \times \mathbb{Z}$ denote the box product of $G$ with the integer line, let $\omega$ assign
true or false to every unordered pair of points of $V \times \mathbb{Z}$, and let
$x \in V \times \mathbb{Z}$. The open cluster of $x$ is the set of points
$y \in V \times \mathbb{Z}$ that are reachable from $x$ (including $x$ itself) in the open
subgraph of $G \times \mathbb{Z}$ determined by $\omega$, that is, joined to $x$ by a path whose
edges $e$ are edges of $G \times \mathbb{Z}$ with $\omega(e)$ true.

Formalized by `MathlibExt.Probability.ProductBondPercolation.cluster`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#cluster).

## Bernoulli bond law on $V \times \mathbb{Z}$

For a type $V$ and $0 \le p \le 1$, the
Bernoulli($p$) bond law on $V \times \mathbb{Z}$ is the product measure on configurations
$\omega$, which assign true (open) or false (closed) to every unordered pair $\{a, b\}$ of
points of $V \times \mathbb{Z}$ (with $a = b$ allowed), under which the values $\omega(e)$ are
independent and each is true with probability $p$ and false with probability $1 - p$.

Formalized by `MathlibExt.Probability.ProductBondPercolation.bernoulliLaw`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#bernoulli-law).

## Almost-sure properties under the Bernoulli bond law

Let $V$ be a type, let $p$ be a real
number with $0 \le p \le 1$, and let $P$ be a property of configurations $\omega$, that is, of
functions assigning true or false to every unordered pair $\{a, b\}$ of points of
$V \times \mathbb{Z}$ (with $a = b$ allowed). We say that $P$ holds almost surely if $P(\omega)$
holds for almost every $\omega$ with respect to the Bernoulli($p$) bond law on
$V \times \mathbb{Z}$.

Formalized by `MathlibExt.Probability.ProductBondPercolation.AlmostSurely`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#almost-surely).

## Open subgraph of a graph

Let $G$ be a simple graph on $V$ and let $\omega$ assign true or
false to every unordered pair of elements of $V$. The open subgraph of $G$ determined by
$\omega$ is the simple graph on $V$ in which $a$ and $b$ are adjacent exactly when they are
adjacent in $G$ and $\omega(\{a, b\})$ is true.

Formalized by `MathlibExt.Probability.ProductBondPercolation.openSubgraph`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#open-subgraph).

## Open cluster in a graph

Let $G$ be a simple graph on $V$, let $\omega$ assign true or
false to every unordered pair of elements of $V$, and let $x \in V$. The open cluster of $x$ is
the set of vertices $y \in V$ that are reachable from $x$ (including $x$ itself) in the open
subgraph of $G$ determined by $\omega$, that is, joined to $x$ by a path whose edges $e$ are
edges of $G$ with $\omega(e)$ true.

Formalized by `MathlibExt.Probability.ProductBondPercolation.gcluster`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#gcluster).

## Bernoulli bond law on $V$

For a type $V$ and $0 \le p \le 1$, the Bernoulli($p$) bond
law on $V$ is the product measure on configurations $\omega$, which assign true (open) or false
(closed) to every unordered pair $\{a, b\}$ of elements of $V$ (with $a = b$ allowed), under
which the values $\omega(e)$ are independent and each is true with probability $p$ and false
with probability $1 - p$.

Formalized by `MathlibExt.Probability.ProductBondPercolation.gbernoulliLaw`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#gbernoulli-law).

## Critical probability for bond percolation

For a simple graph $G$ on a countable vertex
set $V$, the critical probability $p_c(G)$ is the infimum of the set consisting of $1$ together
with every $p \in [0, 1]$ for which, under the Bernoulli($p$) bond law on $V$, the event that
the open cluster in $G$ of some vertex is infinite has positive probability. In particular
$p_c(G) = 1$ when no such $p$ exists.

Countability of $V$ makes the event that some open cluster is infinite measurable for the
product law.

Formalized by `MathlibExt.Probability.ProductBondPercolation.criticalProb`, a definition declared in [MathlibExt/Probability/ProductBondPercolation.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ProductBondPercolation.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html#critical-prob).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Percolation on product graphs](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/phase-transition/percolation-on-product-graphs)
