---
declaration: lemma
origin: cited
lean: rdist_of_sums_ge'
statement: formalized
proof: formalized
---

# Distance between sums

We have

$$
d[X_1+\tilde X_1; X_2+\tilde X_2] \geq k - \frac{\eta}{2} ( d[X_1; X_1] + d[X_2;X_2] ).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Distance lower bound](../basic-facts-about-minimizers/distance-lower.md)
- [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md)

## Proof

From [Distance lower bound](../basic-facts-about-minimizers/distance-lower.md) one has

$$
\begin{aligned}
d[X_1+\tilde X_1; X_2+\tilde X_2] \geq k &- \eta(d[X^0_1;X_1] - d[X^0_1;X_1+\tilde X_1]) \\
&- \eta(d[X^0_2;X_2] - d[X^0_2;X_2+\tilde X_2]).
\end{aligned}
$$

Now [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md) gives

$$
d[X^0_1;X_1+\tilde X_1] - d[X^0_1;X_1] \leq \tfrac{1}{2} d[X_1;X_1]
$$

and

$$
d[X^0_2;X_2+\tilde X_2] - d[X^0_2;X_2] \leq \tfrac{1}{2} d[X_2;X_2],
$$

and the claim follows.

## Lean

Formalized as [`rdist_of_sums_ge'`](https://teorth.github.io/pfr/docs/find/#doc/rdist_of_sums_ge').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 162](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L162)
