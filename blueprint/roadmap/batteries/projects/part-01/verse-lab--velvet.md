---
declaration: module
origin: cited
lean: Velvet, Velvet.Examples
statement: formalized
proof: formalized
---

# velvet

*Velvet: A Multi-Modal Verifier for Imperative Programs in Lean*

[verse-lab/velvet](https://github.com/verse-lab/velvet) at commit [b2a349a5](https://github.com/verse-lab/velvet/tree/b2a349a57021b6d4e24ab403365b404db1ce7e08), 2026-11-05.

> Velvet is a Dafny-style verifier for imperative programs embedded in the Lean proof assistant. Velvet seamlessly combines SMT-inspired proof automation with Lean's interactive proof mode, enabling multi-modal verification: programs can be compiled, executed, validated using property-based testing, and formally verified within one unified environment.

*Quoted from [README.md](https://github.com/verse-lab/velvet/blob/b2a349a57021b6d4e24ab403365b404db1ce7e08/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Language](../../../mathlib/overview/logic-and-computation/formal-languages/language.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Set](../../../mathlib/overview/data-structures/sets/set.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Velvet`](https://github.com/verse-lab/velvet/blob/b2a349a57021b6d4e24ab403365b404db1ce7e08/Velvet.lean), [`Velvet.Examples`](https://github.com/verse-lab/velvet/blob/b2a349a57021b6d4e24ab403365b404db1ce7e08/Velvet/Examples.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (77 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0.
- 140 .lean files; its Lean libraries `Velvet`, `Examples` hold 78, declaring 453 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/verse-lab/velvet/blob/b2a349a57021b6d4e24ab403365b404db1ce7e08/LICENSE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* names 7 of the 7 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [verse-lab/velvet at b2a349a5](https://github.com/verse-lab/velvet/tree/b2a349a57021b6d4e24ab403365b404db1ce7e08)
