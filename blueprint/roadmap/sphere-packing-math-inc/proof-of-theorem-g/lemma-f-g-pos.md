---
declaration: lemma
origin: cited
lean: F_pos, G_pos
statement: formalized
proof: formalized
---

# F-G-pos

For all $t > 0$, we have $F(it) > 0$ and $G(it) > 0$.

## Depends on

- [ramanujan-formula](../modular-forms/part-03/thm-ramanujan-formula.md)
- [theta-pos](../modular-forms/part-03/cor-theta-pos.md)

## Proof

By Ramanujan's identity [(37)](../modular-forms/part-03/thm-ramanujan-formula.md), we have $F(z) = 9 E_4'(z)^2$ and

$$
F(it) = 9E_4'(it)^2 = 9 \left(240\sum_{n \geq 1} n \sigma_3(n) e^{-2 \pi n t} \right)^{2} > 0.
$$

$G(it) > 0$ follows from positivity of $H_2(it)$ and $H_4(it)$ (Lemma [theta-pos](../modular-forms/part-03/cor-theta-pos.md)).

## Lean

Formalized as [`F_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/F_pos), [`G_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/G_pos).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 80](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L80)
