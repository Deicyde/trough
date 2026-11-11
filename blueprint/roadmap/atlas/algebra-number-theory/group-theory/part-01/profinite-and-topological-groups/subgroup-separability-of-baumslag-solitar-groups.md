---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.BS1, MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.IsSeparableSubgroup, MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.IsLocallySubgroupSeparable, MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.solvableLERFIffNoBaumslagSolitar, MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.solvableLERFIffNoBaumslagSolitar_refuted
statement: formalized
---

# Subgroup separability of Baumslag–Solitar groups

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups/index.html).

## The Baumslag–Solitar group BS(1, n)

For a natural number $n$, $\mathrm{BS}(1, n)$ is the
group with presentation $\langle a, b \mid b a b^{-1} = a^n \rangle$.

Formalized by `MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.BS1`, an abbreviation declared in [WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups/index.html#bs1).

## Separable subgroup

A subgroup $H$ of a group $G$ is separable when for every element
$x \in G$ with $x \notin H$ there are a finite group $F$ and a group homomorphism
$f \colon G \to F$ with $f(x) \notin f(H)$.

Formalized by `MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.IsSeparableSubgroup`, a definition declared in [WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups/index.html#is-separable-subgroup).

## Locally subgroup-separable (LERF) group

A group $G$ is locally subgroup-separable, or
LERF, when every finitely generated subgroup of $G$ is separable.

Formalized by `MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.IsLocallySubgroupSeparable`, a definition declared in [WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups/index.html#is-locally-subgroup-separable).

## Kourovka Problem 16.2 (R. C. Alperin)

A finitely generated solvable group $G$ is locally
subgroup-separable if and only if there is no $n > 1$ such that $G$ has a subgroup isomorphic to
the Baumslag–Solitar group $\mathrm{BS}(1, n)$.

Formalized by `MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.solvableLERFIffNoBaumslagSolitar`, a definition declared in [WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups/index.html#solvable-lerfiff-no-baumslag-solitar).

## Kourovka Problem 16.2 has a negative answer

There is a finitely generated solvable group $G$
for which the following two conditions are not equivalent: $G$ is locally subgroup-separable;
there is no $n > 1$ such that $G$ has a subgroup isomorphic to the Baumslag–Solitar group
$\mathrm{BS}(1, n)$.

Button's counterexample is the solvable ascending HNN extension of
$\mathbb{Z} \times \mathbb{Z} = \langle u, v \rangle$ by the injective endomorphism
$u \mapsto u^5 v^{-1}$, $v \mapsto u^2$: it is not locally subgroup-separable but contains no
$\mathrm{BS}(1, m)$ with $m \ne 0, \pm 1$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.2 (R. C. Alperin); resolution: J. O. Button, Strictly ascending HNN extensions in soluble groups, Ricerche di Matematica 61 (2012), no. 1, 139-145, arXiv:1004.0197, Theorem 2.1 and the remark after it (the soluble ascending HNN extension G = ⟨t, ℤ × ℤ⟩ with θ(u) = u⁵v⁻¹, θ(v) = u² is not LERF and contains no BS(1, m), m ≠ 0, ±1, so the answer to Problem 16.2 is no); Kourovka Archive, Problem 16.2 (No, it is not), https://arxiv.org/abs/1004.0197.

Stated but not proved: `MathlibExt.GroupTheory.SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.solvableLERFIffNoBaumslagSolitar_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SolvableLERFBaumslagSolitarKourovka16Problem2Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups/index.html#solvable-lerfiff-no-baumslag-solitar-ref).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgroup separability of Baumslag–Solitar groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/subgroup-separability-of-baumslag-solitar-groups)
