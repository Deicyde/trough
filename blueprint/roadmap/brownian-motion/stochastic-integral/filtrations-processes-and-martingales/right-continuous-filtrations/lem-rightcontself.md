---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont_self
---

# rightContSelf

The right continuation of the right continuation of $\mathcal{F}$ is equal to the right continuation of $\mathcal{F}$.

## Depends on

- [Right continuation](def-rightlimitfiltration.md)

## Proof depends on

- [leRightCont](lem-lerightcont.md)
- [rightContDef](lem-rightcontdef.md)

## Proof

Let $t \in T$. From Lemma [leRightCont](lem-lerightcont.md), we already now that $\mathcal{F}_{t+} \subseteq \mathcal{F}_{t++}$. Endow $T$ with the order topology and split according to Lemma [rightContDef](lem-rightcontdef.md). If $t$ is isolated on the right, then $\mathcal{F}_{t++} = \mathcal{F}_{t+}$ and we are done. Otherwise consider $u > t$. Then there exists $v \in T$ such that $t < v < u$. If $v$ is not isolated on the right then

$$
\mathcal{F}_{t++} = \mathop{\Large\sqcap}_{s > t} \mathcal{F}_{s+} \subseteq \mathcal{F}_{v+} = \mathop{\Large\sqcap}_{s > v} \mathcal{F}_s \subseteq \mathcal{F}_u,
$$

and otherwise

$$
\mathcal{F}_{t++} = \mathop{\Large\sqcap}_{s > t} \mathcal{F}_{s+} \subseteq \mathcal{F}_{v+} = \mathcal{F}_v \subseteq \mathcal{F}_u,
$$

thus $\mathcal{F}_{t++} \subseteq \mathop{\Large\sqcap}_{s > t} \mathcal{F}_s = \mathcal{F}_{t+}$, which concludes the proof.

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont_self`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont_self).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 510](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L510)
