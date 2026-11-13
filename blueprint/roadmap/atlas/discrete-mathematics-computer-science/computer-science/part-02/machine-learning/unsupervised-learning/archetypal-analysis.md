---
declaration: section
origin: cited
lean: Cslib.MachineLearning.ArchetypalAnalysis.rss, Cslib.MachineLearning.ArchetypalAnalysis.Feasible, Cslib.MachineLearning.ArchetypalAnalysis.mean, Cslib.MachineLearning.ArchetypalAnalysis.rss_const_mean_le, Cslib.MachineLearning.ArchetypalAnalysis.exists_frontier_rss_le, Cslib.MachineLearning.ArchetypalAnalysis.exists_frontier_minimizer, Cslib.MachineLearning.ArchetypalAnalysis.rss_eq_zero_of_subset
statement: formalized
proof: formalized
---

# Archetypal analysis

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html).

## Residual sum of squares in archetypal analysis

The residual sum of squares of archetypes `z` for the data `x`: each data point is
replaced by the closest point of the convex hull of the archetypes. This is only meaningful
for `0 < p`: for `p = 0` the hull is empty and `infDist` to the empty set is `0` by
convention, so `rss` is `0` vacuously and must not be read as a perfect fit.

Formalized by `Cslib.MachineLearning.ArchetypalAnalysis.rss`, a definition declared in [CSLibExt/MachineLearning/ArchetypalAnalysis.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/ArchetypalAnalysis.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html#rss).

## Feasible archetypes

Archetypes are feasible if each is a mixture of the data points.

Formalized by `Cslib.MachineLearning.ArchetypalAnalysis.Feasible`, a definition declared in [CSLibExt/MachineLearning/ArchetypalAnalysis.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/ArchetypalAnalysis.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html#feasible).

## Sample mean of the data

The sample mean of the data.

Formalized by `Cslib.MachineLearning.ArchetypalAnalysis.mean`, a definition declared in [CSLibExt/MachineLearning/ArchetypalAnalysis.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/ArchetypalAnalysis.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html#mean).

## The sample mean is the optimal single archetype

Cutler–Breiman Proposition 1(i): with a single archetype, the sample mean is feasible and
minimizes the RSS.

Formalized by `Cslib.MachineLearning.ArchetypalAnalysis.rss_const_mean_le`, a theorem declared in [CSLibExt/MachineLearning/ArchetypalAnalysis.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/ArchetypalAnalysis.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html#rss-const-mean-le).

## Feasible archetypes can be moved to the boundary of the hull

Cutler–Breiman Proposition 1(ii): for at least two archetypes, any feasible archetypes can
be replaced by feasible archetypes on the boundary of the convex hull of the data whose convex
hull contains the original one; in particular the RSS does not increase.

Formalized by `Cslib.MachineLearning.ArchetypalAnalysis.exists_frontier_rss_le`, a theorem declared in [CSLibExt/MachineLearning/ArchetypalAnalysis.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/ArchetypalAnalysis.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html#exists-frontier-rss-le).

## Existence of an archetype minimizer on the hull boundary

If the RSS has a feasible minimizer with `p ≥ 2` archetypes, it has one with every
archetype on the boundary of the convex hull of the data.

Formalized by `Cslib.MachineLearning.ArchetypalAnalysis.exists_frontier_minimizer`, a theorem declared in [CSLibExt/MachineLearning/ArchetypalAnalysis.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/ArchetypalAnalysis.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html#exists-frontier-minimizer).

## The RSS vanishes when the archetypes' convex hull contains the data

Cutler–Breiman Proposition 1(iii): if every data point is a mixture of the archetypes, the
RSS vanishes. Requires `0 < p`: for `p = 0` the hull is empty, so `rss` is `0` vacuously
and the vanishing would not witness a fit.

Formalized by `Cslib.MachineLearning.ArchetypalAnalysis.rss_eq_zero_of_subset`, a theorem declared in [CSLibExt/MachineLearning/ArchetypalAnalysis.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/ArchetypalAnalysis.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html#rss-eq-zero-of-subset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Archetypal analysis](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/unsupervised-learning/archetypal-analysis)
