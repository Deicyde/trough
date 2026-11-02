---
declaration: definition
origin: cited
lean: multiTau
statement: formalized
---

# $\tau$-functional

If $(X_i)_{1 \leq i \leq m}$ is a tuple, we define its $\tau$-functional

$$
\tau[ (X_i)_{1 \leq i \leq m}] := D[(X_i)_{1 \leq i \leq m}] + \eta \sum_{i=1}^m d[X_i; X^0].
$$

## Depends on

- [Multidistance](../multidistance/multidist-def.md)

## Lean

Formalized as [`multiTau`](https://teorth.github.io/pfr/docs/find/#doc/multiTau).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 285](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L285)
