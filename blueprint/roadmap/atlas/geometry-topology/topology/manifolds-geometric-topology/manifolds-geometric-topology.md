---
declaration: section
origin: cited
lean: MathlibExt.Topology.BudneyGabaiWanted.Topology.budney_gabai_knotted_three_spheres, MathlibExt.Topology.MilnorExoticSphereSevenWanted.Topology.milnor_exotic_sphere_seven, MathlibExt.Topology.HilbertSmith3DWanted.Topology.hilbert_smith_padic_dimension_three
statement: formalized
---

# Manifolds and geometric topology: its own results

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/index.html).

Topological and smooth manifolds in low and high dimensions: surfaces, 3- and 4-manifolds, the Poincaré conjecture, exotic spheres, triangulations, diffeomorphism groups and transformation groups.

## Budney–Gabai knotted three-spheres in $S^1 \times S^3$

Let $S^1 \subset \mathbb{R}^2$ and
$S^3 \subset \mathbb{R}^4$ be the unit spheres, and fix a point $x_0 \in S^1$. There is a sequence
$e_0, e_1, e_2, \dots$ of smooth embeddings $S^3 \to S^1 \times S^3$ such that the complement of
the image of each $e_n$ is connected, each $e_n$ is homotopic to the standard cross-section
$p \mapsto (x_0, p)$, and for $i \ne j$ the images of $e_i$ and $e_j$ are not smoothly isotopic:
there is no smooth map $H : [0, 1] \times S^3 \to S^1 \times S^3$ such that every slice
$H(t, \cdot)$ is a smooth embedding, $H(0, \cdot)$ has the same image as $e_i$, and $H(1, \cdot)$
has the same image as $e_j$.

## Sources

- R. Budney and D. Gabai, 'Knotted 3-balls in S⁴', Corollary 8.6, arXiv:1912.09029v3 (2021), https://arxiv.org/abs/1912.09029. Problem `budney_gabai_knotted_three_spheres` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.BudneyGabaiWanted.Topology.budney_gabai_knotted_three_spheres` is written with `theorem_wanted` in [WantedExt/Topology/BudneyGabaiWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/BudneyGabaiWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/index.html#budney-gabai-knotted-three-spheres).

## Milnor's exotic 7-sphere

There is a smooth manifold $M$ modelled on $\mathbb{R}^7$ (a
topological space with a $C^\infty$ atlas of charts into $\mathbb{R}^7$) that is homeomorphic to
the unit sphere $S^7 \subset \mathbb{R}^8$ but is not diffeomorphic to $S^7$ with its standard
smooth structure.

## Sources

- J. Milnor, On manifolds homeomorphic to the 7-sphere, Ann. of Math. 64 (1956), 399-405. Problem `milnor_exotic_sphere_seven` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.MilnorExoticSphereSevenWanted.Topology.milnor_exotic_sphere_seven` is written with `theorem_wanted` in [WantedExt/Topology/MilnorExoticSphereSevenWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/MilnorExoticSphereSevenWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/index.html#milnor-exotic-sphere-seven).

## Pardon's theorem: the p-adic integers cannot act faithfully and continuously on a connected 3-manifold

**Pardon's theorem: the p-adic integers cannot act faithfully and continuously on a
connected 3-manifold.** Let $p$ be a prime and $M$ a connected, Hausdorff, second-countable
topological space with an atlas of charts modelled on $\mathbb{R}^3$, that is, a connected
topological 3-manifold without boundary. Then there is no faithful action of the additive group
$\mathbb{Z}_p$ of $p$-adic integers on $M$ that is jointly continuous as a map
$\mathbb{Z}_p \times M \to M$.

This is the $p$-adic case of the Hilbert–Smith conjecture in dimension three; deducing that every
locally compact group acting faithfully on a connected 3-manifold is a Lie group also needs the
classical reduction to $\mathbb{Z}_p$-actions, which is not part of this statement.

## Sources

- John Pardon, 'The Hilbert-Smith conjecture for three-manifolds', Journal of the American Mathematical Society 26 (2013), no. 3, 879-899, Theorem 1.5. https://doi.org/10.1090/S0894-0347-2013-00766-3. Problem `hilbert_smith_padic_dimension_three` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.HilbertSmith3DWanted.Topology.hilbert_smith_padic_dimension_three` is written with `theorem_wanted` in [WantedExt/Topology/HilbertSmith3DWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/HilbertSmith3DWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/index.html#hilbert-smith-padic-dimension-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Manifolds and geometric topology](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/manifolds-geometric-topology)
