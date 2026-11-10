---
declaration: lemma
origin: cited
lean: condKLDiv_nonneg
statement: formalized
proof: formalized
---

# Conditional Gibbs inequality

$D_{KL}((X|W)\Vert Y) \geq 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Gibbs inequality](gibbs.md)

## Proof

Clear from Definition [Conditional Kullback–Leibler divergence](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L65) and Lemma [Gibbs inequality](gibbs.md).

## Lean

Formalized as [`condKLDiv_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/condKLDiv_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 78](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L78)
