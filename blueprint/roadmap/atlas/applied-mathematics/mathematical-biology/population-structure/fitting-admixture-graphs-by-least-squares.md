---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS1, MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS2, MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS1_basis_change, MathlibExt.Biology.PopulationGenetics.QpGraph.exists_scoreS2_basis_change_ne, MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS2_eq_scoreS1_diagonal, MathlibExt.Biology.PopulationGenetics.QpGraph.designMatrix, MathlibExt.Biology.PopulationGenetics.QpGraph.f4_eq_designMatrix_mulVec, MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS1_le_of_normal_eq
statement: formalized
proof: formalized
---

# Fitting admixture graphs by least squares

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html).

## Generalized least-squares qpGraph score S1

The qpGraph score `S1(g) = -½ (g - f)ᵀ Q⁻¹ (g - f)` (Patterson et al. 2012, eq. 6) of
predicted statistics `g` against estimated statistics `f` with error covariance `Q`.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS1`, a definition declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#score-s1).

## Least-squares qpGraph score S2

The least-squares qpGraph score `S2(g) = -∑ᵢ (gᵢ - fᵢ)² / (Qᵢᵢ + λ)` (Patterson et al.
2012, eq. 7). A term with `Qᵢᵢ + λ = 0` is `0` by the convention `x / 0 = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS2`, a definition declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#score-s2).

## Basis independence of the qpGraph score S1

`S1` is basis independent: under an invertible change of basis `A` of the statistics, with
the covariance transformed to `A Q Aᵀ`, the score is unchanged. (The identity holds for every
`Q`; for singular `Q` both sides are `0` by Mathlib's convention `Q⁻¹ = 0`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS1_basis_change`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#score-s1-basis-change).

## The qpGraph score S2 depends on the basis

`S2` is not basis independent (Patterson et al. 2012, after eq. 7): there are a positive
definite covariance `Q`, an invertible change of basis `A` and statistics `f`, `g` such that,
for every `λ`, the score changes.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.exists_scoreS2_basis_change_ne`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#exists-score-s2-basis-change-ne).

## Score S2 as score S1 with a diagonal covariance

`S2` is twice `S1` with the covariance replaced by the diagonal matrix of the
`Qᵢᵢ + λ`, when these are nonzero.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS2_eq_scoreS1_diagonal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#score-s2-eq-score-s1-diagonal).

## qpGraph design matrix of basis f4 statistics

The qpGraph design matrix of basis statistics `f4 (A i) (B i) (C i) (D i)` for lineage
weights `w`: entry `(i, e)` is `(w Aᵢ e - w Bᵢ e) * (w Cᵢ e - w Dᵢ e)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.designMatrix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#design-matrix).

## Predicted f4 statistics are linear in the edge lengths

In the drift model, with the admixture weights fixed, the predicted statistics are linear in
the edge lengths: `g = B ℓ` for the design matrix `B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.f4_eq_designMatrix_mulVec`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#f4-eq-design-matrix-mul-vec).

## Solutions of the normal equations maximize the score S1

GLS maximizes `S1`: for positive definite `Q`, a solution `ℓ̂` of the normal equations
`Bᵀ Q⁻¹ B ℓ̂ = Bᵀ Q⁻¹ f` maximizes `ℓ ↦ S1(B ℓ)` over all `ℓ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.scoreS1_le_of_normal_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#score-s1-le-of-normal-eq).

## Uniqueness of the generalized least-squares maximizer

Uniqueness of the GLS maximizer: for positive definite `Q` and a design matrix of full
column rank (`B.mulVec` injective), a vector `ℓ` with the same score as a solution `ℓ̂` of the
normal equations equals `ℓ̂`.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.eq_of_scoreS1_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#eq-of-score-s1-eq).

## Invertibility of the generalized least-squares Gram matrix

For positive definite `Q` and a design matrix of full column rank, the GLS Gram matrix
`Bᵀ Q⁻¹ B` is invertible.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.isUnit_det_gram`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#is-unit-det-gram).

## Closed-form generalized least-squares estimate of edge lengths

The closed-form GLS estimate `ℓ̂ = (Bᵀ Q⁻¹ B)⁻¹ Bᵀ Q⁻¹ f` solves the normal equations when the
Gram matrix is invertible.

Formalized by `MathlibExt.Biology.PopulationGenetics.QpGraph.normal_eq_gls`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/QpGraph.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/QpGraph.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html#normal-eq-gls).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fitting admixture graphs by least squares](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-structure/fitting-admixture-graphs-by-least-squares)
