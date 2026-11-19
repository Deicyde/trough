---
declaration: theorem
origin: cited
lean: Specs.mp_reduce_2k_setup, Tom.InvmodPost.spec_neg_odd, Specs.mp_read_radix, Specs.mp_dr_reduce, Specs.mp_gcd, Specs.mp_init_copy, Specs.mp_mul
statement: formalized
proof: formalized
---

# verified-libtommath

[BasisResearch/verified-libtommath](https://github.com/BasisResearch/verified-libtommath) at commit [cfc232aa](https://github.com/BasisResearch/verified-libtommath/tree/cfc232aa5e5cc22d690efeb9a03d065eb531a16c), 2026-10-31.

> Lean 4 proofs that [libtommath](https://github.com/libtom/libtommath) v1.3.0, compiled for bare-metal RV64I (`c/tommath-arith.elf`: xPack GCC 15.2.0, `-O2`, 28-bit digits), is correct: all 100 functions of the image (76 libtommath functions and the 24 newlib/libgcc routines they call: the allocator, `memset`/`memcpy`/`memmove`, 64-bit multiply and divide) meet specifications over Lean's `Int`/`Nat`, as total-correctness triples on the Sail RISC-V model.

*Quoted from [README.md](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/README.md), Apache-2.0.*

## Depends on

- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Language](../../../mathlib/overview/logic-and-computation/formal-languages/language.md)
- [Ring](../../../mathlib/overview/general-algebra/rings/ring.md)
- [Closure](../../../mathlib/overview/topology/general-topology/part-01/closure.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Specs.mp_reduce_2k_setup`](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/Tom/Machine/Specs/Reduce2kSetup.lean#L22) (theorem)
- [`Tom.InvmodPost.spec_neg_odd`](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/Tom/Spec/Gcd.lean#L982) (theorem)
- [`Specs.mp_read_radix`](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/Tom/Machine/Specs/ReadRadix.lean#L19) (theorem)
- [`Specs.mp_dr_reduce`](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/Tom/Machine/Specs/DrReduce.lean#L22) (theorem)
- [`Specs.mp_gcd`](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/Tom/Machine/Specs/Gcd.lean#L21) (theorem)
- [`Specs.mp_init_copy`](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/Tom/Machine/Specs/Init.lean#L42) (theorem)
- [`Specs.mp_mul`](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/Tom/Machine/Specs/Mul.lean#L19) (theorem)

No file its headlines import, directly or not (1029 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0.
- 1,667 .lean files; its Lean libraries `Vsa`, `VsaIris`, `TomSpec`, `Tom` hold 1,532, declaring 31,244 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/BasisResearch/verified-libtommath/blob/cfc232aa5e5cc22d690efeb9a03d065eb531a16c/LICENSE)).

## Builds on

- `iris` (https://github.com/leanprover-community/iris-lean) at `740e2c4a`.
- `«lean-riscv»`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* names 4 of the 7 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [BasisResearch/verified-libtommath at cfc232aa](https://github.com/BasisResearch/verified-libtommath/tree/cfc232aa5e5cc22d690efeb9a03d065eb531a16c)
