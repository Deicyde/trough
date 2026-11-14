---
declaration: lemma
origin: cited
lean: ProbabilityTheory.locally_of_ae
statement: formalized
proof: formalized
---

# locally_of_ae

If $P$ be a predicate on paths such that the constant path $0$ satisfies $P$ and $X$ is a stochastic process satisfying $P$ a.s. then, $X$ satisfies $P$ locally.

## Depends on

- [Local property](../local-properties/def-locally.md)

## Proof depends on

- [isLocalizingSequence_ae](../local-properties/lem-islocalizingsequence-ae.md)

## Proof

Follows directly by using the localizing sequence defined in Lemma [isLocalizingSequence_ae](../local-properties/lem-islocalizingsequence-ae.md).

## Lean

Formalized as [`ProbabilityTheory.locally_of_ae`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.locally_of_ae).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 228](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L228)
