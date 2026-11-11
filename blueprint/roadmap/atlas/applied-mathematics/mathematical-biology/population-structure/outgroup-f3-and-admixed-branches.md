---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f3_eq_sum_inter_symmDiff, MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f3_outgroup, MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f3_outgroup_le_iff, MathlibExt.Biology.PopulationGenetics.TreeFStatistics.mixedDrift, MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f2_admixedBranch, MathlibExt.Biology.PopulationGenetics.TreeFStatistics.alpha_eq_of_f2, MathlibExt.Biology.PopulationGenetics.TreeFStatistics.mixedDrift_eq
statement: formalized
proof: formalized
---

# Outgroup f3 and admixed branches

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html).

## Outgroup f3

## f3 statistic as shared drift on a tree

With binary loadings, `f3 O A B` is the total drift length of the edges shared by the paths
`O–A` and `O–B` (on a tree, the path from `O` to the `A–B` path).

Formalized by `MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f3_eq_sum_inter_symmDiff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html#f3-eq-sum-inter-symm-diff).

## Outgroup f3 statistic

Outgroup `f3` (Raghavan et al. 2014): with binary loadings, if the lineage of `O` shares no
edge with the lineages of `A` and `B`, then `f3 O A B` is the drift from the outgroup to the root
plus the drift shared by `A` and `B`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f3_outgroup`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html#f3-outgroup).

## Outgroup f3 ranks populations by shared drift

For a fixed outgroup `O` and population `A`, the outgroup `f3` ranks candidates `B` by the
drift they share with `A`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f3_outgroup_le_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html#f3-outgroup-le-iff).

## MixMapper mixed drift

MixMapper's mixed drift `α² ℓ_a + (1 - α)² ℓ_b + ℓ_c`: the only combination of the terminal
drift lengths that enters the `f2` statistics of an admixed population.

Formalized by `MathlibExt.Biology.PopulationGenetics.TreeFStatistics.mixedDrift`, a definition declared in [MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html#mixed-drift).

## Admixed-branch identity for f2 statistics

The admixed-branch identity (Lipson et al. 2013): if `Mx` is an `α : 1 - α` mixture of the
endpoints of the edges `a` (below `A`) and `b` (below `B`), followed by drift on `c`, and `A`,
`B`, `X` do not use `a`, `b`, `c`, then
`f2 Mx X = α f2 A X + (1 - α) f2 B X - α (1 - α) f2 A B + mixedDrift α ℓ_a ℓ_b ℓ_c`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TreeFStatistics.f2_admixedBranch`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html#f2-admixed-branch).

## Identifiability of the admixture proportion from f2 statistics

Identifiability of the mixture proportion (our formulation): with the split points `A`, `B`
given, two references `X₁`, `X₂` satisfying the hypotheses of `f2_admixedBranch` and with
different contrasts `f2 A Xᵢ - f2 B Xᵢ` determine `α` from `f2` statistics.

Formalized by `MathlibExt.Biology.PopulationGenetics.TreeFStatistics.alpha_eq_of_f2`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html#alpha-eq-of-f2).

## Mixed drift determined by f2 statistics

Given `α`, the mixed drift is determined by the `f2` statistics of one reference `X`.

Formalized by `MathlibExt.Biology.PopulationGenetics.TreeFStatistics.mixedDrift_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/TreeFStatistics.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html#mixed-drift-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Outgroup f3 and admixed branches](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-structure/outgroup-f3-and-admixed-branches)
