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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 159](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L159)
