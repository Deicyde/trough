---
declaration: lemma
origin: cited
lean: condRho_sum_le'
statement: formalized
proof: formalized
---

# rho-increase-symmetrized

For independent random variables $Y_1,Y_2,Y_3,Y_4$ over $G$, define $T_1:=Y_1+Y_2,T_2:=Y_1+Y_3,T_3:=Y_2+Y_3$ and $S:=Y_1+Y_2+Y_3+Y_4$. Then

$$
\sum_{1 \leq i\lt j \leq 3} (\rho(T_i|T_j,S) + \rho(T_j|T_i,S) -  \frac{1}{2}\sum_{i} \rho(Y_i))\le \sum_{1\leq i < j \leq 4}d[Y_i;Y_j]
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [rho-increase](rho-increase.md)

## Proof

Apply Lemma [rho-increase](rho-increase.md) on $(Y_i,Y_j,Y_k,Y_4)$ for $(i,j,k)=(1,2,3),(2,3,1),(1,3,2)$, and take the sum.

## Lean

Formalized as [`condRho_sum_le'`](https://teorth.github.io/pfr/docs/find/#doc/condRho_sum_le').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 311](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L311)
