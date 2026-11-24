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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 224](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/entropy.tex#L224)
