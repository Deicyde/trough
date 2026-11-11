---
declaration: section
origin: cited
lean: IsGHarmonic, IsGHarmonic.intro, IsGHarmonic.pos, IsGHarmonic.witnesses, isGHarmonic_iff, isGHarmonic_empty, isGHarmonic_singleton_one, not_isGHarmonic_of_zero
statement: formalized
proof: formalized
---

# Disjoint coset systems

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html).

## G-harmonic tuples

Let $G$ be a group and $a = (a_1, \dots, a_n)$ a tuple of natural
numbers. The tuple $a$ is $G$-harmonic if every $a_i$ is positive and there exist subgroups
$U_1, \dots, U_n$ of $G$ and elements $g_1, \dots, g_n \in G$ such that $U_i$ has index $a_i$ in
$G$ for every $i$ and the left cosets $g_1 U_1, \dots, g_n U_n$ are pairwise disjoint.

Formalized by `IsGHarmonic`, a definition declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#is-gharmonic).

## Constructing a G-harmonic tuple

Let $G$ be a group and $a = (a_1, \dots, a_n)$ a tuple
of natural numbers with every $a_i$ positive. If $U_1, \dots, U_n$ are subgroups of $G$ such that
$U_i$ has index $a_i$ in $G$ for every $i$, and $g_1, \dots, g_n \in G$ are elements such that the
left cosets $g_1 U_1, \dots, g_n U_n$ are pairwise disjoint, then $a$ is $G$-harmonic.

Formalized by `IsGHarmonic.intro`, a theorem declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#intro).

## Entries of a G-harmonic tuple are positive

Let $G$ be a group. If a tuple
$a = (a_1, \dots, a_n)$ of natural numbers is $G$-harmonic, then $a_i > 0$ for every $i$.

Formalized by `IsGHarmonic.pos`, a theorem declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#pos).

## Witnesses for a G-harmonic tuple

Let $G$ be a group. If a tuple $a = (a_1, \dots, a_n)$
of natural numbers is $G$-harmonic, then there exist subgroups $U_1, \dots, U_n$ of $G$ and
elements $g_1, \dots, g_n \in G$ such that $U_i$ has index $a_i$ in $G$ for every $i$ and the
left cosets $g_1 U_1, \dots, g_n U_n$ are pairwise disjoint.

Formalized by `IsGHarmonic.witnesses`, a theorem declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#witnesses).

## Characterization of G-harmonic tuples

Let $G$ be a group and $a = (a_1, \dots, a_n)$ a
tuple of natural numbers. Then $a$ is $G$-harmonic if and only if every $a_i$ is positive and
there are subgroups $U_1, \dots, U_n$ of $G$ and elements $g_1, \dots, g_n \in G$ such that $U_i$
has index $a_i$ in $G$ for every $i$ and the left cosets $g_1 U_1, \dots, g_n U_n$ are pairwise
disjoint.

Formalized by `isGHarmonic_iff`, a theorem declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#is-gharmonic-iff).

## The empty tuple is G-harmonic

For every group $G$, the empty tuple of natural numbers is
(vacuously) $G$-harmonic.

Formalized by `isGHarmonic_empty`, a theorem declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#is-gharmonic-empty).

## The tuple (1) is G-harmonic

For every group $G$, the one-entry tuple $(1)$ is
$G$-harmonic; the subgroup $G$ itself, of index $1$, with coset representative $1$ witnesses
this.

Formalized by `isGHarmonic_singleton_one`, a theorem declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#is-gharmonic-singleton-one).

## Tuples with a zero entry are not G-harmonic

Let $G$ be a group. If a tuple
$a = (a_1, \dots, a_n)$ of natural numbers has $a_i = 0$ for some $i$, then $a$ is not
$G$-harmonic.

Formalized by `not_isGHarmonic_of_zero`, a theorem declared in [MathlibExt/GroupTheory/GHarmonic.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GHarmonic.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html#not-is-gharmonic-of-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Disjoint coset systems](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups/disjoint-coset-systems)
