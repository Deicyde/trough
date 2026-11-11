---
declaration: definition
origin: cited
lean: ProbabilityTheory.CondIndepFun
statement: formalized
---

# Conditionally independent random variables

Two random variables $X: \Omega \to S$ and $Y: \Omega \to T$ are conditionally independent relative to another random variable $Z: \Omega \to U$ if $P[X = s \wedge Y = t| Z=u] = P[X=s|Z=u] P[Y=t|Z=u]$ for all $s \in S, t \in T, u \in U$. (We won't need conditional independence for more variables than this.)

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.CondIndepFun`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.CondIndepFun).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 307](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L307)
