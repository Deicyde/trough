---
declaration: corollary
origin: cited
lean: Δ_imag_axis_pos
statement: formalized
proof: formalized
---

# disc-pos

$\Delta(it) > 0$ for all $t > 0$.

## Depends on

- [disc-definition](def-disc-definition.md)

## Proof

By [disc-definition](def-disc-definition.md), we have

$$
\Delta(it) = e^{-2 \pi t} \prod_{n \ge 1} (1 - e^{-2 \pi n t})^{24} > 0.
$$

## Lean

Formalized as [`Δ_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Δ_imag_axis_pos).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 255](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L255)
