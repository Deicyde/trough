---
declaration: lemma
origin: cited
lean: Bialgebra.span_isGroupLikeElem_eq_top_of_isDiagonalisable
statement: formalized
proof: formalized
---

# 0-is-diag-bialg-group-like-span

A diagonalizable bialgebra is spanned by its group-like elements.

## Depends on

- [Diagonalizable bialgebras](0-is-diag-bialg.md)
- [Group-like elements](0-grp-like.md)

## Proof depends on

- [0-grp-like-grp-alg-span](0-grp-like-grp-alg-span.md)

## Proof

This is true for a group algebra by [0-grp-like-grp-alg-span](0-grp-like-grp-alg-span.md), and the property of being spanned by its group-like elements is preserves by isomorphisms of bialgebras.

## Lean

Formalized as [`Bialgebra.span_isGroupLikeElem_eq_top_of_isDiagonalisable`](https://yaeldillies.github.io/toric/docs/find/#doc/Bialgebra.span_isGroupLikeElem_eq_top_of_isDiagonalisable).

## Sources

- [Toric varieties blueprint: chapters/2-3-hopf-algebras.tex, line 465](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-3-hopf-algebras.tex#L465)
