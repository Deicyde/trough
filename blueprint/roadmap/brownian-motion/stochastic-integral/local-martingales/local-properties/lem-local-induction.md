---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsStable.locally_induction
---

# Local implication from global implication

Suppose that the filtration is right-continuous. Let $P, Q$ be two classes of stochastic processes such that $P \subseteq Q_{\mathrm{loc}}$ and $Q$ is stable. Let $X$ be a stochastic process that satisfies $P$ locally. Then $X$ satisfies $Q$ locally. In short, if $P$ implies $Q$ locally, then $P$ locally implies $Q$ locally.

## Depends on

- [Local property](def-locally.md)
- [stable](def-stable.md)

## Proof depends on

- [locally_locally](lem-locally-locally.md)
- [locally_mono](lem-locally-mono.md)

## Proof

Since $X \in P_{\mathrm{loc}}$, then $X \in (Q_{\mathrm{loc}})_{\mathrm{loc}}$ by assumption and Lemma [locally_mono](lem-locally-mono.md). By Lemma [locally_locally](lem-locally-locally.md), $(Q_{\mathrm{loc}})_{\mathrm{loc}} = Q_{\mathrm{loc}}$. Thus $X \in Q_{\mathrm{loc}}$.

## Lean

Formalized as [`ProbabilityTheory.IsStable.locally_induction`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsStable.locally_induction).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 206](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L206)
