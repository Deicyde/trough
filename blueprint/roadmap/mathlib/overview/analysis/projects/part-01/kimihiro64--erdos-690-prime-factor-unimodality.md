---
declaration: theorem
origin: cited
lean: PrimeFactorUnimodality.completeClassification_elementary
statement: formalized
---

# Erdos 690: Prime-Factor Density Unimodality

[kimihiro64/erdos-690-prime-factor-unimodality](https://github.com/kimihiro64/erdos-690-prime-factor-unimodality) at commit [e4d234d4](https://github.com/kimihiro64/erdos-690-prime-factor-unimodality/tree/e4d234d4fe2e75fe1de504e9cd47709f75dcc11d), 2026-11-09.

> An unconditional Lean 4 proof of the complete classification: for every positive integer `k`, the density of the `k`th smallest distinct prime divisor is unimodal precisely when `k <= 3`.

*Quoted from [README.md](https://github.com/kimihiro64/erdos-690-prime-factor-unimodality/blob/e4d234d4fe2e75fe1de504e9cd47709f75dcc11d/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Continuity of integrals with respect to parameters](../../../../undergraduate/measures-and-integral-calculus/integration/continuity-of-integrals-with-respect-to-paramete.md)
- [Bochner integral](../../measures-and-integral-calculus/part-01/bochner-integral.md)
- [The Infinitude of Primes](../../../../hundred-theorems/part-01/the-infinitude-of-primes.md)
- [Integration by parts](../../../../undergraduate/single-variable-real-analysis/integration/integration-by-parts.md)
- [Rational number](../../../general-algebra/numbers/rational-number.md)
- [Complex number](../../../general-algebra/numbers/complex-number.md)
- [Real number](../../../general-algebra/numbers/real-number.md)
- [Logarithm](../../special-functions/logarithm.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`PrimeFactorUnimodality.completeClassification_elementary`](https://github.com/kimihiro64/erdos-690-prime-factor-unimodality/blob/e4d234d4fe2e75fe1de504e9cd47709f75dcc11d/PrimeFactorUnimodality/Proof/CompleteClassificationElementary.lean#L17) (theorem)

## Project

- Lean v4.34.0, Mathlib at [5ed29652](https://github.com/leanprover-community/mathlib4/tree/5ed2965256430c3649e86755f9576b54eca72435).
- 6,256 .lean files; its Lean libraries `PrimeFactorUnimodality`, `PrimeNumberTheoremAnd`, `VendorPrimeNumberTheoremAnd`, `Challenge`, `Solution`, `Submission` hold 5,000 (the first read), declaring 38,997 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/kimihiro64/erdos-690-prime-factor-unimodality/blob/e4d234d4fe2e75fe1de504e9cd47709f75dcc11d/LICENSE)).

## Builds on

- Mathlib, at [5ed29652](https://github.com/leanprover-community/mathlib4/tree/5ed2965256430c3649e86755f9576b54eca72435).

## Placement

Of its imports of Mathlib modules in an overview area, 207 of 391 are in Analysis, 2.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (207 of 391 imports, 2.0×), General algebra (142 of 391 imports, 1.0×). *Proof depends on* lists 8 of the 59 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [kimihiro64/erdos-690-prime-factor-unimodality at e4d234d4](https://github.com/kimihiro64/erdos-690-prime-factor-unimodality/tree/e4d234d4fe2e75fe1de504e9cd47709f75dcc11d)
