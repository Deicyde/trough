---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.eigenvector_mem_range_of_hasEigenvector, MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.exists_linearIndependent_eigenvectors, MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.finite_nonzero_hasEigenvalue_of_finiteDimensional_range, MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.ncard_nonzero_hasEigenvalue_le_finrank_range, MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.isCompactOperator_of_finiteDimensional_range, MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.spectrum_subset_insert_zero_hasEigenvalue, MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.hasEigenvalue_subset_spectrum, MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.finite_spectrum_of_finiteDimensional_range
statement: formalized
proof: formalized
---

# Spectrum of finite-rank operators

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html).

## Linear Algebra

## Eigenvectors for nonzero eigenvalues lie in the range

An eigenvector for a nonzero eigenvalue lies in the range: if
`T v = μ • v` with `μ ≠ 0`, then `v = T (μ⁻¹ • v)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.eigenvector_mem_range_of_hasEigenvector`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#eigenvector-mem-range-of-has-eigenvector).

## Independent eigenvectors for distinct nonzero eigenvalues

Choose one eigenvector for each nonzero eigenvalue of `T`. The chosen
eigenvectors are linearly independent (eigenvectors for distinct eigenvalues)
and all lie in the range of `T`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.exists_linearIndependent_eigenvectors`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#exists-linear-independent-eigenvectors).

## Eigenvalue finiteness for finite-rank operators

A finite-rank
operator has only finitely many distinct nonzero eigenvalues.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.finite_nonzero_hasEigenvalue_of_finiteDimensional_range`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#finite-nonzero-has-eigenvalue-of-finite).

## Eigenvalue-count bound for finite-rank operators

There are at most
`finrank (range T)` distinct nonzero eigenvalues.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.Module.End.ncard_nonzero_hasEigenvalue_le_finrank_range`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#ncard-nonzero-has-eigenvalue-le-finrank).

## Finite-rank operators are compact

A finite-rank operator is compact: it factors through its
finite-dimensional range, and every continuous linear map out of a
finite-dimensional (hence locally compact) space is compact.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.isCompactOperator_of_finiteDimensional_range`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#is-compact-operator-of-finite-dimensiona).

## Nonzero spectral values of a finite-rank operator are eigenvalues

The spectrum of a finite-rank operator is contained in
`{0} ∪ {eigenvalues}`: every nonzero spectral value is an eigenvalue, by
the Fredholm alternative for compact operators.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.spectrum_subset_insert_zero_hasEigenvalue`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#spectrum-subset-insert-zero-has-eigenval).

## Eigenvalues of a finite-rank operator lie in its spectrum

Every eigenvalue of a finite-rank operator lies in its spectrum.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.hasEigenvalue_subset_spectrum`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#has-eigenvalue-subset-spectrum).

## Spectrum of a finite-rank operator is finite

The spectrum of a finite-rank operator is finite.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.finite_spectrum_of_finiteDimensional_range`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#finite-spectrum-of-finite-dimensional-ra).

## Bound on the size of the spectrum of a finite-rank operator

The spectrum of a finite-rank operator has at most
`finrank (range T) + 1` points.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.ncard_spectrum_le_finrank_range_add_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#ncard-spectrum-le-finrank-range-add-one).

## Spectrum of a finite-rank operator on an infinite-dimensional space

The spectrum is exactly `{0} ∪ {eigenvalues}`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.FiniteRankSpectrum.spectrum_eq_insert_zero_hasEigenvalue`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/FiniteRankSpectrum.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html#spectrum-eq-insert-zero-has-eigenvalue).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectrum of finite-rank operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory/spectrum-of-finite-rank-operators)
