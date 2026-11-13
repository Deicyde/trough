---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsPiNumber, MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsPiSubgroup, MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsHallPiSubgroup, MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsMaximalPiSubgroup, MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsDPiGroup, MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.piCore, MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.threeHallSubgroupsIntersectInCore, MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.threeHallSubgroupsIntersectInCore_refuted
statement: formalized
---

# Hall π-subgroups

27 results, 22 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html).

## π-numbers (Kourovka 18.31)

Let $\pi$ be a set of natural numbers. A natural number $n$
is a $\pi$-number when every prime divisor of $n$ lies in $\pi$.

Formalized by `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsPiNumber`, a definition declared in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-pi-number).

## π-subgroups

Let $\pi$ be a set of natural numbers. A subgroup $H$ of a group $G$ is a
$\pi$-subgroup when its order is a $\pi$-number, that is, every prime divisor of $|H|$ lies in
$\pi$.

The order of an infinite subgroup is taken to be $0$, which every prime divides.

Formalized by `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsPiSubgroup`, a definition declared in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-pi-subgroup).

## Hall π-subgroups (Kourovka 18.31)

Let $\pi$ be a set of natural numbers. A subgroup $H$
of a group $G$ is a Hall $\pi$-subgroup when it is a $\pi$-subgroup and no prime divisor of its
index $|G : H|$ lies in $\pi$.

An infinite index is taken to be $0$, which every prime divides.

Formalized by `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsHallPiSubgroup`, a definition declared in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-hall-pi-subgroup).

## Maximal π-subgroups (Kourovka 18.31)

Let $\pi$ be a set of natural numbers. A subgroup
$H$ of a group $G$ is a maximal $\pi$-subgroup when it is a $\pi$-subgroup and every
$\pi$-subgroup $K$ of $G$ containing $H$ equals $H$.

Formalized by `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsMaximalPiSubgroup`, a definition declared in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-maximal-pi-subgroup).

## Dπ-groups

Let $\pi$ be a set of natural numbers. A group $G$ is a
$D_\pi$-group when any two maximal $\pi$-subgroups $H$ and $K$ of $G$ are conjugate, that is,
$K = gHg^{-1}$ for some $g \in G$.

## Sources

- Kourovka Archive, Problem 3.62.

Formalized by `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.IsDPiGroup`, a definition declared in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-dpi-group).

## The π-core

Let $\pi$ be a set of natural numbers. For a group $G$, the $\pi$-core
$O_\pi(G)$ is the subgroup of $G$ generated by all normal $\pi$-subgroups of $G$.

When $G$ is finite, $O_\pi(G)$ is the largest normal $\pi$-subgroup of $G$.

Formalized by `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.piCore`, a definition declared in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#pi-core).

## Three Hall π-subgroups meeting in the π-core (Kourovka 18.31)

For every set $\pi$ of
natural numbers and every finite $D_\pi$-group $G$, there are Hall $\pi$-subgroups $H_1$, $H_2$,
$H_3$ of $G$, not necessarily distinct, with $H_1 \cap H_2 \cap H_3 = O_\pi(G)$, the
$\pi$-core of $G$.

This is the question of E. P. Vdovin and D. O. Revin; only the primes in $\pi$ matter.

Formalized by `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.threeHallSubgroupsIntersectInCore`, a definition declared in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#three-hall-subgroups-intersect-in-core).

## Three Hall π-subgroups need not meet in the π-core

It is not the case that for every set
$\pi$ of natural numbers every finite $D_\pi$-group $G$ has Hall $\pi$-subgroups $H_1$, $H_2$,
$H_3$ with $H_1 \cap H_2 \cap H_3 = O_\pi(G)$, the $\pi$-core of $G$: the answer to
Kourovka 18.31 is negative.

V. I. Zenkov (2022) gave a counterexample: $G$ an extension of $L_2(27)$ by a field automorphism
of order $3$, with a subgroup $H$ that is an extension of a Borel subgroup of $L_2(27)$ by a field
automorphism of order $3$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.31 (E. P. Vdovin, D. O. Revin); resolution: V. I. Zenkov, Siberian Math. J. 63 (2022), no. 4, 720-722, Kourovka Archive, Problem 18.31: No; G an extension of L_2(27) by a field automorphism of order 3, H an extension of a Borel subgroup of L_2(27) by a field automorphism of order 3, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.DPiHallIntersectionKourovka18Problem31Wanted.threeHallSubgroupsIntersectInCore_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiHallIntersectionKourovka18Problem31Wanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#three-hall-subgroups-intersect-in-core-r).

## $\pi$-numbers

Let $\pi$ be a set of natural numbers. A natural number $n$ is a
$\pi$-number when every prime dividing $n$ lies in $\pi$.

Formalized by `MathlibExt.GroupTheory.DPiNormalSubgroupKourovka13Problem33Wanted.IsPiNumber`, a definition declared in [WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-pi-number-2).

## Hall $\pi$-subgroups

Let $\pi$ be a set of natural numbers. A subgroup $H$ of a group $G$
is a Hall $\pi$-subgroup when its order $|H|$ is a $\pi$-number and no prime dividing its index
$|G : H|$ lies in $\pi$. Here an infinite order or index is taken to be $0$, which every prime
divides.

Formalized by `MathlibExt.GroupTheory.DPiNormalSubgroupKourovka13Problem33Wanted.IsHallPiSubgroup`, a definition declared in [WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-hall-pi-subgroup-2).

## $D_\pi$-groups

Let $\pi$ be a set of natural numbers (only the primes in $\pi$ matter). A
group $G$ is a $D_\pi$-group (Kourovka Archive 3.62) when $G$ has a Hall $\pi$-subgroup, any two
Hall $\pi$-subgroups $H$ and $K$ of $G$ are conjugate ($K = gHg^{-1}$ for some $g \in G$), and every
subgroup of $G$ whose order is a $\pi$-number lies in some Hall $\pi$-subgroup. Here the order of an
infinite subgroup is taken to be $0$, which every prime divides.

Formalized by `MathlibExt.GroupTheory.DPiNormalSubgroupKourovka13Problem33Wanted.IsDPi`, a definition declared in [WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-dpi).

## Kourovka Problem 13.33

This is the proposition (F. Gross) that for every set $\pi$ of
natural numbers, every normal subgroup of a finite $D_\pi$-group is itself a $D_\pi$-group.

Formalized by `MathlibExt.GroupTheory.DPiNormalSubgroupKourovka13Problem33Wanted.normalSubgroupOfDPiIsDPi`, a definition declared in [WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#normal-subgroup-of-dpi-is-dpi).

## Normal subgroups of finite $D_\pi$-groups are $D_\pi$-groups

Kourovka Problem 13.33 has a
positive answer: for every set $\pi$ of natural numbers, every normal subgroup of a finite
$D_\pi$-group is itself a $D_\pi$-group.

The Kourovka Archive answers 13.33 "Yes, it is" modulo the classification of finite simple groups
(E. P. Vdovin and D. O. Revin, 2006).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.33 (F. Gross; V. D. Mazurov); resolution: E. P. Vdovin and D. O. Revin, in: Ischia Group Theory 2004, Contemp. Math. 402, Amer. Math. Soc., 2006, 229-263, Kourovka Archive, Problem 13.33: Yes, it is mod CFSG.

Stated but not proved: `MathlibExt.GroupTheory.DPiNormalSubgroupKourovka13Problem33Wanted.normalSubgroupOfDPiIsDPi_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DPiNormalSubgroupKourovka13Problem33Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#normal-subgroup-of-dpi-is-dpi-holds).

## $\pi$-number

Let $\pi$ be a set of natural numbers (only the primes in it matter). A
natural number $n$ is a $\pi$-number when every prime divisor of $n$ lies in $\pi$.

Formalized by `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.IsPiNumber`, a definition declared in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-pi-number-3).

## Hall $\pi$-subgroup

Let $\pi$ be a set of natural numbers and $G$ a group. A subgroup $H$
of $G$ is a Hall $\pi$-subgroup when its order $|H|$ is a $\pi$-number and no prime divisor of its
index $|G : H|$ lies in $\pi$.

An infinite order or index counts as $0$; the notion is meant for finite groups.

Formalized by `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.IsHallPiSubgroup`, a definition declared in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-hall-pi-subgroup-3).

## Maximal $\pi$-subgroup

Let $\pi$ be a set of natural numbers and $G$ a group. A subgroup
$H$ of $G$ is a maximal $\pi$-subgroup when its order $|H|$ is a $\pi$-number and every subgroup $L$
of $G$ that contains $H$ and whose order is a $\pi$-number equals $H$.

An infinite order counts as $0$; the notion is meant for finite groups.

Formalized by `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.IsMaximalPiSubgroup`, a definition declared in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-maximal-pi-subgroup-2).

## $C_\pi$-group

Let $\pi$ be a set of natural numbers. A group $G$ is a $C_\pi$-group when it
has a Hall $\pi$-subgroup and any two Hall $\pi$-subgroups $H$ and $K$ of $G$ are conjugate, that
is, $K = gHg^{-1}$ for some $g \in G$.

Formalized by `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.IsCPiGroup`, a definition declared in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-cpi-group).

## $D_\pi$-group

Let $\pi$ be a set of natural numbers. A group $G$ is a $D_\pi$-group when
any two maximal $\pi$-subgroups $H$ and $K$ of $G$ are conjugate, that is, $K = gHg^{-1}$ for
some $g \in G$.

Formalized by `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.IsDPiGroup`, a definition declared in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-dpi-group-2).

## Kourovka Problem 17.44(a): overgroups of Hall subgroups in $C_\pi$-groups

The statement,
posed by E. P. Vdovin and D. O. Revin, that for every set $\pi$ of natural numbers and every finite
$C_\pi$-group $G$, every subgroup $K$ of $G$ that contains a Hall $\pi$-subgroup of $G$ is itself a
$C_\pi$-group.

Formalized by `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.hallOvergroupCPi`, a definition declared in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#hall-overgroup-cpi).

## Kourovka Problem 17.44(b): overgroups of Hall subgroups in $D_\pi$-groups

The statement,
posed by E. P. Vdovin and D. O. Revin, that for every set $\pi$ of natural numbers and every finite
$D_\pi$-group $G$, every subgroup $K$ of $G$ that contains a Hall $\pi$-subgroup of $G$ is itself a
$D_\pi$-group.

Formalized by `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.hallOvergroupDPi`, a definition declared in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#hall-overgroup-dpi).

## Overgroups of Hall subgroups in $C_\pi$-groups (Vdovin–Revin)

Let $\pi$ be a set of natural
numbers and let $G$ be a finite $C_\pi$-group. Then every subgroup $K$ of $G$ that contains a Hall
$\pi$-subgroup of $G$ is itself a $C_\pi$-group. This answers Kourovka Problem 17.44(a) in the
affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.44 (E. P. Vdovin, D. O. Revin); resolution: (a) E. P. Vdovin and D. O. Revin, Siberian Math. J. 54 (2013), 22-28; (b) N. Ch. Manzaeva, preprint, arXiv:1504.03137, and E. P. Vdovin, N. Ch. Manzaeva and D. O. Revin, Sb. Math. 211 (2020), 309-335, Kourovka Archive, Problem 17.44 (a) Yes, it is; b) Yes, it is), https://arxiv.org/abs/1504.03137.

Stated but not proved: `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.hallOvergroupCPi_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#hall-overgroup-cpi-holds).

## Overgroups of Hall subgroups in $D_\pi$-groups (Manzaeva, Vdovin–Manzaeva–Revin)

Let $\pi$ be
a set of natural numbers and let $G$ be a finite $D_\pi$-group. Then every subgroup $K$ of $G$ that
contains a Hall $\pi$-subgroup of $G$ is itself a $D_\pi$-group. This answers Kourovka Problem
17.44(b) in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.44 (E. P. Vdovin, D. O. Revin); resolution: (a) E. P. Vdovin and D. O. Revin, Siberian Math. J. 54 (2013), 22-28; (b) N. Ch. Manzaeva, preprint, arXiv:1504.03137, and E. P. Vdovin, N. Ch. Manzaeva and D. O. Revin, Sb. Math. 211 (2020), 309-335, Kourovka Archive, Problem 17.44 (a) Yes, it is; b) Yes, it is), https://arxiv.org/abs/1504.03137.

Stated but not proved: `MathlibExt.GroupTheory.HallOvergroupCPiDPiKourovka17Problem44Wanted.hallOvergroupDPi_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallOvergroupCPiDPiKourovka17Problem44Wanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#hall-overgroup-dpi-holds).

## π-numbers

Let $\pi$ be a set of natural numbers. A natural number $n$ is a $\pi$-number
when every prime divisor of $n$ lies in $\pi$.

Formalized by `MathlibExt.GroupTheory.HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.IsPiNumber`, a definition declared in [WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-pi-number-4).

## Hall π-subgroups

Let $\pi$ be a set of natural numbers and let $H$ be a subgroup of a
group $G$. Then $H$ is a Hall $\pi$-subgroup when its order $|H|$ is a $\pi$-number and no prime
divisor of its index $|G : H|$ lies in $\pi$.

Formalized by `MathlibExt.GroupTheory.HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.IsHallPiSubgroup`, a definition declared in [WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#is-hall-pi-subgroup-4).

## The class $E_\pi$ of groups with a Hall π-subgroup

Let $\pi$ be a set of natural numbers.
A group $G$ belongs to the class $E_\pi$ when $G$ has a Hall $\pi$-subgroup.

Formalized by `MathlibExt.GroupTheory.HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.HasHallPiSubgroup`, a definition declared in [WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#has-hall-pi-subgroup).

## Zavarnitsine's question on Hall subgroups for intersections of prime sets

This is the
statement that for all sets $\pi_1$ and $\pi_2$ of natural numbers, every finite group that has a
Hall $\pi_1$-subgroup and a Hall $\pi_2$-subgroup also has a Hall $(\pi_1 \cap \pi_2)$-subgroup;
that is, writing $E_\pi$ for the class of finite groups with a Hall $\pi$-subgroup,
$E_{\pi_1} \cap E_{\pi_2}$ is contained in $E_{\pi_1 \cap \pi_2}$.

This is Kourovka Notebook Problem 18.38 (A. V. Zavarnitsine).

Formalized by `MathlibExt.GroupTheory.HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.hallSubgroupForIntersectionOfPrimeSets`, a definition declared in [WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#hall-subgroup-for-intersection-of-prime).

## Hall subgroups exist for intersections of prime sets

For all sets $\pi_1$ and $\pi_2$ of
natural numbers, every finite group that has a Hall $\pi_1$-subgroup and a Hall $\pi_2$-subgroup
also has a Hall $(\pi_1 \cap \pi_2)$-subgroup; that is, writing $E_\pi$ for the class of finite
groups with a Hall $\pi$-subgroup, $E_{\pi_1} \cap E_{\pi_2}$ is contained in
$E_{\pi_1 \cap \pi_2}$.

This answers Kourovka Notebook Problem 18.38 (A. V. Zavarnitsine) in the affirmative; the 21st
issue records the answer "Yes, it does" (N. Yang and A. A. Buturlakin, 2025).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.38 (A. V. Zavarnitsine); resolution: N. Yang and A. A. Buturlakin, A generalization of the Arad-Ward theorem on Hall subgroups, preprint, arXiv:2501.05865 (2025), abstract: E_{π₁} ∩ E_{π₂} is contained in E_{π₁ ∩ π₂}; the Kourovka Notebook (21st issue) marks 18.38 solved, https://arxiv.org/abs/2501.05865.

Stated but not proved: `MathlibExt.GroupTheory.HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.hallSubgroupForIntersectionOfPrimeSets_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/HallSubgroupPrimeSetIntersectionKourovka18Problem38Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html#hall-subgroup-for-intersection-of-prime-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hall π-subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/sylow-and-hall-subgroups/hall-subgroups)
