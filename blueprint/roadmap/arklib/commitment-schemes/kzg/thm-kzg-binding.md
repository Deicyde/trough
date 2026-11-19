---
declaration: theorem
origin: cited
lean: KZG.CommitmentScheme.bindingReduction, KZG.CommitmentScheme.binding_reduces_to_tSdh, KZG.CommitmentScheme.binding
statement: formalized
---

# KZG evaluation binding

Assume $g_1\neq 1$ and $e(g_1,g_2)\neq 1_{G_T}$. A binding adversary outputs a commitment, a point $z$, two values $v_1,v_2$ and two prover states, and then runs the opening prover from each state. It wins when $v_1\neq v_2$ and both openings are accepted. Uniform queries are forwarded to private sampling, from an empty cache. For every binding adversary $\mathcal{B}$, the probability that $\mathcal{B}$ wins is at most the probability that the explicit reduction $R(\mathcal{B})$ wins the $t$-SDH game. Consequently, if the $t$-SDH assumption holds over $\mathcal{A}$ with error $\varepsilon$ and $R(\mathcal{B})\in\mathcal{A}$, then $\mathcal{B}$ wins with probability at most $\varepsilon$.

## Depends on

- [KZG commitment scheme](def-kzg.md)
- [$t$-SDH](def-tsdh.md)

## Lean

Stated as [`KZG.CommitmentScheme.bindingReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.CommitmentScheme.bindingReduction), [`KZG.CommitmentScheme.binding_reduces_to_tSdh`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.CommitmentScheme.binding_reduces_to_tSdh), [`KZG.CommitmentScheme.binding`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/KZG.CommitmentScheme.binding); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: commitments/kzg.tex, line 55](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/commitments/kzg.tex#L55)
