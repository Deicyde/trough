---
declaration: proposition
origin: cited
lean: multidist_eq_zero
statement: formalized
proof: formalized
---

# Vanishing

If $D[X_{[m]}]=0$, then for each $1 \leq i \leq m$ there is a finite subgroup $H_i \leq G$ such that $d[X_i; U_{H_i}] = 0$.

## Depends on

- [Multidistance](multidist-def.md)

## Proof depends on

- [Multidistance and Ruzsa distance, I](multidist-ruzsa-i.md)
- [Distance nonnegative](../../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md)
- [General 100% inverse theorem](../../the-100-version-of-pfr/lem-100pc.md)

## Proof

From [Multidistance and Ruzsa distance, II](multidist-ruzsa-ii.md) and [Distance nonnegative](../../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md) we have $d[X_j; X_j]=0$ for all $1 \leq j \leq m$. The claim now follows from [General 100% inverse theorem](../../the-100-version-of-pfr/lem-100pc.md).

## Lean

Formalized as [`multidist_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/multidist_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 268](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L268)
