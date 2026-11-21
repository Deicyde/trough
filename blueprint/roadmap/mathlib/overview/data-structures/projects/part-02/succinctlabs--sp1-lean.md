---
declaration: theorem
origin: cited
lean: SP1Clean.Soundness.sp1_machine_soundness
statement: formalized
---

# sp1-lean

[succinctlabs/sp1-lean](https://github.com/succinctlabs/sp1-lean) at commit [512e944a](https://github.com/succinctlabs/sp1-lean/tree/512e944ab2a680593125265694dcbd9b058b4dcb), 2026-06-26.

## Depends on

- [Development](../part-01/verified-zkevm--clean.md)

## Proof depends on

- [List](../../list-like-structures/list.md)
- [Multiset](../../sets/multiset.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Array](../../list-like-structures/array.md)
- [Finite set](../../sets/finite-set.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`SP1Clean.Soundness.sp1_machine_soundness`](https://github.com/succinctlabs/sp1-lean/blob/512e944ab2a680593125265694dcbd9b058b4dcb/SP1Clean/Soundness/SP1GatedVm.lean#L299) (theorem)

Of the files its headlines import, directly or not, `SP1Clean/Soundness/SP1GatedVm.lean` hold `sorry` or `admit`.

## Project

- Lean v4.28.0, Mathlib at [8f9d9cff](https://github.com/leanprover-community/mathlib4/tree/8f9d9cff6bd728b17a24e163c9402775d9e6a365).
- 396 .lean files; its Lean libraries `SP1Clean`, `SP1Math`, `SP1Model`, `SP1Extracted`, `SP1FormalModel`, `SP1Native` and 2 more hold 394, declaring 2,771 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/succinctlabs/sp1-lean/blob/512e944ab2a680593125265694dcbd9b058b4dcb/LICENSE-APACHE)).

## Builds on

- Mathlib, at [8f9d9cff](https://github.com/leanprover-community/mathlib4/tree/8f9d9cff6bd728b17a24e163c9402775d9e6a365).
- [Clean](../part-01/verified-zkevm--clean.md) at `292b9cc3`.
- `LeanRV64D` (https://github.com/succinctlabs/sail-riscv-lean) at `b8186950`.
- `RISCV` (https://github.com/succinctlabs/riscv-lean) at `58725b8c`.

## Placement

Of its imports of Mathlib modules in an overview area, 59 of 64 are in Data structures, 6.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (59 of 64 imports, 6.5×). *Proof depends on* lists 7 of the 7 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [succinctlabs/sp1-lean at 512e944a](https://github.com/succinctlabs/sp1-lean/tree/512e944ab2a680593125265694dcbd9b058b4dcb)
