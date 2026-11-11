---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaA1, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaA2, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaB1, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaB2, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaE1, MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaE2
statement: formalized
proof: formalized
---

# Segregating sites and pairwise differences

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html).

## Tajima's constant $a_1$

`a₁ = ∑_{i=1}^{n-1} 1/i` (Tajima 1989).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaA1`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-a1).

## Tajima's constant $a_2$

`a₂ = ∑_{i=1}^{n-1} 1/i²` (Tajima 1989).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaA2`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-a2).

## Tajima's constant $b_1$

`b₁ = (n + 1) / (3 (n - 1))` (Tajima 1989), for `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaB1`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-b1).

## Tajima's constant $b_2$

`b₂ = 2 (n² + n + 3) / (9 n (n - 1))` (Tajima 1989), for `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaB2`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-b2).

## Tajima's constant $c_1$

`c₁ = b₁ - 1/a₁` (Tajima 1989), for `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC1`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-c1).

## Tajima's constant $c_2$

`c₂ = b₂ - (n + 2)/(a₁ n) + a₂/a₁²` (Tajima 1989), for `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaC2`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-c2).

## Tajima's constant $e_1$

`e₁ = c₁ / a₁` (Tajima 1989), for `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaE1`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-e1).

## Tajima's constant $e_2$

`e₂ = c₂ / (a₁² + a₂)` (Tajima 1989), for `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaE2`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-e2).

## Tajima's $a_1$ is a harmonic number

`a₁` is the harmonic number `H_{n-1}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.tajimaA1_eq_harmonic`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#tajima-a1-eq-harmonic).

## Variance of the total branch length

**Variance of the total branch length** (Watterson 1975):
`Var L = ∑_{k=2}^n k² Var T_k = 4 ∑_{j=1}^{n-1} 1/j²` (uses independence of the holding
times).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.variance_totalLength`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#variance-total-length).

## Variance of the number of segregating sites

**Variance of the number of segregating sites** (Watterson 1975;
Tajima 1989): if, given the genealogy σ-algebra `m`, the number `S` of
segregating sites has conditional mean and conditional variance `(θ/2) L` (as for a Poisson
count with mean `θ L / 2`), then `Var S = θ a₁ + θ² a₂`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.variance_segSites`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#variance-seg-sites).

## Pairs of genes in a sample

The pairs of genes in a sample of size `n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.samplePairs`, an abbreviation declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#sample-pairs).

## Mean number of pairwise differences

The mean number of pairwise differences `π = C(n, 2)⁻¹ ∑_{i<j} D_{ij}` (Tajima 1983), where
`D s` is the number of sites at which the two sequences of the pair `s` differ.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.meanPairDiff`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#mean-pair-diff).

## Expected pairwise differences

**Expected pairwise differences** (Tajima 1983): if, for each pair `s` of sampled genes,
the coalescence time `τ s` of the pair is exponential with rate `1` and the number `D s` of
differences has conditional mean `θ τ s` given the genealogy σ-algebra `m` (mutations at rate
`θ / 2` on each of the two branches of length `τ s`), then `E π = θ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.integral_meanPairDiff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#integral-mean-pair-diff).

## Tajima's numerator has mean zero

**Tajima's numerator has mean zero** (Tajima 1989): under the hypotheses of
`integral_meanPairDiff` and Watterson's (`E[S | m] = (θ/2) L`),
`E[π - S / a₁] = 0` for a sample of size `n ≥ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_tajimaNumerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#integral-tajima-numerator).

## Unbiased estimator of Tajima's variance term

**Unbiased estimator of Tajima's variance term** (Tajima 1989): with `S` as in
`variance_segSites`, `E[e₁ S + e₂ S (S - 1)] = c₁ θ + c₂ θ²` for `n ≥ 2`. (By Tajima's
analysis `c₁ θ + c₂ θ²` is `Var(π - S / a₁)`.)

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_tajimaVarEstimator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Tajima.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#integral-tajima-var-estimator).

## Counting sample pairs by overlap with a given pair

Among the pairs of a sample of size `n`, one equals a given pair `s`, `2 (n - 2)` share
exactly one gene with it and `C(n - 2, 2)` are disjoint from it.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.sum_samplePairs_card_inter`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#sum-sample-pairs-card-inter).

## Variance of the mean number of pairwise differences

**Variance of the mean number of pairwise differences** (Tajima 1983):
`Var π = b₁ θ + b₂ θ²` for a sample of size `n ≥ 2`, under the conditional-moment model of the
module docstring: `τ s ~ Exp(1)`, `E[τ s τ t] = 4/3` (one shared gene), `11/9` (disjoint
pairs); the shared path lengths `ℓ`; `E[D s | m] = θ τ s` and
`E[D s D t | m] = θ² τ s τ t + (θ / 2) ℓ s t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.variance_meanPairDiff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#variance-mean-pair-diff).

## Probability that a pair lies in separate lineages

The probability `(k - 1) (n + 1) / ((n - 1) (k + 1))` that a given pair of a sample of
size `n` is still in two distinct lineages while the genealogy has `k` lineages
(`2 ≤ k ≤ n`, `n ≥ 2`; at `n = 1` the definition divides by zero and returns `0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.pairSeparateProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#pair-separate-prob).

## Mean coalescence time of a pair is one

`∑_{k=2}^n p_k / C(k, 2) = 1`: the mean coalescence time of a pair is `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.sum_pairSeparateProb_div_choose`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#sum-pair-separate-prob-div-choose).

## Sum of pair-separation probabilities over squared pair counts

`∑_{k=2}^n k p_k / C(k, 2)² = (n + 2) / n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.sum_mul_pairSeparateProb_div_choose_sq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#sum-mul-pair-separate-prob-div-choose-sq).

## Covariance of `π` and `S`

`Cov(π, S) = θ + (n + 2) θ² / (2 n)` for `n ≥ 2`, if
`τ s ~ Exp(1)`, `E[τ s L] = 2 a₁ + (n + 2) / n` (`L` the total branch length),
`E[D s | m] = θ τ s`, `E[S | m] = (θ / 2) L` and `E[D s S | m] = (θ² / 2) τ s L + θ τ s` (the
path of each pair lies in the tree). This is the covariance behind Tajima's (1989) `c₁, c₂`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.covariance_meanPairDiff_segSites`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#covariance-mean-pair-diff-seg-sites).

## Tajima's variance identity

**Tajima's variance identity** (Tajima 1989): `Var(π - S / a₁) = c₁ θ + c₂ θ²` for a
sample of size `n ≥ 2`, under the hypotheses of `variance_meanPairDiff`,
`covariance_meanPairDiff_segSites` and `variance_segSites`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.variance_tajimaNumerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#variance-tajima-numerator).

## Pair coalescence time against the total branch length

If the coalescence time of a
pair is `τ = ∑_{k=2}^n χ k T k`, where `χ k` indicates that the pair is still in two distinct
lineages while there are `k` lineages, and the topology is independent of the holding times in
the sense `E[χ k T k T k'] = p k E[T k T k']` with `p k = pairSeparateProb n k`, then
`E[τ L] = 2 a₁ + (n + 2) / n` for `n ≥ 2`. Only this factorization is used, so `χ k` need not
be an indicator in the statement.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanTimes.integral_pairTime_mul_totalLength`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/TajimaVariance.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html#integral-pair-time-mul-total-length).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Segregating sites and pairwise differences](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/segregating-sites-and-pairwise-differences)
