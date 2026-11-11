---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.generatorRank, MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.trivialZModpRep, MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.relationRank, MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.golod_shafarevich_inequality
statement: formalized
---

# Golod–Shafarevich inequality

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/golod-shafarevich-inequality/index.html).

## Generator rank

For a topological group $G$, the generator rank $d(G)$ is the least
natural number $k$ such that some finite subset of $G$ with $k$ elements generates a dense
subgroup of $G$, that is, a subgroup whose closure is all of $G$. If no finite subset of $G$
generates a dense subgroup, then $d(G)$ is defined to be $0$. For a finite discrete group this is
the ordinary minimal number of generators.

Formalized by `MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.generatorRank`, a definition declared in [WantedExt/GroupTheory/GolodShafarevichWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GolodShafarevichWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/golod-shafarevich-inequality/index.html#generator-rank).

## Trivial representation on $\mathbb{Z}/p\mathbb{Z}$

For a natural number $p$ and a
topological group $G$, this is $\mathbb{Z}/p\mathbb{Z}$, with its discrete topology, regarded as
a continuous representation of $G$ over $\mathbb{Z}/p\mathbb{Z}$ on which every element of $G$
acts as the identity.

Formalized by `MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.trivialZModpRep`, a definition declared in [WantedExt/GroupTheory/GolodShafarevichWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GolodShafarevichWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/golod-shafarevich-inequality/index.html#trivial-zmodp-rep).

## Relation rank

For a prime $p$ and a topological group $G$, the relation rank $r(G)$
is the dimension over $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ of the continuous cohomology
group $H^2(G, \mathbb{F}_p)$, where $G$ acts trivially on $\mathbb{F}_p$. If this space is
infinite-dimensional, then $r(G)$ is defined to be $0$.

Formalized by `MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.relationRank`, a definition declared in [WantedExt/GroupTheory/GolodShafarevichWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GolodShafarevichWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/golod-shafarevich-inequality/index.html#relation-rank).

## Golod–Shafarevich inequality

Let $p$ be a prime and let $Q$ be a nontrivial finite
$p$-group, viewed as a topological group with the discrete topology. Then the generator rank
$d(Q)$ and the relation rank $r(Q)$, the dimension over $\mathbb{F}_p$ of the continuous
cohomology group $H^2(Q, \mathbb{F}_p)$ with trivial coefficients, satisfy $d(Q)^2 < 4\, r(Q)$.

## Sources

- NSW (J. Neukirch, A. Schmidt, K. Wingberg, *Cohomology of Number Fields*, 2nd ed., Grundlehren 323, Springer 2008), Theorem 3.9.7; J.-P. Serre, *Galois Cohomology*, Chapter I, Appendix 2, Theorem 1. Lean hypothesis: https://github.com/logical-intelligence/erdos-unit-distance (Hyp_GolodShafarevichInequality). Problem `golod_shafarevich_inequality` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.GolodShafarevichWanted.GroupTheory.golod_shafarevich_inequality` is written with `theorem_wanted` in [WantedExt/GroupTheory/GolodShafarevichWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/GolodShafarevichWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/golod-shafarevich-inequality/index.html#golod-shafarevich-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Golod–Shafarevich inequality](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/golod-shafarevich-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/golod-shafarevich-inequality)
