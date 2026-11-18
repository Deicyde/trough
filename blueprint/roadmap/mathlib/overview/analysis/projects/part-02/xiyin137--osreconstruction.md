---
declaration: theorem
origin: cited
lean: os_to_wightman, os_to_wightman_osii_original, OSReconstruction.wightman_to_os_axioms, OSFixedOrderGrowthCondition.sobolev_index_eq_zero
statement: formalized
proof: formalized
---

# OSReconstruction

[xiyin137/OSreconstruction](https://github.com/xiyin137/OSreconstruction) at commit [cf0904e3](https://github.com/xiyin137/OSreconstruction/tree/cf0904e34a7c146a9f312f601e3707dca4a87697), 2026-11-03.

> A Lean 4 formalization of the **Osterwalder-Schrader reconstruction theorem**, built on [Mathlib](https://github.com/leanprover-community/mathlib4).

*Quoted from [README.md](https://github.com/xiyin137/OSreconstruction/blob/cf0904e34a7c146a9f312f601e3707dca4a87697/README.md), Apache-2.0.*

## Depends on

- [Complex number](../../../general-algebra/numbers/complex-number.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Baire theorem](../../../topology/metric-spaces/baire-theorem.md)
- [Morera's theorem](../../../../thousand-plus/analysis/30-functions-of-a-complex-variable/moreras-theorem.md)
- [Fourier transforms on $\mathcal{S}(\R^d)$](../../../../undergraduate/distribution-calculus/spaces-s-r-d/fourier-transforms-on-s-r-d.md)
- [Inverse Fourier transform](../../../../undergraduate/distribution-calculus/tempered-distributions/inverse-fourier-transform.md)
- [Stability by derivation](../../../../undergraduate/distribution-calculus/spaces-s-r-d/stability-by-derivation.md)
- [Hahn-Banach theorem](../../normed-vector-spaces-banach-spaces/hahn-banach-theorem.md)
- [Convolution of two functions of $\mathcal{S}(\R^d)$](../../../../undergraduate/distribution-calculus/spaces-s-r-d/convolution-of-two-functions-of-s-r-d.md)
- [Schwartz space](../../distribution-theory/schwartz-space.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`os_to_wightman`](https://github.com/xiyin137/OSreconstruction/blob/cf0904e34a7c146a9f312f601e3707dca4a87697/os-reconstruction/OSReconstruction/Wightman/Reconstruction/Main.lean#L30) (theorem)
- [`os_to_wightman_osii_original`](https://github.com/xiyin137/OSreconstruction/blob/cf0904e34a7c146a9f312f601e3707dca4a87697/os-reconstruction/OSReconstruction/Wightman/Reconstruction/WickRotation/OSIIQuantitativeEndpoint.lean#L67) (theorem)
- [`OSReconstruction.wightman_to_os_axioms`](https://github.com/xiyin137/OSreconstruction/blob/cf0904e34a7c146a9f312f601e3707dca4a87697/os-reconstruction/OSReconstruction/Wightman/Reconstruction/WickRotation/RToEReconstruction.lean#L57) (theorem)
- [`OSFixedOrderGrowthCondition.sobolev_index_eq_zero`](https://github.com/xiyin137/OSreconstruction/blob/cf0904e34a7c146a9f312f601e3707dca4a87697/os-reconstruction/OSReconstruction/Wightman/Reconstruction/WickRotation/deprecated/OSFixedOrderGrowth.lean#L33) (theorem)

No file its headlines import, directly or not (847 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc4, Mathlib at [1f414401](https://github.com/leanprover-community/mathlib4/tree/1f414401f69059aa7eead47b53ee40bd38455eeb).
- 855 .lean files; its Lean libraries `OSReconstruction`, `ComparatorAudit` hold 854, declaring 11,628 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/xiyin137/OSreconstruction/blob/cf0904e34a7c146a9f312f601e3707dca4a87697/LICENSE)).

## Builds on

- Mathlib, at [1f414401](https://github.com/leanprover-community/mathlib4/tree/1f414401f69059aa7eead47b53ee40bd38455eeb).
- `GaussianField` (https://github.com/mrdouglasny/gaussian-field.git) at `e28a3812`.

## Placement

Of its imports of Mathlib modules in an overview area, 565 of 798 are in Analysis, 2.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (565 of 798 imports, 2.6×), Topology (89 of 798 imports, 1.5×). *Proof depends on* names 8 of the 116 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [xiyin137/OSreconstruction at cf0904e3](https://github.com/xiyin137/OSreconstruction/tree/cf0904e34a7c146a9f312f601e3707dca4a87697)
