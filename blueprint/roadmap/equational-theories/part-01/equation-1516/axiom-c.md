---
declaration: proposition
origin: cited
---

# Obtaining Axioms A, C

One can find maps $L_x: G \to G$ for each “non-square” $x \in G'$, such that Axioms A, C hold.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We can work with a single $x \in G'$. Our task is to find a function $L_x$ for which

$$
L_x x = Sx\qquad\text{(4)}
$$

and

$$
L_{Sy} L_x L_x y = x\qquad\text{(5)}
$$

for all $y \in G$ (note that $L_{Sy}$ is already fully constructed).

Define a *seed* to be an injective partial function $L_x$ defined on finitely many values and satisfying (4), as well as (5) whenever $L_x L_x y$ is defined. If there is a $y \in G$ for which $L_x y$ is currently undefined, then by hypothesis $y$ is equal to $L_x z$ for at most one $z$. If such a $z$ exists, we set $L_x y$ to be an element of $\{ w: L_{Sz} w = x \}$ different from $y$ that is not already in the domain or range of $L_x$; we are able to do so thanks to the infinite surjectivity ([Base magma](1516-base.md) (ii)) and the fact that the domain and the range of $L_x$ are finite. If no such $z$ exists, we set $L_x y$ to be arbitrary element of $G$ not already in the domain or range. In either case, we see that the seed property is preserved. Starting from the seed in which $L_x$ is only defined on $x$ and maps it to $Sx$, we obtain the claim.

## Sources

- [Equational Theories blueprint: chapter/1516.tex, line 157](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1516.tex#L157)
