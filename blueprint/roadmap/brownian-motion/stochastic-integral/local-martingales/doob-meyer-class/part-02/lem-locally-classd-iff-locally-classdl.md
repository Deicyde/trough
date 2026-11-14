---
declaration: lemma
origin: cited
lean: ProbabilityTheory.locally_classD_iff_locally_classDL
statement: formalized
proof: formalized
---

# locally_classD_iff_locally_classDL

Assume $T$ has a bottom element and that its closed intervals are compact, and that the filtration is right-continuous. A càdlàg process is locally of class D if and only if it is locally of class DL.

## Depends on

- [Doob-Meyer class, class D](../part-01/def-classd.md)
- [Class DL](../part-01/def-classdl.md)
- [Local property](../../local-properties/def-locally.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)

## Proof depends on

- [locally_classD_of_locally_classDL](lem-locally-classd-of-locally-classdl.md)
- [classDLOfClassD](../part-01/lem-classdlofclassd.md)
- [locally_mono](../../local-properties/lem-locally-mono.md)

## Proof

The forward direction follows from Lemma [classDLOfClassD](../part-01/lem-classdlofclassd.md) along with Lemma [locally_mono](../../local-properties/lem-locally-mono.md). The reverse direction is Lemma [locally_classD_of_locally_classDL](lem-locally-classd-of-locally-classdl.md).

## Lean

Formalized as [`ProbabilityTheory.locally_classD_iff_locally_classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.locally_classD_iff_locally_classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 807](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L807)
