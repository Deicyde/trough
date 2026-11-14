---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Locally.of_prop
---

# implies_locally

For any class of processes $P$, we have $P \subseteq P_{\mathrm{loc}}$.

## Depends on

- [Local property](def-locally.md)

## Proof depends on

- [localizingSequence_const_top](lem-localizingsequence-const-top.md)

## Proof

Take $\tau_n = \infty$ for all $n$.

## Lean

Formalized as [`ProbabilityTheory.Locally.of_prop`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.Locally.of_prop).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 104](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L104)
