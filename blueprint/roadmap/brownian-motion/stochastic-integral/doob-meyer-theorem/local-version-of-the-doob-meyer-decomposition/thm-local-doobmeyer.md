---
declaration: theorem
origin: cited
lean: ProbabilityTheory.IsLocalSubmartingale.doob_meyer
statement: formalized
---

# Doob-Meyer decomposition

An adapted process $X$ is a cadlag local submartingale iff $X = M + A$ where $M$ is a cadlag local martingale and $A$ is a predictable, cadlag, locally integrable and increasing process starting at $0$. The processes $M$ and $A$ are uniquely determined by $X$ a.s.

## Depends on

- [IsLocalSubmartingale](../../local-martingales/local-martingales/def-islocalsubmartingale.md)
- [Predictable process](../../filtrations-processes-and-martingales/predictable-processes/def-predictable.md)
- [Local martingale](../../local-martingales/local-martingales/def-islocalmartingale.md)

## Proof depends on

- [IsLocalSubmartingale.locally_classD](../../local-martingales/doob-meyer-class/part-02/lem-islocalsubmartingale-locally-classd.md)

## Lean

Stated as [`ProbabilityTheory.IsLocalSubmartingale.doob_meyer`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsLocalSubmartingale.doob_meyer); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/doob_meyer.tex, line 1161](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/doob_meyer.tex#L1161)
