---
declaration: lemma
origin: cited
lean: dist_le_of_sum_zero
statement: formalized
proof: formalized
---

# rho-BSG-triplet

If $G$-valued random variables $T_1,T_2,T_3$ satisfy $T_1+T_2+T_3=0$, then

$$
d[X_1;X_2]\le 3\mathbb{I}[T_1:T_2] + (2\mathbb{H}[T_3]-\mathbb{H}[T_1]-\mathbb{H}[T_2])+ \eta(\rho(T_1|T_3)+\rho(T_2|T_3)-\rho(X_1)-\rho(X_2)).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Balog-Szemerédi-Gowers](../../entropic-ruzsa-calculus/part-02/entropic-bsg.md)
- [phi-min-def](phi-min-def.md)

## Proof

Conditioned on every $T_3=t$, $d[X_1;X_2]\le d[T_1|T_3=t;T_2|T_3=t]+\eta(\rho(T_1|T_3=t)+\rho(T_2|T_3=t)-\rho(X_1)-\rho(X_2))$ by [Definition phi-min-def](phi-min-def.md). Then take the weighted average with weight $\mathbf{P}(T_3=t)$ and then apply [Balog-Szemerédi-Gowers](../../entropic-ruzsa-calculus/part-02/entropic-bsg.md) to bound the RHS.

## Lean

Formalized as [`dist_le_of_sum_zero`](https://teorth.github.io/pfr/docs/find/#doc/dist_le_of_sum_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 262](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L262)
