---
declaration: module
origin: cited
lean: Cedar, Cedar.SymCC, CedarFFI
statement: formalized
proof: formalized
---

# Cedar Specification

[cedar-policy/cedar-spec](https://github.com/cedar-policy/cedar-spec) at commit [cca421ef](https://github.com/cedar-policy/cedar-spec/tree/cca421ef3134f0d0141958aed03bac67752871eb), 2026-11-17.

> This repository contains the formalization of Cedar and infrastructure for performing differential randomized testing (DRT) between the formalization and Rust production implementation available in [`cedar`](https://github.com/cedar-policy/cedar).

*Quoted from [README.md](https://github.com/cedar-policy/cedar-spec/blob/cca421ef3134f0d0141958aed03bac67752871eb/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Cedar`](https://github.com/cedar-policy/cedar-spec/blob/cca421ef3134f0d0141958aed03bac67752871eb/cedar-lean/Cedar.lean), [`Cedar.SymCC`](https://github.com/cedar-policy/cedar-spec/blob/cca421ef3134f0d0141958aed03bac67752871eb/cedar-lean/Cedar/SymCC.lean), [`CedarFFI`](https://github.com/cedar-policy/cedar-spec/blob/cca421ef3134f0d0141958aed03bac67752871eb/cedar-lean/CedarFFI.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (387 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0.
- 388 .lean files; its Lean libraries `Cedar`, `SymCC`, `Cedar.SymCC`, `DiffTest`, `UnitTest`, `SymTest` and 3 more hold 387, declaring 5,374 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/cedar-policy/cedar-spec/blob/cca421ef3134f0d0141958aed03bac67752871eb/LICENSE)).

## Placement

It requires neither Mathlib nor another library mapped here; 21 files of the project import Batteries modules.

## Mathlib use

*Proof depends on* lists 5 of the 5 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [cedar-policy/cedar-spec at cca421ef](https://github.com/cedar-policy/cedar-spec/tree/cca421ef3134f0d0141958aed03bac67752871eb)
