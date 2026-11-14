---
declaration: lemma
origin: cited
lean: MLDE_F, MLDE_G
statement: formalized
proof: formalized
---

# FG-de

$F$ and $G$ satisfy the following differential equations:

$$
\begin{aligned}
\partial_{12}\partial_{10} F - \frac{5}{6} E_{4} F &= 7200 \Delta (-E_{2}')\qquad\text{(11)}\\
\partial_{12}\partial_{10} G - \frac{5}{6} E_{4} G &= -640 \Delta H_{2}\qquad\text{(12)}\end{aligned}
$$

## Depends on

- [ramanujan-formula](../modular-forms/part-03/thm-ramanujan-formula.md)
- [serre-der-prod-rule](../modular-forms/part-03/thm-serre-der-prod-rule.md)
- [theta-der](../modular-forms/part-03/prop-theta-der.md)
- [lv1-lv2-identities](../modular-forms/part-03/lemma-lv1-lv2-identities.md)

## Proof

Both can be shown by direct computations. By Ramanujan's identities (Theorem [ramanujan-formula](../modular-forms/part-03/thm-ramanujan-formula.md)) and the product rule of Serre derivatives (Theorem [serre-der-prod-rule](../modular-forms/part-03/thm-serre-der-prod-rule.md)), we have

$$
\begin{aligned}
\partial_{5} (E_2 E_4 - E_6) &= (E_2 E_4 - E_6)' - \frac{5}{12} E_2 (E_2 E_4 - E_6) \\
&= \frac{E_2^2 - E_4}{12} \cdot E_4 + E_2 \cdot \frac{E_2 E_4 - E_6}{3} - \frac{E_2 E_6 - E_4^2}{2} - \frac{5}{12}E_2 (E_2 E_4 - E_6) \\
&= -\frac{5}{12} (E_2 E_6 - E_4^2)\qquad\text{(13)}\\
\partial_{7} (E_2 E_6 - E_4^2) &= (E_2 E_6 - E_4^2)' - \frac{7}{12} E_2 (E_2 E_6 - E_4^2) \\
&= \frac{E_2^2 - E_4}{12} \cdot E_6 + E_2 \cdot \frac{E_2 E_6 - E_4^2}{2} - 2 E_4 \cdot \frac{E_2 E_4 - E_6}{3} - \frac{7}{12} E_2 (E_2 E_6 - E_4^2) \\
&= -\frac{7}{12} E_4 (E_2 E_4 - E_6)\qquad\text{(14)}\end{aligned}
$$

and using these we can compute

$$
\begin{aligned}
\partial_{10} F &= \partial_{10} (E_2 E_4 - E_6)^2 \\
&= 2 (E_2 E_4 - E_6) \partial_{5} (E_2 E_4 - E_6) \\
&= -\frac{6}{5} (E_2 E_4 - E_6) (E_2 E_6 - E_4^2), \\
\partial_{12}\partial_{10} F &= -\frac{5}{6} \partial_{12} ((E_2 E_4 - E_6) (E_2 E_6 - E_4)) \\
&= -\frac{5}{6} (\partial_{5}(E_2 E_4 - E_6)) (E_2 E_6 - E_4^2) - \frac{5}{6} (E_2 E_4 - E_6) (\partial_{7} (E_2 E_6 - E_4)) \\
&= \frac{25}{72} (E_2 E_6 - E_4^2)^2 + \frac{35}{72} E_4 (E_2 E_4 - E_6)^2, \\
\partial_{12}\partial_{10}F - \frac{5}{6} E_4 F &= \frac{25}{72}(E_2 E_6 - E_4^2)^2 + \frac{35}{72} E_4 (E_2 E_4 - E_6)^2 - \frac{5}{6} E_4 (E_2 E_4 - E_6)^2 \\
&= \frac{25}{72} ((E_2 E_6 - E_4^2)^2 - E_4 (E_2 E_4 - E_6)^2) \\
&= \frac{25}{72} (- E_2^2 E_4^3 + E_2^2 E_6^2 + E_4^4 - E_4 E_6^3) \\
&= -\frac{25}{72} (E_4^3 - E_6^2) (E_2^2 - E_4) \\
&= 7200 \cdot \frac{E_4^3 - E_6^2}{1728} \cdot \frac{-E_2^2 + E_4}{12}\\
&= 7200 \Delta (-E_2')
\end{aligned}
$$

which proves (11). Similarly, (12) can be proved using Proposition [theta-der](../modular-forms/part-03/prop-theta-der.md) and Lemma [lv1-lv2-identities](../modular-forms/part-03/lemma-lv1-lv2-identities.md).

## Lean

Formalized as [`MLDE_F`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MLDE_F), [`MLDE_G`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MLDE_G).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modform-ineq.tex, line 99](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modform-ineq.tex#L99)
