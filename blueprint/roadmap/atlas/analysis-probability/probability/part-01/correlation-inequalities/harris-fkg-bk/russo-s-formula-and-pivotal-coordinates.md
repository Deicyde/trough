---
declaration: section
origin: cited
lean: StatMech.setOpen, StatMech.setClosed, StatMech.setClosed_le_setOpen, StatMech.setOpen_congr, StatMech.setClosed_congr, StatMech.IsPivotal, StatMech.isPivotal_comm, StatMech.isPivotal_congr
statement: formalized
proof: formalized
---

# Russo's formula and pivotal coordinates

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html).

## Opening a coordinate of a configuration

`setOpen e ω` is `ω` with coordinate `e` set to `true` (open).

Formalized by `StatMech.setOpen`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#set-open).

## Closing a coordinate of a configuration

`setClosed e ω` is `ω` with coordinate `e` set to `false` (closed).

Formalized by `StatMech.setClosed`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#set-closed).

## Closed configuration lies below the opened one

Closing a coordinate gives a smaller configuration than opening it.

Formalized by `StatMech.setClosed_le_setOpen`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#set-closed-le-set-open).

## Opening a coordinate depends only on the other coordinates

`setOpen e ω` depends only on the values of `ω` off `e`.

Formalized by `StatMech.setOpen_congr`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#set-open-congr).

## Closing a coordinate depends only on the other coordinates

`setClosed e ω` depends only on the values of `ω` off `e`.

Formalized by `StatMech.setClosed_congr`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#set-closed-congr).

## Pivotal coordinate for an event

The coordinate `e` is *pivotal* for the event `A` at `ω` if exactly one of `setOpen e ω` and
`setClosed e ω` lies in `A`. The condition does not depend on `ω e`.

Formalized by `StatMech.IsPivotal`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#is-pivotal).

## Symmetric form of pivotality

Pivotality with the two sides swapped.

Formalized by `StatMech.isPivotal_comm`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#is-pivotal-comm).

## Pivotality depends only on the other coordinates

Pivotality of `e` depends only on the values of `ω` off `e`.

Formalized by `StatMech.isPivotal_congr`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#is-pivotal-congr).

## Opening a coordinate preserves its pivotality

Opening `e` does not change whether `e` is pivotal.

Formalized by `StatMech.isPivotal_setOpen`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#is-pivotal-set-open).

## Closing a coordinate preserves its pivotality

Closing `e` does not change whether `e` is pivotal.

Formalized by `StatMech.isPivotal_setClosed`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#is-pivotal-set-closed).

## Pivotal coordinates of an increasing event

For an increasing event `A`, the coordinate `e` is pivotal at `ω` iff `setClosed e ω ∉ A`
and `setOpen e ω ∈ A`.

Formalized by `StatMech.isPivotal_iff_of_isIncreasing`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Pivotal.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Pivotal.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#is-pivotal-iff-of-is-increasing).

## Bernoulli weight of a single coordinate

The weight of coordinate `e` in configuration `ω` with parameter `p`: `p` if `ω e` is open
(`true`), `1 - p` otherwise.

Formalized by `StatMech.edgeWeight`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#edge-weight).

## Product of coordinate weights off one coordinate

The product of the coordinate weights over all coordinates except `e`.

Formalized by `StatMech.weightOff`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#weight-off).

## Bernoulli product weight of a configuration

The product weight `∏ e, edgeWeight p ω e` of a configuration; for `p ∈ [0, 1]` the
probability of `ω` under independent Bernoulli(`p`) coordinates.

Formalized by `StatMech.configWeight`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#config-weight).

## Bernoulli weight of an event

The weight `∑ ω ∈ A, configWeight p ω` of an event `A`; for `p ∈ [0, 1]` its probability
under independent Bernoulli(`p`) coordinates.

Formalized by `StatMech.prob`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#prob).

## Weight of the event that a coordinate is pivotal

The weight of the event that coordinate `e` is pivotal for `A`.

Formalized by `StatMech.pivotalProb`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#pivotal-prob).

## Configuration weight as a product weight

`configWeight` is the product weight `StatMech.pweight` for Bernoulli coordinate weights.

Formalized by `StatMech.configWeight_eq_pweight`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#config-weight-eq-pweight).

## Nonnegativity of the configuration weight

The product weight `configWeight p ω` is nonnegative for `p ∈ [0, 1]`.

Formalized by `StatMech.configWeight_nonneg`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#config-weight-nonneg).

## Nonnegativity of the pivotal weight

The pivotal weight `pivotalProb p A e` is nonnegative for `p ∈ [0, 1]`.

Formalized by `StatMech.pivotalProb_nonneg`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#pivotal-prob-nonneg).

## Event weight as a product-weight probability

`prob` is `StatMech.wprob` for Bernoulli coordinate weights.

Formalized by `StatMech.prob_eq_wprob`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#prob-eq-wprob).

## Configuration weight splits at one coordinate

The product weight splits as the weight of `e` times the weight of the other coordinates.

Formalized by `StatMech.configWeight_eq`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#config-weight-eq).

## Off-coordinate weight depends only on the other coordinates

`weightOff p e ω` depends only on the values of `ω` off `e`.

Formalized by `StatMech.weightOff_congr`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#weight-off-congr).

## Derivative of a single coordinate weight

The derivative in `p` of a coordinate weight is `1` if the coordinate is open, `-1`
otherwise.

Formalized by `StatMech.hasDerivAt_edgeWeight`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#has-deriv-at-edge-weight).

## Derivative of the configuration weight

The derivative in `p` of the product weight (product rule).

Formalized by `StatMech.hasDerivAt_configWeight`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#has-deriv-at-config-weight).

## Derivative of the event weight before grouping

The derivative in `p` of `prob p A`, before grouping by pivotal coordinates.

Formalized by `StatMech.hasDerivAt_prob`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#has-deriv-at-prob).

## Opening a coordinate of a split configuration

Opening `e` in the configuration with value `b` at `e` and `η` elsewhere.

Formalized by `StatMech.setOpen_symm`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#set-open-symm).

## Closing a coordinate of a split configuration

Closing `e` in the configuration with value `b` at `e` and `η` elsewhere.

Formalized by `StatMech.setClosed_symm`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#set-closed-symm).

## Russo's formula on a single fiber

Russo's formula on one fiber `{ωt, ωf}` of configurations differing only at `e`.

Formalized by `StatMech.russo_per_eta`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#russo-per-eta).

## Contribution of one coordinate to Russo's formula

The contribution of coordinate `e` to the derivative of `prob p A` is
`pivotalProb p A e`, for increasing `A`.

Formalized by `StatMech.russo_per_edge`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#russo-per-edge).

## Russo's formula

**Russo's formula** (Russo 1981; Margulis 1974): for an increasing event `A` on a finite
set of coordinates, `p ↦ prob p A` has derivative `∑ e, pivotalProb p A e` at every `p`.

Formalized by `StatMech.hasDerivAt_prob_eq_sum_pivotalProb`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#has-deriv-at-prob-eq-sum-pivotal-prob).

## Russo's formula

**Russo's formula**, `deriv` form: `d/dp prob p A = ∑ e, pivotalProb p A e` for
increasing `A`.

Formalized by `StatMech.deriv_prob_eq_sum_pivotalProb`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Russo.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/Russo.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html#deriv-prob-eq-sum-pivotal-prob).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Russo's formula and pivotal coordinates](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/correlation-inequalities/harris-fkg-bk/russo-s-formula-and-pivotal-coordinates)
