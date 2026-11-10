---
declaration: lemma
origin: cited
lean: averaged_construct_good
statement: formalized
proof: formalized
---

# Constructing good variables, III'

One has

$$
\begin{aligned}  k & \leq I(U : V \, | \, S) + I(V : W \, | \,S) + I(W : U \, | \, S) + \frac{\eta}{6}  \sum_{i=1}^2 \sum_{A,B \in \{U,V,W\}: A \neq B} (d[X^0_i;A|B,S] - d[X^0_i; X_i]).
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Constructing good variables, II'](construct-good-improv.md)
- [Key identity](../entropy-version-of-pfr/endgame/key-ident.md)

## Proof

For each $s$ in the range of $S$, apply [Constructing good variables, II'](construct-good-improv.md) with $T_1,T_2,T_3$ equal to $(U|S=s)$, $(V|S=s)$, $(W|S=s)$ respectively (which works thanks to [Key identity](../entropy-version-of-pfr/endgame/key-ident.md)), multiply by $\mathbb{P}[S=s]$, and sum in $s$ to conclude.

## Lean

Formalized as [`averaged_construct_good`](https://teorth.github.io/pfr/docs/find/#doc/averaged_construct_good).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 77](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/improved_exponent.tex#L77)
