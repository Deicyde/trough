---
declaration: section
origin: cited
lean: MathlibExt.Probability.KolmogorovContinuity.dyadicRationals, MathlibExt.Probability.KolmogorovContinuity.dyadic_holder_of_increment_bound, MathlibExt.Probability.KolmogorovContinuity.kolmogorov_ae_holder_on_dyadics, MathlibExt.Probability.KolmogorovContinuity.kolmogorov_continuity_theorem, MathlibExt.Probability.KolmogorovContinuity.kolmogorov_ae_holder_on_dyadics_of_isKolmogorovProcess, MathlibExt.Probability.KolmogorovContinuousModification.exists_continuous_modification
statement: formalized
proof: formalized
---

# Kolmogorov continuity theorem

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html).

## Dyadic rationals

The set of **dyadic rationals**: real numbers of the form `k / 2 ^ n`
for some integer `k` and natural number `n`.

Formalized by `MathlibExt.Probability.KolmogorovContinuity.dyadicRationals`, a definition declared in [MathlibExt/Probability/KolmogorovContinuity.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/KolmogorovContinuity.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html#dyadic-rationals).

## Deterministic chaining

If every adjacent dyadic increment at level
`m` is at most `D * 2^{-mγ}`, then `f` is `γ`-Hölder on the dyadic
rationals of `[0, 1]`, with an explicit constant.

Formalized by `MathlibExt.Probability.KolmogorovContinuity.dyadic_holder_of_increment_bound`, a theorem declared in [MathlibExt/Probability/KolmogorovContinuity.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/KolmogorovContinuity.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html#dyadic-holder-of-increment-bound).

## Almost sure Hölder bound on the dyadic rationals

A single full-measure set carries a Hölder bound for the original process
on the dyadic rationals of `[0, 1]`. The moment-integrability correction in
the module docstring is required for this Bochner formulation.

Formalized by `MathlibExt.Probability.KolmogorovContinuity.kolmogorov_ae_holder_on_dyadics`, a theorem declared in [MathlibExt/Probability/KolmogorovContinuity.lean, line 744](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/KolmogorovContinuity.lean#L744). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html#kolmogorov-ae-holder-on-dyadics).

## Kolmogorov continuity theorem

**Kolmogorov continuity theorem**, in the original modification formulation.
The direct dyadic bound permits choosing `Y = X`. See the module docstring for
the necessary moment-integrability correction to the archived v1 statement.

Formalized by `MathlibExt.Probability.KolmogorovContinuity.kolmogorov_continuity_theorem`, a theorem declared in [MathlibExt/Probability/KolmogorovContinuity.lean, line 860](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/KolmogorovContinuity.lean#L860). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html#kolmogorov-continuity-theorem).

## Hölder bound on dyadics for a Kolmogorov process

The canonical Kolmogorov-process condition implies a common a.e. Hölder
bound for `X` on the dyadics of `[0, 1]`. Its measurable-pair and finite
lintegral fields supply the Bochner hypotheses internally, including when
`M = 0`. No claim is made about the raw paths at every real time.

Formalized by `MathlibExt.Probability.KolmogorovContinuity.kolmogorov_ae_holder_on_dyadics_of_isKolmogorovProcess`, a theorem declared in [MathlibExt/Probability/KolmogorovContinuity.lean, line 926](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/KolmogorovContinuity.lean#L926). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html#kolmogorov-ae-holder-on-dyadics-of-is-ko).

## Kolmogorov continuous-modification theorem for real-valued processes

A real-valued Kolmogorov process on `NNReal` whose time exponent is greater
than one has one modification with measurable coordinates and continuous paths
on every sample. The same modification agrees exactly at time zero and
preserves every closed set containing an original sample path. Fixed-time
almost-everywhere equality is asserted separately at each time; no
indistinguishability claim is made for the raw process.

Formalized by `MathlibExt.Probability.KolmogorovContinuousModification.exists_continuous_modification`, a theorem declared in [MathlibExt/Probability/KolmogorovContinuousModification.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/KolmogorovContinuousModification.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html#exists-continuous-modification).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kolmogorov continuity theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/stochastic-calculus/kolmogorov-continuity-theorem)
