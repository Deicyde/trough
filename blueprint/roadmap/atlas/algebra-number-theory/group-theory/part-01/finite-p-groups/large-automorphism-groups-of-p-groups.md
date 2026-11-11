---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.cyclicSubgroupOfIndexFromLargeAutomorphism, MathlibExt.GroupTheory.LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.cyclicSubgroupOfIndexFromLargeAutomorphism_holds
statement: formalized
---

# Large automorphism groups of p-groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/large-automorphism-groups-of-p-groups/index.html).

## Kourovka Problem 15.32: large automorphisms and cyclic subgroups

For every prime $p$ and
all natural numbers $k$ and $m$ with $m \ge 64k + 2$, every finite group $G$ of order $p^m$ that
has an automorphism of order $p^{m-k}$ has a cyclic subgroup of index $p^k$.

Kourovka 15.32 (Ya. G. Berkovich) asks for some threshold $f(k)$ beyond which this holds; the
threshold $f(k) = 64k + 2$ is the one of its resolution.

Formalized by `MathlibExt.GroupTheory.LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.cyclicSubgroupOfIndexFromLargeAutomorphism`, a definition declared in [WantedExt/GroupTheory/LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/large-automorphism-groups-of-p-groups/index.html#cyclic-subgroup-of-index-from-large-auto).

## Large automorphisms of p-groups force cyclic subgroups of given index

For every prime $p$ and
all natural numbers $k$ and $m$ with $m \ge 64k + 2$, if a finite group $G$ of order $p^m$ has an
automorphism of order $p^{m-k}$, then $G$ has a cyclic subgroup of index $p^k$.

Resolved true: Jayadevan proved this with the threshold $f(k) = 64k + 2$; the Kourovka Notebook
(21st issue) marks 15.32 solved, "Yes, one can take $f(k) = 64k + 2$" (AI solution confirmed by
A. Caranti).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 15.32 (Ya. G. Berkovich); resolution: A. Jayadevan, Large-order automorphisms of finite p-groups force cyclic subgroups of prescribed index, preprint, Zenodo record 22910914 (2026), AI-generated solution confirmed by A. Caranti, main theorem (for every k ≥ 0, a group of order p^m with m ≥ 64k + 2 and an automorphism of order p^(m-k) has a cyclic subgroup of index exactly p^k); the Kourovka Notebook (21st issue) marks 15.32 solved, https://zenodo.org/records/22910914.

Stated but not proved: `MathlibExt.GroupTheory.LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.cyclicSubgroupOfIndexFromLargeAutomorphism_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LargeAutomorphismCyclicSubgroupKourovka15Problem32Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/large-automorphism-groups-of-p-groups/index.html#cyclic-subgroup-of-index-from-large-auto-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large automorphism groups of p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/large-automorphism-groups-of-p-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/finite-p-groups/large-automorphism-groups-of-p-groups)
