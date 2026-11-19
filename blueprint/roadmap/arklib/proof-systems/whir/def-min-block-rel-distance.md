---
declaration: definition
origin: cited
lean: BlockRelDistance.blockRelDistanceFromCode
statement: formalized
---

# min_block_rel_distance

For $f : \mathcal{L}^{2^i} \to \mathbb{F}$ and $S \subseteq \mathbb{F}^{\mathcal{L}^{2^i}}$, we let $\Delta_{r}(\mathcal{C}^{(i)}, i, k, f, S) := \inf_{g \in S} \Delta_{r}(\mathcal{C}^{(i)}, i, k, f, g)$, with value $\infty$ when $S$ is empty (the infimum is taken in the extended nonnegative reals).

## Depends on

- [block_rel_distance](def-block-rel-distance.md)

## Lean

Formalized as [`BlockRelDistance.blockRelDistanceFromCode`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BlockRelDistance.blockRelDistanceFromCode).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 275](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L275)
