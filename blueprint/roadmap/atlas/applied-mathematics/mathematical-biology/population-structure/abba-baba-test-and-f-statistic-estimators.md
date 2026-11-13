---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.configProb, MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect, MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.abba, MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.baba, MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.abbaPol, MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.babaPol, MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sum_configProb, MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect_prod
statement: formalized
proof: formalized
---

# ABBA–BABA test and f-statistic estimators

39 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html).

## Site patterns

## Probability of a derived-allele configuration

Probability of the derived/ancestral configuration `x` when haplotype `i` is sampled
independently and carries the derived allele with probability `q i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.configProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#config-prob).

## Expectation under independent haplotype sampling

Expectation of a function `g` of the configuration under independent sampling of one
haplotype per population at derived-allele frequencies `q`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sample-expect).

## Unpolarized ABBA site-pattern indicator

Unpolarized `ABBA` indicator for populations `(P1, P2, P3, O)`: `P1` agrees with `O`, `P2`
with `P3`, and `P1` differs from `P2` (the patterns `ABBA` and `BAAB`).

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.abba`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#abba).

## Unpolarized BABA site-pattern indicator

Unpolarized `BABA` indicator for populations `(P1, P2, P3, O)`: `P1` agrees with `P3`, `P2`
with `O`, and `P1` differs from `P2` (the patterns `BABA` and `ABAB`).

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.baba`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#baba).

## Polarized ABBA site-pattern indicator

Polarized `ABBA` indicator (Durand et al. 2011): `P1` and `O` ancestral, `P2` and `P3`
derived.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.abbaPol`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#abba-pol).

## Polarized BABA site-pattern indicator

Polarized `BABA` indicator (Durand et al. 2011): `P1` and `P3` derived, `P2` and `O`
ancestral.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.babaPol`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#baba-pol).

## Configuration probabilities sum to one

The configuration probabilities sum to `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sum_configProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sum-config-prob).

## Sampling expectation of a product factorizes

`sampleExpect` of a product of functions of single coordinates factorizes:
`E[∏ i, g i (x i)] = ∏ i, (g i true * q i + g i false * (1 - q i))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect_prod`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sample-expect-prod).

## Additivity of the sampling expectation

`sampleExpect` is additive in the function.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect_add`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sample-expect-add).

## Sampling expectation commutes with subtraction

`sampleExpect` commutes with subtraction of functions.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect_sub`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sample-expect-sub).

## Sampling expectation is an expectation of independent indicators

`sampleExpect` is the expectation under independent sampling: if the derived-allele
indicators `X i` are independent random variables with `P(X i = true) = q i`, then
`E[g (X 0, …, X (n - 1))] = sampleExpect g q`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_eq_sampleExpect`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-eq-sample-expect).

## ABBA–BABA site-pattern identity

The site-pattern identity: `1[BABA] - 1[ABBA] = (x₁ - x₂) (x₃ - x₄)` for every
configuration of derived-allele indicators.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.baba_sub_abba`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#baba-sub-abba).

## ABBA–BABA identity

**ABBA–BABA identity** (Patterson et al. 2012; Durand et al. 2011): under independent
sampling of one haplotype per population at derived-allele frequencies `q` (any reals;
frequencies in `[0, 1]` in the biological model), `E[BABA - ABBA] = (q₁ - q₂) (q₃ - q₄)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect_baba_sub_abba`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sample-expect-baba-sub-abba).

## Expected polarized ABBA–BABA difference

Polarized form (Durand et al. 2011, with `q 3` the derived-allele frequency in the
outgroup): `E[BABA_pol - ABBA_pol] = (q₁ - q₂) q₃ (1 - q₄)`. When the outgroup is fixed for the
ancestral allele (`q 3 = 0`) this is `(q₁ - q₂) (q₃ - q₄)`, as in the unpolarized identity.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sampleExpect_babaPol_sub_abbaPol`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sample-expect-baba-pol-sub-abba-pol).

## ABBA–BABA equals `f4`

When the frequencies `p X ω` are themselves random (drift, and
the choice of locus) and one haplotype is sampled from each population independently given the
frequencies, the expected `BABA - ABBA` difference is `f4 P1 P2 P3 O`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_sampleExpect_baba_sub_abba`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-sample-expect-baba-sub-abba).

## Linearity of the f4-statistic in its first pair

Linearity of `f4` in its first pair: if `p A - p B = ∑ l, c l * (p (C l) - p (D l))`
pointwise, then `f4 A B Y Z = ∑ l, c l * f4 (C l) (D l) Y Z`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.f4_eq_sum_of_sub_eq_sum`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#f4-eq-sum-of-sub-eq-sum).

## qpAdm model equation

**qpAdm model equation** (Haak et al. 2015, Supplementary Information): if the target `T`
is an admixture of sources `S k` with weights `w k` summing to `1` (`p T = ∑ k, w k * p (S k)`
pointwise; the weights may be negative, as in fitted qpAdm models), then for all `X`, `Y`, `Z`,
`f4 T X Y Z = ∑ k, w k * f4 (S k) X Y Z`. The merged `DriftModel.f4_admixture_right` is a
two-source drift-model instance (mixture in the second pair, one source as fourth argument).

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.f4_affine_combination`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#f4-affine-combination).

## qpWave matrix of f4-statistics

The qpWave matrix of left populations `L 0, …, L n` and right populations
`R 0, …, R r`: entry `(i, j)` is `f4 (L (i + 1)) (L 0) (R (j + 1)) (R 0)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.f4Matrix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#f4-matrix).

## qpWave rank bound

**qpWave rank bound** (Reich et al. 2012, Supplementary Information; Patterson et al.
2012): if the frequency of every left population `L i` is an affine combination
`∑ l, a i l * p (S l)` (`∑ l, a i l = 1`, coefficients of any sign) of the frequencies of
`k + 1` source populations, then the matrix `f4 (L i) (L 0) (R j) (R 0)` (`i, j ≥ 1`) has rank
at most `k`; with `k` sources, at most `k - 1`. The right populations are arbitrary. The
converse (rank `k` forces `k + 1` streams) and the statistical rank test are not covered.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.rank_f4Matrix_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#rank-f4-matrix-le).

## Unbiased heterozygosity estimator

Unbiased estimator of `p (1 - p)` from `x` derived copies among `m` sampled copies:
`x (m - x) / (m (m - 1))` (meaningful for `m ≥ 2`).

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.hetHat`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#het-hat).

## Unbiased f2 estimator

The unbiased `f2` estimator of Patterson et al. (2012), Appendix:
`(â - b̂)² - â (1 - â) / (m_A - 1) - b̂ (1 - b̂) / (m_B - 1)` with `â = x_A / m_A`,
written as `(x_A / m_A - x_B / m_B)² - x_A (m_A - x_A) / (m_A² (m_A - 1)) - …`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.f2Hat`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#f2-hat).

## Unbiased f3 estimator

The unbiased `f3` estimator of Patterson et al. (2012), Appendix:
`(ĉ - â) (ĉ - b̂) - ĉ (1 - ĉ) / (m_C - 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.f3Hat`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#f3-hat).

## f4 estimator

The `f4` estimator `(â - b̂) (ĉ - d̂)`; it needs no correction for four distinct
populations.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.f4Hat`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#f4-hat).

## Estimator of Hudson's F_ST denominator

Hudson's `F_ST` denominator estimator `â (1 - b̂) + b̂ (1 - â)` (Bhatia et al. 2013); the
numerator estimator is `f2Hat`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.hudsonDenHat`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#hudson-den-hat).

## Hudson's F_ST denominator at one site

Hudson's `F_ST` denominator at one site: `p_A (1 - p_B) + p_B (1 - p_A)`, the probability
that two copies, one from each population, differ. The numerator is `(p_A - p_B) ^ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.hudsonDen`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#hudson-den).

## Hudson's F_ST (ratio of averages)

Hudson's `F_ST` over sites `s` in the ratio-of-averages form of Bhatia et al. (2013):
`∑ s, (p_A s - p_B s) ^ 2 / ∑ s, hudsonDen (p_A s) (p_B s)`. It is defined when the denominator
is positive (it vanishes only if every site is fixed for the same allele in both populations);
otherwise Lean's value `0` is a junk value.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.hudsonFst`, a definition declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#hudson-fst).

## Hudson's numerator is at most the denominator

At each site Hudson's numerator is at most the denominator for frequencies in `[0, 1]`: the
difference is `p_A (1 - p_A) + p_B (1 - p_B) ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.sq_sub_le_hudsonDen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#sq-sub-le-hudson-den).

## Hudson's F_ST lies between 0 and 1

Hudson's `F_ST` lies in `[0, 1]` for frequencies in `[0, 1]`. (When the denominator vanishes
the junk value `0` also lies in `[0, 1]`, so no positivity hypothesis is needed.)

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.hudsonFst_mem_Icc`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#hudson-fst-mem-icc).

## Sample allele frequency is unbiased

The sample frequency is unbiased: for `X ~ Bin(m, p)` with `m ≥ 1`, `E[X / m] = p`. (For
`m = 0`, `X / 0 = 0` is a junk value, hence `m ≥ 1`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_div_of_hasLaw_binomial`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-div-of-has-law-binomial).

## Unbiased heterozygosity

For `X ~ Bin(m, p)` with `m ≥ 2`,
`E[X (m - X) / (m (m - 1))] = p (1 - p)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_hetHat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-het-hat).

## Unbiased `f2`

**Unbiased `f2`** (Patterson et al. 2012, Appendix): with independent binomial samples
`X_A ~ Bin(m_A, p_A)`, `X_B ~ Bin(m_B, p_B)`, `m_A, m_B ≥ 2`,
`E[f2Hat] = (p_A - p_B) ^ 2`, the population `f2` at the site.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_f2Hat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-f2-hat).

## Unbiased `f3`

**Unbiased `f3`** (Patterson et al. 2012, Appendix): with pairwise independent binomial
samples, `m_C ≥ 2` and `m_A, m_B ≥ 1`, `E[f3Hat] = (p_C - p_A) (p_C - p_B)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_f3Hat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-f3-hat).

## Unbiased `f4`

For four populations sampled independently across the two pairs
(`m ≥ 1` each), `E[f4Hat] = (p_A - p_B) (p_C - p_D)`; no correction is needed.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_f4Hat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-f4-hat).

## Hudson's denominator is unbiased

**Hudson's denominator is unbiased** (Bhatia et al. 2013): with independent binomial samples
(`m ≥ 1` each), `E[hudsonDenHat] = hudsonDen p_A p_B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_hudsonDenHat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-hudson-den-hat).

## Unbiasedness of the summed f2 estimator

Summed over sites, Hudson's numerator estimator `∑ s, f2Hat` is unbiased for
`∑ s, (p_A s - p_B s) ^ 2` (independence is needed only within each site).

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_sum_f2Hat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 570](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L570). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-sum-f2-hat).

## Unbiasedness of the summed Hudson denominator estimator

Summed over sites, Hudson's denominator estimator is unbiased for
`∑ s, hudsonDen (p_A s) (p_B s)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_sum_hudsonDenHat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-sum-hudson-den-hat).

## Hudson's `F_ST`, ratio of averages

**Hudson's `F_ST`, ratio of averages** (Bhatia et al. 2013): the ratio of the expected
summed numerator and denominator estimators is the population `hudsonFst`. This is a statement
about the ratio of expectations; the expectation of the ratio of the estimated sums is in
general not `hudsonFst`.

Formalized by `MathlibExt.Biology.PopulationGenetics.ADMIXTOOLS.integral_sum_div_integral_sum`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-sum-div-integral-sum).

## The unpolarized D-statistic numerator vanishes on a tree

In the drift model, if no edge
lies on both the `P1–P2` and the `P3–O` path (as on the tree `((P1, P2), P3), O`), then the
expected unpolarized `ABBA` and `BABA` counts are equal. Thus `BABA - ABBA` and its sign reversal
have expectation `0`. The integrability hypotheses make both expectations meaningful.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.integral_sampleExpect_abba_eq_baba`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 626](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L626). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#integral-sample-expect-abba-eq-baba).

## qpAdm model equation in the drift model

If the lineage weights of `T` are an affine
combination `∑ k, w k • weight (S k)` of those of the sources (`∑ k, w k = 1`, weights of any
sign), then `f4 T X Y Z = ∑ k, w k * f4 (S k) X Y Z`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f4_affine_combination`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean, line 643](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/ADMIXTOOLS.lean#L643). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html#f4-affine-combination-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: ABBA–BABA test and f-statistic estimators](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-structure/abba-baba-test-and-f-statistic-estimators)
