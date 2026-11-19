---
declaration: lemma
origin: cited
lean: ProbabilityTheory.ClassDL.hasLocallyIntegrableSup
statement: formalized
proof: formalized
---

# ClassDL.hasLocallyIntegrableSup

Assume $T$ has a bottom element and that its closed intervals are compact, and that the filtration is right-continuous. If $X$ is a càdlàg process of class DL, then it has locally integrable supremum.

## Depends on

- [Doob-Meyer class, class D](../part-01/def-classd.md)
- [Locally integrable supremum](../part-01/def-locallyintegrablesup.md)
- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)
- [Right-continuous filtration](../../../filtrations-processes-and-martingales/right-continuous-filtrations/def-rightcontinuous.md)

## Proof depends on

- [isLocalizingSequence_leastGE](lem-islocalizingsequence-leastge.md)
- [sup_stoppedProcess_le](lem-sup-stoppedprocess-le.md)
- [IsStronglyProgressive.hasStronglyMeasurableSup](../part-01/lem-isstronglyprogressive-hasstronglymeasurables.md)

## Proof

Set $\tau_n := \inf \{t | X_t \ge n\}$. This is a localizing sequence by Lemma [isLocalizingSequence_leastGE](lem-islocalizingsequence-leastge.md). For every $t \in T$, we have by Lemma [sup_stoppedProcess_le](lem-sup-stoppedprocess-le.md) that $(X^{\tau_n})^*_t \le n + \mathbb{I}_{\tau_n \le t} \|X_{\tau_n}\| = n + \mathbb{I}_{\tau_n \le t} \|X_{\tau_n \land t}\|$. Because X is of class DL, $X_{\tau_n \land t}$ is integrable, so $(X^{\tau_n})^*_t$ is integrable too, so $(X^{\tau_n} \mathbb{I}_{\tau_n > 0})^*_t$ is integrable. Thus $X$ has locally integrable supremum.

## Lean

Formalized as [`ProbabilityTheory.ClassDL.hasLocallyIntegrableSup`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.ClassDL.hasLocallyIntegrableSup).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 762](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L762)
