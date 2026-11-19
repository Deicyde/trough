---
declaration: lemma
origin: cited
lean: ProbabilityTheory.isStable_martingale
statement: formalized
proof: formalized
---

# stable_IsMartingale

The class of cadlag martingales is stable. That is, if $M$ is a cadlag martingale and $\tau$ is a stopping time, then the stopped process cadlag $M^{\tau}\mathbb{I}_{\tau > 0}$ is also a martingale.

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [stable](../local-properties/def-stable.md)
- [Cadlag function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)

## Proof depends on

- [Optional sampling (continuous time)](../../filtrations-processes-and-martingales/optional-sampling/lem-optionalsampling.md)

## Proof

Clearly, the stopped process $M^{\tau}\mathbb{I}_{\tau > 0}$ is cadlag and it remains to show that it is a martingale.

Fixing $s \le t \in T$, as $\{\tau > 0\} \in \mathcal{F}_0 \subseteq \mathcal{F}_s$, we have

$$
P[M^{\tau}_t \mathbb{I}_{\tau > 0} \mid \mathcal{F}_s] = \mathbb{I}_{\tau > 0}P[M_{\tau \wedge t} \mid \mathcal{F}_{s}].
$$

Thus, as $\tau \wedge t$ is a bounded stopping time, we have by the optional stopping theorem (Lemma [Optional sampling (continuous time)](../../filtrations-processes-and-martingales/optional-sampling/lem-optionalsampling.md)) that $P[M_{\tau \wedge t} \mid \mathcal{F}_{s}] = M_{(\tau \wedge t) \wedge s} = M_{\tau \wedge s}$ and so, $P[M^{\tau}_t \mathbb{I}_{\tau > 0} \mid \mathcal{F}_s] = M^{\tau}_s \mathbb{I}_{\tau > 0}$ as required.

## Lean

Formalized as [`ProbabilityTheory.isStable_martingale`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isStable_martingale).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 368](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L368)
