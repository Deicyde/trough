---
declaration: theorem
origin: cited
lean: Demos.Gpt.Exact.steps_exact, Demos.Gpt.Causal.forward_causal, Demos.Euler.Verified.euler_solve_call, Demos.Drone.Verified.drone_compute, Demos.Drone.Verified.drone_safe, Demos.Slew.Safety.plan_safe, Demos.Slew.Optimal.plan_optimal, Demos.Conjunction.pc_enclosure
statement: formalized
---

# LeanExe

[jsmorph/leanexe](https://github.com/jsmorph/leanexe) at commit [9de80c54](https://github.com/jsmorph/leanexe/tree/9de80c54a4c00359afb41d79aecb71b6a37fd672), 2026-11-18.

> LeanExe compiles functions written in a restricted dialect of Lean to WebAssembly, C, AArch64 machine code, WGSL, PTX, and Thumb-2 machine code for the STM32F767ZI microcontroller, an Arm Cortex-M7, on ST's NUCLEO-F767ZI development board, and proves in Lean that the compiled code computes those functions.

*Quoted from [README.md](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/README.md), Apache-2.0.*

## Depends on

- [Array](../../../data-structures/list-like-structures/array.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Regular expression](../../../logic-and-computation/formal-languages/regular-expression.md)
- [Inverse hyperbolic trigonometric functions](../../special-functions/inverse-hyperbolic-trigonometric-functions.md)
- [Eigenvector](../../../linear-algebra/structure-theory-of-endomorphisms/eigenvector.md)
- [Inverse trigonometric functions](../../special-functions/inverse-trigonometric-functions.md)
- [Hyperbolic trigonometric functions](../../special-functions/hyperbolic-trigonometric-functions.md)
- [Trigonometric functions](../../special-functions/trigonometric-functions.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Angle](../../../geometry/affine-and-euclidean-geometry/angle.md)

## Main results

Its Lean names are 8 of the 120 theorems its README names in code:

- [`Demos.Gpt.Exact.steps_exact`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Gpt/Exact.lean#L902) (theorem)
- [`Demos.Gpt.Causal.forward_causal`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Gpt/Causal.lean#L551) (theorem)
- [`Demos.Euler.Verified.euler_solve_call`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Euler/VerifiedCall.lean#L292) (theorem)
- [`Demos.Drone.Verified.drone_compute`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Drone/Verified.lean#L36) (theorem)
- [`Demos.Drone.Verified.drone_safe`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Drone/Verified.lean#L58) (theorem)
- [`Demos.Slew.Safety.plan_safe`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Slew/Safety.lean#L312) (theorem)
- [`Demos.Slew.Optimal.plan_optimal`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Slew/Optimal.lean#L723) (theorem)
- [`Demos.Conjunction.pc_enclosure`](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/Demos/Conjunction/Soundness.lean#L750) (theorem)

Of the files its headlines import, directly or not, `Demos/Slew/Optimal.lean`, `Verified/Reflect/Definitions.lean` hold `sorry` or `admit`.

## Project

- Lean v4.34.0-rc2, Mathlib at [85e3a25e](https://github.com/leanprover-community/mathlib4/tree/85e3a25e006c35636f0e53b0e9296caca2685bc0).
- 3,832 .lean files; its Lean libraries `LeanExe`, `Examples`, `Library`, `Demos`, `TestSupport`, `Verified` hold 3,694, declaring 44,644 names, with `sorry` in 3 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/jsmorph/leanexe/blob/9de80c54a4c00359afb41d79aecb71b6a37fd672/LICENSE)).

## Builds on

- Mathlib, at [85e3a25e](https://github.com/leanprover-community/mathlib4/tree/85e3a25e006c35636f0e53b0e9296caca2685bc0).
- `CodeLib` (https://github.com/jsmorph/talos) at `87e3aa5e`.
- `Verifier`.

## Placement

Of its imports of Mathlib modules in an overview area, 132 of 277 are in Analysis, 1.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (132 of 277 imports, 1.8×), Data structures (40 of 277 imports, 1.0×), General algebra (65 of 277 imports, 0.7×). *Proof depends on* lists 8 of the 56 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [jsmorph/leanexe at 9de80c54](https://github.com/jsmorph/leanexe/tree/9de80c54a4c00359afb41d79aecb71b6a37fd672)
