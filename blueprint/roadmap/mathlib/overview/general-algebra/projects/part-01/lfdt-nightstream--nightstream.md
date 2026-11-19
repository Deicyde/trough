---
declaration: theorem
origin: cited
lean: NightstreamFPrime.Lifecycle.BoundedDepth.stepHolds_iff, NightstreamFPrime.Layout.BoundedDepth.StepCircuits.soundness, NightstreamFPrime.Layout.BoundedDepth.LightAssemblerCompleteness.complete, NightstreamFPrime.Layout.BoundedDepth.RefreshAssemblerCompleteness.complete
statement: formalized
proof: formalized
---

# Nightstream

[LFDT-Nightstream/Nightstream](https://github.com/LFDT-Nightstream/Nightstream) at commit [b4e170d4](https://github.com/LFDT-Nightstream/Nightstream/tree/b4e170d48ff19d421a9a55db4ffa3789c3ff5503), 2026-11-18.

> Nightstream is a research proving system that combines SuperNeo folding for CCS with HyperNova-style recursion. The active field is the prime field of `2^64 − 59` with a degree-two extension. Ajtai commitments bind witnesses, and the transcripts of the folding scheme and of the step circuits use Poseidon2 only. The Akita commitment scheme (ePrint 2026/1983) compresses the final proof. Akita uses Keccak-family hashes for its own challenges.

*Quoted from [README.md](https://github.com/LFDT-Nightstream/Nightstream/blob/b4e170d48ff19d421a9a55db4ffa3789c3ff5503/README.md), Apache-2.0.*

## Depends on

- [Natural number](../../numbers/natural-number.md)

## Proof depends on

- [Fermat's little theorem](../../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
- [List](../../../data-structures/list-like-structures/list.md)
- [Discrete law](../../../probability-theory/random-variables-and-their-laws/discrete-law.md)
- [Multiset](../../../data-structures/sets/multiset.md)
- [Rupture field](../../field-theory/rupture-field.md)
- [Characteristic p](../../field-theory/characteristic-p.md)
- [Field](../../field-theory/field.md)
- [Array](../../../data-structures/list-like-structures/array.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`NightstreamFPrime.Lifecycle.BoundedDepth.stepHolds_iff`](https://github.com/LFDT-Nightstream/Nightstream/blob/b4e170d48ff19d421a9a55db4ffa3789c3ff5503/formal/nightstream-fprime/NightstreamFPrime/Lifecycle/BoundedDepth/Step.lean#L235) (theorem)
- [`NightstreamFPrime.Layout.BoundedDepth.StepCircuits.soundness`](https://github.com/LFDT-Nightstream/Nightstream/blob/b4e170d48ff19d421a9a55db4ffa3789c3ff5503/formal/nightstream-fprime/NightstreamFPrime/Layout/BoundedDepth/StepCircuits.lean#L78) (theorem)
- [`NightstreamFPrime.Layout.BoundedDepth.LightAssemblerCompleteness.complete`](https://github.com/LFDT-Nightstream/Nightstream/blob/b4e170d48ff19d421a9a55db4ffa3789c3ff5503/formal/nightstream-fprime/NightstreamFPrime/Layout/BoundedDepth/LightAssemblerCompleteness.lean#L190) (theorem)
- [`NightstreamFPrime.Layout.BoundedDepth.RefreshAssemblerCompleteness.complete`](https://github.com/LFDT-Nightstream/Nightstream/blob/b4e170d48ff19d421a9a55db4ffa3789c3ff5503/formal/nightstream-fprime/NightstreamFPrime/Layout/BoundedDepth/RefreshAssemblerCompleteness.lean#L471) (theorem)

No file its headlines import, directly or not (318 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 1,007 .lean files; its Lean libraries `NightstreamFPrime`, `NightstreamFPrimeTests` hold 1,007, declaring 16,892 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/LFDT-Nightstream/Nightstream/blob/b4e170d48ff19d421a9a55db4ffa3789c3ff5503/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `CompPoly` (https://github.com/Verified-zkEVM/CompPoly) at `06686e4c`.

## Placement

Of its imports of Mathlib modules in an overview area, 99 of 156 are in General algebra, 1.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (99 of 156 imports, 1.8×), Data structures (34 of 156 imports, 1.5×). *Proof depends on* lists 8 of the 24 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [LFDT-Nightstream/Nightstream at b4e170d4](https://github.com/LFDT-Nightstream/Nightstream/tree/b4e170d48ff19d421a9a55db4ffa3789c3ff5503)
