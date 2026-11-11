---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.IsInClassS, MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.LocallyIsomorphic, MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.uncountablyManyLocalIsomorphismClasses, MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.uncountablyManyLocalIsomorphismClasses_holds
statement: formalized
---

# Totally disconnected locally compact groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/totally-disconnected-locally-compact-groups/index.html).

## Caprace's class $\mathcal{S}$

A group $G$ with a topology belongs to the class
$\mathcal{S}$ when it is a topological group that is Hausdorff, totally disconnected, locally
compact and not discrete, is generated as a group by some compact subset, and is topologically
simple: $G$ is nontrivial and its only closed normal subgroups are the trivial subgroup and $G$
itself.

Formalized by `MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.IsInClassS`, a definition declared in [WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/totally-disconnected-locally-compact-groups/index.html#is-in-class-s).

## Locally isomorphic topological groups

Two topological groups are locally isomorphic: they contain open subgroups that are isomorphic
as topological groups.

Formalized by `MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.LocallyIsomorphic`, a definition declared in [WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/totally-disconnected-locally-compact-groups/index.html#locally-isomorphic).

## Caprace's problem on local isomorphism classes (Kourovka 19.22)

The statement that the
groups in Caprace's class $\mathcal{S}$ fall into uncountably many local isomorphism classes: there
is a family $(G_i)_{i \in I}$ of groups in $\mathcal{S}$, indexed by an uncountable set $I$, such
that $G_i$ and $G_j$ are not locally isomorphic whenever $i \ne j$.

Formalized by `MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.uncountablyManyLocalIsomorphismClasses`, a definition declared in [WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/totally-disconnected-locally-compact-groups/index.html#uncountably-many-local-isomorphism-class).

## Uncountably many local isomorphism classes of simple tdlc groups

There is a family
$(G_i)_{i \in I}$ of groups in Caprace's class $\mathcal{S}$ (non-discrete, compactly generated,
topologically simple, totally disconnected, locally compact Hausdorff topological groups), indexed
by an uncountable set $I$, such that $G_i$ and $G_j$ are not locally isomorphic whenever $i \ne j$.
This answers Kourovka Notebook Problem 19.22 (P.-E. Caprace) in the affirmative.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.22 (P.-E. Caprace); resolution: I. Castellano, J. Fariña-Asategui, M. E. Garciarena, B. Marchionna, M. Quick, C. D. Reid, S. M. Smith, S. Tornier, M. Vannacci and J. S. Wilson, Uncountably many local isomorphism types of compactly generated simple groups, preprint, arXiv:2609.17410 (2026), Theorem A: there exist 2^ℵ₀ many non-discrete compactly generated simple tdlc groups which are not pairwise locally isomorphic; the Kourovka Notebook (21st issue) marks 19.22 solved: Yes, it is, https://arxiv.org/abs/2609.17410.

Stated but not proved: `MathlibExt.GroupTheory.LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.uncountablyManyLocalIsomorphismClasses_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/LocalIsomorphismClassesSimpleTdlcKourovka19Problem22Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/totally-disconnected-locally-compact-groups/index.html#uncountably-many-local-isomorphism-class-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Totally disconnected locally compact groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/totally-disconnected-locally-compact-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/totally-disconnected-locally-compact-groups)
