---
declaration: corollary
origin: cited
lean: Bialgebra.isDiagonalisable_iff_span_isGroupLikeElem_eq_top
statement: formalized
proof: formalized
---

# 0-is-diag-bialg-iff-span-group-like

A bialgebra over a domain is diagonalizable if and only if it is spanned by its group-like elements.

## Depends on

- [Diagonalizable bialgebras](0-is-diag-bialg.md)
- [Group-like elements](0-grp-like.md)

## Proof depends on

- [0-is-diag-bialg-group-like-span](0-is-diag-bialg-group-like-span.md)

## Proof

We know that a diagonalizable bialgebra is spanned by its group-like elements by [0-is-diag-bialg-group-like-span](0-is-diag-bialg-group-like-span.md), and that a bialgebra over a domain that is spanned by its group-like elements is diagonalizable by [Quotient of a diagonalisable bialgebra is diagonalisable](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-3-hopf-algebras.tex#L504) (and by the fact that a bijective morphism of bialgebras is an isomorphism).

## Lean

Formalized as [`Bialgebra.isDiagonalisable_iff_span_isGroupLikeElem_eq_top`](https://yaeldillies.github.io/toric/docs/find/#doc/Bialgebra.isDiagonalisable_iff_span_isGroupLikeElem_eq_top).

## Sources

- [Toric varieties blueprint: chapters/2-3-hopf-algebras.tex, line 527](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-3-hopf-algebras.tex#L527)
