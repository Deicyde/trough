---
declaration: lemma
origin: cited
lean: ProbabilityTheory.mutual_comp_le
statement: formalized
proof: formalized
---

# One-sided unconditional data processing inequality

Let $X,Y$ be random variables. For any function $f, g$ on the range of $X$, we have $\mathbb{I}[f(X) : Y] \leq \mathbb{I}[X:Y]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Alternative formulae for mutual information](../../shannon-entropy-inequalities/part-01/alternative-mutual.md)
- [Submodularity](../../shannon-entropy-inequalities/part-01/submodularity.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)

## Proof

By [Alternative formulae for mutual information](../../shannon-entropy-inequalities/part-01/alternative-mutual.md) it suffices to show that $\mathbb{H}[Y|X] \leq \mathbb{H}[Y|f(X)]$. But this follows from [Submodularity](../../shannon-entropy-inequalities/part-01/submodularity.md) (and [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)).

## Lean

Formalized as [`ProbabilityTheory.mutual_comp_le`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.mutual_comp_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 14](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L14)
