---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.RNA.Nussinov.IsStructure, Cslib.Bioinformatics.RNA.Nussinov.listMax, Cslib.Bioinformatics.RNA.Nussinov.nussinov, Cslib.Bioinformatics.RNA.Nussinov.card_le_nussinov, Cslib.Bioinformatics.RNA.Nussinov.exists_isStructure_card_eq
statement: formalized
proof: formalized
---

# Nussinov algorithm for RNA secondary structure

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure/index.html).

## RNA secondary structure

A secondary structure on `s` (Nussinov et al. 1978): a finite set of base pairs `(i, j)`,
each closing a hairpin with at least `m` unpaired positions strictly inside (`i + m < j`), joining
complementary bases (`pair s[i] s[j]`, which also puts both positions inside `s`), with every
position in at most one pair and no two pairs crossing (`i < k < j < l`).

Formalized by `Cslib.Bioinformatics.RNA.Nussinov.IsStructure`, a structure declared in [CSLibExt/Bioinformatics/RNA/Nussinov.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/RNA/Nussinov.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure/index.html#is-structure).

## Maximum of a list of natural numbers

The largest of a list of naturals (`0` for the empty list).

Formalized by `Cslib.Bioinformatics.RNA.Nussinov.listMax`, a definition declared in [CSLibExt/Bioinformatics/RNA/Nussinov.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/RNA/Nussinov.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure/index.html#list-max).

## The Nussinov recursion

The first base `a` of `a :: rest` is either unpaired, or paired
with `rest[k]` for some `k ≥ m` with `pair a rest[k]`, splitting the rest into the enclosed part
`rest.take k` and the outer part `rest.drop (k + 1)`. Exponential-time specification; the usual
`O(n³)` table memoizes it on the intervals of `s`.

Formalized by `Cslib.Bioinformatics.RNA.Nussinov.nussinov`, a definition declared in [CSLibExt/Bioinformatics/RNA/Nussinov.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/RNA/Nussinov.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure/index.html#nussinov).

## Soundness bound

Every secondary structure has at most `nussinov pair m s` pairs.

Formalized by `Cslib.Bioinformatics.RNA.Nussinov.card_le_nussinov`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Nussinov.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/RNA/Nussinov.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure/index.html#card-le-nussinov).

## Optimality

Some secondary structure has exactly `nussinov pair m s` pairs, so the
recursion computes the maximum number of pairs over all non-crossing structures.

Formalized by `Cslib.Bioinformatics.RNA.Nussinov.exists_isStructure_card_eq`, a theorem declared in [CSLibExt/Bioinformatics/RNA/Nussinov.lean, line 518](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/RNA/Nussinov.lean#L518). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure/index.html#exists-is-structure-card-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nussinov algorithm for RNA secondary structure](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/nussinov-algorithm-for-rna-secondary-structure)
