---
declaration: corollary
origin: cited
lean: ProbabilityTheory.condEntropy_le_entropy
statement: formalized
proof: formalized
---

# Conditioning reduces entropy

With notation as above, we have $\mathbb{H}[X|Y] \leq \mathbb{H}[X]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Nonnegativity of mutual information](mutual-nonneg.md)
- [Alternative formulae for mutual information](alternative-mutual.md)

## Proof

Combine [Nonnegativity of mutual information](mutual-nonneg.md) with [Alternative formulae for mutual information](alternative-mutual.md).

## Lean

Formalized as [`ProbabilityTheory.condEntropy_le_entropy`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_le_entropy).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 212](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L212)
