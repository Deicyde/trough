---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.Contiguity.IsContiguous, MathlibExt.Probability.Statistics.Contiguity.gaussianReal_withDensity_exp, MathlibExt.Probability.Statistics.Contiguity.isContiguous_withDensity_exp, MathlibExt.Probability.Statistics.Contiguity.tendstoInDistribution_withDensity_exp, MathlibExt.Probability.Statistics.Contiguity.IsContiguous.tendsto_measure_abs_sub_ge
statement: formalized
proof: formalized
---

# Contiguity and Le Cam's lemmas

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas/index.html).

## Contiguity of sequences of measures

The sequence of measures `Q n` is **contiguous** with respect to `P n` (`Q ◁ P`): every
sequence of measurable sets whose `P n`-measure tends to `0` has `Q n`-measure tending to `0`.

## Sources

- van der Vaart (1998), Definition 6.3.

Formalized by `MathlibExt.Probability.Statistics.Contiguity.IsContiguous`, a definition declared in [MathlibExt/Probability/Statistics/Contiguity.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Contiguity.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas/index.html#is-contiguous).

## Exponential tilting of a centered Gaussian

The law `N(0, v)` reweighted by the density
`exp(h x - h² v / 2)` is `N(h v, v)`. For `v = 0` both sides are the Dirac mass at `0`.

Formalized by `MathlibExt.Probability.Statistics.Contiguity.gaussianReal_withDensity_exp`, a theorem declared in [MathlibExt/Probability/Statistics/Contiguity.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Contiguity.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas/index.html#gaussian-real-with-density-exp).

## Le Cam's first lemma

**Le Cam's first lemma** (LAN case). Let `Qₙ = exp(Λₙ) · P` be probability measures. If
`Sₙ → N(0, v)` in distribution under `P` and `Λₙ - h Sₙ → -h² v / 2` in `P`-probability, then
`Qₙ` is contiguous with respect to `P`. This is the case of Le Cam's first lemma in which
`Λₙ → N(-σ²/2, σ²)` under `P`, `σ² = h² v`; the general form (any limit `L` of `dQₙ/dP` with
`E L = 1`) is not stated here.

## Sources

- Le Cam (1960); van der Vaart (1998), Lemma 6.4 and Example 6.5.

Formalized by `MathlibExt.Probability.Statistics.Contiguity.isContiguous_withDensity_exp`, a theorem declared in [MathlibExt/Probability/Statistics/Contiguity.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Contiguity.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas/index.html#is-contiguous-with-density-exp).

## Le Cam's third lemma

**Le Cam's third lemma** (LAN case). Let `Qₙ = exp(Λₙ) · P` be probability measures. If
`Sₙ → N(0, v)` in distribution under `P` and `Λₙ - h Sₙ → -h² v / 2` in `P`-probability, then
`Sₙ → N(h v, v)` in distribution under `Qₙ`. This is the case of Le Cam's third lemma for the
central sequence itself (covariance `h v` with `Λₙ`); the general form, for an arbitrary
statistic jointly asymptotically normal with `Λₙ`, is not stated here.

## Sources

- Le Cam (1960); van der Vaart (1998), Theorem 6.6.

Formalized by `MathlibExt.Probability.Statistics.Contiguity.tendstoInDistribution_withDensity_exp`, a theorem declared in [MathlibExt/Probability/Statistics/Contiguity.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Contiguity.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas/index.html#tendsto-in-distribution-with-density-exp).

## Contiguity transfers convergence in probability

If `Q ◁ P` (a fixed `P`) and the
measurable functions `T n` converge to `c` in `P`-probability, then
`Q n {ω | ε ≤ |T n ω - c|} → 0` for every `ε > 0`.

## Sources

- van der Vaart (1998), ch. 6.

Formalized by `MathlibExt.Probability.Statistics.Contiguity.IsContiguous.tendsto_measure_abs_sub_ge`, a theorem declared in [MathlibExt/Probability/Statistics/Contiguity.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Contiguity.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas/index.html#tendsto-measure-abs-sub-ge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Contiguity and Le Cam's lemmas](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/statistical-estimation/contiguity-and-le-cam-s-lemmas)
