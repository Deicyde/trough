---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Linkage.alleleFreqFst, MathlibExt.Biology.PopulationGenetics.Linkage.alleleFreqSnd, MathlibExt.Biology.PopulationGenetics.Linkage.linkageDiseq, MathlibExt.Biology.PopulationGenetics.Linkage.recombine, MathlibExt.Biology.PopulationGenetics.Linkage.recombine_eq_sub, MathlibExt.Biology.PopulationGenetics.Linkage.sum_recombine, MathlibExt.Biology.PopulationGenetics.Linkage.recombine_nonneg, MathlibExt.Biology.PopulationGenetics.Linkage.alleleFreqFst_recombine
statement: formalized
proof: formalized
---

# Linkage disequilibrium and Haldane's map function

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html).

## Two-locus random mating

## Allele frequency at the first locus

The frequency `∑ b, x (a, b)` of allele `a` at the first locus.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.alleleFreqFst`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#allele-freq-fst).

## Allele frequency at the second locus

The frequency `∑ a, x (a, b)` of allele `b` at the second locus.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.alleleFreqSnd`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#allele-freq-snd).

## Linkage disequilibrium of a two-locus gamete law

The linkage disequilibrium `D = x_AB x_ab - x_Ab x_aB`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.linkageDiseq`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#linkage-diseq).

## Random mating with recombination

One generation of random mating with recombination fraction `r`:
`recombine r x g = (1 - r) x_g + r p_{g.1} q_{g.2}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.recombine`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#recombine).

## Classical form of the recombination recursion

The classical form of the recursion: coupling gametes (`AB`, `ab`) lose `r D` and repulsion
gametes (`Ab`, `aB`) gain `r D`. This identity holds for every real `r`; the biological domain
is `0 ≤ r ≤ 1/2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.recombine_eq_sub`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#recombine-eq-sub).

## Recombination preserves total gamete frequency

Recombination keeps gamete frequencies summing to `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.sum_recombine`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#sum-recombine).

## Recombination preserves nonnegativity of gamete frequencies

Recombination keeps gamete frequencies nonnegative for `0 ≤ r ≤ 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.recombine_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#recombine-nonneg).

## Recombination preserves first-locus allele frequencies

Allele frequencies at the first locus are unchanged by random mating (for every real
`r`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.alleleFreqFst_recombine`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#allele-freq-fst-recombine).

## Recombination preserves second-locus allele frequencies

Allele frequencies at the second locus are unchanged by random mating (for every real
`r`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.alleleFreqSnd_recombine`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#allele-freq-snd-recombine).

## Linkage disequilibrium decays by the factor $1 - r$

Linkage disequilibrium decays by the factor `1 - r` per generation: `D' = (1 - r) D`
(for every real `r`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.linkageDiseq_recombine`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#linkage-diseq-recombine).

## Linkage disequilibrium after $t$ generations

After `t` generations, `D_t = (1 - r)^t D_0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.linkageDiseq_iterate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#linkage-diseq-iterate).

## Linkage disequilibrium tends to zero

Linkage disequilibrium tends to `0` whenever `0 < r ≤ 1`; this contains the biological
range `0 < r ≤ 1/2`. For `r = 0` (complete linkage) `D` is constant.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.tendsto_linkageDiseq_iterate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#tendsto-linkage-diseq-iterate).

## Haldane's map function

Haldane's map function `r(d) = (1 - e^{-2d}) / 2`: the recombination fraction between two
loci at map distance `d` Morgans when crossovers form a Poisson process (no interference).

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.haldane`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#haldane).

## Series for the probability of an odd Poisson count

The probability that a Poisson count of mean `d` is odd, as a series:
`∑_{k odd} e^{-d} d^k / k! = (1 - e^{-2d}) / 2` (Haldane 1919). The series identity holds for
every real `d`; it is a probability for `0 ≤ d`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.hasSum_poisson_odd`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#has-sum-poisson-odd).

## Haldane's map function from Poisson crossovers

Haldane's map function (Haldane 1919): if the number of crossovers in an interval of map
length `d` Morgans is Poisson with mean `d`, the probability of an odd number of crossovers,
i.e. of recombination between the ends of the interval, is `(1 - e^{-2d}) / 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.poissonMeasure_real_odd`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#poisson-measure-real-odd).

## Nonnegativity of Haldane's map function

Haldane's map function is nonnegative at nonnegative distances.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.haldane_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#haldane-nonneg).

## Haldane's recombination fraction is below one half

The recombination fraction is always below `1/2` (for every real `d`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.haldane_lt_half`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#haldane-lt-half).

## Distant loci are unlinked in the limit

Loci far apart are unlinked in the limit: `r → 1/2` as `d → ∞`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.tendsto_haldane_atTop`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#tendsto-haldane-at-top).

## Inverse Haldane map function recovers map distance

The inverse map function `d = -½ log(1 - 2r)` recovers the map distance.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.neg_half_log_haldane`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#neg-half-log-haldane).

## Every recombination fraction below one half is attained

Every `r < 1/2` is the recombination fraction at the distance `-½ log(1 - 2r)`. The
hypothesis keeps `log` on positive arguments: at `r = 1/2` the right side would use the junk
value `log 0 = 0`. The distance is nonnegative exactly when `0 ≤ r`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Linkage.haldane_neg_half_log`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Linkage.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Linkage.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html#haldane-neg-half-log).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linkage disequilibrium and Haldane's map function](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/linkage-disequilibrium-and-haldane-s-map-functio)
