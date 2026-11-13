---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.popMean, MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.centredCov, MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.f2_eq_centredCov, MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.centredCov_eq_doubleCenter_f2, MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.f2_eq_iff_centredCov_eq, MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.starWeight, MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.admixWeight, MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.starLen
statement: formalized
proof: formalized
---

# Centred population covariance and f-statistics

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html).

## Covariance

## Mean frequency across populations

The mean frequency `p̄ ω = (1 / n) ∑ X, p X ω` across the `n` populations.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.popMean`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#pop-mean).

## Centred leaf covariance

The centred leaf covariance `K X Y = 𝔼[(p X - p̄) * (p Y - p̄)]`: the second moments of the
frequencies centred across populations (not over `Ω`).

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.centredCov`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#centred-cov).

## f2 from the centred leaf covariance

`f2` from the centred leaf covariance: `f2 X Y = K X X + K Y Y - 2 K X Y`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.f2_eq_centredCov`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#f2-eq-centred-cov).

## Centred leaf covariance as the double centring of f2

The centred leaf covariance from `f2`: `K` is half the double centring of the `f2` matrix,
`K X Y = (f̄2 X· + f̄2 ·Y - f2 X Y - f̄2 ··) / 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.centredCov_eq_doubleCenter_f2`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#centred-cov-eq-double-center-f2).

## f-statistics determine exactly the centred leaf covariance

**f-statistics determine exactly the centred leaf covariance.** f-statistics see a model only through its centred leaf covariance: two square-integrable
frequency models have the same `f2` at every pair (hence the same `f3` and `f4`, by `f3_eq_f2`
and `f4_eq_f2`) if and only if they have the same centred leaf covariance.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.f2_eq_iff_centredCov_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#f2-eq-iff-centred-cov-eq).

## Lineage weights of the three-population star tree

Lineage weights of the star tree on three populations `0 = A`, `1 = B`, `2 = C`: edge `e`
is the leaf edge of population `e`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.starWeight`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#star-weight).

## Lineage weights of the three-population admixture model

Lineage weights of the admixture model: `A` and `B` sit on edges `0` and `1`, and `C` is an
`α : 1 - α` mixture of `A` and `B` followed by drift on its private edge `2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.admixWeight`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#admix-weight).

## Edge lengths of the star tree matching an admixture model

Edge lengths of the star tree matching the admixture model with edge lengths `a`, `b`, `c`:
`(1 - α)(a + b)`, `α (a + b)` and `c - α (1 - α)(a + b)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.starLen`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#star-len).

## Admixed population's weights in the admixture model

In the admixture model, `C` is the `α : 1 - α` mixture of `A` and `B` plus its private
edge.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.admixWeight_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#admix-weight-two).

## Star-tree model has binary loadings

The star-tree model has binary loadings.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.hasBinaryLoadings_star`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#has-binary-loadings-star).

## Admixture model lacks binary loadings

For `α ∉ {0, 1}` the admixture model does not have binary loadings.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.not_hasBinaryLoadings_admix`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#not-has-binary-loadings-admix).

## Star tree and admixture model have equal f2

The star tree and the admixture model have the same `f2` at every pair of populations.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.f2_star_eq_f2_admix`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#f2-star-eq-f2-admix).

## Star tree and admixture model have equal f4

The star tree and the admixture model have the same `f4` (hence the same `f3`) at every
quadruple of populations.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.f4_star_eq_f4_admix`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#f4-star-eq-f4-admix).

## Nonnegativity of the matching star-tree edge lengths

The matching star tree has nonnegative edge lengths when `0 ≤ α ≤ 1`, `a, b ≥ 0`, and the
private drift of `C` is at least `α (1 - α)(a + b)`, i.e. when `f3 C A B ≥ 0` in the admixture
model.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatisticsCovariance.starLen_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/FStatisticsCovariance.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html#star-len-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Centred population covariance and f-statistics](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-structure/centred-population-covariance-and-f-statistics)
