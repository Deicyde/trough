---
declaration: lemma
origin: cited
lean: condRuzsaDist_le, condRuzsaDist_le'
statement: formalized
proof: formalized
---

# Upper bound on conditioned Ruzsa distance

Suppose that $(X, Z)$ and $(Y, W)$ are random variables, where $X, Y$ take values in an abelian group. Then

$$
d[X  | Z;Y | W] \leq d[X ; Y] + \tfrac{1}{2}  \mathbb{I}[X : Z] + \tfrac{1}{2}  \mathbb{I}[Y : W].
$$

In particular,

$$
d[X ;Y | W] \leq d[X ; Y] + \tfrac{1}{2}  \mathbb{I}[Y : W].
$$

## Depends on

- [Conditioned Ruzsa distance](../part-01/cond-dist-def.md)
- [Mutual information](../../shannon-entropy-inequalities/part-01/information-def.md)

## Proof depends on

- [Alternate form of distance](../part-01/cond-dist-alt.md)
- [Existence of independent copies](../part-01/independent-exist.md)
- [Conditioning reduces entropy](../../shannon-entropy-inequalities/part-01/cond-reduce.md)

## Proof

Using [Alternate form of distance](../part-01/cond-dist-alt.md) and [Existence of independent copies](../part-01/independent-exist.md), if $(X',Z'), (Y',W')$ are independent copies of the variables $(X,Z)$, $(Y,W)$, we have

$$
\begin{aligned}
d[X  | Z; Y | W]&= \mathbb{H}[X'-Y'|Z',W'] - \tfrac{1}{2} \mathbb{H}[X'|Z'] - \tfrac{1}{2}H[Y'|W'] \\
&\le \mathbb{H}[X'-Y']- \tfrac{1}{2} \mathbb{H}[X'|Z'] - \tfrac{1}{2}H[Y'|W'] \\
&= d[X';Y'] + \tfrac{1}{2}  \mathbb{I}[X' : Z'] + \tfrac{1}{2}  \mathbb{I}[Y' : W'].
\end{aligned}
$$

Here, in the middle step we used [Conditioning reduces entropy](../../shannon-entropy-inequalities/part-01/cond-reduce.md), and in the last step we used [Ruzsa distance](../part-01/ruz-dist-def.md) and [Mutual information](../../shannon-entropy-inequalities/part-01/information-def.md).

## Lean

Formalized as [`condRuzsaDist_le`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_le), [`condRuzsaDist_le'`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_le').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 307](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L307)
