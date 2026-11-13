---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.IsGraphon, MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.labelledDensity, MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.density, MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.WeaklyIsomorphic, MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.IsFinitelyForcible, MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.finitelyForcibleOptimum, MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.finitelyForcibleOptimum_refuted
statement: formalized
---

# Finitely forcible graphons

7 results, 6 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html).

## Graphon

A graphon is a function $W$ of two real variables that is jointly measurable
(measurable as a function on $\mathbb{R}^2$), symmetric ($W(x, y) = W(y, x)$ for all real $x, y$)
and takes values in $[0, 1]$ at every point of $\mathbb{R}^2$.

Only the values of $W$ on $[0, 1]^2$ enter the densities.

Formalized by `MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.IsGraphon`, a definition declared in [WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html#is-graphon).

## Labelled density

For a graph $G$ on the vertex set $\{0, \dots, k-1\}$ and a function $W$
of two real variables, the labelled density of $G$ in $W$ is

$$\tau(G, W) = \int_{[0,1]^k} \prod_{i < j} w_{ij}(x) \, dx,$$

where the integral is with respect to Lebesgue measure (and is taken to be $0$ if the integrand is
not integrable), the product runs over the pairs $i < j$ of vertices, and $w_{ij}(x) = W(x_i, x_j)$
if $i$ and $j$ are adjacent in $G$ and $w_{ij}(x) = 1 - W(x_i, x_j)$ otherwise.

When $W$ is a graphon, $\tau(G, W)$ is the probability that the $W$-random graph on
$\{0, \dots, k-1\}$ (independent uniform points $x_i \in [0, 1]$, each pair $\{i, j\}$ joined
independently with probability $W(x_i, x_j)$) equals $G$.

Formalized by `MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.labelledDensity`, a definition declared in [WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html#labelled-density).

## Density of a graph in a graphon

For a graph $H$ on the vertex set $\{0, \dots, k-1\}$ and
a function $W$ of two real variables, the density $d(H, W)$ is the sum of the labelled densities
$\tau(G, W)$ over all graphs $G$ on $\{0, \dots, k-1\}$ that are isomorphic to $H$.

When $W$ is a graphon, $d(H, W)$ is the probability that the $W$-random graph on
$\{0, \dots, k-1\}$ is isomorphic to $H$.

Formalized by `MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.density`, a definition declared in [WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html#density).

## Weak isomorphism

Two functions $W_1$ and $W_2$ of two real variables are weakly isomorphic
if $d(H, W_1) = d(H, W_2)$ for every natural number $k$ and every graph $H$ on the vertex set
$\{0, \dots, k-1\}$, where $d(H, W)$ is the density of $H$ in $W$.

The notion is meant for graphons, but no graphon condition is imposed on $W_1$ and $W_2$.

Formalized by `MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.WeaklyIsomorphic`, a definition declared in [WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html#weakly-isomorphic).

## Finitely forcible graphon

A function $W$ of two real variables is finitely forcible if
there are finitely many graphs $H_1, \dots, H_\ell$ such that every graphon $W'$ with
$d(H_i, W') = d(H_i, W)$ for all $i$ is weakly isomorphic to $W$.

Formalized by `MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.IsFinitelyForcible`, a definition declared in [WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html#is-finitely-forcible).

## Lovász's finitely forcible optimum conjecture

The proposition that for all graphs
$H_1, \dots, H_\ell$ and reals $d_1, \dots, d_\ell$, if some graphon $W$ satisfies
$d(H_i, W) = d_i$ for every $i$, then some finitely forcible graphon $W_0$ satisfies
$d(H_i, W_0) = d_i$ for every $i$.

This is Lovász's conjecture that every extremal problem has a finitely forcible optimum
(Oberwolfach Report 11/2010, p. 554), in the form of Grzesik, Kráľ and Lovász, Conjecture 1.

Formalized by `MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.finitelyForcibleOptimum`, a definition declared in [WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html#finitely-forcible-optimum).

## Lovász's finitely forcible optimum conjecture is false

There are graphs $H_1, \dots, H_\ell$
and reals $d_1, \dots, d_\ell$ such that some graphon $W$ satisfies $d(H_i, W) = d_i$ for every $i$,
but no finitely forcible graphon $W_0$ satisfies $d(H_i, W_0) = d_i$ for every $i$.

Grzesik, Kráľ and Lovász (Theorem 18) construct such graphs and reals for which every graphon
$W$ with $d(H_i, W) = d_i$ for all $i$ is weakly isomorphic to a member of a family none of whose
graphons is finitely forcible.

## Sources

- L. Lovász (joint work with B. Szegedy), Extremal graphs and graph limits, in Graph Theory, Oberwolfach Reports 7 (2010), no. 11, pp. 554-555, question 1, DOI 10.4171/OWR/2010/11; resolution: A. Grzesik, D. Kráľ and L. M. Lovász, Elusive extremal graphs, Proc. Lond. Math. Soc. (3) 121 (2020), 1685-1736, DOI 10.1112/plms.12382, arXiv:1807.01141, Conjecture 1 (Lovász): if some convergent sequence of graphs has limit densities d(H_i) = d_i for i = 1, ..., ℓ, then some finitely forcible such sequence does; Theorem 18: there are a family W of graphons, graphs H_1, ..., H_ℓ and reals d_1, ..., d_ℓ such that a graphon is weakly isomorphic to a member of W if and only if d(H_i, W) = d_i for all i, and no graphon in W is finitely forcible; 'Our main result (Theorem 18) implies that the conjecture is false', https://arxiv.org/abs/1807.01141.

Stated but not proved: `MathlibExt.Combinatorics.FinitelyForcibleOptimumOWR4212Problem011Wanted.finitelyForcibleOptimum_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/FinitelyForcibleOptimumOWR4212Problem011Wanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html#finitely-forcible-optimum-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finitely forcible graphons](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/random-graphs/finitely-forcible-graphons)
