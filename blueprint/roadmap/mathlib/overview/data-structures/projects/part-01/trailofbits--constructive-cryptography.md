---
declaration: module
origin: cited
lean: Commons, ConstructiveCryptography, Probability
statement: formalized
proof: formalized
---

# Constructive Cryptography on Random Systems

[trailofbits/constructive-cryptography](https://github.com/trailofbits/constructive-cryptography) at commit [5a280a80](https://github.com/trailofbits/constructive-cryptography/tree/5a280a800529d839aa38ddbb43460473be62f5bb), 2026-11-14.

> This repository formalizes Constructive Cryptography [1, 2] in Lean 4. The framework is instantiated on a theory of random systems [3, 4] in which a system answers exactly on a declared domain of input histories, and a converter may stop at random. The classes of the framework are assumptions; their instances on interfaces take every field from the typed systems and typed converters of the random-systems library. The algebra of typed systems and converters is also stated in category-theoretic terms; a categorical model of composable security is given in [7].

*Quoted from [README.md](https://github.com/trailofbits/constructive-cryptography/blob/5a280a800529d839aa38ddbb43460473be62f5bb/README.md), MIT, Copyright (c) 2026 Trail of Bits.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Distributions](../../../analysis/distribution-theory/distributions.md)
- [Monoidal category](../../../general-algebra/category-theory/monoidal-category.md)
- [Category](../../../general-algebra/category-theory/category.md)
- [Rupture field](../../../general-algebra/field-theory/rupture-field.md)
- [Euler's totient function ($\varphi$)](../../../general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)
- [List](../../list-like-structures/list.md)
- [Group action](../../../general-algebra/group-theory/part-01/group-action.md)
- [Lipschitz continuity](../../../topology/metric-spaces/lipschitz-continuity.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Commons`](https://github.com/trailofbits/constructive-cryptography/blob/5a280a800529d839aa38ddbb43460473be62f5bb/src/Commons.lean), [`ConstructiveCryptography`](https://github.com/trailofbits/constructive-cryptography/blob/5a280a800529d839aa38ddbb43460473be62f5bb/src/ConstructiveCryptography.lean), [`Probability`](https://github.com/trailofbits/constructive-cryptography/blob/5a280a800529d839aa38ddbb43460473be62f5bb/src/Probability.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (361 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 362 .lean files; its Lean libraries `Probability`, `RandomSystems`, `ConstructiveCryptography`, `Commons`, `Examples`, `Tests` hold 361, declaring 4,543 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/trailofbits/constructive-cryptography/blob/5a280a800529d839aa38ddbb43460473be62f5bb/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 41 of 107 are in Data structures, 2.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (41 of 107 imports, 2.7×), Combinatorics (12 of 107 imports, 2.6×), General algebra (41 of 107 imports, 1.1×). *Proof depends on* lists 8 of the 23 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [trailofbits/constructive-cryptography at 5a280a80](https://github.com/trailofbits/constructive-cryptography/tree/5a280a800529d839aa38ddbb43460473be62f5bb)
