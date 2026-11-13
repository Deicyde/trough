---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.isomorphicSimpleMaximalSubgroupsAutConjugate, MathlibExt.GroupTheory.IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.isomorphicSimpleMaximalSubgroupsAutConjugate_refuted
statement: formalized
---

# Conjugacy of maximal subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/conjugacy-of-maximal-subgroups/index.html).

## Schmid's question on isomorphic simple maximal subgroups (Kourovka 18.115)

The statement
that in every finite simple group $G$, any two isomorphic maximal subgroups $X$ and $Y$ that are
themselves simple groups are conjugate in $\operatorname{Aut} G$, that is, $\varphi(X) = Y$ for
some automorphism $\varphi$ of $G$.

Formalized by `MathlibExt.GroupTheory.IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.isomorphicSimpleMaximalSubgroupsAutConjugate`, a definition declared in [WantedExt/GroupTheory/IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/conjugacy-of-maximal-subgroups/index.html#isomorphic-simple-maximal-subgroups-aut).

## Isomorphic simple maximal subgroups need not be conjugate under automorphisms

There are a
finite simple group $G$ and isomorphic maximal subgroups $X$ and $Y$ of $G$, both simple groups,
such that no automorphism $\varphi$ of $G$ satisfies $\varphi(X) = Y$. That is, the answer to
Kourovka Problem 18.115 is negative.

The Kourovka Archive answers 18.115 "No, not always": there are two $\operatorname{Aut} G$-classes
of $M_{12}$ in $E_6(5)$ (Kleidman–Wilson, 1990), and Craven (2023) found two classes of
$\mathrm{PSL}_2(11)$ and two of $\mathrm{PSL}_2(19)$ in $E_6(q)$ for certain $q$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.115 (P. Schmid); resolution: P. B. Kleidman and R. A. Wilson, J. London Math. Soc. (2) 42 (1990), 555-561; D. A. Craven, Invent. Math. 234 (2023), no. 2, 637-719, Kourovka Archive, Problem 18.115: No, not always; two Aut G-classes of M_12 in E_6(5) (Kleidman-Wilson), and two classes of PSL_2(11) and of PSL_2(19) in E_6(q) for certain q (Craven), https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.isomorphicSimpleMaximalSubgroupsAutConjugate_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IsomorphicSimpleMaximalSubgroupsKourovka18Problem115Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/conjugacy-of-maximal-subgroups/index.html#isomorphic-simple-maximal-subgroups-aut-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugacy of maximal subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/conjugacy-of-maximal-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/subgroup-embedding/conjugacy-of-maximal-subgroups)
