---
declaration: section
origin: cited
lean: MathlibExt.Topology.AutFnFiniteIndexPositiveBettiWanted.firstBettiRank, MathlibExt.Topology.AutFnFiniteIndexPositiveBettiWanted.conjecture, MathlibExt.Topology.AutFnFiniteIndexPositiveBettiWanted.conjecture_refuted, MathlibExt.Topology.AutFnFiniteIndexPropertyFAWanted.HasPropertyFA, MathlibExt.Topology.AutFnFiniteIndexPropertyFAWanted.conjecture, MathlibExt.Topology.AutFnFiniteIndexPropertyFAWanted.conjecture_holds
statement: formalized
---

# Finite-index subgroups of automorphism groups of free groups

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html).

## First Betti number of a group

The first Betti number of a group $G$ is the rank, as a
cardinal, of its abelianization $G^{\mathrm{ab}}$ viewed as a $\mathbb{Z}$-module.

## Sources

- [AMR-109-0273] (Question 2.5, PDF p. 330).

Formalized by `MathlibExt.Topology.AutFnFiniteIndexPositiveBettiWanted.firstBettiRank`, a definition declared in [WantedExt/Topology/AutFnFiniteIndexPositiveBettiWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AutFnFiniteIndexPositiveBettiWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html#first-betti-rank).

## Farb's positive first Betti number question for $\mathrm{Aut}(F_n)$

The proposition that
for every natural number $n > 3$, the automorphism group $\mathrm{Aut}(F_n)$ of the free group
$F_n$ on $n$ generators has a finite-index subgroup $H$ whose first Betti number, the
$\mathbb{Z}$-rank of the abelianization of $H$, is positive.

## Sources

- Farb Question 2.5 [AMR-109-0273] (PDF p. 330).

Formalized by `MathlibExt.Topology.AutFnFiniteIndexPositiveBettiWanted.conjecture`, a definition declared in [WantedExt/Topology/AutFnFiniteIndexPositiveBettiWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AutFnFiniteIndexPositiveBettiWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html#conjecture).

## Some $\mathrm{Aut}(F_n)$ with $n > 3$ has no finite-index subgroup of positive first Betti number

**Some $\mathrm{Aut}(F_n)$ with $n > 3$ has no finite-index subgroup of positive first Betti
number.** It is not the case that for every natural number $n > 3$ the automorphism group
$\mathrm{Aut}(F_n)$ of the free group $F_n$ on $n$ generators has a finite-index subgroup $H$ whose
first Betti number, the $\mathbb{Z}$-rank of the abelianization of $H$, is positive.

The case $n = 5$ fails: Kaluba, Nowak and Ozawa proved that $\mathrm{Aut}(F_5)$ has Kazhdan's
property (T), which passes to finite-index subgroups and forces finite abelianization, so every
finite-index subgroup of $\mathrm{Aut}(F_5)$ has first Betti number $0$.

## Sources

- M. Kaluba, P. W. Nowak, N. Ozawa, Aut(F5) has property (T), Math. Ann. 375 (2019), no. 3-4, 1169-1191, https://arxiv.org/abs/1712.07167.

Stated but not proved: `MathlibExt.Topology.AutFnFiniteIndexPositiveBettiWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Topology/AutFnFiniteIndexPositiveBettiWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AutFnFiniteIndexPositiveBettiWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html#conjecture-refuted).

## Serre's Property FA

A group $G$ has Property FA when every action of $G$ on a tree
without edge inversion has a global fixed vertex: for every tree $T$ with vertex set $V$ and every
homomorphism $\alpha$ from $G$ to the group of permutations of $V$ such that each $\alpha(g)$
satisfies $\alpha(g)(u) \sim \alpha(g)(v) \iff u \sim v$ for all vertices $u, v$ (where $\sim$ is
adjacency in $T$), and such that no $\alpha(g)$ swaps the two ends of an edge, there is a vertex
$v$ with $\alpha(g)(v) = v$ for all $g \in G$.

## Sources

- [AMR-109-0276] (Question 2.8, PDF p. 331).

Formalized by `MathlibExt.Topology.AutFnFiniteIndexPropertyFAWanted.HasPropertyFA`, a definition declared in [WantedExt/Topology/AutFnFiniteIndexPropertyFAWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AutFnFiniteIndexPropertyFAWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html#has-property-fa).

## Farb's question on Property FA for finite-index subgroups of $\operatorname{Aut}(F_n)$

The proposition that for every natural number $n \ge 4$, every subgroup of finite index in the
automorphism group $\operatorname{Aut}(F_n)$ of the free group $F_n$ on $n$ generators has Serre's
Property FA.

## Sources

- Farb Question 2.8 [AMR-109-0276] (PDF p. 331).

Formalized by `MathlibExt.Topology.AutFnFiniteIndexPropertyFAWanted.conjecture`, a definition declared in [WantedExt/Topology/AutFnFiniteIndexPropertyFAWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AutFnFiniteIndexPropertyFAWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html#conjecture-2).

## Finite-index subgroups of $\operatorname{Aut}(F_n)$ have Property FA for $n \ge 4$

For every
natural number $n \ge 4$, every subgroup of finite index in the automorphism group
$\operatorname{Aut}(F_n)$ of the free group $F_n$ on $n$ generators has Serre's Property FA.

This answers Farb's Question 2.8 positively: $\operatorname{Aut}(F_n)$ has Kazhdan's property (T)
for $n \ge 4$ (Kaluba–Kielak–Nowak for $n \ge 6$, Kaluba–Nowak–Ozawa for $n = 5$, Nitsche for
$n = 4$), property (T) passes to finite-index subgroups, and it implies Serre's Property FA
(Watatani).

## Sources

- Marek Kaluba, Dawid Kielak and Piotr W. Nowak, On property (T) for Aut(F_n) and SL_n(Z), Ann. of Math. 193 (2021), arXiv:1812.03456, https://arxiv.org/abs/1812.03456; Martin Nitsche, Computer proofs for Property (T), and SDP duality, arXiv:2009.05134v3 (2022), https://arxiv.org/abs/2009.05134.

Stated but not proved: `MathlibExt.Topology.AutFnFiniteIndexPropertyFAWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Topology/AutFnFiniteIndexPropertyFAWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/AutFnFiniteIndexPropertyFAWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite-index subgroups of automorphism groups of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/finite-index-subgroups-of-automorphism-groups-of)
