---
declaration: theorem
origin: cited
lean: Vsa.Sim.EndToEnd.endToEnd_refinement, Vsa.Sim.EndToEnd.endToEnd_refinement_loaded, Vsa.Sim.EndToEnd.endToEnd_trichotomy, Vsa.While.bigStep_not_err, Vsa.While.bigStep_not_diverges, Vsa.While.err_not_diverges, Vsa.Sim.Boot.proofElf_halts, Vsa.While.Types.preservation
statement: formalized
proof: formalized
---

# Ship your interpreter

[BasisResearch/ship-your-interpreter](https://github.com/BasisResearch/ship-your-interpreter) at commit [fb07094c](https://github.com/BasisResearch/ship-your-interpreter/tree/fb07094cff916318c34b07494a7d739f1e53989b), 2026-10-01.

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)

## Main results

Its Lean names are 8 of the 30 theorems its README names in code:

- [`Vsa.Sim.EndToEnd.endToEnd_refinement`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/VsaIris/Interp/EndToEnd.lean#L159) (theorem)
- [`Vsa.Sim.EndToEnd.endToEnd_refinement_loaded`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/VsaIris/Interp/EndToEnd.lean#L153) (theorem)
- [`Vsa.Sim.EndToEnd.endToEnd_trichotomy`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/VsaIris/Interp/EndToEndTrichotomy.lean#L61) (theorem)
- [`Vsa.While.bigStep_not_err`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/Vsa/While/Exclusive.lean#L1476) (theorem)
- [`Vsa.While.bigStep_not_diverges`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/Vsa/While/Exclusive.lean#L1483) (theorem)
- [`Vsa.While.err_not_diverges`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/Vsa/While/Exclusive.lean#L1491) (theorem)
- [`Vsa.Sim.Boot.proofElf_halts`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/Vsa/Sim/Boot/EndToEnd.lean#L14) (theorem)
- [`Vsa.While.Types.preservation`](https://github.com/BasisResearch/ship-your-interpreter/blob/fb07094cff916318c34b07494a7d739f1e53989b/Vsa/While/TypePreservation.lean#L158) (theorem)

No file its headlines import, directly or not (661 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0.
- 1,113 .lean files; its Lean libraries `Vsa`, `VsaIris`, `VsaBoot` hold 819, declaring 11,276 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- No license file; facts only.

## Builds on

- `iris` (https://github.com/leanprover-community/iris-lean) at `740e2c4a`.
- `«lean-riscv»`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* lists 5 of the 5 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [BasisResearch/ship-your-interpreter at fb07094c](https://github.com/BasisResearch/ship-your-interpreter/tree/fb07094cff916318c34b07494a7d739f1e53989b)
