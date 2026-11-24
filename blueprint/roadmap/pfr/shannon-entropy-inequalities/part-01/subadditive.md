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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 199](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy.tex#L199)
