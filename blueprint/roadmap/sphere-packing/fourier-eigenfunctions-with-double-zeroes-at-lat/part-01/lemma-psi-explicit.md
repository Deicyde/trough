---
declaration: lemma
origin: cited
lean: ψI_eq, ψT_eq, ψS_eq
statement: formalized
proof: formalized
---

# psi-explicit

$$
\begin{aligned}
\psi_I &= 128 \left(\frac{H_3 + H_4}{H_2^2} + \frac{H_4 - H_2}{H_3^2}\right)\qquad\text{(21)}\\
\psi_T &= 128 \left(\frac{H_3 + H_4}{H_2^2} + \frac{H_2 + H_3}{H_4^2}\right)\qquad\text{(22)}\\
\psi_S &= 128 \left(\frac{H_4 - H_2}{H_3^2} - \frac{H_2 + H_3}{H_4^2}\right)\qquad\text{(23)}\end{aligned}
$$

## Depends on

- [psiI-psiT-psiS](def-psii-psit-psis.md)
- [theta-transform-S-T](../../modular-forms/part-02/lemma-theta-transform-s-t.md)

## Proof

By Lemma [theta-transform-S-T](../../modular-forms/part-02/lemma-theta-transform-s-t.md) and the cocycle property of the slash action,

$$
\begin{aligned}
H_2|_{2}ST = -H_3, \qquad
H_3|_{2}ST = -H_4, \qquad
H_4|_{2}ST = H_2,
\end{aligned}
$$

so, since the automorphy factors cancel in the quotient defining $h$,

$$
h|_{-2}ST = 128\,\frac{(H_3|_2 ST) + (H_4|_2 ST)}{((H_2|_2 ST))^2}
= 128\, \frac{-H_4 + H_2}{H_3^2},
$$

which gives (21). Applying $|_{-2}T$ and $|_{-2}S$ to $\psi_I$, using Lemma [theta-transform-S-T](../../modular-forms/part-02/lemma-theta-transform-s-t.md) again, gives (22) and (23).

## Lean

Formalized as [`ψI_eq`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψI_eq), [`ψT_eq`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψT_eq), [`ψS_eq`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/ψS_eq).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/construct-a-b.tex, line 517](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/construct-a-b.tex#L517)
