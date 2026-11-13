---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.IsMonsterFirstKind, MathlibExt.GroupTheory.MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.monsterHasTorsionFreeCyclicCentralExtension, MathlibExt.GroupTheory.MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.monsterHasTorsionFreeCyclicCentralExtension_refuted
statement: formalized
---

# Monsters of the first kind

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/monsters-of-the-first-kind/index.html).

## Monster of the first kind

A group $G$ is a *monster of the first kind* (V. P. Shunkov)
when $G$ is infinite, $G$ has an element of order greater than $2$, and for every element $a$ of
order greater than $2$ and every proper subgroup $H$ of $G$ there is $g \in G \setminus H$ such
that $a$ and $g^{-1} a g$ generate $G$. Here an element of infinite order counts as having order
greater than $2$.

Formalized by `MathlibExt.GroupTheory.MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.IsMonsterFirstKind`, a definition declared in [WantedExt/GroupTheory/MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/monsters-of-the-first-kind/index.html#is-monster-first-kind).

## Shunkov's question on central extensions of monsters

Kourovka Problem 14.104
(V. P. Shunkov) asks whether this proposition holds: for every monster of the first kind $M$ there
are a torsion-free group $E$ and a cyclic subgroup $C$ contained in the center of $E$ such that
$E / C \cong M$.

Formalized by `MathlibExt.GroupTheory.MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.monsterHasTorsionFreeCyclicCentralExtension`, a definition declared in [WantedExt/GroupTheory/MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/monsters-of-the-first-kind/index.html#monster-has-torsion-free-cyclic-central).

## Not every monster of the first kind is a torsion-free group modulo a central cyclic subgroup

It is not the case that for every monster of the first kind $M$ there are a torsion-free group $E$
and a cyclic subgroup $C$ contained in the center of $E$ with $E / C \cong M$. So Kourovka
Problem 14.104 has a negative answer.

The Kourovka Archive answers 14.104 "No, not always" (A. I. Sozutov): if a torsion-free group $E$
has a central cyclic subgroup $C$ with $E / C \cong M$, then every finite subgroup of $M$ is
cyclic, and some monsters of the first kind have non-cyclic finite subgroups.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 14.104 (V. P. Shunkov); resolution: A. I. Sozutov, letter of 20 November 2001, Kourovka Archive, Problem 14.104: such an extension forces every finite subgroup of the monster to be cyclic, which fails for some monsters (answer: No, not always).

Stated but not proved: `MathlibExt.GroupTheory.MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.monsterHasTorsionFreeCyclicCentralExtension_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MonsterTorsionFreeCentralExtensionKourovka14Problem104Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/monsters-of-the-first-kind/index.html#monster-has-torsion-free-cyclic-central-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monsters of the first kind](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/monsters-of-the-first-kind/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/monsters-of-the-first-kind)
