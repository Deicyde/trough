---
declaration: corollary
origin: cited
lean: exists_isUniform_of_rdist_eq_zero
statement: formalized
proof: formalized
---

# General 100% inverse theorem

Suppose that $X_1,X_2$ are $G$-valued random variables such that $d[X_1;X_2]=0$. Then there exists a subgroup $H \leq G$ such that $d[X_1;U_H] = d[X_2;U_H] = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Symmetric 100% inverse theorem](lem-100pc-self.md)
- [Ruzsa triangle inequality](../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)
- [Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md)

## Proof

Using [Ruzsa triangle inequality](../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md) and [Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md) we have $d[X_1;X_1]=0$, hence by [Symmetric 100% inverse theorem](lem-100pc-self.md) $d[X_1;U_H]=0$ for some subgroup $H$. By [Ruzsa triangle inequality](../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md) and [Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md) again we also have $d[X_2;U_H]$ as required.

## Lean

Formalized as [`exists_isUniform_of_rdist_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/exists_isUniform_of_rdist_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/100_percent.tex, line 51](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/100_percent.tex#L51)
