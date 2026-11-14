---
declaration: theorem
origin: cited
lean: MeasureTheory.IsPavingAnalytic.isCapacitable
statement: formalized
proof: formalized
---

# Choquet's capacitability theorem

Let $F$ be a set of sets of $\mathcal{X}$ and let $I$ be an $F$-capacity. Suppose that $F$ contains the empty set and is closed under pairwise intersections and unions. Then every $F$-analytic set is $I$-capacitable.

## Depends on

- [Analytic set](../part-01/def-ispavinganalytic.md)
- [IsCapacitable](../part-02/def-iscapacitable.md)

## Proof depends on

- [isCapacitable_of_mem_countableInfClosure_countableSupClosure](lem-iscapacitable-of-mem-countableinfclosure-cou.md)
- [IsCompactSystem.infClosure](../part-01/lem-iscompactsystem-infclosure.md)
- [IsCapacitable.fst](lem-iscapacitable-fst.md)

## Lean

Formalized as [`MeasureTheory.IsPavingAnalytic.isCapacitable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsPavingAnalytic.isCapacitable).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 591](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L591)
