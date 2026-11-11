---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Selection.meanFitness, MathlibExt.Biology.PopulationGenetics.Selection.fitnessVariance, MathlibExt.Biology.PopulationGenetics.Selection.select, MathlibExt.Biology.PopulationGenetics.Selection.meanFitness_select_sub, MathlibExt.Biology.PopulationGenetics.Selection.meanFitness_pos, MathlibExt.Biology.PopulationGenetics.Selection.meanFitness_le_meanFitness_select, MathlibExt.Biology.PopulationGenetics.Selection.select_nonneg, MathlibExt.Biology.PopulationGenetics.Selection.sum_select
statement: formalized
proof: formalized
---

# Natural selection, Fisher's theorem and the Price equation

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html).

## Haploid selection

## Mean fitness of a population

The mean fitness `w̄ = ∑ i, p i * w i` of a population with type frequencies `p` and
fitnesses `w`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.meanFitness`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#mean-fitness).

## Variance of fitness

The variance of fitness `Var_p(w) = ∑ i, p i * (w i - w̄) ^ 2` under the type frequencies
`p`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.fitnessVariance`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#fitness-variance).

## One generation of haploid selection

One generation of haploid selection: `select p w i = p i * w i / w̄`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.select`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#select).

## Fisher's fundamental theorem of natural selection

Fisher's fundamental theorem of natural selection in its exact haploid, discrete-generation
form: the change in mean fitness over one generation of selection is the variance of fitness
divided by the mean fitness, `w̄(p') - w̄(p) = Var_p(w) / w̄(p)` (cf. Fisher 1930, who states the
theorem for the additive genetic variance). The identity needs only `∑ p = 1` and `w̄ ≠ 0`; the
model domain is the simplex with `w > 0` (`meanFitness_pos`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.meanFitness_select_sub`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#mean-fitness-select-sub).

## Positivity of mean fitness on the simplex

Mean fitness is positive on the simplex when every fitness is positive.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.meanFitness_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#mean-fitness-pos).

## Mean fitness never decreases under haploid selection

Mean fitness never decreases under haploid selection (corollary of Fisher's theorem).

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.meanFitness_le_meanFitness_select`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#mean-fitness-le-mean-fitness-select).

## Haploid selection preserves nonnegative frequencies

Haploid selection keeps frequencies nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.select_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#select-nonneg).

## Haploid selection preserves total frequency one

Haploid selection keeps the frequencies summing to `1` whenever `w̄ ≠ 0` (for `w̄ = 0`
the division by zero would give `0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.sum_select`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#sum-select).

## Marginal fitness of an allele

The marginal fitness `∑ j, (w i j + w j i) / 2 * p j` of allele `i`: the mean fitness of a
genotype carrying `i` whose other allele is drawn from the frequencies `p`, averaging the two
positions at which `i` can sit in the ordered genotype.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.marginalFitness`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#marginal-fitness).

## Marginal fitness for symmetric genotype fitnesses

For symmetric genotype fitnesses the marginal fitness is the row marginal
`∑ j, w i j * p j`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.marginalFitness_of_symm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#marginal-fitness-of-symm).

## Diploid mean fitness under Hardy–Weinberg proportions

The mean fitness `w̄ = ∑ i, ∑ j, p i * p j * w i j` of a population in Hardy–Weinberg
proportions with allele frequencies `p` and genotype fitnesses `w`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#diploid-mean-fitness).

## One generation of diploid viability selection

One generation of diploid viability selection under random mating, followed by Mendelian
transmission of either allele of each survivor:
`diploidSelect p w i = p i * (∑ j, (w i j + w j i) / 2 * p j) / w̄`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidSelect`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#diploid-select).

## Positivity of diploid mean fitness

Diploid mean fitness is positive on the simplex when every genotype fitness is positive.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#diploid-mean-fitness-pos).

## Diploid selection preserves nonnegative allele frequencies

Diploid viability selection keeps allele frequencies nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidSelect_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#diploid-select-nonneg).

## Diploid selection preserves total allele frequency one

Diploid viability selection keeps allele frequencies summing to `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.sum_diploidSelect`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#sum-diploid-select).

## Price equation

The Price equation (exact, finite population). Individual `i` has fitness `w i` (number of
offspring), trait value `z i`, and mean offspring trait value `z' i`. With population means
`w̄ = 𝔼 i, w i`, `z̄ = 𝔼 i, z i` and offspring mean trait `z̄' = ∑ i, w i * z' i / ∑ i, w i`,
`w̄ (z̄' - z̄) = Cov(w, z) + E[w (z' - z)]`, where `Cov` is the population covariance
(Price 1970). Nonnegativity of `w` is not needed; only a nonzero total offspring number.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.price`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Selection.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Selection.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html#price).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Natural selection, Fisher's theorem and the Price equation](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/natural-selection-fisher-s-theorem-and-the-price)
