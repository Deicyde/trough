---
declaration: lemma
origin: cited
lean: EisensteinSeries.eisensteinSeries_SIF
statement: formalized
proof: formalized
---

# Ek-is-modular-form

For all $k$, $E_k\in M_k(\Gamma_1)$. Especially, we have

$$
E_k \left(-\frac{1}{z}\right) = z^k E_k(z).\qquad\text{(2)}
$$

## Depends on

- [Mk](def-mk.md)
- [Ek](def-ek.md)

## Proof

This follows from the fact that the sum converges absolutely. Now apply slash operator with $\gamma = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$ gives (2).

## Lean

Formalized as [`EisensteinSeries.eisensteinSeries_SIF`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/EisensteinSeries.eisensteinSeries_SIF).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 115](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L115)
