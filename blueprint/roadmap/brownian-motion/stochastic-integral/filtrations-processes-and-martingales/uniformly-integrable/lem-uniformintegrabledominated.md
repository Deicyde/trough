---
declaration: lemma
origin: cited
lean: MeasureTheory.uniformIntegrable_of_dominated
statement: formalized
---

# uniformIntegrableDominated

Let $(X_s)_{s \in S}$ be a family of random variables and $(Y_t)_{t \in T}$ be a family of uniformly integrable random variables. If for all $s$, there exists $t$ such that $\|X_s\| \le \|Y_t\|$ almost surely, then $X$ is uniformly integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $\epsilon > 0$. The family $Y$ is uniformly integrable, thus there exists $C \ge 0$ such that for $t \in T$, $P[\|Y_t\|^p \mathbb{I}_{\|Y_t\| \ge C}]^{1/p} \le \epsilon$. For all $s$, there exists $t$ such that $\|X_s\|^p \le \|Y_t\|^p$, so $P[\|X_s\|^p \mathbb{I}_{\|X_s\| \ge C}]^{1/p} \le \epsilon$. Thus $X$ is uniformly integrable.

## Lean

Stated as [`MeasureTheory.uniformIntegrable_of_dominated`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.uniformIntegrable_of_dominated); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 800](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L800)
