---
declaration: corollary
origin: cited
---

# 677-satisfy

The operation $\diamond$ satisfies 677.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the previous lemma and definition of $\diamond$, it suffices to show that $y < (x, (y \diamond x) \diamond y)$. Defining $z,u,v$ as before, this amounts to showing that $y < v$. We already have $v = (x,u)$, hence by [Properties of operation](op-prop.md) $x < v$. Also recall that $y$ is bounded by one of $x,z$, and $z$ is bounded by one of $y,u$. Since $u$ is also bounded by $v$, we obtain the claim.

## Sources

- [Equational Theories blueprint: chapter/677.tex, line 150](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/677.tex#L150)
