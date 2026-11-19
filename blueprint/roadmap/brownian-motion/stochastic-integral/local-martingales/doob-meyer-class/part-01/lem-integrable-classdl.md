---
declaration: lemma
origin: cited
lean: MeasureTheory.Integrable.classDL
statement: formalized
proof: formalized
---

# Integrable.classDL

Let $X$ be a progressively measurable stochastic process with integrable supremum (Definition [Integrable supremum](def-hasintegrablesup.md)). Then $X$ is of class DL.

## Depends on

- [Class DL](def-classdl.md)
- [Integrable supremum](def-hasintegrablesup.md)

## Proof depends on

- [uniformIntegrableDominatedSingleton](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominatedsingleton.md)

## Proof

Let $t \in T$. For every stopping time $\tau$ with $\tau \le t$, we have $\|X_\tau\| \le X^*_t$. Measurability of $X_\tau$ follows from progressive measurability of $X$. Because by hypothesis $X^*_t$ is integrable, we deduce from Lemma [uniformIntegrableDominatedSingleton](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominatedsingleton.md) that $\{X_\tau \mid \tau \text{ is a stopping time with } \tau \le t\}$ is uniformly integrable. This proves that $X$ is of class DL.

## Lean

Formalized as [`MeasureTheory.Integrable.classDL`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Integrable.classDL).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 638](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L638)
