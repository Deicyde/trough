---
declaration: lemma
origin: cited
lean: MeasureTheory.Submartingale.locally_classD
statement: formalized
proof: formalized
---

# Submartingale.locally_classD

Every cadlag submartingale is locally of class D.

## Depends on

- [Submartingale](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-submartingale.md)
- [Doob-Meyer class, class D](../part-01/def-classd.md)
- [Local property](../../local-properties/def-locally.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)

## Proof depends on

- [Submartingale.classDL](../part-01/lem-submartingale-classdl.md)
- [locally_classD_iff_locally_classDL](lem-locally-classd-iff-locally-classdl.md)

## Proof

By Lemma [locally_classD_iff_locally_classDL](lem-locally-classd-iff-locally-classdl.md), it suffices to show that every cadlag submartingale is locally of class DL. This can be proved with Lemma [Submartingale.classDL](../part-01/lem-submartingale-classdl.md).

## Lean

Formalized as [`MeasureTheory.Submartingale.locally_classD`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.locally_classD).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 861](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L861)
