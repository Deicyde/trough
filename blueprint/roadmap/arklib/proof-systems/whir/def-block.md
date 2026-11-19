---
declaration: definition
origin: cited
lean: Domain.CosetFftDomainClass.block
statement: formalized
---

# block

Let $\mathcal{L} \subseteq \mathbb{F}$ be a smooth evaluation domain and $k \in \mathbb{N}$ be a folding parameter. For $0\le i\le k$ and $z \in \mathcal{L}^{2^k}$, define $\mathrm{Block}(\mathcal{L}, i, k, z) := \{ y \in \mathcal{L}^{2^i} : y^{2^{k-i}} = z \}$. The formalization takes the domain $\mathcal{L}^{2^i}$ and the exponent $k-i$ as its arguments.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Domain.CosetFftDomainClass.block`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Domain.CosetFftDomainClass.block).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 254](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L254)
