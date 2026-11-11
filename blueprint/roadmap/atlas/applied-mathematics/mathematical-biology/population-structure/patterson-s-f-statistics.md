---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.FStatistics.f2, MathlibExt.Biology.PopulationGenetics.FStatistics.f3, MathlibExt.Biology.PopulationGenetics.FStatistics.f4, MathlibExt.Biology.PopulationGenetics.FStatistics.f2_self, MathlibExt.Biology.PopulationGenetics.FStatistics.f2_comm, MathlibExt.Biology.PopulationGenetics.FStatistics.f2_nonneg, MathlibExt.Biology.PopulationGenetics.FStatistics.f4_comm_pairs, MathlibExt.Biology.PopulationGenetics.FStatistics.f4_swap_left
statement: formalized
proof: formalized
---

# Patterson's f-statistics

40 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html).

## Definitions and model-free identities

## f2 statistic

The statistic `f2 X Y = 𝔼[(p X - p Y) ^ 2]`, the expected squared allele-frequency
difference between populations `X` and `Y`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f2`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f2).

## f3 statistic

The statistic `f3 C A B = 𝔼[(p C - p A) * (p C - p B)]` of a target population `C` against
two source populations `A` and `B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f3`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3).

## f4 statistic

The statistic `f4 A B C D = 𝔼[(p A - p B) * (p C - p D)]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f4`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4).

## f2 of a population with itself is zero

`f2 X X = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f2_self`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f2-self).

## Symmetry of the f2 statistic

`f2` is symmetric.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f2_comm`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f2-comm).

## Nonnegativity of the f2 statistic

`f2` is nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f2_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f2-nonneg).

## f4 is symmetric under exchanging the two pairs

`f4` is symmetric under exchanging the two pairs.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f4_comm_pairs`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-comm-pairs).

## f4 changes sign when the first pair is swapped

`f4` changes sign when the first pair is swapped.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f4_swap_left`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-swap-left).

## f4 changes sign when the second pair is swapped

`f4` changes sign when the second pair is swapped.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f4_swap_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-swap-right).

## f2 as a special case of f4

`f2` is the special case `f4 A B A B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f2_eq_f4`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f2-eq-f4).

## f3 as a special case of f4

`f3` is the special case `f4 C A C B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f3_eq_f4`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3-eq-f4).

## Square of a difference of square-integrable frequencies is integrable

A difference of square-integrable frequencies has integrable square.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.integrable_sub_sq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#integrable-sub-sq).

## f3 in terms of f2

`f3` in terms of `f2`: `f3 C A B = (f2 C A + f2 C B - f2 A B) / 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f3_eq_f2`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3-eq-f2).

## f4 in terms of f2

`f4` in terms of `f2`: `f4 A B C D = (f2 A D + f2 B C - f2 A C - f2 B D) / 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.f4_eq_f2`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-eq-f2).

## Admixture-graph drift model

The admixture-graph drift model, stated at the level of second moments.

The allele frequency of population `X` is `root + ∑ e, weight X e * incr e` (see
`DriftModel.freq`), where `E` is the (finite) set of edges of the graph.

* `root` is the ancestral (root) allele frequency;
* `incr e` is the drift increment (frequency change) along edge `e`;
* `len e` is the drift length of edge `e`, i.e. the second moment `𝔼[incr e ^ 2]`;
* `weight X e` is the probability that a lineage sampled in `X` traverses `e`: on an
  admixture graph it is the sum, over root-to-`X` paths through `e`, of the product of the
  admixture proportions on the path; on a tree it is the `0`/`1` indicator that `e` lies on
  the root-to-`X` lineage.

f-statistics depend only on second moments of frequency differences, in which the root
cancels, so only these are assumed: the increments are square integrable, pairwise
uncorrelated (the mixed second moments `𝔼[incr e * incr f]`, `e ≠ f`, vanish, as they do for
independent mean-zero drift on distinct edges), and `𝔼[incr e ^ 2] = len e`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel`, a structure declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#drift-model).

## Allele frequency of a population in the drift model

The allele frequency of population `X`: the root frequency plus the weighted sum of the
drift increments of the edges traversed by lineages from `X`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.freq`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#freq).

## Drift lengths are nonnegative

Drift lengths are nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.len_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#len-nonneg).

## Weighted sum of drift increments is square integrable

A weighted sum of increments is square integrable.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.memLp_sum_incr`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#mem-lp-sum-incr).

## Population frequencies are square integrable

Population frequencies are square integrable.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.memLp_freq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#mem-lp-freq).

## Bilinearity of the second moment of drift increments

Bilinearity of the second moment of increments:
`𝔼[(∑ e, a e * incr e) * (∑ f, b f * incr f)] = ∑ e, a e * b e * len e`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.integral_sum_mul_sum`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#integral-sum-mul-sum).

## f4 in the drift model

`f4` in the drift model: the root cancels, and `f4 A B C D` is the drift length shared by
the paths `A–B` and `C–D`, weighted by `(w A e - w B e) * (w C e - w D e)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f4_freq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-freq).

## f2 in the drift model

`f2` in the drift model: `f2 X Y = ∑ e, (w X e - w Y e) ^ 2 * len e`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f2_freq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f2-freq).

## f3 in the drift model

`f3` in the drift model: `f3 C A B = ∑ e, (w C e - w A e) * (w C e - w B e) * len e`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f3_freq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3-freq).

## f4 vanishes for edge-disjoint paths

`f4 A B C D = 0` when no edge contributes to both the `A–B` and the `C–D` path. On a tree
with split `AB | CD` the paths `A–B` and `C–D` share no edge, so this hypothesis holds.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f4_eq_zero_of_disjoint`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-eq-zero-of-disjoint).

## Binary loadings of a drift model

The model has binary loadings if every lineage weight is `0` or `1`.

Every tree model has binary loadings: there `weight X e` is the indicator of `e` lying on the
root-to-`X` path. The converse fails, since nothing forces the weight-`1` edge sets to be
compatible root-to-leaf paths: two edges of length `1` and four populations with weight
vectors `00`, `10`, `01`, `11` have binary loadings, but their `f2` distances form a square,
which violates the four-point condition of tree metrics. The results below use only the binary
values, so they apply to every tree.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.HasBinaryLoadings`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#has-binary-loadings).

## Lineage of a population in the drift model

The edges of weight `1` for population `X`; on a tree, the root-to-`X` lineage.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.lineage`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#lineage).

## f3 is nonnegative under binary loadings

With binary loadings `f3` is nonnegative; on a tree it is the drift length of the path from
`C` to the `A–B` path.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f3_nonneg_of_hasBinaryLoadings`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3-nonneg-of-has-binary-loadings).

## f2 as a symmetric-difference drift length under binary loadings

With binary loadings `f2 X Y` is the total drift length of the edges in exactly one of the
weight-`1` edge sets of `X` and `Y`. On a tree, where these sets are the root-to-`X` and
root-to-`Y` paths, this is the additive tree distance between `X` and `Y`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f2_eq_sum_symmDiff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f2-eq-sum-symm-diff).

## Three-population test: negative f3 rules out a tree

Three-population test: a negative `f3 C A B` is incompatible with binary loadings, hence
with every tree model.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.not_hasBinaryLoadings_of_f3_neg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#not-has-binary-loadings-of-f3-neg).

## f3 of a pure admixture

If `C` is a mixture of `A` and `B` in proportions `α : 1 - α` (with no subsequent drift),
then `f3 C A B = -α (1 - α) f2 A B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f3_admixture`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3-admixture).

## f3 of an admixture followed by drift

Admixture followed by drift: if `C` is an `α : 1 - α` mixture of `A` and `B` that then
drifts along a private edge `c` (not traversed by `A` or `B`), then
`f3 C A B = len c - α (1 - α) f2 A B`; post-admixture drift can mask the admixture signal.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f3_admixture_drift`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3-admixture-drift).

## Nondegenerate pure admixture gives negative f3

Three-population test, converse direction: a nondegenerate pure admixture
(`0 < α < 1`, `f2 A B > 0`) yields a negative `f3 C A B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f3_neg_of_admixture`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f3-neg-of-admixture).

## f4 of an admixed population scales with the mixture proportion

If `X` is an `α : 1 - α` mixture of `Y` and `C`, then `f4 A O X C = α * f4 A O Y C`
(bilinearity of `f4`, together with `f4 A O C C = 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f4_admixture_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-admixture-right).

## f4-ratio estimation of the admixture proportion

**f4-ratio estimation of the admixture proportion.** f4-ratio estimation (Patterson et al. 2012). Let `X` be an `α : 1 - α` mixture of a
source lineage `Y` and of `C`, where `Y` is unsampled but sister to the sampled population `B`
relative to the `A–O` path, so that `f4 A O Y C = f4 A O B C`. If this value is nonzero, the
ratio `f4 A O X C / f4 A O B C` of two estimable statistics recovers the admixture
proportion `α`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.DriftModel.f4_ratio`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#f4-ratio).

## Mean allele frequency of a subdivided population

Mean allele frequency `q̄ = ∑ i, c i * q i` of a population made of subpopulations with
weights `c i` and allele frequencies `q i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.meanFreq`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#mean-freq).

## Mean within-subpopulation heterozygosity

Mean within-subpopulation (Hardy–Weinberg) heterozygosity `H_S = ∑ i, c i * 2 q i (1 - q i)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.hetSub`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#het-sub).

## Total heterozygosity of the pooled population

Total heterozygosity `H_T = 2 q̄ (1 - q̄)` expected under random mating of the pooled
population.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.hetTotal`, a definition declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#het-total).

## Wahlund identity

Wahlund identity: for weights summing to `1`, `H_T - H_S = 2 ∑ i, c i * (q i - q̄) ^ 2`,
twice the weighted variance of subpopulation frequencies.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.wahlund`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#wahlund).

## Wahlund effect

The Wahlund effect: with nonnegative weights summing to `1`, subdivision lowers
heterozygosity, `H_S ≤ H_T`.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.hetSub_le_hetTotal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#het-sub-le-het-total).

## Nonnegativity of the fixation index $F_{ST}$

`F_ST = (H_T - H_S) / H_T` is nonnegative for nonnegative weights summing to `1`. The ratio
is defined only when `H_T > 0` (at a fixed allele `H_T = H_S = 0`), so that is assumed.

Formalized by `MathlibExt.Biology.PopulationGenetics.FStatistics.fst_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/FStatistics.lean, line 430](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/FStatistics.lean#L430). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html#fst-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Patterson's f-statistics](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/patterson-s-f-statistics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-structure/patterson-s-f-statistics)
