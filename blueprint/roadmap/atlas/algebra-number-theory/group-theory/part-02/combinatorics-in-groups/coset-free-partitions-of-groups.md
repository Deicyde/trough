---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OddExponentCosetFreePartitionKourovka13Problem46Wanted.oddExponentCosetFreePartition, MathlibExt.GroupTheory.OddExponentCosetFreePartitionKourovka13Problem46Wanted.oddExponentCosetFreePartition_holds
statement: formalized
---

# Coset-free partitions of groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/coset-free-partitions-of-groups/index.html).

## Kourovka Problem 13.46: coset-free partitions

The proposition that every uncountable
abelian group $G$ of finite odd exponent can be written as $G = A_1 \cup A_2$ with $A_1$ and $A_2$
disjoint, so that for every infinite subgroup $H$ of $G$ and every $g \in G$, the coset $gH$ is
contained neither in $A_1$ nor in $A_2$. The problem is due to I. V. Protasov.

Formalized by `MathlibExt.GroupTheory.OddExponentCosetFreePartitionKourovka13Problem46Wanted.oddExponentCosetFreePartition`, a definition declared in [WantedExt/GroupTheory/OddExponentCosetFreePartitionKourovka13Problem46Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OddExponentCosetFreePartitionKourovka13Problem46Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/coset-free-partitions-of-groups/index.html#odd-exponent-coset-free-partition).

## Uncountable abelian groups of odd exponent have coset-free partitions

Every uncountable
abelian group $G$ of finite odd exponent can be written as $G = A_1 \cup A_2$ with $A_1$ and $A_2$
disjoint, so that for every infinite subgroup $H$ of $G$ and every $g \in G$, the coset $gH$ is
contained neither in $A_1$ nor in $A_2$. This answers Kourovka Problem 13.46 in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.46 (I. V. Protasov); resolution: E. G. Zelenyuk, Math. Notes 67 (2000), 599-602, Kourovka Archive, Problem 13.46 (answer: Yes, it can).

Stated but not proved: `MathlibExt.GroupTheory.OddExponentCosetFreePartitionKourovka13Problem46Wanted.oddExponentCosetFreePartition_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OddExponentCosetFreePartitionKourovka13Problem46Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/OddExponentCosetFreePartitionKourovka13Problem46Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/coset-free-partitions-of-groups/index.html#odd-exponent-coset-free-partition-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coset-free partitions of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/coset-free-partitions-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups/coset-free-partitions-of-groups)
