---
declaration: definition
origin: cited
lean: groupCohomology.rest
statement: formalized
---

# restriction map

If $S$ is a subgroup of $G$, then we write $H^n(S,M)$ for the cohomology groups of the restricted representation $M \downarrow S$. If $f : G^n \to M$ is an element of $C^n(G,M)$, then we may restrict $f$ to a function $S^n \to M$. Restricting functions in this way defines a map of cochain complexes $C^\bullet(G,M) \to C^\bullet(S,M)$, and hence a map of cohomology groups

$$
\mathrm{rest} : H^n(G,M) \to H^n(S,M).
$$

This map is called the *restriction map*, and is a morphism of functors from $H^n(G,-)$ to $H^n(S, -) \circ \mathbf{res}$.

## Depends on

- [inflation restriction functors](def-inflation-restriction-functors.md)

## Lean

Formalized as [`groupCohomology.rest`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupCohomology.rest).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 172](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L172)
