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

Clear from Definition [Conditional Kullback–Leibler divergence](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/further_improvement.tex#L65) and Lemma [Gibbs inequality](gibbs.md).

## Lean

Formalized as [`condKLDiv_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/condKLDiv_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 78](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/further_improvement.tex#L78)
