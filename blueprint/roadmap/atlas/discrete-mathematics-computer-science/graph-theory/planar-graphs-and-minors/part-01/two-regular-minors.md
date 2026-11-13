---
declaration: section
origin: cited
lean: MathlibExt.GraphTheory.TwoRegularMinorForcingWanted.HasMinor, MathlibExt.GraphTheory.TwoRegularMinorForcingWanted.conjecture, MathlibExt.GraphTheory.TwoRegularMinorForcingWanted.conjecture_holds
statement: formalized
---

# Two-regular minors

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/two-regular-minors/index.html).

## Minor via branch sets

For finite simple graphs $G$ and $H$, $G$ has $H$ as a minor if
there is a family of vertex sets $B_w$ of $G$, one for each vertex $w$ of $H$, such that each
$B_w$ is nonempty and induces a connected subgraph of $G$, the sets $B_u$ and $B_v$ are disjoint
whenever $u \ne v$, and for every edge $uv$ of $H$ some vertex of $B_u$ is adjacent in $G$ to
some vertex of $B_v$.

Formalized by `MathlibExt.GraphTheory.TwoRegularMinorForcingWanted.HasMinor`, a definition declared in [WantedExt/GraphTheory/TwoRegularMinorForcingWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/TwoRegularMinorForcingWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/two-regular-minors/index.html#has-minor).

## Average-degree conjecture for 2-regular minors

For every natural number $t$, every
finite simple graph whose average degree is at least $4t/3 - 2$ (the average degree of the graph
with no vertices being taken as $0$) contains every 2-regular simple graph on $t$ vertices as a
minor.

Formalized by `MathlibExt.GraphTheory.TwoRegularMinorForcingWanted.conjecture`, a definition declared in [WantedExt/GraphTheory/TwoRegularMinorForcingWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/TwoRegularMinorForcingWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/two-regular-minors/index.html#conjecture).

## Csóka–Lo–Norin–Wu–Yepremyan theorem on 2-regular minors

For every natural number $t$,
every finite simple graph $G$ whose average degree (the sum of the vertex degrees divided by the
number of vertices, taken to be $0$ when $G$ has no vertices) is at least $4t/3 - 2$ contains
every 2-regular simple graph $H$ on $t$ vertices as a minor: there are nonempty, pairwise
disjoint sets of vertices of $G$, one for each vertex of $H$, each inducing a connected subgraph
of $G$, such that whenever two vertices of $H$ are adjacent, some edge of $G$ joins their sets.

Csoka, Lo, Norin, Wu and Yepremyan proved this, verifying a conjecture of Reed and Wood; the
non-strict threshold follows from the form of their bound in Corollary 8 and Lemma 9.

## Sources

- Endre Csoka, Irene Lo, Sergey Norin, Hehui Wu and Liana Yepremyan, The extremal function for disconnected minors, Journal of Combinatorial Theory Series B (2017), arXiv:1509.01185, https://arxiv.org/abs/1509.01185.

Stated but not proved: `MathlibExt.GraphTheory.TwoRegularMinorForcingWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/GraphTheory/TwoRegularMinorForcingWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GraphTheory/TwoRegularMinorForcingWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/two-regular-minors/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-regular minors](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/two-regular-minors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/two-regular-minors)
