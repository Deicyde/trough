---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condIndep_copies
statement: formalized
proof: formalized
---

# Existence of conditional independent trials

For $X,Y$ random variables, there exist random variables $X_1,X_2,Y'$ on a common probability space with $(X_1, Y'), (X_2, Y')$ both having the distribution of $(X,Y)$, and $X_1, X_2$ conditionally independent over $Y'$ in the sense of [Conditionally independent random variables](../../shannon-entropy-inequalities/part-02/conditional-independent-def.md).

## Depends on

- [Conditionally independent random variables](../../shannon-entropy-inequalities/part-02/conditional-independent-def.md)

## Proof

Explicit construction.

## Lean

Formalized as [`ProbabilityTheory.condIndep_copies`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condIndep_copies).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 256](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/distance.tex#L256)
