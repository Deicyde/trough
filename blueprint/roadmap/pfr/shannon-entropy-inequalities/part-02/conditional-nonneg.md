---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condMutualInfo_nonneg
statement: formalized
proof: formalized
---

# Nonnegativity of conditional mutual information

If $X,Y,Z$ are random variables, then $\mathbb{I}[X:Y|Z] \ge 0$.

## Depends on

- [Conditional mutual information](conditional-mutual-def.md)

## Proof depends on

- [Submodularity](../part-01/submodularity.md)

## Proof

Use [Conditional mutual information](conditional-mutual-def.md) and [Submodularity](../part-01/submodularity.md).

## Lean

Formalized as [`ProbabilityTheory.condMutualInfo_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condMutualInfo_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 295](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L295)
