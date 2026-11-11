---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.maximalSolubleSubgroupNormalizerSupplement, MathlibExt.GroupTheory.MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.maximalSolubleSubgroupNormalizerSupplement_holds
statement: formalized
---

# Maximal soluble subgroups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/maximal-soluble-subgroups/index.html).

## Kourovka 14.62: a maximal soluble subgroup whose normalizer supplements

The proposition
that for every finite group $G$ and every non-soluble normal subgroup $H$ of $G$ there is
a maximal soluble subgroup $S$ of $H$ (a soluble subgroup $S \le H$ contained in no strictly
larger soluble subgroup of $H$) such that $G = H\,N_G(S)$, where $N_G(S)$ is the normalizer of $S$
in $G$; since $H$ is normal, this says that $H$ and $N_G(S)$ generate $G$.

Formalized by `MathlibExt.GroupTheory.MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.maximalSolubleSubgroupNormalizerSupplement`, a definition declared in [WantedExt/GroupTheory/MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/maximal-soluble-subgroups/index.html#maximal-soluble-subgroup-normalizer-supp).

## Zenkov–Monakhov–Revin theorem (Kourovka 14.62)

For every finite group $G$ and every
non-soluble normal subgroup $H$ of $G$ there is a maximal soluble subgroup $S$ of $H$ (a soluble
subgroup $S \le H$ contained in no strictly larger soluble subgroup of $H$) such that
$G = H\,N_G(S)$, where $N_G(S)$ is the normalizer of $S$ in $G$; since $H$ is normal, this says
that $H$ and $N_G(S)$ generate $G$.

Zenkov, Monakhov and Revin proved this using the classification of finite simple groups, so the
Kourovka Archive answers 14.62 "Yes, it always exists".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.62 (V. S. Monakhov); resolution: V. I. Zenkov, V. S. Monakhov and D. O. Revin, Algebra and Logic 43 (2004), no. 2, 102-108 (using the classification of finite simple groups), Kourovka Archive, Problem 14.62 (answer: Yes, it always exists mod CFSG).

Stated but not proved: `MathlibExt.GroupTheory.MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.maximalSolubleSubgroupNormalizerSupplement_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/MaximalSolubleSubgroupNormalizerKourovka14Problem62Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/maximal-soluble-subgroups/index.html#maximal-soluble-subgroup-normalizer-supp-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximal soluble subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/subgroup-embedding/maximal-soluble-subgroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/subgroup-embedding/maximal-soluble-subgroups)
