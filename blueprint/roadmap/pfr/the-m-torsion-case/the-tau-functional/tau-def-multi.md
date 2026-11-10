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

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 285](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L285)
