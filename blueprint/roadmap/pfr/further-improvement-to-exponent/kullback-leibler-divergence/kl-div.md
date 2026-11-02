---
declaration: definition
origin: cited
lean: KLDiv
statement: formalized
---

# Kullback–Leibler divergence

If $X,Y$ are two $G$-valued random variables, the Kullback–Leibler divergence is defined as

$$
D_{KL}(X\Vert Y) := \sum_x \mathbf{P}(X=x) \log \frac{\mathbf{P}(X=x)}{\mathbf{P}(Y=x)}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`KLDiv`](https://teorth.github.io/pfr/docs/find/#doc/KLDiv).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 7](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L7)
