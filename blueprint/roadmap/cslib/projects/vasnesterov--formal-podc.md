---
declaration: module
origin: cited
lean: Papers, Podc
statement: formalized
---

# formalpodc: Lean 4 formalizations of PODC papers

[vasnesterov/formal_podc](https://github.com/vasnesterov/formal_podc) at commit [db6d4b9c](https://github.com/vasnesterov/formal_podc/tree/db6d4b9c4bfbb1c9cc1e9635b4d9ca3dd5dce40a), 2026-11-10.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [DFA](../../mathlib/overview/logic-and-computation/formal-languages/dfa.md)
- [Regular language](../../mathlib/overview/logic-and-computation/formal-languages/regular-language.md)
- [NFA](../../mathlib/overview/logic-and-computation/formal-languages/nfa.md)
- [Structure of finitely generated abelian groups](../../mathlib/overview/general-algebra/group-theory/part-02/structure-of-finitely-generated-abelian-groups.md)
- [Szpilrajn extension theorem](../../mathlib/thousand-plus/general-topics-history-and-foundations/szpilrajn-extension-theorem.md)
- [Hall's marriage theorem](../../mathlib/overview/combinatorics/transversals/halls-marriage-theorem.md)
- [Degree-sum formula](../../mathlib/overview/combinatorics/graph-theory/degree-sum-formula.md)
- [Strong pigeonhole principle](../../mathlib/overview/combinatorics/pigeonhole-principles/strong-pigeonhole-principle.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Papers`](https://github.com/vasnesterov/formal_podc/blob/db6d4b9c4bfbb1c9cc1e9635b4d9ca3dd5dce40a/Papers.lean), [`Podc`](https://github.com/vasnesterov/formal_podc/blob/db6d4b9c4bfbb1c9cc1e9635b4d9ca3dd5dce40a/Podc.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Papers/PODC2024/AnonymousCoverings/Model.lean`, `Papers/PODC2024/AnonymousCoverings/Snapshot.lean`, `Papers/PODC2024/AnonymousCoverings/WriteScan.lean`, `Podc/Computability/Distributed/MobileRobots/Model.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0-rc3, Mathlib at [9a6fbe02](https://github.com/leanprover-community/mathlib4/tree/9a6fbe02d04cd1f582eac50a8a4e34ad67582169).
- 3,977 .lean files; its Lean libraries `Podc`, `Papers` hold 3,977, declaring 81,273 names, with `sorry` in 4 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- No license file; facts only.

## Builds on

- Mathlib, at [9a6fbe02](https://github.com/leanprover-community/mathlib4/tree/9a6fbe02d04cd1f582eac50a8a4e34ad67582169).
- [cslib](../README.md) at `8357cd8a`, a GitHub fork of leanprover/cslib.

## Placement

Its Lake manifest requires `cslib`, a GitHub fork of leanprover/cslib.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Combinatorics (121 of 596 imports, 4.7×), Topology (70 of 596 imports, 1.6×), Data structures (128 of 596 imports, 1.5×). *Proof depends on* names 8 of the 101 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [vasnesterov/formal_podc at db6d4b9c](https://github.com/vasnesterov/formal_podc/tree/db6d4b9c4bfbb1c9cc1e9635b4d9ca3dd5dce40a)
