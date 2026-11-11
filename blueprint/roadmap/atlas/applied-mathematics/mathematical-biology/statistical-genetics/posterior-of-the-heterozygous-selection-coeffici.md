---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.ShetPosterior.balanceMean, MathlibExt.Biology.StatisticalGenetics.ShetPosterior.balanceMean_antitoneOn, MathlibExt.Biology.StatisticalGenetics.ShetPosterior.posteriorTail_antitone_of_antitoneOn, MathlibExt.Biology.StatisticalGenetics.ShetPosterior.posteriorTail_balance_antitone
statement: formalized
proof: formalized
---

# Posterior of the heterozygous selection coefficient

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/posterior-of-the-heterozygous-selection-coeffici/index.html).

## Mean PTV count at mutation-selection balance

Mean PTV allele count `n U / s` at deterministic mutation–selection balance, for `n`
sampled chromosomes, PTV mutation rate `U` and heterozygous selection coefficient `s > 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ShetPosterior.balanceMean`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/posterior-of-the-heterozygous-selection-coeffici/index.html#balance-mean).

## Balance mean is decreasing in the selection coefficient

The balance mean is antitone in `s > 0` for `n U ≥ 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ShetPosterior.balanceMean_antitoneOn`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/posterior-of-the-heterozygous-selection-coeffici/index.html#balance-mean-antitone-on).

## Posterior of `s_het` is stochastically nonincreasing in the PTV count, any antitone mean

**Posterior of `s_het` is stochastically nonincreasing in the PTV count, any antitone
mean**: for a prior `μ` on `s_het` concentrated on `(0, ∞)`, a Poisson count with mean `λ`
nonnegative and antitone on `(0, ∞)`, integrable likelihoods and positive marginal likelihoods,
`P(s_het > t ∣ k') ≤ P(s_het > t ∣ k)` whenever `k ≤ k'`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ShetPosterior.posteriorTail_antitone_of_antitoneOn`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/posterior-of-the-heterozygous-selection-coeffici/index.html#posterior-tail-antitone-of-antitone-on).

## Cassa et al. (2017) model

With the balance mean `n U / s_het` (`n, U > 0`) and any
probability prior on `s_het ∈ (0, ∞)`, the posterior probability `P(s_het > t ∣ k)` is
nonincreasing in the observed PTV count `k`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ShetPosterior.posteriorTail_balance_antitone`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ShetPosterior.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/posterior-of-the-heterozygous-selection-coeffici/index.html#posterior-tail-balance-antitone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Posterior of the heterozygous selection coefficient](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/posterior-of-the-heterozygous-selection-coeffici/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/posterior-of-the-heterozygous-selection-coeffici)
