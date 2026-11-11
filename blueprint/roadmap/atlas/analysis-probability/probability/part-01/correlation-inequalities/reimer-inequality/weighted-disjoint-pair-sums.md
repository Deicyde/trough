---
declaration: section
origin: cited
lean: StatMech.rbyCexA, StatMech.rbyCexB, StatMech.rby_separate_compression_strictly_decreases, StatMech.fwt, StatMech.fwt', StatMech.wdpairs, StatMech.wdpairs', StatMech.fmarg
statement: formalized
proof: formalized
---

# Weighted disjoint-pair sums

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html).

## First family in the weighted-pair counterexamples

The family `{∅, {0}}` on `Fin 2`, used in the counterexamples of this file.

Formalized by `StatMech.rbyCexA`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#rby-cex-a).

## Second family in the weighted-pair counterexamples

The family `{∅}` on `Fin 2`, used in the counterexamples of this file.

Formalized by `StatMech.rbyCexB`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#rby-cex-b).

## Down- and up-compressing two families can decrease disjoint pairs

Down-compressing `𝒜` and up-compressing `ℬ` at the same coordinate can strictly decrease
the number of disjoint pairs.

Formalized by `StatMech.rby_separate_compression_strictly_decreases`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#rby-separate-compression-strictly-decrea).

## Product weight of a finset

The product weight `∏ x, w x (x ∈ S)` of the configuration with support `S`.

Formalized by `StatMech.fwt`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#fwt).

## Product weight of a finset off one coordinate

The product weight of `S` over all coordinates except `i`.

Formalized by `StatMech.fwt'`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#fwt-2).

## Weighted number of disjoint pairs

The weighted number of disjoint pairs: `∑ fwt w S * fwt w T` over disjoint
`(S, T) ∈ 𝒜 × ℬ`.

Formalized by `StatMech.wdpairs`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#wdpairs).

## Weighted number of disjoint pairs off one coordinate

`wdpairs` with coordinate `i` omitted from the weights.

Formalized by `StatMech.wdpairs'`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#wdpairs-2).

## Weight of a family of finsets

The weight `∑ S ∈ 𝒜, fwt w S` of a family.

Formalized by `StatMech.fmarg`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#fmarg).

## Weight of a family off one coordinate

`fmarg` with coordinate `i` omitted from the weights.

Formalized by `StatMech.fmarg'`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#fmarg-2).

## Weighted disjoint pairs bounded by the product of family weights

For nonnegative weights, `wdpairs w 𝒜 ℬ ≤ fmarg w 𝒜 * fmarg w ℬ` (drop the disjointness
constraint).

Formalized by `StatMech.wdpairs_le_mul`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerWeightedPairs.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#wdpairs-le-mul).

## Expansion of the Reimer deficit over one coordinate

The deficit `fmarg w 𝒜 * fmarg w ℬ - wdpairs w 𝒜 ℬ` expanded over coordinate `i`.

Formalized by `StatMech.wbutterfly_deficit_identity`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSymmetricWeights.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSymmetricWeights.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#wbutterfly-deficit-identity).

## Box value of a doubled family under a symmetric weight

`(∏ x, w x true)^2 * #𝒰`: for a symmetric weight, the weight of a doubled family.

Formalized by `StatMech.wboxValue`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSymmetricWeights.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSymmetricWeights.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#wbox-value).

## Box-value bound fails for non-symmetric weights

For a non-symmetric weight, `wdpairs w 𝒜 ℬ ≤ wboxValue w (boxDoubled 𝒜 ℬ)` can fail.

Formalized by `StatMech.wdpairs_not_le_wboxValue_general`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSymmetricWeights.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSymmetricWeights.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html#wdpairs-not-le-wbox-value-general).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted disjoint-pair sums](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/weighted-disjoint-pair-sums)
