---
declaration: corollary
origin: cited
lean: ProbabilityTheory.entropy_pair_le_add
statement: formalized
proof: formalized
---

# Subadditivity

With notation as above, we have $\mathbb{H}[X,Y] \leq \mathbb{H}[X] + \mathbb{H}[Y]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Nonnegativity of mutual information](mutual-nonneg.md)
- [Alternative formulae for mutual information](alternative-mutual.md)

## Proof

Use [Nonnegativity of mutual information](mutual-nonneg.md).

## Lean

Formalized as [`ProbabilityTheory.entropy_pair_le_add`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_pair_le_add).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 199](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L199)
