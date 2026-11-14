---
navigation: transparent
---

# Simulator to State-Restoration Knowledge…

### Zero-Knowledge

- [Simulator](def-simulator.md)

**Remark (Zero-Knowledge Definition).** *Honest-verifier* zero-knowledge asks for a simulator whose transcripts, on every valid input, are (statistically) indistinguishable from those of the interaction between the honest prover and the honest verifier. Full zero-knowledge asks the same against every (malicious) verifier. Neither definition is formalized.

### Oracle-Specific Security

For oracle reductions, the security definitions are analogous to those for standard reductions, but adapted to work with oracle interfaces:

- [Oracle Reduction Completeness](def-oracle-reduction-completeness.md)
- [Oracle Verifier Soundness](def-oracle-verifier-soundness.md)
- [Oracle Verifier Knowledge Soundness](def-oracle-verifier-knowledge-soundness.md)
- [Oracle Verifier RBR Soundness](def-oracle-verifier-rbr-soundness.md)
- [Oracle Verifier RBR Knowledge Soundness](def-oracle-verifier-rbr-knowledge-soundness.md)

### State-Restoration Security

State-restoration security is developed in the interaction layer (`ArkLib/Interaction`), which is meant to replace the legacy oracle-reduction layer used in the rest of this chapter. It covers a fixed-round public-coin oracle protocol: $k$ rounds, in each of which the prover sends an oracle message from a finite type and the verifier replies with a uniform challenge from a finite nonempty type. In the state-restoration setting the adversary may query challenges for any transcript prefix it likes, in any order and repeatedly, before it commits to one transcript.

- [State-Restoration Experiment](def-sr-experiment.md)
- [Round-by-Round Knowledge Certificate in the Interaction Layer](def-interaction-knowledge-certificate.md)
- [State-Restoration Knowledge Soundness](thm-sr-knowledge-soundness.md)
- [State-Restoration Knowledge Soundness with Per-Round Errors](thm-sr-knowledge-soundness-nonuniform.md)

The library states state-restoration security only in this knowledge form. The bound concerns the interaction-layer verifier; its transfer to the Fiat–Shamir transform is discussed in [Security Properties](../../the-fiat-shamir-transformation/README.md). `docs/design/00-current-status.md` records the status of the interaction layer.
