---
declaration: lemma
origin: cited
lean: Cayley.step_orbit
statement: formalized
proof: formalized
---

# step_orbit

If $(s, R_i)$ is a Rupert pair with $R_i \in SO(3)$, then there is a Rupert pair $(s, s\,Q)$ with $Q \in SO(3)$ and $F(H^e Q g_k) \le F(Q)$ for all $e$ and $k$.

## Depends on

- [Symmetries](../moves-that-preserve-rupert-pairs/lem-move-sym.md)
- [Inner half-turn](../moves-that-preserve-rupert-pairs/lem-move-halfturn.md)
- [orbit_score](def-orbit-score.md)

## Proof

Take the element of the finite orbit of $s^T R_i$ with the largest score; it is reached by the moves of Lemmas [Symmetries](../moves-that-preserve-rupert-pairs/lem-move-sym.md) and [Inner half-turn](../moves-that-preserve-rupert-pairs/lem-move-halfturn.md), and the orbit of a member of the orbit is the same orbit.

## Lean

Formalized as [`Cayley.step_orbit`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.step_orbit).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 157](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L157)
