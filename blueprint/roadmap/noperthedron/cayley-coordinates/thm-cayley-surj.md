---
declaration: theorem
origin: cited
lean: Cayley.exists_cayleyMatrix_of_trace_nonneg
statement: formalized
proof: formalized
---

# cayley_surj

Every $A \in SO(3)$ with $\operatorname{\mathrm{tr}} A \ge 0$ is $\mathrm{Cay}(r)$ for some $r$ with $|r|^2 \le 3$.

## Depends on

- [cayley_so3](lem-cayley-so3.md)

## Proof depends on

- [Axis-angle form](lem-axis-angle.md)
- [Rodrigues form](lem-cayley-rodrigues.md)

## Proof

Write $A$ as a rotation by angle $\gamma \in (-\pi, \pi]$ about a unit axis $a$ (Lemma [Axis-angle form](lem-axis-angle.md)). Then $\operatorname{\mathrm{tr}} A = 1 + 2 \cos\gamma \ge 0$ gives $\cos\gamma \ge -1/2$. Put $c = \sin\gamma / (1 + \cos\gamma) = \tan(\gamma/2)$ and $r = c\,a$. Then $c^2 = (1 - \cos\gamma)/(1 + \cos\gamma) \le 3$, and comparing the Rodrigues forms of $A$ and of $\mathrm{Cay}(r)$ gives $A = \mathrm{Cay}(r)$.

## Lean

Formalized as [`Cayley.exists_cayleyMatrix_of_trace_nonneg`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.exists_cayleyMatrix_of_trace_nonneg).

## Sources

- [Noperthedron blueprint: chapters/cayley.tex, line 79](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/cayley.tex#L79)
