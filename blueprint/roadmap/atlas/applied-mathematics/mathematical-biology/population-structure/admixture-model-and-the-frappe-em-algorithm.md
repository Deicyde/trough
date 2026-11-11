---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.Params, Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.qf, Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.joint, Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.joint_pos, Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.marginal_eq, Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.qf_pos, Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.qf_lt_one, Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.isRef
statement: formalized
proof: formalized
---

# Admixture model and the FRAPPE EM algorithm

40 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html).

## The model

## Parameters of the admixture model

Parameters `θ = (Q, F)` of the admixture model: positive ancestry proportions `Q i k` summing
to one over `k`, and reference-allele frequencies `F k j` strictly between `0` and `1`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.Params`, a structure declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#params).

## Reference-allele probability in the admixture model

The reference-allele probability `qf θ i j = ∑ k, Q i k * F k j` of a copy of SNP `j` in
individual `i`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.qf`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#qf).

## Joint weight of an allele copy and its ancestral population

The joint weight of an allele copy `(i, j, a)` and its ancestral population `k`:
`Q i k * (if a then F k j else 1 - F k j)`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.joint`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#joint).

## Positivity of the admixture joint weight

The joint weight is positive (the standing hypothesis of the generic EM).

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.joint_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#joint-pos).

## The marginal of an allele copy

Reference with probability `qf θ i j`, alternative with
probability `1 - qf θ i j`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.marginal_eq`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#marginal-eq).

## Positivity of the reference-allele probability

The reference-allele probability is positive.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.qf_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#qf-pos).

## Reference-allele probability is less than one

The reference-allele probability is below one.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.qf_lt_one`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#qf-lt-one).

## Reference-allele indicator for a genotype copy

Whether copy `c` of the genotype `g i j` (with `g i j` reference copies) carries the
reference allele: copies `c < g i j` do.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.isRef`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#is-ref).

## Observation of one allele copy of a genotype

The observation `(i, j, a)` of copy `c` of genotype `g i j`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.copyAllele`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#copy-allele).

## Polymorphic genotype data

Every SNP is polymorphic in the sample: some individual carries a reference allele and some
individual carries an alternative allele. Without it the M-step frequency is `0` or `1`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.Polymorphic`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#polymorphic).

## Allele-copy observations of a genotype matrix

The `2 |I| |J|` allele-copy observations of the genotype matrix `g`, indexed by `Fin`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.data`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#data).

## Sum over allele-copy data as a triple sum

A sum over the indexed data is a sum over individuals, SNPs and copies.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.sum_data`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#sum-data).

## Admixture log-likelihood

The admixture log-likelihood
`ℓ(Q, F) = ∑ i, ∑ j, (g i j * log (qf θ i j) + (2 - g i j) * log (1 - qf θ i j))`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.admixtureLogLik`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#admixture-log-lik).

## The EM log-likelihood of the allele copies is the admixture log-likelihood

**The EM log-likelihood of the allele copies is the admixture log-likelihood.**

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.logLik_eq_admixtureLogLik`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#log-lik-eq-admixture-log-lik).

## The EM theorem for the admixture model

A step that does not decrease `Q(· | θ)` does
not decrease the admixture log-likelihood.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.admixtureLogLik_le_of_emQ_le`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#admixture-log-lik-le-of-em-q-le).

## The admixture log-likelihood is monotone along the iterates

**The admixture log-likelihood is monotone along the iterates** of any M-step `M` with
`Q(M θ | θ) ≥ Q(θ | θ)`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.admixtureLogLik_iterate_monotone`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#admixture-log-lik-iterate-monotone).

## Ancestry responsibility of an allele copy (E-step)

The responsibility `r = P(z = k | copy c of (i, j))` (the E-step).

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.resp`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#resp).

## Positivity of the admixture responsibilities

The responsibilities are positive.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.resp_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#resp-pos).

## Admixture responsibilities sum to one

The responsibilities of a copy sum to one over the populations.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.sum_resp`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#sum-resp).

## Expected ancestry count of an individual

The expected number of allele copies of individual `i` from population `k`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.ancCount`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#anc-count).

## FRAPPE update of the ancestry proportions

The FRAPPE update of the ancestry proportions,
`Q' i k = (∑ j, ∑ c, r) / (2 J)`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.mStepQ`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#m-step-q).

## Expected ancestry counts sum to the number of allele copies

The expected ancestry counts of an individual sum to its `2 J` allele copies.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.sum_ancCount`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#sum-anc-count).

## Positivity of the expected ancestry counts

The expected ancestry counts are positive when there is at least one SNP.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.ancCount_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#anc-count-pos).

## Positivity of the updated ancestry proportions

The updated ancestry proportions are positive.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.mStep_Q_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#m-step-q-pos).

## Updated ancestry proportions sum to one

The updated ancestry proportions of each individual sum to one.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.mStep_Q_sum`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#m-step-q-sum).

## Expected population count of a SNP

The expected number of allele copies of SNP `j` from population `k`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.popCount`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#pop-count).

## Expected reference-allele count of a SNP per population

The expected number of reference copies of SNP `j` from population `k`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.refCount`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#ref-count).

## Expected alternative-allele count of a SNP per population

The expected number of alternative copies of SNP `j` from population `k`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.altCount`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#alt-count).

## FRAPPE update of the allele frequencies

The FRAPPE update of the allele frequencies,
`F' k j = (∑ i, ∑ c reference, r) / (∑ i, ∑ c, r)`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.mStepF`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#m-step-f).

## Reference and alternative counts add to the population count

Reference plus alternative expected counts give the population's expected count.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.refCount_add_altCount`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#ref-count-add-alt-count).

## Positivity of expected reference counts on polymorphic data

On polymorphic data the expected reference counts are positive.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.refCount_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#ref-count-pos).

## Positivity of expected alternative counts on polymorphic data

On polymorphic data the expected alternative counts are positive.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.altCount_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#alt-count-pos).

## Positivity of expected population counts on polymorphic data

On polymorphic data the expected population counts are positive.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.popCount_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#pop-count-pos).

## Positivity of the updated allele frequencies

On polymorphic data the updated allele frequencies are positive.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.mStep_F_pos`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#m-step-f-pos).

## Updated allele frequencies are less than one

On polymorphic data the updated allele frequencies are below one.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.mStep_F_lt_one`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#m-step-f-lt-one).

## The FRAPPE EM step

**The FRAPPE EM step** `θ ↦ (Q', F')`, with `Q' = mStepQ` and `F' = mStepF`; it
lies in the strictly positive parameter set when `J` is nonempty and every SNP is
polymorphic.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.emStep`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#em-step).

## Decomposition of the admixture EM objective

`Q(θ' | θ)` splits into an ancestry term per individual and a two-point term per population
and SNP.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.emQ_eq`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#em-q-eq).

## The FRAPPE update maximizes `Q(· | θ)`

No parameter `θ'` in the strictly
positive parameter set has a larger `Q(θ' | θ)` than the closed-form update `emStep g hg θ`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.emQ_le_emStep`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#em-q-le-em-step).

## Each FRAPPE EM step does not decrease the admixture log-likelihood

**Each FRAPPE EM step does not decrease the admixture log-likelihood.**

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.admixtureLogLik_le_emStep`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#admixture-log-lik-le-em-step).

## The admixture log-likelihood is monotone along the FRAPPE EM iterates

**The admixture log-likelihood is monotone along the FRAPPE EM iterates.**

Formalized by `Cslib.Bioinformatics.PopulationStructure.AdmixtureEM.admixtureLogLik_iterate_emStep_monotone`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/AdmixtureEM.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html#admixture-log-lik-iterate-em-step-monoto).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Admixture model and the FRAPPE EM algorithm](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-structure/admixture-model-and-the-frappe-em-algorithm)
