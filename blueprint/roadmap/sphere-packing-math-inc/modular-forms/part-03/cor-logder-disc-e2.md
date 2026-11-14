---
declaration: corollary
origin: cited
lean: D_Delta_eq_E₂_mul_Delta
statement: formalized
proof: formalized
---

# logder-disc-E2

$$
\Delta' = E_2 \Delta.\qquad\text{(44)}
$$

## Depends on

- [ramanujan-formula](thm-ramanujan-formula.md)
- [disc-definition](../part-01/def-disc-definition.md)

## Proof

By Ramanujan's formula [(37)](thm-ramanujan-formula.md) and [(38)](thm-ramanujan-formula.md),

$$
\Delta' = \frac{3 E_4^2 E_4' - 2 E_6 E_6'}{1728} = \frac{1}{1728} \left(3 E_4^2 \cdot \frac{E_2 E_4 - E_6}{3} - 2 E_6 \cdot \frac{E_2 E_6 - E_4^2}{2}\right) = \frac{E_2(E_4^3 - E_6^2)}{1728} = E_2\Delta.
$$

## Lean

Formalized as [`D_Delta_eq_E₂_mul_Delta`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/D_Delta_eq_E₂_mul_Delta).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 632](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L632)
