---
declaration: module
origin: cited
lean: AKS, Random.Cert
statement: formalized
---

# AKS sorting network — Lean formalisation

[girving/aks](https://github.com/girving/aks) at commit [c7fb62ed](https://github.com/girving/aks/tree/c7fb62ed80a4a610f87f34db0082cadbd7c00c9f), 2026-03-19.

> A formal verification of the Ajtai–Komlós–Szemerédi (1983) `O(n log n)` sorting network construction in [Lean 4](https://lean-lang.org/) with [Mathlib](https://github.com/leanprover-community/mathlib4), using the Seiferas (2009) separator-based correctness proof and the Margulis–Gabber–Galil (1973/1981) expander. All code and proofs were written by Claude Code + Claude Opus 4.6, with extensive human hand-holding throughout.

*Quoted from [README.md](https://github.com/girving/aks/blob/c7fb62ed80a4a610f87f34db0082cadbd7c00c9f/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Self-adjoint operator](../../../analysis/hilbert-spaces/self-adjoint-operator.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Finite set](../../../data-structures/sets/finite-set.md)
- [Ring-valued matrix](../../matrices/ring-valued-matrix.md)
- [Array](../../../data-structures/list-like-structures/array.md)
- [List](../../../data-structures/list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`AKS`](https://github.com/girving/aks/blob/c7fb62ed80a4a610f87f34db0082cadbd7c00c9f/AKS.lean), [`Random.Cert`](https://github.com/girving/aks/blob/c7fb62ed80a4a610f87f34db0082cadbd7c00c9f/Random/Cert.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.29.0-rc4, Mathlib at [294b7c26](https://github.com/leanprover-community/mathlib4/tree/294b7c26a7cac74c34b43ddace82c85ebff331b1).
- 116 .lean files; its Lean libraries `RandomCert`, `RandomBridge`, `RandomConcrete`, `RandomMisc`, `RandomBench`, `AKS` and 1 more hold 116, declaring 1,362 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/girving/aks/blob/c7fb62ed80a4a610f87f34db0082cadbd7c00c9f/LICENSE)).

## Builds on

- Mathlib, at [294b7c26](https://github.com/leanprover-community/mathlib4/tree/294b7c26a7cac74c34b43ddace82c85ebff331b1).

## Placement

Of its imports of Mathlib modules in an overview area, 8 of 43 are in Linear algebra, 3.2 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (8 of 43 imports, 3.2×), Data structures (9 of 43 imports, 1.5×), Analysis (9 of 43 imports, 0.8×). *Proof depends on* lists 8 of the 13 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [girving/aks at c7fb62ed](https://github.com/girving/aks/tree/c7fb62ed80a4a610f87f34db0082cadbd7c00c9f)
