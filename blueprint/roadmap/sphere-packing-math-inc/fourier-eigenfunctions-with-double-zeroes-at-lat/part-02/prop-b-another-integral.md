---
declaration: proposition
origin: cited
lean: MagicFunction.g.CohnElkies.IntegralReps.bRadial_eq_another_integral_main
statement: formalized
proof: formalized
---

# b-another-integral

For $r\geq0$ we have

$$
b(r)=-4i\,\sin(\pi r^2/2)^2\,\left(\frac{144}{\pi\,r^2}+\frac{1}{\pi\,(r^2-2)}+\int\limits_0^\infty\,\left(\psi_I(it)-144-e^{2\pi t}\right)\,e^{-\pi r^2 t}\,dt\right).\qquad\text{(44)}
$$

The integral converges absolutely for all $r\in\mathbb{R}_{\geq 0}$.

## Depends on

- [b-double-zeros](../part-01/prop-b-double-zeros.md)
- [b-definition](../part-01/def-b-definition.md)

## Proof

The proof is analogous to the proof of Proposition [a-another-integral](../part-01/prop-a-another-integral.md). First, suppose that $r>\sqrt{2}$. Then by Proposition [b-double-zeros](../part-01/prop-b-double-zeros.md)

$$
b(r)=4i\,\sin(\pi r^2/2)^2\,\int\limits_{0}^{\infty}\psi_I(it)\,e^{-\pi r^2 t}\,dt.
$$

From [(29)](../part-01/README.md) we obtain

$$
\psi_I(it)=e^{2\pi t}+144+O(e^{-\pi t})\quad\mbox{as}\;t\to\infty.\qquad\text{(45)}
$$

For $r>\sqrt{2}$ we have

$$
\int\limits_0^\infty \left(e^{2\pi t}+144\right)\,e^{-\pi r^2 t}\,dt
=\frac{1}{\pi\,(r^2-2)}+\frac{144}{\pi\,r^2}.
$$

Therefore, the identity (44) holds for $r>\sqrt{2}$.

On the other hand, from the definition [(30)](../part-01/def-b-definition.md) we see that $b(r)$ is analytic in some neighborhood of $[0,\infty)$. The asymptotic expansion (45) implies that the right hand side of (44) is also analytic in some neighborhood of $[0,\infty)$. Hence, the identity (44) holds on the whole interval $[0,\infty)$. This finishes the proof of the proposition.

## Lean

Formalized as [`MagicFunction.g.CohnElkies.IntegralReps.bRadial_eq_another_integral_main`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.IntegralReps.bRadial_eq_another_integral_main).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 694](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L694)
