---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: groupHomology.inhomogeneousChains, groupHomology, groupHomology.chainsMap, groupHomology.map
---

# group homology

There is also a chain complex of $R$-modules:

$$
\cdots \stackrel{d_2}\to C_2(G,M) \stackrel{d_1}\to C_1(G,M) \stackrel{d_0}\to C_0(G,M)
$$

whose $n$-th term is the space of finitely supported functions $f : G^n \to_0 M$, with appropriately defined boundary maps $d_n$. In the literature $C_n(G,M)$ is often defined as $R[G]^{\otimes n} \otimes_R M$, to which it is canonically isomorphic. In the case $n=0$ this is interpreted as meaning $C_0(G,M) = M$. The homology groups of $C_n(G,M)$ are called the *homology groups of $M$* and are written $H_n(G,M)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`groupHomology.inhomogeneousChains`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupHomology.inhomogeneousChains), [`groupHomology`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupHomology), [`groupHomology.chainsMap`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupHomology.chainsMap), [`groupHomology.map`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupHomology.map).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 316](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L316)
