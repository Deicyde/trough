---
declaration: lemma
origin: cited
lean: sub_multiDistance_le
statement: formalized
proof: formalized
---

# Lower bound on multidistance

If $(X_i)_{1 \leq i \leq m}$ is a $\tau$-minimizer, and $k := D[(X_i)_{1 \leq i \leq m}]$, then for any other tuple $(X'_i)_{1 \leq i \leq m}$, one has

$$
k - D[(X'_i)_{1 \leq i \leq m}] \leq \eta \sum_{i=1}^m d[X_i; X'_i].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [$\tau$-minimizer](tau-min-multi.md)
- [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)

## Proof

By [$\tau$-minimizer](tau-min-multi.md) we have

$$
\tau[ (X_i)_{1 \leq i \leq m}] \leq \tau[ (X'_i)_{1 \leq i \leq m}]
$$

and hence by [$\tau$-functional](tau-def-multi.md)

$$
k + \eta \sum_{i=1}^m d[X_i; X^0] \leq D[(X'_i)_{1 \leq i \leq m}] + \eta \sum_{i=1}^m d[X'_i; X^0].
$$

On the other hand, by [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md) we have

$$
d[X'_i; X^0] \leq d[X_i; X^0] + d[X_i; X'_i].
$$

The claim follows.

## Lean

Formalized as [`sub_multiDistance_le`](https://teorth.github.io/pfr/docs/find/#doc/sub_multiDistance_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 315](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L315)
