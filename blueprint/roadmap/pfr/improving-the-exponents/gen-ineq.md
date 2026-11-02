---
declaration: lemma
origin: cited
lean: gen_ineq_00, gen_ineq_01, gen_ineq_10
statement: formalized
proof: formalized
---

# General inequality

Let $X_1, X_2, X_3, X_4$ be independent $G$-valued random variables, and let $Y$ be another $G$-valued random variable. Set $S := X_1+X_2+X_3+X_4$. Then

$$
\begin{aligned}
&  d[Y; X_1+X_2|X_1 + X_3, S] - d[Y; X_1] \\
&\quad \leq \tfrac{1}{4} (d[X_1;X_2] + 2d[X_1;X_3] + d[X_2;X_4])\\
&\qquad \qquad + \tfrac{1}{4} (d[X_1|X_1+X_3;X_2|X_2+X_4] - d[X_3|X_3+X_4; X_1|X_1+X_2])\\
&\qquad \qquad + \tfrac{1}{8} (\mathbb{H}[X_1+X_2] - \mathbb{H}[X_3+X_4] + \mathbb{H}[X_2] - \mathbb{H}[X_3]\\
&\qquad \qquad \qquad + \mathbb{H}[X_2|X_2+X_4] - \mathbb{H}[X_1|X_1+X_3]).
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Upper bound on conditioned Ruzsa distance](../entropic-ruzsa-calculus/part-02/cond-dist-fact.md)
- [Comparison of Ruzsa distances, I](../entropic-ruzsa-calculus/part-02/first-useful.md)
- [Specific fibring identity](../the-fibring-lemma/cor-fibre.md)

## Proof

On the one hand, by [Upper bound on conditioned Ruzsa distance](../entropic-ruzsa-calculus/part-02/cond-dist-fact.md) and two applications of [Comparison of Ruzsa distances, I](../entropic-ruzsa-calculus/part-02/first-useful.md) we have

$$
\begin{aligned}
&d[Y;X_1+X_2|X_1 + X_3, S] \\
&\quad \leq d[Y;X_1+X_2|S] + \tfrac{1}{2} \mathbb{I}[X_1 + X_2 : X_1 + X_3|S] \\
&\quad \leq d[Y;X_1+X_2]\\
&\qquad + \tfrac{1}{2} (d[X_1+X_2;X_3+X_4] + \mathbb{I}[X_1 + X_2 : X_1 + X_3|S])\\
&\qquad + \tfrac{1}{4} (\mathbb{H}[X_1+X_2] - \mathbb{H}[X_3+X_4])\\
&\quad \leq d[Y;X_1] \\
&\qquad + \tfrac{1}{2} (d[X_1;X_2] + d[X_1+X_2;X_3+X_4] + \mathbb{I}[X_1 + X_2 : X_1 + X_3|S])\\
&\qquad + \tfrac{1}{4} (\mathbb{H}[X_1+X_2] - \mathbb{H}[X_3+X_4] + \mathbb{H}[X_2] - \mathbb{H}[X_1]).
\end{aligned}
$$

From [Specific fibring identity](../the-fibring-lemma/cor-fibre.md) (with $Y_1,Y_2,Y_3,Y_4$ set equal to $X_3, X_1, X_4, X_2$ respectively) one has

$$
d[X_3+X_4; X_1+X_2] + d[X_3|X_3+X_4; X_1|X_1+X_2]
$$

$$
+ \mathbb{I}[X_3 + X_1 : X_1 + X_2|S] = d[X_3;X_1] + d[X_4;X_2].
$$

Rearranging the mutual information and Ruzsa distances slightly, we conclude that

$$
\begin{aligned}
&d[Y;X_1+X_2|X_1 + X_3, S] \\
&\quad \leq d[Y;X_1] \\
&\qquad + \tfrac{1}{2} (d[X_1;X_2] + d[X_1;X_3] + d[X_2;X_4] - d[X_3|X_3+X_4; X_1|X_1+X_2])\\
&\qquad + \tfrac{1}{4} (\mathbb{H}[X_1+X_2] - \mathbb{H}[X_3+X_4] + \mathbb{H}[X_2] - \mathbb{H}[X_1]).
\end{aligned}
$$

On the other hand, $(X_1+X_2|X_1 + X_3, S)$ has an identical distribution to the independent sum of $(X_1|X_1+X_3)$ and $(X_2|X_2+X_4)$. We may therefore apply [Comparison of Ruzsa distances, I](../entropic-ruzsa-calculus/part-02/first-useful.md) to conditioned variables $(X_1|X_1+X_3=s)$ and $(X_2|X_2+X_4=t)$ and average in $s,t$ to obtain the alternative bound

$$
\begin{aligned}
&  d[Y;X_1+X_2|X_1 + X_3, S] \\
&\quad \leq d[Y;X_1|X_1+X_3] + \tfrac{1}{2} d[X_1|X_1+X_3; X_2|X_2+X_4] \\
&\qquad + \tfrac{1}{4} (\mathbb{H}[X_2|X_2+X_4] - \mathbb{H}[X_1|X_1+X_3]) \\
&\quad  \leq d[Y;X_1] \\
&\qquad + \tfrac{1}{2} (d[X_1;X_3] + d[X_1|X_1+X_3;X_2|X_2+X_4])\\
&\qquad + \tfrac{1}{4} (\mathbb{H}[X_2|X_2+X_4] - \mathbb{H}[X_1|X_1+X_3] + \mathbb{H}[X_1] - \mathbb{H}[X_3]).
\end{aligned}
$$

If one takes the arithmetic mean of these two bounds and simplifies using [Specific fibring identity](../the-fibring-lemma/cor-fibre.md), one obtains the claim.

## Lean

Formalized as [`gen_ineq_00`](https://teorth.github.io/pfr/docs/find/#doc/gen_ineq_00), [`gen_ineq_01`](https://teorth.github.io/pfr/docs/find/#doc/gen_ineq_01), [`gen_ineq_10`](https://teorth.github.io/pfr/docs/find/#doc/gen_ineq_10).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 88](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/improved_exponent.tex#L88)
