---
declaration: section
origin: cited
lean: MathlibExt.Analysis.OptimalTransportWanted.Analysis.Couplings, MathlibExt.Analysis.OptimalTransportWanted.Analysis.kantorovichCost, MathlibExt.Analysis.OptimalTransportWanted.Analysis.monge_kantorovich_exists
statement: formalized
---

# Monge–Kantorovich existence theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/monge-kantorovich-existence-theorem/index.html).

## Couplings

Let $X$ and $Y$ be measurable spaces, $P$ a measure on $X$ and $Q$ a measure
on $Y$. A coupling of $P$ and $Q$ is a probability measure $\pi$ on $X \times Y$ whose marginals
are $P$ and $Q$: the pushforward of $\pi$ under the projection $X \times Y \to X$ is $P$, and its
pushforward under the projection $X \times Y \to Y$ is $Q$. The set of couplings is written
$\Pi(P, Q)$.

Formalized by `MathlibExt.Analysis.OptimalTransportWanted.Analysis.Couplings`, a definition declared in [WantedExt/Analysis/OptimalTransportWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/OptimalTransportWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/monge-kantorovich-existence-theorem/index.html#couplings).

## Kantorovich cost

Let $X$ and $Y$ be measurable spaces and
$c \colon X \times Y \to [0, \infty]$ a cost function. The Kantorovich cost of a measure $\pi$ on
$X \times Y$ is $I(\pi) = \int_{X \times Y} c \, d\pi \in [0, \infty]$, the Lebesgue integral of
$c$ against $\pi$ (for a non-measurable $c$, the lower Lebesgue integral).

Formalized by `MathlibExt.Analysis.OptimalTransportWanted.Analysis.kantorovichCost`, a definition declared in [WantedExt/Analysis/OptimalTransportWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/OptimalTransportWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/monge-kantorovich-existence-theorem/index.html#kantorovich-cost).

## Monge–Kantorovich existence theorem

Let $X$ and $Y$ be Polish spaces with their Borel
$\sigma$-algebras, let $P$ and $Q$ be probability measures on $X$ and $Y$, and let
$c \colon X \times Y \to [0, \infty]$ be continuous. Then there is a coupling $\pi$ of $P$ and $Q$
whose Kantorovich cost $\int c \, d\pi$ is at most the Kantorovich cost $\int c \, d\pi'$ of every
coupling $\pi'$ of $P$ and $Q$: the Kantorovich cost attains its minimum on the set of couplings
of $P$ and $Q$.

## Sources

- L. V. Kantorovich (1942), after G. Monge (1781). Listed as §73 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `monge_kantorovich` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.OptimalTransportWanted.Analysis.monge_kantorovich_exists` is written with `theorem_wanted` in [WantedExt/Analysis/OptimalTransportWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/OptimalTransportWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/monge-kantorovich-existence-theorem/index.html#monge-kantorovich-exists).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monge–Kantorovich existence theorem](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/monge-kantorovich-existence-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/optimal-transport/monge-kantorovich-existence-theorem)
