---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Series.HilbertInequality.hilbertKernel, MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow, MathlibExt.Analysis.Series.HilbertInequality.hilbertKernel_nonneg, MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow_nonneg, MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow_continuousOn, MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow_antitoneOn, MathlibExt.Analysis.Series.HilbertInequality.hasDerivAt_hilbertAntideriv, MathlibExt.Analysis.Series.HilbertInequality.intervalIntegral_hilbertKernelRow
statement: formalized
proof: formalized
---

# Hilbert's inequality

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html).

## Hilbert kernel

The Hilbert kernel with `0`-based indices: `1 / ((m + 1) + (n + 1))`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernel`, a definition declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel).

## Row integrand for the Hilbert kernel

The row integrand `x ↦ 1 / ((M + x) * √x)` used to bound the row sums
of the Hilbert kernel by an integral.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow`, a definition declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-row).

## Nonnegativity of the Hilbert kernel

The Hilbert kernel is nonnegative.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernel_nonneg`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-nonneg).

## Nonnegativity of the Hilbert row integrand

The row integrand is nonnegative on `(0, ∞)` when `M > 0`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow_nonneg`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-row-nonneg).

## Continuity of the Hilbert row integrand

The row integrand is continuous on `(0, ∞)` when `M > 0`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow_continuousOn`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-row-continuous-on).

## Hilbert row integrand is decreasing on (1, ∞)

The row integrand is antitone on `[1, ∞)` when `M > 0`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRow_antitoneOn`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-row-antitone-on).

## Derivative of the arctangent antiderivative of the row integrand

The derivative of the antiderivative `(2 / √M) * arctan √(x / M)`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hasDerivAt_hilbertAntideriv`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#has-deriv-at-hilbert-antideriv).

## Finite integral of the Hilbert row integrand

The finite integral of the row integrand, via its antiderivative.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.intervalIntegral_hilbertKernelRow`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#interval-integral-hilbert-kernel-row).

## Integrability of the Hilbert row integrand on (1, ∞)

The row integrand is integrable on `(1, ∞)`, with a uniform bound on
the interval integrals.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.integrableOn_Ioi_hilbertKernelRow`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#integrable-on-ioi-hilbert-kernel-row).

## Improper integral of the Hilbert row integrand

The improper integral of the row integrand over `(1, ∞)`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.integral_Ioi_hilbertKernelRow`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#integral-ioi-hilbert-kernel-row).

## Lower bound for the arctangent

A lower bound for `arctan`: `t / (1 + t ^ 2) ≤ arctan t` for `t ≥ 0`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.div_one_add_sq_le_arctan`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#div-one-add-sq-le-arctan).

## Terms of the Hilbert row series

The `n`-th term of the row series, `1 / ((M + (n + 1)) * √((n + 1)))`,
as a function of `n : ℕ`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernelRowSeq`, a definition declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-row-seq).

## Summability of the Hilbert row series

Summability of the row series.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.summable_hilbertKernelRowSeq`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#summable-hilbert-kernel-row-seq).

## Summability of the Hilbert row series in unfolded form

Summability of the row series in unfurled form.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.summable_hilbertKernelRow`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#summable-hilbert-kernel-row).

## Row sum bound for the Hilbert kernel

The row sum of the Hilbert kernel is at most `π / √(m + 1)`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernel_row_sum_le`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-row-sum-le).

## Symmetry of the Hilbert kernel

The Hilbert kernel is symmetric.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbertKernel_symm`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-kernel-symm).

## Schur test for finite bilinear forms

The Schur test for finite bilinear forms: a weighted row/column bound
implies a bound on the bilinear form with constant `√(α * β)`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.schurTest_finite`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#schur-test-finite).

## Finite Hilbert inequality

The finite form of Hilbert's inequality, from the Schur test with the
weights `r n = 1 / √(n + 1)` and the row bound `hilbertKernel_row_sum_le`.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbert_inequality_finite`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-inequality-finite).

## Summability of the Hilbert double series

The nonnegative Hilbert double series is summable for square-summable inputs.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.summable_hilbert_terms`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 638](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L638). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#summable-hilbert-terms).

## Hilbert's inequality

Hilbert's inequality for square-summable real sequences.

Formalized by `MathlibExt.Analysis.Series.HilbertInequality.hilbert_inequality`, a theorem declared in [MathlibExt/Analysis/Series/HilbertInequality.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/HilbertInequality.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html#hilbert-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert's inequality](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/hilbert-s-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/inequalities/hilbert-s-inequality)
