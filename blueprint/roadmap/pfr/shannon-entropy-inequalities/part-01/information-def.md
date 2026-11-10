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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 159](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L159)
