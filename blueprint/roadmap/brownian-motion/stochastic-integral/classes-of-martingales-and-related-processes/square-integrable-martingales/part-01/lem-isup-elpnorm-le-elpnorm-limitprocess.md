---
declaration: lemma
origin: cited
lean: MeasureTheory.iSup_eLpNorm_le_eLpNorm_limitProcess
statement: formalized
proof: formalized
---

# iSup_eLpNorm_le_eLpNorm_limitProcess

For $M$ a càdlàg and uniformly integrable martingale,

$$
\sup_{t \in T} \Vert M_t \Vert_2 \le \Vert M_\infty \Vert_2.
$$

## Depends on

- [limitProcess](../../../filtrations-processes-and-martingales/martingale-convergence/def-limitprocess.md)

## Proof depends on

- [condExp_limitProcess](lem-condexp-limitprocess.md)

## Proof

By Lemma [condExp_limitProcess](lem-condexp-limitprocess.md), We have that $P[M_\infty | \mathcal{F}_t] = M t$ almost surely, thus

$$
\|M_t\|_2 = \|P[M_\infty | \mathcal{F}_t]\|_2 \le \|M_\infty\|_2,
$$

where the last inequality is [eLpNorm\_condExp\_le\_eLpNorm](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/ConditionalExpectation/Real.html#MeasureTheory.eLpNorm_condExp_le_eLpNorm).

## Lean

Formalized as [`MeasureTheory.iSup_eLpNorm_le_eLpNorm_limitProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.iSup_eLpNorm_le_eLpNorm_limitProcess).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 324](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L324)
