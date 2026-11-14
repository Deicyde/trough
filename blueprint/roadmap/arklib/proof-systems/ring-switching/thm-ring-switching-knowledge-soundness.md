---
declaration: theorem
origin: cited
lean: RingSwitching.Packing.RingSwitch.knowledgeSoundness, RingSwitching.Packing.TensorPrefix.knowledgeSoundness, Binius.FRIBinius.RingSwitch.verifier_knowledgeSoundness, Binius.FRIBinius.RingSwitch.fullVerifier_knowledgeSoundness, Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness_and_knowledgeSoundness
statement: formalized
---

# Knowledge soundness

Under the hypotheses of Theorem [Closing a contextual opening](thm-ring-switching-soundness.md) on $C$, the batching rule and oracle compatibility, the shared protocol is knowledge sound, from its input relation to the contextual evaluation relation, with error $\varepsilon_{\mathrm{batch}} + 2m/\lvert C\rvert$. If oracle compatibility is functional, the DP24 prefix protocol is knowledge sound with error

$$
\frac{\kappa}{\lvert L\rvert} + \frac{2\ell'}{\lvert L\rvert},
$$

and so is the Binius frontend in the concrete setup above. The full Binius verifier is knowledge sound for its relaxed input relation with error

$$
\frac{\kappa}{\lvert L\rvert} + \frac{2\ell'}{\lvert L\rvert}
+ \varepsilon_{\mathrm{BBF}},
$$

and the full reduction is also perfectly complete for exact encodings.

## Depends on

- [Round-by-round knowledge soundness of the prefix protocol](thm-ring-switching-core-soundness.md)
- [Binius with Binary Basefold](thm-binius-ring-switching-soundness.md)
- [RBR Knowledge Soundness Implies Knowledge Soundness](../../oracle-reductions/definitions/part-02/thm-rbr-knowledge-soundness-implies-knowledge-so.md)

## Lean

Stated as [`RingSwitching.Packing.RingSwitch.knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.RingSwitch.knowledgeSoundness), [`RingSwitching.Packing.TensorPrefix.knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.Packing.TensorPrefix.knowledgeSoundness), [`Binius.FRIBinius.RingSwitch.verifier_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.RingSwitch.verifier_knowledgeSoundness), [`Binius.FRIBinius.RingSwitch.fullVerifier_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.RingSwitch.fullVerifier_knowledgeSoundness), [`Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness_and_knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness_and_knowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 261](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L261)
