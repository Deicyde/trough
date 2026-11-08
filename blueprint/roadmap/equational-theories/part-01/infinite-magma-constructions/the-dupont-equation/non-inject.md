---
declaration: corollary
origin: cited
lean: Eq63.Equation63_not_implies_Equation1692
statement: formalized
---

# Non-injective Dupont solution

The Dupont equation admits non-injective solutions, and hence can violate Equation 1692.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

It suffices to find a partial solution that violates injectivity. This can be done for instance by adjoining $\{-13, 10\}$ to $E_0$ and defining $f(10)= 2 = f(6)$, $f(-13)=-10$, and performing a finite check to verify that this is still a partial solution.

## Lean

Stated as [`Eq63.Equation63_not_implies_Equation1692`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq63.Equation63_not_implies_Equation1692); the blueprint does not mark its proof formalized.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 850](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L850)
