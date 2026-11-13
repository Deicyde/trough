---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.derivedSubgroupIsFrattini, MathlibExt.GroupTheory.DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.derivedSubgroupIsFrattini_refuted
statement: formalized
---

# Derived and Frattini subgroups of p-groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/derived-and-frattini-subgroups-of-p-groups/index.html).

## Derived subgroups of p-groups as Frattini subgroups (Kourovka 16.11)

The conjecture of
Ya. G. Berkovich that for every prime $p$ and every finite $p$-group $G$ there is a finite
$p$-group $H$ whose Frattini subgroup $\Phi(H)$, the intersection of the maximal subgroups of $H$,
is isomorphic to the derived subgroup $[G, G]$ of $G$.

Formalized by `MathlibExt.GroupTheory.DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.derivedSubgroupIsFrattini`, a definition declared in [WantedExt/GroupTheory/DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/derived-and-frattini-subgroups-of-p-groups/index.html#derived-subgroup-is-frattini).

## Derived subgroups of p-groups need not be Frattini subgroups of p-groups

There exist a prime
$p$ and a finite $p$-group $G$ such that for every finite $p$-group $H$, the Frattini subgroup
$\Phi(H)$ of $H$ is not isomorphic to the derived subgroup $[G, G]$ of $G$. That is, the conjecture
of Kourovka Problem 16.11 is false.

Ionin and Semidetnov take $p = 2$ and $G$ the group SmallGroup(256, 511), whose derived subgroup
is the Hall-Senior group 32/40 (a GAP computation); by a theorem of van der Waall and de Nijs, that
group is not isomorphic to the Frattini subgroup of any finite 2-group. The authors state that
their solutions were found with the assistance of large language models and checked by them.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.11 (Ya. G. Berkovich); resolution: V. Ionin and A. Semidetnov, On some more problems from the Kourovka Notebook, preprint, arXiv:2608.29219 (2026), Answer 3.2 with Lemma 3.4 and Theorem 3.3 (van der Waall-de Nijs, Theorem 1.15): for p = 2, G = SmallGroup(256, 511) has derived subgroup the Hall-Senior group 32/40, which is the Frattini subgroup of no finite 2-group; the Kourovka Notebook (21st issue) marks 16.11 solved (No, not always), https://arxiv.org/abs/2608.29219.

Stated but not proved: `MathlibExt.GroupTheory.DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.derivedSubgroupIsFrattini_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/DerivedSubgroupAsFrattiniKourovka16Problem11Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/derived-and-frattini-subgroups-of-p-groups/index.html#derived-subgroup-is-frattini-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Derived and Frattini subgroups of p-groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/derived-and-frattini-subgroups-of-p-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/finite-p-groups/derived-and-frattini-subgroups-of-p-groups)
