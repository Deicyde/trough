---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DensityRestrictedSumsetShiftErdosProblem656Wanted.restrictedSumsetShiftInDenseSet, MathlibExt.Combinatorics.DensityRestrictedSumsetShiftErdosProblem656Wanted.restrictedSumsetShiftInDenseSet_holds
statement: formalized
---

# Shifted sumsets in sets of positive density

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/shifted-sumsets-in-sets-of-positive-density/index.html).

## Erdős Problem 656 (shifted restricted sumsets in dense sets)

The statement that for every
set $A$ of natural numbers with positive upper density, that is, with
$\limsup_{N \to \infty} |A \cap \{0, \dots, N - 1\}| / N > 0$, there are an infinite set
$B \subseteq A$ and an integer $t$ such that $b_1 + b_2 + t \in A$ for all distinct
$b_1, b_2 \in B$.

Formalized by `MathlibExt.Combinatorics.DensityRestrictedSumsetShiftErdosProblem656Wanted.restrictedSumsetShiftInDenseSet`, a definition declared in [WantedExt/Combinatorics/DensityRestrictedSumsetShiftErdosProblem656Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DensityRestrictedSumsetShiftErdosProblem656Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/shifted-sumsets-in-sets-of-positive-density/index.html#restricted-sumset-shift-in-dense-set).

## Erdős Problem 656 is true

For every set $A$ of natural numbers with positive upper density,
that is, with $\limsup_{N \to \infty} |A \cap \{0, \dots, N - 1\}| / N > 0$, there are an infinite
set $B \subseteq A$ and an integer $t$ such that $b_1 + b_2 + t \in A$ for all distinct
$b_1, b_2 \in B$.

This is the theorem of Kra, Moreira, Richter and Robertson.

## Sources

- T. F. Bloom, Erdős Problems, Problem #656, https://www.erdosproblems.com/656 (status PROVED); resolution: B. Kra, J. Moreira, F. K. Richter and D. Robertson, A proof of Erdős's B + B + t conjecture, Commun. Am. Math. Soc. (2024), 480-494, arXiv:2206.12377, abstract: every set A of natural numbers with positive upper density can be shifted to contain the restricted sumset {b₁ + b₂ : b₁, b₂ ∈ B, b₁ ≠ b₂} for some infinite set B ⊂ A, https://arxiv.org/abs/2206.12377.

Stated but not proved: `MathlibExt.Combinatorics.DensityRestrictedSumsetShiftErdosProblem656Wanted.restrictedSumsetShiftInDenseSet_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/DensityRestrictedSumsetShiftErdosProblem656Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DensityRestrictedSumsetShiftErdosProblem656Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/shifted-sumsets-in-sets-of-positive-density/index.html#restricted-sumset-shift-in-dense-set-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shifted sumsets in sets of positive density](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/shifted-sumsets-in-sets-of-positive-density/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases/shifted-sumsets-in-sets-of-positive-density)
