---
declaration: lemma
origin: cited
lean: Cayley.θ₁_eq, Cayley.cos_θ₁_bounds, Cayley.sin_θ₁_bounds
statement: formalized
proof: formalized
---

# theta1

Let $\theta_1 = 2\pi/15$. Then $\theta_1 = \pi/3 - \pi/5$, and $\cos\theta_1$ and $\sin\theta_1$ are known to $28$ decimal places.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

$\cos(\pi/5) = (1 + \sqrt5)/4$ and $\sin(\pi/5) = \sqrt{10 - 2\sqrt5}/4$; expand $\cos$ and $\sin$ of the difference, and bound $\sqrt3$, $\sqrt5$ by rationals.

## Lean

Formalized as [`Cayley.θ₁_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.θ₁_eq), [`Cayley.cos_θ₁_bounds`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cos_θ₁_bounds), [`Cayley.sin_θ₁_bounds`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.sin_θ₁_bounds).

## Sources

- [Noperthedron blueprint: chapters/data.tex, line 8](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/data.tex#L8)
