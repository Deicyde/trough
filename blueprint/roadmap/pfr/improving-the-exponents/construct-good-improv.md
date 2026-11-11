---
declaration: lemma
origin: cited
lean: construct_good_improved'
statement: formalized
proof: formalized
---

# Constructing good variables, II'

One has

$$
\begin{aligned}  k & \leq  \delta + \frac{\eta}{6}  \sum_{i=1}^2 \sum_{1 \leq j,l \leq 3; j \neq l} (d[X^0_i;T_j|T_l] - d[X^0_i; X_i])
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Constructing good variables, I'](construct-good-prelim-improv.md)

## Proof

Average [Constructing good variables, I'](construct-good-prelim-improv.md) over all six permutations of $T_1,T_2,T_3$.

## Lean

Formalized as [`construct_good_improved'`](https://teorth.github.io/pfr/docs/find/#doc/construct_good_improved').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 57](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/improved_exponent.tex#L57)
