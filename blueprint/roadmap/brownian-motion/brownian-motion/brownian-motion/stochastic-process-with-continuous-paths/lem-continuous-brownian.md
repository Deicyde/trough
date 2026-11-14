---
declaration: lemma
origin: cited
lean: ProbabilityTheory.continuous_brownian
statement: formalized
proof: formalized
---

# continuous_brownian

The paths of the Brownian motion are continuous.

## Depends on

- [Brownian motion](def-brownian.md)

## Proof depends on

- [isHolderWith_brownian](lem-isholderwith-brownian.md)

## Proof

The paths are $1/4$-Hölder continuous by Lemma [isHolderWith_brownian](lem-isholderwith-brownian.md) because $0 < 1/4 < 1/2$, therefore they are continuous.

## Lean

Formalized as [`ProbabilityTheory.continuous_brownian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.continuous_brownian).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 116](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L116)
