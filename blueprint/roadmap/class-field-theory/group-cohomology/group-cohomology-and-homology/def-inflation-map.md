---
declaration: definition
origin: cited
lean: groupCohomology.cochain_infl, groupCohomology.infl
statement: formalized
---

# inflation map

If $S$ is a normal subgroup of $G$, then we write $H^n(G/S,M^S)$ for the cohomology groups of the representation $M^S$ of $G/S$. If $f : (G/S)^n \to M^S$ is an element of $C^n(G/S,M^S)$, then we may “inflate” $f$ to a function $G^n \to M$. This inflation process defines a map of cochain complexes $C^\bullet(G/S,M^S) \to C^\bullet(G,M)$, and hence a map of cohomology groups, called the *inflation map*:

$$
\mathrm{infl} : H^n(G/S,M^H) \to H^n(G,M).
$$

More precisely, the inflation map is a morphism of functors from $H^n (G/S, -)\circ \mathbf{invar}$ to $H^n(G,-)$.

## Depends on

- [inflation restriction functors](def-inflation-restriction-functors.md)

## Lean

Formalized as [`groupCohomology.cochain_infl`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.cochain_infl), [`groupCohomology.infl`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.infl).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 189](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L189)
