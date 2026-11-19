---
declaration: theorem
origin: cited
lean: RingSwitching.Packing.ProductSumcheck.rbrKnowledgeSoundness, RingSwitching.Packing.TensorPrefix.rbrKnowledgeSoundness, RingSwitching.Packing.TensorPrefix.rbrError_sum
statement: formalized
---

# Round-by-round knowledge soundness of the prefix protocol

Suppose $L$ is a finite commutative ring with no zero divisors and every oracle statement is compatible with at most one packed polynomial. The product sum-check, and the DP24 prefix head followed by it, are round-by-round knowledge sound at every fixed transcript prefix. The prefix protocol's challenge-index error sum is exactly

$$
\frac{\kappa}{\lvert L\rvert} + \frac{2\ell'}{\lvert L\rvert}.
$$

The head contributes one batching challenge; each sum-check challenge contributes $2/\lvert L\rvert$. The terminal message has no challenge and contributes no challenge error. The check holds for every multiplier value, including zero.

## Depends on

- [Ring-switching profile](def-ring-switching-profile.md)
- [Multilinear packing](def-pack-mle.md)
- [Round-by-Round Knowledge Soundness under a Guarded First Verifier](../../oracle-reductions/composition-of-oracle-reductions/part-01/thm-rbr-knowledge-soundness-append-guarded.md)
- [Round-by-Round Knowledge Soundness of a Guarded Chain](../../oracle-reductions/composition-of-oracle-reductions/part-01/thm-rbr-knowledge-soundness-compose-guarded.md)

## Lean

Stated as [`RingSwitching.Packing.ProductSumcheck.rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.ProductSumcheck.rbrKnowledgeSoundness), [`RingSwitching.Packing.TensorPrefix.rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.TensorPrefix.rbrKnowledgeSoundness), [`RingSwitching.Packing.TensorPrefix.rbrError_sum`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.TensorPrefix.rbrError_sum); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 193](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L193)
