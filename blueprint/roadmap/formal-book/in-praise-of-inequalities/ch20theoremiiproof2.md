---
declaration: theorem
origin: cited
lean: harmonic_geometric_arithmetic₂
statement: formalized
proof: formalized
---

# Another Proof

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

Of the many other proofs of the arithmetic-geometric mean inequality, let us single out a particularly striking one by Horst Alzer, with some shortenings due to France Dacar. As a matter of fact, this proof yields the stronger inequality

$$
a_1^{p_1} a_2^{p_2} \cdots a_n^{p_n} \le p_1 a_1 + p_2 a_2 + \cdots + p_n a_n
$$

for any positive numbers $a_1, \dots, a_n$, $p_1, \dots, p_n$ with $\sum_{i=1}^n p_i = 1$. Let us denote the expression on the left side by $G$, and on the right side by $A$. Fix $c > 0$ and define the function $f(t) := \frac{1}{c} - \frac{1}{t}$ on $\mathbb{R}_{>0}$. Since $f(t) < 0$ for $t < c$ and $f(t) > 0$ for $t > c$, we get the inequality

$$
\int_c^x f(t)\,dt \ge 0
$$

for every $x > 0$, with equality if and only if $x = c$. Now

$$
0 \le \int_c^x f(t)\,dt = \left[\frac{t}{c} - \log t\right]_c^x = \frac{x}{c} - 1 - \log\frac{x}{c},
$$

and setting $c = G$ and $x = a_i$ we conclude that

$$
\frac{a_i}{G} - 1 \ge \log a_i - \log G \qquad \text{for } i = 1, 2, \dots, n.
$$

Multiplying this inequality by $p_i$ and summing over all $i$ gives

$$
\sum_{i=1}^n p_i \frac{a_i}{G} - \sum_{i=1}^n p_i \ge \sum_{i=1}^n p_i \log a_i - \sum_{i=1}^n p_i \log G.
$$

With $\sum p_i = 1$, the left side equals $\frac{A}{G} - 1$, while the right side is $\log\left(\prod a_i^{p_i}\right) - \log G = \log G - \log G = 0$. We conclude $\frac{A}{G} - 1 \ge 0$, which is $A \ge G$. In the case of equality, all inequalities must be equalities, which implies $a_1 = \cdots = a_n = G$.

## Lean

Formalized as [`harmonic_geometric_arithmetic₂`](https://mo271.github.io/FormalBook/docs/find/#doc/harmonic_geometric_arithmetic₂).

## Sources

- [Formal Book blueprint: chapter/chapter20.tex, line 72](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter20.tex#L72)
