---
declaration: definition
origin: cited
---

# Conditional Kullback–Leibler divergence

If $X,Y,Z$ are random variables, with $X,Z$ defined on the same sample space, we define

$$
D_{KL}(X|Z \Vert  Y) := \sum_z \mathbf{P}(Z=z) D_{KL}( (X|Z=z) \Vert  Y).
$$

## Depends on

- [Kullback–Leibler divergence](kl-div.md)

## Lean

The blueprint marks this formalized but names no Lean declaration.

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 65](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L65)
