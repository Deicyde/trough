---
declaration: lemma
origin: cited
lean: ent_sub_nsmul_le, ent_of_sub_smul'
statement: formalized
proof: formalized
---

# Sums of dilates I

Let $X,Y,X'$ be independent $G$-valued random variables, with $X'$ a copy of $X$, and let $a$ be an integer. Then

$$
\mathbb{H}[X-(a+1)Y] \leq \mathbb{H}[X-aY] + \mathbb{H}[X-Y-X'] - \mathbb{H}[X]
$$

and

$$
\mathbb{H}[X-(a-1)Y] \leq \mathbb{H}[X-aY] + \mathbb{H}[X-Y-X'] - \mathbb{H}[X].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Improved Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle-improved.md)
- [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md)

## Proof

From [Improved Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle-improved.md) we have

$$
\mathbb{H}[(X-Y)-aY] \leq \mathbb{H}[(X-Y) - X'] + \mathbb{H}[X'-aY] - \mathbb{H}[X']
$$

which gives the first inequality. Similarly from [Improved Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle-improved.md) we have

$$
\mathbb{H}[(X+Y)-aY] \leq \mathbb{H}[(X+Y) - X'] + \mathbb{H}[X'-aY] - \mathbb{H}[X']
$$

which (when combined with [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md)) gives the second inequality.

## Lean

Formalized as [`ent_sub_nsmul_le`](https://teorth.github.io/pfr/docs/find/#doc/ent_sub_nsmul_le), [`ent_of_sub_smul'`](https://teorth.github.io/pfr/docs/find/#doc/ent_of_sub_smul').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 125](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L125)
