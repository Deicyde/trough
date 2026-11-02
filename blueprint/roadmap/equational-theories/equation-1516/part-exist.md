---
declaration: lemma
origin: cited
---

# Existence of partial solution

A partial solution exists.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We define $L_{c'} y$ for $y = (a,c,n) \in G'$ as follows:

- (i) If $c' = a$ and $n=0$, then $L_{c'} y := a$.
- (ii) If $c' = a$ and $n \neq 0$, then $L_{c'} y := (a,c,0)$.
- (iii) If $c' = c_{y,b}$ for some $b$, then $L_{c'} y := b$.
- (iv) In all other cases, $L_{c'} y$ is undefined.

We of course also define $L_{c'} y$ for $y \in \mathbb{Z}$ using [Base magma](1516-base.md).

From Lemma [Useful elements](aux.md) we see that this is a well-defined operation, with $L_c y$ undefined for any $y = (a,c,n) \in G'$. So properties (a)-(e) and (g) are clear from construction. Property (e) is also clear from construction in each of the three cases (i), (ii), (iii) (for (i), (ii) we also use the fact that $L_a a = a$).

## Sources

- [Equational Theories blueprint: chapter/1516.tex, line 106](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1516.tex#L106)
