---
declaration: definition
origin: cited
lean: TauMinimizes
statement: formalized
---

# $\tau$-minimizer

A pair of $G$-valued random variables $X_1, X_2$ are said to be a $\tau$-minimizer if one has

$$
\tau[X_1;X_2] \leq \tau[X'_1;X'_2]
$$

for all $G$-valued random variables $X'_1, X'_2$.

## Depends on

- [$\tau$ functional](tau-def.md)

## Lean

Formalized as [`TauMinimizes`](https://teorth.github.io/pfr/docs/find/#doc/TauMinimizes).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 26](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy_pfr.tex#L26)
