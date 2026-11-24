---
declaration: theorem
origin: cited
lean: Cayley.Pack.RootOK, Cayley.Pack.kernel_sound
statement: formalized
proof: formalized
---

# Soundness

If each of the 15 root boxes carries an accepted skeleton with accepted subtrees for its holes, then $\operatorname{\mathbf{P}}$ is not Rupert.

## Depends on

- [Reduction](../../the-reduction/the-reduced-domain/thm-reduction.md)
- [Coverage](../root-boxes/lem-cover.md)
- [root_covered](../the-tree-walk/lem-root-covered.md)

## Proof

If $\operatorname{\mathbf{P}}$ were Rupert, Theorem [Reduction](../../the-reduction/the-reduced-domain/thm-reduction.md) would give a reduced $(u, v, j, r)$ with a Rupert pair. By Lemma [Coverage](../root-boxes/lem-cover.md) it is a point of a root box, where it would be a bad point. Lemma [root_covered](../the-tree-walk/lem-root-covered.md) says there is none.

## Lean

Formalized as [`Cayley.Pack.RootOK`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.RootOK), [`Cayley.Pack.kernel_sound`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.kernel_sound).

## Sources

- [Noperthedron blueprint: chapters/main.tex, line 98](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/main.tex#L98)
