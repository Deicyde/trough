---
declaration: lemma
origin: cited
lean: ProbabilityTheory.locally_classD_of_locally_classDL
statement: formalized
proof: formalized
---

# locally_classD_of_locally_classDL

If the filtration is right-continuous and $X$ is locally of class DL then it is locally of class D.

## Depends on

- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)
- [Local property](../../local-properties/def-locally.md)
- [Doob-Meyer class, class D](../part-01/def-classd.md)
- [Class DL](../part-01/def-classdl.md)

## Proof depends on

- [Local implication from global implication](../../local-properties/lem-local-induction.md)
- [ClassDL.locally_classD](lem-classdl-locally-classd.md)
- [isStable_classD](../part-01/lem-isstable-classd.md)

## Proof

Apply Lemma [Local implication from global implication](../../local-properties/lem-local-induction.md) using Lemma [ClassDL.locally_classD](lem-classdl-locally-classd.md) and Lemma [isStable_classD](../part-01/lem-isstable-classd.md).

## Lean

Formalized as [`ProbabilityTheory.locally_classD_of_locally_classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.locally_classD_of_locally_classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 702](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L702)
