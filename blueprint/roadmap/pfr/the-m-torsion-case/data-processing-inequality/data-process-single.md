---
declaration: lemma
origin: cited
lean: ProbabilityTheory.entropy_comp_le
statement: formalized
proof: formalized
---

# Data processing for a single variable

Let $X$ be a random variable. Then for any function $f$ on the range of $X$, one has $\mathbb{H}[f(X)] \leq \mathbb{H}[X]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md)

## Proof

We have

$$
\mathbb{H}[X] = \mathbb{H}[X,f(X)] = \mathbb{H}[f(X)] + \mathbb{H}[X|f(X)]
$$

thanks to [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md) and [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md), giving the claim.

## Lean

Formalized as [`ProbabilityTheory.entropy_comp_le`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_comp_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 5](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L5)
