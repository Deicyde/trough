---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: Matrix.posSemidef_gram
---

# posSemidef_gramMatrix

A gram matrix is positive semidefinite.

## Depends on

- [Gram matrix](def-grammatrix.md)

## Proof

Symmetry is obvious from the definition. Let $x \in E$. Then

$$
\begin{aligned}
\langle x, G x \rangle
&= \sum_{i,j} x_i x_j \langle v_i, v_j \rangle
\\
&= \langle \sum_i x_i v_i, \sum_j x_j v_j \rangle
\\
&= \left\Vert \sum_i x_i v_i \right\Vert^2
\\
&\ge 0
\: .
\end{aligned}
$$

## Lean

Formalized as [`Matrix.posSemidef_gram`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Matrix.posSemidef_gram).

## Sources

- [Brownian motion blueprint: chapters/projective_family.tex, line 55](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/projective_family.tex#L55)
