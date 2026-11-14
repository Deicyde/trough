---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsLocalSubmartingale.locally_classD
statement: formalized
proof: formalized
---

# IsLocalSubmartingale.locally_classD

Every local submartingale is locally of class D.

## Depends on

- [IsLocalSubmartingale](../../local-martingales/def-islocalsubmartingale.md)
- [Doob-Meyer class, class D](../part-01/def-classd.md)
- [Local property](../../local-properties/def-locally.md)

## Proof depends on

- [Local implication from global implication](../../local-properties/lem-local-induction.md)
- [stable_IsSubmartingale](../../local-martingales/lem-stable-issubmartingale.md)
- [Submartingale.locally_classD](lem-submartingale-locally-classd.md)
- [isStable_classD](../part-01/lem-isstable-classd.md)

## Proof

By Lemma [Local implication from global implication](../../local-properties/lem-local-induction.md), it suffices to show that if $X$ is a submartingale then it is locally of class D. This is done in Lemma [Submartingale.locally_classD](lem-submartingale-locally-classd.md).

## Lean

Formalized as [`ProbabilityTheory.IsLocalSubmartingale.locally_classD`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsLocalSubmartingale.locally_classD).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 876](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L876)
