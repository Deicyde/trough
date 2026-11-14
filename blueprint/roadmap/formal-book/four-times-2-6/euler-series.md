---
declaration: theorem
origin: cited
lean: euler_series
statement: formalized
---

# Euler's series: Proof 1

$$
\sum_{n \ge 1} \frac{1}{n^2} = \frac{\pi^2}{6}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The proof consists in two different evaluations of the double integral

$$
I := \int_0^1 \int_0^1 \frac{1}{1-xy} dx dy.
$$

For the first one, we expand $\frac{1}{1-xy}$ as a geometric series, decompose the summands as products, and integrate effortlessly:

$$
\begin{aligned}
I &= \int_0^1 \int_0^1 \sum_{n \ge 0} (xy)^n \, dx \, dy = \sum_{n \ge 0} \int_0^1 \int_0^1 x^n y^n \, dx \, dy \\
&= \sum_{n \ge 0} \left(\int_0^1 x^n \, dx\right) \left(\int_0^1 y^n \, dy\right) = \sum_{n \ge 0} \frac{1}{n+1} \frac{1}{n+1} \\
&= \sum_{n \ge 0} \frac{1}{(n+1)^2} = \sum_{n \ge 1} \frac{1}{n^2} = \zeta(2).
\end{aligned}
$$

This evaluation also shows that the double integral (over a positive function with a pole at $x=y=1$) is finite. Note that the computation is also easy and straightforward if we read it backwards — thus the evaluation of $\zeta(2)$ leads one to the double integral $I$.

The second way to evaluate $I$ comes from a change of coordinates: in the new coordinates given by $u := \frac{y+x}{2}$ and $v := \frac{y-x}{2}$ the domain of integration is a square of side length $\frac{1}{2}\sqrt{2}$, which we get from the old domain by first rotating it by $45^\circ$ and then shrinking it by a factor of $\sqrt{2}$. Substitution of $x = u-v$ and $y = u+v$ yields

$$
\frac{1}{1-xy} = \frac{1}{1-u^2+v^2}.
$$

To transform the integral, we have to replace $dx \, dy$ by $2 \, du \, dv$, to compensate for the fact that our coordinate transformation reduces areas by a constant factor of $2$ (which is the Jacobi determinant of the transformation). The new domain of integration, and the function to be integrated, are symmetric with respect to the $u$-axis, so we just need to compute two times (another factor of $2$ arises here!) the integral over the upper half domain, which we split into two parts in the most natural way:

$$
I = 4 \int_0^{1/2} \left(\int_0^u \frac{dv}{1-u^2+v^2}\right) du + 4 \int_{1/2}^1 \left(\int_0^{1-u} \frac{dv}{1-u^2+v^2}\right) du.
$$

Using $\int \frac{dx}{a^2+x^2} = \frac{1}{a} \arctan \frac{x}{a} + C$, this becomes

$$
\begin{aligned}
I &= 4 \int_0^{1/2} \frac{1}{\sqrt{1-u^2}} \arctan \left(\frac{u}{\sqrt{1-u^2}}\right) du \\
&\quad + 4 \int_{1/2}^1 \frac{1}{\sqrt{1-u^2}} \arctan \left(\frac{1-u}{\sqrt{1-u^2}}\right) du.
\end{aligned}
$$

These integrals can be simplified and finally evaluated by substituting $u = \sin \theta$ resp. $u = \cos \theta$. But we proceed more directly, by computing that the derivative of $g(u) := \arctan \left(\frac{u}{\sqrt{1-u^2}}\right)$ is $g'(u) = \frac{1}{\sqrt{1-u^2}}$, while the derivative of $h(u) := \arctan \left(\frac{1-u}{\sqrt{1-u^2}}\right) = \arctan \left(\sqrt{\frac{1-u}{1+u}}\right)$ is $h'(u) = -\frac{1}{2} \frac{1}{\sqrt{1-u^2}}$. So we may use $\int_a^b f'(x) f(x) dx = \left[ \frac{1}{2} f(x)^2 \right]_a^b = \frac{1}{2} f(b)^2 - \frac{1}{2} f(a)^2$ and get

$$
\begin{aligned}
I &= 4 \int_0^{1/2} g'(u) g(u) du + 4 \int_{1/2}^1 -2 h'(u) h(u) du \\
&= 2 \left[ g(u)^2 \right]_0^{1/2} - 4 \left[ h(u)^2 \right]_{1/2}^1 \\
&= 2 g\left(\frac{1}{2}\right)^2 - 2 g(0)^2 - 4 h(1)^2 + 4 h\left(\frac{1}{2}\right)^2 \\
&= 2 \left(\frac{\pi}{6}\right)^2 - 0 - 0 + 4 \left(\frac{\pi}{6}\right)^2 = \frac{\pi^2}{6}. \qedhere
\end{aligned}
$$

## Lean

Stated as [`euler_series`](https://mo271.github.io/FormalBook/docs/find/#doc/euler_series); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter09.tex, line 3](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter09.tex#L3)
