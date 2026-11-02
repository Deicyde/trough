---
declaration: theorem
origin: cited
---

# The fundamental property of invariants

Let $E$ and $E'$ be equations involving a set of variables $X$, and let $G$ be a lifting magma family.

If $E$ is true with the substitution $\iota_X$, and $E$ implies $E'$, then so is $E'$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Applying the evaluation [Evaluation theorem for lifting magma families](lifting-magma-basis-evaluation.md), we see that $E$ is satisfied by $G_X$. Since $E$ implies $E'$, $E'$ is also satisfied by $G_X$, and in particular, $E'$ is true with the substitution $\iota_X$.

## Sources

- [Equational Theories blueprint: chapter/metatheorems_from_invariants.tex, line 144](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/metatheorems_from_invariants.tex#L144)
