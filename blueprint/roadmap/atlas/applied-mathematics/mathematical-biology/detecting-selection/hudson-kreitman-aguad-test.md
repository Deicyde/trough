---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.hkaPolyMean, MathlibExt.Biology.PopulationGenetics.Coalescent.hkaPolyVar, MathlibExt.Biology.PopulationGenetics.Coalescent.hkaDivMean, MathlibExt.Biology.PopulationGenetics.Coalescent.hkaDivVar, MathlibExt.Biology.PopulationGenetics.Coalescent.integral_hkaDivergence, MathlibExt.Biology.PopulationGenetics.Coalescent.variance_hkaDivergence, MathlibExt.Biology.PopulationGenetics.Coalescent.hkaStatistic, MathlibExt.Biology.PopulationGenetics.Coalescent.hkaPolyVar_pos
statement: formalized
proof: formalized
---

# Hudson–Kreitman–Aguadé test

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html).

## HKA expected number of segregating sites

HKA's expected number of segregating sites `θ C(n)` in a sample of `n` genes with scaled
mutation rate `θ` (use `f θ` for species `B`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaPolyMean`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-poly-mean).

## HKA variance of the number of segregating sites

HKA's variance of the number of segregating sites, `θ C(n) + θ² C₂(n)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaPolyVar`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-poly-var).

## HKA expected divergence

HKA's expected divergence `θ (T + (1 + f) / 2)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaDivMean`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-div-mean).

## HKA variance of the divergence

HKA's variance of the divergence, `θ (T + (1 + f) / 2) + (θ (1 + f) / 2)²`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaDivVar`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-div-var).

## Expected divergence

**Expected divergence** (Hudson, Kreitman & Aguadé 1987): if the ancestral coalescence time
`τ` is exponential with rate `2 / (1 + f)` and, given the genealogy σ-algebra `m`, the
divergence `D` has conditional mean `θ (T + τ)`, then `E D = θ (T + (1 + f) / 2)`
(for `f > -1`). No integrability hypothesis on `D` is needed: if `D` were not integrable its
conditional expectation would be `0` (Mathlib's convention), and the hypothesis would force
`θ = 0`, where the identity reads `0 = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.integral_hkaDivergence`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#integral-hka-divergence).

## Variance of the divergence

**Variance of the divergence** (Hudson, Kreitman & Aguadé 1987): under the hypotheses of
`integral_hkaDivergence`, if moreover `D` is square integrable with conditional variance
`θ (T + τ)` given `m` (as for a Poisson count), then
`Var D = θ (T + (1 + f) / 2) + (θ (1 + f) / 2)²`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.variance_hkaDivergence`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#variance-hka-divergence).

## Hudson–Kreitman–Aguadé statistic

The **HKA statistic** for `L` loci with polymorphism counts `SA i`, `SB i`, divergences
`D i`, parameters `θ i`, `T`, `f` and sample sizes `nA`, `nB`: the sum over loci of the
squared standardized deviations of the three counts from their HKA expectations.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaStatistic`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-statistic).

## Positivity of the HKA polymorphism variance

HKA's variances are positive in the biological domain: `θ > 0`, `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaPolyVar_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-poly-var-pos).

## Positivity of the HKA divergence variance

HKA's divergence variance is positive for `θ > 0`, `T ≥ 0`, `f > -1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaDivVar_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-div-var-pos).

## The HKA statistic has mean `3 L` at the true parameters

If every count is square
integrable with the HKA mean and variance (as derived above under the neutral model), with
`θ i > 0`, `T ≥ 0`, `f > 0` and `nA, nB ≥ 2`, then `E X² = 3 L`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.integral_hkaStatistic`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#integral-hka-statistic).

## HKA's estimating equations

**HKA's estimating equations** (Hudson, Kreitman & Aguadé 1987) for parameters
`θ i`, `T`, `f` given the counts: the totals over loci of polymorphism in `A`, in `B` and of
divergence match their expectations, and at each locus the total of the three counts matches
its expectation. (Only `L - 1` of the per-locus equations are independent of the totals.)

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaEquations`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-equations).

## True parameters solve the HKA estimating equations

The true parameters solve HKA's estimating equations at the expected counts.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.hkaEquations_expected`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/HKA.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html#hka-equations-expected).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hudson–Kreitman–Aguadé test](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/detecting-selection/hudson-kreitman-aguad-test)
