---
declaration: definition
origin: cited
lean: ModularGroup.S, ModularGroup.T, α, β
statement: formalized
---

# Gamma-generators

Define the matrices

$$
S = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in \Gamma_1,
T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \in \Gamma_1,
\alpha = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \in \Gamma_2 \subset \Gamma_1,
\beta = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} \in \Gamma_2 \subset \Gamma_1.
$$

It is easily verifiable that $\alpha = T^2$ and $\beta = -S\alpha^{-1}S = -ST^{-2}S$.

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`ModularGroup.S`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularGroup.S), [`ModularGroup.T`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularGroup.T), [`α`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/α), [`β`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/β).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 26](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L26)
