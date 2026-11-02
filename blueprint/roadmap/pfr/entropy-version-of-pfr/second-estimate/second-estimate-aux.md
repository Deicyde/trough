---
declaration: lemma
origin: cited
lean: second_estimate_aux
statement: formalized
proof: formalized
---

# second-estimate-aux

We have

$$
d[X_1;X_1] + d[X_2;X_2] \leq 2 k + \frac{2(2 \eta k - I_1)}{1-\eta}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Entropy bound on quadruple sum](../first-estimate/foursum-bound.md)
- [Distance between sums](dist-sums.md)

## Proof

We may use [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md) to expand

$$
\begin{aligned}
& d[X_1+\tilde X_1;X_2+\tilde X_2] \\ &= \mathbb{H}[X_1+\tilde X_1 + X_2 + \tilde X_2]  - \tfrac{1}{2} \mathbb{H}[X_1+\tilde X_1] - \tfrac{1}{2} \mathbb{H}[X_2+\tilde X_2] \\
&= \mathbb{H}[X_1+\tilde X_1 + X_2 + \tilde X_2]  - \tfrac{1}{2} \mathbb{H}[X_1] - \tfrac{1}{2} \mathbb{H}[X_2]  \\ & \qquad\qquad\qquad   - \tfrac{1}{2} \left( d[X_1;X_1] + d[X_2; X_2] \right),
\end{aligned}
$$

and hence by [Entropy bound on quadruple sum](../first-estimate/foursum-bound.md)

$$
d[X_1+\tilde X_1; X_2+\tilde X_2] \leq (2+\eta) k - \tfrac{1}{2} \left( d[X_1;X_1] + d[X_2;X_2] \right) - I_1.
$$

Combining this bound with [Distance between sums](dist-sums.md) we obtain the result.

## Lean

Formalized as [`second_estimate_aux`](https://teorth.github.io/pfr/docs/find/#doc/second_estimate_aux).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 183](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L183)
