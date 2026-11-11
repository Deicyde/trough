---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.closedSubdegreeFiniteDistinguishingSet, MathlibExt.GroupTheory.SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.closedSubdegreeFiniteDistinguishingSet_holds
statement: formalized
---

# Distinguishing sets of subdegree-finite groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/distinguishing-sets-of-subdegree-finite-groups/index.html).

## Kourovka Problem 19.89: Smith's conjecture on distinguishing sets

The statement that for
every countably infinite set $\Omega$ and every subgroup $G$ of the symmetric group
$\mathrm{Sym}(\Omega)$ that is closed in the topology of pointwise convergence and
subdegree-finite (for all $a, b \in \Omega$ the orbit of $b$ under the stabilizer of $a$ in $G$ is
finite), if every non-identity element of $G$ moves infinitely many points of $\Omega$, then there
is a subset $X \subseteq \Omega$ whose setwise stabilizer in $G$ is trivial: the only $g \in G$
with $g(X) = X$ is the identity.

Formalized by `MathlibExt.GroupTheory.SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.closedSubdegreeFiniteDistinguishingSet`, a definition declared in [WantedExt/GroupTheory/SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/distinguishing-sets-of-subdegree-finite-groups/index.html#closed-subdegree-finite-distinguishing-s).

## Lehner's theorem on distinguishing sets of subdegree-finite groups

Let $\Omega$ be a
countably infinite set and let $G$ be a subgroup of the symmetric group $\mathrm{Sym}(\Omega)$
that is closed in the topology of pointwise convergence and subdegree-finite: for all
$a, b \in \Omega$ the orbit of $b$ under the stabilizer of $a$ in $G$ is finite. If every
non-identity element of $G$ moves infinitely many points of $\Omega$, then there is a subset
$X \subseteq \Omega$ whose setwise stabilizer in $G$ is trivial: the only $g \in G$ with
$g(X) = X$ is the identity.

Lehner proves more generally that every locally compact permutation group on a countable set in
which every non-identity element moves infinitely many points has a subset with trivial setwise
stabilizer; closed subdegree-finite permutation groups are locally compact.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.89 (S. M. Smith); resolution: F. Lehner, Asymmetric colouring of locally compact permutation groups, Bull. London Math. Soc. 55 (2023), 1874-1879 (arXiv:2208.08844), Theorem 2: a locally compact permutation group on a countable set with infinite motion (minimal degree) has an asymmetric 2-colouring, a subset with trivial setwise stabiliser; Section 2: every closed, subdegree-finite permutation group is locally compact; the Kourovka Notebook (21st issue) marks 19.89 solved: the conjecture is proved, https://arxiv.org/abs/2208.08844.

Stated but not proved: `MathlibExt.GroupTheory.SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.closedSubdegreeFiniteDistinguishingSet_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SubdegreeFiniteDistinguishingSetKourovka19Problem89Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/distinguishing-sets-of-subdegree-finite-groups/index.html#closed-subdegree-finite-distinguishing-s-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distinguishing sets of subdegree-finite groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/distinguishing-sets-of-subdegree-finite-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/distinguishing-sets-of-subdegree-finite-groups)
