---
declaration: theorem
origin: cited
lean: rupert_implies_rot_rupert
statement: formalized
proof: formalized
---

# rupert_implies_rot_rupert

Let $S \subseteq \operatorname{\mathbb{R}}^3$ be point-symmetric and convex. If a pose with offset $o$ passes $S$ through itself, then so does the same pose with offset $0$.

## Depends on

- [pointsymmetric](../../the-noperthedron/definition-of-the-noperthedron/def-pointsymmetric.md)

## Proof

Write $K$ for the closure of the inner shadow and $L$ for the interior of the outer shadow; both are point-symmetric and $L$ is convex. From $o + K \subseteq L$ and symmetry, $-o + K = -(o + K) \subseteq L$. Every $k \in K$ is the midpoint of $o + k \in L$ and $-o + k \in L$, so $k \in L$ by convexity.

## Lean

Formalized as [`rupert_implies_rot_rupert`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/rupert_implies_rot_rupert).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 43](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/prelims.tex#L43)
