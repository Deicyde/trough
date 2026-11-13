---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.AeNullSequenceUnboundedMultipliersWanted.exists_tendsto_abs_atTop_and_ae_tendsto_mul_zero, MathlibExt.MeasureTheory.DilatedL1FunctionDecayAeWanted.ae_tendsto_rpow_neg_mul_comp_mul_zero
statement: formalized
---

# Almost everywhere convergence

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/almost-everywhere-convergence/index.html).

## Unbounded multipliers preserving almost-everywhere convergence to zero

Let
$(f_n)_{n \in \mathbb{N}}$ be a sequence of Borel measurable functions $f_n : \mathbb{R} \to
\mathbb{R}$ such that $f_n(x) \to 0$ for almost every $x \in [0, 1]$. Then there is a sequence of
real numbers $(c_n)_{n \in \mathbb{N}}$ with $|c_n| \to \infty$ such that $c_n f_n(x) \to 0$ for
almost every $x \in [0, 1]$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_38`.

Stated but not proved: `MathlibExt.MeasureTheory.AeNullSequenceUnboundedMultipliersWanted.exists_tendsto_abs_atTop_and_ae_tendsto_mul_zero` is written with `theorem_wanted` in [WantedExt/MeasureTheory/AeNullSequenceUnboundedMultipliersWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/AeNullSequenceUnboundedMultipliersWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/almost-everywhere-convergence/index.html#exists-tendsto-abs-at-top-and-ae-tendsto).

## Decay of dilates of an integrable function

Let $f : \mathbb{R} \to \mathbb{R}$ be
Lebesgue integrable and let $\lambda > 0$. Then for almost every $x \in \mathbb{R}$,
$n^{-\lambda} f(nx) \to 0$ as $n \to \infty$ through the positive integers.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_37`.

Stated but not proved: `MathlibExt.MeasureTheory.DilatedL1FunctionDecayAeWanted.ae_tendsto_rpow_neg_mul_comp_mul_zero` is written with `theorem_wanted` in [WantedExt/MeasureTheory/DilatedL1FunctionDecayAeWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/DilatedL1FunctionDecayAeWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/almost-everywhere-convergence/index.html#ae-tendsto-rpow-neg-mul-comp-mul-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Almost everywhere convergence](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/almost-everywhere-convergence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/integration/almost-everywhere-convergence)
