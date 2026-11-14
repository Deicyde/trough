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

- [level-N-princ-cong-subgp](def-level-n-princ-cong-subgp.md)

## Lean

Formalized as [`ModularGroup.S`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularGroup.S), [`ModularGroup.T`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ModularGroup.T), [`α`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/α), [`β`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/β).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 25](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L25)
