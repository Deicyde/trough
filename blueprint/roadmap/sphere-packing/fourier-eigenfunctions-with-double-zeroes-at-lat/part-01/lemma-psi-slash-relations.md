---
declaration: lemma
origin: cited
lean: ψT_slash_T, ψS_slash_S, ψT_slash_S, ψS_slash_T, ψS_slash_ST, ψS_slash_TSTS
statement: formalized
---

# psi-slash-relations

We have

$$
\begin{aligned}
\psi_T|_{-2}T &= \psi_I, & \text{i.e.}\quad \psi_I(z) &= \psi_T(z+1),\qquad\text{(24)}\\
\psi_S|_{-2}S &= \psi_I, & \psi_I(z) &= z^2\,\psi_S(-1/z),\qquad\text{(25)}\\
\psi_T|_{-2}S &= -\psi_T, & -\psi_T(z) &= z^2\,\psi_T(-1/z),\qquad\text{(26)}\\
\psi_S|_{-2}T &= -\psi_S, & -\psi_S(z) &= \psi_S(z+1),\qquad\text{(27)}\\
\psi_S|_{-2}ST &= \psi_T, & \psi_T(z) &= (z+1)^2\,\psi_S\!\left(\frac{-1}{z+1}\right),\qquad\text{(28)}\\
\psi_S|_{-2}TSTS &= \psi_T, & \psi_T(z) &= (z-1)^2\,\psi_S\!\left(\frac{-1}{z-1}\right).\qquad\text{(29)}\end{aligned}
$$

## Depends on

- [psiI-psiT-psiS](def-psii-psit-psis.md)
- [psi-explicit](lemma-psi-explicit.md)

## Lean

Stated as [`ψT_slash_T`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψT_slash_T), [`ψS_slash_S`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψS_slash_S), [`ψT_slash_S`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψT_slash_S), [`ψS_slash_T`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψS_slash_T), [`ψS_slash_ST`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψS_slash_ST), [`ψS_slash_TSTS`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψS_slash_TSTS); the blueprint marks no proof of it as formalized.

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 541](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L541)
