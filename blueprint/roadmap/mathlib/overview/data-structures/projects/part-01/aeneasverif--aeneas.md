---
declaration: module
origin: cited
lean: Aeneas, AeneasMeta
statement: formalized
---

# Aeneas

[AeneasVerif/aeneas](https://github.com/AeneasVerif/aeneas) at commit [1dc8ad31](https://github.com/AeneasVerif/aeneas/tree/1dc8ad31b1b062a77c50e29144a6c7bba955fa09), 2026-11-14.

> Aeneas (pronunced [Eh-nee-as]) is a verification toolchain for Rust programs. It relies on a translation from Rust's MIR internal language to a pure lambda calculus. It is intended to be used in combination with [Charon](https://github.com/AeneasVerif/charon), which compiles Rust programs to an intermediate representation called LLBC. It currently has backends for [F\*](https://www.fstar-lang.org), [Coq](https://coq.inria.fr/), [HOL4](https://hol-theorem-prover.org/) and [LEAN](https://leanprover.github.io/).

*Quoted from [README.md](https://github.com/AeneasVerif/aeneas/blob/1dc8ad31b1b062a77c50e29144a6c7bba955fa09/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Hash map](../../maps/hash-map.md)
- [Array](../../list-like-structures/array.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Set](../../sets/set.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Aeneas`](https://github.com/AeneasVerif/aeneas/blob/1dc8ad31b1b062a77c50e29144a6c7bba955fa09/backends/lean/Aeneas.lean), [`AeneasMeta`](https://github.com/AeneasVerif/aeneas/blob/1dc8ad31b1b062a77c50e29144a6c7bba955fa09/backends/lean/AeneasMeta.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `backends/lean/Aeneas/Data/Range/DivRange/Basic.lean`, `backends/lean/Aeneas/Data/Range/DivRange/Lemmas.lean`, `backends/lean/Aeneas/Data/Range/MulRange/Basic.lean`, `backends/lean/Aeneas/Data/Range/MulRange/Lemmas.lean`, `backends/lean/Aeneas/Data/Range/SRRange/Basic.lean`, `backends/lean/Aeneas/Tactic/Step/StepStar.lean`, `backends/lean/Aeneas/Tactic/Step/Tests/IntroOutputsRecursion.lean`, `backends/lean/AeneasMeta/Utils.lean` hold `sorry` or `admit`.

## Project

- Lean v4.36.0-rc2, Mathlib at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).
- 418 .lean files; its Lean libraries `Aeneas`, `AeneasMeta` hold 272, declaring 3,810 names, with `sorry` in 8 files and 7 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE.md](https://github.com/AeneasVerif/aeneas/blob/1dc8ad31b1b062a77c50e29144a6c7bba955fa09/LICENSE.md)).

## Builds on

- Mathlib, at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).

## Placement

Of its imports of Mathlib modules in an overview area, 14 of 41 are in Data structures, 2.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (14 of 41 imports, 2.4×), General algebra (24 of 41 imports, 1.6×). *Proof depends on* names 7 of the 7 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AeneasVerif/aeneas at 1dc8ad31](https://github.com/AeneasVerif/aeneas/tree/1dc8ad31b1b062a77c50e29144a6c7bba955fa09)
