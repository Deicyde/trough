---
declaration: lemma
origin: cited
lean: dist_diff_bound_1, dist_diff_bound_2
statement: formalized
proof: formalized
---

# Bound on distance differences

We have

$$
\begin{aligned}  &\sum_{i=1}^2 \sum_{A,B \in \{U,V,W\}: A \neq B}  d[X_i^0;A|B, S] - d[X_i^0;X_i]\\
&\qquad \leq 12 k + \frac{4(2 \eta k - I_1)}{1-\eta}.
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [General inequality](gen-ineq.md)
- [Conditional entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md)
- [second-estimate-aux](../entropy-version-of-pfr/second-estimate/second-estimate-aux.md)

## Proof

If we apply [General inequality](gen-ineq.md) with $X_1:=X_1$, $Y:=X_1^0$ and $(X_2,X_3,X_4)$ equal to the $3!$ permutations of $(X_2,\tilde X_1,\tilde X_2)$, and sums (using the symmetry $\mathbb{H}[X|X+Y] = \mathbb{H}[Y|X+Y]$, which follows from [Conditional entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md)), we can bound

$$
\sum_{A,B \in \{U,V,W\}: A \neq B}  d[X_1^0;A|B, S] - d[X_1^0;X_1]
$$

by

$$
\begin{aligned}
&\quad \tfrac{1}{4} (6d[X_1;X_2] + 6d[X_1;\tilde X_2]\\
&\qquad + 6d[X_1;\tilde X_1] + 2d[\tilde X_1;\tilde X_2] + 2 d[\tilde X_1;X_2] + 2d[X_2;\tilde X_2])\\
&\quad + \tfrac{1}{8} (2\mathbb{H}[X_1+X_2] + 2\mathbb{H}[X_1+\tilde X_1] + 2 \mathbb{H}[X_1+\tilde X_2] \\
&\qquad - 2\mathbb{H}[\tilde X_1+X_2] - 2\mathbb{H}[X_2+\tilde X_2] - 2\mathbb{H}[\tilde X_1+\tilde X_2])\\
&\qquad \qquad + \tfrac{1}{4} (\mathbb{H}[X_2|X_2+\tilde X_2] + \mathbb{H}[\tilde X_1|\tilde X_1+\tilde X_2] + \mathbb{H}[\tilde X_1|X_1+\tilde X_2] \\
&\qquad \qquad \qquad - \mathbb{H}[X_1|X_1+\tilde X_1] - \mathbb{H}[X_1|X_1+X_2] - \mathbb{H}[X_1|X_1+\tilde X_2]),
\end{aligned}
$$

which simplifies to

$$
\begin{aligned}
&\quad \tfrac{1}{4} (16k + 6d[X_1;X_1] + 2d[X_2;X_2])\\
&\qquad \qquad + \tfrac{1}{4} (H[X_1+\tilde X_1] - H[X_2+\tilde X_2] + d[X_2|X_2+\tilde X_2] - d[X_1|X_1+\tilde X_1]).
\end{aligned}
$$

A symmetric argument also bounds

$$
\sum_{A,B \in \{U,V,W\}: A \neq B}  d[X_2^0;A|B, S] - d[X_2^0;X_2]
$$

by

$$
\begin{aligned}
&\quad \tfrac{1}{4} (16k + 6d[X_2;X_2] + 2d[X_1;X_1])\\
&\qquad \qquad + \tfrac{1}{4} (H[X_2+\tilde X_2] - H[X_1+\tilde X_1] + d[X_1|X_1+\tilde X_1] - d[X_2|X_2+\tilde X_2]).
\end{aligned}
$$

On the other hand, from [Lemma second-estimate-aux](../entropy-version-of-pfr/second-estimate/second-estimate-aux.md) one has

$$
d[X_1;X_1] + d[X_2;X_2] \leq 2 k + \frac{2(2 \eta k - I_1)}{1-\eta}.
$$

Summing the previous three estimates, we obtain the claim.

## Lean

Formalized as [`dist_diff_bound_1`](https://teorth.github.io/pfr/docs/find/#doc/dist_diff_bound_1), [`dist_diff_bound_2`](https://teorth.github.io/pfr/docs/find/#doc/dist_diff_bound_2).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 139](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/improved_exponent.tex#L139)
