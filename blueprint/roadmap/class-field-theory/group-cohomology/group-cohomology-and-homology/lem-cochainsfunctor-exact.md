---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: groupCohomology.map_cochainsFunctor_shortExact
---

# cochainsFunctor exact

The functor taking $M$ to $C^\bullet (G,M)$ is exact. I.e. if $0 \to A \to B \to C \to 0$ is a short exact sequence in $\mathbf{Rep}(R,G)$. Then the corresponding sequence of cochain complexes is exact:

$$
0 \to C^\bullet(G,A) \to C^\bullet(G,B) \to C^\bullet(G,C) \to 0.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is already in Mathlib.

## Lean

Formalized as [`groupCohomology.map_cochainsFunctor_shortExact`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.map_cochainsFunctor_shortExact).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 209](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L209)
