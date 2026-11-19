---
declaration: theorem
origin: cited
lean: ConLeche.main_no_False, ConLeche.main_oleans_no_False
statement: formalized
---

# con-agua

*con-agua – A Lean checker verified at the assembly level*

[leanprover/con-agua](https://github.com/leanprover/con-agua) at commit [22f93860](https://github.com/leanprover/con-agua/tree/22f938604abefbee97913e89745530fb37502ba7), 2026-11-16.

## Depends on

- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)

## Proof depends on

- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Closure](../../../mathlib/overview/topology/general-topology/part-01/closure.md)
- [Field](../../../mathlib/overview/general-algebra/field-theory/field.md)

## Main results

Its Lean names are the theorems of its top-level module named Main, MainTheorem(s) or Statement(s):

- [`ConLeche.main_no_False`](https://github.com/leanprover/con-agua/blob/22f938604abefbee97913e89745530fb37502ba7/vendor/con-leche/ConLeche/MainTheorem.lean#L152) (theorem)
- [`ConLeche.main_oleans_no_False`](https://github.com/leanprover/con-agua/blob/22f938604abefbee97913e89745530fb37502ba7/vendor/con-leche/ConLeche/MainTheorem.lean#L166) (theorem)

Of the files its headlines import, directly or not, `vendor/con-leche/ConLeche/Driver/OwnerParse.lean`, `vendor/con-leche/ConLeche/Frontend/Stream.lean` hold `sorry` or `admit`.

## Project

- Lean nightly-2026-10-20.
- 2,489 .lean files; its Lean libraries `ConAgua`, `ConAguaAsm`, `ConLeche`, `ConRonArena`, `ConRonBridge` hold 2,284, declaring 41,982 names, with `sorry` in 8 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License files: `LICENSE`; facts only.

## Builds on

- `Kraken` (https://github.com/sgraf812/kraken) at `ba128349`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* names 6 of the 7 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [leanprover/con-agua at 22f93860](https://github.com/leanprover/con-agua/tree/22f938604abefbee97913e89745530fb37502ba7)
