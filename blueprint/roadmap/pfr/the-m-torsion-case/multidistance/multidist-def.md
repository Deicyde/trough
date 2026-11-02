---
declaration: definition
origin: cited
lean: multiDist
statement: formalized
---

# Multidistance

Let $m$ be a positive integer, and let $X_{[m]} = (X_i)_{1 \leq i \leq m}$ be an $m$-tuple of $G$-valued random variables $X_i$. Then we define

$$
D[X_{[m]}] := \mathbb{H}[\sum_{i=1}^m \tilde X_i] - \frac{1}{m} \sum_{i=1}^m \mathbb{H}[\tilde X_i],
$$

where the $\tilde X_i$ are independent copies of the $X_i$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`multiDist`](https://teorth.github.io/pfr/docs/find/#doc/multiDist).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 172](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L172)
