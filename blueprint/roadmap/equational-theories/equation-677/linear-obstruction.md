---
declaration: lemma
origin: cited
---

# No linear counterexamples

Suppose we have a finite magma $M$ satisfying 677 which is linear in the sense that $M$ is an abelian group and $x \diamond y = \alpha x + \beta y + c$ for some endomorphisms $\alpha,\beta: M \to M$ and constant $c$. Then $M$ satisfies 255.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the previous lemma, it suffices to show that right multiplication $R_x$ is surjective, or equivalently injective by finiteness. If this is not the case, then we can find distinct $y,y'$ such that $R_x y = R_x y'$, hence $L_y x = L_{y'} x$. But in this linear model, $L_y$ and $L_{y'}$ differ by a constant, hence we have $L_y = L_{y'}$. Applying 677-alt we have

$$
L_y L_x L_{L_y x} y = x =  L_y L_x L_{L_y x} y'
$$

and hence by left-invertibility $y=y'$, a contradiction.

## Sources

- [Equational Theories blueprint: chapter/677.tex, line 66](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/677.tex#L66)
