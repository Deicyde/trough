---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.IsIntegrableGroupTable, MathlibExt.GroupTheory.IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.integrabilityDecidable, MathlibExt.GroupTheory.IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.integrabilityDecidable_holds
statement: formalized
---

# Integrable groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/integrable-groups/index.html).

## Integrable group tables

A finite list $t = (t_0, \dots, t_{n-1})$ of finite lists of
natural numbers is an integrable group table when there is a group structure on
$\{0, \dots, n-1\}$ such that, for all $i, j < n$, the product of $i$ and $j$ is the entry of $t_i$
at index $j$, counting from $0$ (an entry missing from a short row is read as $0$), and some finite
group $H$ has derived subgroup $[H, H]$ isomorphic to this group. Lists that are not the
multiplication table of a group on $\{0, \dots, n-1\}$ do not satisfy the predicate.

Formalized by `MathlibExt.GroupTheory.IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.IsIntegrableGroupTable`, a definition declared in [WantedExt/GroupTheory/IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/integrable-groups/index.html#is-integrable-group-table).

## Kourovka Problem 21.32 (decidability of integrability)

The statement that integrable group
tables form a decidable set: some computable function decides, for every finite list
$t = (t_0, \dots, t_{n-1})$ of finite lists of natural numbers, whether $t$ is an integrable group
table, that is, whether there is a group structure on $\{0, \dots, n-1\}$ in which, for all
$i, j < n$, the product of $i$ and $j$ is the entry of $t_i$ at index $j$, counting from $0$ (an
entry missing from a short row is read as $0$), and which is isomorphic to the derived subgroup of
some finite group.

Formalized by `MathlibExt.GroupTheory.IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.integrabilityDecidable`, a definition declared in [WantedExt/GroupTheory/IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/integrable-groups/index.html#integrability-decidable).

## Integrability of finite groups is decidable

Integrable group tables form a decidable set: some
computable function decides, for every finite list $t = (t_0, \dots, t_{n-1})$ of finite lists of
natural numbers, whether there is a group structure on $\{0, \dots, n-1\}$ in which, for all
$i, j < n$, the product of $i$ and $j$ is the entry of $t_i$ at index $j$, counting from $0$ (an
entry missing from a short row is read as $0$), and which is isomorphic to the derived subgroup of
some finite group. That is, the decidability part of Kourovka Problem 21.32 has a positive answer.

Kalithasan and Thomas bound the order of some integral of an integrable finite group $G$ (their
Theorem 3.3 and its Corollary), which makes the problem decidable; the 21st issue of the Kourovka
Notebook marks 21.32 solved ("Yes, it is decidable, in nondeterministic quasi-polynomial time").
The complexity bound is not part of this statement.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 21.32 (P. J. Cameron); resolution: S. Kalithasan and V. Z. Thomas, On the decidability of the integrability of finite groups, preprint, arXiv:2602.18829 (2026), Theorem 3.3 (an integrable finite group G has an integral, a group with derived subgroup ≅ G, of order bounded in terms of |Aut(G)|, |Z(G)|, μ(G) and d(Z(G))) and its Corollary: integrability of a finite group is decidable; Kourovka Notebook (21st issue), Problem 21.32: Yes, it is decidable, in nondeterministic quasi-polynomial time, https://arxiv.org/abs/2602.18829.

Stated but not proved: `MathlibExt.GroupTheory.IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.integrabilityDecidable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/IntegrableFiniteGroupDecidableKourovka21Problem32Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/integrable-groups/index.html#integrability-decidable-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integrable groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/integrable-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/extensions-and-cohomology/integrable-groups)
