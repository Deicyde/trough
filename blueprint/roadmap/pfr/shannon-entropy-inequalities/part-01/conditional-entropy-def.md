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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 112](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L112)
