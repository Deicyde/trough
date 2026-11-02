---
declaration: lemma
origin: cited
lean: QuotientGroup.mk_image_finite_of_compact_of_open
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/563
---

# QuotientGroup.mk\_image\_finite\_of\_compact\_of\_open

If $U$ and $V$ are compact subgroups of a topological group $G$, if $V$ is also open, and if $g\in G$, then the double coset space $UgV$ is a finite union of left cosets $g_iV$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The subset $UgV$ of $G$ is a continuous image of the compact set $U\times V$ and is hence compact, and it is covered by the disjoint left cosets $g_iV$; this cover must thus be finite.

## Lean

Formalized as [`QuotientGroup.mk_image_finite_of_compact_of_open`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/QuotientGroup.mk_image_finite_of_compact_of_open).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HeckeOperatorProject.tex, line 97](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HeckeOperatorProject.tex#L97)
