---
declaration: definition
origin: cited
lean: BinaryTower.BTField
statement: formalized
---

# Binary Tower Field

A binary tower field $\mathcal{T}_{\iota}$ for $\iota \in \mathbb{N}$ is defined inductively as the $\iota$-th field in the sequence of quadratic extensions over the ground field $\mathbb{F}_2$.

- $\mathcal{T}_{0} := \mathbb{F}_{2}$
- $\forall \iota > 0$, $\mathcal{T}_{\iota} := \mathcal{T}_{\iota-1}[X_{\iota-1}] / (X_{\iota-1}^{2}+X_{\iota-2} \cdot X_{\iota-1}+1)$, where we conventionally set $X_{-1} := 1$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`BinaryTower.BTField`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BinaryTower.BTField).

## Sources

- [ArkLib blueprint: proof_systems/binius.tex, line 9](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/binius.tex#L9)
