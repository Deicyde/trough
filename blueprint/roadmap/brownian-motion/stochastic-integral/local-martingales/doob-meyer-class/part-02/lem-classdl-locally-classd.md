---
declaration: lemma
origin: cited
lean: ProbabilityTheory.ClassDL.locally_classD
statement: formalized
proof: formalized
---

# ClassDL.locally_classD

If $X$ is of class DL then it is locally of class D.

## Depends on

- [Class DL](../part-01/def-classdl.md)
- [Local property](../../local-properties/def-locally.md)
- [Doob-Meyer class, class D](../part-01/def-classd.md)

## Proof depends on

- [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md)
- [uniformIntegrableDominated](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominated.md)

## Proof

Take $\tau_n := n$. Then

$$
\begin{aligned}
\{X^{\tau_n}_\sigma \mid \sigma \text{ is a finite stopping time}\} & = \{X_{\sigma \land n} \mid \sigma \text{ is a finite stopping time}\} \\
& \subseteq \{X_\sigma \mid \sigma \text{ is a stopping time with } \sigma \le n\}.
\end{aligned}
$$

Because $X$ is of class DL, that last set is uniformly integrable, thus

$$
\{X^{\tau_n}_\sigma \mid \sigma \text{ is a finite stopping time}\}
$$

is uniformly integrable thanks to Lemma [uniformIntegrableComp](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrablecomp.md). Lemma [uniformIntegrableDominated](../../../filtrations-processes-and-martingales/uniformly-integrable/lem-uniformintegrabledominated.md) allows to conclude that

$$
\{X^{\tau_n}_\sigma \mathbb{I}_{\tau_n > 0} \mid \sigma \text{ is a finite stopping time}\}
$$

is uniformly integrable, thus $X^{\tau_n} \mathbb{I}_{\tau_n > 0}$ is of class D. Obviously $\tau_n \rightarrow +\infty$ as $n$ goes to infinity, so $X$ is locally of class D.

## Lean

Formalized as [`ProbabilityTheory.ClassDL.locally_classD`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.ClassDL.locally_classD).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 679](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L679)
