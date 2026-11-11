---
declaration: section
origin: cited
lean: IsThreeManifold, IsThreeManifoldWithBoundary, isThreeManifold_iff, IsThreeManifold.locallyCompactSpace
statement: formalized
proof: formalized
---

# Topological 3-manifolds

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/topological-3-manifolds/index.html).

## Topological 3-manifold

Let $M$ be a topological space equipped with an atlas of charts,
each a homeomorphism from an open subset of $M$ onto an open subset of $\mathbb{R}^3$, whose domains
cover $M$. Then $M$ is a topological 3-manifold if it is Hausdorff and second-countable.

Formalized by `IsThreeManifold`, a class declared in [MathlibExt/Topology/ThreeManifold.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ThreeManifold.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/topological-3-manifolds/index.html#is-three-manifold).

## Topological 3-manifold with boundary

A **topological 3-manifold with boundary**: a Hausdorff, second-countable topological space
locally homeomorphic to the Euclidean half-space `EuclideanHalfSpace 2`.

Formalized by `IsThreeManifoldWithBoundary`, a class declared in [MathlibExt/Topology/ThreeManifold.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ThreeManifold.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/topological-3-manifolds/index.html#is-three-manifold-with-boundary).

## Characterization of topological 3-manifolds

Let $M$ be a topological space equipped
with an atlas of charts modelled on $\mathbb{R}^3$, so that $M$ is locally homeomorphic to
$\mathbb{R}^3$. Then $M$ is a topological 3-manifold if and only if $M$ is Hausdorff and
second-countable.

Formalized by `isThreeManifold_iff`, a theorem declared in [MathlibExt/Topology/ThreeManifold.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ThreeManifold.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/topological-3-manifolds/index.html#is-three-manifold-iff).

## Topological 3-manifolds are locally compact

Every topological 3-manifold $M$ is locally
compact, since $\mathbb{R}^3$ is.

Formalized by `IsThreeManifold.locallyCompactSpace`, a theorem declared in [MathlibExt/Topology/ThreeManifold.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/ThreeManifold.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/topological-3-manifolds/index.html#locally-compact-space).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Topological 3-manifolds](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/topological-3-manifolds/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/manifolds-geometric-topology/topological-3-manifolds)
