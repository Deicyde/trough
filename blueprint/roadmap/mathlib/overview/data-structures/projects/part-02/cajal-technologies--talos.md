---
declaration: module
origin: cited
lean: CodeLib, CodeLib.Examples.Gcd, CodeLib.Examples.MergeSort.StdIO
statement: formalized
proof: formalized
---

# Talos

[cajal-technologies/talos](https://github.com/cajal-technologies/talos) at commit [d7c84ac6](https://github.com/cajal-technologies/talos/tree/d7c84ac660757953b752bdfc9cb8dae3dab623ed), 2026-11-02.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Language](../../../logic-and-computation/formal-languages/language.md)
- [Module](../../../linear-algebra/fundamentals/module.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Array](../../list-like-structures/array.md)
- [Integer](../../../general-algebra/numbers/integer.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`CodeLib`](https://github.com/cajal-technologies/talos/blob/d7c84ac660757953b752bdfc9cb8dae3dab623ed/codelib/CodeLib.lean), [`CodeLib.Examples.Gcd`](https://github.com/cajal-technologies/talos/blob/d7c84ac660757953b752bdfc9cb8dae3dab623ed/codelib/CodeLib/Examples/Gcd.lean), [`CodeLib.Examples.MergeSort.StdIO`](https://github.com/cajal-technologies/talos/blob/d7c84ac660757953b752bdfc9cb8dae3dab623ed/codelib/CodeLib/Examples/MergeSort/StdIO.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (86 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 410 .lean files; its Lean libraries `CodeLib` hold 87, declaring 1,732 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License files: `LICENSE`; facts only.

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `iris` (https://github.com/leanprover-community/iris-lean.git) at `9a4ae0df`.
- `WasmInterpreterLean`.

## Placement

Of its imports of Mathlib modules in an overview area, 5 of 6 are in Data structures, 5.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (5 of 6 imports, 5.9×), General algebra (1 of 6 imports, 0.5×). *Proof depends on* lists 6 of the 6 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [cajal-technologies/talos at d7c84ac6](https://github.com/cajal-technologies/talos/tree/d7c84ac660757953b752bdfc9cb8dae3dab623ed)
