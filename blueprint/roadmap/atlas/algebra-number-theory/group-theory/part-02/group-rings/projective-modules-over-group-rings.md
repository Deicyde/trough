---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.IsPolycyclic, MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.IsAlmostPolycyclic, MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.projectiveWithTwoIndependentFree, MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.projectiveWithTwoIndependentFree_refuted
statement: formalized
---

# Projective modules over group rings

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/projective-modules-over-group-rings/index.html).

## Polycyclic group

A group $G$ is polycyclic if for some $n \ge 0$ there are subgroups
$1 = H_0 \le H_1 \le \cdots \le H_n = G$ such that for each $i < n$, $H_i$ is normal in
$H_{i+1}$ and the quotient $H_{i+1} / H_i$ is cyclic.

Formalized by `MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.IsPolycyclic`, a definition declared in [WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/projective-modules-over-group-rings/index.html#is-polycyclic).

## Almost polycyclic group

A group $G$ is almost polycyclic (polycyclic-by-finite) if it
has a subgroup of finite index that is polycyclic.

Formalized by `MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.IsAlmostPolycyclic`, a definition declared in [WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/projective-modules-over-group-rings/index.html#is-almost-polycyclic).

## Artamonov's freeness question (Kourovka 11.5)

This is the proposition that, for every
commutative ring $k$, every torsion-free almost polycyclic group $G$ (no element $g \ne 1$ of $G$
has finite order) and every finitely generated projective module $P$ over the group ring $kG$, if
$P$ contains two elements that are linearly independent over $kG$, then $P$ is a free
$kG$-module.

Formalized by `MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.projectiveWithTwoIndependentFree`, a definition declared in [WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/projective-modules-over-group-rings/index.html#projective-with-two-independent-free).

## Artamonov's freeness question has a negative answer

It is not the case that for every
commutative ring $k$, every torsion-free almost polycyclic group $G$ (no element $g \ne 1$ of $G$
has finite order) and every finitely generated projective module $P$ over the group ring $kG$
containing two elements that are linearly independent over $kG$, the module $P$ is free over $kG$.

Jayadevan's counterexample takes $k = \mathbb{F}_2 \times \mathbb{F}_2$ and the trivial group $G$,
so that $kG = k$; then $P = k^2 \oplus (\mathbb{F}_2 \times 0)$ is a finitely generated projective
$k$-module containing an independent pair, but $|P| = 32$ is not a power of $4 = |k|$, so $P$ is
not free. The Kourovka Notebook (21st issue) marks 11.5 solved, "No, not always" (AI solution
confirmed by D. Segal); the example gives nothing for field coefficients.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 11.5 (V. A. Artamonov); resolution: A. Jayadevan, A coefficient-ring obstruction to freeness of projective group-ring modules, preprint, Zenodo record 22846603 (2026), main example: `k = 𝔽₂ × 𝔽₂`, `G = 1`, `P = k² ⊕ (𝔽₂ × 0)` is projective with an independent pair but has 32 elements, while finite free `k`-modules have `4ⁿ`; the Kourovka Notebook (21st issue) marks 11.5 solved (AI solution confirmed by D. Segal), https://zenodo.org/records/22846603.

Stated but not proved: `MathlibExt.GroupTheory.ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.projectiveWithTwoIndependentFree_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ProjectiveGroupRingModuleFreeKourovka11Problem5Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/projective-modules-over-group-rings/index.html#projective-with-two-independent-free-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Projective modules over group rings](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/projective-modules-over-group-rings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/group-rings/projective-modules-over-group-rings)
