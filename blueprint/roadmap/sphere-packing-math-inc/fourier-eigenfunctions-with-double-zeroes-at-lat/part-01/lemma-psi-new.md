---
declaration: lemma
origin: cited
lean: ψI_eq, ψT_eq, ψS_eq'
statement: formalized
proof: formalized
---

# psi-new

$\psi_I(z), \psi_S(z), \psi_T(z)$ can be written as

$$
\begin{aligned}
\psi_I(z) &= \frac{H_4^3 (5 H_2^2 + 5 H_2 H_4 + 2 H_4^2)}{2\Delta},\qquad\text{(26)}\\
\psi_S(z) &= -\frac{H_2^3 (2 H_2^2 + 5 H_2 H_4 + 5 H_4^2)}{2 \Delta}.\qquad\text{(27)}\\
\psi_T(z) &= \frac{H_3^3 (5 H_2^2 - 5 H_2 H_3 + 2 H_3^2)}{2 \Delta}\qquad\text{(28)}\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By Lemma [theta-transform-S-T](../../modular-forms/part-02/lemma-theta-transform-s-t.md), we have

$$
\begin{aligned}
H_2|_{-2}ST = (-H_4)|_{-2}T = -H_3, \\
H_3|_{-2}ST = (-H_3)|_{-2}T = -H_4, \\
H_4|_{-2}ST = (-H_2)|_{-2}T = H_2.
\end{aligned}
$$

Using these equations and Lemma [lv1-lv2-identities](../../modular-forms/part-03/lemma-lv1-lv2-identities.md), we can rewrite $\psi_I(z)$ as

$$
\begin{aligned}
\psi_I(z) &= h(z) - h|_{-2}ST(z) \\
&= 128 \frac{H_3 + H_4}{H_2^2} - 128 \frac{-H_4 + H_2}{H_3^2} \\
&= 128 \frac{H_3^2 (H_3 + H_4) - H_2^2 (H_2 - H_4)}{H_2^2 H_3^2} \\
&= 128 \frac{(H_2 + H_4)^2 (H_2 + 2 H_4) - H_2^2 (H_2 - H_4)}{H_2^2 H_3^2} \\
&= 128 \frac{H_4(5 H_2^2 + 5 H_2 H_4 + 2 H_4^2)}{ H_2^2 H_3^2} \\
&= 128 \frac{H_4^3(5 H_2^2 + 5 H_2 H_4 + 2 H_4^2)}{ H_2^2 H_3^2 H_4^3} \\
&= \frac{H_4^3 (5 H_2^2 + 5 H_2 H_4 + 2 H_4^2)}{2\Delta}.
\end{aligned}
$$

Applying $|_{-2}S$ and $|_{-2}T$ to the expression of $\psi_I$ proves (27) and (28).

## Lean

Formalized as [`ψI_eq`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψI_eq), [`ψT_eq`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψT_eq), [`ψS_eq'`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψS_eq').

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 449](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L449)
