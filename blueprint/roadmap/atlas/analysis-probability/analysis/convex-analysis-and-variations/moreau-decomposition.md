---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_eq_iff, MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_inner_le_zero, MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_inner_self, MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_eq_of_forall_inner_le_zero, MathlibExt.Analysis.Convex.MoreauDecomposition.polarCone, MathlibExt.Analysis.Convex.MoreauDecomposition.mem_polarCone, MathlibExt.Analysis.Convex.MoreauDecomposition.sub_convexProjection_mem_polarCone, MathlibExt.Analysis.Convex.MoreauDecomposition.polarCone_eq_innerDual_neg
statement: formalized
proof: formalized
---

# Moreau decomposition

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html).

## Variational characterization of projection onto a convex cone

Variational characterization of the projection onto a cone with complete carrier:
`p` is the projection of `x` iff the residual pairs nonpositively with the
cone and is orthogonal to `p`. The ambient space need not be complete.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_eq_iff`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#convex-projection-eq-iff).

## Cone projection residual pairs nonpositively with the cone

The residual of the cone projection pairs nonpositively with every point of the cone.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_inner_le_zero`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#convex-projection-inner-le-zero).

## Cone projection residual is orthogonal to the projection

The residual of the cone projection is orthogonal to the projection.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_inner_self`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#convex-projection-inner-self).

## Variational characterization determines the cone projection

A point satisfying the cone variational characterization is the projection.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_eq_of_forall_inner_le_zero`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#convex-projection-eq-of-forall-inner-le).

## Negative polar cone

The negative polar is the standard dual cone of the negated set. Continuity
makes its carrier closed without requiring completeness of the ambient space.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.polarCone`, a definition declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#polar-cone).

## Membership in the negative polar cone

Membership in the negative polar uses the nonpositive inner-product convention.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.mem_polarCone`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#mem-polar-cone).

## Cone projection residual lies in the negative polar

The residual of a cone projection lies in its negative polar.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.sub_convexProjection_mem_polarCone`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#sub-convex-projection-mem-polar-cone).

## Negative polar agrees with the inner dual of the negated cone

In a complete ambient space, the negative polar agrees with Mathlib's
inner dual of the negated carrier.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.polarCone_eq_innerDual_neg`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#polar-cone-eq-inner-dual-neg).

## Moreau decomposition, polar form

The cone projection's residual is the
projection onto its negative polar. This accepts a Mathlib proper cone directly.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.convexProjection_polarCone`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#convex-projection-polar-cone).

## Moreau decomposition

A point is the sum of its projections onto a
proper cone and its negative polar, and the projections are orthogonal.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.moreau_decomposition`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#moreau-decomposition).

## Bipolar theorem for closed convex cones

The negative bipolar of a proper cone is itself, by Mathlib's inner-dual bipolar theorem.

Formalized by `MathlibExt.Analysis.Convex.MoreauDecomposition.polarCone_polarCone`, a theorem declared in [MathlibExt/Analysis/Convex/MoreauDecomposition.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/MoreauDecomposition.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html#polar-cone-polar-cone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moreau decomposition](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations/moreau-decomposition)
