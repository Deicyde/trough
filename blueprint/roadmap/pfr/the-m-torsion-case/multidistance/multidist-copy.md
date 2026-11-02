---
declaration: lemma
origin: cited
lean: multiDist_copy
statement: formalized
proof: formalized
---

# Multidistance of copy

If $X_{[m]} = (X_i)_{1 \leq i \leq m}$ and $Y_{[m]} = (Y_i)_{1 \leq i \leq m}$ are such that $X_i$ and $Y_i$ have the same distribution for each $i$, then $D[X_{[m]}] = D[Y_{[m]}]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Multidistance](multidist-def.md)

## Proof

Clear from Lemma [Copy preserves entropy](../../entropic-ruzsa-calculus/part-01/copy-ent.md).

## Lean

Formalized as [`multiDist_copy`](https://teorth.github.io/pfr/docs/find/#doc/multiDist_copy).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 179](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L179)
