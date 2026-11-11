---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.FreeSolubleGroupRankTwo, MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.IsTestElement, MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.freeSolubleRankTwoHasTestElement, MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.freeSolubleRankTwoHasTestElement_holds
statement: formalized
---

# Test elements

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/test-elements/index.html).

## Free soluble group of rank two

The free soluble group of rank `2` and derived length `d`: the quotient `F₂ / F₂⁽ᵈ⁾` of the free
group on two generators by the `d`-th term of its derived series.

Formalized by `MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.FreeSolubleGroupRankTwo`, an abbreviation declared in [WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/test-elements/index.html#free-soluble-group-rank-two).

## Test element

An element $u$ of a group $G$ is a test element of $G$ if every endomorphism
$\varphi$ of $G$ with $\varphi(u) = u$ is bijective, that is, an automorphism of $G$.

Formalized by `MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.IsTestElement`, a definition declared in [WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/test-elements/index.html#is-test-element).

## Kourovka Problem 14.88 (test elements of free soluble groups of rank 2)

The statement that
for every integer $d > 2$ the free soluble group $F_2 / F_2^{(d)}$ of rank $2$ and derived length
$d$ has a test element, where $F_2$ is the free group on two generators and $F_2^{(d)}$ is the
$d$-th term of its derived series.

Kourovka Notebook Problem 14.88 is due to B. Fine and V. Shpilrain.

Formalized by `MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.freeSolubleRankTwoHasTestElement`, a definition declared in [WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/test-elements/index.html#free-soluble-rank-two-has-test-element).

## Free soluble groups of rank two have test elements

Resolved true: the Kourovka Archive answers 14.88 "Yes, it does" (Timoshenko): for every `d > 2` the
free soluble group `F₂/F₂⁽ᵈ⁾` of rank `2` and derived length `d` has a test element. Source: E. I.
Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st
issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.88 (B. Fine, V. Shpilrain);
resolution: E. I. Timoshenko, Computing test rank for a free solvable group, Algebra and Logic 45
(2006), no. 4, 254-260, main result (the test rank of a non-abelian free solvable group of finite
rank is one less than its rank, so F₂/F₂⁽ᵈ⁾ has test elements for every d > 2), as recorded in V.
Shpilrain's list of open problems in combinatorial group theory, problem (S9); Kourovka Archive,
Problem 14.88 (answer: Yes, it does), https://shpilrain.ccny.cuny.edu/gworld/problems/Back2.html.

Stated but not proved: `MathlibExt.GroupTheory.FreeSolubleTestElementKourovka14Problem88Wanted.freeSolubleRankTwoHasTestElement_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeSolubleTestElementKourovka14Problem88Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/test-elements/index.html#free-soluble-rank-two-has-test-element-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Test elements](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/test-elements/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/test-elements)
