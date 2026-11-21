---
declaration: module
origin: cited
lean: AcceptedRestrictions, ActivePools, AllWeightSectorAllocation
statement: formalized
---

# Matrix multiplication bounds: Lean formalization

[olliepro/LeanMMBound](https://github.com/olliepro/LeanMMBound) at commit [93492a4d](https://github.com/olliepro/LeanMMBound/tree/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55), 2026-10-06.

> **Paper: [Cross-Level Laser Extraction for Faster Matrix Multiplication](https://github.com/olliepro/LeanMMBound/blob/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55/paper/matrix-multiplication-exponent.pdf)** — LaTeX source in [`paper/`](https://github.com/olliepro/LeanMMBound/blob/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55/paper).

*Quoted from [README.md](https://github.com/olliepro/LeanMMBound/blob/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Behrend's construction](../additive-combinatorics/behrends-construction.md)
- [Sets without arithmetic progressions](../additive-combinatorics/sets-without-arithmetic-progressions.md)
- [List](../../data-structures/list-like-structures/list.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Group action](../../general-algebra/group-theory/part-01/group-action.md)
- [Exponential](../../analysis/special-functions/exponential.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`AcceptedRestrictions`](https://github.com/olliepro/LeanMMBound/blob/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55/src/AcceptedRestrictions.lean), [`ActivePools`](https://github.com/olliepro/LeanMMBound/blob/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55/src/ActivePools.lean), [`AllWeightSectorAllocation`](https://github.com/olliepro/LeanMMBound/blob/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55/src/AllWeightSectorAllocation.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 2,173 .lean files; its Lean libraries `Challenge`, `Solution`, `MatrixBounds` hold 2,173, declaring 34,469 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/olliepro/LeanMMBound/blob/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 20 of 105 are in Combinatorics, 4.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Combinatorics (20 of 105 imports, 4.4×), General algebra (51 of 105 imports, 1.4×), Data structures (17 of 105 imports, 1.1×). *Proof depends on* lists 8 of the 18 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [olliepro/LeanMMBound at 93492a4d](https://github.com/olliepro/LeanMMBound/tree/93492a4dd1ee90fd98cd7b339af77bb8bbc8be55)
