---
declaration: theorem
origin: cited
lean: GaussianField.measure_eq_of_moments, GaussianField.weakLimit_centered_gaussianReal, GaussianField.integrable_exp_smul_of_integrable_exp_sq, GaussianField.mgf_eq_of_covariance, GaussianField.eval_map_eq_gaussianReal, Pphi2.canonicalRoughFieldFunction_covariance_eq, Pphi2.canonicalSumFieldFunction_covariance_eq_GJ, Pphi2.canonicalRoughFieldFunction_eq_of_snd
statement: formalized
proof: formalized
---

# pphi2

[mrdouglasny/pphi2](https://github.com/mrdouglasny/pphi2) at commit [83501022](https://github.com/mrdouglasny/pphi2/tree/83501022fc6ff5f38e93a4d5b631ef4044b66216), 2026-10-08.

> Formal construction of the P(Φ)₂ Euclidean quantum field theory in Lean 4, following the Glimm-Jaffe/Nelson lattice approach.

*Quoted from [README.md](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/README.md), Apache-2.0.*

## Depends on

- [Vector-valued integrable function (Bochner integral)](../../analysis/measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Exponential](../../analysis/special-functions/exponential.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Gaussian law](../random-variables-and-their-laws/gaussian-law.md)

## Proof depends on

- [Plancherel’s theorem](../../../undergraduate/measures-and-integral-calculus/fourier-analysis/plancherels-theorem.md)
- [Jensen's inequality (integral version)](../../analysis/convexity/jensens-inequality-integral-version.md)
- [Convolution](../../analysis/measures-and-integral-calculus/part-02/convolution.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)
- [Existence of Hilbert basis](../../analysis/hilbert-spaces/existence-of-hilbert-basis.md)
- [Fourier transform as an integral](../../analysis/fourier-analysis/fourier-transform-as-an-integral.md)
- [Hilbert bases](../../../undergraduate/topology/hilbert-spaces/hilbert-bases.md)
- [Characteristic function](../definitions-in-probability-theory/characteristic-function.md)

## Main results

Its Lean names are 8 of the 226 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`GaussianField.measure_eq_of_moments`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/TorusContinuumLimit/MeasureUniqueness.lean#L754) (theorem)
- [`GaussianField.weakLimit_centered_gaussianReal`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/TorusContinuumLimit/MeasureUniqueness.lean#L280) (theorem)
- [`GaussianField.integrable_exp_smul_of_integrable_exp_sq`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/TorusContinuumLimit/MeasureUniqueness.lean#L677) (theorem)
- [`GaussianField.mgf_eq_of_covariance`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/TorusContinuumLimit/MeasureUniqueness.lean#L75) (theorem)
- [`GaussianField.eval_map_eq_gaussianReal`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/TorusContinuumLimit/MeasureUniqueness.lean#L124) (theorem)
- [`Pphi2.canonicalRoughFieldFunction_covariance_eq`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/NelsonEstimate/FieldDecomposition.lean#L2243) (theorem)
- [`Pphi2.canonicalSumFieldFunction_covariance_eq_GJ`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/NelsonEstimate/FieldDecomposition.lean#L3859) (theorem)
- [`Pphi2.canonicalRoughFieldFunction_eq_of_snd`](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/Pphi2/NelsonEstimate/FieldDecomposition.lean#L255) (theorem)

No file its headlines import, directly or not (17 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.30.0, Mathlib at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- 198 .lean files; its Lean libraries `Pphi2`, `Common` hold 175, declaring 1,901 names, with `sorry` in 0 files and 26 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/mrdouglasny/pphi2/blob/83501022fc6ff5f38e93a4d5b631ef4044b66216/LICENSE)).

## Builds on

- Mathlib, at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- `bochner` (https://github.com/mrdouglasny/bochner.git) at `34222bb7`.
- `GaussianField` (https://github.com/mrdouglasny/gaussian-field.git) at `d63a2856`.
- `GibbsVariational` (https://github.com/mrdouglasny/gibbs-variational.git) at `a7535d19`.
- `«gaussian-hilbert»` (https://github.com/mrdouglasny/gaussian-hilbert.git) at `56ee09f0`.
- `«reflection-positivity»` (https://github.com/mrdouglasny/reflection-positivity.git) at `1cf71831`.

## Placement

Of its imports of Mathlib modules in an overview area, 19 of 173 are in Probability Theory, 5.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (19 of 173 imports, 5.8×), Analysis (125 of 173 imports, 2.7×). *Proof depends on* names 8 of the 76 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [mrdouglasny/pphi2 at 83501022](https://github.com/mrdouglasny/pphi2/tree/83501022fc6ff5f38e93a4d5b631ef4044b66216)
