---
declaration: lemma
origin: cited
lean: F_imag_axis_pos, G_imag_axis_pos
statement: formalized
proof: formalized
---

# F-G-pos

For all $t > 0$, we have $F(it) > 0$ and $G(it) > 0$.

## Depends on

- [ramanujan-formula](../modular-forms/part-02/thm-ramanujan-formula.md)
- [theta-pos](../modular-forms/part-02/cor-theta-pos.md)

## Proof

By Ramanujan's identity [(27)](../modular-forms/part-02/thm-ramanujan-formula.md), we have $F(z) = 9 E_4'(z)^2$ and

$$
F(it) = 9E_4'(it)^2 = 9 \left(240\sum_{n \geq 1} n \sigma_3(n) e^{-2 \pi n t} \right)^{2} > 0.
$$

$G(it) > 0$ follows from positivity of $H_2(it)$ and $H_4(it)$ (Lemma [theta-pos](../modular-forms/part-02/cor-theta-pos.md)).

## Lean

Formalized as [`F_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/F_imag_axis_pos), [`G_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/G_imag_axis_pos).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modform-ineq.tex, line 74](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L74)
