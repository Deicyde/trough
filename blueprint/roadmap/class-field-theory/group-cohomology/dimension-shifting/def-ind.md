---
declaration: definition
origin: cited
lean: Representation.ind₁', Rep.ind₁'
statement: formalized
---

# ind'

There is a representation $\mathrm{ind}_1' (M)$ on the $R$-module of finitely supported functions $G \to_0 M$. The action of an element $g \in G$ on a function $f : G \to_0 M$ is given by

$$
(g \bullet f)(x) = g \bullet (f (xg)),\qquad
\text{i.e. }
g \bullet \mathrm{single}(g,m) = \mathrm{single}(xg^{-1}, g\bullet m).
$$

The map $\mathrm{ind}_1'$ is functorial in $M$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Representation.ind₁'`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.ind₁'), [`Rep.ind₁'`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.ind₁').

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1065](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1065)
