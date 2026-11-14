---
declaration: corollary
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.IsSetSemiring.exists_disjoint_finset_diff_eq
---

# semiRingOfSets_subtractUnion

Suppose that $C$ is a semi-ring of sets, and let $A_k \in C$, $k \in \{1, ..., n\}$, and $B\in C$ . Then there exists a family of pairwise disjoint sets $B_j \in C$, $j \in \{1, ..., m\}$, such that

$$
B\setminus\bigcup_{k=1}^n A_k = \bigcup_{j=1}^m B_j.
$$

## Depends on

- [Semi-ring of sets](def-semiringofsets.md)

## Proof depends on

- [semiRingOfSets_disjoint_of_union](lem-semiringofsets-disjoint-of-union.md)

## Proof

This is easily done by induction on $n$, thanks to the Lemma [semiRingOfSets_disjoint_of_union](lem-semiringofsets-disjoint-of-union.md).

## Lean

Formalized as [`MeasureTheory.IsSetSemiring.exists_disjoint_finset_diff_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsSetSemiring.exists_disjoint_finset_diff_eq).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 36](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L36)
