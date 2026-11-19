---
declaration: theorem
origin: cited
lean: Cayley.Pack.walk, Cayley.Pack.covered_of_check
statement: formalized
proof: formalized
---

# walk

If a tree is accepted on a box, then the box is covered.

## Depends on

- [split_cover](lem-split-cover.md)
- [gap_leaf_sound](../../boxes-and-leaf-certificates/gap-leaves/thm-gap-leaf-sound.md)
- [dom_leaf_sound](../../boxes-and-leaf-certificates/domain-leaves/thm-dom-leaf-sound.md)
- [bad](../../boxes-and-leaf-certificates/boxes/def-bad.md)

## Proof

Induction on the tree, using Lemma [split_cover](lem-split-cover.md) at the internal nodes and Theorems [gap_leaf_sound](../../boxes-and-leaf-certificates/gap-leaves/thm-gap-leaf-sound.md) and [dom_leaf_sound](../../boxes-and-leaf-certificates/domain-leaves/thm-dom-leaf-sound.md) at the leaves.

## Lean

Formalized as [`Cayley.Pack.walk`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.walk), [`Cayley.Pack.covered_of_check`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.covered_of_check).

## Sources

- [Noperthedron blueprint: chapters/main.tex, line 64](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/main.tex#L64)
