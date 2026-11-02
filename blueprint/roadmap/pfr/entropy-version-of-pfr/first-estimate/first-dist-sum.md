---
declaration: lemma
origin: cited
lean: rdist_of_sums_ge
statement: formalized
proof: formalized
---

# Lower bound on distances

We have

$$
\begin{aligned}
d[X_1+\tilde X_2; X_2+\tilde X_1] \geq k &- \eta (d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1]) \\& \qquad- \eta (d[X^0_2; X_2+\tilde X_1] - d[X^0_2; X_2])
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Distance lower bound](../basic-facts-about-minimizers/distance-lower.md)

## Proof

Immediate from [Distance lower bound](../basic-facts-about-minimizers/distance-lower.md).

## Lean

Formalized as [`rdist_of_sums_ge`](https://teorth.github.io/pfr/docs/find/#doc/rdist_of_sums_ge).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 91](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L91)
