---
declaration: lemma
origin: cited
lean: sub_condMultiDistance_le
statement: formalized
proof: formalized
---

# Lower bound on conditional multidistance

If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, and $k := D[(X_i)_{1 \leq i \leq m}]$, then for any other tuples $(X'_i)_{1 \leq i \leq m}$ and $(Y_i)_{1 \leq i \leq m}$ with the $X'_i$ $G$-valued, one has

$$
k - D[(X'_i)_{1 \leq i \leq m} | (Y_i)_{1 \leq i \leq m}] \leq \eta \sum_{i=1}^m d[X_i; X'_i|Y_i].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Lower bound on multidistance](multidist-lower.md)
- [Conditional multidistance](cond-multidist-def.md)
- [Alternate form of conditional multidistance](cond-multidist-alt.md)

## Proof

Immediate from [Lower bound on multidistance](multidist-lower.md), [Alternate form of conditional multidistance](cond-multidist-alt.md), and [Conditioned Ruzsa distance](../../entropic-ruzsa-calculus/part-01/cond-dist-def.md).

## Lean

Formalized as [`sub_condMultiDistance_le`](https://teorth.github.io/pfr/docs/find/#doc/sub_condMultiDistance_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 355](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L355)
