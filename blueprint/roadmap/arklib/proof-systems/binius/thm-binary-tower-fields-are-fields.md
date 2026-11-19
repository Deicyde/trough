---
declaration: theorem
origin: cited
lean: BinaryTower.BTFieldIsField, BinaryTower.BTFieldCard, BinaryTower.BTFieldChar2
statement: formalized
---

# Binary Tower Fields are fields

We prove that the binary tower fields are finite fields:

- The ground field $\mathcal{T}_{0} := \mathbb{F}_2$ is a field. For all $\iota > 0$, $\mathcal{T}_{\iota}$ is the quotient ring of $\mathcal{T}_{\iota-1}[X_{\iota-1}]$ by the irreducible polynomial $X_{\iota-1}^{2}+X_{\iota-2} \cdot X_{\iota-1}+1$, therefore $\mathcal{T}_{\iota}$ is a field extension of $\mathcal{T}_{\iota-1}$.
- For all $\iota \in \mathbb{N}$, the cardinality of $\mathcal{T}_{\iota}$ is $2^{2^{\iota}}$.
- For all $\iota \in \mathbb{N}$, the characteristic of $\mathcal{T}_{\iota}$ is 2.

## Depends on

- [Binary Tower Field](def-binary-tower-field.md)
- [Irreducible defining polynomial](thm-binary-tower-field-irreducible.md)

## Lean

Stated as [`BinaryTower.BTFieldIsField`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BinaryTower.BTFieldIsField), [`BinaryTower.BTFieldCard`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BinaryTower.BTFieldCard), [`BinaryTower.BTFieldChar2`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BinaryTower.BTFieldChar2); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/binius.tex, line 27](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/binius.tex#L27)
