---
declaration: theorem
origin: cited
lean: tau_minimizer_exists_rdist_eq_zero
statement: formalized
proof: formalized
---

# Limiting improved $\tau$-decrement

For $\eta = 1/8$, there exist tau-minimizers $X_1, X_2$ satisfying $d[X_1;X_2] = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Improved $\tau$-decrement](de-prop-improv.md)
- [$\tau$ has minimum](../entropy-version-of-pfr/tau-min.md)

## Proof

For each $\eta<1/8$, consider minimizers $X_1^\eta$ and $X_2^\eta$ from [$\tau$ has minimum](../entropy-version-of-pfr/tau-min.md). By [Improved $\tau$-decrement](de-prop-improv.md), they satisfy $d[X_1^\eta; X_2^\eta]=0$. By compactness of the space of probability measures on $G$, one may extract a converging subsequence of the distributions of $X_1^\eta$ and $X_2^\eta$ as $\eta \to 1/8$. By continuity of all the involved quantities, the limit is a pair of tau-minimizers for $1/8$ satisfying additionally $d[X_1;X_2] = 0$.

## Lean

Formalized as [`tau_minimizer_exists_rdist_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/tau_minimizer_exists_rdist_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 185](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/improved_exponent.tex#L185)
