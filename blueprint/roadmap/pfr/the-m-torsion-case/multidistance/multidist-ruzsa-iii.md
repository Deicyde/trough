---
declaration: lemma
origin: cited
lean: multidist_ruzsa_III
statement: formalized
proof: formalized
---

# Multidistance and Ruzsa distance, III

Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. If the $X_i$ all have the same distribution, then $D[X_{[m]}] \leq m d[X_i;X_i]$ for any $1 \leq i \leq m$.

## Depends on

- [Multidistance](multidist-def.md)

## Proof depends on

- [Kaimonovich–Vershik–Madiman inequality](../more-ruzsa-distance-estimates/klm-1.md)
- [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md)
- [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md)
- [Multidistance of copy](multidist-copy.md)
- [Multidistance of independent variables](multidist-indep.md)

## Proof

By [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md), [Multidistance of copy](multidist-copy.md) we may take the $X_i$ to be jointly independent. Let $X_0$ be a further independent copy of the $X_i$. From [Kaimonovich–Vershik–Madiman inequality](../more-ruzsa-distance-estimates/klm-1.md), we have

$$
\mathbb{H}[-X_0 + \sum_{i=1}^m X_i] - \mathbb{H}[-X_0] \leq \sum_{i=1}^m \mathbb{H}[X_0 - X_i] - \mathbb{H}[-X_0]
$$

and hence by [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md) and [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)

$$
\mathbb{H}[-X_0 + \sum_{i=1}^m X_i] - \mathbb{H}[X_0] \leq m d[X_i,X_i].
$$

On the other hand, by [Independent lower bound on sumset](../../entropic-ruzsa-calculus/part-01/sumset-lower.md) we have

$$
\mathbb{H}[\sum_{i=1}^m X_i] \leq \mathbb{H}[-X_0 + \sum_{i=1}^m X_i]
$$

and the claim follows.

## Lean

Formalized as [`multidist_ruzsa_III`](https://teorth.github.io/pfr/docs/find/#doc/multidist_ruzsa_III).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 231](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L231)
