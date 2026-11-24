---
declaration: proposition
origin: cited
lean: AffineAddMonoid.embedding, AffineAddMonoid.embedding_injective
statement: formalized
proof: formalized
---

# Embedding an affine monoid inside a lattice

If $M$ is an affine monoid, then $M$ can be embedded inside ${\mathbb Z}^n$ for some $n$.

## Depends on

- [Affine monoid](0-aff-mon.md)

## Proof

Embed $M$ inside its Grothendieck group $G$. Prove that $G$ is finitely generated free.

## Lean

Formalized as [`AffineAddMonoid.embedding`](https://yaeldillies.github.io/toric/docs/find/#doc/AffineAddMonoid.embedding), [`AffineAddMonoid.embedding_injective`](https://yaeldillies.github.io/toric/docs/find/#doc/AffineAddMonoid.embedding_injective).

## Sources

- [Toric varieties blueprint: chapters/2-2-affine-monoids.tex, line 33](https://github.com/YaelDillies/toric/blob/97b1287db93f2eee84c8bb4e408058d9e721ce5b/blueprint/src/chapters/2-2-affine-monoids.tex#L33)
