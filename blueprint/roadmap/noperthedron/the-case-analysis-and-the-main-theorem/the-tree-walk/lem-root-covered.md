---
declaration: lemma
origin: cited
lean: Cayley.Pack.root_covered, Cayley.K.holes
statement: formalized
proof: formalized
---

# root_covered

If the skeleton is accepted on a root box when holes count as passing, its holes are exactly the boxes of the listed subtrees, and every listed subtree is accepted on its box, then the root box is covered.

## Depends on

- [walk](thm-walk.md)

## Proof

A bad point of the root box lies in a hole, by the same induction as Theorem [walk](thm-walk.md), and the hole's box is covered.

## Lean

Formalized as [`Cayley.Pack.root_covered`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.root_covered), [`Cayley.K.holes`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.holes).

## Sources

- [Noperthedron blueprint: chapters/main.tex, line 81](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/main.tex#L81)
