---
declaration: theorem
origin: cited
lean: erdos_gallai_A_ge_two_thirds_T
statement: formalized
proof: formalized
---

# ch20theorem2

Let $f(x)$ be a real polynomial of degree $n \ge 2$ with only real roots, such that $f(x)> 0$ for $-1 < x < 1$ amd $f(-1) = f(1) = 0$. Then

$$
\frac{2}{3}T \le A \le \frac{2}{3}R,
$$

and equality holds in both cases only for $n=2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

**Proof of $\frac{2}{3}T \le A$.** Since $f(x)$ has only real roots, and none of them in the open interval $(-1,1)$, it can be written (apart from a constant positive factor which cancels out) in the form

$$
f(x) = (1-x^2)\prod_i (\alpha_i - x)\prod_j (\beta_j + x)
$$

with $\alpha_i \ge 1$, $\beta_j \ge 1$. Hence $A = \int_{-1}^{1} f(x)\,dx$.

By making the substitution $x \to -x$, we find that also $A = \int_{-1}^{1} (1-x^2)\prod_i(\alpha_i + x)\prod_j(\beta_j - x)\,dx$, and hence by the inequality of the arithmetic and the geometric mean (note that all factors are $\ge 0$):

$$
\begin{aligned}
A &= \int_{-1}^{1} \frac{1}{2}\left[(1-x^2)\prod(\alpha_i - x)\prod(\beta_j + x) + (1-x^2)\prod(\alpha_i + x)\prod(\beta_j - x)\right] dx \\
&\ge \int_{-1}^{1} (1-x^2)\left[\prod(\alpha_i^2 - x^2)\prod(\beta_j^2 - x^2)\right]^{1/2} dx \\
&\ge \int_{-1}^{1} (1-x^2)\left[\prod(\alpha_i^2 - 1)\prod(\beta_j^2 - 1)\right]^{1/2} dx \\
&= \frac{4}{3}\left[\prod(\alpha_i^2 - 1)\prod(\beta_j^2 - 1)\right]^{1/2}.
\end{aligned}
$$

Computing $f'(1)$ and $f'(-1)$ from the product form, we find $f'(1) = -2\prod(\alpha_i - 1)\prod(\beta_j + 1)$ and $f'(-1) = 2\prod(\alpha_i + 1)\prod(\beta_j - 1)$, hence $-f'(1)f'(-1) = 4\prod(\alpha_i^2-1)\prod(\beta_j^2-1)$, so

$$
A \ge \frac{2}{3}(-f'(1)f'(-1))^{1/2}.
$$

Applying the inequality of the harmonic and geometric mean to $-f'(1)$ and $f'(-1)$, we arrive by formula (2) for $T$ at

$$
A \ge \frac{2}{3}\cdot\frac{2}{\frac{1}{-f'(1)} + \frac{1}{f'(-1)}} = \frac{4}{3}\cdot\frac{f'(1)f'(-1)}{f'(1)-f'(-1)} = \frac{2}{3}T.
$$

**The inequality $A \le \frac{2}{3}R$:** The book notes “The reader is invited to search for an equally inspired proof of the second inequality in Theorem 2.” This half is not formalized in Lean.

## Lean

Formalized as [`erdos_gallai_A_ge_two_thirds_T`](https://mo271.github.io/FormalBook/docs/find/#doc/erdos_gallai_A_ge_two_thirds_T).

## Sources

- [Formal Book blueprint: chapter/chapter20.tex, line 188](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter20.tex#L188)
