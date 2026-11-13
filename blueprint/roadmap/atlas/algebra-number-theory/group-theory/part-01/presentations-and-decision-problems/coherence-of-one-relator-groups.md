---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.Group.Coherent, MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.Ring.Coherent, MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.Group.OneRelator, MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.OnCoherenceOfOneRelatorGroups.theorem_1_1
statement: formalized
---

# Coherence of one-relator groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/coherence-of-one-relator-groups/index.html).

## Coherent groups and rings

## Coherent group

A group is coherent if all of its finitely generated subgroups are
finitely presented.

Formalized by `MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.Group.Coherent`, a definition declared in [WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/coherence-of-one-relator-groups/index.html#coherent).

## Coherent ring

A semiring $R$ is (left) coherent if every finitely generated left ideal
of $R$ is finitely presented as an $R$-module.

Formalized by `MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.Ring.Coherent`, a definition declared in [WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/coherence-of-one-relator-groups/index.html#coherent-2).

## One-relator group

A group `G` is called one-relator if it has a presentation with a single relation.

Formalized by `MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.Group.OneRelator`, a definition declared in [WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/coherence-of-one-relator-groups/index.html#one-relator-group).

## Jaikin-Zapirain–Linton theorem: one-relator groups are coherent

Let $G$ be a one-relator
group and $K$ a field. Then $G$ is a coherent group and the group algebra $K[G]$ is a (left)
coherent ring.

## Sources

- A. Jaikin-Zapirain and M. Linton, `On the coherence of one-relator groups and their group algebras`, Annals of Math, 201 (3) 2025. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_on_coherence_of_one_relator_groups` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.OnCoherenceOfOneRelatorGroupsWanted.OnCoherenceOfOneRelatorGroups.theorem_1_1` is written with `theorem_wanted` in [WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OnCoherenceOfOneRelatorGroupsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/coherence-of-one-relator-groups/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Coherence of one-relator groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/coherence-of-one-relator-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/coherence-of-one-relator-groups)
