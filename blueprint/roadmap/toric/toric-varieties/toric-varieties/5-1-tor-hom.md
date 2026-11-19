---
declaration: definition
origin: cited
lean: AlgebraicGeometry.ToricVariety
statement: formalized
---

# Torus morphisms, torus isomorphisms

Let $k$ be a field. Let $T_1, T_2$ be tori over $k$. Let $X_1, X_2$ be toric varieties with torus $T_1, T_2$ respectively. A *toric morphism* from $X_1$ to $X_2$ is the data of a $k$-morphism $X_1 \to X_2$ and a $k$-group homomorphism $T_1 \to T_2$ that commute with the embeddings $T_1 \to X_1, T_2 \to X_2$ and the actions. A *toric isomorphism* from $X_1$ to $X_2$ is the data of two isomorphisms $X_1 \cong X_2$ and $T_1 \cong T_2$ that commute with the embeddings $T_1 \to X_1, T_2 \to X_2$.

## Depends on

- [The split torus](../../scheme-theory/the-torus/0-torus.md)

## Lean

Formalized as [`AlgebraicGeometry.ToricVariety`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.ToricVariety).

## Sources

- [Toric varieties blueprint: chapters/5-1-toric-variety.tex, line 24](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/5-1-toric-variety.tex#L24)
