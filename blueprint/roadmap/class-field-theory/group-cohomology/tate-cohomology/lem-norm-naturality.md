---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: Rep.norm_comm, Rep.normNatTrans
---

# norm naturality

For every map $f : A \to B$ in $\mathbf{Rep}(R,G)$ we have a commuting square:

$$
\begin{array}{rcl}
A & \stackrel{f}\to & B \\[2mm]
N_G\downarrow && \downarrow N_G \\
A & \stackrel{f}\to & B
\end{array} .
$$

Equivalently, $N_G$ is an endomorphism of the forgetful functor $\mathbf{Rep}(R,G) \to \mathbf{Mod}(R)$.

## Depends on

- [norm](def-norm.md)

## Proof

For $m \in M$ we have

$$
f(N_G (m))
= f\left( \sum_{g \in G} g \bullet m\right)
= \sum_{g \in G} g \bullet f(m)
= N_G(f(m)).
$$

## Lean

Formalized as [`Rep.norm_comm`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.norm_comm), [`Rep.normNatTrans`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.normNatTrans).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 486](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L486)
