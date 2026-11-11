---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Module.BestApproximation.exists_bestApproximation_of_finiteDimensional, MathlibExt.Analysis.Normed.Module.BestApproximation.eq_of_isBestApproximation_of_strictConvexSpace, MathlibExt.Analysis.Normed.Module.BestApproximation.exists_unique_bestApproximation_of_finiteDimensional
statement: formalized
proof: formalized
---

# Best approximation in normed spaces

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/best-approximation-in-normed-spaces/index.html).

## Existence of best approximations in finite-dimensional subspaces

Every point of a normed space has a nearest point in a
finite-dimensional subspace (proximinality). No completeness hypothesis on
the ambient space is needed: completeness enters only through the
finite-dimensional subspace, whose closed balls are compact.

Formalized by `MathlibExt.Analysis.Normed.Module.BestApproximation.exists_bestApproximation_of_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/Normed/Module/BestApproximation.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/BestApproximation.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/best-approximation-in-normed-spaces/index.html#exists-best-approximation-of-finite-dime).

## Uniqueness of best approximation in strictly convex spaces

In a strictly convex real normed space, a convex set contains at most one
point nearest to a given point: the midpoint of two distinct nearest points
would be strictly closer, by `norm_midpoint_lt_iff`.

Formalized by `MathlibExt.Analysis.Normed.Module.BestApproximation.eq_of_isBestApproximation_of_strictConvexSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/BestApproximation.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/BestApproximation.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/best-approximation-in-normed-spaces/index.html#eq-of-is-best-approximation-of-strict-co).

## Unique best approximation in finite-dimensional subspaces

Existence plus uniqueness: a finite-dimensional subspace of a strictly
convex real normed space admits a unique best approximation to every
point.

Formalized by `MathlibExt.Analysis.Normed.Module.BestApproximation.exists_unique_bestApproximation_of_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/Normed/Module/BestApproximation.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/BestApproximation.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/best-approximation-in-normed-spaces/index.html#exists-unique-best-approximation-of-fini).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Best approximation in normed spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/best-approximation-in-normed-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/approximation-theory/best-approximation-in-normed-spaces)
