---
declaration: theorem
origin: cited
lean: harmonic_geometric_arithmetic₃
statement: formalized
proof: formalized
---

# Still another Proof

Let $a_1, \dots, a_n$ be positive real numbers, then

$$
\frac{n}{\frac{1}{a_1}+\dots+\frac{1}{a_n}} \le
\sqrt[n]{a_1a_2\dots a_n} \le
\frac{a_1+\dots+ a_n}{n}
$$

with equality in both cases if and only if all $a_i$'s are equal.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

There is another nice proof, due to Michael D. Hirschhorn. It uses Bernoulli's inequality, which says

$$
(1+t)^{n+1} \ge 1 + (n+1)t \qquad \text{for real } t \ge -1.
$$

Suppose $a_1, a_2, \dots, a_{n+1} > 0$ and set

$$
t = \frac{\frac{a_1 + \cdots + a_{n+1}}{n+1}}{\frac{a_1 + \cdots + a_n}{n}} - 1.
$$

By Bernoulli,

$$
\left(\frac{\frac{a_1 + \cdots + a_{n+1}}{n+1}}{\frac{a_1 + \cdots + a_n}{n}}\right)^{n+1}
\ge 1 + (n+1)\left(\frac{\frac{a_1 + \cdots + a_{n+1}}{n+1}}{\frac{a_1 + \cdots + a_n}{n}} - 1\right)
= \frac{n\, a_{n+1}}{a_1 + \cdots + a_n},
$$

which translates into

$$
\left(\frac{a_1 + \cdots + a_{n+1}}{n+1}\right)^{n+1} \ge a_{n+1} \left(\frac{a_1 + \cdots + a_n}{n}\right)^n,
$$

and the arithmetic-geometric mean inequality follows by induction.

## Lean

Formalized as [`harmonic_geometric_arithmetic₃`](https://mo271.github.io/FormalBook/docs/find/#doc/harmonic_geometric_arithmetic₃).

## Sources

- [Formal Book blueprint: chapter/chapter20.tex, line 118](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter20.tex#L118)
