---
declaration: definition
origin: cited
lean: ProbabilityTheory.entropy
statement: formalized
---

# Entropy

If $X$ is an $S$-valued random variable, the entropy $\mathbb{H}[X]$ of $X$ is defined

$$
\mathbb{H}[X] := \sum_{s \in S} \mathbb{P}[X=x] \log \frac{1}{\mathbb{P}[X=x]}
$$

with the convention that $0 \log \frac{1}{0} = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.entropy`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 5](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy.tex#L5)
