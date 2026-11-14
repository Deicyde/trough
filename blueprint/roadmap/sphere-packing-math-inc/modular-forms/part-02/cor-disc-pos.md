---
declaration: corollary
origin: cited
lean: Delta_imag_axis_pos
statement: formalized
proof: formalized
---

# disc-pos

$\Delta(it) > 0$ for all $t > 0$.

## Depends on

- [disc-definition](../part-01/def-disc-definition.md)

## Proof

By [disc-definition](../part-01/def-disc-definition.md), we have

$$
\Delta(it) = e^{-2 \pi t} \prod_{n \ge 1} (1 - e^{-2 \pi n t})^{24} > 0.
$$

## Lean

Formalized as [`Delta_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Delta_imag_axis_pos).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 239](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L239)
