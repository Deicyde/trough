---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.BurnsideHigmanEmbeddingKourovka12Problem32Wanted.BurnsidePresented, MathlibExt.GroupTheory.BurnsideHigmanEmbeddingKourovka12Problem32Wanted.higmanEmbeddingBurnsideVariety, MathlibExt.GroupTheory.BurnsideHigmanEmbeddingKourovka12Problem32Wanted.higmanEmbeddingBurnsideVariety_holds
statement: formalized
---

# Higman embedding in Burnside varieties

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/higman-embedding-in-burnside-varieties/index.html).

## Groups finitely presented in a Burnside variety

For natural numbers $n$ and $m$ and a
finite set $S$ of elements of the free group on $x_0, \dots, x_{m-1}$, this is the group with
generators $x_0, \dots, x_{m-1}$ and relators $S$ together with $w^n$ for every element $w$ of the
free group: the group finitely presented by $S$ in the Burnside variety $\mathfrak{B}_n$ of groups
of exponent $n$.

Formalized by `MathlibExt.GroupTheory.BurnsideHigmanEmbeddingKourovka12Problem32Wanted.BurnsidePresented`, an abbreviation declared in [WantedExt/GroupTheory/BurnsideHigmanEmbeddingKourovka12Problem32Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BurnsideHigmanEmbeddingKourovka12Problem32Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/higman-embedding-in-burnside-varieties/index.html#burnside-presented).

## Kourovka Problem 12.32: Higman embedding for Burnside varieties

There is $n_0$ such that
for every odd $n \ge n_0$ the following holds. Let $G$ be a group given by generators
$x_0, x_1, \dots$ and a recursively enumerable set of relators, and suppose that $g^n = 1$ for
every $g \in G$. Then for some $m$ and some finite set $S$ of elements of the free group on
$x_0, \dots, x_{m-1}$, there is an injective homomorphism from $G$ to the group finitely presented
by $S$ in the Burnside variety $\mathfrak{B}_n$, whose relators are $S$ together with $w^n$ for
every element $w$ of that free group.

The relators are words in the generators, and recursive enumerability refers to these words.

Formalized by `MathlibExt.GroupTheory.BurnsideHigmanEmbeddingKourovka12Problem32Wanted.higmanEmbeddingBurnsideVariety`, a definition declared in [WantedExt/GroupTheory/BurnsideHigmanEmbeddingKourovka12Problem32Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BurnsideHigmanEmbeddingKourovka12Problem32Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/higman-embedding-in-burnside-varieties/index.html#higman-embedding-burnside-variety).

## Higman embedding theorem for Burnside varieties

There is $n_0$ such that for every odd
$n \ge n_0$, every group of exponent $n$ given by generators $x_0, x_1, \dots$ and a recursively
enumerable set of relators embeds in a group finitely presented in the Burnside variety
$\mathfrak{B}_n$: a group with generators $x_0, \dots, x_{m-1}$ for some $m$ whose relators are a
finite set $S$ together with $w^n$ for every word $w$.

Olshanskii proves this with the ambient group 2-generated; the statement here does not require it.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.32 (S. V. Ivanov); resolution: A. Yu. Olshanskii, Groups finitely presented in Burnside varieties, J. Algebra 560 (2020), 960-1052, Theorem 1.1 (finitely generated groups) and Corollary 1.2 (countably many generators; the ambient group can be taken 2-generated), for all odd n ≥ C; Kourovka Archive, Problem 12.32.

Stated but not proved: `MathlibExt.GroupTheory.BurnsideHigmanEmbeddingKourovka12Problem32Wanted.higmanEmbeddingBurnsideVariety_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/BurnsideHigmanEmbeddingKourovka12Problem32Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/BurnsideHigmanEmbeddingKourovka12Problem32Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/higman-embedding-in-burnside-varieties/index.html#higman-embedding-burnside-variety-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Higman embedding in Burnside varieties](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/higman-embedding-in-burnside-varieties/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/higman-embedding-in-burnside-varieties)
