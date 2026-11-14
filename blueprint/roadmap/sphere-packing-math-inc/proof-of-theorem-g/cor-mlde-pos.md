---
declaration: corollary
origin: cited
lean: SerreDer_22_L₁₀_pos
statement: formalized
proof: formalized
---

# MLDE-pos

[(11)](lemma-fg-de.md) (resp. [(12)](lemma-fg-de.md)) is positive (resp. negative) on the (positive) imaginary axis.

## Depends on

- [FG-de](lemma-fg-de.md)
- [disc-pos](../modular-forms/part-02/cor-disc-pos.md)
- [theta-pos](../modular-forms/part-03/cor-theta-pos.md)
- [E2](../modular-forms/part-01/def-e2.md)

## Proof

From [(5)](../modular-forms/part-01/def-e2.md) and Lemma [disc-pos](../modular-forms/part-02/cor-disc-pos.md),

$$
7200 (-E_2'(it)) \Delta(it) = 7200 \cdot 24 \left(\sum_{n \ge 1} n \sigma_1(n) e^{-2 \pi n t}\right) \cdot \Delta(it) > 0.
$$

Negativity of [(12)](lemma-fg-de.md), i.e. $-640 \Delta(it) H_2(it) < 0$ follows from Corollary [theta-pos](../modular-forms/part-03/cor-theta-pos.md) and [disc-pos](../modular-forms/part-02/cor-disc-pos.md).

## Lean

Formalized as [`SerreDer_22_L₁₀_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SerreDer_22_L₁₀_pos).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 136](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L136)
