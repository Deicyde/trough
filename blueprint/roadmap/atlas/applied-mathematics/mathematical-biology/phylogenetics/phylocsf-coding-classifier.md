---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.PhyloCSF.leafData, Cslib.Bioinformatics.Phylogenetics.PhyloCSF.siteLik, Cslib.Bioinformatics.Phylogenetics.PhyloCSF.alignLik, Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score, Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score_decibans, Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score_decibans_eq, Cslib.Bioinformatics.Phylogenetics.PhyloCSF.siteLik_eq_sum_prune, Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score_eq_log_div
statement: formalized
proof: formalized
---

# PhyloCSF coding classifier

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html).

## Leaf data of an alignment column

The leaf data of an alignment column `col : L → S`: the indicator of the observed codon at
each leaf.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.leafData`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#leaf-data).

## Likelihood of one alignment column

The likelihood of one alignment column under the model `(t, π)`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.siteLik`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#site-lik).

## Likelihood of an alignment of independent columns

The likelihood of an alignment of `m` independent columns: the product of the site
likelihoods.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.alignLik`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#align-lik).

## The PhyloCSF score

**The PhyloCSF score** (natural-log scale): the sum over the columns of the
log-likelihood ratio of the coding model `(tC, πC)` against the non-coding model
`(tN, πN)`. The published PhyloCSF score is reported in decibans; see `score_decibans`
for the conversion. Thresholds for this `score` are in natural-log units.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#score).

## The published PhyloCSF score in decibans

`10 * log₁₀(L_C / L_N)`, i.e.
`(10 / log 10) * score`, since `log₁₀ x = log x / log 10`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score_decibans`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#score-decibans).

## Deciban score as a rescaled natural-log score

Decibans are the natural-log score rescaled by `10 / log 10`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score_decibans_eq`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#score-decibans-eq).

## Site likelihood by Felsenstein's pruning algorithm

Each site likelihood is computed by Felsenstein's pruning algorithm.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.siteLik_eq_sum_prune`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#site-lik-eq-sum-prune).

## The score is the log-likelihood ratio of the alignment

**The score is the log-likelihood ratio of the alignment** when all site likelihoods are
positive.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.score_eq_log_div`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#score-eq-log-div).

## Score threshold test for calling an alignment coding

The threshold test on the score: call the alignment coding (`1`) iff the score exceeds the
cutoff `c`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.scoreTest`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#score-test).

## PhyloCSF's score threshold test is most powerful for unnormalized weights

With
positive site likelihoods under both models, a randomized test `φ` whose weighted size under
the non-coding weights is at most that of `scoreTest c` has at most its weighted power under
the coding weights. This is the dominated Neyman–Pearson inequality for the unnormalized
alignment weights `alignLik`; it becomes a statement about statistical size and power only
under additional normalization hypotheses (`∑ A, alignLik = 1` for each model).

Formalized by `Cslib.Bioinformatics.Phylogenetics.PhyloCSF.weighted_power_le_scoreTest`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Phylogenetics/PhyloCSF.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html#weighted-power-le-score-test).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: PhyloCSF coding classifier](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/phylocsf-coding-classifier/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/phylogenetics/phylocsf-coding-classifier)
