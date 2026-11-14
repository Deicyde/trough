---
declaration: proposition
origin: cited
lean: MagicFunction.g.CohnElkies.IntegralReps.aRadial_eq_another_integral_main
statement: formalized
proof: formalized
---

# a-another-integral

For $r\geq0$ we have

$$
\begin{aligned}a(r)=&4i\,\sin(\pi r^2/2)^2\,\Bigg(\frac{36}{\pi^3\,(r^2-2)}-\frac{8640}{\pi^3\,r^4}+\frac{18144}{\pi^3\,r^2}\qquad\text{(20)}\\ +&\int\limits_0^\infty\,\left(t^2\,\phi_0\Big(\frac{i}{t}\Big)-\frac{36}{\pi^2}\,e^{2\pi t}+\frac{8640}{\pi}\,t-\frac{18144}{\pi^2}\right)\,e^{-\pi r^2 t}\,dt \Bigg) .\end{aligned}
$$

The integral converges absolutely for all $r\in\mathbb{R}_{\geq 0}$.

## Depends on

- [a-double-zeros](prop-a-double-zeros.md)
- [phi4-phi2-phi0](def-phi4-phi2-phi0.md)
- [phi0-transform](lemma-phi0-transform.md)
- [a-definition](def-a-definition.md)

## Proof

Suppose that $r>\sqrt{2}$. Then by Proposition [a-double-zeros](prop-a-double-zeros.md)

$$
a(r)=4i\,\sin(\pi r^2/2)^2\,\int\limits_{0}^{\infty}\phi_0(i/t)\,t^2\,e^{-\pi r^2 t}\,dt.
$$

From [(7)](lemma-phi0-transform.md) we obtain

$$
\phi_0(i/t)\,t^2=\frac{36}{\pi^2}\,e^{2 \pi t}-\frac{8640}{\pi}\,t+\frac{18144}{\pi^2}+O(t^2\,e^{-2\pi t})\quad\mbox{as}\;t\to\infty.\qquad\text{(21)}
$$

For $r>\sqrt{2}$ we have

$$
\int\limits_0^\infty \left(\frac{36}{\pi^2}\,e^{2 \pi t}+\frac{8640}{\pi}\,t+\frac{18144}{\pi^2}\right)\,e^{-\pi r^2 t}\,dt
=\frac{36}{\pi^3\,(r^2-2)}-\frac{8640}{\pi^3\,r^4}+\frac{18144}{\pi^3\,r^2}.
$$

Therefore, the identity (20) holds for $r>\sqrt{2}$.

On the other hand, from the definition [(8)](def-a-definition.md) we see that $a(r)$ is analytic in some neighborhood of $[0,\infty)$. The asymptotic expansion (21) implies that the right hand side of (20) is also analytic in some neighborhood of $[0,\infty)$. Hence, the identity (20) holds on the whole interval $[0,\infty)$. This finishes the proof of the proposition.

## Lean

Formalized as [`MagicFunction.g.CohnElkies.IntegralReps.aRadial_eq_another_integral_main`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.g.CohnElkies.IntegralReps.aRadial_eq_another_integral_main).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 378](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L378)
