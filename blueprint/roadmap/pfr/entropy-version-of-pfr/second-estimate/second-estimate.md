---
declaration: lemma
origin: cited
lean: second_estimate
statement: formalized
proof: formalized
---

# Second estimate

We have

$$
I_2 \leq 2 \eta k + \frac{2 \eta (2 \eta k - I_1)}{1 - \eta}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md)
- [Distance lower bound](../basic-facts-about-minimizers/distance-lower.md)
- [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md)
- [second-estimate-aux](second-estimate-aux.md)

## Proof

We apply [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md), but now with the choice

$$
(Y_1,Y_2,Y_3,Y_4) := (X_2, X_1, \tilde X_2, \tilde X_1).
$$

Now [Specific fibring identity](../../the-fibring-lemma/cor-fibre.md) can be rewritten as

$$
\begin{aligned}
&d[X_1+\tilde X_1;X_2+\tilde X_2] + d[X_1|X_1+\tilde X_1; X_2|X_2+\tilde X_2] \\
&\quad + \mathbb{I}[X_1+X_2 : X_1 + \tilde X_1 \,|\, X_1+X_2+\tilde X_1+\tilde X_2] = 2k,
\end{aligned}
$$

recalling once again that $k := d[X_1;X_2]$. From [Conditional distance lower bound](../basic-facts-about-minimizers/cond-distance-lower.md) one has

$$
\begin{aligned}
d[X_1|X_1+\tilde X_1; X_2|X_2+\tilde X_2]   \geq k &- \eta (d[X^0_1;X_1] - d[X^0_1;X_1|X_1+\tilde X_1]) \\& - \eta (d[X^0_2;X_2] - d[X^0_2;X_2|X_2+\tilde X_2]) .
\end{aligned}
$$

while from [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md) we have

$$
d[X^0_1;X_1|X_1+\tilde X_1] -  d[X^0_1;X_1] \leq  \tfrac{1}{2} d[X_1;X_1],
$$

and

$$
d[X^0_2;X_2|X_2+\tilde X_2] -  d[X^0_2;X_2] \leq \tfrac{1}{2} d[X_1;X_2].
$$

Combining all these inequalities with [Distance between sums](dist-sums.md), we have

$$
\mathbb{I}[X_1+X_2 : X_1 + \tilde X_1 | X_1+X_2+\tilde X_1+\tilde X_2] \leq \eta ( d[X_1; X_1] + d[X_2; X_2] ).
$$

Together with [Lemma second-estimate-aux](second-estimate-aux.md), this gives the conclusion.

## Lean

Formalized as [`second_estimate`](https://teorth.github.io/pfr/docs/find/#doc/second_estimate).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 202](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L202)
