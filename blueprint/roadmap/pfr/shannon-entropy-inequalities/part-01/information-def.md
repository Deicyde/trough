---
declaration: definition
origin: cited
lean: ProbabilityTheory.mutualInfo, ProbabilityTheory.mutualInfo_def
statement: formalized
---

# Mutual information

If $X: \Omega \to S$, $Y: \Omega \to T$ are random variables, then

$$
\mathbb{I}[X : Y] := \mathbb{H}[X] + \mathbb{H}[Y] - \mathbb{H}[X,Y].
$$

## Depends on

- [Entropy](entropy-def.md)

## Lean

Formalized as [`ProbabilityTheory.mutualInfo`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutualInfo), [`ProbabilityTheory.mutualInfo_def`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutualInfo_def).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 159](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy.tex#L159)
