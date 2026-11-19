---
declaration: definition
origin: cited
lean: Representation.coind₁, Rep.coind₁, Rep.ind₁
statement: formalized
---

# induced

Let $G$ be a group, $R$ a commutative ring and $A$ an $R$-module.

- There is a representation of $G$ over $R$ on the space of all functions $f : G \to A$. The action of an element $g \in G$ on $f$ is defined by

    $$
    (g \bullet f) (x) = f(xg).
    $$

    This representation is called the coinduced representation and is denoted $\mathrm{coind}_1(G,A)$.

- There is a representation of $G$ over $R$ on the space of all finitely supported functions $f : G \to_0 A$. The action of an element $g \in G$ on $f$ is defined by

    $$
    (g \bullet f) (x) = f(xg), \qquad i.e.\;
    g \bullet \mathrm{single}(x,m) = \mathrm{single}(xg^{-1},m).
    $$

    This representation is called the induced representation and is denoted $\mathrm{ind}_1(G,A)$.

More precisely, $\mathrm{coind}_1(G,-)$ and $\mathrm{ind}_1(G,-)$ are both functors from $\mathbf{Mod}(R)$ to $\mathbf{Rep}(R,G)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Representation.coind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.coind₁), [`Rep.coind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.coind₁), [`Rep.ind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.ind₁).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 709](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L709)
