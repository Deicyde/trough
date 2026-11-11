---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.uniformConvexSpace_of_finiteDimensional_strictConvexSpace, MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.strictConvexSpace_iff_uniformConvexSpace_of_finiteDimensional, MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.exists_tendsto_of_minimizingSequence, MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.exists_unique_nearestPoint_of_minimizingSequence_of_finiteDimensional, MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.exists_unique_tendsto_of_minimizingSequence_of_finiteDimensional
statement: formalized
proof: formalized
---

# Uniformly convex spaces

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces/index.html).

## Strict convexity implies uniform convexity in finite dimensions

In a finite-dimensional real normed space, strict convexity implies
uniform convexity. The proof maximizes `‖x + y‖` over the compact set of
pairs of unit vectors at distance at least `ε`; strict convexity says the
maximum is `< 2`, and the gap is the required `δ`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.uniformConvexSpace_of_finiteDimensional_strictConvexSpace`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces/index.html#uniform-convex-space-of-finite-dimension).

## Strict and uniform convexity agree in finite dimensions

In finite dimensions, strict convexity and uniform convexity are
equivalent.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.strictConvexSpace_iff_uniformConvexSpace_of_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces/index.html#strict-convex-space-iff-uniform-convex-s).

## Convergence of minimizing sequences in uniformly convex spaces

In a complete uniformly convex space, a minimizing sequence for the
distance from a point `x` to a closed convex set `K` converges to a point
of `K` attaining that distance. The argument is the usual one: if the
sequence were not Cauchy, two far-apart almost-minimizing terms would have
normalized displacements far apart on the unit sphere, and uniform
convexity would force their midpoint to beat the infimum, contradicting
convexity of `K`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.exists_tendsto_of_minimizingSequence`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces/index.html#exists-tendsto-of-minimizing-sequence).

## Unique nearest point from a minimizing sequence in finite dimensions

In a finite-dimensional strictly convex space, a minimizing sequence for
the distance to a closed convex set supplies a unique nearest point. The
uniqueness clause only assumes that a second point belongs to the set and
attains the distance; it does not assume that the minimizing sequence
converges to that point.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.exists_unique_nearestPoint_of_minimizingSequence_of_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces/index.html#exists-unique-nearest-point-of-minimizin).

## Minimizing sequences converge to the unique nearest point

In a finite-dimensional strictly convex space, a minimizing sequence for
the distance to a closed convex set converges to the unique point of the
set attaining that distance. This preserves the original combined API as a
corollary of nearest-point uniqueness and minimizing-sequence convergence.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.UniformConvex.exists_unique_tendsto_of_minimizingSequence_of_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/UniformConvex.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces/index.html#exists-unique-tendsto-of-minimizing-sequ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Uniformly convex spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/uniformly-convex-spaces)
