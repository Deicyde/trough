---
declaration: section
origin: cited
lean: MathlibExt.Topology.CerfGammaFourWanted.Topology.cerf_gamma_four, MathlibExt.Topology.Manifold.ScottishBook29Wanted.identity_component_of_sphere_homeomorphism_group_simple, MathlibExt.Topology.SmaleConjectureWanted.Topology.smale_conjecture, MathlibExt.Topology.WatanabeSmaleDisproofWanted.Topology.watanabe_four_dim_smale_disproof
statement: formalized
---

# Homeomorphism and diffeomorphism groups of spheres

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/homeomorphism-and-diffeomorphism-groups-of-spher/index.html).

## Cerf's theorem $\Gamma_4 = 0$

Let $S^3 \subset \mathbb{R}^4$ be the unit sphere. Every
smooth diffeomorphism $f$ of $S^3$ is smoothly isotopic to the restriction of a linear isometry of
$\mathbb{R}^4$: there are an orthogonal matrix $A \in O(4)$ and smooth maps
$F, F' : [0, 1] \times S^3 \to S^3$ such that for every $t \in [0, 1]$ the maps $F(t, \cdot)$ and
$F'(t, \cdot)$ are inverse to each other, and $F(0, p) = f(p)$ and $F(1, p) = Ap$ for all
$p \in S^3$.

## Sources

- J. Cerf, Sur les diffeomorphismes de la sphere de dimension trois, Lecture Notes in Mathematics 53, Springer (1968). Problem `cerf_gamma_four` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.CerfGammaFourWanted.Topology.cerf_gamma_four` is written with `theorem_wanted` in [WantedExt/Topology/CerfGammaFourWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/CerfGammaFourWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/homeomorphism-and-diffeomorphism-groups-of-spher/index.html#cerf-gamma-four).

## Normal subgroups of the identity component of the homeomorphism group of a sphere

Let
$n \ne 4$ be a natural number and let $S^n$ be the unit sphere in $\mathbb{R}^{n+1}$. Give the
group $\mathrm{Homeo}(S^n)$ of homeomorphisms of $S^n$ the topology induced by the embedding
$h \mapsto (h, h^{-1})$ into pairs of continuous self-maps of $S^n$ with the compact-open
topology, and let $G_0$ be the connected component of the identity in $\mathrm{Homeo}(S^n)$.
If $N$ is a subgroup of $\mathrm{Homeo}(S^n)$ contained in $G_0$ such that $h k h^{-1} \in N$
for all $h \in G_0$ and $k \in N$, then either $N$ is the trivial subgroup or $G_0 \subseteq N$.
In other words, the only normal subgroups of $G_0$ are the trivial one and $G_0$ itself.

This is Ulam's Problem 29 of the Scottish Book, which asked the question for every $n$; the
case $n = 4$ is excluded here. The restriction $n \ne 4$ is the caveat attached to the sphere
case in the Encyclopedia of Mathematics; Epstein's theorem itself is stated for manifolds in
general.

## Sources

- S. Ulam, Problem 29 of the Scottish Book; D. B. A. Epstein, The simplicity of certain groups of homeomorphisms, Compositio Mathematica 22 (1970), 165-173; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.Manifold.ScottishBook29Wanted.identity_component_of_sphere_homeomorphism_group_simple` is written with `theorem_wanted` in [WantedExt/Topology/Manifold/ScottishBook29Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/Manifold/ScottishBook29Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/homeomorphism-and-diffeomorphism-groups-of-spher/index.html#identity-component-of-sphere-homeomorphi).

## Smale conjecture (Hatcher), relative parametrized form

Let $n \ge 1$ and let $X$ be a
compact, Hausdorff, second-countable smooth manifold with boundary modelled on the
$n$-dimensional half-space, with boundary $\partial X$. Write $S^3$ for the unit sphere of
$\mathbb{R}^4$ and let the orthogonal group $O(4)$ act linearly on it. Let
$F, F' : X \times S^3 \to S^3$ be smooth maps with $F(x, F'(x, p)) = p$ and $F'(x, F(x, p)) = p$
for all $x \in X$ and $p \in S^3$, and let $\psi_\partial : \partial X \to O(4)$ be a continuous
map with $F(b, p) = \psi_\partial(b)\, p$ for all $b \in \partial X$ and $p \in S^3$. Then there
are a continuous map $\psi : X \to O(4)$ that agrees with $\psi_\partial$ on $\partial X$ and
smooth maps $H, H' : X \times [0, 1] \times S^3 \to S^3$ such that for all $x \in X$,
$t \in [0, 1]$ and $p \in S^3$ we have $H(x, t, H'(x, t, p)) = p$, $H'(x, t, H(x, t, p)) = p$,
$H(x, 0, p) = F(x, p)$ and $H(x, 1, p) = \psi(x)\, p$, and $H(b, t, p) = F(b, p)$ whenever
$b \in \partial X$.

Thus each $F(x, \cdot)$ is a diffeomorphism of $S^3$, and $H$ is a smooth isotopy through
diffeomorphisms, relative to $\partial X$, from the family $F$ to the linear family $\psi$.

## Sources

- A. Hatcher, A proof of the Smale conjecture, Diff(S3) = O(4), Ann. of Math. 117 (1983). Problem `smale_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.SmaleConjectureWanted.Topology.smale_conjecture` is written with `theorem_wanted` in [WantedExt/Topology/SmaleConjectureWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/SmaleConjectureWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/homeomorphism-and-diffeomorphism-groups-of-spher/index.html#smale-conjecture).

## The four-dimensional Smale conjecture is false (Watanabe)

Write $S^4$ for the unit sphere
of $\mathbb{R}^5$ and let the orthogonal group $O(5)$ act linearly on it. There are an $n \ge 1$,
a compact, Hausdorff, second-countable smooth manifold $X$ with boundary modelled on the
$n$-dimensional half-space, with boundary $\partial X$, smooth maps
$F, F' : X \times S^4 \to S^4$ with $F(x, F'(x, p)) = p$ and $F'(x, F(x, p)) = p$ for all
$x \in X$ and $p \in S^4$, and a continuous map $\psi_\partial : \partial X \to O(5)$ with
$F(b, p) = \psi_\partial(b)\, p$ for all $b \in \partial X$ and $p \in S^4$, such that the
following fails: there are a continuous map $\psi : X \to O(5)$ that agrees with
$\psi_\partial$ on $\partial X$ and smooth maps $H, H' : X \times [0, 1] \times S^4 \to S^4$
such that for all $x \in X$, $t \in [0, 1]$ and $p \in S^4$ we have
$H(x, t, H'(x, t, p)) = p$, $H'(x, t, H(x, t, p)) = p$, $H(x, 0, p) = F(x, p)$ and
$H(x, 1, p) = \psi(x)\, p$, and $H(b, t, p) = F(b, p)$ whenever $b \in \partial X$.

In other words, the relative parametrized form of the statement that $O(5) \to \mathrm{Diff}(S^4)$
is a homotopy equivalence, the analogue of Hatcher's theorem for $S^3$, does not hold.

## Sources

- T. Watanabe, *Some exotic nontrivial elements of the rational homotopy groups of Diff(S⁴)*, arXiv:1812.02448 (2018). Pairs with the positive S³ statement of Hatcher (Ann. of Math. 117, 1983). Problem `watanabe_four_dim_smale_disproof` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.WatanabeSmaleDisproofWanted.Topology.watanabe_four_dim_smale_disproof` is written with `theorem_wanted` in [WantedExt/Topology/WatanabeSmaleDisproofWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/WatanabeSmaleDisproofWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/homeomorphism-and-diffeomorphism-groups-of-spher/index.html#watanabe-four-dim-smale-disproof).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Homeomorphism and diffeomorphism groups of spheres](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/homeomorphism-and-diffeomorphism-groups-of-spher/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/manifolds-geometric-topology/homeomorphism-and-diffeomorphism-groups-of-spher)
