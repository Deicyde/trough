---
declaration: section
origin: cited
lean: MathlibExt.Probability.TailIntegralRV.intervalIntegrable_of_antitone_bdd, MathlibExt.Probability.TailIntegralRV.layerCake_firstMoment, MathlibExt.Probability.TailIntegralRV.tailIntegral_tendsto, MathlibExt.Probability.TruncatedMoment.tailGe, MathlibExt.Probability.TruncatedMoment.tailGt, MathlibExt.Probability.TruncatedMoment.tailGt_eq_combinedTail, MathlibExt.Probability.TruncatedMoment.tailGe_eq_combinedTail_add_atoms, MathlibExt.Probability.TruncatedMoment.tailGe_ratio_tendsto
statement: formalized
proof: formalized
---

# Truncated moments of regularly varying tails

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html).

## Antitone bounded functions are interval integrable

Antitone bounded functions are interval-integrable.

Formalized by `MathlibExt.Probability.TailIntegralRV.intervalIntegrable_of_antitone_bdd`, a theorem declared in [MathlibExt/Probability/TailIntegralRV.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TailIntegralRV.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#interval-integrable-of-antitone-bdd).

## Layer-cake formula for the first moment

Layer-cake formula for the first moment on `(0, a]`: the integral of `y`
over `(0, a]` equals the integral of the right tail minus the endpoint
correction.

Formalized by `MathlibExt.Probability.TailIntegralRV.layerCake_firstMoment`, a theorem declared in [MathlibExt/Probability/TailIntegralRV.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TailIntegralRV.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#layer-cake-first-moment).

## Corrected regularly-varying tail integral

For a probability measure `μ`
on `ℝ` with regularly varying combined tail of index `-α`, `0 < α < 1`, and
tail balance `p`, the first-moment tail integral satisfies
`(∫ y in Ioc 0 (c * x), y ∂μ) / (x * combinedTail μ x) → p * α * c ^ (1 - α) / (1 - α)`.

Formalized by `MathlibExt.Probability.TailIntegralRV.tailIntegral_tendsto`, a theorem declared in [MathlibExt/Probability/TailIntegralRV.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TailIntegralRV.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#tail-integral-tendsto).

## Closed upper tail of a measure

The upper tail `(μ {y | s ≤ |y|}).toReal`.

Formalized by `MathlibExt.Probability.TruncatedMoment.tailGe`, a definition declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#tail-ge).

## Strict upper tail of a measure

The lower tail `(μ {y | s < |y|}).toReal`.

Formalized by `MathlibExt.Probability.TruncatedMoment.tailGt`, a definition declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#tail-gt).

## Strict absolute tail equals the combined tail

At nonnegative thresholds the strict absolute tail is the canonical combined tail.

Formalized by `MathlibExt.Probability.TruncatedMoment.tailGt_eq_combinedTail`, a theorem declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#tail-gt-eq-combined-tail).

## Non-strict absolute tail as combined tail plus endpoint atoms

The non-strict absolute tail adds both endpoint atoms to the canonical strict tail.

Formalized by `MathlibExt.Probability.TruncatedMoment.tailGe_eq_combinedTail_add_atoms`, a theorem declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#tail-ge-eq-combined-tail-add-atoms).

## Upper tail is asymptotic to the combined tail

The upper tail is asymptotically the combined tail.

Formalized by `MathlibExt.Probability.TruncatedMoment.tailGe_ratio_tendsto`, a theorem declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#tail-ge-ratio-tendsto).

## Lower tail is asymptotic to the combined tail

The lower tail is asymptotically the combined tail.

Formalized by `MathlibExt.Probability.TruncatedMoment.tailGt_ratio_tendsto`, a theorem declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#tail-gt-ratio-tendsto).

## Layer-cake formula for the truncated second moment

Layer-cake formula for the truncated second moment, in terms of the upper
tail `tailGe`. The term `x ^ 2 * tailGt μ x` removes the contribution
from points with `|y| > x`, which lie outside the closed truncation interval.

Formalized by `MathlibExt.Probability.TruncatedMoment.layerCake`, a theorem declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#layer-cake).

## Truncated second moment asymptotic for regularly varying tails

The corrected truncated-second-moment asymptotic: for a probability measure
on `ℝ` with regularly varying combined tail of index `-α`, `0 < α < 2`, the
ratio `(∫ y in Icc (-x) x, y ^ 2 ∂μ) / (x ^ 2 * combinedTail μ x)` tends to
`α / (2 - α)`.

Correction: `v1/Atlas/TheoryOfProbability/code/RegularVariation.lean` states
this with the constant `2 / (2 - α)`, which is wrong; the Pareto tail gives
`α / (2 - α)` (see the test file).

Formalized by `MathlibExt.Probability.TruncatedMoment.truncatedMoment_tendsto`, a theorem declared in [MathlibExt/Probability/TruncatedMomentRV.lean, line 561](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/TruncatedMomentRV.lean#L561). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html#truncated-moment-tendsto).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Truncated moments of regularly varying tails](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/infinite-divisibility-regular-variation/truncated-moments-of-regularly-varying-tails)
