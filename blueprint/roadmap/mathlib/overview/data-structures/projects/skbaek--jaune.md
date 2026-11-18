---
declaration: theorem
origin: cited
lean: Examples.Arithmetic.result, Jaune.Bytes.sha256_eq_fips, Jaune.Bytes.keccak_eq_fips
statement: formalized
proof: formalized
---

# Jaune

[skbaek/jaune](https://github.com/skbaek/jaune) at commit [ba15f397](https://github.com/skbaek/jaune/tree/ba15f397195d9c73c89aec7bfc179e0f32a3e8dc), 2026-11-18.

> **[skbaek.github.io/jaune](https://skbaek.github.io/jaune/)** — the guided tour: claim, evidence, trust boundaries, roadmap. **[Blanc](https://github.com/skbaek/blanc)** ([site](https://skbaek.github.io/blanc/)) — the sibling project: a verification stack built on these semantics, which proves theorems about Ethereum bytecode as it is deployed and offers a native contract language with a verified compiler. It is Jaune's end-to-end case study.

*Quoted from [README.md](https://github.com/skbaek/jaune/blob/ba15f397195d9c73c89aec7bfc179e0f32a3e8dc/README.md), MIT, Copyright (c) 2025 skbaek.*

## Depends on

- [List](../list-like-structures/list.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Array](../list-like-structures/array.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Hash map](../maps/hash-map.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Examples.Arithmetic.result`](https://github.com/skbaek/jaune/blob/ba15f397195d9c73c89aec7bfc179e0f32a3e8dc/Examples/Arithmetic.lean#L192) (theorem)
- [`Jaune.Bytes.sha256_eq_fips`](https://github.com/skbaek/jaune/blob/ba15f397195d9c73c89aec7bfc179e0f32a3e8dc/Jaune/SHA256Spec.lean#L740) (theorem)
- [`Jaune.Bytes.keccak_eq_fips`](https://github.com/skbaek/jaune/blob/ba15f397195d9c73c89aec7bfc179e0f32a3e8dc/Jaune/KeccakSpec.lean#L962) (theorem)

No file its headlines import, directly or not (29 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 265 .lean files; its Lean libraries `Jaune`, `JauneChecks`, `Examples`, `Assurance`, `JauneConsensus`, `ConsensusAssurance` and 2 more hold 243, declaring 7,700 names, with `sorry` in 1 file and 3 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: MIT ([LICENSE](https://github.com/skbaek/jaune/blob/ba15f397195d9c73c89aec7bfc179e0f32a3e8dc/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 5 of 6 are in Data structures, 5.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (5 of 6 imports, 5.9×), General algebra (1 of 6 imports, 0.5×). *Proof depends on* names 3 of the 5 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [skbaek/jaune at ba15f397](https://github.com/skbaek/jaune/tree/ba15f397195d9c73c89aec7bfc179e0f32a3e8dc)
