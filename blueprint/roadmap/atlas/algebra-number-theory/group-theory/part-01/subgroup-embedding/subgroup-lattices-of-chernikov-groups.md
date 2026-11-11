---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.IsQuasicyclic, MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.IsChernikov, MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.ContainsQuasicyclicSquare, MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.HasFiniteOrderDimension, MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.chernikovSubgroupLatticeFiniteDimension, MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.chernikovSubgroupLatticeFiniteDimension_holds
statement: formalized
---

# Subgroup lattices of Chernikov groups

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html).

## Quasicyclic group

A group $Q$ is quasicyclic if it is abelian and infinite and every
proper subgroup of $Q$ is finite.

These are exactly the Prüfer groups $C_{p^\infty}$ for primes $p$.

Formalized by `MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.IsQuasicyclic`, a definition declared in [WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html#is-quasicyclic).

## Chernikov group

A group $G$ is a Chernikov group if it has a normal subgroup of finite
index that is isomorphic to a direct product $Q_1 \times \dots \times Q_r$ of finitely many
quasicyclic groups $Q_1, \dots, Q_r$. The case $r = 0$ is allowed, so every finite group is a
Chernikov group.

Formalized by `MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.IsChernikov`, a definition declared in [WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html#is-chernikov).

## Groups containing the square of a quasicyclic group

A group $G$ contains a direct product
of two quasicyclic groups over the same prime when there are a quasicyclic group $Q$ and an
injective group homomorphism $Q \times Q \to G$ (quasicyclic groups over the same prime are
isomorphic).

Formalized by `MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.ContainsQuasicyclicSquare`, a definition declared in [WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html#contains-quasicyclic-square).

## Poset of finite order dimension

A partially ordered set has finite (order) dimension: its order relation is the intersection
of finitely many linear orders on the same set.

Formalized by `MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.HasFiniteOrderDimension`, a definition declared in [WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html#has-finite-order-dimension).

## Shevrin's problem on the dimension of subgroup lattices of Chernikov groups

The
proposition that for every Chernikov group $G$ that does not contain a direct product of two
quasicyclic groups over the same prime (that is, there is no quasicyclic group $Q$ with an
injective homomorphism $Q \times Q \to G$), the lattice of subgroups of $G$ has finite order
dimension: the inclusion order on the subgroups of $G$ is the intersection of finitely many linear
orders on that set. This is Kourovka Problem 11.116 (L. N. Shevrin).

Formalized by `MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.chernikovSubgroupLatticeFiniteDimension`, a definition declared in [WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html#chernikov-subgroup-lattice-finite-dimens).

## Subgroup lattices of Chernikov groups without a quasicyclic square have finite dimension

Let $G$ be a Chernikov group, that is, a group with a normal subgroup of finite index isomorphic to
a direct product of finitely many quasicyclic groups (infinite abelian groups all of whose proper
subgroups are finite). Suppose that $G$ does not contain a direct product of two quasicyclic groups
over the same prime: there is no quasicyclic group $Q$ with an injective homomorphism
$Q \times Q \to G$. Then the lattice of subgroups of $G$ has finite order dimension: the inclusion
order on the subgroups of $G$ is the intersection of finitely many linear orders on that set.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 11.116 (L. N. Shevrin); resolution: M. Kinyon and J. Urban (with Codex gpt-6-astra), Results on problems from the Kourovka Notebook, preprint, version 4 (19 September 2026), Section 3.9: if `D ⊴ G` has index `m` and `D = C_{p₁^∞} × ⋯ × C_{p_r^∞}` with distinct primes, the subgroup lattice of `G` embeds in a product of `2rm` chains, so its order dimension is at most `2rm`; the Kourovka Notebook (21st issue) marks 11.116 solved (AI solution confirmed by P. Shumyatsky), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.chernikovSubgroupLatticeFiniteDimension_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ChernikovSubgroupLatticeDimensionKourovka11Problem116Wanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html#chernikov-subgroup-lattice-finite-dimens-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgroup lattices of Chernikov groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/subgroup-embedding/subgroup-lattices-of-chernikov-groups)
