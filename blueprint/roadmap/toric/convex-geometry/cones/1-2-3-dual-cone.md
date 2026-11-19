---
declaration: definition
origin: cited
lean: PointedCone.dual
statement: formalized
---

# Dual cone

Given a polyhedral cone $\sigma \subseteq N$, its **dual cone** is defined by

$$
\sigma^\vee = \{m \in M | \forall u \in \sigma, \langle m, u\rangle \ge 0\}.
$$

## Depends on

- [Convex hull](1-2-2-convex-hull.md)

## Lean

Formalized as [`PointedCone.dual`](https://yaeldillies.github.io/toric/docs/find/#doc/PointedCone.dual).

## Sources

- [Toric varieties blueprint: chapters/3-1-cones.tex, line 53](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/3-1-cones.tex#L53)
