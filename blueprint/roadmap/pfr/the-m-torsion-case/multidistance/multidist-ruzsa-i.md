---
declaration: lemma
origin: cited
lean: multidist_ruzsa_I
statement: formalized
proof: formalized
---

# Multidistance and Ruzsa distance, I

Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. Then

$$
\sum_{1 \leq j,k \leq m: j \neq k} d[X_j; -X_k] \leq m(m-1) D[X_{[m]}].
$$

## Depends on

- [Multidistance](multidist-def.md)

## Proof depends on

- [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md)
- [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Multidistance of independent variables](multidist-indep.md)
- [Multidistance of copy](multidist-copy.md)

## Proof

By [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md), [Multidistance of copy](multidist-copy.md) we may take the $X_i$ to be jointly independent. From [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md), we see that for any distinct $1 \leq j,k \leq m$, we have

$$
\mathbb{H}[X_j+X_k] \leq \mathbb{H}[\sum_{i=1}^m X_i],
$$

and hence by [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)

$$
d[X_j;-X_k] \leq \mathbb{H}[\sum_{i=1}^m X_i] - \frac{1}{2} \mathbb{H}[X_j] - \frac{1}{2} \mathbb{H}[X_k].
$$

Summing this over all pairs $(j,k)$, $j \neq k$ and using Lemma [Multidistance of independent variables](multidist-indep.md), we obtain the claim.

## Lean

Formalized as [`multidist_ruzsa_I`](https://teorth.github.io/pfr/docs/find/#doc/multidist_ruzsa_I).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 205](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L205)
