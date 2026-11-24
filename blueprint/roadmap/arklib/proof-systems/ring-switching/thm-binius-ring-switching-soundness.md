---
declaration: theorem
origin: cited
lean: Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness_and_rbrKnowledgeSoundness, Binius.FRIBinius.RingSwitch.fullError_sum_le
statement: formalized
---

# Binius with Binary Basefold

In the concrete setup above, the full Binius verifier is round-by-round knowledge sound for its relaxed, unique-decoding-radius input relation. Decoder functionality discharges commitment binding. Its challenge-index error sum is bounded by

$$
\frac{\kappa}{\lvert L\rvert} + \frac{2\ell'}{\lvert L\rvert}
+ \varepsilon_{\mathrm{BBF}},
$$

where $\varepsilon_{\mathrm{BBF}}$ is the concrete Binary Basefold opening's closed-form upper bound. Exact codeword encodings give the separate completeness relation in Theorem [Perfect completeness](thm-ring-switching-completeness.md).

## Depends on

- [Full Binius ring-switching reduction](def-full-ring-switching.md)
- [Closing a contextual opening](thm-ring-switching-soundness.md)

## Lean

Stated as [`Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness_and_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.RingSwitch.fullReduction_perfectCompleteness_and_rbrKnowledgeSoundness), [`Binius.FRIBinius.RingSwitch.fullError_sum_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Binius.FRIBinius.RingSwitch.fullError_sum_le); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 252](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/ring_switching.tex#L252)
