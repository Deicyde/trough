---
declaration: definition
origin: cited
lean: KZG.CommitmentScheme.kzg, KZG.commit, KZG.generateOpening, KZG.verifyOpening
statement: formalized
---

# KZG commitment scheme

- **Key generation.** Sample a uniform nonzero $\tau\in\mathbb{Z}_p$. Both keys are the reference string $\bigl((g_1^{\tau^i})_{i\leq n},(g_2,g_2^{\tau})\bigr)$.
- **Commitment.** $C=\prod_{i\leq n}(g_1^{\tau^i})^{a_i}=g_1^{f(\tau)}$.
- **Opening.** To open at $z$ with value $v$, the prover sends one element $\pi\in G_1$, the commitment to the quotient $(f(X)-f(z))/(X-z)$.
- **Verification.** Accept when $e(C\cdot g_1^{-v},g_2)=e(\pi,g_2^{\tau}\cdot g_2^{-z})$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`KZG.CommitmentScheme.kzg`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.CommitmentScheme.kzg), [`KZG.commit`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.commit), [`KZG.generateOpening`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.generateOpening), [`KZG.verifyOpening`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.verifyOpening).

## Sources

- [ArkLib blueprint: commitments/kzg.tex, line 14](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/kzg.tex#L14)
