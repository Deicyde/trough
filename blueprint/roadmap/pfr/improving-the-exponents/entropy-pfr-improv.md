---
declaration: theorem
origin: cited
lean: entropic_PFR_conjecture_improv
statement: formalized
proof: formalized
---

# Improved entropy version of PFR

Let $G = \mathbb{F}_2^n$, and suppose that $X^0_1, X^0_2$ are $G$-valued random variables. Then there is some subgroup $H \leq G$ such that

$$
d[X^0_1;U_H] + d[X^0_2;U_H] \le 10 d[X^0_1;X^0_2],
$$

where $U_H$ is uniformly distributed on $H$. Furthermore, both $d[X^0_1;U_H]$ and $d[X^0_2;U_H]$ are at most $\tfrac{11}{2} d[X^0_1;X^0_2]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Limiting improved $\tau$-decrement](de-prop-lim-improv.md)
- [General 100% inverse theorem](../the-100-version-of-pfr/lem-100pc.md)
- [Ruzsa triangle inequality](../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)

## Proof

Let $X_1, X_2$ be the good $\tau$-minimizer from [Limiting improved $\tau$-decrement](de-prop-lim-improv.md). By construction, $d[X_1;X_2]=0$. From [General 100% inverse theorem](../the-100-version-of-pfr/lem-100pc.md), $d[X_1;U_H] = d[X_2; U_H] = 0$. Also from $\tau$-minimization we have $\tau[X_1;X_2] \leq \tau[X^0_2;X^0_1]$. Using this and the Ruzsa triangle inequality we can conclude.

## Lean

Formalized as [`entropic_PFR_conjecture_improv`](https://teorth.github.io/pfr/docs/find/#doc/entropic_PFR_conjecture_improv).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 197](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/improved_exponent.tex#L197)
