---
declaration: lemma
origin: cited
lean: sum_dist_diff_le
statement: formalized
proof: formalized
---

# Bound on distance increments

We have

$$
\begin{aligned}
\sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \big(d[X^0_i;A|S] & - d[X^0_i;X_i]\big) \\
&\leq (6 - 3\eta) k + 3(2 \eta k - I_1).
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Comparison of Ruzsa distances, II](../../entropic-ruzsa-calculus/part-02/second-useful.md)
- [Entropy bound on quadruple sum](../first-estimate/foursum-bound.md)

## Proof

By [Comparison of Ruzsa distances, II](../../entropic-ruzsa-calculus/part-02/second-useful.md) (taking $X = X_1^0$, $Y = X_1$, $Z = X_2$ and $Z' = \tilde X_1 + \tilde X_2$, so that $Y + Z = U$ and $Y + Z + Z' = S$) we have, noting that $\mathbb{H}[Y+ Z] = \mathbb{H}[Z']$,

$$
d[X^0_1;U|S] - d[X^0_1;X_1] \leq \tfrac{1}{2} (\mathbb{H}[S] -  \mathbb{H}[X_1]).
$$

Further applications of [Comparison of Ruzsa distances, II](../../entropic-ruzsa-calculus/part-02/second-useful.md) give

$$
\begin{aligned}
d[X^0_2;U|S] - d[X^0_2; X_2] &\leq \tfrac{1}{2} (\mathbb{H}[S] -  \mathbb{H}[X_2]) \\
d[X^0_1;V|S] - d[X^0_1;X_1] &\leq \tfrac{1}{2} (\mathbb{H}[S] -  \mathbb{H}[X_1])\\
d[X^0_2;V|S] - d[X^0_2;X_2] &\leq \tfrac{1}{2} (\mathbb{H}[S] -  \mathbb{H}[X_2])
\end{aligned}
$$

and

$$
d[X^0_1;W|S] - d[X^0_1;X_1] \leq \tfrac{1}{2} (\mathbb{H}[S] + \mathbb{H}[W] - \mathbb{H}[X_1] - \mathbb{H}[W']),
$$

where $W' := X_2 + \tilde X_2$. To treat $d[X^0_2;W|S]$, first note that this equals $d[X^0_2;W'|S]$, since for a fixed choice $s$ of $S$ we have $W' = W + s$ (here we need some helper lemma about Ruzsa distance). Now we may apply [Comparison of Ruzsa distances, II](../../entropic-ruzsa-calculus/part-02/second-useful.md) to obtain

$$
d[X^0_2;W'|S] - d[X^0_2;X_2] \leq \tfrac{1}{2} (\mathbb{H}[S] + \mathbb{H}[W'] - \mathbb{H}[X_2] - \mathbb{H}[W]).
$$

Summing these six estimates and using [Entropy bound on quadruple sum](../first-estimate/foursum-bound.md), we conclude that

$$
\begin{aligned}
\sum_{i=1}^2 \sum_{A\in\{U,V,W\}} \big(d[X^0_i;A|S] & - d[X^0_i;X_i]\big) \\
&\leq 3 \mathbb{H}[S] - \tfrac{3}{2} \mathbb{H}[X_1] - \tfrac{3}{2} \mathbb{H}[X_2]\\
&\leq (6 - 3\eta) k + 3(2 \eta k - I_1)
\end{aligned}
$$

as required.

## Lean

Formalized as [`sum_dist_diff_le`](https://teorth.github.io/pfr/docs/find/#doc/sum_dist_diff_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 280](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L280)
