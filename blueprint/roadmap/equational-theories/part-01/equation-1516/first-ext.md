---
declaration: lemma
origin: cited
---

# First extension

Suppose we have a partial solution for which $L_{c'} y$ is currently undefined for some $c' \in \mathbb{Z}$ and $y \in G$. Then one can extend this partial solution in such a manner that $L_{c'} y$ is now defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Write $y = (a,c,n)$. Because $L_a: \mathbb{Z} \to \mathbb{Z}$ and $L_{c'}: \mathbb{Z} \to \mathbb{Z}$ are surjective, we can find $b \in \mathbb{Z}$ such that $L_a L_{c'} b = c'$. If we had $b=c'$, then $L_a c' = c'$, which from [(1)](README.md) (and $Sc' = c'$) implies that $a = c'$, which contradicts the undefined nature of $L_{c'} y$ thanks to properties (b), (c) of a partial solution. Hence, $b \neq c'$. We then set $L_{c'} y := b$. It is then clear that all the properties (a)-(g) of a partial solution are maintained.

## Sources

- [Equational Theories blueprint: chapter/1516.tex, line 123](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1516.tex#L123)
