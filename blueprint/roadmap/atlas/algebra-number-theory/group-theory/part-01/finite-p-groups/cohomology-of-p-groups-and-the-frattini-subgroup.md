---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.InFrattiniCenter, MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.FrattiniCenterH1Trivial, MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.nonabelianPGroupFrattiniCenterH1Trivial, MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.nonabelianPGroupFrattiniCenterH1Trivial_holds
statement: formalized
---

# Cohomology of p-groups and the Frattini subgroup

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/cohomology-of-p-groups-and-the-frattini-subgroup/index.html).

## Centre of the Frattini subgroup

An element $x$ of a group $G$ lies in the centre
$Z(\Phi(G))$ of the Frattini subgroup $\Phi(G)$ when $x \in \Phi(G)$ and $xy = yx$ for every
$y \in \Phi(G)$.

Formalized by `MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.InFrattiniCenter`, a definition declared in [WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/cohomology-of-p-groups-and-the-frattini-subgroup/index.html#in-frattini-center).

## Vanishing first cohomology of $G/\Phi(G)$ in $Z(\Phi(G))$

Let $G$ be a group, let
$\Phi(G)$ be its Frattini subgroup and let $Z(\Phi(G))$ be the centre of $\Phi(G)$. The property
holds when every map $\delta \colon G \to Z(\Phi(G))$ with
$\delta(gh) = \delta(g)\, g\, \delta(h)\, g^{-1}$ for all $g, h \in G$ and $\delta(g) = 1$ for all
$g \in \Phi(G)$ is a coboundary: there is an $a \in Z(\Phi(G))$ with $\delta(g) = g a g^{-1} a^{-1}$
for all $g \in G$.

Such maps $\delta$ are exactly the inflations to $G$ of the 1-cocycles of $G/\Phi(G)$ with values
in $Z(\Phi(G))$ for the conjugation action, so the property says
$H^1(G/\Phi(G), Z(\Phi(G))) = 0$.

Formalized by `MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.FrattiniCenterH1Trivial`, a definition declared in [WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/cohomology-of-p-groups-and-the-frattini-subgroup/index.html#frattini-center-h1-trivial).

## Kourovka Problem 17.2 (a non-abelian $p$-group with trivial $H^1$)

The statement, a
question of P. Schmid recorded by A. Abdollahi, that there exist a prime $p$ and a finite
non-abelian $p$-group $G$ such that, writing $\Phi(G)$ for the Frattini subgroup of $G$ and
$Z(\Phi(G))$ for its centre, the first cohomology group $H^1(G/\Phi(G), Z(\Phi(G)))$ for the
conjugation action of $G/\Phi(G)$ on $Z(\Phi(G))$ is trivial.

Formalized by `MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.nonabelianPGroupFrattiniCenterH1Trivial`, a definition declared in [WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/cohomology-of-p-groups-and-the-frattini-subgroup/index.html#nonabelian-pgroup-frattini-center-h1-tri).

## A non-abelian $p$-group with $H^1(G/\Phi(G), Z(\Phi(G))) = 0$ (Kourovka 17.2)

There exist a
prime $p$ and a finite non-abelian $p$-group $G$ such that, writing $\Phi(G)$ for the Frattini
subgroup of $G$ and $Z(\Phi(G))$ for its centre, the first cohomology group
$H^1(G/\Phi(G), Z(\Phi(G)))$ for the conjugation action of $G/\Phi(G)$ on $Z(\Phi(G))$ is trivial.

This answers Kourovka Problem 17.2 in the affirmative: the Kourovka Archive answers "Yes, it does",
citing Abdollahi (2011).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.2 (A. Abdollahi); resolution: A. Abdollahi, J. Algebra 342 (2011), 154-160, Kourovka Archive, Problem 17.2 (Yes, it does).

Stated but not proved: `MathlibExt.GroupTheory.FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.nonabelianPGroupFrattiniCenterH1Trivial_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrattiniCenterFirstCohomologyKourovka17Problem2Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/cohomology-of-p-groups-and-the-frattini-subgroup/index.html#nonabelian-pgroup-frattini-center-h1-tri-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cohomology of p-groups and the Frattini subgroup](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/cohomology-of-p-groups-and-the-frattini-subgroup/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-p-groups/cohomology-of-p-groups-and-the-frattini-subgroup)
