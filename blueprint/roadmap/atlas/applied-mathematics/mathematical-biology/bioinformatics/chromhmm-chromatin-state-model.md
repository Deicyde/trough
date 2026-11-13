---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Regulatory.ChromHMM.onesCount, Cslib.Bioinformatics.Regulatory.ChromHMM.zerosCount, Cslib.Bioinformatics.Regulatory.ChromHMM.factoredUpdate, Cslib.Bioinformatics.Regulatory.ChromHMM.sum_bernPMF, Cslib.Bioinformatics.Regulatory.ChromHMM.sum_mul_log_bernPMF, Cslib.Bioinformatics.Regulatory.ChromHMM.sum_mul_log_bernPMF_le_factoredUpdate, Cslib.Bioinformatics.Regulatory.ChromHMM.factoredUpdate_pos, Cslib.Bioinformatics.Regulatory.ChromHMM.factoredUpdate_lt_one
statement: formalized
proof: formalized
---

# ChromHMM chromatin-state model

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html).

## The factored emission update

## Weight of binary vectors with a mark present

The weight `∑ o with o j = true, c o` of the binary vectors with mark `j` present.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.onesCount`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#ones-count).

## Weight of binary vectors with a mark absent

The weight `∑ o with o j = false, c o` of the binary vectors with mark `j` absent.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.zerosCount`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#zeros-count).

## Factored per-mark update

The factored (per-mark) update `ones j / (ones j + zeros j)`.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.factoredUpdate`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#factored-update).

## Product of Bernoulli distributions sums to one

A product of Bernoulli distributions sums to one over the binary vectors, for every
parameter vector `p` (the identity is algebraic: `∏ j, (p j + (1 - p j)) = 1`).

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.sum_bernPMF`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#sum-bern-pmf).

## Expected product-Bernoulli log-likelihood splits over marks

The expected log-likelihood of weighted binary vectors under a product of Bernoulli
distributions with parameters in `(0, 1)` splits over the marks.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.sum_mul_log_bernPMF`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#sum-mul-log-bern-pmf).

## The factored update maximizes the expected log-likelihood

**The factored update maximizes the expected log-likelihood** over all products of
Bernoulli distributions with parameters in `(0, 1)`, for nonnegative weights `c` in which every
mark is both present and absent with positive weight.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.sum_mul_log_bernPMF_le_factoredUpdate`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#sum-mul-log-bern-pmf-le-factored-update).

## Positivity of the factored update

The factored update is positive when both counts are.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.factoredUpdate_pos`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#factored-update-pos).

## Factored update is below one

The factored update is below one when both counts are positive.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.factoredUpdate_lt_one`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#factored-update-lt-one).

## ChromHMM parameters

ChromHMM parameters: initial and transition weights, and the presence probability of each
mark in each state.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.Params`, a structure declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#params).

## HMM of ChromHMM parameters

The HMM of ChromHMM parameters: emissions are products of Bernoulli distributions.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.Params.toHMM`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#to-hmm).

## Valid ChromHMM parameters

Valid parameters: positive initial and transition distributions, mark probabilities in
`(0, 1)`.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.Params.Valid`, a structure declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#valid).

## Parameter space of ChromHMM

The parameter space of ChromHMM.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.ValidParams`, an abbreviation declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#valid-params).

## Valid ChromHMM parameters give a valid HMM

A valid ChromHMM parameter is a valid HMM.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.Params.Valid.toHMM`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#to-hmm-2).

## Valid HMM built from a valid ChromHMM parameter

The valid HMM of a valid ChromHMM parameter.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.toValidHMM`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#to-valid-hmm).

## ChromHMM joint weight of a state path and mark vectors

The EM model of ChromHMM: the joint weight of a state path and a sequence of mark vectors.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.joint`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#joint).

## Expected number of bins in a state with a mark present

The expected number of bins in state `s` with mark `j` present.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.markOnes`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#mark-ones).

## Expected number of bins in a state with a mark absent

The expected number of bins in state `s` with mark `j` absent.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.markZeros`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#mark-zeros).

## The ChromHMM M-step

The Baum-Welch initial and transition updates, and the factored
emission update `prob s j = markOnes / (markOnes + markZeros)`.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.mStep`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#m-step).

## The factored update in posterior form

`markOnes s j` is the posterior expected number
of bins in state `s` at which mark `j` is present.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.markOnes_eq`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#mark-ones-eq).

## Rich data for the ChromHMM M-step

Data on which the ChromHMM M-step is valid: a sequence, a transition, and every mark both
present and absent somewhere.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.Rich`, a structure declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#rich).

## The ChromHMM update is a valid parameter

**The ChromHMM update is a valid parameter** on rich data.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.mStep_valid`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#m-step-valid).

## One ChromHMM step on rich data

One ChromHMM step, on rich data.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.emStep`, a definition declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#em-step).

## Positivity of the ChromHMM joint weight

The ChromHMM joint weight is positive.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.joint_pos`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#joint-pos).

## The ChromHMM update maximizes `Q(· | θ)`

**The ChromHMM update maximizes `Q(· | θ)`** over all valid product-Bernoulli HMMs.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.emQ_le_emStep`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#em-q-le-em-step).

## Each ChromHMM step does not decrease the log-likelihood

**Each ChromHMM step does not decrease the log-likelihood.**

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.logLik_le_emStep`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#log-lik-le-em-step).

## The log-likelihood is monotone along the ChromHMM iterates

**The log-likelihood is monotone along the ChromHMM iterates.**

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.logLik_iterate_emStep_monotone`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#log-lik-iterate-em-step-monotone).

## EM log-likelihood as a sum of HMM log-likelihoods

The EM log-likelihood is the sum of the HMM log-likelihoods of the sequences.

Formalized by `Cslib.Bioinformatics.Regulatory.ChromHMM.logLik_eq`, a theorem declared in [CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Regulatory/ChromHMM.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html#log-lik-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: ChromHMM chromatin-state model](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/chromhmm-chromatin-state-model)
