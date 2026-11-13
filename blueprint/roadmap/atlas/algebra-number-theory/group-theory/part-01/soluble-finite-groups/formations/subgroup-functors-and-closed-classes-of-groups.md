---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.FiniteGroupClass, MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.IsClosedClass, MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.SubgroupAssignment, MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.IsClosedSubgroupFunctor, MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.FunctorLE, MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.primesOf, MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.existsNonnilpotentClassOfSmallWidth, MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.existsNonnilpotentClassOfSmallWidth_refuted
statement: formalized
---

# Subgroup functors and closed classes of groups

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html).

## Classes of finite groups (Kourovka 16.82 setting)

A class $\mathfrak{X}$ of finite groups
is a predicate on finite groups $G$ (with carrier in the lowest type universe, together with their
group structure); the groups satisfying it are the members of the class, written
$G \in \mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.FiniteGroupClass`, an abbreviation declared in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#finite-group-class).

## Closed classes of finite groups

A class $\mathfrak{X}$ of finite groups is closed when it
contains at least one group and is closed under homomorphic images, subgroups and direct products:
if $G \in \mathfrak{X}$ and $f : G \to H$ is a surjective homomorphism onto a finite group $H$,
then $H \in \mathfrak{X}$; every subgroup of a group in $\mathfrak{X}$ lies in $\mathfrak{X}$; and
if $G, H \in \mathfrak{X}$, then $G \times H \in \mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.IsClosedClass`, a definition declared in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#is-closed-class).

## Subgroup assignments

A subgroup assignment $\tau$ assigns to every finite group $G$ (with
carrier in the lowest type universe) a set $\tau(G)$ of subgroups of $G$.

Formalized by `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.SubgroupAssignment`, an abbreviation declared in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#subgroup-assignment).

## Closed subgroup functors

Let $\mathfrak{X}$ be a class of finite groups. A subgroup
assignment $\tau$ is a closed subgroup functor on $\mathfrak{X}$ (A. N. Skiba) when the following
three conditions hold. For every $G \in \mathfrak{X}$, $G \in \tau(G)$. For every surjective
homomorphism $\varphi : A \to B$ with $A, B \in \mathfrak{X}$, $\varphi(H) \in \tau(B)$ for every
$H \in \tau(A)$ and $\varphi^{-1}(T) \in \tau(A)$ for every $T \in \tau(B)$. For every
$G \in \mathfrak{X}$, every $H \in \tau(G)$ and every $K \in \tau(H)$, the subgroup $K$, viewed as
a subgroup of $G$, lies in $\tau(G)$; that is, $\tau(H) \subseteq \tau(G)$.

Formalized by `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.IsClosedSubgroupFunctor`, a definition declared in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#is-closed-subgroup-functor).

## Order on subgroup functors

Let $\mathfrak{X}$ be a class of finite groups. For subgroup
assignments $\tau_1$ and $\tau_2$, $\tau_1 \le \tau_2$ on $\mathfrak{X}$ when
$\tau_1(G) \subseteq \tau_2(G)$ for every $G \in \mathfrak{X}$. This is the order of the lattice
$F(\mathfrak{X})$ of closed subgroup functors on $\mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.FunctorLE`, a definition declared in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#functor-le).

## Prime divisors of a class of finite groups

For a class $\mathfrak{X}$ of finite groups,
$\pi(\mathfrak{X})$ is the set of primes $p$ that divide the order of some group in
$\mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.primesOf`, a definition declared in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#primes-of).

## Kourovka Problem 16.82 (Skiba)

For a class $\mathfrak{X}$ of finite groups, let
$\pi(\mathfrak{X})$ be the set of primes dividing the order of some group in $\mathfrak{X}$, and
for subgroup assignments $\tau_1, \tau_2$ write $\tau_1 \le \tau_2$ on $\mathfrak{X}$ when
$\tau_1(G) \subseteq \tau_2(G)$ for every $G \in \mathfrak{X}$. There is a class $\mathfrak{X}$ of
finite groups that contains at least one group, is closed under homomorphic images, subgroups and
direct products, and contains a non-nilpotent group, such that the lattice $F(\mathfrak{X})$ of
closed subgroup functors on $\mathfrak{X}$ has width at most $|\pi(\mathfrak{X})|$: every set of
closed subgroup functors on $\mathfrak{X}$ in which no two distinct members $\tau_1, \tau_2$
satisfy $\tau_1 \le \tau_2$ on $\mathfrak{X}$ has cardinality at most $|\pi(\mathfrak{X})|$.

Formalized by `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.existsNonnilpotentClassOfSmallWidth`, a definition declared in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#exists-nonnilpotent-class-of-small-width).

## Kourovka Problem 16.82 has a negative answer

For a class $\mathfrak{X}$ of finite groups,
let $\pi(\mathfrak{X})$ be the set of primes dividing the order of some group in $\mathfrak{X}$,
and for subgroup assignments $\tau_1, \tau_2$ write $\tau_1 \le \tau_2$ on $\mathfrak{X}$ when
$\tau_1(G) \subseteq \tau_2(G)$ for every $G \in \mathfrak{X}$. There is no class $\mathfrak{X}$ of
finite groups that contains at least one group, is closed under homomorphic images, subgroups and
direct products, contains a non-nilpotent group, and has the following property: every set of
closed subgroup functors on $\mathfrak{X}$ in which no two distinct members $\tau_1, \tau_2$
satisfy $\tau_1 \le \tau_2$ on $\mathfrak{X}$ has cardinality at most $|\pi(\mathfrak{X})|$. In
other words, for every such class the lattice $F(\mathfrak{X})$ of closed subgroup functors on
$\mathfrak{X}$ has width greater than $|\pi(\mathfrak{X})|$.

The Kourovka Archive answers 16.82 "No such classes exist", citing Kamornikov (2010).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.82 (A. N. Skiba); resolution: S. F. Kamornikov, Siberian Math. J. 51 (2010), no. 5, 824-829, Kourovka Archive, Problem 16.82 (No such classes exist).

Stated but not proved: `MathlibExt.GroupTheory.ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.existsNonnilpotentClassOfSmallWidth_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ClosedSubgroupFunctorLatticeWidthKourovka16Problem82Wanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html#exists-nonnilpotent-class-of-small-width-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgroup functors and closed classes of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/subgroup-functors-and-closed-classes-of-groups)
