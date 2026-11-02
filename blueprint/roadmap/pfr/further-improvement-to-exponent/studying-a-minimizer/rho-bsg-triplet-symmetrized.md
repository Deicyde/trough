---
declaration: lemma
origin: cited
lean: dist_le_of_sum_zero'
statement: formalized
proof: formalized
---

# rho-BSG-triplet-symmetrized

If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then

$$
d[X_1;X_2] \leq  \sum_{1 \leq i\lt j \leq 3} \mathbb{I}[T_i:T_j] + \frac{\eta}{3}   \sum_{1 \leq i\lt j \leq 3} (\rho(T_i|T_j) + \rho(T_j|T_i) -\rho(X_1)-\rho(X_2))
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [rho-BSG-triplet](rho-bsg-triplet.md)

## Proof

Take the average of [Lemma rho-BSG-triplet](rho-bsg-triplet.md) over all $6$ permutations of $T_1,T_2,T_3$.

## Lean

Formalized as [`dist_le_of_sum_zero'`](https://teorth.github.io/pfr/docs/find/#doc/dist_le_of_sum_zero').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 271](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L271)
