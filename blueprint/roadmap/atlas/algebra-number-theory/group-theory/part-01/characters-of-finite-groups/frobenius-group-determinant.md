---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FrobeniusDeterminantWanted.RepresentationTheory.FrobeniusDeterminant.groupMatrix, MathlibExt.GroupTheory.FrobeniusDeterminantWanted.RepresentationTheory.FrobeniusDeterminant.groupDeterminant, MathlibExt.GroupTheory.FrobeniusDeterminantWanted.RepresentationTheory.FrobeniusDeterminant.frobenius_group_determinant
statement: formalized
---

# Frobenius group determinant

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/frobenius-group-determinant/index.html).

## Group matrix

For a finite group $G$, the group matrix of Dedekind and Frobenius is the
$G \times G$ matrix over the polynomial ring $\mathbb{C}[x_g : g \in G]$ whose entry at $(g, h)$ is
the variable $x_{gh}$.

Formalized by `MathlibExt.GroupTheory.FrobeniusDeterminantWanted.RepresentationTheory.FrobeniusDeterminant.groupMatrix`, a definition declared in [WantedExt/GroupTheory/FrobeniusDeterminantWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrobeniusDeterminantWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/frobenius-group-determinant/index.html#group-matrix).

## Group determinant

For a finite group $G$, the group determinant $\Theta(G)$ is the
determinant of the group matrix of $G$, the $G \times G$ matrix over $\mathbb{C}[x_g : g \in G]$
whose entry at $(g, h)$ is the variable $x_{gh}$; it is a polynomial in these variables.

Formalized by `MathlibExt.GroupTheory.FrobeniusDeterminantWanted.RepresentationTheory.FrobeniusDeterminant.groupDeterminant`, a definition declared in [WantedExt/GroupTheory/FrobeniusDeterminantWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrobeniusDeterminantWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/frobenius-group-determinant/index.html#group-determinant).

## Frobenius determinant theorem

Let $G$ be a finite group and let $r$ be the number of
conjugacy classes of $G$. Then there exist polynomials $p_1, \dots, p_r$ in
$\mathbb{C}[x_g : g \in G]$ such that each $p_j$ is irreducible, $p_i$ and $p_j$ are not associated
for $i \neq j$, and the group determinant of $G$ equals $\prod_{j=1}^{r} p_j^{\deg p_j}$, where
$\deg p_j$ is the total degree of $p_j$.

## Sources

- Knill, *Some fundamental theorems in mathematics*, §171. Problem `frobenius_group_determinant` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.FrobeniusDeterminantWanted.RepresentationTheory.FrobeniusDeterminant.frobenius_group_determinant` is written with `theorem_wanted` in [WantedExt/GroupTheory/FrobeniusDeterminantWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FrobeniusDeterminantWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/frobenius-group-determinant/index.html#frobenius-group-determinant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frobenius group determinant](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/frobenius-group-determinant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/characters-of-finite-groups/frobenius-group-determinant)
