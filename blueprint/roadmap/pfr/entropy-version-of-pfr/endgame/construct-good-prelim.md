---
declaration: lemma
origin: cited
lean: construct_good_prelim
statement: formalized
proof: formalized
---

# Constructing good variables, I

One has

$$
\begin{aligned}  k \leq
\delta + \eta (& d[X^0_1;T_1]-d[X^0_1;X_1])
+ \eta (d[X^0_2;T_2]-d[X^0_2;X_2]) \\ & + \tfrac12 \eta \mathbb{I}[T_1:T_3] + \tfrac12 \eta \mathbb{I}[T_2:T_3].
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Balog-Szemerédi-Gowers](../../entropic-ruzsa-calculus/part-02/entropic-bsg.md)
- [Upper bound on conditioned Ruzsa distance](../../entropic-ruzsa-calculus/part-02/cond-dist-fact.md)
- [Distance lower bound](../basic-facts-about-minimizers/distance-lower.md)

## Proof

We apply [Balog-Szemerédi-Gowers](../../entropic-ruzsa-calculus/part-02/entropic-bsg.md) with $(A,B) = (T_1, T_2)$ there. Since $T_1 + T_2 = T_3$, the conclusion is that

$$
\begin{aligned}  \sum_{t_3} \mathbb{P}[T_3 = t_3] & d[(T_1 | T_3 = t_3); (T_2 | T_3 = t_3)] \\ & \leq 3 \mathbb{I}[T_1 : T_2] + 2 \mathbb{H}[T_3] - \mathbb{H}[T_1] - \mathbb{H}[T_2].\qquad\text{(2)}\end{aligned}
$$

The right-hand side in (2) can be rearranged as

$$
\begin{aligned} & 2( \mathbb{H}[T_1] + \mathbb{H}[T_2] + \mathbb{H}[T_3]) - 3 \mathbb{H}[T_1,T_2] \\ & = 2(\mathbb{H}[T_1] + \mathbb{H}[T_2] + \mathbb{H}[T_3]) - \mathbb{H}[T_1,T_2] - \mathbb{H}[T_2,T_3] - \mathbb{H}[T_1, T_3] = \delta,\end{aligned}
$$

using the fact (from [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)) that all three terms $\mathbb{H}[T_i,T_j]$ are equal to $\mathbb{H}[T_1,T_2,T_3]$ and hence to each other. We also have

$$
\begin{aligned}
&  \sum_{t_3} P[T_3 = t_3] \bigl(d[X^0_1; (T_1 | T_3=t_3)] - d[X^0_1;X_1]\bigr) \\
&\quad = d[X^0_1; T_1 | T_3] - d[X^0_1;X_1] \leq d[X^0_1;T_1] - d[X^0_1;X_1] + \tfrac{1}{2} \mathbb{I}[T_1 : T_3]
\end{aligned}
$$

by [Upper bound on conditioned Ruzsa distance](../../entropic-ruzsa-calculus/part-02/cond-dist-fact.md), and similarly

$$
\begin{aligned}
&  \sum_{t_3} \mathbb{P}[T_3 = t_3] (d[X^0_2;(T_2 | T_3=t_3)] - d[X^0_2; X_2]) \\
&\quad\quad\quad\quad\quad\quad \leq d[X^0_2;T_2] - d[X^0_2;X_2] + \tfrac{1}{2} \mathbb{I}[T_2 : T_3].
\end{aligned}
$$

Putting the above observations together, we have

$$
\begin{aligned}
\sum_{t_3} \mathbb{P}[T_3=t_3] \psi[(T_1 | T_3=t_3); (T_2 | T_3=t_3)] \leq \delta + \eta (d[X^0_1;T_1]-d[X^0_1;X_1]) \\
+ \eta (d[X^0_2;T_2]-d[X^0_2;X_2]) + \tfrac12 \eta \mathbb{I}[T_1:T_3] + \tfrac12 \eta \mathbb{I}[T_2:T_3]
\end{aligned}
$$

where we introduce the notation

$$
\psi[Y_1; Y_2] := d[Y_1;Y_2] +  \eta (d[X_1^0;Y_1] - d[X_1^0;X_1]) + \eta(d[X_2^0;Y_2] - d[X_2^0;X_2]).
$$

On the other hand, from [Distance lower bound](../basic-facts-about-minimizers/distance-lower.md) we have $k \leq \psi[Y_1;Y_2]$, and the claim follows.

## Lean

Formalized as [`construct_good_prelim`](https://teorth.github.io/pfr/docs/find/#doc/construct_good_prelim).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 327](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L327)
