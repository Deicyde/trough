---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ScottishBook95Wanted.real_addGroup_embeds_in_perm_nat, MathlibExt.GroupTheory.SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.separableMetrizableGroupEmbedsInSym, MathlibExt.GroupTheory.SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.separableMetrizableGroupEmbedsInSym_refuted
statement: formalized
---

# Subgroups of the infinite symmetric group

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/subgroups-of-the-infinite-symmetric-group/index.html).

## The additive group of the reals embeds in the infinite symmetric group

There is an injective
group homomorphism from the additive group $(\mathbb{R}, +)$ of real numbers into the group
$S_\infty$ of all permutations of the natural numbers.

## Sources

- J. Schreier and S. Ulam, Problem 95 of the Scottish Book; affirmative answer of Schreier and Ulam, November 1935, recorded in the typescript addendum Ad 95. `Multiplicative ℝ` is the additive group `ℝ` viewed multiplicatively, so a monoid homomorphism out of it is an additive homomorphism out of `ℝ`.

Stated but not proved: `MathlibExt.GroupTheory.ScottishBook95Wanted.real_addGroup_embeds_in_perm_nat` is written with `theorem_wanted` in [WantedExt/GroupTheory/ScottishBook95Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ScottishBook95Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/subgroups-of-the-infinite-symmetric-group/index.html#real-add-group-embeds-in-perm-nat).

## Claim of Kourovka Problem 18.36

The claim (J. D. Dixon) that every group $G$ that
admits a metrizable topology making it a separable topological group admits an injective group
homomorphism into the group $\mathrm{Sym}(\mathbb{N})$ of all permutations of the natural
numbers.

Formalized by `MathlibExt.GroupTheory.SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.separableMetrizableGroupEmbedsInSym`, a definition declared in [WantedExt/GroupTheory/SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/subgroups-of-the-infinite-symmetric-group/index.html#separable-metrizable-group-embeds-in-sym).

## Separable metrizable groups need not embed in the infinite symmetric group

The claim of
Kourovka Problem 18.36 is false: there is a group $G$ that admits a metrizable topology
making it a separable topological group but admits no injective group homomorphism into the
group $\mathrm{Sym}(\mathbb{N})$ of all permutations of the natural numbers.

Rosendal and Solecki (2007) give an uncountable connected Polish group (a separable
completely metrizable topological group) every abstract homomorphism of which into
$\mathrm{Sym}(\mathbb{N})$ is trivial, so it has no injective one.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.36 (J. D. Dixon); resolution: C. Rosendal and S. Solecki, Israel J. Math. 162 (2007), 349-371, an uncountable connected Polish group whose every abstract homomorphism into Sym(ℕ) is trivial; see also A. Kaïchouh and F. Le Maître, Bull. London Math. Soc. 47 (2015), 996-1009 (S. Corson, letter of 5 June 2024); the Kourovka Notebook (21st issue) marks 18.36 solved, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.separableMetrizableGroupEmbedsInSym_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/SeparableMetrizableGroupSymEmbeddingKourovka18Problem36Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/subgroups-of-the-infinite-symmetric-group/index.html#separable-metrizable-group-embeds-in-sym-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subgroups of the infinite symmetric group](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/subgroups-of-the-infinite-symmetric-group/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/subgroups-of-the-infinite-symmetric-group)
