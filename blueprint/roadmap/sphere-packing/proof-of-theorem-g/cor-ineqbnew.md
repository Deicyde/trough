---
declaration: corollary
origin: cited
lean: FG_inequality_2
statement: formalized
proof: formalized
---

# ineqBnew

[Lemma ineqABnew-equiv](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L50) holds.

## Depends on

- [Qlim](lemma-qlim.md)
- [Qdec](prop-qdec.md)
- [F-G-pos](lemma-f-g-pos.md)

## Proof

$$
\frac{F(it)}{G(it)} = Q(t) < \lim_{u \to 0^+} Q(u) = \frac{18}{\pi^2}
$$

and by Lemma [F-G-pos](lemma-f-g-pos.md), [Lemma ineqABnew-equiv](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L50) follows.

## Lean

Formalized as [`FG_inequality_2`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/FG_inequality_2).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modform-ineq.tex, line 223](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L223)
