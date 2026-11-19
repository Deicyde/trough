---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isStable_hasIntegrableSup
statement: formalized
proof: formalized
---

# isStable_hasIntegrableSup

The class of process with integrable supremum is stable.

## Depends on

- [stable](../../local-properties/def-stable.md)
- [Integrable supremum](def-hasintegrablesup.md)

## Proof

Let $X$ be a process with integrable supremum and $\tau$ be a stopping time. Let $t \in T$. Then $(X^\tau)^*_t = \sup_{s \le t} \|X_{\tau \land s}\| \le \sup_{s \le t} \|X_s\| = X^*_t$, and as $X^*_t$ is integrable, so is $(X^\tau)^*_t$. Thus $(X^\tau \mathbb{I}_{\tau > 0})^*_t$ is integrable, concluding the proof.

## Lean

Formalized as [`ProbabilityTheory.isStable_hasIntegrableSup`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isStable_hasIntegrableSup).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 588](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L588)
