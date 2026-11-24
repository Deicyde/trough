---
declaration: definition
origin: cited
lean: ProbabilityTheory.condMutualInfo
statement: formalized
---

# Conditional mutual information

If $X,Y,Z$ are random variables, with $Z$ $U$-valued, then

$$
\mathbb{I}[X:Y|Z] := \sum_{z \in U} P[Z=z] \mathbb{I}[(X|Z=z): (Y|Z=z)].
$$

## Depends on

- [Mutual information](../part-01/information-def.md)
- [Conditioned event](../part-01/condition-event-def.md)

## Lean

Formalized as [`ProbabilityTheory.condMutualInfo`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condMutualInfo).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 273](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy.tex#L273)
