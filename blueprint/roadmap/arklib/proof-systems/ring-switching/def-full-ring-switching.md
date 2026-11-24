---
declaration: definition
origin: cited
lean: Binius.FRIBinius.RingSwitch.fullReduction
statement: formalized
---

# Full Binius ring-switching reduction

In the concrete setup above, compose the shared DP24 prefix protocol with the Binary Basefold opening. The composition runs a ring-switching sum-check before the opening and ends in an accept/reject statement, rather than an unclosed evaluation claim. The unrolled protocol of Definition [Unrolled FRI-Binius](def-unrolled-fri-binius.md) instead runs a single sum-check.

## Depends on

- [Ring-switching profile](def-ring-switching-profile.md)
- [Multilinear packing](def-pack-mle.md)

## Lean

Formalized as [`Binius.FRIBinius.RingSwitch.fullReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.RingSwitch.fullReduction).

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 159](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/ring_switching.tex#L159)
