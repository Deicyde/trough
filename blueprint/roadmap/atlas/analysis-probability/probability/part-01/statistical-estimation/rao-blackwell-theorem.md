---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.Sufficiency.integrable_comp_condExp, MathlibExt.Probability.Statistics.Sufficiency.integral_comp_condExp_le, MathlibExt.Probability.Statistics.Sufficiency.integral_sq_sub_eq_add, MathlibExt.Probability.Statistics.Sufficiency.integral_sq_sub_condExp_eq_iff, MathlibExt.Probability.Statistics.Sufficiency.IsSufficient.raoBlackwell, MathlibExt.Probability.Statistics.Sufficiency.raoBlackwell_comap
statement: formalized
proof: formalized
---

# Rao–Blackwell theorem

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html).

## Integrability of a convex loss of a conditional expectation

For a convex loss `L`, `L ∘ μ[W | m]` is integrable whenever `W` and `L ∘ W` are.

Formalized by `MathlibExt.Probability.Statistics.Sufficiency.integrable_comp_condExp`, a theorem declared in [MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html#integrable-comp-cond-exp).

## Rao–Blackwell inequality for one law

For a convex loss `L` and an integrable `W` with
integrable loss, `∫ L(μ[W | m]) dμ ≤ ∫ L(W) dμ`.

Formalized by `MathlibExt.Probability.Statistics.Sufficiency.integral_comp_condExp_le`, a theorem declared in [MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html#integral-comp-cond-exp-le).

## Squared-error decomposition

For `W` with a finite second moment and any target `c`,
`E (W - c)² = E (μ[W | m] - c)² + E (W - μ[W | m])²`. This is the Pythagorean identity
`MeasureTheory.integral_sq_sub_eq_integral_sq_sub_condExp_add` with the constant predictor
`fun _ => c`, with the two summands commuted; it is not a second Pythagorean proof.

Formalized by `MathlibExt.Probability.Statistics.Sufficiency.integral_sq_sub_eq_add`, a theorem declared in [MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html#integral-sq-sub-eq-add).

## Equality case under squared error

Conditioning leaves the squared-error risk at `c`
unchanged if and only if `W` already equals `μ[W | m]` almost everywhere.

Formalized by `MathlibExt.Probability.Statistics.Sufficiency.integral_sq_sub_condExp_eq_iff`, a theorem declared in [MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html#integral-sq-sub-cond-exp-eq-iff).

## The Rao–Blackwell theorem

Let `m` be sufficient for the family of probability measures
`P`, and let `W` be a measurable estimator that is integrable under every `P θ`. There is one
parameter-free `m`-measurable estimator `η`, a version of `P_θ[W | m]` for every `θ`, with
the same mean as `W` under every `θ` and no larger risk under every loss `ℓ θ` that is convex
in the estimate (for which `ℓ θ ∘ W` is integrable).

## Sources

- Rao (1945); Blackwell (1947); Casella–Berger, Section 7.3.

Formalized by `MathlibExt.Probability.Statistics.Sufficiency.IsSufficient.raoBlackwell`, a theorem declared in [MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html#rao-blackwell).

## The Rao–Blackwell theorem for a sufficient statistic

If the statistic `T` is
sufficient for `P` and `W` is a measurable estimator with finite second moment under every
`P θ`, there is a measurable `φ` such that `φ ∘ T` is a version of every `E_θ[W | T]`, has the
same mean as `W`, and for every target `τ θ` satisfies
`E_θ (W - τ θ)² = E_θ (φ(T) - τ θ)² + E_θ (W - φ(T))²`.

Formalized by `MathlibExt.Probability.Statistics.Sufficiency.raoBlackwell_comap`, a theorem declared in [MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/Sufficiency/RaoBlackwell.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html#rao-blackwell-comap).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rao–Blackwell theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/rao-blackwell-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/statistical-estimation/rao-blackwell-theorem)
