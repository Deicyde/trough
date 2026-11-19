---
declaration: lemma
origin: cited
lean: BlockRelDistance.relHammingDist_le_blockRelDistance, BlockRelDistance.listBlock_subset_listHamming
statement: formalized
---

# block_rel_distance

For $i\le k$ and $f, g : \mathcal{L}^{2^i} \to \mathbb{F}$, we have that $\Delta(f, g) \leq \Delta_{r}(\mathcal{C}^{(i)}, i, k, f, g)$. Consequently, $\Lambda_{r}(\mathcal{C}^{(i)}, i, k, f, \delta) \subseteq \Lambda(\mathcal{C}^{(i)}, f, \delta)$ for $\delta\in[0,1]$.

## Depends on

- [block_rel_distance](def-block-rel-distance.md)
- [Distance from a Code](../../supporting-theories/coding-theory/def-distance-from-code.md)
- [list_close_codewords_block](def-list-close-codewords-block.md)
- [List of Close Codewords](../../supporting-theories/coding-theory/def-list-close-codewords.md)

## Lean

Stated as [`BlockRelDistance.relHammingDist_le_blockRelDistance`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BlockRelDistance.relHammingDist_le_blockRelDistance), [`BlockRelDistance.listBlock_subset_listHamming`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BlockRelDistance.listBlock_subset_listHamming); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 295](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L295)
