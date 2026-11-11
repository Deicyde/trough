---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.IsPLocal, MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.IsPLocalization, MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.SplitsAtPrime, MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.nilpotentExtensionSplitsIfSplitsAtPrimes, MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.nilpotentExtensionSplitsIfSplitsAtPrimes_refuted
statement: formalized
---

# Localization of nilpotent groups

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups/index.html).

## $p$-local groups

Let $p$ be a natural number. A group $H$ is $p$-local when, for every
natural number $n$ coprime to $p$, the map $x \mapsto x^n$ is a bijection of $H$.

This is the notion of a $P$-local group of Hilton, Mislin and Roitberg, for $P$ the set whose only
element is $p$.

Formalized by `MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.IsPLocal`, a definition declared in [WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups/index.html#is-plocal).

## $p$-localization of a group

Let $p$ be a natural number. A homomorphism of groups
$e \colon G \to L$ is a $p$-localization when $L$ is nilpotent and $p$-local, and every
homomorphism $f$ from $G$ to a nilpotent $p$-local group $H$ factors uniquely through $e$: there is
exactly one homomorphism $g \colon L \to H$ with $g \circ e = f$.

Formalized by `MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.IsPLocalization`, a definition declared in [WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups/index.html#is-plocalization).

## Splitting at a prime

Let $p$ be a natural number and $\pi \colon G \to Q$ a homomorphism
of groups (in the intended use, the quotient map of an extension). Then $\pi$ splits at $p$ when
there exist $p$-localizations $e_G \colon G \to G_p$ and $e_Q \colon Q \to Q_p$ and homomorphisms
$\pi_p \colon G_p \to Q_p$ and $s \colon Q_p \to G_p$ with $\pi_p \circ e_G = e_Q \circ \pi$ and
$\pi_p \circ s = \mathrm{id}_{Q_p}$; that is, the localized quotient map $\pi_p$ has a homomorphic
section.

Since $Q_p$ is nilpotent and $p$-local, $\pi_p$ is the unique homomorphism with
$\pi_p \circ e_G = e_Q \circ \pi$; since localizations are unique up to unique isomorphism, the
condition does not depend on the chosen localizations.

Formalized by `MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.SplitsAtPrime`, a definition declared in [WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups/index.html#splits-at-prime).

## Hilton's splitting question for nilpotent extensions (Kourovka 12.93)

The proposition
that every extension of nilpotent groups with finitely generated quotient that splits at every
prime splits: for all nilpotent groups $N$, $G$ and $Q$ with $Q$ finitely generated, every
injective homomorphism $i \colon N \to G$ and every surjective homomorphism $\pi \colon G \to Q$
with $\operatorname{im} i = \ker \pi$ such that the extension splits at every prime $p$, there is
a homomorphism $s \colon Q \to G$ with $\pi \circ s = \mathrm{id}_Q$.

Formalized by `MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.nilpotentExtensionSplitsIfSplitsAtPrimes`, a definition declared in [WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups/index.html#nilpotent-extension-splits-if-splits-at).

## Nilpotent extensions that split at every prime need not split

It is not true that every
extension of nilpotent groups with finitely generated quotient that splits at every prime splits:
there are nilpotent groups $N$, $G$ and $Q$ with $Q$ finitely generated, an injective homomorphism
$i \colon N \to G$ and a surjective homomorphism $\pi \colon G \to Q$ with $\operatorname{im} i =
\ker \pi$, such that the extension splits at every prime $p$ (for some $p$-localizations $G_p$
of $G$ and $Q_p$ of $Q$, the localized quotient map $\pi_p \colon G_p \to Q_p$ has a homomorphic
section) but there is no homomorphism $s \colon Q \to G$ with $\pi \circ s = \mathrm{id}_Q$.

Lorensen constructed such extensions in which $N$, $G$ and $Q$ are finitely generated and
torsion-free.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.93 (P. Hilton); resolution: K. Lorensen, Nonsplit nilpotent group extensions that split at every prime, Math. Proc. Cambridge Philos. Soc. 123 (1998), no. 2, 213-215, doi:10.1017/S0305004197002211, introduction (first page, shown on Cambridge Core): examples of nilpotent group extensions which split at every p-localization but fail to split, disproving Hilton's conjecture that any nilpotent group extension with finitely generated quotient which splits at every prime must split; in both families of counterexamples the groups are torsion-free and finitely generated. Kourovka Archive, Problem 12.93: 'No, not always', https://doi.org/10.1017/S0305004197002211.

Stated but not proved: `MathlibExt.GroupTheory.NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.nilpotentExtensionSplitsIfSplitsAtPrimes_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NilpotentExtensionSplitAtPrimesKourovka12Problem93Wanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups/index.html#nilpotent-extension-splits-if-splits-at-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Localization of nilpotent groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/localization-of-nilpotent-groups)
