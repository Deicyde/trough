---
declaration: corollary
origin: cited
lean: H₂_imag_axis_pos, H₄_imag_axis_pos, jacobi_identity
statement: formalized
proof: formalized
---

# theta-pos

All three functions $t \mapsto H_2(it), H_3(it), H_4(it)$ are positive for $t > 0$.

## Depends on

- [jacobi-identity](../part-02/lemma-jacobi-identity.md)
- [theta-transform-S-T](../part-02/lemma-theta-transform-s-t.md)

## Proof

By Lemma [jacobi-identity](../part-02/lemma-jacobi-identity.md) and the transformation law [(17)](../part-02/lemma-theta-transform-s-t.md), it is enough to prove the positivity for $\Theta_2(it)$, which is clear from its definition:

$$
\Theta_{2}(it) = \sum_{n \in \mathbb{Z}} e^{- \pi (n + \frac{1}{2})^{2} t} > 0.
$$

## Lean

Formalized as [`H₂_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₂_imag_axis_pos), [`H₄_imag_axis_pos`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₄_imag_axis_pos), [`jacobi_identity`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/jacobi_identity).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 511](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L511)
