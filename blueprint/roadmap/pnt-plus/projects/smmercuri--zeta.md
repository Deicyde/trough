---
declaration: theorem
origin: cited
lean: Complex.Stirling.norm_digamma_sub_log_le', sum_integral_gramCoord_le, abs_riemannSiegelTheta_sub_stirling_le, abs_hardyZ_sub_re_le, Zeta.RiemannSiegel.kernel_add_one, Zeta.RiemannSiegel.kernel_add_one_sub_kernel, Zeta.RiemannSiegel.tendsto_contourIntegral_atTop_nhds_riemannZeta_add_contourIntegral_half, Zeta.RiemannSiegel.kernel_eq_tsum_of_im_neg
statement: formalized
proof: formalized
---

# zeta

*Certifying the Riemann hypothesis up to bounded height in Lean*

[smmercuri/zeta](https://github.com/smmercuri/zeta) at commit [34037d5a](https://github.com/smmercuri/zeta/tree/34037d5a7662e2eb6e970bfb22299c84e45ed5d9), 2026-11-15.

> This repository proves in Lean's kernel that all the nontrivial zeros of the Riemann zeta function up to a specified height $T$ lie on the critical line, as predicted by the Riemann hypothesis. Intervals are certified on the critical line, proving the location of nontrivial zeros with configurable precision. The main theorem is proved fully in the kernel, depending only on the standard axiom set `[propext, Classical.choice, Quot.sound]`.

*Quoted from [README.md](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/README.md), Apache-2.0.*

## Depends on

- [Logarithm](../../mathlib/overview/analysis/special-functions/logarithm.md)
- [Complex exponential](../../mathlib/undergraduate/single-variable-complex-analysis/complex-valued-series/complex-exponential.md)
- [Limit of a map with respect to filters](../../mathlib/overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Proof depends on

- [Log](../../mathlib/undergraduate/single-variable-complex-analysis/complex-valued-series/power-series-expansion-of-elementary-functions/log.md)
- [Characterization of convexity](../../mathlib/overview/analysis/convexity/characterization-of-convexity.md)
- [Bernoulli numbers](../../mathlib/overview/general-algebra/number-theory/bernoulli-numbers.md)
- [Sin (extension of trigonometric functions to the complex plane)](../../mathlib/undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/sin.md)
- [Euler’s Summation of 1 + (1/2)^2 + (1/3)^2 + ….](../../mathlib/hundred-theorems/part-01/eulers-summation-of-1-1-2-2-1-3-2.md)
- [Fundamental theorem of calculus, part 2](../../mathlib/overview/analysis/measures-and-integral-calculus/part-01/fundamental-theorem-of-calculus-part-2.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../mathlib/undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Geometric series](../../mathlib/undergraduate/single-variable-real-analysis/numerical-series/geometric-series.md)

## Main results

Its Lean names are 8 of the 16 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`Complex.Stirling.norm_digamma_sub_log_le'`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/Gamma/DigammaStirling.lean#L478) (theorem)
- [`sum_integral_gramCoord_le`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/Gram/Averaging.lean#L157) (theorem)
- [`abs_riemannSiegelTheta_sub_stirling_le`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/Zeros/HardyZ.lean#L379) (theorem)
- [`abs_hardyZ_sub_re_le`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/Zeros/HardyZ.lean#L271) (theorem)
- [`Zeta.RiemannSiegel.kernel_add_one`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/RiemannSiegel/Kernel.lean#L62) (theorem)
- [`Zeta.RiemannSiegel.kernel_add_one_sub_kernel`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/RiemannSiegel/Kernel.lean#L70) (theorem)
- [`Zeta.RiemannSiegel.tendsto_contourIntegral_atTop_nhds_riemannZeta_add_contourIntegral_half`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/RiemannSiegel/Siegel.lean#L50) (theorem)
- [`Zeta.RiemannSiegel.kernel_eq_tsum_of_im_neg`](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/Zeta/RiemannSiegel/Kernel.lean#L86) (theorem)

No file its headlines import, directly or not (38 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 346 .lean files; its Lean libraries `Zeta`, `Enclosure`, `Fast`, `Bernoulli`, `Native`, `NativeEval` and 1 more hold 346, declaring 2,340 names, with `sorry` in 55 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/smmercuri/zeta/blob/34037d5a7662e2eb6e970bfb22299c84e45ed5d9/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- [PrimeNumberTheoremAnd](../README.md) at `16a89862`, a GitHub fork of AlexKontorovich/PrimeNumberTheoremAnd.

## Placement

Its Lake manifest requires `PrimeNumberTheoremAnd`, a GitHub fork of AlexKontorovich/PrimeNumberTheoremAnd, whose modules 9 files of the project import.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (207 of 262 imports, 2.9×), General algebra (43 of 262 imports, 0.5×). *Proof depends on* lists 8 of the 59 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [smmercuri/zeta at 34037d5a](https://github.com/smmercuri/zeta/tree/34037d5a7662e2eb6e970bfb22299c84e45ed5d9)
