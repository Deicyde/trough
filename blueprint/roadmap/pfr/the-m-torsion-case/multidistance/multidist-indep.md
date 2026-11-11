---
declaration: lemma
origin: cited
lean: multiDist_indep
statement: formalized
proof: formalized
---

# Multidistance of independent variables

If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ are jointly independent, then $D[X_{[m]}] = \mathbb{H}[\sum_{i=1}^m X_i] - \frac{1}{m} \sum_{i=1}^m \mathbb{H}[X_i]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Multidistance](multidist-def.md)

## Proof

Clear from definition.

## Lean

Formalized as [`multiDist_indep`](https://teorth.github.io/pfr/docs/find/#doc/multiDist_indep).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 185](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L185)
