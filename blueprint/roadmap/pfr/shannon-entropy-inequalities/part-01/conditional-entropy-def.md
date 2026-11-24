---
declaration: definition
origin: cited
lean: ProbabilityTheory.condEntropy
statement: formalized
---

# Conditional entropy

If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, the conditional entropy $\mathbb{H}[X|Y]$ is defined as

$$
\mathbb{H}[X|Y] := \sum_{y \in Y} \mathbb{P}[Y = y] \mathbb{H}[(X | Y=y)].
$$

## Depends on

- [Entropy](entropy-def.md)
- [Conditioned event](condition-event-def.md)

## Lean

Formalized as [`ProbabilityTheory.condEntropy`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 112](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy.tex#L112)
