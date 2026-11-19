---
declaration: theorem
origin: cited
lean: Derivative.serreDerivative_mul
statement: formalized
proof: formalized
---

# serre-der-prod-rule

The Serre derivative satisfies the following product rule: for any quasimodular forms $F$ and $G$,

$$
\partial_{w_1 + w_2} (FG) = (\partial_{w_1}F)G + F (\partial_{w_2}G).
$$

## Depends on

- [serre-der](def-serre-der.md)

## Proof

It follows from the definition:

$$
\begin{aligned}
\partial_{w_1 + w_2} (FG) &= (FG)' - \frac{w_1 + w_2}{12} E_2 (FG) \\
&= F'G + FG' - \frac{w_1 + w_2}{12} E_2(FG) \\
&= \left(F' - \frac{w_1}{12}E_2 F\right)G + F \left(G' - \frac{w_2}{12}E_2 G\right) \\
&= (\partial_{w_1}F)G + F(\partial_{w_2}G).
\end{aligned}
$$

## Lean

Formalized as [`Derivative.serreDerivative_mul`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/Derivative.serreDerivative_mul).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 715](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L715)
