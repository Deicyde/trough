---
declaration: definition
origin: cited
lean: BlockRelDistance.blockRelDistanceBall
statement: formalized
---

# list_close_codewords_block

For the smooth Reed Solomon code $\mathcal{C}^{(i)}$, proximity parameter $\delta \in [0,1]$, and $f : \mathcal{L}^{2^i} \to \mathbb{F}$, we let

$$
\Lambda_{r}(\mathcal{C}^{(i)}, i, k, f, \delta) := \{ u \in \mathcal{C}^{(i)} \mid \Delta_{r}(\mathcal{C}^{(i)}, i, k, f, u) \leq \delta \},
$$

denote the list of codewords in $\mathcal{C}^{(i)}$ within relative block distance at most $\delta$ from $f$.

## Depends on

- [block_rel_distance](def-block-rel-distance.md)

## Lean

Formalized as [`BlockRelDistance.blockRelDistanceBall`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BlockRelDistance.blockRelDistanceBall).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 284](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L284)
