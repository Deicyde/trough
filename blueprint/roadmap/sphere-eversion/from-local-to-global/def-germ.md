---
declaration: definition
origin: cited
lean: Filter.Germ
statement: formalized
---

# germ

Let $X$ be a topological space, $x$ a point in $X$ and $Y$ a set. A germ of function from $X$ to $Y$ at $x$ is an element of the quotient $(X → Y)_x$ of the set of functions from $X$ to $Y$ by the relation $f ∼ g$ if $f$ and $g$ coincide near $x$. The image of a function $f$ in this quotient will be denoted by $[f]_x$.

A local predicate on functions from $X$ to $Y$ is a family $P$ of predicates on the germ set $(X → Y)_x$ for every $x$ in $X$. We say that a function $f$ satisfies $P$ at $x$ if $P [f]_x$ holds, and $f$ satisfies $P$ if it satisfies $P$ at every point.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Filter.Germ`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/Filter.Germ).

## Sources

- [Sphere eversion blueprint: local_to_global.tex, line 76](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/local_to_global.tex#L76)
