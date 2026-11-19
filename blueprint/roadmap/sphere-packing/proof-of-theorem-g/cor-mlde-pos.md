---
declaration: corollary
origin: cited
lean: MLDE_F_imag_axis_pos, MLDE_G_imag_axis_neg
statement: formalized
proof: formalized
---

# MLDE-pos

[(9)](lemma-fg-de.md) (resp. [(10)](lemma-fg-de.md)) is positive (resp. negative) on the (positive) imaginary axis.

## Depends on

- [FG-de](lemma-fg-de.md)
- [disc-pos](../modular-forms/part-01/cor-disc-pos.md)
- [theta-pos](../modular-forms/part-02/cor-theta-pos.md)
- [E2](../modular-forms/part-01/def-e2.md)

## Proof

From [(5)](../modular-forms/part-01/def-e2.md) and Lemma [disc-pos](../modular-forms/part-01/cor-disc-pos.md),

$$
7200 (-E_2'(it)) \Delta(it) = 7200 \cdot 24 \left(\sum_{n \ge 1} n \sigma_1(n) e^{-2 \pi n t}\right) \cdot \Delta(it) > 0.
$$

Negativity of [(10)](lemma-fg-de.md), i.e. $-640 \Delta(it) H_2(it) < 0$ follows from Corollary [theta-pos](../modular-forms/part-02/cor-theta-pos.md) and [disc-pos](../modular-forms/part-01/cor-disc-pos.md).

## Lean

Formalized as [`MLDE_F_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MLDE_F_imag_axis_pos), [`MLDE_G_imag_axis_neg`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MLDE_G_imag_axis_neg).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modform-ineq.tex, line 130](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L130)
