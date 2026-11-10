---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condMutual_comp_comp_le
statement: formalized
proof: formalized
---

# Data processing inequality

Let $X,Y,Z$. For any functions $f, g$ on the ranges of $X, Y$ respectively, we have $\mathbb{I}[f(X) : g(Y )|Z] \leq \mathbb{I}[X :Y |Z]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Unconditional data processing inequality](data-process-unc.md)
- [Conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-def.md)

## Proof

Apply [Unconditional data processing inequality](data-process-unc.md) to $X,Y$ conditioned to the event $Z=z$, multiply by ${\bf P}[Z=z]$, and sum using [Conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-def.md).

## Lean

Formalized as [`ProbabilityTheory.condMutual_comp_comp_le`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condMutual_comp_comp_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 28](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L28)
