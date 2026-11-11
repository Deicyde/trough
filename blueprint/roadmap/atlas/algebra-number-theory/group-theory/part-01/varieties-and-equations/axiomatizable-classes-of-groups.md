---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.GroupClass, MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.IsFormation, MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.IsAxiomatizable, MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.IsVariety, MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.axiomatizableFormationIsVariety, MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.axiomatizableFormationIsVariety_refuted
statement: formalized
---

# Axiomatizable classes of groups

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html).

## Class of groups

A class of groups, as a predicate on groups in `Type`.

Formalized by `MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.GroupClass`, an abbreviation declared in [WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html#group-class).

## Formations of groups in the sense of Gaglione and Spellman

A class $\mathfrak{F}$ of
groups is a formation when it contains at least one group, it is closed under surjective
homomorphic images (if $G \in \mathfrak{F}$ and $\varphi \colon G \to H$ is a surjective
homomorphism, then $H \in \mathfrak{F}$), and for every group $G$ and all normal subgroups $N_1$,
$N_2$ of $G$, if $G/N_1$ and $G/N_2$ lie in $\mathfrak{F}$, then so does $G/(N_1 \cap N_2)$.

Together with closure under homomorphic images, the last condition amounts to closure under
subdirect products of finitely many factors; the groups need not be finite.

Formalized by `MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.IsFormation`, a definition declared in [WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html#is-formation).

## First-order axiomatizable classes of groups

A class $\mathfrak{F}$ of groups is
first-order axiomatizable when there is a theory $T$ in the first-order language of groups such
that a group $G$ lies in $\mathfrak{F}$ if and only if $G$, with its canonical structure, is a
model of $T$.

Formalized by `MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.IsAxiomatizable`, a definition declared in [WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html#is-axiomatizable).

## Varieties of groups

A class $\mathfrak{F}$ of groups is a variety when there is a set
$W$ of elements of the free group on generators $x_0, x_1, x_2, \dots$ such that a group $G$ lies
in $\mathfrak{F}$ if and only if every $w \in W$ evaluates to $1$ in $G$ under every assignment of
elements of $G$ to the generators.

Formalized by `MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.IsVariety`, a definition declared in [WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html#is-variety).

## The Gaglione–Spellman question on axiomatizable formations (Kourovka 14.32)

The
proposition that every first-order axiomatizable formation of groups is a variety: every class
$\mathfrak{F}$ of groups that is a formation and is first-order axiomatizable is a variety.

Formalized by `MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.axiomatizableFormationIsVariety`, a definition declared in [WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html#axiomatizable-formation-is-variety).

## Not every axiomatizable formation of groups is a variety

The Gaglione–Spellman question
(Kourovka 14.32) has a negative answer: it is not the case that every first-order axiomatizable
formation of groups is a variety, that is, some class of groups is a formation and is first-order
axiomatizable but is not a variety.

Kearnes proved more: every variety of groups that contains a finite non-solvable group contains a
first-order axiomatizable subformation that is not a variety.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.32 (A. M. Gaglione, D. Spellman); resolution: K. A. Kearnes, J. Group Theory 13 (2010), no. 2, 233-241, Kourovka Archive, Problem 14.32: every variety of groups containing a finite non-solvable member contains an axiomatic subformation that is not a variety (answer: No).

Stated but not proved: `MathlibExt.GroupTheory.AxiomatizableFormationVarietyKourovka14Problem32Wanted.axiomatizableFormationIsVariety_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AxiomatizableFormationVarietyKourovka14Problem32Wanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html#axiomatizable-formation-is-variety-refut).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Axiomatizable classes of groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/varieties-and-equations/axiomatizable-classes-of-groups)
