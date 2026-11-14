---
declaration: theorem
origin: cited
lean: serre_D_mul
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

Formalized as [`serre_D_mul`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/serre_D_mul).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 691](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L691)
