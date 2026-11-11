---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TwoLargestOrbitsDihedralKourovka18Problem44Wanted.twoLargestOrbitsImpliesDihedralEight, MathlibExt.GroupTheory.TwoLargestOrbitsDihedralKourovka18Problem44Wanted.twoLargestOrbitsImpliesDihedralEight_holds
statement: formalized
---

# Largest orbits of linear group actions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/largest-orbits-of-linear-group-actions/index.html).

## Keller's question on two largest orbits and the dihedral group of order eight (Kourovka Problem 18.44)

**Keller's question on two largest orbits and the dihedral group of order eight (Kourovka
Problem 18.44).** The statement that for every finite non-abelian group $G$, with derived subgroup
$G'$, and every finite faithful irreducible $G$-module $V$ (a nonzero finite abelian group on which
$G$ acts faithfully by automorphisms with no $G$-invariant subgroups other than $0$ and $V$),
writing $M = |G/G'|$: if every orbit of $G$ on $V$ has at most $M$ elements and exactly two orbits
have exactly $M$ elements, then $G$ is isomorphic to the dihedral group of order $8$ and
$|V| = 9$.

Formalized by `MathlibExt.GroupTheory.TwoLargestOrbitsDihedralKourovka18Problem44Wanted.twoLargestOrbitsImpliesDihedralEight`, a definition declared in [WantedExt/GroupTheory/TwoLargestOrbitsDihedralKourovka18Problem44Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwoLargestOrbitsDihedralKourovka18Problem44Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/largest-orbits-of-linear-group-actions/index.html#two-largest-orbits-implies-dihedral-eigh).

## Two largest orbits force the dihedral group of order eight (Kourovka 18.44)

Let $G$ be a
finite non-abelian group, let $G'$ be its derived subgroup, and let $V$ be a finite faithful
irreducible $G$-module, that is, a nonzero finite abelian group on which $G$ acts faithfully by
automorphisms with no $G$-invariant subgroups other than $0$ and $V$. Write $M = |G/G'|$. If every
orbit of $G$ on $V$ has at most $M$ elements and exactly two orbits have exactly $M$ elements, then
$G$ is isomorphic to the dihedral group of order $8$ and $|V| = 9$.

Jones and Keller (2020), Theorem 3.1, prove this, showing moreover that $V$ is the $2$-dimensional
vector space $V(2, 3)$ over the field with $3$ elements; the Kourovka Notebook (21st issue) accepts
it as answering 18.44.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.44 (T. M. Keller); resolution: N. A. Jones and T. M. Keller, Orbit sizes and the dihedral group of order eight, Ann. Mat. Pura Appl. 199 (2020), 2323-2340, Theorem 3.1: G finite nonabelian, V finite faithful irreducible G-module, M = |G/G'| the largest orbit size with exactly two orbits of size M; then G is dihedral of order 8 and V = V(2, 3), https://doi.org/10.1007/s10231-020-00970-x.

Stated but not proved: `MathlibExt.GroupTheory.TwoLargestOrbitsDihedralKourovka18Problem44Wanted.twoLargestOrbitsImpliesDihedralEight_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/TwoLargestOrbitsDihedralKourovka18Problem44Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TwoLargestOrbitsDihedralKourovka18Problem44Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/largest-orbits-of-linear-group-actions/index.html#two-largest-orbits-implies-dihedral-eigh-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Largest orbits of linear group actions](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/largest-orbits-of-linear-group-actions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/largest-orbits-of-linear-group-actions)
