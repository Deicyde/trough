---
declaration: lemma
origin: cited
lean: construct_good
statement: formalized
proof: formalized
---

# Constructing good variables, II

One has

$$
\begin{aligned}  k & \leq  \delta + \frac{\eta}{3} \biggl( \delta + \sum_{i=1}^2 \sum_{j = 1}^3 (d[X^0_i;T_j] - d[X^0_i; X_i]) \biggr).
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Constructing good variables, I](construct-good-prelim.md)

## Proof

Average [Constructing good variables, I](construct-good-prelim.md) over all six permutations of $T_1,T_2,T_3$.

## Lean

Formalized as [`construct_good`](https://teorth.github.io/pfr/docs/find/#doc/construct_good).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 367](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L367)
