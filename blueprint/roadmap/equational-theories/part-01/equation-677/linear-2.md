---
declaration: lemma
origin: cited
---

# No counterexamples via linear extension

Suppose that we have a magma with carrier $G \times M$ satisfying 677, where $G$ already is a magma satisfying 677 and 255, $M$ is an abelian group, and the multiplication operation on $G \times M$ is of the form

$$
(x,s) \diamond (y,t) = (x \diamond y, \alpha_{x,y} s + \beta_{x,y} t + c_{x,y})
$$

for some endomorphisms $\alpha_{x,y},\beta_{x,y}: M \to M$ and constants $c_{x,y}$. Then $G \times M$ satisfies 255.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By [Basic properties of 677 magma](677-basic.md), it suffices to show that for any $(y,t)$, the equation $(x,s) \diamond (y,t) = (y,t)$ is solvable. Since $G$ already satisfies 255, we know that we can find $x$ such that $x \diamond y = y$, so it suffices to show that the operation $s \mapsto \alpha_{x,y} s + \beta_{x,y} t + c_{x,y}$ is surjective, or equivalently injective. If this were not the case, then we could find $s,s'$ such that $\alpha_{x,y} s = \alpha_{x,y} s'$, and hence $L_{(x,s)} (y,t') = L_{(x,s')} (y,t')$ for all $t' \in M$. Since

$$
x \diamond y = y = x \diamond (y \diamond ((x \diamond y) \diamond x))
$$

from [(1)](README.md), we have $y = y \diamond ((x \diamond y) \diamond x)$, and hence $L_{(y,t)} L_{L_{(x,s)} (y,t)} (x,s)$ is of the form $(y,t')$ for some $t'$, and similarly with $(x,s)$ replaced by $(x,s')$. We conclude that

$$
L_{(x,s)} L_{(y,t)} L_{L_{(x,s)} (y,t)} (x,s) = (y,t) =
L_{(x,s)} L_{(y,t)} L_{L_{(x,s)} (y,t)} (x,s')
$$

and hence by left invertibility $s=s'$, a contradiction.

## Sources

- [Equational Theories blueprint: chapter/677.tex, line 76](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/677.tex#L76)
