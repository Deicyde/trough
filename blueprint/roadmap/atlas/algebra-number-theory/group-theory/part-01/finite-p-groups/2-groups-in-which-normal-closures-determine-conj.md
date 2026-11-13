---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.normalClosureConjDerivedAbelian, MathlibExt.GroupTheory.TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.normalClosureConjDerivedAbelian_refuted
statement: formalized
---

# 2-groups in which normal closures determine conjugacy

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/2-groups-in-which-normal-closures-determine-conj/index.html).

## Golikova–Starostin question on finite $2$-groups in which normal closures determine conjugacy (Kourovka 12.15)

**Golikova–Starostin question on finite $2$-groups in which normal closures determine
conjugacy (Kourovka 12.15).** The statement that for every finite $2$-group $G$ in which any two
elements with the same normal closure are conjugate, the derived subgroup $G'$ of $G$ is
abelian.

Formalized by `MathlibExt.GroupTheory.TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.normalClosureConjDerivedAbelian`, a definition declared in [WantedExt/GroupTheory/TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/2-groups-in-which-normal-closures-determine-conj/index.html#normal-closure-conj-derived-abelian).

## Equal normal closures forcing conjugacy does not make the derived subgroup of a finite $2$-group abelian (Kourovka 12.15)

**Equal normal closures forcing conjugacy does not make the derived subgroup of a finite $2$-group
abelian (Kourovka 12.15).** There exists a finite $2$-group $G$ in which any two elements with the
same normal closure are conjugate, but whose derived subgroup $G'$ is not abelian.

Muliarchyk gives an explicit such group of order $2^{11} = 2048$, given by a power-commutator
presentation, whose second derived subgroup $G'' = (G')'$ is nontrivial (a ChatGPT-assisted
construction with a symbolic proof); the Kourovka Notebook (21st issue) marks 12.15 solved, "No,
not always".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 12.15 (E. A. Golikova, A. I. Starostin); resolution: K. Muliarchyk, An explicit counterexample to Kourovka Notebook Problem 12.15, preprint (13 August 2026), main result: an explicit group of order `2¹¹ = 2048`, given by a power-commutator presentation, satisfies the hypothesis and has `G'' = ⟨z⟩ ≠ 1`; the Kourovka Notebook (21st issue) marks 12.15 solved, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/08/kourovka_12_15_counterexample.pdf.

Stated but not proved: `MathlibExt.GroupTheory.TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.normalClosureConjDerivedAbelian_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/TwoGroupNormalClosureConjugateKourovka12Problem15Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/2-groups-in-which-normal-closures-determine-conj/index.html#normal-closure-conj-derived-abelian-refu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: 2-groups in which normal closures determine conjugacy](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/finite-p-groups/2-groups-in-which-normal-closures-determine-conj/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/finite-p-groups/2-groups-in-which-normal-closures-determine-conj)
