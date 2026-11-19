---
declaration: theorem
origin: cited
lean: euler_series'
statement: formalized
---

# Euler's series: Proof 2

$$
\sum_{k \ge 0}\frac{1}{(2k+1)^2} = \frac{\pi^2}{8}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

As above, we may express this as a double integral, namely

$$
J = \int_0^1 \int_0^1 \frac{1}{1-x^2 y^2} dx \, dy = \sum_{k \ge 0} \frac{1}{(2k+1)^2}.
$$

So we have to compute this integral $J$. And for this Beukers, Calabi and Kolk proposed the new coordinates

$$
u := \arccos \sqrt{\frac{1-x^2}{1-x^2 y^2}} \quad v := \arccos \sqrt{\frac{1-y^2}{1-x^2 y^2}}.
$$

To compute the double integral, we may ignore the boundary of the domain, and consider $x, y$ in the range $0 < x < 1$ and $0 < y < 1$. Then $u, v$ will lie in the triangle $u > 0, v > 0, u+v < \pi/2$. The coordinate transformation can be inverted explicitly, which leads one to the substitution

$$
x = \frac{\sin u}{\cos v} \quad \text{and} \quad y = \frac{\sin v}{\cos u}.
$$

It is easy to check that these formulas define a bijective coordinate transformation between the interior of the unit square $S = \{(x, y) : 0 \le x, y \le 1\}$ and the interior of the triangle $T = \{(u, v) : u, v \ge 0, u+v \le \pi/2\}$. Now we have to compute the Jacobi determinant of the coordinate transformation, and magically it turns out to be

$$
\det \begin{pmatrix} \frac{\cos u}{\cos v} & \frac{\sin u \sin v}{\cos^2 v} \\ \frac{\sin u \sin v}{\cos^2 u} & \frac{\cos v}{\cos u} \end{pmatrix} = 1 - \frac{\sin^2 u \sin^2 v}{\cos^2 u \cos^2 v} = 1 - x^2 y^2.
$$

But this means that the integral that we want to compute is transformed into

$$
J = \int_0^{\pi/2} \int_0^{\pi/2-u} 1 dv du,
$$

which is just the area $\frac{1}{2} (\frac{\pi}{2})^2 = \frac{\pi^2}{8}$ of the triangle $T$.

## Lean

Stated as [`euler_series'`](https://mo271.github.io/FormalBook/docs/find/#doc/euler_series'); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter09.tex, line 59](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter09.tex#L59)
