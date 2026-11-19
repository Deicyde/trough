---
declaration: proposition
origin: cited
lean: finite_addIrreducible
statement: formalized
proof: formalized
---

# A salient finitely generated monoid has finitely many irreducible elements

If $M$ is a finitely generated monoid with a single unit, then only finitely many elements of $M$ are irreducible.

## Depends on

- [Irreducible element](0-irred.md)

## Proof depends on

- [Irreducible elements lie in all sets generating a salient monoid](0-irred-subset-gen.md)

## Proof

Let $S$ be a finite set generating $M$. Write $I$ the set of irreducible elements. By Proposition [Irreducible elements lie in all sets generating a salient monoid](0-irred-subset-gen.md), $I \subseteq S$. Hence $I$ is finite.

## Lean

Formalized as [`finite_addIrreducible`](https://yaeldillies.github.io/toric/docs/find/#doc/finite_addIrreducible).

## Sources

- [Toric varieties blueprint: chapters/2-2-affine-monoids.tex, line 99](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-2-affine-monoids.tex#L99)
