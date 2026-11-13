---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.JustFinitePresentationKourovka21Problem10Wanted.finiteGroupHasJustFinitePresentation, MathlibExt.GroupTheory.JustFinitePresentationKourovka21Problem10Wanted.finiteGroupHasJustFinitePresentation_holds
statement: formalized
---

# Just finite presentations

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/just-finite-presentations/index.html).

## Barnea's question on just finite presentations (Kourovka 21.10)

The statement that every
finite group $G$ has a just finite presentation: a presentation $\langle X \mid R \rangle$ with $X$
and $R$ finite that defines $G$ and such that removing any single relator from $R$ gives a
presentation of an infinite group.

Formalized by `MathlibExt.GroupTheory.JustFinitePresentationKourovka21Problem10Wanted.finiteGroupHasJustFinitePresentation`, a definition declared in [WantedExt/GroupTheory/JustFinitePresentationKourovka21Problem10Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustFinitePresentationKourovka21Problem10Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/just-finite-presentations/index.html#finite-group-has-just-finite-presentatio).

## Every finite group has a just finite presentation

For every finite group $G$ there are a
natural number $n$ and a finite subset $R$ of the free group on $n$ generators $x_1, \dots, x_n$
such that the group $\langle x_1, \dots, x_n \mid R \rangle$ is isomorphic to $G$ and, for every
$r \in R$, the group $\langle x_1, \dots, x_n \mid R \setminus \{r\} \rangle$ is infinite. That is,
the answer to Kourovka Problem 21.10 is positive.

Lackenby's paper acknowledges assistance from the Google DeepMind AI co-mathematician tool.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 21.10 (Y. Barnea); resolution: M. Lackenby, Every finite group admits a just finite presentation, preprint, arXiv:2605.10402 (2026), Theorem 1: every finite group admits a finite, just finite presentation (a consequence of Theorem 2 on just-(FA) presentations); Kourovka Notebook (21st issue), Problem 21.10: Yes, it is true, https://arxiv.org/abs/2605.10402.

Stated but not proved: `MathlibExt.GroupTheory.JustFinitePresentationKourovka21Problem10Wanted.finiteGroupHasJustFinitePresentation_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/JustFinitePresentationKourovka21Problem10Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/JustFinitePresentationKourovka21Problem10Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/just-finite-presentations/index.html#finite-group-has-just-finite-presentatio-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Just finite presentations](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/just-finite-presentations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/just-finite-presentations)
