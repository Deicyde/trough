---
declaration: definition
origin: cited
lean: ProtocolSpec.dir, ProtocolSpec.Type, ProtocolSpec.MessageIdx, ProtocolSpec.ChallengeIdx, ProtocolSpec.Message, ProtocolSpec.Challenge
statement: formalized
---

# Protocol Specification Components

Given a protocol spec $\mathsf{pSpec} : \mathsf{ProtocolSpec}\ n$, we define:

- $\mathsf{pSpec}.\mathsf{Dir}\ i := (\mathsf{pSpec}\ i).\mathsf{fst}$ extracts the direction of the $i$-th message.
- $\mathsf{pSpec}.\mathsf{Type}\ i := (\mathsf{pSpec}\ i).\mathsf{snd}$ extracts the type of the $i$-th message.
- $\mathsf{pSpec}.\mathsf{MessageIdx} := \{i : \mathsf{Fin}\ n \mathbin{/\!/} \mathsf{pSpec}.\mathsf{Dir}\ i = \mathsf{P \!\!\rightarrow\!\! V}\}$ is the subtype of indices corresponding to prover messages.
- $\mathsf{pSpec}.\mathsf{ChallengeIdx} := \{i : \mathsf{Fin}\ n \mathbin{/\!/} \mathsf{pSpec}.\mathsf{Dir}\ i = \mathsf{V \!\!\rightarrow\!\! P}\}$ is the subtype of indices corresponding to verifier challenges.
- $\mathsf{pSpec}.\mathsf{Message}\ i := (i : \mathsf{pSpec}.\mathsf{MessageIdx}) \to \mathsf{pSpec}.\mathsf{Type}\ i.\mathsf{val}$ is an indexed family of message types in the protocol.
- $\mathsf{pSpec}.\mathsf{Challenge}\ i := (i : \mathsf{pSpec}.\mathsf{ChallengeIdx}) \to \mathsf{pSpec}.\mathsf{Type}\ i.\mathsf{val}$ is an indexed family of challenge types in the protocol.

## Depends on

- [Protocol Specification](def-protocol-spec.md)

## Lean

Formalized as [`ProtocolSpec.dir`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.dir), [`ProtocolSpec.Type`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.Type), [`ProtocolSpec.MessageIdx`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.MessageIdx), [`ProtocolSpec.ChallengeIdx`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.ChallengeIdx), [`ProtocolSpec.Message`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.Message), [`ProtocolSpec.Challenge`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.Challenge).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 118](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L118)
