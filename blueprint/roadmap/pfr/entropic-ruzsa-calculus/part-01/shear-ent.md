---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condEntropy_add_right, ProbabilityTheory.condEntropy_add_left, ProbabilityTheory.condEntropy_sub_right, ProbabilityTheory.condEntropy_sub_left
statement: formalized
proof: formalized
---

# Shearing preserves entropy

If $X,Y$ are $G$-valued, then $\mathbb{H}[X \pm Y | Y]=\mathbb{H}[X|Y]$ and $\mathbb{H}[X \pm Y, Y] = \mathbb{H}[X, Y]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Conditional entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md)
- [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md)

## Proof

Immediate from [Conditional entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md) and [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md).

## Lean

Formalized as [`ProbabilityTheory.condEntropy_add_right`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_add_right), [`ProbabilityTheory.condEntropy_add_left`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_add_left), [`ProbabilityTheory.condEntropy_sub_right`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_sub_right), [`ProbabilityTheory.condEntropy_sub_left`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_sub_left).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 14](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L14)
