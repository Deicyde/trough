---
declaration: definition
origin: cited
lean: condMultiDist
statement: formalized
---

# Conditional multidistance

If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are tuples of random variables, with the $X_i$ being $G$-valued (but the $Y_i$ need not be), then we define

$$
D[ X_{[m]} | Y_{[m]} ] = \sum_{(y_i)_{1 \leq i \leq m}} \biggl(\prod_{1 \leq i \leq m} p_{Y_i}(y_i)\biggr) D[ (X_i \,|\, Y_i \mathop{=}y_i)_{1 \leq i \leq m}]\qquad\text{(1)}
$$

where each $y_i$ ranges over the support of $p_{Y_i}$ for $1 \leq i \leq m$.

## Depends on

- [Multidistance](../multidistance/multidist-def.md)

## Lean

Formalized as [`condMultiDist`](https://teorth.github.io/pfr/docs/find/#doc/condMultiDist).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 329](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L329)
