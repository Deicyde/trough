---
declaration: theorem
origin: cited
lean: rupert_iff_rupert_set
statement: formalized
proof: formalized
---

# Rupert Polyhedron iff Rupert Set

The convex polyhedron with vertex set $V$ is Rupert if and only if the convex hull of $V$ is a Rupert set, i.e. there is a pose (two rotations and an offset) under which the closure of the inner shadow lies in the interior of the outer shadow.

## Depends on

- [rupert](../def-rupert.md)

## Proof

The convex hull of a finite set is compact, so its shadow is closed.

## Lean

Formalized as [`rupert_iff_rupert_set`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/rupert_iff_rupert_set).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 29](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/prelims.tex#L29)
