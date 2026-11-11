---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SimpleGroupCharacterValuesKourovka11Problem97Wanted.irrCharValues, MathlibExt.GroupTheory.SimpleGroupCharacterValuesKourovka11Problem97Wanted.finitelyManySimpleGivenCharacterValues, MathlibExt.GroupTheory.SimpleGroupCharacterValuesKourovka11Problem97Wanted.finitelyManySimpleGivenCharacterValues_refuted
statement: formalized
---

# Character values of simple groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-values-of-simple-groups/index.html).

## Values of the irreducible characters at an element

For an element $g$ of a group $G$, the
set of complex numbers $\chi(g)$, where $\chi$ ranges over the characters of the irreducible
finite-dimensional complex representations of $G$.

Formalized by `MathlibExt.GroupTheory.SimpleGroupCharacterValuesKourovka11Problem97Wanted.irrCharValues`, a definition declared in [WantedExt/GroupTheory/SimpleGroupCharacterValuesKourovka11Problem97Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupCharacterValuesKourovka11Problem97Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-values-of-simple-groups/index.html#irr-char-values).

## Kourovka Problem 11.97 (simple groups with a given set of character values)

The
statement that for every finite set $S$ of complex numbers there is a bound $N$ such that every
finite non-abelian simple group $G$ having an element $g$ at which the set of values of the
irreducible complex characters of $G$ is exactly $S$ has order at most $N$. The problem is due to
S. P. Strunkov.

"Only finitely many such groups" up to isomorphism is stated as this bound on the order.

Formalized by `MathlibExt.GroupTheory.SimpleGroupCharacterValuesKourovka11Problem97Wanted.finitelyManySimpleGivenCharacterValues`, a definition declared in [WantedExt/GroupTheory/SimpleGroupCharacterValuesKourovka11Problem97Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupCharacterValuesKourovka11Problem97Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-values-of-simple-groups/index.html#finitely-many-simple-given-character-val).

## Kourovka Problem 11.97 has a negative answer

There is a finite set $S$ of complex numbers
such that for every natural number $N$ there is a finite non-abelian simple group $G$ with more
than $N$ elements and an element $g \in G$ at which the set of values of the irreducible complex
characters of $G$ is exactly $S$.

The Kourovka Archive records (V. D. Mazurov) that every complex irreducible character of
$L_2(2^m)$, $m \ge 2$, takes a value in $\{0, 1, -1\}$ at an involution, so some subset of
$\{0, 1, -1\}$ is the set of values at an involution for infinitely many of these non-abelian
simple groups.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.97 (S. P. Strunkov); resolution: V. D. Mazurov, Kourovka Archive, Problem 11.97: "No; all complex irreducible characters of the groups `L_2(2^m)`, `m ≥ 2`, take the values `0, ±1` on involutions", https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SimpleGroupCharacterValuesKourovka11Problem97Wanted.finitelyManySimpleGivenCharacterValues_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SimpleGroupCharacterValuesKourovka11Problem97Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SimpleGroupCharacterValuesKourovka11Problem97Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-values-of-simple-groups/index.html#finitely-many-simple-given-character-val-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Character values of simple groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-values-of-simple-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/characters-of-finite-groups/character-values-of-simple-groups)
