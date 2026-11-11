---
declaration: section
origin: cited
lean: MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.Closed4Manifold, MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.intHomology, MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.Closed4Manifold.IsAspherical, MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.Closed4Manifold.IsIntegerHomologySphere, MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.aspherical_integer_homology_four_sphere
statement: formalized
---

# Aspherical homology 4-spheres

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres/index.html).

## Closed topological 4-manifold

A closed topological 4-manifold is a nonempty, compact,
connected, Hausdorff, second-countable topological space $M$ together with an atlas of charts
covering $M$, each a homeomorphism from an open subset of $M$ onto an open subset of
$\mathbb{R}^4$ (charts are modelled on all of $\mathbb{R}^4$, not on a half-space, so $M$ has no
boundary).

No smoothness or compatibility between charts is required, so this is a topological, not
necessarily smooth, manifold.

Formalized by `MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.Closed4Manifold`, a structure declared in [WantedExt/Topology/AsphericalHomologySphereWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/AsphericalHomologySphereWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres/index.html#closed4-manifold).

## Integral singular homology as a $\mathbb{Z}$-module

For a natural number $k$ and a
topological space $X$, $H_k(X; \mathbb{Z})$ is the $k$-th singular homology of $X$ with
coefficients in $\mathbb{Z}$, viewed as a $\mathbb{Z}$-module.

Formalized by `MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.intHomology`, a definition declared in [WantedExt/Topology/AsphericalHomologySphereWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/AsphericalHomologySphereWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres/index.html#int-homology).

## Aspherical closed 4-manifold

A closed topological 4-manifold $M$ is aspherical if for
every $k \ge 2$ and every point $x \in M$ the homotopy group $\pi_k(M, x)$ is trivial.

Formalized by `MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.Closed4Manifold.IsAspherical`, a definition declared in [WantedExt/Topology/AsphericalHomologySphereWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/AsphericalHomologySphereWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres/index.html#is-aspherical).

## Integer homology 4-sphere

A closed topological 4-manifold $M$ is an integer homology
4-sphere if for every $k \ge 0$ the integral singular homology $H_k(M; \mathbb{Z})$ is isomorphic,
as a $\mathbb{Z}$-module, to $H_k(S^4; \mathbb{Z})$, where $S^4$ is the unit sphere in
$\mathbb{R}^5$.

Formalized by `MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.Closed4Manifold.IsIntegerHomologySphere`, a definition declared in [WantedExt/Topology/AsphericalHomologySphereWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/AsphericalHomologySphereWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres/index.html#is-integer-homology-sphere).

## Existence of an aspherical integer homology 4-sphere

There is a closed connected
topological 4-manifold $M$ that is aspherical, meaning that for every $k \ge 2$ and every point
$x \in M$ the homotopy group $\pi_k(M, x)$ is trivial, and that is an integer homology 4-sphere,
meaning that for every $k \ge 0$ the integral singular homology $H_k(M; \mathbb{Z})$ is isomorphic
to $H_k(S^4; \mathbb{Z})$, where $S^4$ is the unit sphere in $\mathbb{R}^5$.

## Sources

- J. G. Ratcliffe and S. T. Tschantz, *Some examples of aspherical 4-manifolds that are homology 4-spheres*, arXiv:math/0312436 (2003), solving [Kir97, Problem 4.17]. Earlier, F. Luo constructed an aspherical rational homology 4-sphere (1988). Problem `aspherical_integer_homology_four_sphere` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.AsphericalHomologySphereWanted.Topology.aspherical_integer_homology_four_sphere` is written with `theorem_wanted` in [WantedExt/Topology/AsphericalHomologySphereWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/AsphericalHomologySphereWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres/index.html#aspherical-integer-homology-four-sphere).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Aspherical homology 4-spheres](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/manifolds-geometric-topology/aspherical-homology-4-spheres)
