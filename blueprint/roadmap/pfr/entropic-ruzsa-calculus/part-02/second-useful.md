---
declaration: lemma
origin: cited
lean: condRuzsaDist_diff_ofsum_le
statement: formalized
proof: formalized
---

# Comparison of Ruzsa distances, II

Let $X, Y, Z, Z'$ be random variables taking values in some abelian group, and with $Y, Z, Z'$ independent. Then we have

$$
\begin{aligned}
& d[X ;Y + Z | Y + Z + Z'] - d[X ;Y] \\ & \qquad \leq \tfrac{1}{2} ( \mathbb{H}[Y + Z + Z'] + \mathbb{H}[Y + Z] - \mathbb{H}[Y] - \mathbb{H}[Z']).\qquad\text{(10)}\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Comparison of Ruzsa distances, I](first-useful.md)

## Proof

By [Comparison of Ruzsa distances, I](first-useful.md) (with a change of variables) we have

$$
d[X ; Y + Z | Y + Z + Z'] - d[X ; Y + Z] \leq \tfrac{1}{2}( \mathbb{H}[Y + Z + Z'] - \mathbb{H}[Z']).
$$

Adding this to [(8)](first-useful.md) gives the result.

## Lean

Formalized as [`condRuzsaDist_diff_ofsum_le`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDist_diff_ofsum_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 349](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L349)
