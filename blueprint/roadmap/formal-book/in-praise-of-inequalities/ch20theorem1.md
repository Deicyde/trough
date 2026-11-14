---
declaration: theorem
origin: cited
lean: laguerre_root_bound
statement: formalized
proof: formalized
---

# ch20theorem1

Suppose all roots of the polynomial $x^n + a_{n-1}x^{n-1} + \dots + a_0$ are real. Then the roots are contained in the interval with the endpoints

$$
-\frac{a_{n-1}}{n}\pm\frac{n-1}{n}\sqrt{a_{n-1}^2 - \frac{2n}{n-1}a_{n-2}}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $y$ be one of the roots and $y_1, \dots, y_{n-1}$ the others. Then the polynomial is $(x-y)(x-y_1)\cdots(x-y_{n-1})$. Thus by comparing coefficients

$$
\begin{aligned}
-a_{n-1} &= y + y_1 + \cdots + y_{n-1}, \\
a_{n-2} &= y(y_1 + \cdots + y_{n-1}) + \sum_{i\lt j} y_i y_j,
\end{aligned}
$$

and so $a_{n-1}^2 - 2a_{n-2} - y^2 = \sum_{i=1}^{n-1} y_i^2$.

By Cauchy's inequality applied to $(y_1, \dots, y_{n-1})$ and $(1, \dots, 1)$,

$$
(a_{n-1} + y)^2 = (y_1 + \cdots + y_{n-1})^2 \le (n-1)\sum_{i=1}^{n-1} y_i^2 = (n-1)(a_{n-1}^2 - 2a_{n-2} - y^2),
$$

or

$$
y^2 + \frac{2a_{n-1}}{n}y + \frac{2(n-1)}{n}a_{n-2} - \frac{n-2}{n}a_{n-1}^2 \le 0.
$$

Thus $y$ (and hence all $y_i$) lie between the two roots of the quadratic function, and these roots are our bounds.

## Lean

Formalized as [`laguerre_root_bound`](https://mo271.github.io/FormalBook/docs/find/#doc/laguerre_root_bound).

## Sources

- [Formal Book blueprint: chapter/chapter20.tex, line 153](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter20.tex#L153)
