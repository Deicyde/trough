---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.threeMaximalSubgroupsFinite, MathlibExt.GroupTheory.ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.threeMaximalSubgroupsFinite_refuted
statement: formalized
---

# Groups with few maximal subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-few-maximal-subgroups/index.html).

## Bergman's question for three maximal subgroups

Kourovka 17.17 (G. M. Bergman) asks
whether a finitely generated group with only finitely many maximal subgroups must be finite. This
is the case of three maximal subgroups, which the problem singles out: every finitely generated
group with exactly three maximal subgroups is finite.

Formalized by `MathlibExt.GroupTheory.ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.threeMaximalSubgroupsFinite`, a definition declared in [WantedExt/GroupTheory/ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-few-maximal-subgroups/index.html#three-maximal-subgroups-finite).

## Not every finitely generated group with three maximal subgroups is finite

There is a
finitely generated infinite group with exactly three maximal subgroups; that is, it is false that
every finitely generated group with exactly three maximal subgroups is finite.

This answers Kourovka Problem 17.17 (G. M. Bergman) in the negative: the Kourovka Archive cites a
2-generated group constructed in Section 7 of Ershov and Jaikin-Zapirain (2013), which is infinite
and has exactly three maximal subgroups, each of index 2.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 17.17 (G. M. Bergman); resolution: M. Ershov and A. Jaikin-Zapirain, J. Reine Angew. Math. 677 (2013), 71-134, Kourovka Archive, Problem 17.17 (No, it need not: a 2-generated 2-LERF group in Section 7 of Ershov-Jaikin-Zapirain is an infinite group with 3 maximal subgroups, all of index 2).

Stated but not proved: `MathlibExt.GroupTheory.ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.threeMaximalSubgroupsFinite_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ThreeMaximalSubgroupsInfiniteKourovka17Problem17Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-few-maximal-subgroups/index.html#three-maximal-subgroups-finite-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Groups with few maximal subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/groups-with-few-maximal-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/subgroup-embedding/groups-with-few-maximal-subgroups)
