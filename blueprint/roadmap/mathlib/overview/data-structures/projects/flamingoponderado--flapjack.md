---
declaration: theorem
origin: cited
lean: Flapjack.Pancake.Proofs.PanToTarget.panToTargetCompileSemanticsArm8L3
statement: formalized
---

# Flapjack

[flamingoponderado/flapjack](https://github.com/flamingoponderado/flapjack) at commit [97910481](https://github.com/flamingoponderado/flapjack/tree/979104819b768f092f738e31ab563edcb0bd7e32), 2026-11-17.

> Flapjack is an in-progress Lean 4 port of the formally verified Pancake compiler.

*Quoted from [README.md](https://github.com/flamingoponderado/flapjack/blob/979104819b768f092f738e31ab563edcb0bd7e32/README.md), BSD-3-Clause, Copyright (c) 2026, Anthony Fox, Google LLC, Ramana Kumar, Magnus Myreen, Michael Norrish, Scott Owens, Yong Kiam Tan, and other contributors listed at https://cakeml.org.*

## Depends on

- [List](../list-like-structures/list.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Integer](../../general-algebra/numbers/integer.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)
- [Set](../sets/set.md)
- [Hash map](../maps/hash-map.md)
- [Array](../list-like-structures/array.md)
- [Multiset](../sets/multiset.md)
- [Finite set](../sets/finite-set.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Flapjack.Pancake.Proofs.PanToTarget.panToTargetCompileSemanticsArm8L3`](https://github.com/flamingoponderado/flapjack/blob/979104819b768f092f738e31ab563edcb0bd7e32/Flapjack/Pancake/Proofs/PanToTarget/Arm8L3Instance.lean#L47) (theorem)

Of the files its headlines import, directly or not, `Flapjack/Compiler/Backend/StackAlloc/Proofs/CodeThm/GenGcMoveLoop.lean` hold `sorry` or `admit`.

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 6,985 .lean files; its Lean libraries `Flapjack` hold 5,000 (the first read), declaring 35,247 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: BSD-3-Clause ([LICENSE](https://github.com/flamingoponderado/flapjack/blob/979104819b768f092f738e31ab563edcb0bd7e32/LICENSE)).

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- `ZirenDet` (https://github.com/ProjectZKM/Ziren) at `e08a9823`.

## Placement

Of its imports of Mathlib modules in an overview area, 166 of 201 are in Data structures, 5.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (166 of 201 imports, 5.8×), General algebra (28 of 201 imports, 0.4×). *Proof depends on* names 8 of the 10 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [flamingoponderado/flapjack at 97910481](https://github.com/flamingoponderado/flapjack/tree/979104819b768f092f738e31ab563edcb0bd7e32)
