---
declaration: theorem
origin: cited
lean: Math.Problems.TernaryGoldbach.ternary_goldbach_of_evidence, Math.Problems.TernaryGoldbach.ternary_goldbach_of_phala_evidence, Math.Problems.TernaryGoldbach.deficitProduct_compcert_run, Math.Problems.TernaryGoldbach.Axiomatized.ternary_goldbach, HeavyCertificates.ternary_goldbach_fullBuild
statement: formalized
---

# Ternary Goldbach in Lean 4

[gersh/ternary-goldbach-lean](https://github.com/gersh/ternary-goldbach-lean) at commit [27df23af](https://github.com/gersh/ternary-goldbach-lean/tree/27df23af6a712895f22204d0d81102baa74f0ebe), 2026-09-02.

> A Lean 4 formalization of the ternary (weak) Goldbach theorem: every odd integer at least seven is a sum of three primes.

*Quoted from [README.md](https://github.com/gersh/ternary-goldbach-lean/blob/27df23af6a712895f22204d0d81102baa74f0ebe/README.md), Apache-2.0.*

## Depends on

- [Integer](../../../general-algebra/numbers/integer.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Sum of a Geometric Series](../../../../hundred-theorems/part-03/sum-of-a-geometric-series.md)
- [Characterization of convexity](../../convexity/characterization-of-convexity.md)
- [Heine-Borel theorem (proper metric space version)](../../../topology/metric-spaces/heine-borel-theorem-proper-metric-space-version.md)
- [Euler's totient function ($\varphi$)](../../../general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Fourier transform on $\mathrm{L}^2(\R^d)$](../../../../undergraduate/measures-and-integral-calculus/fourier-analysis/fourier-transform-on-l-2-r-d.md)
- [Euler’s Summation of 1 + (1/2)^2 + (1/3)^2 + ….](../../../../hundred-theorems/part-01/eulers-summation-of-1-1-2-2-1-3-2.md)
- [Mellin inversion theorem](../../../../thousand-plus/analysis/30-functions-of-a-complex-variable/mellin-inversion-theorem.md)
- [Poisson’s formula](../../../../undergraduate/distribution-calculus/applications/poissons-formula.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Math.Problems.TernaryGoldbach.ternary_goldbach_of_evidence`](https://github.com/gersh/ternary-goldbach-lean/blob/27df23af6a712895f22204d0d81102baa74f0ebe/Math/Problems/TernaryGoldbach/PhalaEvidenceBoundary.lean#L182) (theorem)
- [`Math.Problems.TernaryGoldbach.ternary_goldbach_of_phala_evidence`](https://github.com/gersh/ternary-goldbach-lean/blob/27df23af6a712895f22204d0d81102baa74f0ebe/Math/Problems/TernaryGoldbach/PhalaEvidenceBoundary.lean#L190) (theorem)
- [`Math.Problems.TernaryGoldbach.deficitProduct_compcert_run`](https://github.com/gersh/ternary-goldbach-lean/blob/27df23af6a712895f22204d0d81102baa74f0ebe/Math/Problems/TernaryGoldbach/Certs/SingularSeriesDeficitProdTwoMillionCert.lean#L114) (theorem)
- [`Math.Problems.TernaryGoldbach.Axiomatized.ternary_goldbach`](https://github.com/gersh/ternary-goldbach-lean/blob/27df23af6a712895f22204d0d81102baa74f0ebe/Math/Problems/TernaryGoldbach/Axiomatized/Statement.lean#L40) (theorem)
- [`HeavyCertificates.ternary_goldbach_fullBuild`](https://github.com/gersh/ternary-goldbach-lean/blob/27df23af6a712895f22204d0d81102baa74f0ebe/HeavyCertificates/TGFiniteCertificatesFull.lean#L70) (theorem)

## Project

- Lean v4.32.1, Mathlib at [520045ab](https://github.com/leanprover-community/mathlib4/tree/520045ab14e26149ee970e2e617ca04b09bde5d6).
- 16,266 .lean files; its Lean libraries `Math`, `HeavyCertificates`, `TernaryCerts`, `Ch25A7BoundaryCert`, `Section413KernelCert`, `MathExtras` and 1 more hold 5,000 (the first read), declaring 37,520 names, with `sorry` in 0 files and 134 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/gersh/ternary-goldbach-lean/blob/27df23af6a712895f22204d0d81102baa74f0ebe/LICENSE)).

## Builds on

- Mathlib, at [520045ab](https://github.com/leanprover-community/mathlib4/tree/520045ab14e26149ee970e2e617ca04b09bde5d6).
- `analytic_nt`.
- `attested_compcert_bridge`.
- `ch25_certificates`.
- `complex_compute`.
- `effective_asymptotics`.
- `fixed_transcendental`.
- `helfgott_certificates`.
- `interval_arith`.
- `kernel_certificates`.
- `leancert` (https://github.com/alerad/leancert) at `121ecfdf`.
- `leancompcert` (https://github.com/gersh/leancompcert.git) at `b430fc71`.
- `parabolic_cylinder`.
- `PrimeNumberTheoremAnd`.
- `quadrature_engine`.
- `rs62_certificates`.
- `saddle_point`.
- `SparkInterval` (https://github.com/gersh/attested-compute.git) at `02846206`.
- `ternary_certificates`.
- `tg_native_certificates`.

## Placement

Of its imports of Mathlib modules in an overview area, 606 of 946 are in Analysis, 2.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (606 of 946 imports, 2.4×), General algebra (276 of 946 imports, 0.8×). *Proof depends on* names 8 of the 93 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [gersh/ternary-goldbach-lean at 27df23af](https://github.com/gersh/ternary-goldbach-lean/tree/27df23af6a712895f22204d0d81102baa74f0ebe)
