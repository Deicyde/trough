---
declaration: module
origin: cited
lean: Display, Examples.CDC, Examples.FPU
statement: formalized
---

# Sparkle HDL

[Verilean/sparkle](https://github.com/Verilean/sparkle) at commit [6c29b9b8](https://github.com/Verilean/sparkle/tree/6c29b9b8b4bed436afcc0a3f23a6335bfbc751a1), 2026-11-09.

> **Write hardware in Lean 4. Prove it correct. Generate Verilog.**

*Quoted from [README.md](https://github.com/Verilean/sparkle/blob/6c29b9b8b4bed436afcc0a3f23a6335bfbc751a1/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Ackermann function](../../../mathlib/overview/logic-and-computation/computability/ackermann-function.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Module](../../../mathlib/overview/linear-algebra/fundamentals/module.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Display`](https://github.com/Verilean/sparkle/blob/6c29b9b8b4bed436afcc0a3f23a6335bfbc751a1/docs/tutorial/Display.lean), [`Examples.CDC`](https://github.com/Verilean/sparkle/blob/6c29b9b8b4bed436afcc0a3f23a6335bfbc751a1/Examples/CDC.lean), [`Examples.FPU`](https://github.com/Verilean/sparkle/blob/6c29b9b8b4bed436afcc0a3f23a6335bfbc751a1/Examples/FPU.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Examples/FPU/Proofs.lean`, `Examples/FPU/Spec.lean`, `IP/BitNet/Spec/FixedPoint.lean`, `Tests/Ved/StrictAuditCheck.lean`, `Tools/DeepElab.lean`, `Tools/VedStrictAudit.lean`, `Tools/VerifyElab.lean` hold `sorry` or `admit`.

## Project

- Lean v4.32.1.
- 1,016 .lean files; its Lean libraries `Sparkle`, `IP.BitNet`, `IP.Drone`, `IP.Humanoid`, `IP.RV32`, `IP.YOLOv8` and 35 more hold 978, declaring 8,140 names, with `sorry` in 9 files and 4 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Verilean/sparkle/blob/6c29b9b8b4bed436afcc0a3f23a6335bfbc751a1/LICENSE)).

## Builds on

- `LSpec` (https://github.com/argumentcomputer/LSpec) at `3e23a4ad`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* names 7 of the 7 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Verilean/sparkle at 6c29b9b8](https://github.com/Verilean/sparkle/tree/6c29b9b8b4bed436afcc0a3f23a6335bfbc751a1)
