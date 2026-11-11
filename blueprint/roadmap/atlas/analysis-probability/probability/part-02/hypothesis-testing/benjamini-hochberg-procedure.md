---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.MultipleTesting.bhIndex, MathlibExt.Probability.Statistics.MultipleTesting.bhRejections, MathlibExt.Probability.Statistics.MultipleTesting.bhIndex_le, MathlibExt.Probability.Statistics.MultipleTesting.bhIndex_le_numBelow, MathlibExt.Probability.Statistics.MultipleTesting.le_bhIndex, MathlibExt.Probability.Statistics.MultipleTesting.card_bhRejections, MathlibExt.Probability.Statistics.MultipleTesting.integral_falseDiscoveryProportion_bhRejections_le
statement: formalized
proof: formalized
---

# Benjamini–Hochberg procedure

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html).

## Benjamini–Hochberg step-up index

The Benjamini–Hochberg step-up index: the largest `k ∈ {0, …, m}` such that at least `k`
p-values are at most `q k / m` (`k = 0` always qualifies).

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.bhIndex`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html#bh-index).

## Benjamini–Hochberg rejection set

The hypotheses rejected by the Benjamini–Hochberg procedure at level `q`: those whose
p-value is at most `q * bhIndex q p / m`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.bhRejections`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html#bh-rejections).

## Benjamini–Hochberg index is at most the number of hypotheses

The BH step-up index is at most `m`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.bhIndex_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html#bh-index-le).

## Benjamini–Hochberg index satisfies the step-up condition

At the BH step-up index `k`, at least `k` p-values are at most `q k / m`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.bhIndex_le_numBelow`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html#bh-index-le-num-below).

## Maximality of the Benjamini–Hochberg index

The BH step-up index is the largest `k ≤ m` with at least `k` p-values at most `q k / m`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.le_bhIndex`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html#le-bh-index).

## Number of Benjamini–Hochberg rejections

The BH procedure at level `q ≥ 0` rejects exactly `bhIndex q p` hypotheses.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.card_bhRejections`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html#card-bh-rejections).

## Benjamini–Hochberg FDR control

If the p-values are independent and every true-null
p-value is uniformly distributed on `[0, 1]`, the BH procedure at level `q ∈ [0, 1]` has false
discovery rate at most `q |H0| / m`. Nothing is assumed about the false-null p-values beyond
measurability and independence. (For `m = 0` both sides are `0`.)

## Sources

- Benjamini & Hochberg (1995), Theorem 1.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.integral_falseDiscoveryProportion_bhRejections_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/BenjaminiHochberg.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html#integral-false-discovery-proportion-bh-r).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Benjamini–Hochberg procedure](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/benjamini-hochberg-procedure)
