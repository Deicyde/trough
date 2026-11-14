---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration.rightCont
---

# filtrationRightCont

The right continuation of $\mathcal{F}$ is a filtration.

## Depends on

- [Filtration](../basic-definitions/part-01/def-filtration.md)
- [Right continuation](def-rightlimitfiltration.md)

## Proof

We endow $T$ with the order topology. Let us first prove that the right continuation is nondecreasing. Let $s, t \in T$ such that $s \le t$.

- Suppose $s$ is isolated on the right. Then $\mathcal{F}_{s+} = \mathcal{F}_s$.

    - If $t$ is isolated on the right, then $\mathcal{F}_{t+} = \mathcal{F}_t$. Because $\mathcal{F}$ is a filtration, we have $\mathcal{F}_s \subseteq \mathcal{F}_t$, and thus $\mathcal{F}_{s+} \subseteq \mathcal{F}_{t+}$.
    - If $t$ is not isolated on the right, then $\mathcal{F}_{t+} = \mathop{\Large\sqcap}_{u > t} \mathcal{F}_{u}$. Let $u > t$. Then $s \le u$, thus $\mathcal{F}_s \subseteq \mathcal{F}_u$. This proves that $\mathcal{F}_s \subseteq \mathop{\Large\sqcap}_{u > t}, \mathcal{F}_u$, and thus $\mathcal{F}_{s+} \subseteq \mathcal{F}_{t+}$.

- Suppose now that $s$ is not isolated on the right, so that $\mathcal{F}_{s+} = \bigsqcup_{u > s} \mathcal{F}_u$.

    - If $t$ is isolated on the right, then $\mathcal{F}_{t+} = \mathcal{F}_t$. As $s$ is not isolated on the right, we deduce that $s \ne t$, and thus $s < t$ because $T$ is a partial order. Therefore $\mathop{\Large\sqcap}_{u > s} \mathcal{F}_u \subseteq \mathcal{F}_t$, and thus $\mathcal{F}_{s+} \subseteq \mathcal{F}_{t+}$.
    - If $t$ is not isolated on the right, then $\mathcal{F}_{t+} = \mathop{\Large\sqcap}_{u > t} \mathcal{F}_u$. For any $u > t$, we have $u > s$ and thus $\mathop{\Large\sqcap}_{v > s} \mathcal{F}_v \subseteq \mathcal{F}_u$, proving that $\mathop{\Large\sqcap}_{u > s} \mathcal{F}_u \subseteq \mathop{\Large\sqcap}_{u > t} \mathcal{F}_u$, and thus $\mathcal{F}_{s+} \subseteq \mathcal{F}_{t+}$.

Turn now to the proof that for all $t \in T$, $\mathcal{F}_{t+} \subseteq \mathcal{A}$. Let $t \in T$. If $t$ is isolated on the right, then $\mathcal{F}_{t+} = \mathcal{F}_t \subseteq \mathcal{A}$ by definition of a filtration. Otherwise there exists $u > t$, and $\mathcal{F}_{t+} \subseteq \mathcal{F}_u \subseteq \mathcal{A}$, so we are done.

## Lean

Formalized as [`MeasureTheory.Filtration.rightCont`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration.rightCont).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 361](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L361)
