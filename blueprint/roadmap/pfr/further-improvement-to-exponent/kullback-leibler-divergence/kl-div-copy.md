---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IdentDistrib.KLDiv_eq
statement: formalized
proof: formalized
---

# Kullback–Leibler divergence of copy

If $X'$ is a copy of $X$, and $Y'$ is a copy of $Y$, then $D_{KL}(X'\Vert Y') = D_{KL}(X\Vert Y)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kullback–Leibler divergence](kl-div.md)

## Proof

Clear from definition.

## Lean

Formalized as [`ProbabilityTheory.IdentDistrib.KLDiv_eq`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.IdentDistrib.KLDiv_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 11](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L11)
