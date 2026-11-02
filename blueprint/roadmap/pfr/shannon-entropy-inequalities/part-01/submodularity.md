---
declaration: corollary
origin: cited
lean: ProbabilityTheory.entropy_submodular, ProbabilityTheory.condEntropy_comp_ge
statement: formalized
proof: formalized
---

# Submodularity

With three random variables $X,Y,Z$, one has $\mathbb{H}[X|Y,Z] \leq \mathbb{H}[X|Z]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Conditioning reduces entropy](cond-reduce.md)

## Proof

Apply the “averaging over conditioning” argument to [Conditioning reduces entropy](cond-reduce.md).

## Lean

Formalized as [`ProbabilityTheory.entropy_submodular`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_submodular), [`ProbabilityTheory.condEntropy_comp_ge`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condEntropy_comp_ge).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 224](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L224)
