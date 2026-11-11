---
declaration: section
origin: cited
lean: StatMech.wprob_fkg_pos, StatMech.wprob_fkg_neg, StatMech.disjointOccurrence_eq_inter_of_mixed, StatMech.reimerMixed_wprob, StatMech.reimerMixed_inequality
statement: formalized
proof: formalized
---

# Reimer's inequality for an increasing and a decreasing event

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr/index.html).

## Harris–FKG inequality for increasing events

The Harris–FKG inequality for a product probability weight: increasing events are positively
correlated.

Formalized by `StatMech.wprob_fkg_pos`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr/index.html#wprob-fkg-pos).

## Harris–FKG inequality for an increasing and a decreasing event

The Harris–FKG inequality for an increasing and a decreasing event: they are negatively
correlated.

Formalized by `StatMech.wprob_fkg_neg`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr/index.html#wprob-fkg-neg).

## Disjoint occurrence of an increasing and a decreasing event

For `A` increasing and `B` decreasing, `A □ B = A ∩ B`.

Formalized by `StatMech.disjointOccurrence_eq_inter_of_mixed`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr/index.html#disjoint-occurrence-eq-inter-of-mixed).

## Reimer's inequality for mixed monotone events, product weights

Reimer's inequality for an increasing and a decreasing event under a product probability
weight.

Formalized by `StatMech.reimerMixed_wprob`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr/index.html#reimer-mixed-wprob).

## Reimer's inequality for mixed monotone events, Bernoulli measure

Reimer's inequality for an increasing and a decreasing event under the product Bernoulli
measure.

Formalized by `StatMech.reimerMixed_inequality`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/ReimerMixedMonotone.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr/index.html#reimer-mixed-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reimer's inequality for an increasing and a decreasing event](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-for-an-increasing-and-a-decr)
