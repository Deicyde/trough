---
declaration: theorem
origin: cited
lean: GraphIso.GensData.AllValid.cons
statement: formalized
proof: formalized
---

# Graph isomorphism in quasipolynomial time, in Lean

[troyjlee/graph-iso-lean](https://github.com/troyjlee/graph-iso-lean) at commit [70d55e26](https://github.com/troyjlee/graph-iso-lean/tree/70d55e26b7fbf8a8725b5faf65c3372a2aa5c26a), 2026-10-29.

> A Lean 4 and Mathlib formalization of Babai's quasipolynomial-time algorithm for graph isomorphism, without the classification of finite simple groups, ending in a statement about single-tape Turing machines. The algorithm, its correctness and its running time are proved in Lean, and the machine that runs it is built from the formalized algorithm.

*Quoted from [README.md](https://github.com/troyjlee/graph-iso-lean/blob/70d55e26b7fbf8a8725b5faf65c3372a2aa5c26a/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Turing machine](../../../logic-and-computation/computability/turing-machine.md)
- [Schreier's lemma](../../../general-algebra/group-theory/part-01/schreiers-lemma.md)
- [Alternating group](../../../general-algebra/group-theory/part-02/alternating-group.md)
- [Alternating groups on 5 letters or more are simple](../../../general-algebra/group-theory/part-02/alternating-groups-on-5-letters-or-more-are-simp.md)
- [Orbit](../../../../undergraduate/group-theory/basic-definitions/orbit.md)
- [Second isomorphism theorem](../../../general-algebra/group-theory/part-01/second-isomorphism-theorem.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Group action](../../../general-algebra/group-theory/part-01/group-action.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`GraphIso.GensData.AllValid.cons`](https://github.com/troyjlee/graph-iso-lean/blob/70d55e26b7fbf8a8725b5faf65c3372a2aa5c26a/lean/GraphIso/Representation/Group.lean#L42) (theorem)

No file its headlines import, directly or not (4 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 430 .lean files; its Lean libraries `GraphIso`, `GraphIsoChecks`, `Challenge`, `Solution` hold 430, declaring 12,172 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/troyjlee/graph-iso-lean/blob/70d55e26b7fbf8a8725b5faf65c3372a2aa5c26a/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 115 of 334 are in Data structures, 2.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (115 of 334 imports, 2.4×), General algebra (182 of 334 imports, 1.5×). *Proof depends on* names 8 of the 35 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [troyjlee/graph-iso-lean at 70d55e26](https://github.com/troyjlee/graph-iso-lean/tree/70d55e26b7fbf8a8725b5faf65c3372a2aa5c26a)
