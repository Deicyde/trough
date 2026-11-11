---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TrivialCentreTwistedClassKourovka18Problem15Wanted.twistedUnitClass, MathlibExt.GroupTheory.TrivialCentreTwistedClassKourovka18Problem15Wanted.trivialCentreHasInnerTwistedClassNotSubgroup, MathlibExt.GroupTheory.TrivialCentreTwistedClassKourovka18Problem15Wanted.trivialCentreHasInnerTwistedClassNotSubgroup_refuted, MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClass, MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.AllTwistedUnitClassesSubgroups, MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClassesSubgroupsImpliesNilpotent, MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClassesSubgroupsFGImpliesAbelian, MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClassesSubgroupsImpliesNilpotent_refuted
statement: formalized
---

# Twisted conjugacy classes

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html).

## Twisted conjugacy class of the identity (Kourovka 18.15)

For a group $G$ and an
automorphism $\varphi$ of $G$, the $\varphi$-twisted conjugacy class of the identity is the set
$[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\} \subseteq G$.

Formalized by `MathlibExt.GroupTheory.TrivialCentreTwistedClassKourovka18Problem15Wanted.twistedUnitClass`, a definition declared in [WantedExt/GroupTheory/TrivialCentreTwistedClassKourovka18Problem15Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TrivialCentreTwistedClassKourovka18Problem15Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#twisted-unit-class).

## Kourovka Problem 18.15: an inner twisted class that is not a subgroup

Every nontrivial
group $G$ with trivial centre has an element $a \in G$ such that, for the inner automorphism
$\varphi(g) = aga^{-1}$, the twisted conjugacy class of the identity
$[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\}$ is not a subgroup of $G$.

The conjecture is due to V. G. Bardakov, M. V. Neshchadim and T. R. Nasybullov.

Formalized by `MathlibExt.GroupTheory.TrivialCentreTwistedClassKourovka18Problem15Wanted.trivialCentreHasInnerTwistedClassNotSubgroup`, a definition declared in [WantedExt/GroupTheory/TrivialCentreTwistedClassKourovka18Problem15Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TrivialCentreTwistedClassKourovka18Problem15Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#trivial-centre-has-inner-twisted-class-n).

## Negative answer to Kourovka Problem 18.15

The conjecture of Kourovka Problem 18.15 is
false: there is a nontrivial group $G$ with trivial centre such that for every $a \in G$, with
$\varphi$ the inner automorphism $\varphi(g) = aga^{-1}$, the twisted conjugacy class of the
identity $[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\}$ is a subgroup of $G$.

The Kourovka Archive answers 18.15 "No, not always", citing V. V. Bludov's Example 2 in
Gonçalves–Nasybullov (2019), a group with trivial centre in which $[e]_\varphi$ is a subgroup for
every inner automorphism $\varphi$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.15 (V. G. Bardakov, M. V. Neshchadim, T. R. Nasybullov); resolution: V. V. Bludov, Example 2 in D. Gonçalves and T. Nasybullov, On groups where the twisted conjugacy class of the unit element is a subgroup, Comm. Algebra 47 (2019), no. 3, 930-944, Kourovka Archive, Problem 18.15: No, not always; see Bludov's Example 2, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.TrivialCentreTwistedClassKourovka18Problem15Wanted.trivialCentreHasInnerTwistedClassNotSubgroup_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TrivialCentreTwistedClassKourovka18Problem15Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TrivialCentreTwistedClassKourovka18Problem15Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#trivial-centre-has-inner-twisted-class-n-2).

## Twisted conjugacy class of the identity (Kourovka 18.14)

For a group $G$ and an
automorphism $\varphi$ of $G$, the $\varphi$-twisted conjugacy class of the identity is the set
$[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\} \subseteq G$.

Formalized by `MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClass`, a definition declared in [WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#twisted-unit-class-2).

## Groups whose twisted classes of the identity are all subgroups

A group $G$ has this
property when, for every automorphism $\varphi$ of $G$, the twisted conjugacy class of the
identity $[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\}$ is a subgroup of $G$.

Formalized by `MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.AllTwistedUnitClassesSubgroups`, a definition declared in [WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#all-twisted-unit-classes-subgroups).

## Kourovka Problem 18.14, nilpotency assertion

Every group $G$ in which, for every
automorphism $\varphi$ of $G$, the twisted conjugacy class of the identity
$[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\}$ is a subgroup of $G$, is nilpotent.

This is the first assertion of the conjecture of V. G. Bardakov, M. V. Neshchadim and
T. R. Nasybullov.

Formalized by `MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClassesSubgroupsImpliesNilpotent`, a definition declared in [WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#twisted-unit-classes-subgroups-implies-n).

## Kourovka Problem 18.14, abelian assertion for finitely generated groups

Every finitely
generated group $G$ in which, for every automorphism $\varphi$ of $G$, the twisted conjugacy class
of the identity $[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\}$ is a subgroup of $G$, is abelian.

This is the second assertion of the conjecture of Kourovka Problem 18.14.

Formalized by `MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClassesSubgroupsFGImpliesAbelian`, a definition declared in [WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#twisted-unit-classes-subgroups-fgimplies).

## Negative answer to the nilpotency assertion of Kourovka Problem 18.14

There is a group $G$
that is not nilpotent although, for every automorphism $\varphi$ of $G$, the twisted conjugacy
class of the identity $[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\}$ is a subgroup of $G$.

Nicotera's Corollary 3.1 gives such an infinite group, a restricted direct product of the finite
groups of Theorem 1.2 for pairwise distinct primes.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.14 (V. G. Bardakov, M. V. Neshchadim, T. R. Nasybullov); resolution: C. Nicotera, On finite groups in which the twisted conjugacy classes of the unit element are subgroups, Arch. Math. 123 (2024), no. 3, 225-232, Theorem 1.2 (for every n and every odd prime p, a finite p-group of class n in which [G, φ] is a subgroup for every φ ∈ Aut G) and Corollary 3.1 (an infinite non-nilpotent group with this property); the Kourovka Notebook (21st issue) marks 18.14 solved, https://doi.org/10.1007/s00013-024-02025-6.

Stated but not proved: `MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClassesSubgroupsImpliesNilpotent_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#twisted-unit-classes-subgroups-implies-n-2).

## Negative answer to the abelian assertion of Kourovka Problem 18.14

There is a finitely
generated group $G$ that is not abelian although, for every automorphism $\varphi$ of $G$, the
twisted conjugacy class of the identity $[e]_\varphi = \{g^{-1}\varphi(g) : g \in G\}$ is a
subgroup of $G$.

Nicotera's Theorem 1.2 gives, for every $n$ and every odd prime $p$, a finite $p$-group of
nilpotency class $n$ with this property; for $n \ge 2$ it is not abelian.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.14 (V. G. Bardakov, M. V. Neshchadim, T. R. Nasybullov); resolution: C. Nicotera, On finite groups in which the twisted conjugacy classes of the unit element are subgroups, Arch. Math. 123 (2024), no. 3, 225-232, Theorem 1.2 (for every n and every odd prime p, a finite p-group of class n in which [G, φ] is a subgroup for every φ ∈ Aut G) and Corollary 3.1 (an infinite non-nilpotent group with this property); the Kourovka Notebook (21st issue) marks 18.14 solved, https://doi.org/10.1007/s00013-024-02025-6.

Stated but not proved: `MathlibExt.GroupTheory.TwistedUnitClassSubgroupKourovka18Problem14Wanted.twistedUnitClassesSubgroupsFGImpliesAbelian_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwistedUnitClassSubgroupKourovka18Problem14Wanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html#twisted-unit-classes-subgroups-fgimplies-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Twisted conjugacy classes](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/twisted-conjugacy-classes)
