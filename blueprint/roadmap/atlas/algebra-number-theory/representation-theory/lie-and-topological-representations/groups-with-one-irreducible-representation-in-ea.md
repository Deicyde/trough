---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.IsIrreducibleRep, MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.IsEquivalentRep, MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.HasUniqueIrreducibleRepOfEachDim, MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.su2OnlyGroupWithUniqueIrreducibleReps, MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.su2OnlyGroupWithUniqueIrreducibleReps_refuted
statement: formalized
---

# Groups with one irreducible representation in each dimension

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea/index.html).

## Irreducible representations into $\mathrm{GL}_n(\mathbb{C})$

Let $G$ be a group and
$\rho \colon G \to \mathrm{GL}_n(\mathbb{C})$ a homomorphism. Then $\rho$ is irreducible when
$n \ge 1$ and the only subspaces $W$ of $\mathbb{C}^n$ with $\rho(g)v \in W$ for all $g \in G$ and
$v \in W$ are $0$ and $\mathbb{C}^n$.

Formalized by `MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.IsIrreducibleRep`, a definition declared in [WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea/index.html#is-irreducible-rep).

## Equivalent representations into $\mathrm{GL}_n(\mathbb{C})$

Let $G$ be a group. Two
homomorphisms $\rho, \sigma \colon G \to \mathrm{GL}_n(\mathbb{C})$ are equivalent when there is a
matrix $P \in \mathrm{GL}_n(\mathbb{C})$ with $\sigma(g) = P \rho(g) P^{-1}$ for all $g \in G$.

Formalized by `MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.IsEquivalentRep`, a definition declared in [WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea/index.html#is-equivalent-rep).

## Groups with exactly one irreducible representation of each dimension

A group $G$ has
exactly one irreducible complex representation of each dimension when for every $n \ge 1$ there
is an irreducible homomorphism $G \to \mathrm{GL}_n(\mathbb{C})$ and any two irreducible
homomorphisms $G \to \mathrm{GL}_n(\mathbb{C})$ are equivalent. Representations are arbitrary
homomorphisms of the abstract group $G$; no continuity is required.

Formalized by `MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.HasUniqueIrreducibleRepOfEachDim`, a definition declared in [WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea/index.html#has-unique-irreducible-rep-of-each-dim).

## McKay's question on $\mathrm{SU}_2(\mathbb{C})$ (Kourovka 16.58)

A group $G$ has exactly
one irreducible complex representation of each dimension $n = 1, 2, \dots$, up to equivalence, if
and only if $G$ is isomorphic to $\mathrm{SU}_2(\mathbb{C})$. Here a representation of dimension
$n$ is any homomorphism $G \to \mathrm{GL}_n(\mathbb{C})$ of abstract groups, with no continuity
required.

Formalized by `MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.su2OnlyGroupWithUniqueIrreducibleReps`, a definition declared in [WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea/index.html#su2-only-group-with-unique-irreducible-r).

## McKay's question 16.58 has a negative answer

It is not the case that a group has exactly
one irreducible complex representation of each dimension $n \ge 1$, up to equivalence, if and only
if it is isomorphic to $\mathrm{SU}_2(\mathbb{C})$. Here a representation of dimension $n$ is any
homomorphism to $\mathrm{GL}_n(\mathbb{C})$ of abstract groups, with no continuity required.

Applying a field automorphism $\varphi$ of $\mathbb{C}$ to matrix entries gives irreducible
$2$-dimensional representations $x \mapsto x^\varphi$ of the abstract group
$\mathrm{SU}_2(\mathbb{C})$, infinitely many of them pairwise non-equivalent (von Neumann), so
$\mathrm{SU}_2(\mathbb{C})$ itself lacks the property. It does have it if only unitary
representations are counted, as these are continuous (Cartan).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.58 (J. McKay); resolution: V. P. Burichenko, letter of 16 July 2013, as recorded in the Kourovka Archive (observation of J. von Neumann), Kourovka Archive, Problem 16.58 (No: for field automorphisms φ of ℂ the representations x ↦ x^φ of SU₂(ℂ) are irreducible and infinitely many are pairwise non-equivalent, so SU₂(ℂ) itself lacks the property; it has it for unitary representations, which are continuous by É. Cartan).

Stated but not proved: `MathlibExt.GroupTheory.UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.su2OnlyGroupWithUniqueIrreducibleReps_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/UniqueIrreducibleRepresentationsSU2Kourovka16Problem58Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea/index.html#su2-only-group-with-unique-irreducible-r-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups with one irreducible representation in each dimension](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RepresentationTheory/lie-and-topological-representations/groups-with-one-irreducible-representation-in-ea)
