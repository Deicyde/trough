---
declaration: definition
origin: cited
lean: Rep.split.FiniteClassFormation
statement: formalized
---

# fundamental class

In this section $G$ is a finite group and $R$ is a commutative ring. If $M$ is a representation of $G$ over $R$ then we shall call $M$ (or more precisely the triple $(R,G,M)$) a *finite class formation* if:

- The ring $R$ has no additive torsion. This implies for all subgroups $S$ of $G$:

    $$
    H^2(S,\mathrm{aug}(R,G)) \cong H^1(S,R) \cong \mathrm{Hom}(S,R) = 0.
    $$

- For all subgroups $S \le G$ we have $H^1(S,M) \cong 0$.

- For all subgroups $S \le G$, $H^2(S,M)$ is isomorphic as an $R$-module to $R / |S| \cdot R$.

If $M$ is a finite class formation then a generator $\sigma$ for $H^2(G,M)$ (by which we mean the image of 1 under some isomorphism $R/|G|R\equiv H^2(G,M)$) is called a *fundamental class*.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Rep.split.FiniteClassFormation`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.split.FiniteClassFormation).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1990](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1990)
