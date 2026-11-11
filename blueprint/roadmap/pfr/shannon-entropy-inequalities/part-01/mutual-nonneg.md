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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 185](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L185)
