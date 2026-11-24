---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: groupCohomology.coindIso, groupHomology.indIso
---

# Shapiro's Lemma

Let $S$ be a subgroup of $G$. Then there are isomorphisms for all $n \ge 0$:

$$
H^n(G,\mathrm{coind}_S(M)) \cong H^n(S,M), \qquad
H_n(G,\mathrm{ind}_S(M)) \cong H_n(S,M), \qquad
$$

More precisely these are isomorphisms of functors.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is already in Mathlib.

## Lean

Formalized as [`groupCohomology.coindIso`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.coindIso), [`groupHomology.indIso`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupHomology.indIso).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 688](https://github.com/kbuzzard/ClassFieldTheory/blob/1e7f5dbe38358bd37a0643bb0db2dd3a436e6cb7/blueprint/src/_2_cohomology.tex#L688)
