---
declaration: lemma
origin: cited
lean: common_center
statement: formalized
proof: formalized
---

# Common centre

Let $K, L \subseteq \operatorname{\mathbb{R}}^2$ be point-symmetric and let $L$ be convex. If $o + K \subseteq L$ for some $o \in \operatorname{\mathbb{R}}^2$, then $K \subseteq L$.

## Depends on

- [pointsymmetric](../../the-noperthedron/definition-of-the-noperthedron/def-pointsymmetric.md)

## Proof

By symmetry, $-o + K = -(o + K) \subseteq L$. Every $k \in K$ is the midpoint of $o + k \in L$ and $-o + k \in L$, so $k \in L$ by convexity.

## Lean

Formalized as [`common_center`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/common_center).

## Sources

- [Noperthedron blueprint: chapters/prelims.tex, line 41](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/prelims.tex#L41)
