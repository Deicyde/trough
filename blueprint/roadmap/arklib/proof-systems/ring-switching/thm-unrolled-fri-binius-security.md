---
declaration: theorem
origin: cited
lean: Binius.FRIBinius.Unrolled.fullVerifier_rbrKnowledgeSoundness, Binius.FRIBinius.Unrolled.fullReduction_perfectCompleteness_and_knowledgeSoundness, Binius.FRIBinius.Unrolled.fullError_sum_le_concrete, Binius.FRIBinius.Unrolled.concreteError_add_eq
statement: formalized
---

# Security of unrolled FRI-Binius

In the concrete setup above, the unrolled verifier is round-by-round knowledge sound for the relaxed input relation of Theorem [Binius with Binary Basefold](thm-binius-ring-switching-soundness.md), and the unrolled reduction is perfectly complete for exact encodings. Its challenge-index error sum, and hence its knowledge-soundness error, is at most

$$
\frac{\kappa + 2\ell'}{\lvert L\rvert} + \frac{2^{\ell'+R}}{\lvert L\rvert}
+ \left(\frac12 + \frac{1}{2\cdot 2^R}\right)^{\gamma},
$$

which is equation (43) of ([Diamond and Posen 2024](https://eprint.iacr.org/archive/2024/504/20250922:164810)). This is the bound of Theorem [Knowledge soundness](thm-ring-switching-knowledge-soundness.md) minus $2\ell'/\lvert L\rvert$: the unrolled protocol runs one sum-check where the separate composition runs two.

## Depends on

- [Unrolled FRI-Binius](def-unrolled-fri-binius.md)
- [Knowledge soundness](thm-ring-switching-knowledge-soundness.md)
- [RBR Knowledge Soundness Implies Knowledge Soundness](../../oracle-reductions/definitions/part-02/thm-rbr-knowledge-soundness-implies-knowledge-so.md)

## Lean

Stated as [`Binius.FRIBinius.Unrolled.fullVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.Unrolled.fullVerifier_rbrKnowledgeSoundness), [`Binius.FRIBinius.Unrolled.fullReduction_perfectCompleteness_and_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.Unrolled.fullReduction_perfectCompleteness_and_knowledgeSoundness), [`Binius.FRIBinius.Unrolled.fullError_sum_le_concrete`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.Unrolled.fullError_sum_le_concrete), [`Binius.FRIBinius.Unrolled.concreteError_add_eq`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.Unrolled.concreteError_add_eq); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 301](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/ring_switching.tex#L301)
