---
declaration: theorem
origin: cited
lean: Goldbach.chen_theorem
statement: formalized
proof: formalized
---

# goldbach-lean

[subfish-zhou/goldbach-lean](https://github.com/subfish-zhou/goldbach-lean) at commit [9d4c3a40](https://github.com/subfish-zhou/goldbach-lean/tree/9d4c3a4010d42aedd9e7231bf94386019cfffccc), 2026-10-28.

> A Lean 4 project formalizing progress toward **Goldbach's conjecture** and building reusable analytic number theory, with **Chen's 1+2 theorem** and **Li–Liu's 1+1.9 theorem** formalized. The separate [Wu04/Wu08 development](research/wu2008/README.md) derives **1+1.8938**; its full source build, statement and axiom checks, and final module kernel replay have passed.

*Quoted from [README.md](https://github.com/subfish-zhou/goldbach-lean/blob/9d4c3a4010d42aedd9e7231bf94386019cfffccc/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Arithmetic functions](../../../general-algebra/number-theory/arithmetic-functions.md)
- [Mellin inversion theorem](../../../../thousand-plus/analysis/30-functions-of-a-complex-variable/mellin-inversion-theorem.md)
- [Bezout’s Theorem](../../../../hundred-theorems/part-03/bezouts-theorem.md)
- [Euler's totient function ($\varphi$)](../../../general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [Logarithm](../../special-functions/logarithm.md)
- [Integration by parts](../../../../undergraduate/single-variable-real-analysis/integration/integration-by-parts.md)
- [Leibniz formula (Single Variable Real Analysis)](../../../../undergraduate/single-variable-real-analysis/differentiability/leibniz-formula.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Goldbach.chen_theorem`](https://github.com/subfish-zhou/goldbach-lean/blob/9d4c3a4010d42aedd9e7231bf94386019cfffccc/Goldbach/Theorem.lean#L15) (theorem)

No file its headlines import, directly or not (528 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0-rc1, Mathlib at [e4c91783](https://github.com/leanprover-community/mathlib4/tree/e4c91783ca8e6a7c693ae624ade32fd22d4e43c1).
- 7,347 .lean files; its Lean libraries `PrimeNumberTheoremAnd`, `AnalyticNumberTheory`, `MathlibNt`, `Goldbach` hold 1,803, declaring 9,617 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/subfish-zhou/goldbach-lean/blob/9d4c3a4010d42aedd9e7231bf94386019cfffccc/LICENSE)).

## Builds on

- Mathlib, at [e4c91783](https://github.com/leanprover-community/mathlib4/tree/e4c91783ca8e6a7c693ae624ade32fd22d4e43c1).

## Placement

Of its imports of Mathlib modules in an overview area, 218 of 462 are in Analysis, 1.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (218 of 462 imports, 1.7×), General algebra (188 of 462 imports, 1.1×). *Proof depends on* names 8 of the 79 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [subfish-zhou/goldbach-lean at 9d4c3a40](https://github.com/subfish-zhou/goldbach-lean/tree/9d4c3a4010d42aedd9e7231bf94386019cfffccc)
