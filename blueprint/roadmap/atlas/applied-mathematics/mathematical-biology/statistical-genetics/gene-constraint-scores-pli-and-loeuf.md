---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.GeneConstraint.poissonLik, MathlibExt.Biology.StatisticalGenetics.GeneConstraint.poissonLik_pos, MathlibExt.Biology.StatisticalGenetics.GeneConstraint.flatPosterior_density, MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper, MathlibExt.Biology.StatisticalGenetics.GeneConstraint.loeuf, MathlibExt.Biology.StatisticalGenetics.GeneConstraint.gammaMeasure_real_Iic_oeUpper, MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper_coverage, MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper_zero
statement: formalized
proof: formalized
---

# Gene constraint scores (pLI and LOEUF)

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html).

## Poisson likelihood of an observed count

The Poisson likelihood `e^{-μ} μ^o / (o!)` of an observed count `o` at mean `μ`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.poissonLik`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#poisson-lik).

## Positivity of the Poisson likelihood

The likelihood is positive at a positive mean.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.poissonLik_pos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#poisson-lik-pos).

## Flat-prior posterior of `γ`

The likelihood `γ ↦ P(o | Poisson(γ E))` times `E` is the
Gamma density of shape `o + 1` and rate `E`. For `E > 0` that density integrates to one, so `E`
is the normalizing constant of the flat-prior posterior (the identity itself is algebraic and
holds for every real `E`).

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.flatPosterior_density`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#flat-posterior-density).

## Upper confidence bound for the observed/expected ratio

The upper confidence bound for the observed/expected ratio at level `α`:
`u_α(o) / E`, with `u_α` Garwood's bound for the Poisson mean.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#oe-upper).

## LOEUF

The upper end of the 90% interval, `oeUpper (1/20)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.loeuf`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#loeuf).

## The flat-prior posterior quantile is Garwood's bound

The Gamma(`o + 1`, `E`) posterior
puts mass exactly `1 - α` below `oeUpper α E o`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.gammaMeasure_real_Iic_oeUpper`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#gamma-measure-real-iic-oe-upper).

## Exact coverage

For every true ratio `γ ≥ 0` and `E > 0`, when `o ~ Poisson(γ E)`,
`P(γ ≤ oeUpper α E o) ≥ 1 - α`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper_coverage`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#oe-upper-coverage).

## Observed/expected upper bound with no observed variants

With no observed variants the bound is `log (1 / α) / E`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper_zero`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#oe-upper-zero).

## LOEUF of a gene with no observed LoF variants

**LOEUF of a gene with no observed LoF variants** is `log 20 / E`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.loeuf_zero`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#loeuf-zero).

## Observed/expected upper bound increases with the observed count

The bound is strictly increasing in the observed count.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper_strictMono`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#oe-upper-strict-mono).

## Observed/expected upper bound decreases with the expected count

The bound is strictly decreasing in the expected count `E > 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.oeUpper_strictAntiOn`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#oe-upper-strict-anti-on).

## Posterior class probability in the Poisson mixture

The posterior probability of class `c` for a gene with `o` observed and `E` expected LoF
variants, in the Poisson mixture with prior weights `w` and class rates `rate`:
`w_c P(o | rate_c E) / ∑_{c'} w_{c'} P(o | rate_{c'} E)`. pLI is this at the class with the smallest
rate.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.classPosterior`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#class-posterior).

## Class posteriors sum to one

The class posteriors sum to one.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.sum_classPosterior`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#sum-class-posterior).

## Recursion for the Poisson likelihood

The likelihood recursion `P(o + 1 | μ) = P(o | μ) μ / (o + 1)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.poissonLik_succ`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#poisson-lik-succ).

## pLI is antitone in the observed count

The posterior of a class `c₀` whose rate is the
smallest is antitone in `o`, for every prior.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.classPosterior_antitone`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#class-posterior-antitone).

## Class posterior is strictly antitone in the observed count

Strictly antitone when some class has a strictly larger rate.

Formalized by `MathlibExt.Biology.StatisticalGenetics.GeneConstraint.classPosterior_strictAnti`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/StatisticalGenetics/GeneConstraint.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#class-posterior-strict-anti).

## Strictly positive class weights summing to one

Strictly positive class weights summing to one.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.PosWeights`, a definition declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#pos-weights).

## Loss-of-function count data for a gene

A gene's data: observed LoF count `o` and positive expected count `E`.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.GeneData`, a structure declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#gene-data).

## Joint likelihood of gene data and constraint class

The joint likelihood of a gene's data and class `z`: `w_z P(o | rate_z E)`.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.joint`, a definition declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#joint).

## Positivity of the Poisson mixture joint likelihood

The joint likelihood is positive for positive rates.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.joint_pos`, a theorem declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#joint-pos).

## Expected number of genes in a constraint class

The expected number of genes in class `z` under the posteriors at weights `w`:
`∑_n P_w(z | o_n)`.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.mass`, a definition declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#mass).

## Positivity of the class masses

The class masses are positive when there is at least one gene.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.mass_pos`, a theorem declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#mass-pos).

## Class masses sum to the number of genes

The class masses add up to the number of genes.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.sum_mass`, a theorem declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#sum-mass).

## EM update of the Poisson mixture class weights

The EM update `w'_z = (1/N) ∑_n P_w(z | o_n)`, for `N > 0` genes and positive rates.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.emStep`, a definition declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#em-step).

## The M-step maximizes `Q(· | w)`

**The M-step maximizes `Q(· | w)`** over admissible weights.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.emQ_le_emStep`, a theorem declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#em-q-le-em-step).

## EM does not decrease the likelihood

**EM does not decrease the likelihood** of the class weights.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.logLik_le_logLik_emStep`, a theorem declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#log-lik-le-log-lik-em-step).

## Monotonicity of the log-likelihood along the class-weight EM iterates

The log-likelihood is monotone along the EM iterates.

Formalized by `Cslib.Bioinformatics.StatisticalGenetics.PoissonClassEM.logLik_iterate_emStep_monotone`, a theorem declared in [CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/StatisticalGenetics/PoissonClassEM.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html#log-lik-iterate-em-step-monotone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gene constraint scores (pLI and LOEUF)](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/statistical-genetics/gene-constraint-scores-pli-and-loeuf)
