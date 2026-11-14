---
declaration: definition
origin: cited
lean: RestrictGermPredicate
statement: formalized
---

# restrict_germ_predicate

Let $X$ be a topological space, $A$ a subset of $X$, $Y$ a set and $P$ a local predicate on functions from $X$ to $Y$. The restriction of $P$ to $A$ is the local predicate $P_{|A}$ defined by the constraint that a function $f$ satisfies $P_{|A}$ at $x$ if $x ∈ A$ implies that $f$ satisfies $P$ near $x$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`RestrictGermPredicate`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RestrictGermPredicate).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 96](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L96)
