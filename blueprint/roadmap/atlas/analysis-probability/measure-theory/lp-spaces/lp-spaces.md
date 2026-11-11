---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.LpSubadditivePowLtOneWanted.integral_abs_rpow_sub_rpow_le_integral_rpow_abs_sub
statement: formalized
---

# Lebesgue spaces: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/index.html).

The spaces Lp of p-th power integrable functions: membership criteria, inclusions, dense subspaces, the essential supremum and weak convergence.

## An integral inequality for $p$-th powers with $0 < p < 1$

Let $\mu$ be a measure on a
measurable space and let $0 < p < 1$. Then for all real-valued $f, g \in L^p(\mu)$,

$$\int \bigl||f|^p - |g|^p\bigr|\,d\mu \le \int |f - g|^p\,d\mu.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l1_53`.

Stated but not proved: `MathlibExt.MeasureTheory.LpSubadditivePowLtOneWanted.integral_abs_rpow_sub_rpow_le_integral_rpow_abs_sub` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LpSubadditivePowLtOneWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LpSubadditivePowLtOneWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/index.html#integral-abs-rpow-sub-rpow-le-integral-r).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lebesgue spaces](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lp-spaces)
