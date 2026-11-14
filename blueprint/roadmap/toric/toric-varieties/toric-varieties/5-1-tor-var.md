---
declaration: definition
origin: cited
lean: AlgebraicGeometry.ToricVariety
statement: formalized
---

# Toric varieties

Let $k$ be a field. Let $T$ be a torus over $k$. A *toric variety* structure on a scheme $X$ over $k$ consists the following data:

- a torus $T$ over $k$,
- a group action $T \times X \to X$ over $k$.
- a dominant open immersion $i : T \hookrightarrow X$ over $k$ that is $T$-equivariant.

## Depends on

- [The split torus](../../scheme-theory/the-torus/0-torus.md)

## Lean

Formalized as [`AlgebraicGeometry.ToricVariety`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.ToricVariety).

## Sources

- [Toric varieties blueprint: chapters/5-1-toric-variety.tex, line 7](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/5-1-toric-variety.tex#L7)
