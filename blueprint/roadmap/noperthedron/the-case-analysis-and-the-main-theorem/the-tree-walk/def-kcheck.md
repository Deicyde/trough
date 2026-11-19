---
declaration: definition
origin: cited
lean: Cayley.K.KTree, Cayley.K.KBox.split, Cayley.K.kCheck
statement: formalized
---

# kcheck

A certificate tree has internal nodes that split a box in half along one coordinate, and leaves that are gap leaves or domain leaves. A tree is *accepted* on a box if every leaf passes on its sub-box.

## Depends on

- [gap_leaf](../../boxes-and-leaf-certificates/gap-leaves/def-gap-leaf.md)
- [dom_leaf](../../boxes-and-leaf-certificates/domain-leaves/def-dom-leaf.md)

## Lean

Formalized as [`Cayley.K.KTree`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.KTree), [`Cayley.K.KBox.split`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.KBox.split), [`Cayley.K.kCheck`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.kCheck).

## Sources

- [Noperthedron blueprint: chapters/main.tex, line 37](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/main.tex#L37)
