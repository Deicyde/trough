---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.linStep, MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.linStep_iterate, MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.linStep_eq_self_iff, MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.tendsto_linStep_iterate, MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.deNovoFraction, MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.deNovoFraction_eq, MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.kernel, MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFreq
statement: formalized
proof: formalized
---

# Mutation–selection balance

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html).

## The linear recursion

## Linear mutation–selection recursion

One generation of the linear model: `x ↦ (1 - s) x + U`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.linStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#lin-step).

## Closed-form orbit of the linear mutation–selection recursion

Closed-form orbit: `x_t = U / s + (1 - s)^t (x_0 - U / s)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.linStep_iterate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#lin-step-iterate).

## Unique fixed point $U/s$ of the linear recursion

`U / s` is the unique fixed point.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.linStep_eq_self_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#lin-step-eq-self-iff).

## Global attraction

For `0 < s < 2` every orbit converges to `U / s`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.tendsto_linStep_iterate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#tendsto-lin-step-iterate).

## Fraction of de novo loss-of-function alleles

The fraction of LoF alleles in the next generation that are new mutations, from
frequency `x`: `U / ((1 - s) x + U)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.deNovoFraction`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#de-novo-fraction).

## At equilibrium the de novo fraction is `s_het`

**At equilibrium the de novo fraction is `s_het`.**

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.deNovoFraction_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#de-novo-fraction-eq).

## Binomial transition kernel for loss-of-function counts

The transition probability from `i` LoF copies among `N` to `j` copies among `N'`: binomial
sampling of `N'` copies with success probability `(1 - s)(i / N) + U`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.kernel`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#kernel).

## Mean loss-of-function frequency of a distribution

The mean LoF frequency `∑ μ_i (i / N)` of a distribution `μ` on `Fin (N + 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFreq`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#mean-freq).

## One generation of the chain on distributions

One generation of the chain acting on distributions.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.pushStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#push-step).

## Rows of the transition kernel have total mass one

The kernel rows have total mass one (for every real sampling probability).

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.sum_kernel`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#sum-kernel).

## Transition kernel entries are probabilities

The kernel entries are probabilities when the sampling probability is in `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.kernel_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#kernel-nonneg).

## Binomial mean of the transition kernel

The binomial mean: `∑_j kernel(i, j) (j / N') = (1 - s)(i / N) + U` for `N' > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.sum_kernel_mul`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#sum-kernel-mul).

## Demography-free mean, one step

For any sizes `N`, `N' > 0` and any distribution `μ`
of total mass one, the mean frequency after one generation is `(1 - s) m + U`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFreq_pushStep`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#mean-freq-push-step).

## Pushing a distribution forward preserves total mass

Pushing a distribution forward preserves total mass.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.sum_pushStep`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#sum-push-step).

## Law of the loss-of-function count under any demography

The law of the LoF count in generation `t` for population sizes `N t` (any demography),
started from `μ₀`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.law`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#law).

## Demography-free mean

For every sequence of positive population sizes, `E[X_t]` follows
the deterministic linear recursion (derived from the binomial mean). The identity holds for all
real `s, U`; `law` is a probability law when `0 ≤ U ≤ s ≤ 1` and `μ₀` is one.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFreq_law`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#mean-freq-law).

## Expected loss-of-function frequency converges to $U/s$

The expected LoF frequency converges to `U / s` under any demography.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.tendsto_meanFreq_law`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#tendsto-mean-freq-law).

## Mean fitness under Hardy–Weinberg proportions

Mean fitness under Hardy–Weinberg with LoF frequency `q` and fitnesses `1, 1 - s, 1 - t`:
`1 - 2 q (1 - q) s - q² t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFitness`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#mean-fitness).

## Loss-of-function frequency after selection

LoF frequency after selection: `q (1 - s (1 - q) - t q) / w̄`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.selected`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#selected).

## One diploid generation of selection and mutation

One generation: selection, then mutation of wild-type alleles at rate `U`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.diploidStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#diploid-step).

## Mean fitness under multiplicative fitness

With multiplicative fitness, `w̄ = (1 - s q)²` for every `q`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFitness_mult`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#mean-fitness-mult).

## `U / s` is an equilibrium

**`U / s` is an equilibrium** of the multiplicative diploid model (an algebraic identity for
`s ≠ 0`, `U ≠ 1`; a frequency in `[0, 1]` when `0 ≤ U ≤ s`).

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.diploidStep_mult_fixed`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#diploid-step-mult-fixed).

## Mean fitness at the multiplicative mutation–selection equilibrium

At the multiplicative equilibrium the mean fitness is `(1 - U)²`, independent of `s`.
Requires `U ≠ 1`, so that `U / s` is genuinely a fixed point (`diploidStep_mult_fixed`):
for `U = 1` the point `U / s` is not an equilibrium.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFitness_mult_at_equilibrium`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#mean-fitness-mult-at-equilibrium).

## Haldane–Muller load

`1 - w̄ = 2U - U²` at the multiplicative equilibrium
(`U ≠ 1`, so `U / s` is a fixed point).

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.load_mult_at_equilibrium`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#load-mult-at-equilibrium).

## Positivity of mean fitness for allele frequencies below one

Mean fitness is positive for `0 ≤ q < 1` and `s, t ≤ 1` (nonnegative fitnesses).

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.meanFitness_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#mean-fitness-pos).

## Equilibria lie at or below `U / s`

**Equilibria lie at or below `U / s`** when homozygotes are at least multiplicatively unfit
(`2s - s² ≤ t`, which includes recessive lethality `t = 1`): every fixed point `q ∈ [0, 1)` of
the diploid map satisfies `q ≤ U / s`.

Formalized by `MathlibExt.Biology.PopulationGenetics.MutationSelectionBalance.le_div_of_diploidStep_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/MutationSelectionBalance.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html#le-div-of-diploid-step-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mutation–selection balance](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/mutation-selection-balance/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/mutation-selection-balance)
