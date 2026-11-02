---
declaration: definition
origin: cited
lean: Magma
statement: formalized
---

# Magma

A *magma* is a set $G$ equipped with a binary operation $\diamond: G \times G \to G$. A *homomorphism* $\varphi : G \to H$ between two magmas is a map such that $\varphi(x \diamond y) = \varphi(x) \diamond \varphi(y)$ for all $x,y \in G$. An *isomorphism* is an invertible homomorphism.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Magma`](https://teorth.github.io/equational_theories/docs/find/#doc/Magma).

## Sources

- [Equational Theories blueprint: chapter/intro.tex, line 2](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/intro.tex#L2)
