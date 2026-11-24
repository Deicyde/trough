---
declaration: lemma
origin: cited
lean: EisensteinSeries.eisensteinSeriesSIF
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

Formalized as [`EisensteinSeries.eisensteinSeriesSIF`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/EisensteinSeries.eisensteinSeriesSIF).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 117](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/modular-forms.tex#L117)
