---
declaration: lemma
origin: cited
lean: ProbabilityTheory.mutualInfo_nonneg
statement: formalized
proof: formalized
---

# Nonnegativity of mutual information

We have $\mathbb{I}[X:Y] \geq 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Concavity](../../applications-of-jensens-inequality/concave.md)
- [Alternative formulae for mutual information](alternative-mutual.md)

## Proof

An application of jensen's inequality and [Concavity](../../applications-of-jensens-inequality/concave.md) and [Alternative formulae for mutual information](alternative-mutual.md).

## Lean

Formalized as [`ProbabilityTheory.mutualInfo_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutualInfo_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 185](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L185)
