---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_diploidSelect_pos, MathlibExt.Biology.PopulationGenetics.Selection.two_mul_relEntropy_le_log_diploidMeanFitness_diploidSelect, MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_le_diploidMeanFitness_diploidSelect, MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_diploidSelect_eq_iff, MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_lt_diploidMeanFitness_diploidSelect, MathlibExt.Biology.PopulationGenetics.Selection.hasDerivAt_diploidMeanFitness_two, MathlibExt.Biology.PopulationGenetics.Selection.diploidSelect_two_sub
statement: formalized
proof: formalized
---

# Baum–Eagon inequality for diploid selection

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html).

## Mean fitness stays positive under diploid selection

Mean fitness stays positive after one generation of diploid viability selection (for
nonnegative frequencies and fitnesses; normalization is not needed).

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_diploidSelect_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html#diploid-mean-fitness-diploid-select-pos).

## Diploid Baum–Eagon mean-fitness inequality, sharp form

With
nonnegative allele frequencies and genotype fitnesses and positive mean fitness, one generation
of selection raises the log mean fitness by at least twice the relative entropy
`∑ i, p'_i log (p'_i / p_i)` of the new allele frequencies `p'` from the old ones `p`
(Baum–Eagon's argument for the quadratic form `w̄`). Alleles absent before selection stay absent
(`p_i = 0 → p'_i = 0`), so the summands with `p_i = 0` vanish. The inequality does not need
`∑ p = 1`; on the simplex its right side is nonnegative (Gibbs' inequality). This is a
mean-fitness monotonicity inequality, not Fisher's fundamental theorem: Fisher's theorem
concerns the change attributable to selection expressed through additive genetic variance.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.two_mul_relEntropy_le_log_diploidMeanFitness_diploidSelect`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html#two-mul-rel-entropy-le-log-diploid-mean).

## Mean fitness never decreases

**Mean fitness never decreases** under diploid multi-allele viability selection with random
mating (Mulholland–Smith 1959; Scheuer–Mandel 1959; Kingman 1961).

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_le_diploidMeanFitness_diploidSelect`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html#diploid-mean-fitness-le-diploid-mean-fit).

## Mean fitness is unchanged exactly at selection equilibria

Mean fitness is unchanged by one generation of selection exactly when the allele
frequencies are at an equilibrium of the selection map.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_diploidSelect_eq_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html#diploid-mean-fitness-diploid-select-eq-i).

## Diploid selection strictly increases mean fitness off equilibria

Away from equilibria, mean fitness strictly increases under diploid viability selection.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidMeanFitness_lt_diploidMeanFitness_diploidSelect`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html#diploid-mean-fitness-lt-diploid-mean-fit).

## Derivative of two-allele mean fitness

For two alleles with frequencies `(x, 1 - x)`, the mean fitness
`w̄(x) = x² w₀₀ + x (1 - x) (w₀₁ + w₁₀) + (1 - x)² w₁₁` has derivative `2 (m₀ - m₁)`, twice the
difference of the marginal fitnesses. This holds for every real `x`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.hasDerivAt_diploidMeanFitness_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html#has-deriv-at-diploid-mean-fitness-two).

## Wright's formula

**Wright's formula** (Wright 1937): for two alleles with frequencies `(x, 1 - x)`, one
generation of viability selection changes the frequency of allele `0` by
`Δx = x (1 - x) (dw̄/dx) / (2 w̄)`. The identity is algebraic and holds for every real `x` with
`w̄(x) ≠ 0`; the model domain is `x ∈ [0, 1]` with nonnegative fitnesses.

Formalized by `MathlibExt.Biology.PopulationGenetics.Selection.diploidSelect_two_sub`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/DiploidSelection.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html#diploid-select-two-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Baum–Eagon inequality for diploid selection](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/baum-eagon-inequality-for-diploid-selection)
