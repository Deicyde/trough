---
declaration: theorem
origin: cited
lean: GaussianTesting.threeCopyAverage_fixed_iff_accProb_eq_one, GaussianTesting.threeCopyAverage_spectrum_subset_unitInterval, GaussianTesting.threeCopyAverage_hasEigenvalue_one, GaussianTesting.threeCopyAverage_isGreatest_eigenvalue, GaussianTesting.testing_fidelity_of_threeCopy_spectrum, GaussianTesting.RobustnessBounds.linear_fidelity, GaussianTesting.schrodingerDifference_even, GaussianTesting.schrodingerDifference_column_even
statement: formalized
proof: formalized
---

# gaussian-testing

*Testing bosonic and fermionic Gaussian states with a constant number of copies*

[qit-lmu/gaussian-testing](https://github.com/qit-lmu/gaussian-testing) at commit [9133f49b](https://github.com/qit-lmu/gaussian-testing/tree/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38), 2026-11-08.

> Lean + Mathlib formalization of the paper by Jop Briët, Davi Castro-Silva, Michael Walter, and Freek Witteveen ([arXiv:2610.06794](https://arxiv.org/abs/2610.06794)).

*Quoted from [README.md](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/README.md), Apache-2.0.*

## Depends on

- [Eigenvalue](../../../linear-algebra/structure-theory-of-endomorphisms/eigenvalue.md)
- [Hilbert bases](../../../../undergraduate/topology/hilbert-spaces/hilbert-bases.md)

## Proof depends on

- [Existence of Hilbert basis](../../hilbert-spaces/existence-of-hilbert-basis.md)
- [Special orthogonal group](../../../../undergraduate/group-theory/classical-automorphism-groups/special-orthogonal-group.md)
- [Cauchy filter](../../../topology/uniform-notions/cauchy-filter.md)
- [Bernoulli law](../../../probability-theory/random-variables-and-their-laws/bernoulli-law.md)
- [Derivative of a composition of functions (Analysis)](../../differentiability/derivative-of-a-composition-of-functions.md)
- [Angle](../../../geometry/affine-and-euclidean-geometry/angle.md)
- [Norm of a continuous linear map](../../normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Fourier transform on $\mathrm{L}^2(\R^d)$](../../../../undergraduate/measures-and-integral-calculus/fourier-analysis/fourier-transform-on-l-2-r-d.md)

## Main results

Its Lean names are 8 of the 43 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`GaussianTesting.threeCopyAverage_fixed_iff_accProb_eq_one`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/GradientFlow/FixedPoints.lean#L34) (theorem)
- [`GaussianTesting.threeCopyAverage_spectrum_subset_unitInterval`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/GradientFlow/FixedPoints.lean#L70) (theorem)
- [`GaussianTesting.threeCopyAverage_hasEigenvalue_one`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/GradientFlow/FixedPoints.lean#L56) (theorem)
- [`GaussianTesting.threeCopyAverage_isGreatest_eigenvalue`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/GradientFlow/FixedPoints.lean#L79) (theorem)
- [`GaussianTesting.testing_fidelity_of_threeCopy_spectrum`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/GradientFlow/HilbertSpectralGap.lean#L72) (theorem)
- [`GaussianTesting.RobustnessBounds.linear_fidelity`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/GradientFlow/SharpRobustness.lean#L69) (theorem)
- [`GaussianTesting.schrodingerDifference_even`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/Bosons/DifferenceParity.lean#L36) (theorem)
- [`GaussianTesting.schrodingerDifference_column_even`](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/GaussianTesting/Bosons/DifferenceParity.lean#L52) (theorem)

No file its headlines import, directly or not (91 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 256 .lean files; its Lean libraries `GaussianTesting` hold 253, declaring 2,553 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/qit-lmu/gaussian-testing/blob/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 154 of 222 are in Analysis, 2.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (154 of 222 imports, 2.6×), Linear algebra (26 of 222 imports, 2.0×). *Proof depends on* lists 8 of the 89 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [qit-lmu/gaussian-testing at 9133f49b](https://github.com/qit-lmu/gaussian-testing/tree/9133f49bfeca4b8f1da6ed1b1f94041b0b148c38)
