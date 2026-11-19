---
declaration: lemma
origin: cited
lean: Cayley.BalancedSupport.exists_axisAngle, Cayley.BalancedSupport.AxisAngle.apply_sub_exact, Cayley.BalancedSupport.AxisAngle.first_inner_eq, Cayley.BalancedSupport.AxisAngle.matrix_trace_eq
statement: formalized
proof: formalized
---

# Axis-angle form

Every $A \in SO(3)$ is a rotation by some angle $\gamma \in (-\pi, \pi]$ about some unit axis $a$: $A v - v = \sin\gamma\; a \times v + (1 - \cos\gamma)\; a \times (a \times v)$. Its trace is $1 + 2\cos\gamma$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Every element of $SO(3)$ is orthogonally conjugate to a rotation $R_z(\gamma)$ about the $z$-axis; transport the formula for $R_z(\gamma)$ along the conjugating frame.

## Lean

Formalized as [`Cayley.BalancedSupport.exists_axisAngle`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.BalancedSupport.exists_axisAngle), [`Cayley.BalancedSupport.AxisAngle.apply_sub_exact`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.BalancedSupport.AxisAngle.apply_sub_exact), [`Cayley.BalancedSupport.AxisAngle.first_inner_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.BalancedSupport.AxisAngle.first_inner_eq), [`Cayley.BalancedSupport.AxisAngle.matrix_trace_eq`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.BalancedSupport.AxisAngle.matrix_trace_eq).

## Sources

- [Noperthedron blueprint: chapters/cayley.tex, line 97](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/cayley.tex#L97)
