---
declaration: definition
origin: cited
lean: Binius.FRIBinius.Unrolled.fullReduction
statement: formalized
---

# Unrolled FRI-Binius

In the concrete setup above, the unrolled protocol of ([Diamond and Posen 2024](https://eprint.iacr.org/archive/2024/504/20250922:164810)) (Construction 5.1), for $K = \mathbb{F}_2$, is the DP24 tensor batching head followed by the Binary Basefold opening of the head's product claim $s_0 = \sum_{y \in \{0,1\}^{\ell'}} \mathcal{M}(y)\, t'(y)$, where $\mathcal{M}$ is the ring-switching multiplier and $t'$ the packed polynomial. The Binary Basefold sum-check is the ring-switching sum-check, so no separate sum-check runs before the opening.

## Depends on

- [Full Binius ring-switching reduction](def-full-ring-switching.md)

## Lean

Formalized as [`Binius.FRIBinius.Unrolled.fullReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.Unrolled.fullReduction).

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 170](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/ring_switching.tex#L170)
