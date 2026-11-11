---
declaration: section
origin: cited
lean: StatMech.NegativelyCorrelated, StatMech.reimer_wprob_of_negCorr, StatMech.reimer_inequality_of_inter_empty, StatMech.evXor, StatMech.evXnor, StatMech.reimer_xor_xnor_inequality, StatMech.slice_disjointOccurrence_le_of_isIncreasing
statement: formalized
proof: formalized
---

# Special cases of Reimer's inequality

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html).

## Negatively correlated events

`A` and `B` are negatively correlated under the weight `φ`:
`wprob φ (A ∩ B) ≤ wprob φ A * wprob φ B`.

Formalized by `StatMech.NegativelyCorrelated`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html#negatively-correlated).

## Reimer's inequality for negatively correlated events

Reimer's inequality for negatively correlated events (since `A □ B ⊆ A ∩ B`).

Formalized by `StatMech.reimer_wprob_of_negCorr`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html#reimer-wprob-of-neg-corr).

## Reimer's inequality for disjoint events

Reimer's inequality for disjoint events under the product Bernoulli measure: both sides
are compared with `P(A □ B) = 0`.

Formalized by `StatMech.reimer_inequality_of_inter_empty`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html#reimer-inequality-of-inter-empty).

## Event that two coordinates differ

The event `ω 0 ≠ ω 1` on two coordinates.

Formalized by `StatMech.evXor`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html#ev-xor).

## Event that two coordinates agree

The event `ω 0 = ω 1` on two coordinates.

Formalized by `StatMech.evXnor`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html#ev-xnor).

## Reimer's inequality for the XOR and XNOR events

Reimer's inequality for `evXor` and `evXnor`, which are neither increasing nor decreasing
(and are disjoint).

Formalized by `StatMech.reimer_xor_xnor_inequality`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html#reimer-xor-xnor-inequality).

## Slice inequalities in the one-coordinate BK induction step

The slice inequalities of the one-coordinate BK induction step, with `A₀, A₁, B₀, B₁` the slices
at the first coordinate: `P(A₀ □ B₀) ≤ P((A₀ □ B₁) ∩ (A₁ □ B₀))` and
`P((A₀ □ B₁) ∪ (A₁ □ B₀)) ≤ P(A₁) P(B₁)`, for increasing events `A, B`.

Formalized by `StatMech.slice_disjointOccurrence_le_of_isIncreasing`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerSpecialCases.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html#slice-disjoint-occurrence-le-of-is-incre).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Special cases of Reimer's inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/special-cases-of-reimer-s-inequality)
