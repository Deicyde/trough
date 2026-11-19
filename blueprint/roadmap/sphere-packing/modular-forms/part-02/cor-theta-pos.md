---
declaration: corollary
origin: cited
lean: H₂_imag_axis_pos, H₄_imag_axis_pos
statement: formalized
proof: formalized
---

# theta-pos

$H_2(it)$ and $H_4(it)$ are positive for $t > 0$.

## Depends on

- [theta-transform-S-T](lemma-theta-transform-s-t.md)

## Proof

By the transformation law [(10)](lemma-theta-transform-s-t.md), it is enough to prove the positivity for $\Theta_2(it)$, which is clear from its definition:

$$
\Theta_{2}(it) = \sum_{n \in \mathbb{Z}} e^{- \pi (n + \frac{1}{2})^{2} t} > 0.
$$

## Lean

Formalized as [`H₂_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₂_imag_axis_pos), [`H₄_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₄_imag_axis_pos).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 534](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L534)
