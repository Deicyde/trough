---
declaration: theorem
origin: cited
lean: BatchedFri.Spec.batchedFRI_soundness, BatchedFri.Spec.BatchingRound.soundness, BatchedFri.Spec.BatchingRound.round_soundness
statement: formalized
---

# Batched FRI soundness

Let $\delta,\varepsilon\geq 0$ and $\theta\in\mathbb{R}$, and assume $\mathsf{caError}(G,C_0,\delta,\delta)\leq\varepsilon$. For every initial distribution of the shared oracle state and every implementation of that oracle, the Batched FRI verifier is sound from the language of the input relation at radius $\delta$ to the language of the FRI output relation at radius $\delta$, with error

$$
\varepsilon+\sum_i\varepsilon^{\mathrm{fold}}_i+(1-\min\{\theta,\delta\})_+^{\,l},
$$

where the last two terms are the FRI soundness error of Theorem [fri-soundness](../fri-soundness/thm-fri-soundness.md). The batching round alone is round-by-round sound with error $\varepsilon$.

## Depends on

- [Batched FRI relation and reduction](def-batched-fri.md)
- [fri-soundness](../fri-soundness/thm-fri-soundness.md)

## Lean

Stated as [`BatchedFri.Spec.batchedFRI_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.batchedFRI_soundness), [`BatchedFri.Spec.BatchingRound.soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.BatchingRound.soundness), [`BatchedFri.Spec.BatchingRound.round_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.BatchingRound.round_soundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 304](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L304)
