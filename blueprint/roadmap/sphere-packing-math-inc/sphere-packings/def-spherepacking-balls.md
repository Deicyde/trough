---
declaration: definition
origin: cited
lean: SpherePacking.balls
statement: formalized
---

# SpherePacking.balls

Given a set $X \subset \mathbb{R}^d$ and a real number $r > 0$ (known as the *separation radius*) such that $\|x - y\| \geq r$ for all distinct $x, y \in X$, we define the *sphere packing* $\mathcal{P}(X)$ with centres at $X$ to be the union of all open balls of radius $r$ centred at points in $X$:

$$
\mathcal{P}(X) := \bigcup_{x \in X} B_d(x, r)
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`SpherePacking.balls`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SpherePacking.balls).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/sphere-packings.tex, line 11](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/sphere-packings.tex#L11)
