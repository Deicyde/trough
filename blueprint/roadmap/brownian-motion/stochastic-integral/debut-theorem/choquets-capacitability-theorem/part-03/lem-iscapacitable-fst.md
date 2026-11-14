---
declaration: lemma
origin: cited
lean: MeasureTheory.IsCapacitable.fst
statement: formalized
proof: formalized
---

# IsCapacitable.fst

Let $F$ be a set of sets of $\mathcal{X}$ and let $I$ be an $F$-capacity. Suppose that $F$ contains the empty set and is closed under pairwise intersections and unions. Let $K$ be a compact system of $\mathcal{K}$ which is also closed under pairwise intersections. If a set $s$ of $\mathcal{X} \times \mathcal{K}$ is capacitable with respect to the capacity $I_{\mathcal{X}}$ of Definition [Capacity.compFst](../part-02/def-capacity-compfst.md), then its projection on $\mathcal{X}$ is capacitable with respect to $I$.

## Depends on

- [IsCapacitable](../part-02/def-iscapacitable.md)
- [Capacity](../part-02/def-capacity.md)
- [Capacity.compFst](../part-02/def-capacity-compfst.md)
- [IsCompactSystem](../part-01/def-iscompactsystem.md)

## Proof depends on

- [fst_image_mem_countableInfClosure](lem-fst-image-mem-countableinfclosure.md)

## Lean

Formalized as [`MeasureTheory.IsCapacitable.fst`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsCapacitable.fst).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 575](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L575)
