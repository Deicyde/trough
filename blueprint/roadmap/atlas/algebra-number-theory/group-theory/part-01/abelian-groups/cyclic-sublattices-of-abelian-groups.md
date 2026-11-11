---
declaration: section
origin: cited
lean: AddSubgroup.IsCyclicSublattice, AddSubgroup.isCyclicSublattice_iff, AddSubgroup.IsCyclicSublattice.le, AddSubgroup.IsCyclicSublattice.isAddCyclic_quotient, AddSubgroup.IsCyclicSublattice.mk
statement: formalized
proof: formalized
---

# Cyclic sublattices of abelian groups

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups/index.html).

## Cyclic sublattice of a subgroup

Let $A$ be an abelian group and let $L'$ and $L$ be
subgroups of $A$. Then $L'$ is a cyclic sublattice of $L$ when $L' \subseteq L$ and the quotient
group $L/L'$ is cyclic; formally the quotient is taken by $L' \cap L$, regarded as a subgroup
of $L$.

Formalized by `AddSubgroup.IsCyclicSublattice`, a definition declared in [MathlibExt/GroupTheory/CyclicSublattice.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/CyclicSublattice.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups/index.html#is-cyclic-sublattice).

## Characterization of cyclic sublattices

Let $L'$ and $L$ be subgroups of an abelian
group $A$. Then $L'$ is a cyclic sublattice of $L$ if and only if $L' \subseteq L$ and the
quotient group $L/(L' \cap L)$, with $L' \cap L$ regarded as a subgroup of $L$, is cyclic.

Formalized by `AddSubgroup.isCyclicSublattice_iff`, a theorem declared in [MathlibExt/GroupTheory/CyclicSublattice.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/CyclicSublattice.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups/index.html#is-cyclic-sublattice-iff).

## A cyclic sublattice is contained in its ambient subgroup

Let $L'$ and $L$ be subgroups
of an abelian group $A$. If $L'$ is a cyclic sublattice of $L$, then $L' \subseteq L$.

Formalized by `AddSubgroup.IsCyclicSublattice.le`, a theorem declared in [MathlibExt/GroupTheory/CyclicSublattice.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/CyclicSublattice.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups/index.html#le).

## The quotient by a cyclic sublattice is cyclic

Let $L'$ and $L$ be subgroups of an
abelian group $A$. If $L'$ is a cyclic sublattice of $L$, then the quotient group $L/L'$ is
cyclic.

Formalized by `AddSubgroup.IsCyclicSublattice.isAddCyclic_quotient`, a theorem declared in [MathlibExt/GroupTheory/CyclicSublattice.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/CyclicSublattice.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups/index.html#is-add-cyclic-quotient).

## Criterion for a cyclic sublattice

Let $L'$ and $L$ be subgroups of an abelian group $A$.
If $L' \subseteq L$ and the quotient group $L/L'$ is cyclic, then $L'$ is a cyclic sublattice
of $L$.

Formalized by `AddSubgroup.IsCyclicSublattice.mk`, a theorem declared in [MathlibExt/GroupTheory/CyclicSublattice.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/CyclicSublattice.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups/index.html#mk).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cyclic sublattices of abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/abelian-groups/cyclic-sublattices-of-abelian-groups)
