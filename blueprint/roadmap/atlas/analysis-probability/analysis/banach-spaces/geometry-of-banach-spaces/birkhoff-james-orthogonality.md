---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.BirkhoffJamesOrthogonal, MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_zero_left, MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_zero_right, MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_self_iff, MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_smul_left_right, MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_of_exists_norming, MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.exists_norming_of_birkhoffJamesOrthogonal, MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_iff_exists_norming
statement: formalized
proof: formalized
---

# Birkhoff–James orthogonality

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html).

## Birkhoff–James orthogonality

## Birkhoff–James orthogonality

`x` is Birkhoff–James orthogonal to `y`
if `x` is a shortest vector on the affine line `x + 𝕜 • y`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.BirkhoffJamesOrthogonal`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal).

## Zero is Birkhoff–James orthogonal to every vector

`0` is Birkhoff–James orthogonal to every vector.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_zero_left`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-zero-left).

## Every vector is Birkhoff–James orthogonal to zero

Every vector is Birkhoff–James orthogonal to `0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_zero_right`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-zero-right).

## Only zero is Birkhoff–James orthogonal to itself

A vector is Birkhoff–James orthogonal to itself if and only if it is `0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_self_iff`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-self-iff).

## Homogeneity of Birkhoff–James orthogonality

Birkhoff–James orthogonality is homogeneous in both arguments.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_smul_left_right`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-smul-left-righ).

## Annihilating norming functional implies Birkhoff–James orthogonality

If a norming functional of `x` vanishes at `y`, then `x` is
Birkhoff–James orthogonal to `y`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_of_exists_norming`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-of-exists-norm).

## Birkhoff–James orthogonality gives an annihilating norming functional

The converse: if `x ≠ 0` is Birkhoff–James orthogonal to `y`, there is a
norming functional of `x` vanishing at `y`. Birkhoff–James orthogonality makes
the distance from `x` to `𝕜 ∙ y` equal to `‖x‖`, so the dual distance formula
supplies an annihilating norming functional.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.exists_norming_of_birkhoffJamesOrthogonal`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#exists-norming-of-birkhoff-james-orthogo).

## Norming-functional characterization of Birkhoff–James orthogonality

For `x ≠ 0`, Birkhoff–James orthogonality to `y` is equivalent to the
existence of a norming functional of `x` vanishing at `y`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_iff_exists_norming`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-iff-exists-nor).

## Duality mapping of a normed space

The **duality mapping** (duality set) at `x`: the functionals `f` with
`f x = ‖x‖ ^ 2` and `‖f‖ = ‖x‖`. At `x = 0` this is the singleton `{0}`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.dualityMapping`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#duality-mapping).

## Duality mapping is nonempty

The duality mapping is nonempty at every point: take a Hahn–Banach norming
functional and scale it by `‖x‖`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.dualityMapping_nonempty`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#duality-mapping-nonempty).

## Duality-mapping characterization of Birkhoff–James orthogonality

Birkhoff–James orthogonality to `y` is equivalent to the existence of a
functional in the duality mapping at `x` that vanishes at `y`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_iff_exists_dualityMapping`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-iff-exists-dua).

## Birkhoff–James orthogonality in inner product spaces

In an inner product space, Birkhoff–James orthogonality is ordinary
inner-product orthogonality.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BirkhoffJames.birkhoffJamesOrthogonal_iff_inner_eq_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BirkhoffJames.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html#birkhoff-james-orthogonal-iff-inner-eq-z).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Birkhoff–James orthogonality](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/birkhoff-james-orthogonality)
