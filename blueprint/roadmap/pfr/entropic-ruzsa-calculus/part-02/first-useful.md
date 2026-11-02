---
declaration: lemma
origin: cited
lean: condRuzsaDist_diff_le, condRuzsaDist_diff_le', condRuzsaDist_diff_le'', condRuzsaDist_diff_le'''
statement: formalized
proof: formalized
---

# Comparison of Ruzsa distances, I

Let $X, Y, Z$ be random variables taking values in some abelian group of characteristic $2$, and with $Y, Z$ independent. Then we have

$$
\begin{aligned} d[X ; Y + Z] -d[X ; Y] &  \leq \tfrac{1}{2} (\mathbb{H}[Y+ Z] - \mathbb{H}[Y]) \\ & = \tfrac{1}{2} d[Y; Z] + \tfrac{1}{4} \mathbb{H}[Z] - \tfrac{1}{4} \mathbb{H}[Y].\qquad\text{(8)}\end{aligned}
$$

and

$$
\begin{aligned}
d[X ;Y|Y+ Z] - d[X ;Y] & \leq \tfrac{1}{2} \bigl(\mathbb{H}[Y+ Z] - \mathbb{H}[Z]\bigr) \\ & = \tfrac{1}{2} d[Y;Z] + \tfrac{1}{4} \mathbb{H}[Y] - \tfrac{1}{4} \mathbb{H}[Z].\qquad\text{(9)}\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Copy preserves Ruzsa distance](../part-01/ruz-copy.md)
- [Existence of independent copies](../part-01/independent-exist.md)
- [Kaimanovich-Vershik-Madiman inequality](kv.md)
- [Ruzsa distance in independent case](../part-01/ruz-indep.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Upper bound on conditioned Ruzsa distance](cond-dist-fact.md)

## Proof

We first prove (8). We may assume (taking an independent copy, using [Existence of independent copies](../part-01/independent-exist.md) and [Copy preserves Ruzsa distance](../part-01/ruz-copy.md), [Ruzsa distance in independent case](../part-01/ruz-indep.md)) that $X$ is independent of $Y, Z$. Then we have

$$
\begin{aligned}  d[X ;Y+ Z] & - d[X ;Y] \\ & = \mathbb{H}[X + Y + Z] - \mathbb{H}[X + Y] - \tfrac{1}{2}\mathbb{H}[Y + Z] + \tfrac{1}{2} \mathbb{H}[Y].\end{aligned}
$$

Combining this with [Kaimanovich-Vershik-Madiman inequality](kv.md) gives the required bound. The second form of the result is immediate [Ruzsa distance in independent case](../part-01/ruz-indep.md).

Turning to (9), we have from [Mutual information](../../shannon-entropy-inequalities/part-01/information-def.md) and [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)

$$
\begin{aligned}  \mathbb{I}[Y : Y+ Z] & = \mathbb{H}[Y] + \mathbb{H}[Y + Z] - \mathbb{H}[Y, Y + Z] \\ & = \mathbb{H}[Y] + \mathbb{H}[Y + Z] - \mathbb{H}[Y, Z]  = \mathbb{H}[Y + Z] - \mathbb{H}[Z],\end{aligned}
$$

and so (9) is a consequence of [Upper bound on conditioned Ruzsa distance](cond-dist-fact.md). Once again the second form of the result is immediate from [Ruzsa distance in independent case](../part-01/ruz-indep.md).

## Lean

Formalized as [`condRuzsaDist_diff_le`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_diff_le), [`condRuzsaDist_diff_le'`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_diff_le'), [`condRuzsaDist_diff_le''`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_diff_le''), [`condRuzsaDist_diff_le'''`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_diff_le''').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 327](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L327)
