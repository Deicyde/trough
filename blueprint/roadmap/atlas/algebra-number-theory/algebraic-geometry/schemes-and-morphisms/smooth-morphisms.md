---
declaration: section
origin: cited
lean: ringKrullDim_le_of_faithfullyFlat, ringKrullDim_le_of_isStandardSmoothOfRelativeDimension, SmoothKrullDimAux.ringKrullDim_le_of_ringHom, AlgebraicGeometry.SmoothOfRelativeDimension.topologicalKrullDim_le, AlgebraicGeometry.isReduced_of_smooth_over_field, AlgebraicGeometry.Smooth.isReduced_of_isReduced_of_isLocallyNoetherian, AlgebraicGeometry.Smooth.exists_smoothOfRelativeDimension_of_preconnectedSpace
statement: formalized
proof: formalized
---

# Smooth morphisms

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html).

## Krull dimension does not increase along faithfully flat maps

Krull dimension does not increase along faithfully flat ring maps.

Formalized by `ringKrullDim_le_of_faithfullyFlat`, a theorem declared in [MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html#ring-krull-dim-le-of-faithfully-flat).

## Krull dimension of a standard smooth algebra

A standard smooth algebra of relative dimension `n` has Krull dimension
at most `n`.

Formalized by `ringKrullDim_le_of_isStandardSmoothOfRelativeDimension`, a theorem declared in [MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html#ring-krull-dim-le-of-is-standard-smooth).

## Krull dimension of a standard smooth algebra over a field

A standard smooth algebra map from a field has Krull dimension at most
the relative dimension.

Formalized by `SmoothKrullDimAux.ringKrullDim_le_of_ringHom`, a theorem declared in [MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html#ring-krull-dim-le-of-ring-hom).

## Dimension of a scheme smooth of relative dimension $n$

A scheme smooth of relative dimension `n` over a field has topological
Krull dimension at most `n`.

Formalized by `AlgebraicGeometry.SmoothOfRelativeDimension.topologicalKrullDim_le`, a theorem declared in [MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/SmoothKrullDim.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html#topological-krull-dim-le).

## Smooth schemes over a field are reduced

A scheme smooth over a field is reduced.

Formalized by `AlgebraicGeometry.isReduced_of_smooth_over_field`, a theorem declared in [MathlibExt/AlgebraicGeometry/SmoothReduced.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/SmoothReduced.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html#is-reduced-of-smooth-over-field).

## Smooth morphisms preserve reducedness

A smooth morphism with reduced locally Noetherian target has reduced source.

Formalized by `AlgebraicGeometry.Smooth.isReduced_of_isReduced_of_isLocallyNoetherian`, a theorem declared in [MathlibExt/AlgebraicGeometry/SmoothReducedSource.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/SmoothReducedSource.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html#is-reduced-of-is-reduced-of-is-locally-n).

## Smooth maps from a preconnected scheme have constant relative dimension

A smooth morphism from a preconnected scheme is smooth of some fixed
relative dimension.

Formalized by `AlgebraicGeometry.Smooth.exists_smoothOfRelativeDimension_of_preconnectedSpace`, a theorem declared in [MathlibExt/AlgebraicGeometry/SmoothRelDim.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/SmoothRelDim.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html#exists-smooth-of-relative-dimension-of-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smooth morphisms](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/schemes-and-morphisms/smooth-morphisms)
