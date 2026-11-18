---
declaration: theorem
origin: cited
lean: LeanTrominoes.PeriodicCNF.PolySpaceHardness.localPeriodicCNF1DSAT_PSPACEComplete, LeanTrominoes.PeriodicCNF.PolySpaceHardness.localPeriodicThreeCNF1DSAT_PSPACEComplete, LeanTrominoes.PeriodicGridDrawing.Arithmetic.isContinuouslyPlanar_inPSPACE, LeanTrominoes.PeriodicCNF.LineWindow.state_bits_le_encoding, LeanTrominoes.PeriodicCNF.LineWindow.check_localPeriodicCNF1DSAT, LeanTrominoes.PeriodicCNFDimensions.satisfiable_coREComplete, LeanTrominoes.PeriodicCNFDimensions.localProblem_coREComplete, LeanTrominoes.Gadget.NormalizedOrientation.coREComplete
statement: formalized
---

# lean-trominoes

[edemaine/lean-trominoes](https://github.com/edemaine/lean-trominoes) at commit [6d5b36c1](https://github.com/edemaine/lean-trominoes/tree/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332), 2026-10-20.

> Lean formalization of [*Undecidability of Tiling with a Tromino*](https://arxiv.org/abs/2509.07906) by the MIT--ULB CompGeom Group, Zachary Abel, Hugo Akitaya, Lily Chung, Erik D. Demaine, Jenny Diomidova, Della Hendrickson, Stefan Langerman, and Jayson Lynch. The working paper is included as [PDF](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/trominoes.pdf) and [source](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/trominoes.texlish). Use the checked-in source as the reference for theorem statements and proofs in this formalization.

*Quoted from [README.md](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/README.md), Apache-2.0.*

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [In terms of Turing machines](../../logic-and-computation/computability/computable-function/in-terms-of-turing-machines.md)
- [Polynomial-time computation](../../logic-and-computation/complexity/polynomial-time-computation.md)
- [Primitive recursive function](../../logic-and-computation/computability/primitive-recursive-function.md)
- [In terms of general recursive functions](../../logic-and-computation/computability/computable-function/in-terms-of-general-recursive-functions.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Cramer’s Rule](../../../hundred-theorems/part-04/cramers-rule.md)
- [List](../list-like-structures/list.md)
- [Representation](../../general-algebra/representation-theory/representation.md)

## Main results

Its Lean names are 8 of the 44 theorems its README names in code:

- [`LeanTrominoes.PeriodicCNF.PolySpaceHardness.localPeriodicCNF1DSAT_PSPACEComplete`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/SAT/CNF/PeriodicCNFPolySpaceMembership.lean#L33) (theorem)
- [`LeanTrominoes.PeriodicCNF.PolySpaceHardness.localPeriodicThreeCNF1DSAT_PSPACEComplete`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/SAT/CNF/PeriodicCNFFieldWidth.lean#L109) (theorem)
- [`LeanTrominoes.PeriodicGridDrawing.Arithmetic.isContinuouslyPlanar_inPSPACE`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/Graphs/Drawings/Grid/PeriodicDrawingPolySpaceVerification.lean#L59) (theorem)
- [`LeanTrominoes.PeriodicCNF.LineWindow.state_bits_le_encoding`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/SAT/CNF/PeriodicCNFLineSearch.lean#L77) (theorem)
- [`LeanTrominoes.PeriodicCNF.LineWindow.check_localPeriodicCNF1DSAT`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/SAT/CNF/PeriodicCNFLineSearch.lean#L51) (theorem)
- [`LeanTrominoes.PeriodicCNFDimensions.satisfiable_coREComplete`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/SAT/CNF/PeriodicCNFDimensions.lean#L113) (theorem)
- [`LeanTrominoes.PeriodicCNFDimensions.localProblem_coREComplete`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/SAT/CNF/PeriodicCNFDimensions.lean#L118) (theorem)
- [`LeanTrominoes.Gadget.NormalizedOrientation.coREComplete`](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LeanTrominoes/Graphs/Orientation/NormalizedOrientationCompleteness.lean#L54) (theorem)

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 10,088 .lean files; its Lean libraries `LeanTrominoes` hold 5,000 (the first read), declaring 28,107 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/edemaine/lean-trominoes/blob/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `lean_wang` (https://github.com/edemaine/lean-wang) at `64268a3a`.

## Placement

Of its imports of Mathlib modules in an overview area, 163 of 250 are in Data structures, 4.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (163 of 250 imports, 4.6×), General algebra (42 of 250 imports, 0.5×). *Proof depends on* names 8 of the 27 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [edemaine/lean-trominoes at 6d5b36c1](https://github.com/edemaine/lean-trominoes/tree/6d5b36c15cec6cb18d30137b7f1c7fb92ea24332)
