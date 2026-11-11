---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState, MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState.sum_univ, MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState.coalescedA, MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState.coalescedB, MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusRate, MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.isRateMatrix_twoLocusRate, MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusDenom, MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusDenom_pos
statement: formalized
proof: formalized
---

# Two-locus coalescent

41 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html).

## States of the two-locus ancestral process

The states of the two-locus ancestral process of a sample of two sequences.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState`, an inductive type declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-state).

## Sum over the two-locus ancestral states

A sum over the six states.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState.sum_univ`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#sum-univ).

## Coalescence indicator at locus A

Whether locus `A` has found its most recent common ancestor.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState.coalescedA`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#coalesced-a).

## Coalescence indicator at locus B

Whether locus `B` has found its most recent common ancestor.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.TwoLocusState.coalescedB`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#coalesced-b).

## Rate matrix of the two-locus coalescent

The rate matrix of the two-locus ancestral process of a sample of two, with time in units of
`2 N` generations and `ρ = 4 N r`: coalescence at rate `1` for every pair of ancestral lineages,
recombination at rate `ρ / 2` for every lineage ancestral at both loci.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusRate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-rate).

## The two-locus coalescent rate matrix is a rate matrix

For `ρ ≥ 0`, `twoLocusRate ρ` is a rate matrix.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.isRateMatrix_twoLocusRate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#is-rate-matrix-two-locus-rate).

## Common denominator of the two-locus moments

The common denominator `ρ² + 13 ρ + 18` of the two-locus moments.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusDenom`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-denom).

## Positivity of the two-locus moment denominator

The denominator `ρ² + 13 ρ + 18` is positive for `ρ ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusDenom_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-denom-pos).

## Mean coalescence time at locus `A`

For `ρ ≥ 0`, the backward equations of `E_i T_A`
(`m i = 0` where `A` has coalesced, `(Q m) i = -1` elsewhere) force `m i = 1` in every state where
`A` has not coalesced: locus `A` alone is Kingman's coalescent of two genes.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.eq_one_of_meanTimeA`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#eq-one-of-mean-time-a).

## Mean coalescence time at locus `B`

**Mean coalescence time at locus `B`** (the mirror image of `eq_one_of_meanTimeA`).

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.eq_one_of_meanTimeB`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#eq-one-of-mean-time-b).

## Second moment of `T_A`

If `m` solves the mean equations of `eq_one_of_meanTimeA` and
`g` the second-moment equations (`g i = 0` where `A` has coalesced, `(Q g) i = -2 m i`
elsewhere), then `g i = 2` where `A` has not coalesced, so the variance read off from these
equations is `2 - 1² = 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.eq_two_of_secondMomentA`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#eq-two-of-second-moment-a).

## Covariance of coalescence times at two linked loci

The covariance `Cov(T_A, T_B) = (ρ + 18) / (ρ² + 13 ρ + 18)` of the coalescence times at two
loci of two sequences sampled linked (Hudson 1983; Kaplan & Hudson 1985).

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusCov`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-cov).

## Covariance of coalescence times

**Covariance of coalescence times** (Hudson 1983; Kaplan & Hudson 1985). Let `mA`, `mB`
solve the mean equations of the two loci and `f` the product-moment equations (`f i = 0` where
either locus has coalesced, `(Q f) i = -(mA i + mB i)` where neither has). Then `f - mA mB` is
`(ρ + 18) / (ρ² + 13ρ + 18)` from `linked`, `6 / (ρ² + 13ρ + 18)` from `partlySplit` and
`4 / (ρ² + 13ρ + 18)` from `split`. This is a statement about the backward equations; that their
solutions are the path-space moments of the chain is proved in `TwoLocusCoalescentPath`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.covariance_of_productMoment`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#covariance-of-product-moment).

## Solution of the two-locus product-moment equations

The explicit solution of the product-moment equations: `1 + Cov` in the three states where
neither locus has coalesced, `0` elsewhere.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.productMoment`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#product-moment).

## Mean coalescence time at locus A

The mean coalescence time at locus `A`: `1` before `A` coalesces, `0` after.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.meanTimeA`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#mean-time-a).

## Mean coalescence time at locus B

The mean coalescence time at locus `B`: `1` before `B` coalesces, `0` after.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.meanTimeB`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#mean-time-b).

## The explicit two-locus moments solve the moment equations

The systems of `covariance_of_productMoment` are solvable: `meanTimeA`, `meanTimeB` and
`productMoment ρ` satisfy them.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.productMoment_solution`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#product-moment-solution).

## Two-locus covariance under complete linkage

Complete linkage: `Cov(T_A, T_B) = 1 = Var T_A`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusCov_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-cov-zero).

## Positivity of the two-locus covariance

The covariance is positive for `ρ ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusCov_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-cov-pos).

## Two-locus covariance is at most one

The covariance is at most `Var T_A = 1` for `ρ ≥ 0` (outside this domain the formula can
exceed `1`; e.g. `twoLocusCov (-1) = 17 / 6`).

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusCov_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-cov-le-one).

## Two-locus covariance decreases with recombination rate

The covariance decreases with the recombination rate.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.antitoneOn_twoLocusCov`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#antitone-on-two-locus-cov).

## Two-locus covariance vanishes under free recombination

Free recombination: `Cov(T_A, T_B) → 0` as `ρ → ∞`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.tendsto_twoLocusCov_atTop`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#tendsto-two-locus-cov-at-top).

## Linkage disequilibrium polynomial

The linkage disequilibrium `D = x_AB x_ab - x_Ab x_aB` as a polynomial.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.diseqPoly`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#diseq-poly).

## Frequency of allele A as a polynomial

The frequency `p = x_AB + x_Ab` of allele `A` as a polynomial.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.freqFstPoly`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#freq-fst-poly).

## Frequency of allele B as a polynomial

The frequency `q = x_AB + x_aB` of allele `B` as a polynomial.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.freqSndPoly`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#freq-snd-poly).

## Weighted disequilibrium polynomial $D(1-2p)(1-2q)$

`D (1 - 2p)(1 - 2q)` as a polynomial.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.diseqZPoly`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#diseq-zpoly).

## Product of heterozygosities polynomial

`Π = p (1 - p) q (1 - q)` as a polynomial.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.hetProdPoly`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#het-prod-poly).

## Generator of the two-locus Wright–Fisher diffusion

The generator of the two-locus Wright–Fisher diffusion on polynomials in the gamete
frequencies, time in units of `2 N` generations, `ρ = 4 N r`, symmetric mutation at rate `ν` per
locus in each direction (`ν = θ / 2`, `θ = 4 N u`):
`L f = ½ ∑ x_g (δ_{gh} - x_h) ∂_g ∂_h f + ∑ (-(ρ/2) ε_g D + ν (x_{g'} + x_{g''} - 2 x_g)) ∂_g f`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusGenerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-generator).

## Drift of gamete frequencies matches recombination

Without mutation the drift of a gamete frequency is `2 N` times its per-generation change
under `Linkage.recombine` when `ρ = 4 N r`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusGenerator_X`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-generator-x).

## Hill–Robertson / Ohta–Kimura, first row

On the simplex,
`L D² = -(3 + ρ + 8ν) D² + D (1 - 2p)(1 - 2q) + p (1 - p) q (1 - q)` (for all real `ρ`, `ν`).

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusGenerator_diseqSq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-generator-diseq-sq).

## Hill–Robertson / Ohta–Kimura, second row

On the simplex,
`L (D z) = 4 D² - (5 + ρ/2 + 8ν) D z` with `z = (1 - 2p)(1 - 2q)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusGenerator_diseqZ`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-generator-diseq-z).

## Hill–Robertson / Ohta–Kimura, third row

On the simplex,
`L Π = D z - (2 + 8ν) Π + ν (p (1 - p) + q (1 - q))`; for `ν = 0` the three rows close.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.twoLocusGenerator_hetProd`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#two-locus-generator-het-prod).

## Stationary law of the two-locus diffusion

A **stationary law** of the two-locus diffusion in the weak (basic adjoint) sense: a
probability measure on the gamete-frequency simplex with `∫ L f dμ = 0` for every polynomial
`f`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.IsStationaryLaw`, a structure declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#is-stationary-law).

## Stationary standardized linkage disequilibrium $\sigma_d^2$

The stationary standardized disequilibrium
`σ_d² = (10 + ρ + 16ν) / (22 + 13ρ + ρ² + 128ν + 24ρν + 128ν²)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.sigmaDSq`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#sigma-dsq).

## Ohta–Kimura `σ_d²`

For a stationary law with `ρ, ν ≥ 0` and `E Π > 0`,
`E D² / E[p (1 - p) q (1 - q)] = sigmaDSq ρ ν`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.IsStationaryLaw.sigmaDSq_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#sigma-dsq-eq).

## Ohta–Kimura formula for $\sigma_d^2$ without mutation

The low-mutation value `σ_d² = (10 + ρ) / (22 + 13ρ + ρ²)` (Ohta & Kimura 1971).

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.sigmaDSq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#sigma-dsq-zero).

## Low-mutation limit of $\sigma_d^2$

`σ_d² → (10 + ρ) / (22 + 13ρ + ρ²)` as the mutation rate tends to `0`, for `ρ ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescent.tendsto_sigmaDSq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescent.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#tendsto-sigma-dsq-zero).

## Mean coalescence time at locus `A`, path form

For the two-locus ancestral process
started from two linked sequences, the hitting time `T_A` of the states where locus `A` has
coalesced has mean `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescentPath.lintegral_coalescenceTimeA`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#lintegral-coalescence-time-a).

## Mean coalescence time at locus `B`, path form

From two linked sequences, the hitting
time `T_B` of the states where locus `B` has coalesced has mean `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescentPath.lintegral_coalescenceTimeB`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#lintegral-coalescence-time-b).

## Product moment of the two coalescence times, path form

**Product moment of the two coalescence times, path form** (Hudson 1983; Kaplan & Hudson
1985): from two linked sequences, `E (T_A T_B) = 1 + (ρ + 18) / (ρ² + 13ρ + 18)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescentPath.lintegral_coalescenceTimeA_mul_coalescenceTimeB`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#lintegral-coalescence-time-a-mul-coalesc).

## Covariance of the coalescence times, path form

**Covariance of the coalescence times, path form** (Hudson 1983; Kaplan & Hudson 1985):
for the two-locus ancestral process started from two linked sequences,
`E (T_A T_B) - E T_A E T_B = (ρ + 18) / (ρ² + 13ρ + 18)`, with all three expectations finite
lower Lebesgue integrals of the hitting times.

Formalized by `MathlibExt.Biology.PopulationGenetics.TwoLocusCoalescentPath.covariance_coalescenceTimes`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TwoLocusCoalescentPath.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html#covariance-coalescence-times).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-locus coalescent](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/two-locus-coalescent/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/two-locus-coalescent)
