---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FiniteAbelianDualWanted.finite_abelian_dual_iso, MathlibExt.GroupTheory.FiniteAbelianDualWanted.dual_prod
statement: formalized
proof: formalized
---

# Dual groups of finite abelian groups

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/dual-groups-of-finite-abelian-groups/index.html).

## A finite abelian group is isomorphic to its dual group

Every finite abelian group $A$ is
isomorphic to its dual group, the group of characters of $A$ under pointwise multiplication,
where a character of $A$ is a map $\chi : A \to \mathbb{C}$ with $\chi(0) = 1$ and
$\chi(a + a') = \chi(a)\chi(a')$ for all $a, a' \in A$.

Proof: Use the structure theorem to write $A$ as a direct sum of finite cyclic groups,
identify each cyclic group $\mathbb{Z}/n\mathbb{Z}$ with its dual group, and transport
characters along the decomposition. This is the proof of Conrad's Theorem 3.13: the cyclic
case, then products of cyclic groups.

## Sources

- K. Conrad, Characters of finite abelian groups, https://kconrad.math.uconn.edu/blurbs/grouptheory/charthy.pdf, Theorem 3.13.

Formalized by `MathlibExt.GroupTheory.FiniteAbelianDualWanted.finite_abelian_dual_iso`, a theorem declared in [MathlibExt/GroupTheory/FiniteAbelianDual.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/FiniteAbelianDual.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/dual-groups-of-finite-abelian-groups/index.html#finite-abelian-dual-iso).

## Characters of a product of abelian groups

For all abelian groups $A$ and $B$, the group of
characters of $A \times B$ is isomorphic to the product of the character groups of $A$ and $B$.
Here a character of $A$ is a map $\chi : A \to \mathbb{C}$ with $\chi(0) = 1$ and
$\chi(a + a') = \chi(a)\chi(a')$ for all $a, a' \in A$, and the characters of $A$ form a group
under pointwise multiplication.

Proof: Restrict a character along the two coordinate inclusions, with inverse
$(\chi_1, \chi_2) \mapsto ((x, y) \mapsto \chi_1(x)\chi_2(y))$. Conrad's Lemma 3.12 uses the
same restriction map for finite groups and concludes by counting; the explicit
inverse removes the finiteness assumption.

## Sources

- K. Conrad, Characters of finite abelian groups, https://kconrad.math.uconn.edu/blurbs/grouptheory/charthy.pdf, Lemma 3.12.

Formalized by `MathlibExt.GroupTheory.FiniteAbelianDualWanted.dual_prod`, a theorem declared in [MathlibExt/GroupTheory/FiniteAbelianDual.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/FiniteAbelianDual.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/dual-groups-of-finite-abelian-groups/index.html#dual-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dual groups of finite abelian groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/abelian-groups/dual-groups-of-finite-abelian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/abelian-groups/dual-groups-of-finite-abelian-groups)
