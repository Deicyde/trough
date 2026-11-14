---
declaration: corollary
origin: cited
lean: FG_inequality_2
statement: formalized
proof: formalized
---

# ineqBnew

[(10)](lemma-ineqabnew-equiv.md) holds.

## Depends on

- [Qlim](lemma-qlim.md)
- [Qdec](prop-qdec.md)
- [F-G-pos](lemma-f-g-pos.md)

## Proof

$$
\frac{F(it)}{G(it)} = Q(t) < \lim_{u \to 0^+} Q(u) = \frac{18}{\pi^2}
$$

and by Lemma [F-G-pos](lemma-f-g-pos.md), [(10)](lemma-ineqabnew-equiv.md) follows.

## Lean

Formalized as [`FG_inequality_2`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/FG_inequality_2).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 216](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L216)
