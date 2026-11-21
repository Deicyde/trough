---
declaration: theorem
origin: cited
lean: FourColor.RealPlane.compactness_extension, FourColor.RealPlane.discretize_to_hypermap, FourColor.four_color_hypermap, FourColor.unavoidability, FourColor.exclude5, FourColor.exclude11, FourColor.theReducibility, FourColor.cfreducible_of_engine
statement: formalized
proof: formalized
---

# The Four Color Theorem in Lean 4

[RBarish-UTokyo/FourColorTheorem-Lean4](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4) at commit [20fa3459](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/tree/20fa34599f5189dd569d96dd22f306c94ab1c446), 2026-09-26.

> A Lean 4 + Mathlib port of Georges Gonthier's Coq/Rocq formal proof of the Four Color Theorem, [math-comp/fourcolor](https://github.com/math-comp/fourcolor) (ported from commit `c1d6b1cd5288bea4b067aac13cdde3c18dffe018`). It is written for the Palomar registry's standards: the proof may use only the axioms `propext`, `Classical.choice` and `Quot.sound`, and every computation in it is checked by the Lean kernel (`decide +kernel`, never `native_decide`).

*Quoted from [README.md](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/README.md), Apache-2.0.*

## Depends on

- [List](../../list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Order of an element](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Set](../../sets/set.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Array](../../list-like-structures/array.md)
- [Finite set](../../sets/finite-set.md)

## Main results

Its Lean names are 8 of the 92 theorems its README names in code:

- [`FourColor.RealPlane.compactness_extension`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/Finitize.lean#L777) (theorem)
- [`FourColor.RealPlane.discretize_to_hypermap`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/Discretize.lean#L682) (theorem)
- [`FourColor.four_color_hypermap`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/FourColorThm.lean#L41) (theorem)
- [`FourColor.unavoidability`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/Unavoidability.lean#L93) (theorem)
- [`FourColor.exclude5`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/Present/P5/Exclude.lean#L96) (theorem)
- [`FourColor.exclude11`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/Present/P11/Exclude.lean#L1249) (theorem)
- [`FourColor.theReducibility`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/Reducibility.lean#L1389) (theorem)
- [`FourColor.cfreducible_of_engine`](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/FourColor/CfReducible.lean#L82) (theorem)

No file its headlines import, directly or not (803 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 816 .lean files; its Lean libraries `FourColor`, `Challenge`, `Solution` hold 815, declaring 10,805 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/blob/20fa34599f5189dd569d96dd22f306c94ab1c446/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 11 of 26 are in Data structures, 3.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (11 of 26 imports, 3.0×), General algebra (13 of 26 imports, 1.4×). *Proof depends on* lists 6 of the 8 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [RBarish-UTokyo/FourColorTheorem-Lean4 at 20fa3459](https://github.com/RBarish-UTokyo/FourColorTheorem-Lean4/tree/20fa34599f5189dd569d96dd22f306c94ab1c446)
