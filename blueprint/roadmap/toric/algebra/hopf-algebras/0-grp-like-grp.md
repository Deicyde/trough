---
declaration: proposition
origin: cited
lean: GroupLike.instGroup, GroupLike.instCommGroup
statement: formalized
proof: formalized
---

# Group-like elements form a group

Group-like elements $\operatorname{GrpLike} A$ of a bialgebra $A$ form a monoid.

Group-like elements $\operatorname{GrpLike} A$ of a Hopf algebra $A$ form a group.

## Depends on

- [Group-like elements](0-grp-like.md)

## Proof

Check that group-like elements are closed under unit, multiplication and inverses.

## Lean

Formalized as [`GroupLike.instGroup`](https://yaeldillies.github.io/toric/docs/find/#doc/GroupLike.instGroup), [`GroupLike.instCommGroup`](https://yaeldillies.github.io/toric/docs/find/#doc/GroupLike.instCommGroup).

## Sources

- [Toric varieties blueprint: chapters/2-3-hopf-algebras.tex, line 252](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-3-hopf-algebras.tex#L252)
