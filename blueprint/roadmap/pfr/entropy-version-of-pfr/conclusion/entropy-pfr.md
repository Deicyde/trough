---
declaration: theorem
origin: cited
lean: entropic_PFR_conjecture
statement: formalized
proof: formalized
---

# Entropy version of PFR

Let $G = \mathbb{F}_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that

$$
d[X^0_1;U_H] + d[X^0_2;U_H] \le 11 d[X^0_1;X^0_2],
$$

where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $6 d[X^0_1;X^0_2]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [$\tau$-decrement](../endgame/de-prop.md)
- [$\tau$ has minimum](../tau-min.md)
- [General 100% inverse theorem](../../the-100-version-of-pfr/lem-100pc.md)
- [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)

## Proof

Let $X_1, X_2$ be the $\tau$-minimizer from [$\tau$ has minimum](../tau-min.md). From [$\tau$-decrement](../endgame/de-prop.md), $d[X_1;X_2]=0$. From [General 100% inverse theorem](../../the-100-version-of-pfr/lem-100pc.md), $d[X_1;U_H] = d[X_2; U_H] = 0$. Also from $\tau$-minimization we have $\tau[X_1;X_2] \leq \tau[X^0_2;X^0_1]$. Using this and the Ruzsa triangle inequality we can conclude.

## Lean

Formalized as [`entropic_PFR_conjecture`](https://teorth.github.io/pfr/docs/find/#doc/entropic_PFR_conjecture).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 417](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L417)
