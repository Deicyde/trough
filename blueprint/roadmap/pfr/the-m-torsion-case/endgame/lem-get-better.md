---
declaration: lemma
origin: cited
lean: dist_of_U_add_le
statement: formalized
proof: formalized
---

# Application of BSG

Let $G$ be an abelian group, let $(T_1,T_2,T_3)$ be a $G^3$-valued random variable such that $T_1+T_2+T_3=0$ holds identically, and write

$$
\delta := \mathbb{I}[T_1 : T_2] + \mathbb{I}[T_1 : T_3] + \mathbb{I}[T_2 : T_3].
$$

Let $Y_1,\dots,Y_n$ be some further $G$-valued random variables and let $\alpha>0$ be a constant. Then there exists a random variable $U$ such that

$$
d[U;U] + \alpha \sum_{i=1}^n d[Y_i;U] \leq \Bigl(2 + \frac{\alpha n}{2} \Bigr) \delta + \alpha \sum_{i=1}^n d[Y_i;T_2].\qquad\text{(6)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Balog-Szemerédi-Gowers](../../entropic-ruzsa-calculus/part-02/entropic-bsg.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md)

## Proof

We apply [Balog-Szemerédi-Gowers](../../entropic-ruzsa-calculus/part-02/entropic-bsg.md) with $X=T_1$ and $Y=T_2$. Since $T_1+T_2=-T_3$, we find that

$$
\begin{split}
\sum_{z} p_{T_3}(z) & d[T_1 \,|\, T_3 \mathop{=} z;T_2 \,|\, T_3 \mathop{=} z] \\
&\leq  3 \mathbb{I}[T_1 : T_2] + 2 \mathbb{H}[T_3] - \mathbb{H}[T_1] - \mathbb{H}[T_2] \\
&\ = \mathbb{I}[T_1 : T_2] + \mathbb{I}[T_1 : T_3] + \mathbb{I}[T_2 : T_3]
= \delta,
\end{split}\qquad\text{(7)}
$$

where the last line follows from [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md) by observing

$$
\mathbb{H}[T_1,T_2] = \mathbb{H}[T_1,T_3] = \mathbb{H}[T_2,T_3] = \mathbb{H}[T_1,T_2,T_3]
$$

since any two of $T_1,T_2,T_3$ determine the third.

By (7) and the triangle inequality,

$$
\sum_z p_{T_3}(z) d[T_2 \,|\, T_3 \mathop{=} z; T_2 \,|\, T_3\mathop{=}z] \leq 2 \delta
$$

and by [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md), for each $Y_i$,

$$
\begin{aligned}
&\sum_z p_{T_3}(z) d[Y_i; T_2 \,|\, T_3 \mathop{=} z] \\
&\qquad= d[Y_i; T_2 \,|\, T_3]
\leq d[Y_i;T_2] + \frac12 \mathbb{I}[T_2 : T_3]
\leq d[Y_i;T_2] + \frac{\delta}{2}.
\end{aligned}
$$

Hence,

$$
\begin{aligned}
&\sum_z p_{T_3}(z) \bigg( d[T_2 \,|\, T_3 \mathop{=} z; T_2 \,|\, T_3 \mathop{=} z] + \alpha \sum_{i=1}^n d[Y_i;T_2 \,|\, T_3 \mathop{=} z] \bigg) \\
&\qquad \leq
\Bigl(2 + \frac{\alpha n}{2} \Bigr) \delta + \alpha \sum_{i=1}^n d[Y_i; T_2],
\end{aligned}
$$

and the result follows by setting $U=(T_2 \,|\, T_3 \mathop{=} z)$ for some $z$ such that the quantity in parentheses on the left-hand side is at most the weighted average value.

## Lean

Formalized as [`dist_of_U_add_le`](https://teorth.github.io/pfr/docs/find/#doc/dist_of_U_add_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 769](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L769)
