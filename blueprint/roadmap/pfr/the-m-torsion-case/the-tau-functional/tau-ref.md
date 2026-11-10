---
declaration: proposition
origin: cited
lean: multiTau_min_sum_le
statement: formalized
proof: formalized
---

# Minimizer close to reference variables

If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, then $\sum_{i=1}^m d[X_i; X^0] \leq \frac{2m}{\eta} d[X^0; X^0]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [$\tau$-minimizer](tau-min-multi.md)
- [Nonnegativity](../multidistance/multidist-nonneg.md)
- [Multidistance and Ruzsa distance, III](../multidistance/multidist-ruzsa-iii.md)

## Proof

By [$\tau$-minimizer](tau-min-multi.md) we have

$$
\tau[ (X_i)_{1 \leq i \leq m}] \leq \tau[ (X^0)_{1 \leq i \leq m}]
$$

and hence by [$\tau$-functional](tau-def-multi.md) and [Nonnegativity](../multidistance/multidist-nonneg.md)

$$
\eta \sum_{i=1}^m d[X_i; X^0] \leq D[(X^0)_{1 \leq i \leq m}] + m d[X^0; X^0].
$$

The claim now follows from [Multidistance and Ruzsa distance, III](../multidistance/multidist-ruzsa-iii.md).

## Lean

Formalized as [`multiTau_min_sum_le`](https://teorth.github.io/pfr/docs/find/#doc/multiTau_min_sum_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 305](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L305)
