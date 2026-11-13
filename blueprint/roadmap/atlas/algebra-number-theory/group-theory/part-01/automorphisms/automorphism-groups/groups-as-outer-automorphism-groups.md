---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.everyFiniteGroupIsOuterAutomorphismGroup, MathlibExt.GroupTheory.OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.everyFiniteGroupIsOuterAutomorphismGroup_holds, MathlibExt.GroupTheory.OuterAutomorphismMetabelianKourovka11Problem26Wanted.OutIsoTo, MathlibExt.GroupTheory.OuterAutomorphismMetabelianKourovka11Problem26Wanted.groupNotOuterAutOfMetabelian, MathlibExt.GroupTheory.OuterAutomorphismMetabelianKourovka11Problem26Wanted.groupNotOuterAutOfMetabelian_refuted
statement: formalized
---

# Groups as outer automorphism groups

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups/index.html).

## Kourovka Problem 16.59 (finite groups as outer automorphism groups)

The statement that
for every finite group $K$ there are a finite group $G$ and a surjective homomorphism
$\mathrm{Aut}(G) \to K$ whose kernel is the group $\mathrm{Inn}(G)$ of inner automorphisms of
$G$, that is, $K$ is isomorphic to $\mathrm{Out}(G) = \mathrm{Aut}(G) / \mathrm{Inn}(G)$.

Formalized by `MathlibExt.GroupTheory.OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.everyFiniteGroupIsOuterAutomorphismGroup`, a definition declared in [WantedExt/GroupTheory/OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups/index.html#every-finite-group-is-outer-automorphism).

## Every finite group is the outer automorphism group of a finite group

For every finite group
$K$ there are a finite group $G$ and a surjective homomorphism $\mathrm{Aut}(G) \to K$ whose
kernel is the group $\mathrm{Inn}(G)$ of inner automorphisms of $G$; equivalently,
$\mathrm{Out}(G) = \mathrm{Aut}(G) / \mathrm{Inn}(G)$ is isomorphic to $K$. That is, the answer
to Kourovka Problem 16.59 is positive.

The Kourovka Archive records the answer "Yes, it does", citing Cornulier's MathOverflow answer.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.59 (D. MacHale); resolution: Y. Cornulier, answer to MathOverflow question 372480 (Is every finite group the outer automorphism group of a finite group?), 2020, Kourovka Archive, Problem 16.59 (Yes, it does), https://mathoverflow.net/questions/372480/is-every-finite-group-the-outer-automorphism-group-of-a-finite-group/372563.

Stated but not proved: `MathlibExt.GroupTheory.OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.everyFiniteGroupIsOuterAutomorphismGroup_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OuterAutomorphismGroupRealizationKourovka16Problem59Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups/index.html#every-finite-group-is-outer-automorphism-2).

## Outer automorphism group isomorphic to a given group

For groups $M$ and $G$, the
statement that $\operatorname{Out}(M) \cong G$, expressed without forming the quotient: there is a
surjective homomorphism $\operatorname{Aut}(M) \to G$ whose kernel is exactly the inner
automorphism group $\operatorname{Inn}(M)$, the image of the conjugation map
$M \to \operatorname{Aut}(M)$.

Formalized by `MathlibExt.GroupTheory.OuterAutomorphismMetabelianKourovka11Problem26Wanted.OutIsoTo`, a definition declared in [WantedExt/GroupTheory/OuterAutomorphismMetabelianKourovka11Problem26Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OuterAutomorphismMetabelianKourovka11Problem26Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups/index.html#out-iso-to).

## A group that is not an outer automorphism group of a centreless metabelian group

The
statement (Kourovka Problem 11.26, Göbel) that there is a group $G$ such that for every metabelian
group $M$ (one whose second derived subgroup $M''$ is trivial) with trivial centre, the outer
automorphism group $\operatorname{Out}(M)$ is not isomorphic to $G$.

Formalized by `MathlibExt.GroupTheory.OuterAutomorphismMetabelianKourovka11Problem26Wanted.groupNotOuterAutOfMetabelian`, a definition declared in [WantedExt/GroupTheory/OuterAutomorphismMetabelianKourovka11Problem26Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OuterAutomorphismMetabelianKourovka11Problem26Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups/index.html#group-not-outer-aut-of-metabelian).

## Every group is the outer automorphism group of a centreless metabelian group

For every group
$G$ there is a metabelian group $M$ (one whose second derived subgroup $M''$ is trivial) with
trivial centre such that the outer automorphism group
$\operatorname{Out}(M) = \operatorname{Aut}(M)/\operatorname{Inn}(M)$ is isomorphic to $G$. This
answers Kourovka Problem 11.26 (Göbel) in the negative (Göbel and Paras).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.26 (R. Göbel); resolution: R. Göbel and A. Paras, J. Pure Appl. Algebra 149, no. 3 (2000), 251-266, Kourovka Archive, Problem 11.26: "No, given any group `G` there is a metabelian group `M` with trivial center such that `Out M ≅ G`", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.OuterAutomorphismMetabelianKourovka11Problem26Wanted.groupNotOuterAutOfMetabelian_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/OuterAutomorphismMetabelianKourovka11Problem26Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OuterAutomorphismMetabelianKourovka11Problem26Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups/index.html#group-not-outer-aut-of-metabelian-refute).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups as outer automorphism groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/groups-as-outer-automorphism-groups)
