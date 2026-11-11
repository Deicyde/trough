---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.BoundedL1MemL2NormBoundWanted.memLp_two_and_eLpNorm_two_le_of_bounded_of_memLp_one, MathlibExt.MeasureTheory.LpTwoLpOneIncomparableWanted.not_memLp_two_subset_one_and_not_memLp_one_subset_two, MathlibExt.MeasureTheory.MemLpOfLqIntegrableOnFiniteMeasureSetsWanted.memLp_of_memLp_of_lintegral_rpow_lt_top_of_measure_lt_top
statement: formalized
---

# Inclusions between Lp spaces

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/inclusions-between-lp-spaces/index.html).

## A bounded integrable function is square integrable

Let $d$ be a natural number, let
$M \ge 0$, and let $f \colon \mathbb{R}^d \to \mathbb{R}$ satisfy $|f(x)| \le M$ for every
$x \in \mathbb{R}^d$. If $f \in L^1(\mathbb{R}^d)$, then $f \in L^2(\mathbb{R}^d)$ and

$$\|f\|_{L^2(\mathbb{R}^d)} \le M^{1/2} \, \|f\|_{L^1(\mathbb{R}^d)}^{1/2},$$

where the spaces and norms are taken with respect to Lebesgue measure.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l1_41`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.BoundedL1MemL2NormBoundWanted.memLp_two_and_eLpNorm_two_le_of_bounded_of_memLp_one` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/BoundedL1MemL2NormBoundWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/BoundedL1MemL2NormBoundWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/inclusions-between-lp-spaces/index.html#mem-lp-two-and-e-lp-norm-two-le-of-bound).

## $L^1(\mathbb{R}^d)$ and $L^2(\mathbb{R}^d)$ are incomparable

Let $d \ge 1$. With respect
to Lebesgue measure on $\mathbb{R}^d$, there is a function $f : \mathbb{R}^d \to \mathbb{R}$ in
$L^2(\mathbb{R}^d)$ that is not in $L^1(\mathbb{R}^d)$, and there is a function
$g : \mathbb{R}^d \to \mathbb{R}$ in $L^1(\mathbb{R}^d)$ that is not in $L^2(\mathbb{R}^d)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l1_97`.

Stated but not proved: `MathlibExt.MeasureTheory.LpTwoLpOneIncomparableWanted.not_memLp_two_subset_one_and_not_memLp_one_subset_two` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LpTwoLpOneIncomparableWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LpTwoLpOneIncomparableWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/inclusions-between-lp-spaces/index.html#not-mem-lp-two-subset-one-and-not-mem-lp).

## An $L^p$ function with finite $L^q$ mass on finite-measure sets is in $L^q$

Let
$1 \le p < q < \infty$ and let $f : \mathbb{R} \to \mathbb{R}$ belong to $L^p(\mathbb{R})$. If
$\int_A |f|^q < \infty$ for every Borel set $A \subseteq \mathbb{R}$ of finite Lebesgue measure,
then $f \in L^q(\mathbb{R})$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_24`.

Stated but not proved: `MathlibExt.MeasureTheory.MemLpOfLqIntegrableOnFiniteMeasureSetsWanted.memLp_of_memLp_of_lintegral_rpow_lt_top_of_measure_lt_top` is written with `theorem_wanted` in [WantedExt/MeasureTheory/MemLpOfLqIntegrableOnFiniteMeasureSetsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/MemLpOfLqIntegrableOnFiniteMeasureSetsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/inclusions-between-lp-spaces/index.html#mem-lp-of-mem-lp-of-lintegral-rpow-lt-to).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inclusions between Lp spaces](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/inclusions-between-lp-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lp-spaces/inclusions-between-lp-spaces)
