---
declaration: lemma
origin: cited
lean: diff_rdist_le_1, diff_rdist_le_2, diff_rdist_le_3, diff_rdist_le_4
statement: formalized
proof: formalized
---

# Upper bound on distance differences

We have

$$
\begin{aligned}
d[X^0_1; X_1+\tilde X_2] - d[X^0_1; X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \mathbb{H}[X_2] - \tfrac{1}{4} \mathbb{H}[X_1]\\
d[X^0_2;X_2+\tilde X_1] - d[X^0_2; X_2] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \mathbb{H}[X_1] - \tfrac{1}{4} \mathbb{H}[X_2], \\
d[X_1^0;X_1|X_1+\tilde X_2] - d[X_1^0;X_1] &\leq \tfrac{1}{2} k + \tfrac{1}{4} \mathbb{H}[X_1] - \tfrac{1}{4} \mathbb{H}[X_2]  \\
d[X_2^0; X_2|X_2+\tilde X_1] - d[X_2^0; X_2] &\leq \tfrac{1}{2}k + \tfrac{1}{4} \mathbb{H}[X_2] - \tfrac{1}{4} \mathbb{H}[X_1].
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md)

## Proof

Immediate from [Comparison of Ruzsa distances, I](../../entropic-ruzsa-calculus/part-02/first-useful.md) (and recalling that $k$ is defined to be $d[X_1;X_2]$).

## Lean

Formalized as [`diff_rdist_le_1`](https://teorth.github.io/pfr/docs/find/#doc/diff_rdist_le_1), [`diff_rdist_le_2`](https://teorth.github.io/pfr/docs/find/#doc/diff_rdist_le_2), [`diff_rdist_le_3`](https://teorth.github.io/pfr/docs/find/#doc/diff_rdist_le_3), [`diff_rdist_le_4`](https://teorth.github.io/pfr/docs/find/#doc/diff_rdist_le_4).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 115](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy_pfr.tex#L115)
