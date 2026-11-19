---
declaration: theorem
origin: cited
lean: CompStark.Stark.completeness, CompStark.Batch.completeness, CompStark.Iop.Setup.completeness, CompStark.Iop.Batch.Setup.completeness, CompStark.Iop.knowledgeSoundness, CompStark.Iop.batchKnowledgeSoundness, CompStark.Iop.Statement.stateRestoration_le, CompStark.Iop.Batch.Statement.stateRestoration_le
statement: formalized
proof: formalized
---

# CompStark

[zksecurity/CompStark](https://github.com/zksecurity/CompStark) at commit [085fe9ce](https://github.com/zksecurity/CompStark/tree/085fe9ce25b588cf13936f3646d24e961c7b5707), 2026-11-13.

> Fast, formally verified STARK provers and verifiers in Lean 4. CompStark implements Plonky3's STARK and batch STARK, proves them complete and knowledge-sound with concrete security bounds, and runs them at speeds comparable to Plonky3.

*Quoted from [README.md](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/README.md), Apache-2.0.*

## Depends on

- [Array](../../list-like-structures/array.md)
- [List](../../list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Proof depends on

- [Lagrange interpolation](../../../../undergraduate/numerical-analysis/approximation-of-numerical-functions/lagrange-interpolation.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Roots of a polynomial](../../../general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [Tree](../../trees/tree.md)
- [Polynomial functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Frobenius morphism](../../../general-algebra/field-theory/frobenius-morphism.md)
- [Polynomial in one indeterminate](../../../general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Multiset](../../sets/multiset.md)

## Main results

Its Lean names are 8 of the 18 theorems its README names in code:

- [`CompStark.Stark.completeness`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Complete/Stark.lean#L690) (theorem)
- [`CompStark.Batch.completeness`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Complete/Batch.lean#L1708) (theorem)
- [`CompStark.Iop.Setup.completeness`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Iop/StarkCompleteness.lean#L324) (theorem)
- [`CompStark.Iop.Batch.Setup.completeness`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Iop/BatchCompleteness.lean#L697) (theorem)
- [`CompStark.Iop.knowledgeSoundness`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Iop/StarkSoundness.lean#L51) (theorem)
- [`CompStark.Iop.batchKnowledgeSoundness`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Iop/BatchSoundness.lean#L89) (theorem)
- [`CompStark.Iop.Statement.stateRestoration_le`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Iop/StarkStateRestoration.lean#L235) (theorem)
- [`CompStark.Iop.Batch.Statement.stateRestoration_le`](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/CompStark/Iop/BatchStateRestoration.lean#L227) (theorem)

No file its headlines import, directly or not (140 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 601 .lean files; its Lean libraries `CompStark`, `CompStarkPackedNative`, `CompStarkTests`, `CompStarkFixtures` hold 598, declaring 10,893 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/zksecurity/CompStark/blob/085fe9ce25b588cf13936f3646d24e961c7b5707/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `Arklib` (https://github.com/mitschabaude-bot/ArkLib.git) at `93fd4833`.
- `CompPoly` (https://github.com/mitschabaude-bot/CompPoly.git) at `14330de8`.
- `VCVio` (https://github.com/mitschabaude-bot/VCVio.git) at `dd5a3aee`.

## Placement

2 of the 3 Mathlib concepts its headline statements name are in Data structures.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (19 of 68 imports, 2.0×), Linear algebra (7 of 68 imports, 1.8×), General algebra (41 of 68 imports, 1.7×). *Proof depends on* lists 8 of the 31 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [zksecurity/CompStark at 085fe9ce](https://github.com/zksecurity/CompStark/tree/085fe9ce25b588cf13936f3646d24e961c7b5707)
