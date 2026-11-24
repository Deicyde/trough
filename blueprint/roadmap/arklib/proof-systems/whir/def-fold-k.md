---
declaration: definition
origin: cited
lean: ProximityGap.iteratedFoldWord
statement: formalized
---

# fold_k

For $k \leq m$ and $\vec{\alpha} = (\alpha_0, \ldots, \alpha_{k-1}) \in \mathbb{F}^k$ we define $\mathrm{Fold}(f, \vec{\alpha}) : \mathcal{L}^{2^k} \to \mathbb{F}$ to equal $\mathrm{Fold}(f, \vec{\alpha}) := f_k$ where $f_k$ is defined recursively as follows: $f_0 := f$, and $f_{i+1} := \mathrm{Fold_f}(f_{i}, \alpha_i)$.

## Depends on

- [foldf](def-foldf.md)

## Lean

Formalized as [`ProximityGap.iteratedFoldWord`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.iteratedFoldWord).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 232](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/whir.tex#L232)
