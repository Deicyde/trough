---
declaration: definition
origin: cited
lean: convexHull
statement: formalized
---

# Convex hull

For a set $S \subseteq N$, the **convex hull of $S$** is

$$
\operatorname{Conv}(S) := \left\{\sum_{u \in S} \lambda_u | \lambda_u \ge 0, \sum_u \lambda_u = 1\right\}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`convexHull`](https://yaeldillies.github.io/toric/docs/find/#doc/convexHull).

## Sources

- [Toric varieties blueprint: chapters/3-1-cones.tex, line 29](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/3-1-cones.tex#L29)
