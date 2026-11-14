---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isStable_classDL
statement: formalized
proof: formalized
---

# isStable_classDL

The class DL is stable.

## Depends on

- [stable](../../local-properties/def-stable.md)
- [Class DL](def-classdl.md)

## Proof depends on

- [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md)
- [uniformIntegrableDominated](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominated.md)
- [isStable_isStronglyProgressive](../../locally-cadlag/lem-isstable-isstronglyprogressive.md)

## Proof

Let $X$ be a process of class DL, $\tau$ be a stopping time. Let $t \in T$. For any stopping time $\sigma \le t$, we have that $X_\sigma^\tau = X_{\sigma \land \tau}$. Because $\sigma \land \tau$ is bounded by $t$ and $X$ is of class DL, we deduce from Lemma [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md) that $\{X_{\sigma \land \tau} \mid \sigma \text{ is a stopping time with } \sigma \le t\}$ is uniformly integrable, and thus that $\{X^\tau_\sigma \mid \sigma \text{ is a stopping time with } \sigma \le t\}$ is uniformly integrable. Using Lemma [uniformIntegrableDominated](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominated.md), we obtain that $\{X^\tau_\sigma \mathbb{I}_{\tau > 0} \mid \sigma \text{ is a stopping time with } \sigma \le t\}$ is uniformly integrable, which concludes the proof.

## Lean

Formalized as [`ProbabilityTheory.isStable_classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isStable_classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 625](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L625)
