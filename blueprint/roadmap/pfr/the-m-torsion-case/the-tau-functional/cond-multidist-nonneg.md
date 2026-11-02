---
declaration: lemma
origin: cited
lean: condMultiDist_nonneg
statement: formalized
proof: formalized
---

# Conditional multidistance nonnegative

If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are tuples of random variables, then $D[ X_{[m]} | Y_{[m]} ] \geq 0$.

## Depends on

- [Conditional multidistance](cond-multidist-def.md)

## Proof depends on

- [Nonnegativity](../multidistance/multidist-nonneg.md)

## Proof

Clear from [Nonnegativity](../multidistance/multidist-nonneg.md) and [Conditional multidistance](cond-multidist-def.md), except that some care may need to be taken to deal with the $y_i$ where $p_{Y_i}$ vanish.

## Lean

Formalized as [`condMultiDist_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/condMultiDist_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 348](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L348)
