---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MaximalSubgroupsSpecialKourovka16Problem13Wanted.IsSpecialGroup, MathlibExt.GroupTheory.MaximalSubgroupsSpecialKourovka16Problem13Wanted.largePGroupsWithSpecialMaximalSubgroups, MathlibExt.GroupTheory.MaximalSubgroupsSpecialKourovka16Problem13Wanted.largePGroupsWithSpecialMaximalSubgroups_holds
statement: formalized
---

# p-groups with special maximal subgroups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/p-groups-with-special-maximal-subgroups/index.html).

## Special group

A group $H$ is special when its center, its commutator subgroup and its
Frattini subgroup coincide: $Z(H) = [H, H] = \Phi(H)$.

Formalized by `MathlibExt.GroupTheory.MaximalSubgroupsSpecialKourovka16Problem13Wanted.IsSpecialGroup`, a definition declared in [WantedExt/GroupTheory/MaximalSubgroupsSpecialKourovka16Problem13Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MaximalSubgroupsSpecialKourovka16Problem13Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/p-groups-with-special-maximal-subgroups/index.html#is-special-group).

## Kourovka Problem 16.13, strong form (statement)

The statement that for every prime $p$
and every natural number $n$ there is a finite $p$-group $G$ of order greater than $n$ all of whose
maximal subgroups $H$ are special, that is, have center $Z(H)$, commutator subgroup $[H, H]$ and
Frattini subgroup $\Phi(H)$ all equal. This is the form in which the problem was resolved; the
problem as posed asks only for one finite $p$-group all of whose maximal subgroups are special.

Formalized by `MathlibExt.GroupTheory.MaximalSubgroupsSpecialKourovka16Problem13Wanted.largePGroupsWithSpecialMaximalSubgroups`, a definition declared in [WantedExt/GroupTheory/MaximalSubgroupsSpecialKourovka16Problem13Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MaximalSubgroupsSpecialKourovka16Problem13Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/p-groups-with-special-maximal-subgroups/index.html#large-pgroups-with-special-maximal-subgr).

## Arbitrarily large $p$-groups all of whose maximal subgroups are special

For every prime $p$
and every natural number $n$ there is a finite $p$-group $G$ of order greater than $n$ such that
every maximal subgroup $H$ of $G$ is special, that is, its center $Z(H)$, its commutator subgroup
$[H, H]$ and its Frattini subgroup $\Phi(H)$ coincide. This answers Kourovka Problem 16.13
positively.

The Kourovka Archive records this answer, citing Cossey (2014); for $p = 2$ a Sylow $2$-subgroup of
$L_3(4)$ is another example (Zenkov).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.13 (Ya. G. Berkovich); resolution: J. Cossey, Bull. Austral. Math. Soc. 89 (2014), 415-419, Kourovka Archive, Problem 16.13 (for all primes, groups of arbitrarily large size; for p = 2 also a Sylow 2-subgroup of L_3(4), V. I. Zenkov, 2014).

Stated but not proved: `MathlibExt.GroupTheory.MaximalSubgroupsSpecialKourovka16Problem13Wanted.largePGroupsWithSpecialMaximalSubgroups_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/MaximalSubgroupsSpecialKourovka16Problem13Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MaximalSubgroupsSpecialKourovka16Problem13Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/p-groups-with-special-maximal-subgroups/index.html#large-pgroups-with-special-maximal-subgr-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: p-groups with special maximal subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/p-groups-with-special-maximal-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/finite-p-groups/p-groups-with-special-maximal-subgroups)
