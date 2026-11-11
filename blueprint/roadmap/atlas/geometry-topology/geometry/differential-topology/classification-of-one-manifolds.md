---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Manifold.OneDimensionalWanted.connected_boundaryless_one_manifold_classification, MathlibExt.Geometry.Manifold.OneDimensionalWanted.compact_connected_one_manifold_with_boundary_classification
statement: formalized
proof: formalized
---

# Classification of one-manifolds

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/classification-of-one-manifolds/index.html).

## Classification of connected $1$-manifolds without boundary

Every connected, Hausdorff,
second-countable smooth $1$-manifold $M$ without boundary is diffeomorphic either to the circle
$S^1$ or to the real line $\mathbb{R}$.

## Sources

- Classification of connected boundaryless 1-manifolds; Milnor (1965); Hirsch; Lean states dichotomy specialization for `𝓡 1`.

Formalized by `MathlibExt.Geometry.Manifold.OneDimensionalWanted.connected_boundaryless_one_manifold_classification`, a theorem declared in [MathlibExt/Geometry/Manifold/OneDimensional.lean, line 3350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/OneDimensional.lean#L3350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/classification-of-one-manifolds/index.html#connected-boundaryless-one-manifold-clas).

## Classification of compact connected $1$-manifolds with boundary

Every compact, connected,
Hausdorff, second-countable smooth $1$-manifold $M$ with (possibly empty) boundary is
diffeomorphic either to the circle $S^1$ or to the closed interval $[0, 1]$.

## Sources

- Classification of 1-manifolds with boundary; Hirsch, Differential Topology; J. Lee, Introduction to Smooth Manifolds, 2nd ed., collar theorem; Lean states compact connected `𝓡∂ 1` with closed interval specialization.

Formalized by `MathlibExt.Geometry.Manifold.OneDimensionalWanted.compact_connected_one_manifold_with_boundary_classification`, a theorem declared in [MathlibExt/Geometry/Manifold/OneDimensional.lean, line 5413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/OneDimensional.lean#L5413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/classification-of-one-manifolds/index.html#compact-connected-one-manifold-with-boun).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Classification of one-manifolds](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/classification-of-one-manifolds/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/differential-topology/classification-of-one-manifolds)
