---
declaration: definition
origin: cited
lean: BlockRelDistance.blockRelDistance
statement: formalized
---

# block_rel_distance

Let $\mathcal{C}^{(i)}$ be as above and let $f, g : \mathcal{L}^{2^i} \to \mathbb{F}$. We define the $(i,k)$-wise block relative distance as

$$
\Delta_{r}(\mathcal{C}^{(i)}, i, k, f, g) = \frac{ \left| \left\{ z \in \mathcal{L}^{2^k} : \exists y \in \mathrm{Block}(\mathcal{L}, i, k, z), f(y) \neq g(y) \right\} \right| }{ |\mathcal{L}^{2^k}| }
$$

## Depends on

- [block](def-block.md)

## Lean

Formalized as [`BlockRelDistance.blockRelDistance`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BlockRelDistance.blockRelDistance).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 265](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L265)
