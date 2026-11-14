---
declaration: lemma
origin: cited
lean: IsGroupLikeElem.map
statement: formalized
proof: formalized
---

# Bialgebra homs preserve group-like elements

Let $f : A \to B$ be a bi-algebra hom. If $a \in A$ is group-like, then $f(a)$ is group-like too.

## Depends on

- [Group-like elements](0-grp-like.md)

## Proof

$a$ is a unit, so $f(a)$ is a unit too. Then

$$
f(a) \otimes f(a) = (f \otimes f)(\Delta_A(a)) = \Delta_B(f(a))
$$

so $f(a)$ is group-like.

## Lean

Formalized as [`IsGroupLikeElem.map`](https://yaeldillies.github.io/toric/docs/find/#doc/IsGroupLikeElem.map).

## Sources

- [Toric varieties blueprint: chapters/2-3-hopf-algebras.tex, line 270](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-3-hopf-algebras.tex#L270)
