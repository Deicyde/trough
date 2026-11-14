---
declaration: lemma
origin: cited
lean: ProbabilityTheory.ClassD.uniformIntegrable'
statement: formalized
proof: formalized
---

# ClassD.uniformIntegrable

A stochastic process of class D is uniformly integrable.

## Depends on

- [Doob-Meyer class, class D](def-classd.md)

## Proof depends on

- [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md)

## Proof

Use the Class D property with the constant stopping times $\tau_n = n$ for all $n$ and apply Lemma [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md).

## Lean

Formalized as [`ProbabilityTheory.ClassD.uniformIntegrable'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.ClassD.uniformIntegrable').

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 460](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L460)
