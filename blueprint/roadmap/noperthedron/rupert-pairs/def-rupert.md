---
declaration: definition
origin: cited
lean: IsRupert
statement: formalized
---

# rupert

A convex polyhedron with vertex set $V$ is *Rupert* if there are rotations $R_i, R_o \in SO(3)$ and an offset $o \in \operatorname{\mathbb{R}}^2$ such that

$$
o + \pi(R_i \mathsf{Co}(V)) \subseteq \operatorname{int} \pi(R_o \mathsf{Co}(V)).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`IsRupert`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/IsRupert).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 7](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/prelims.tex#L7)
