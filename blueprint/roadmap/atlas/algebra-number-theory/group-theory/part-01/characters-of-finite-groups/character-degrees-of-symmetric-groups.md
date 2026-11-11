---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.IsIrreducibleRep, MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.IsEquivalentRep, MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.symmetricGroupManyCharactersOfEqualDegree, MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.symmetricGroupManyCharactersOfEqualDegree_holds
statement: formalized
---

# Character degrees of symmetric groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-symmetric-groups/index.html).

## Irreducible complex matrix representations (Kourovka 16.67)

Let $G$ be a group and $n$ a
natural number. A homomorphism $\rho \colon G \to \mathrm{GL}_n(\mathbb{C})$ is irreducible when
$n \ge 1$ and every subspace $W$ of $\mathbb{C}^n$ such that $\rho(g) v \in W$ for all $g \in G$
and all $v \in W$ is either $0$ or $\mathbb{C}^n$.

Formalized by `MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.IsIrreducibleRep`, a definition declared in [WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-symmetric-groups/index.html#is-irreducible-rep).

## Equivalent complex matrix representations (Kourovka 16.67)

Let $G$ be a group and $n$ a
natural number. Two homomorphisms $\rho, \sigma \colon G \to \mathrm{GL}_n(\mathbb{C})$ are
equivalent when there is a single invertible matrix $P \in \mathrm{GL}_n(\mathbb{C})$ with
$\sigma(g) = P \rho(g) P^{-1}$ for every $g \in G$.

Formalized by `MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.IsEquivalentRep`, a definition declared in [WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-symmetric-groups/index.html#is-equivalent-rep).

## Moretó's conjecture on equal character degrees of symmetric groups

For every natural
number $k$ there is a natural number $n_0$ such that for every $n \ge n_0$ there are a natural
number $d$ and irreducible representations $\rho_1, \dots, \rho_k$ of the symmetric group $S_n$
into $\mathrm{GL}_d(\mathbb{C})$ that are pairwise inequivalent: $\rho_i$ and $\rho_j$ are not
equivalent whenever $i \ne j$.

Since irreducible complex characters correspond to equivalence classes of irreducible complex
representations and the degree of a character is the dimension, this says that $S_n$ has at least
$k$ distinct irreducible complex characters of the same degree.

Formalized by `MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.symmetricGroupManyCharactersOfEqualDegree`, a definition declared in [WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-symmetric-groups/index.html#symmetric-group-many-characters-of-equal).

## Symmetric groups have many irreducible characters of equal degree

Moretó's conjecture
holds: for every natural number $k$ there is a natural number $n_0$ such that for every
$n \ge n_0$ there are a natural number $d$ and irreducible representations
$\rho_1, \dots, \rho_k$ of the symmetric group $S_n$ into $\mathrm{GL}_d(\mathbb{C})$ that are
pairwise inequivalent.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.67 (A. Moretó); resolution: D. A. Craven, Symmetric group character degrees and hook numbers, Proc. London Math. Soc. (3) 96 (2008), 26-50, arXiv:0709.0897, Theorem 1.2 (the size of a largest set of irreducible characters of S_n of one degree tends to infinity), the case k = 1 of Theorem 1.1 (for any k and ℓ and all sufficiently large n, S_n has k disjoint sets of ℓ irreducible characters, equal degrees within each set); Kourovka Archive, Problem 16.67 (This is proved), https://arxiv.org/abs/0709.0897.

Stated but not proved: `MathlibExt.GroupTheory.SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.symmetricGroupManyCharactersOfEqualDegree_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SymmetricGroupEqualCharacterDegreesKourovka16Problem67Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-symmetric-groups/index.html#symmetric-group-many-characters-of-equal-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Character degrees of symmetric groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-symmetric-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-symmetric-groups)
