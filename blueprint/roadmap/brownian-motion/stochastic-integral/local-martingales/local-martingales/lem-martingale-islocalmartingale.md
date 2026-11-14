---
declaration: lemma
origin: cited
lean: ProbabilityTheory.Martingale.IsLocalMartingale
statement: formalized
proof: formalized
---

# Martingale.IsLocalMartingale

Every cadlag martingale is a local martingale.

## Depends on

- [Local martingale](def-islocalmartingale.md)
- [Cadlag function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)

## Proof depends on

- [implies_locally](../local-properties/lem-implies-locally.md)

## Proof

This follows from Lemma [implies_locally](../local-properties/lem-implies-locally.md).

## Lean

Formalized as [`ProbabilityTheory.Martingale.IsLocalMartingale`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.Martingale.IsLocalMartingale).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 355](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L355)
