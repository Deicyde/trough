---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: Representation.norm, Rep.tateNorm
---

# norm

Let $G$ be a finite group and $M$ a representation of $G$ over a commutative ring $R$. There is a canonical linear map $N_G : M \to M$ called the *norm*, defined by

$$
N_G(m) = \sum_{g \in G} g \bullet m.
$$

We shall also regard the norm as a linear map from $C_0(G,M)$ to $C^0(G,M)$, both of which may be identified with $M$.

(We'll see in the next lemma that $N_G$ commutes with the action of $G$, so is a morphism in $\mathbf{Rep}(R,G)$. However, we shall only regard it as a morphism in $\mathbf{Mod}(R)$. The reason is that the chain and cochain modules $C^0(G,M)$ and $C_0(G,M)$ are regarded as $R$-modules rather than representations of $G$.)

## Depends on

- [group homology](../group-cohomology-and-homology/def-group-homology.md)

## Lean

Formalized as [`Representation.norm`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.norm), [`Rep.tateNorm`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.tateNorm).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 407](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L407)
