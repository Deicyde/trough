---
declaration: lemma
origin: cited
lean: ProbabilityTheory.Locally.rightContinuous
statement: formalized
proof: formalized
---

# locally_rightContinuous

A stochastic process $X$ is locally right continuous if and only if it is right continuous almost surely.

## Depends on

- [Local property](../local-properties/def-locally.md)
- [Right continuous function](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-rightcontinuous.md)

## Proof depends on

- [locally_of_ae](lem-locally-of-ae.md)

## Proof

If $X$ is a.s. right continuous, then it is locally right continuous by Lemma [locally_of_ae](lem-locally-of-ae.md).

On the other hand, assuming $X$ is locally right continuous, there exists a localizing sequence $(\tau_n)_{n \in \mathbb{N}}$ such that for all $n \in \mathbb{N}$ and $\omega \in \Omega$, $(X^{\tau_n}\mathbb{I}_{\tau_n > 0})(\omega)$ is right continuous. Thus, for almost surely every $\omega$ and any $t \in T$ there exists $N \in \mathbb{N}$ such that $\tau_N(\omega) > t + 1$ (not that the ordering of a.s. and for all is important). Hence, as $X_s(\omega) = (X^{\tau_N}\mathbb{I}_{\tau_N > 0})_s(\omega)$ on a neighborhood of $t$, we have that $X(\omega)$ is right continuous at $t$. Consequently, as $t$ was arbitrary, $X$ is a.s. right continuous.

## Lean

Formalized as [`ProbabilityTheory.Locally.rightContinuous`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.Locally.rightContinuous).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 240](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L240)
