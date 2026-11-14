---
declaration: theorem
origin: cited
lean: Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness, RingSwitching.Packing.RingSwitch.append_perfectCompleteness
statement: formalized
---

# Perfect completeness

The full Binius reduction is perfectly complete for its input relation with an exact first codeword encoding. The honest folded element passes the column check, its target is the round-zero sum, and the matrix terminal check produces the correct opening of the same packed polynomial. The Binary Basefold opening is complete on that strict relation. More generally, the shared reduction can be closed by a guarded opening already typed at its contextual evaluation endpoint, provided that opening is perfectly complete on that relation for every fixed initial oracle state.

## Depends on

- [Full Binius ring-switching reduction](def-full-ring-switching.md)

## Lean

Stated as [`Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness), [`RingSwitching.Packing.RingSwitch.append_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.RingSwitch.append_perfectCompleteness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 178](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L178)
