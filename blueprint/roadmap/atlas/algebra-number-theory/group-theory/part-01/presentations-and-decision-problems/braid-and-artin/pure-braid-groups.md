---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.PureBraidConjugateInverseKourovka11Problem54Wanted.pureBraidGroup, MathlibExt.GroupTheory.PureBraidConjugateInverseKourovka11Problem54Wanted.pureBraidConjInvTrivial, MathlibExt.GroupTheory.PureBraidConjugateInverseKourovka11Problem54Wanted.pureBraidConjInvTrivial_holds, MathlibExt.GroupTheory.PureBraidUniqueRootsKourovka11Problem55Wanted.pureBraidGroup, MathlibExt.GroupTheory.PureBraidUniqueRootsKourovka11Problem55Wanted.pureBraidUniqueRoots, MathlibExt.GroupTheory.PureBraidUniqueRootsKourovka11Problem55Wanted.pureBraidUniqueRoots_holds
statement: formalized
---

# Pure braid groups

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html).

## Pure braid group

For $n \in \mathbb{N}$, the pure (coloured) braid group $P_{n+1}$ on
$n + 1$ strands is the normal closure, in the braid group $B_{n+1}$, of the squares $\sigma_i^2$ of
the standard generators $\sigma_1, \dots, \sigma_n$ of $B_{n+1}$, where $B_{n+1}$ is the Artin
group of the Coxeter matrix of type $A_n$.

This is the kernel of the map $B_{n+1} \to S_{n+1}$, since adding the relations $\sigma_i^2 = 1$ to
the braid relations presents the Coxeter group of type $A_n$, the symmetric group $S_{n+1}$.

Formalized by `MathlibExt.GroupTheory.PureBraidConjugateInverseKourovka11Problem54Wanted.pureBraidGroup`, a definition declared in [WantedExt/GroupTheory/PureBraidConjugateInverseKourovka11Problem54Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PureBraidConjugateInverseKourovka11Problem54Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html#pure-braid-group).

## Kourovka 11.54: pure braids conjugate to their inverses

The proposition that for every
$n \in \mathbb{N}$, every pure braid $\beta$ on $n + 1$ strands that is conjugate to its inverse
inside the pure braid group, that is, $\gamma \beta \gamma^{-1} = \beta^{-1}$ for some pure braid
$\gamma$ on $n + 1$ strands, is the identity braid.

This is Kourovka Problem 11.54 (G. S. Makanin).

Formalized by `MathlibExt.GroupTheory.PureBraidConjugateInverseKourovka11Problem54Wanted.pureBraidConjInvTrivial`, a definition declared in [WantedExt/GroupTheory/PureBraidConjugateInverseKourovka11Problem54Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PureBraidConjugateInverseKourovka11Problem54Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html#pure-braid-conj-inv-trivial).

## Kourovka 11.54: only the trivial pure braid is conjugate to its inverse

For every
$n \in \mathbb{N}$ and every pure braid $\beta$ on $n + 1$ strands, if
$\gamma \beta \gamma^{-1} = \beta^{-1}$ for some pure braid $\gamma$ on $n + 1$ strands, then
$\beta = 1$.

The Kourovka Archive answers 11.54 affirmatively (V. A. Roman'kov): the pure braid group embeds in
the IA-automorphism group of a free group, which is residually torsion-free nilpotent, and in a
torsion-free nilpotent group an element conjugate to its inverse is trivial.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.54 (G. S. Makanin); resolution: V. A. Roman'kov, letter of 3 October 1990; see also V. G. Bardakov, Russ. Acad. Sci. Sb. Math. 76, no. 1 (1993), 123-153, Kourovka Archive, Problems 11.54 and 11.55: both affirmative, since the coloured braid group embeds in the group of automorphisms of `F_n` acting trivially modulo `F_n'`, which is residually torsion-free nilpotent, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.PureBraidConjugateInverseKourovka11Problem54Wanted.pureBraidConjInvTrivial_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PureBraidConjugateInverseKourovka11Problem54Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PureBraidConjugateInverseKourovka11Problem54Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html#pure-braid-conj-inv-trivial-holds).

## Pure braid group

For $n \in \mathbb{N}$, the pure (coloured) braid group $P_{n+1}$ on
$n + 1$ strands is the normal closure, in the braid group $B_{n+1}$, of the squares $\sigma_i^2$ of
the standard generators $\sigma_1, \dots, \sigma_n$ of $B_{n+1}$, where $B_{n+1}$ is the Artin
group of the Coxeter matrix of type $A_n$.

This is the kernel of the map $B_{n+1} \to S_{n+1}$, since adding the relations $\sigma_i^2 = 1$ to
the braid relations presents the Coxeter group of type $A_n$, the symmetric group $S_{n+1}$.

Formalized by `MathlibExt.GroupTheory.PureBraidUniqueRootsKourovka11Problem55Wanted.pureBraidGroup`, a definition declared in [WantedExt/GroupTheory/PureBraidUniqueRootsKourovka11Problem55Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PureBraidUniqueRootsKourovka11Problem55Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html#pure-braid-group-2).

## Kourovka 11.55: unique roots in pure braid groups

The proposition that for every
$n \in \mathbb{N}$ and every integer $k \ge 1$, if pure braids $\alpha$ and $\beta$ on $n + 1$
strands satisfy $\alpha^k = \beta^k$, then $\alpha = \beta$.

This is Kourovka Problem 11.55 (G. S. Makanin): extraction of roots in the group of coloured
braids is unique.

Formalized by `MathlibExt.GroupTheory.PureBraidUniqueRootsKourovka11Problem55Wanted.pureBraidUniqueRoots`, a definition declared in [WantedExt/GroupTheory/PureBraidUniqueRootsKourovka11Problem55Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PureBraidUniqueRootsKourovka11Problem55Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html#pure-braid-unique-roots).

## Kourovka 11.55: roots in pure braid groups are unique

For every $n \in \mathbb{N}$ and every
integer $k \ge 1$, if pure braids $\alpha$ and $\beta$ on $n + 1$ strands satisfy
$\alpha^k = \beta^k$, then $\alpha = \beta$.

The Kourovka Archive answers 11.55 affirmatively (V. A. Roman'kov): the pure braid group embeds in
the IA-automorphism group of a free group, which is residually torsion-free nilpotent, and
torsion-free nilpotent groups have unique roots.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.55 (G. S. Makanin); resolution: V. A. Roman'kov, letter of 3 October 1990; see also V. G. Bardakov, Russ. Acad. Sci. Sb. Math. 76, no. 1 (1993), 123-153, Kourovka Archive, Problems 11.54 and 11.55: both affirmative, since the coloured braid group embeds in the group of automorphisms of `F_n` acting trivially modulo `F_n'`, which is residually torsion-free nilpotent, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.PureBraidUniqueRootsKourovka11Problem55Wanted.pureBraidUniqueRoots_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/PureBraidUniqueRootsKourovka11Problem55Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/PureBraidUniqueRootsKourovka11Problem55Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html#pure-braid-unique-roots-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pure braid groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/pure-braid-groups)
