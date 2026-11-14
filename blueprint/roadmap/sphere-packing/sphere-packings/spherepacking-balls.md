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

- [Sphere packing in dimension 8 blueprint: subsections/sphere-packings.tex, line 11](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/sphere-packings.tex#L11)
