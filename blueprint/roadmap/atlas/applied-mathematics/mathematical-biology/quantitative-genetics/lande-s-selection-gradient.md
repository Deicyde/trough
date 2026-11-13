---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.SelectionGradient.integral_sub_mul_gaussianReal, MathlibExt.Biology.StatisticalGenetics.SelectionGradient.meanFitness, MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferential, MathlibExt.Biology.StatisticalGenetics.SelectionGradient.hasDerivAt_meanFitness, MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferential_eq_mul_deriv_log, MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferential_div_eq, MathlibExt.Biology.StatisticalGenetics.SelectionGradient.meanFitnessMV, MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferentialMV
statement: formalized
proof: formalized
---

# Lande's selection gradient

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html).

## Stein's lemma

**Stein's lemma** for the normal law `N(μ, v)`, `v > 0`: if `g` is differentiable with
derivative `g'` and `g`, `(z - μ) g z` and `g'` are integrable, then
`𝔼[(z - μ) g z] = v 𝔼[g' z]` (Stein 1981, Lemma 1).

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.integral_sub_mul_gaussianReal`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#integral-sub-mul-gaussian-real).

## Mean fitness of a normally distributed trait

The mean fitness `w̄(μ) = 𝔼[W z]` of a population whose trait is distributed as
`N(μ, v)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.meanFitness`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#mean-fitness).

## Directional selection differential

The directional selection differential `S = 𝔼[(z - μ) W z] / w̄`: the mean trait of the
selected parents, weighting each individual by its fitness, minus the mean trait `μ` before
selection. If `w̄ = 0` the division returns the junk value `0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferential`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#selection-differential).

## Derivative of mean fitness with respect to the trait mean

The derivative of mean fitness with respect to the trait mean is
`d/dμ w̄(μ) = 𝔼[(z - μ) W z] / v`, for bounded measurable fitness and `v > 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.hasDerivAt_meanFitness`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#has-deriv-at-mean-fitness).

## Lande's equation

**Lande's equation** for one normally distributed trait (Lande 1979): the selection
differential is the phenotypic variance times the derivative of log mean fitness with respect
to the trait mean, `S = v · d/dμ log w̄(μ)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferential_eq_mul_deriv_log`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#selection-differential-eq-mul-deriv-log).

## The Lande–Arnold selection gradient

**The Lande–Arnold selection gradient** for one normally distributed trait: for a
differentiable bounded fitness function with integrable derivative, `β = S / v = 𝔼[W' z] / w̄`,
the average slope of relative fitness `W / w̄` (Lande–Arnold 1983).

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferential_div_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradient.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#selection-differential-div-eq).

## Mean fitness of a multivariate normal trait

The mean fitness `w̄(μ) = 𝔼[W z]` of a population whose trait vector is distributed as
`N(μ, P)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.meanFitnessMV`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#mean-fitness-mv).

## Multivariate directional selection differential

The directional selection differential `S = 𝔼[W z · (z - μ)] / w̄` of a trait vector
distributed as `N(μ, P)`: the fitness-weighted mean trait vector of the selected parents minus
the mean `μ` before selection. If `w̄ = 0` it is the junk value `0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferentialMV`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#selection-differential-mv).

## Lande's gradient of mean fitness for multivariate traits

The gradient of mean fitness with respect to the vector of trait means is
`∇_μ w̄(μ) = P⁻¹ 𝔼[W z · (z - μ)]`, for positive definite `P` and bounded measurable `W`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.hasGradientAt_meanFitnessMV`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#has-gradient-at-mean-fitness-mv).

## Lande's equation

**Lande's equation** (Lande 1979): for a multivariate normal trait vector, the selection
differential is the phenotypic covariance matrix applied to the gradient of log mean fitness
with respect to the trait means, `S = P ∇_μ log w̄(μ)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.SelectionGradient.selectionDifferentialMV_eq`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/SelectionGradientMultivariate.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html#selection-differential-mv-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lande's selection gradient](https://deicyde.github.io/atlas-lean/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/quantitative-genetics/lande-s-selection-gradient)
