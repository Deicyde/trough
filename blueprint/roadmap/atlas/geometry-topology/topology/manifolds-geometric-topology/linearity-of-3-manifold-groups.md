---
declaration: section
origin: cited
lean: MathlibExt.Topology.NonlinearThreeManifoldGroupWanted.Topology.Closed3Manifold, MathlibExt.Topology.NonlinearThreeManifoldGroupWanted.Topology.nonlinear_three_manifold_group
statement: formalized
---

# Linearity of 3-manifold groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearity-of-3-manifold-groups/index.html).

## Closed topological 3-manifold

A closed topological 3-manifold is a nonempty, compact,
connected, Hausdorff, second-countable topological space $M$ together with an atlas of charts,
homeomorphisms from open subsets of $M$ onto open subsets of $\mathbb{R}^3$, whose domains cover
$M$. Since the charts land in $\mathbb{R}^3$ itself rather than in a half-space, $M$ has no
boundary.

Formalized by `MathlibExt.Topology.NonlinearThreeManifoldGroupWanted.Topology.Closed3Manifold`, a structure declared in [WantedExt/Topology/NonlinearThreeManifoldGroupWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/NonlinearThreeManifoldGroupWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearity-of-3-manifold-groups/index.html#closed3-manifold).

## A closed 3-manifold group with no faithful representation in $GL_4(\mathbb{R})$

There
is a closed connected topological 3-manifold $M$ with a point $x$ such that no group
homomorphism from the fundamental group $\pi_1(M, x)$ to $GL_4(\mathbb{R})$ is injective.

## Sources

- J. O. Button, *Aspherical 3-manifold groups not in GL(4, k) for any field k*, arXiv:1404.4639 (2014). See the discussion of [Kir97, Problem 3.33] in the K3 problem list. Problem `nonlinear_three_manifold_group` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.NonlinearThreeManifoldGroupWanted.Topology.nonlinear_three_manifold_group` is written with `theorem_wanted` in [WantedExt/Topology/NonlinearThreeManifoldGroupWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/NonlinearThreeManifoldGroupWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearity-of-3-manifold-groups/index.html#nonlinear-three-manifold-group).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linearity of 3-manifold groups](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearity-of-3-manifold-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/manifolds-geometric-topology/linearity-of-3-manifold-groups)
